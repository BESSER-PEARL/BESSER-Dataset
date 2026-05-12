import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HaxeDependencyDeclaration,
    haxe_HaxeUsingDeclaration,
    haxe_HaxeImportDeclaration,
    HaxeAbstractOperation,
    HaxeSingleVariableDeclaration,
    HaxeField,
    HaxeClassifier,
    haxe_HaxeEnum,
    haxe_HaxeAbstract,
    HaxeTypeAccess,
    haxe_HaxeFunctionTypeAccess,
    haxe_HaxeConstructor,
    haxe_HaxeAttribute,
    HaxeMetadataContainer,
    HaxeFieldContainer,
    HaxeType,
    haxe_HaxeTypedef,
    haxe_HaxeClassifier,
    haxe_HaxeTypeParameter,
    HaxePathReferentiable,
    HaxeVariableDeclaration,
    haxe_HaxeEnumConstructor,
    haxe_HaxeVariableDeclarationFragment,
    HaxePathReference,
    haxe_HaxeClassifierAccess,
    HaxeMethodInvocation,
    haxe_HaxeSuperConstructorInvocation,
    HaxeAbstractMethodInvocation,
    HaxeTypedElement,
    haxe_HaxeVariableDeclarationGroup,
    haxe_HaxeOperation,
    HaxeAbstractFunction,
    haxe_HaxeAbstractOperation,
    HaxeConstant,
    haxe_HaxeRegexLiteral,
    haxe_HaxeIdentifierLiteral,
    haxe_HaxeNullLiteral,
    haxe_HaxeBooleanLiteral,
    haxe_HaxeNumberLiteral,
    haxe_HaxeStringLiteral,
    HaxeExpressionStatement,
    haxe_HaxeThrowExpression,
    haxe_HaxeReturn,
    HaxeBinaryExpression,
    haxe_HaxeAssignment,
    haxe_HaxeInfixExpression,
    HaxeUnaryExpression,
    haxe_HaxePostfixExpression,
    haxe_HaxePrefixExpression,
    haxe_HaxeSingleVariableDeclaration,
    HaxeLoopStatement,
    haxe_HaxeDoWhileStatement,
    haxe_HaxeWhileStatement,
    haxe_HaxeForStatement,
    HaxeConditionalExpression,
    haxe_HaxeTernaryExpression,
    haxe_HaxeIfStatement,
    HaxeExpression,
    haxe_HaxeParenthizedExpression,
    haxe_HaxeCatchClause,
    haxe_HaxeFieldAccess,
    haxe_HaxeBlock,
    haxe_HaxeTypeCheckExpression,
    haxe_HaxeCallExpression,
    haxe_HaxePackageAccess,
    haxe_HaxeConstant,
    haxe_HaxeArrayInitializer,
    haxe_HaxeInExpression,
    haxe_HaxeTypeAccess,
    haxe_HaxeSingleVariableAccess,
    haxe_HaxeConditionalExpression,
    haxe_HaxeFunctionExpression,
    haxe_HaxeSwitch,
    haxe_HaxeArrayCreation,
    haxe_HaxeThisExpression,
    haxe_HaxeArrayAccess,
    haxe_HaxeExpressionStatement,
    haxe_HaxeUnsafeCastExpression,
    haxe_HaxeCase,
    haxe_HaxeBreak,
    haxe_HaxeBinaryExpression,
    haxe_HaxeUnaryExpression,
    haxe_HaxeSuperMethodInvocation,
    haxe_HaxeContinue,
    haxe_HaxeCastingExpression,
    haxe_HaxeTryExpression,
    haxe_HaxeVariableDeclarationExpression,
    haxe_HaxeMethodInvocation,
    haxe_HaxeObjectDeclaration,
    haxe_HaxeEmptyStatement,
    haxe_HaxeLoopStatement,
    haxe_HaxePackage,
    HaxeNamedElement,
    haxe_HaxeMetadata,
    haxe_HaxeVariableDeclaration,
    haxe_HaxeFieldDeclaration,
    haxe_HaxeField,
    HaxeComment,
    haxe_HaxeHaxedocComment,
    HaxeASTNode,
    haxe_HaxeDependencyDeclaration,
    haxe_HaxeTextElement,
    haxe_HaxeType,
    haxe_HaxeExpression,
    haxe_HaxeAbstractFunction,
    haxe_HaxeTagElement,
    haxe_HaxeAbstractMethodInvocation,
    haxe_HaxeNamedElement,
    haxe_HaxeComment,
    HaxeModelElement,
    haxe_HaxeFieldContainer,
    haxe_HaxePathReference,
    haxe_HaxeMetadataContainer,
    haxe_HaxeTypedElement,
    haxe_HaxeASTNode,
    haxe_HaxeModelElement,
    haxe_HaxeModule,
    haxe_HaxePathReferentiable,
    haxe_HaxeClass,
    haxe_HaxeModel,
    HaxeAssignmentOperator,
    HaxeAttributeProperty,
    HaxeInfixOperators,
    HaxePrefixOperators,
    HaxeTarget,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_haxedependencydeclaration_is_not_abstract():
    assert not inspect.isabstract(HaxeDependencyDeclaration)


def test_haxedependencydeclaration_constructor_exists():
    assert callable(HaxeDependencyDeclaration.__init__)


def test_haxedependencydeclaration_constructor_args():
    sig = inspect.signature(HaxeDependencyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeusingdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeUsingDeclaration)


def test_haxe_haxeusingdeclaration_constructor_exists():
    assert callable(haxe_HaxeUsingDeclaration.__init__)


def test_haxe_haxeusingdeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeUsingDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeImportDeclaration)


def test_haxe_haxeimportdeclaration_constructor_exists():
    assert callable(haxe_HaxeImportDeclaration.__init__)


def test_haxe_haxeimportdeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxeabstractoperation_is_not_abstract():
    assert not inspect.isabstract(HaxeAbstractOperation)


def test_haxeabstractoperation_constructor_exists():
    assert callable(HaxeAbstractOperation.__init__)


def test_haxeabstractoperation_constructor_args():
    sig = inspect.signature(HaxeAbstractOperation.__init__)
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



def test_haxe_haxeenum_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeEnum)


def test_haxe_haxeenum_constructor_exists():
    assert callable(haxe_HaxeEnum.__init__)


def test_haxe_haxeenum_constructor_args():
    sig = inspect.signature(haxe_HaxeEnum.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeabstract_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAbstract)


def test_haxe_haxeabstract_constructor_exists():
    assert callable(haxe_HaxeAbstract.__init__)


def test_haxe_haxeabstract_constructor_args():
    sig = inspect.signature(haxe_HaxeAbstract.__init__)
    params = list(sig.parameters.keys())



def test_haxetypeaccess_is_not_abstract():
    assert not inspect.isabstract(HaxeTypeAccess)


def test_haxetypeaccess_constructor_exists():
    assert callable(HaxeTypeAccess.__init__)


def test_haxetypeaccess_constructor_args():
    sig = inspect.signature(HaxeTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefunctiontypeaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeFunctionTypeAccess)


def test_haxe_haxefunctiontypeaccess_constructor_exists():
    assert callable(haxe_HaxeFunctionTypeAccess.__init__)


def test_haxe_haxefunctiontypeaccess_constructor_args():
    sig = inspect.signature(haxe_HaxeFunctionTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeconstructor_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeConstructor)


def test_haxe_haxeconstructor_constructor_exists():
    assert callable(haxe_HaxeConstructor.__init__)


def test_haxe_haxeconstructor_constructor_args():
    sig = inspect.signature(haxe_HaxeConstructor.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeattribute_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAttribute)


def test_haxe_haxeattribute_constructor_exists():
    assert callable(haxe_HaxeAttribute.__init__)


def test_haxe_haxeattribute_constructor_args():
    sig = inspect.signature(haxe_HaxeAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "setterProperty" in params, "Missing parameter 'setterProperty'"
    assert "getterProperty" in params, "Missing parameter 'getterProperty'"

def test_haxe_haxeattribute_has_setterProperty():
    assert hasattr(haxe_HaxeAttribute, "setterProperty")
    descriptor = None
    for klass in haxe_HaxeAttribute.__mro__:
        if "setterProperty" in klass.__dict__:
            descriptor = klass.__dict__["setterProperty"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxeattribute_has_getterProperty():
    assert hasattr(haxe_HaxeAttribute, "getterProperty")
    descriptor = None
    for klass in haxe_HaxeAttribute.__mro__:
        if "getterProperty" in klass.__dict__:
            descriptor = klass.__dict__["getterProperty"]
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



def test_haxe_haxetypedef_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTypedef)


def test_haxe_haxetypedef_constructor_exists():
    assert callable(haxe_HaxeTypedef.__init__)


def test_haxe_haxetypedef_constructor_args():
    sig = inspect.signature(haxe_HaxeTypedef.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeclassifier_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeClassifier)


def test_haxe_haxeclassifier_constructor_exists():
    assert callable(haxe_HaxeClassifier.__init__)


def test_haxe_haxeclassifier_constructor_args():
    sig = inspect.signature(haxe_HaxeClassifier.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetypeparameter_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTypeParameter)


def test_haxe_haxetypeparameter_constructor_exists():
    assert callable(haxe_HaxeTypeParameter.__init__)


def test_haxe_haxetypeparameter_constructor_args():
    sig = inspect.signature(haxe_HaxeTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_haxepathreferentiable_is_not_abstract():
    assert not inspect.isabstract(HaxePathReferentiable)


def test_haxepathreferentiable_constructor_exists():
    assert callable(HaxePathReferentiable.__init__)


def test_haxepathreferentiable_constructor_args():
    sig = inspect.signature(HaxePathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_haxevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(HaxeVariableDeclaration)


def test_haxevariabledeclaration_constructor_exists():
    assert callable(HaxeVariableDeclaration.__init__)


def test_haxevariabledeclaration_constructor_args():
    sig = inspect.signature(HaxeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeenumconstructor_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeEnumConstructor)


def test_haxe_haxeenumconstructor_constructor_exists():
    assert callable(haxe_HaxeEnumConstructor.__init__)


def test_haxe_haxeenumconstructor_constructor_args():
    sig = inspect.signature(haxe_HaxeEnumConstructor.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxevariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeVariableDeclarationFragment)


def test_haxe_haxevariabledeclarationfragment_constructor_exists():
    assert callable(haxe_HaxeVariableDeclarationFragment.__init__)


def test_haxe_haxevariabledeclarationfragment_constructor_args():
    sig = inspect.signature(haxe_HaxeVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_haxepathreference_is_not_abstract():
    assert not inspect.isabstract(HaxePathReference)


def test_haxepathreference_constructor_exists():
    assert callable(HaxePathReference.__init__)


def test_haxepathreference_constructor_args():
    sig = inspect.signature(HaxePathReference.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeclassifieraccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeClassifierAccess)


def test_haxe_haxeclassifieraccess_constructor_exists():
    assert callable(haxe_HaxeClassifierAccess.__init__)


def test_haxe_haxeclassifieraccess_constructor_args():
    sig = inspect.signature(haxe_HaxeClassifierAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(HaxeMethodInvocation)


def test_haxemethodinvocation_constructor_exists():
    assert callable(HaxeMethodInvocation.__init__)


def test_haxemethodinvocation_constructor_args():
    sig = inspect.signature(HaxeMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxesuperconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeSuperConstructorInvocation)


def test_haxe_haxesuperconstructorinvocation_constructor_exists():
    assert callable(haxe_HaxeSuperConstructorInvocation.__init__)


def test_haxe_haxesuperconstructorinvocation_constructor_args():
    sig = inspect.signature(haxe_HaxeSuperConstructorInvocation.__init__)
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



def test_haxe_haxevariabledeclarationgroup_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeVariableDeclarationGroup)


def test_haxe_haxevariabledeclarationgroup_constructor_exists():
    assert callable(haxe_HaxeVariableDeclarationGroup.__init__)


def test_haxe_haxevariabledeclarationgroup_constructor_args():
    sig = inspect.signature(haxe_HaxeVariableDeclarationGroup.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeoperation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeOperation)


def test_haxe_haxeoperation_constructor_exists():
    assert callable(haxe_HaxeOperation.__init__)


def test_haxe_haxeoperation_constructor_args():
    sig = inspect.signature(haxe_HaxeOperation.__init__)
    params = list(sig.parameters.keys())
    assert "macro" in params, "Missing parameter 'macro'"

def test_haxe_haxeoperation_has_macro():
    assert hasattr(haxe_HaxeOperation, "macro")
    descriptor = None
    for klass in haxe_HaxeOperation.__mro__:
        if "macro" in klass.__dict__:
            descriptor = klass.__dict__["macro"]
            break
    assert isinstance(descriptor, property)



def test_haxeabstractfunction_is_not_abstract():
    assert not inspect.isabstract(HaxeAbstractFunction)


def test_haxeabstractfunction_constructor_exists():
    assert callable(HaxeAbstractFunction.__init__)


def test_haxeabstractfunction_constructor_args():
    sig = inspect.signature(HaxeAbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeabstractoperation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAbstractOperation)


def test_haxe_haxeabstractoperation_constructor_exists():
    assert callable(haxe_HaxeAbstractOperation.__init__)


def test_haxe_haxeabstractoperation_constructor_args():
    sig = inspect.signature(haxe_HaxeAbstractOperation.__init__)
    params = list(sig.parameters.keys())
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "overrides" in params, "Missing parameter 'overrides'"

def test_haxe_haxeabstractoperation_has_isInline():
    assert hasattr(haxe_HaxeAbstractOperation, "isInline")
    descriptor = None
    for klass in haxe_HaxeAbstractOperation.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxeabstractoperation_has_overrides():
    assert hasattr(haxe_HaxeAbstractOperation, "overrides")
    descriptor = None
    for klass in haxe_HaxeAbstractOperation.__mro__:
        if "overrides" in klass.__dict__:
            descriptor = klass.__dict__["overrides"]
            break
    assert isinstance(descriptor, property)



def test_haxeconstant_is_not_abstract():
    assert not inspect.isabstract(HaxeConstant)


def test_haxeconstant_constructor_exists():
    assert callable(HaxeConstant.__init__)


def test_haxeconstant_constructor_args():
    sig = inspect.signature(HaxeConstant.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeregexliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeRegexLiteral)


def test_haxe_haxeregexliteral_constructor_exists():
    assert callable(haxe_HaxeRegexLiteral.__init__)


def test_haxe_haxeregexliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeRegexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "options" in params, "Missing parameter 'options'"
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_haxe_haxeregexliteral_has_options():
    assert hasattr(haxe_HaxeRegexLiteral, "options")
    descriptor = None
    for klass in haxe_HaxeRegexLiteral.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxeregexliteral_has_pattern():
    assert hasattr(haxe_HaxeRegexLiteral, "pattern")
    descriptor = None
    for klass in haxe_HaxeRegexLiteral.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxeidentifierliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeIdentifierLiteral)


def test_haxe_haxeidentifierliteral_constructor_exists():
    assert callable(haxe_HaxeIdentifierLiteral.__init__)


def test_haxe_haxeidentifierliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeIdentifierLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe_haxeidentifierliteral_has_value():
    assert hasattr(haxe_HaxeIdentifierLiteral, "value")
    descriptor = None
    for klass in haxe_HaxeIdentifierLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxenullliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeNullLiteral)


def test_haxe_haxenullliteral_constructor_exists():
    assert callable(haxe_HaxeNullLiteral.__init__)


def test_haxe_haxenullliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxebooleanliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeBooleanLiteral)


def test_haxe_haxebooleanliteral_constructor_exists():
    assert callable(haxe_HaxeBooleanLiteral.__init__)


def test_haxe_haxebooleanliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe_haxebooleanliteral_has_value():
    assert hasattr(haxe_HaxeBooleanLiteral, "value")
    descriptor = None
    for klass in haxe_HaxeBooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxenumberliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeNumberLiteral)


def test_haxe_haxenumberliteral_constructor_exists():
    assert callable(haxe_HaxeNumberLiteral.__init__)


def test_haxe_haxenumberliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_haxe_haxenumberliteral_has_value():
    assert hasattr(haxe_HaxeNumberLiteral, "value")
    descriptor = None
    for klass in haxe_HaxeNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxestringliteral_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeStringLiteral)


def test_haxe_haxestringliteral_constructor_exists():
    assert callable(haxe_HaxeStringLiteral.__init__)


def test_haxe_haxestringliteral_constructor_args():
    sig = inspect.signature(haxe_HaxeStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "escapedValue" in params, "Missing parameter 'escapedValue'"

def test_haxe_haxestringliteral_has_escapedValue():
    assert hasattr(haxe_HaxeStringLiteral, "escapedValue")
    descriptor = None
    for klass in haxe_HaxeStringLiteral.__mro__:
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



def test_haxe_haxethrowexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeThrowExpression)


def test_haxe_haxethrowexpression_constructor_exists():
    assert callable(haxe_HaxeThrowExpression.__init__)


def test_haxe_haxethrowexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeThrowExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxereturn_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeReturn)


def test_haxe_haxereturn_constructor_exists():
    assert callable(haxe_HaxeReturn.__init__)


def test_haxe_haxereturn_constructor_args():
    sig = inspect.signature(haxe_HaxeReturn.__init__)
    params = list(sig.parameters.keys())



def test_haxebinaryexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeBinaryExpression)


def test_haxebinaryexpression_constructor_exists():
    assert callable(HaxeBinaryExpression.__init__)


def test_haxebinaryexpression_constructor_args():
    sig = inspect.signature(HaxeBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeassignment_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAssignment)


def test_haxe_haxeassignment_constructor_exists():
    assert callable(haxe_HaxeAssignment.__init__)


def test_haxe_haxeassignment_constructor_args():
    sig = inspect.signature(haxe_HaxeAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe_haxeassignment_has_operator():
    assert hasattr(haxe_HaxeAssignment, "operator")
    descriptor = None
    for klass in haxe_HaxeAssignment.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxeinfixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeInfixExpression)


def test_haxe_haxeinfixexpression_constructor_exists():
    assert callable(haxe_HaxeInfixExpression.__init__)


def test_haxe_haxeinfixexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeInfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe_haxeinfixexpression_has_operator():
    assert hasattr(haxe_HaxeInfixExpression, "operator")
    descriptor = None
    for klass in haxe_HaxeInfixExpression.__mro__:
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



def test_haxe_haxepostfixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePostfixExpression)


def test_haxe_haxepostfixexpression_constructor_exists():
    assert callable(haxe_HaxePostfixExpression.__init__)


def test_haxe_haxepostfixexpression_constructor_args():
    sig = inspect.signature(haxe_HaxePostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "isIncrement" in params, "Missing parameter 'isIncrement'"

def test_haxe_haxepostfixexpression_has_isIncrement():
    assert hasattr(haxe_HaxePostfixExpression, "isIncrement")
    descriptor = None
    for klass in haxe_HaxePostfixExpression.__mro__:
        if "isIncrement" in klass.__dict__:
            descriptor = klass.__dict__["isIncrement"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxeprefixexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePrefixExpression)


def test_haxe_haxeprefixexpression_constructor_exists():
    assert callable(haxe_HaxePrefixExpression.__init__)


def test_haxe_haxeprefixexpression_constructor_args():
    sig = inspect.signature(haxe_HaxePrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_haxe_haxeprefixexpression_has_operator():
    assert hasattr(haxe_HaxePrefixExpression, "operator")
    descriptor = None
    for klass in haxe_HaxePrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxesinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeSingleVariableDeclaration)


def test_haxe_haxesinglevariabledeclaration_constructor_exists():
    assert callable(haxe_HaxeSingleVariableDeclaration.__init__)


def test_haxe_haxesinglevariabledeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isOptional" in params, "Missing parameter 'isOptional'"

def test_haxe_haxesinglevariabledeclaration_has_isOptional():
    assert hasattr(haxe_HaxeSingleVariableDeclaration, "isOptional")
    descriptor = None
    for klass in haxe_HaxeSingleVariableDeclaration.__mro__:
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



def test_haxe_haxedowhilestatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeDoWhileStatement)


def test_haxe_haxedowhilestatement_constructor_exists():
    assert callable(haxe_HaxeDoWhileStatement.__init__)


def test_haxe_haxedowhilestatement_constructor_args():
    sig = inspect.signature(haxe_HaxeDoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxewhilestatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeWhileStatement)


def test_haxe_haxewhilestatement_constructor_exists():
    assert callable(haxe_HaxeWhileStatement.__init__)


def test_haxe_haxewhilestatement_constructor_args():
    sig = inspect.signature(haxe_HaxeWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeforstatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeForStatement)


def test_haxe_haxeforstatement_constructor_exists():
    assert callable(haxe_HaxeForStatement.__init__)


def test_haxe_haxeforstatement_constructor_args():
    sig = inspect.signature(haxe_HaxeForStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxeconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeConditionalExpression)


def test_haxeconditionalexpression_constructor_exists():
    assert callable(HaxeConditionalExpression.__init__)


def test_haxeconditionalexpression_constructor_args():
    sig = inspect.signature(HaxeConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeternaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTernaryExpression)


def test_haxe_haxeternaryexpression_constructor_exists():
    assert callable(haxe_HaxeTernaryExpression.__init__)


def test_haxe_haxeternaryexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeTernaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeifstatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeIfStatement)


def test_haxe_haxeifstatement_constructor_exists():
    assert callable(haxe_HaxeIfStatement.__init__)


def test_haxe_haxeifstatement_constructor_args():
    sig = inspect.signature(haxe_HaxeIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxeexpression_is_not_abstract():
    assert not inspect.isabstract(HaxeExpression)


def test_haxeexpression_constructor_exists():
    assert callable(HaxeExpression.__init__)


def test_haxeexpression_constructor_args():
    sig = inspect.signature(HaxeExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeparenthizedexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeParenthizedExpression)


def test_haxe_haxeparenthizedexpression_constructor_exists():
    assert callable(haxe_HaxeParenthizedExpression.__init__)


def test_haxe_haxeparenthizedexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeParenthizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxecatchclause_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeCatchClause)


def test_haxe_haxecatchclause_constructor_exists():
    assert callable(haxe_HaxeCatchClause.__init__)


def test_haxe_haxecatchclause_constructor_args():
    sig = inspect.signature(haxe_HaxeCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefieldaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeFieldAccess)


def test_haxe_haxefieldaccess_constructor_exists():
    assert callable(haxe_HaxeFieldAccess.__init__)


def test_haxe_haxefieldaccess_constructor_args():
    sig = inspect.signature(haxe_HaxeFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeblock_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeBlock)


def test_haxe_haxeblock_constructor_exists():
    assert callable(haxe_HaxeBlock.__init__)


def test_haxe_haxeblock_constructor_args():
    sig = inspect.signature(haxe_HaxeBlock.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetypecheckexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTypeCheckExpression)


def test_haxe_haxetypecheckexpression_constructor_exists():
    assert callable(haxe_HaxeTypeCheckExpression.__init__)


def test_haxe_haxetypecheckexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeTypeCheckExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxecallexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeCallExpression)


def test_haxe_haxecallexpression_constructor_exists():
    assert callable(haxe_HaxeCallExpression.__init__)


def test_haxe_haxecallexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeCallExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxepackageaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePackageAccess)


def test_haxe_haxepackageaccess_constructor_exists():
    assert callable(haxe_HaxePackageAccess.__init__)


def test_haxe_haxepackageaccess_constructor_args():
    sig = inspect.signature(haxe_HaxePackageAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeconstant_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeConstant)


def test_haxe_haxeconstant_constructor_exists():
    assert callable(haxe_HaxeConstant.__init__)


def test_haxe_haxeconstant_constructor_args():
    sig = inspect.signature(haxe_HaxeConstant.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxearrayinitializer_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeArrayInitializer)


def test_haxe_haxearrayinitializer_constructor_exists():
    assert callable(haxe_HaxeArrayInitializer.__init__)


def test_haxe_haxearrayinitializer_constructor_args():
    sig = inspect.signature(haxe_HaxeArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeinexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeInExpression)


def test_haxe_haxeinexpression_constructor_exists():
    assert callable(haxe_HaxeInExpression.__init__)


def test_haxe_haxeinexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeInExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetypeaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTypeAccess)


def test_haxe_haxetypeaccess_constructor_exists():
    assert callable(haxe_HaxeTypeAccess.__init__)


def test_haxe_haxetypeaccess_constructor_args():
    sig = inspect.signature(haxe_HaxeTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxesinglevariableaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeSingleVariableAccess)


def test_haxe_haxesinglevariableaccess_constructor_exists():
    assert callable(haxe_HaxeSingleVariableAccess.__init__)


def test_haxe_haxesinglevariableaccess_constructor_args():
    sig = inspect.signature(haxe_HaxeSingleVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeConditionalExpression)


def test_haxe_haxeconditionalexpression_constructor_exists():
    assert callable(haxe_HaxeConditionalExpression.__init__)


def test_haxe_haxeconditionalexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefunctionexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeFunctionExpression)


def test_haxe_haxefunctionexpression_constructor_exists():
    assert callable(haxe_HaxeFunctionExpression.__init__)


def test_haxe_haxefunctionexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeFunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeswitch_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeSwitch)


def test_haxe_haxeswitch_constructor_exists():
    assert callable(haxe_HaxeSwitch.__init__)


def test_haxe_haxeswitch_constructor_args():
    sig = inspect.signature(haxe_HaxeSwitch.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxearraycreation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeArrayCreation)


def test_haxe_haxearraycreation_constructor_exists():
    assert callable(haxe_HaxeArrayCreation.__init__)


def test_haxe_haxearraycreation_constructor_args():
    sig = inspect.signature(haxe_HaxeArrayCreation.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxethisexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeThisExpression)


def test_haxe_haxethisexpression_constructor_exists():
    assert callable(haxe_HaxeThisExpression.__init__)


def test_haxe_haxethisexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxearrayaccess_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeArrayAccess)


def test_haxe_haxearrayaccess_constructor_exists():
    assert callable(haxe_HaxeArrayAccess.__init__)


def test_haxe_haxearrayaccess_constructor_args():
    sig = inspect.signature(haxe_HaxeArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeexpressionstatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeExpressionStatement)


def test_haxe_haxeexpressionstatement_constructor_exists():
    assert callable(haxe_HaxeExpressionStatement.__init__)


def test_haxe_haxeexpressionstatement_constructor_args():
    sig = inspect.signature(haxe_HaxeExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeunsafecastexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeUnsafeCastExpression)


def test_haxe_haxeunsafecastexpression_constructor_exists():
    assert callable(haxe_HaxeUnsafeCastExpression.__init__)


def test_haxe_haxeunsafecastexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeUnsafeCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxecase_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeCase)


def test_haxe_haxecase_constructor_exists():
    assert callable(haxe_HaxeCase.__init__)


def test_haxe_haxecase_constructor_args():
    sig = inspect.signature(haxe_HaxeCase.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxebreak_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeBreak)


def test_haxe_haxebreak_constructor_exists():
    assert callable(haxe_HaxeBreak.__init__)


def test_haxe_haxebreak_constructor_args():
    sig = inspect.signature(haxe_HaxeBreak.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxebinaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeBinaryExpression)


def test_haxe_haxebinaryexpression_constructor_exists():
    assert callable(haxe_HaxeBinaryExpression.__init__)


def test_haxe_haxebinaryexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeunaryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeUnaryExpression)


def test_haxe_haxeunaryexpression_constructor_exists():
    assert callable(haxe_HaxeUnaryExpression.__init__)


def test_haxe_haxeunaryexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxesupermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeSuperMethodInvocation)


def test_haxe_haxesupermethodinvocation_constructor_exists():
    assert callable(haxe_HaxeSuperMethodInvocation.__init__)


def test_haxe_haxesupermethodinvocation_constructor_args():
    sig = inspect.signature(haxe_HaxeSuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxecontinue_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeContinue)


def test_haxe_haxecontinue_constructor_exists():
    assert callable(haxe_HaxeContinue.__init__)


def test_haxe_haxecontinue_constructor_args():
    sig = inspect.signature(haxe_HaxeContinue.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxecastingexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeCastingExpression)


def test_haxe_haxecastingexpression_constructor_exists():
    assert callable(haxe_HaxeCastingExpression.__init__)


def test_haxe_haxecastingexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeCastingExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetryexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTryExpression)


def test_haxe_haxetryexpression_constructor_exists():
    assert callable(haxe_HaxeTryExpression.__init__)


def test_haxe_haxetryexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeTryExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxevariabledeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeVariableDeclarationExpression)


def test_haxe_haxevariabledeclarationexpression_constructor_exists():
    assert callable(haxe_HaxeVariableDeclarationExpression.__init__)


def test_haxe_haxevariabledeclarationexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeVariableDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxemethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeMethodInvocation)


def test_haxe_haxemethodinvocation_constructor_exists():
    assert callable(haxe_HaxeMethodInvocation.__init__)


def test_haxe_haxemethodinvocation_constructor_args():
    sig = inspect.signature(haxe_HaxeMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeobjectdeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeObjectDeclaration)


def test_haxe_haxeobjectdeclaration_constructor_exists():
    assert callable(haxe_HaxeObjectDeclaration.__init__)


def test_haxe_haxeobjectdeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeObjectDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeemptystatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeEmptyStatement)


def test_haxe_haxeemptystatement_constructor_exists():
    assert callable(haxe_HaxeEmptyStatement.__init__)


def test_haxe_haxeemptystatement_constructor_args():
    sig = inspect.signature(haxe_HaxeEmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeloopstatement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeLoopStatement)


def test_haxe_haxeloopstatement_constructor_exists():
    assert callable(haxe_HaxeLoopStatement.__init__)


def test_haxe_haxeloopstatement_constructor_args():
    sig = inspect.signature(haxe_HaxeLoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxepackage_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePackage)


def test_haxe_haxepackage_constructor_exists():
    assert callable(haxe_HaxePackage.__init__)


def test_haxe_haxepackage_constructor_args():
    sig = inspect.signature(haxe_HaxePackage.__init__)
    params = list(sig.parameters.keys())



def test_haxenamedelement_is_not_abstract():
    assert not inspect.isabstract(HaxeNamedElement)


def test_haxenamedelement_constructor_exists():
    assert callable(HaxeNamedElement.__init__)


def test_haxenamedelement_constructor_args():
    sig = inspect.signature(HaxeNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxemetadata_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeMetadata)


def test_haxe_haxemetadata_constructor_exists():
    assert callable(haxe_HaxeMetadata.__init__)


def test_haxe_haxemetadata_constructor_args():
    sig = inspect.signature(haxe_HaxeMetadata.__init__)
    params = list(sig.parameters.keys())
    assert "compilerMetadata" in params, "Missing parameter 'compilerMetadata'"

def test_haxe_haxemetadata_has_compilerMetadata():
    assert hasattr(haxe_HaxeMetadata, "compilerMetadata")
    descriptor = None
    for klass in haxe_HaxeMetadata.__mro__:
        if "compilerMetadata" in klass.__dict__:
            descriptor = klass.__dict__["compilerMetadata"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeVariableDeclaration)


def test_haxe_haxevariabledeclaration_constructor_exists():
    assert callable(haxe_HaxeVariableDeclaration.__init__)


def test_haxe_haxevariabledeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefielddeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeFieldDeclaration)


def test_haxe_haxefielddeclaration_constructor_exists():
    assert callable(haxe_HaxeFieldDeclaration.__init__)


def test_haxe_haxefielddeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefield_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeField)


def test_haxe_haxefield_constructor_exists():
    assert callable(haxe_HaxeField.__init__)


def test_haxe_haxefield_constructor_args():
    sig = inspect.signature(haxe_HaxeField.__init__)
    params = list(sig.parameters.keys())
    assert "isPrivate" in params, "Missing parameter 'isPrivate'"
    assert "isStatic" in params, "Missing parameter 'isStatic'"

def test_haxe_haxefield_has_isPrivate():
    assert hasattr(haxe_HaxeField, "isPrivate")
    descriptor = None
    for klass in haxe_HaxeField.__mro__:
        if "isPrivate" in klass.__dict__:
            descriptor = klass.__dict__["isPrivate"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxefield_has_isStatic():
    assert hasattr(haxe_HaxeField, "isStatic")
    descriptor = None
    for klass in haxe_HaxeField.__mro__:
        if "isStatic" in klass.__dict__:
            descriptor = klass.__dict__["isStatic"]
            break
    assert isinstance(descriptor, property)



def test_haxecomment_is_not_abstract():
    assert not inspect.isabstract(HaxeComment)


def test_haxecomment_constructor_exists():
    assert callable(HaxeComment.__init__)


def test_haxecomment_constructor_args():
    sig = inspect.signature(HaxeComment.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxehaxedoccomment_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeHaxedocComment)


def test_haxe_haxehaxedoccomment_constructor_exists():
    assert callable(haxe_HaxeHaxedocComment.__init__)


def test_haxe_haxehaxedoccomment_constructor_args():
    sig = inspect.signature(haxe_HaxeHaxedocComment.__init__)
    params = list(sig.parameters.keys())



def test_haxeastnode_is_not_abstract():
    assert not inspect.isabstract(HaxeASTNode)


def test_haxeastnode_constructor_exists():
    assert callable(HaxeASTNode.__init__)


def test_haxeastnode_constructor_args():
    sig = inspect.signature(HaxeASTNode.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxedependencydeclaration_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeDependencyDeclaration)


def test_haxe_haxedependencydeclaration_constructor_exists():
    assert callable(haxe_HaxeDependencyDeclaration.__init__)


def test_haxe_haxedependencydeclaration_constructor_args():
    sig = inspect.signature(haxe_HaxeDependencyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetextelement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTextElement)


def test_haxe_haxetextelement_constructor_exists():
    assert callable(haxe_HaxeTextElement.__init__)


def test_haxe_haxetextelement_constructor_args():
    sig = inspect.signature(haxe_HaxeTextElement.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_haxe_haxetextelement_has_text():
    assert hasattr(haxe_HaxeTextElement, "text")
    descriptor = None
    for klass in haxe_HaxeTextElement.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxetype_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeType)


def test_haxe_haxetype_constructor_exists():
    assert callable(haxe_HaxeType.__init__)


def test_haxe_haxetype_constructor_args():
    sig = inspect.signature(haxe_HaxeType.__init__)
    params = list(sig.parameters.keys())
    assert "extern" in params, "Missing parameter 'extern'"
    assert "private" in params, "Missing parameter 'private'"

def test_haxe_haxetype_has_extern():
    assert hasattr(haxe_HaxeType, "extern")
    descriptor = None
    for klass in haxe_HaxeType.__mro__:
        if "extern" in klass.__dict__:
            descriptor = klass.__dict__["extern"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxetype_has_private():
    assert hasattr(haxe_HaxeType, "private")
    descriptor = None
    for klass in haxe_HaxeType.__mro__:
        if "private" in klass.__dict__:
            descriptor = klass.__dict__["private"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxeexpression_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeExpression)


def test_haxe_haxeexpression_constructor_exists():
    assert callable(haxe_HaxeExpression.__init__)


def test_haxe_haxeexpression_constructor_args():
    sig = inspect.signature(haxe_HaxeExpression.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeabstractfunction_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAbstractFunction)


def test_haxe_haxeabstractfunction_constructor_exists():
    assert callable(haxe_HaxeAbstractFunction.__init__)


def test_haxe_haxeabstractfunction_constructor_args():
    sig = inspect.signature(haxe_HaxeAbstractFunction.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetagelement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTagElement)


def test_haxe_haxetagelement_constructor_exists():
    assert callable(haxe_HaxeTagElement.__init__)


def test_haxe_haxetagelement_constructor_args():
    sig = inspect.signature(haxe_HaxeTagElement.__init__)
    params = list(sig.parameters.keys())
    assert "tagName" in params, "Missing parameter 'tagName'"

def test_haxe_haxetagelement_has_tagName():
    assert hasattr(haxe_HaxeTagElement, "tagName")
    descriptor = None
    for klass in haxe_HaxeTagElement.__mro__:
        if "tagName" in klass.__dict__:
            descriptor = klass.__dict__["tagName"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxeabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeAbstractMethodInvocation)


def test_haxe_haxeabstractmethodinvocation_constructor_exists():
    assert callable(haxe_HaxeAbstractMethodInvocation.__init__)


def test_haxe_haxeabstractmethodinvocation_constructor_args():
    sig = inspect.signature(haxe_HaxeAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxenamedelement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeNamedElement)


def test_haxe_haxenamedelement_constructor_exists():
    assert callable(haxe_HaxeNamedElement.__init__)


def test_haxe_haxenamedelement_constructor_args():
    sig = inspect.signature(haxe_HaxeNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_haxe_haxenamedelement_has_name():
    assert hasattr(haxe_HaxeNamedElement, "name")
    descriptor = None
    for klass in haxe_HaxeNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxecomment_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeComment)


def test_haxe_haxecomment_constructor_exists():
    assert callable(haxe_HaxeComment.__init__)


def test_haxe_haxecomment_constructor_args():
    sig = inspect.signature(haxe_HaxeComment.__init__)
    params = list(sig.parameters.keys())
    assert "enclosedByParent" in params, "Missing parameter 'enclosedByParent'"
    assert "prefixOfParent" in params, "Missing parameter 'prefixOfParent'"
    assert "content" in params, "Missing parameter 'content'"
    assert "lineComment" in params, "Missing parameter 'lineComment'"

def test_haxe_haxecomment_has_enclosedByParent():
    assert hasattr(haxe_HaxeComment, "enclosedByParent")
    descriptor = None
    for klass in haxe_HaxeComment.__mro__:
        if "enclosedByParent" in klass.__dict__:
            descriptor = klass.__dict__["enclosedByParent"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxecomment_has_prefixOfParent():
    assert hasattr(haxe_HaxeComment, "prefixOfParent")
    descriptor = None
    for klass in haxe_HaxeComment.__mro__:
        if "prefixOfParent" in klass.__dict__:
            descriptor = klass.__dict__["prefixOfParent"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxecomment_has_content():
    assert hasattr(haxe_HaxeComment, "content")
    descriptor = None
    for klass in haxe_HaxeComment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxecomment_has_lineComment():
    assert hasattr(haxe_HaxeComment, "lineComment")
    descriptor = None
    for klass in haxe_HaxeComment.__mro__:
        if "lineComment" in klass.__dict__:
            descriptor = klass.__dict__["lineComment"]
            break
    assert isinstance(descriptor, property)



def test_haxemodelelement_is_not_abstract():
    assert not inspect.isabstract(HaxeModelElement)


def test_haxemodelelement_constructor_exists():
    assert callable(HaxeModelElement.__init__)


def test_haxemodelelement_constructor_args():
    sig = inspect.signature(HaxeModelElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxefieldcontainer_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeFieldContainer)


def test_haxe_haxefieldcontainer_constructor_exists():
    assert callable(haxe_HaxeFieldContainer.__init__)


def test_haxe_haxefieldcontainer_constructor_args():
    sig = inspect.signature(haxe_HaxeFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxepathreference_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePathReference)


def test_haxe_haxepathreference_constructor_exists():
    assert callable(haxe_HaxePathReference.__init__)


def test_haxe_haxepathreference_constructor_args():
    sig = inspect.signature(haxe_HaxePathReference.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxemetadatacontainer_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeMetadataContainer)


def test_haxe_haxemetadatacontainer_constructor_exists():
    assert callable(haxe_HaxeMetadataContainer.__init__)


def test_haxe_haxemetadatacontainer_constructor_args():
    sig = inspect.signature(haxe_HaxeMetadataContainer.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxetypedelement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeTypedElement)


def test_haxe_haxetypedelement_constructor_exists():
    assert callable(haxe_HaxeTypedElement.__init__)


def test_haxe_haxetypedelement_constructor_args():
    sig = inspect.signature(haxe_HaxeTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeastnode_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeASTNode)


def test_haxe_haxeastnode_constructor_exists():
    assert callable(haxe_HaxeASTNode.__init__)


def test_haxe_haxeastnode_constructor_args():
    sig = inspect.signature(haxe_HaxeASTNode.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxemodelelement_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeModelElement)


def test_haxe_haxemodelelement_constructor_exists():
    assert callable(haxe_HaxeModelElement.__init__)


def test_haxe_haxemodelelement_constructor_args():
    sig = inspect.signature(haxe_HaxeModelElement.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxemodule_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeModule)


def test_haxe_haxemodule_constructor_exists():
    assert callable(haxe_HaxeModule.__init__)


def test_haxe_haxemodule_constructor_args():
    sig = inspect.signature(haxe_HaxeModule.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxepathreferentiable_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxePathReferentiable)


def test_haxe_haxepathreferentiable_constructor_exists():
    assert callable(haxe_HaxePathReferentiable.__init__)


def test_haxe_haxepathreferentiable_constructor_args():
    sig = inspect.signature(haxe_HaxePathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_haxe_haxeclass_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeClass)


def test_haxe_haxeclass_constructor_exists():
    assert callable(haxe_HaxeClass.__init__)


def test_haxe_haxeclass_constructor_args():
    sig = inspect.signature(haxe_HaxeClass.__init__)
    params = list(sig.parameters.keys())
    assert "isInterface" in params, "Missing parameter 'isInterface'"

def test_haxe_haxeclass_has_isInterface():
    assert hasattr(haxe_HaxeClass, "isInterface")
    descriptor = None
    for klass in haxe_HaxeClass.__mro__:
        if "isInterface" in klass.__dict__:
            descriptor = klass.__dict__["isInterface"]
            break
    assert isinstance(descriptor, property)



def test_haxe_haxemodel_is_not_abstract():
    assert not inspect.isabstract(haxe_HaxeModel)


def test_haxe_haxemodel_constructor_exists():
    assert callable(haxe_HaxeModel.__init__)


def test_haxe_haxemodel_constructor_args():
    sig = inspect.signature(haxe_HaxeModel.__init__)
    params = list(sig.parameters.keys())
    assert "sourceFolder" in params, "Missing parameter 'sourceFolder'"
    assert "target" in params, "Missing parameter 'target'"
    assert "name" in params, "Missing parameter 'name'"
    assert "targetFolder" in params, "Missing parameter 'targetFolder'"

def test_haxe_haxemodel_has_sourceFolder():
    assert hasattr(haxe_HaxeModel, "sourceFolder")
    descriptor = None
    for klass in haxe_HaxeModel.__mro__:
        if "sourceFolder" in klass.__dict__:
            descriptor = klass.__dict__["sourceFolder"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxemodel_has_target():
    assert hasattr(haxe_HaxeModel, "target")
    descriptor = None
    for klass in haxe_HaxeModel.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxemodel_has_name():
    assert hasattr(haxe_HaxeModel, "name")
    descriptor = None
    for klass in haxe_HaxeModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_haxe_haxemodel_has_targetFolder():
    assert hasattr(haxe_HaxeModel, "targetFolder")
    descriptor = None
    for klass in haxe_HaxeModel.__mro__:
        if "targetFolder" in klass.__dict__:
            descriptor = klass.__dict__["targetFolder"]
            break
    assert isinstance(descriptor, property)

def test_haxeassignmentoperator_exists():
    # Check that the Enumeration exists
    assert HaxeAssignmentOperator is not None

def test_haxeassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeAssignmentOperator]
    expected_literals = [
        "BITWISE_OR_ASSIGN",
        "MINUS_ASSIGN",
        "SHIFT_LEFT_ASSIGN",
        "BITWISE_AND_ASSIGN",
        "ASSIGN",
        "DIVISION_ASSIGN",
        "TIMES_ASSIGN",
        "PLUS_ASSIGN",
        "XOR_ASSIGN",
        "SHIFT_RIGTH_ASSIGN",
        "SHIFT_ARITH_ASSIGN",
        "REMAINDER_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeAssignmentOperator"

def test_haxeattributeproperty_exists():
    # Check that the Enumeration exists
    assert HaxeAttributeProperty is not None

def test_haxeattributeproperty_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeAttributeProperty]
    expected_literals = [
        "null",
        "default",
        "dynamic",
        "method",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeAttributeProperty"

def test_haxeinfixoperators_exists():
    # Check that the Enumeration exists
    assert HaxeInfixOperators is not None

def test_haxeinfixoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeInfixOperators]
    expected_literals = [
        "OR",
        "BITWISE_AND",
        "RANGE",
        "SHIFT_ARITH",
        "MINUS",
        "XOR",
        "DIVISION",
        "LESS_EQUALS",
        "SHIFT_RIGTH",
        "SHIFT_LEFT",
        "TIMES",
        "BITWISE_OR",
        "REMAINDER",
        "LESS_THAN",
        "PLUS",
        "NEQ",
        "GREATER_EQUALS",
        "EQ",
        "GREATER_THAN",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeInfixOperators"

def test_haxeprefixoperators_exists():
    # Check that the Enumeration exists
    assert HaxePrefixOperators is not None

def test_haxeprefixoperators_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxePrefixOperators]
    expected_literals = [
        "DECREMENT",
        "ONECOMPLEMENT",
        "PLUS",
        "INCREMENT",
        "MINUS",
        "NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxePrefixOperators"

def test_haxetarget_exists():
    # Check that the Enumeration exists
    assert HaxeTarget is not None

def test_haxetarget_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HaxeTarget]
    expected_literals = [
        "cs",
        "flash",
        "neko",
        "java",
        "cpp",
        "js",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HaxeTarget"


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
HaxeDependencyDeclaration_strategy = st.builds(
    HaxeDependencyDeclaration,
)
haxe_HaxeUsingDeclaration_strategy = st.builds(
    haxe_HaxeUsingDeclaration,
)
haxe_HaxeImportDeclaration_strategy = st.builds(
    haxe_HaxeImportDeclaration,
)
HaxeAbstractOperation_strategy = st.builds(
    HaxeAbstractOperation,
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
haxe_HaxeEnum_strategy = st.builds(
    haxe_HaxeEnum,
)
haxe_HaxeAbstract_strategy = st.builds(
    haxe_HaxeAbstract,
)
HaxeTypeAccess_strategy = st.builds(
    HaxeTypeAccess,
)
haxe_HaxeFunctionTypeAccess_strategy = st.builds(
    haxe_HaxeFunctionTypeAccess,
)
haxe_HaxeConstructor_strategy = st.builds(
    haxe_HaxeConstructor,
)
haxe_HaxeAttribute_strategy = st.builds(
    haxe_HaxeAttribute,
    setterProperty=
        safe_text,
    getterProperty=
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
haxe_HaxeTypedef_strategy = st.builds(
    haxe_HaxeTypedef,
)
haxe_HaxeClassifier_strategy = st.builds(
    haxe_HaxeClassifier,
)
haxe_HaxeTypeParameter_strategy = st.builds(
    haxe_HaxeTypeParameter,
)
HaxePathReferentiable_strategy = st.builds(
    HaxePathReferentiable,
)
HaxeVariableDeclaration_strategy = st.builds(
    HaxeVariableDeclaration,
)
haxe_HaxeEnumConstructor_strategy = st.builds(
    haxe_HaxeEnumConstructor,
)
haxe_HaxeVariableDeclarationFragment_strategy = st.builds(
    haxe_HaxeVariableDeclarationFragment,
)
HaxePathReference_strategy = st.builds(
    HaxePathReference,
)
haxe_HaxeClassifierAccess_strategy = st.builds(
    haxe_HaxeClassifierAccess,
)
HaxeMethodInvocation_strategy = st.builds(
    HaxeMethodInvocation,
)
haxe_HaxeSuperConstructorInvocation_strategy = st.builds(
    haxe_HaxeSuperConstructorInvocation,
)
HaxeAbstractMethodInvocation_strategy = st.builds(
    HaxeAbstractMethodInvocation,
)
HaxeTypedElement_strategy = st.builds(
    HaxeTypedElement,
)
haxe_HaxeVariableDeclarationGroup_strategy = st.builds(
    haxe_HaxeVariableDeclarationGroup,
)
haxe_HaxeOperation_strategy = st.builds(
    haxe_HaxeOperation,
    macro=
        st.booleans()
)
HaxeAbstractFunction_strategy = st.builds(
    HaxeAbstractFunction,
)
haxe_HaxeAbstractOperation_strategy = st.builds(
    haxe_HaxeAbstractOperation,
    isInline=
        st.booleans(),
    overrides=
        st.booleans()
)
HaxeConstant_strategy = st.builds(
    HaxeConstant,
)
haxe_HaxeRegexLiteral_strategy = st.builds(
    haxe_HaxeRegexLiteral,
    options=
        safe_text,
    pattern=
        safe_text
)
haxe_HaxeIdentifierLiteral_strategy = st.builds(
    haxe_HaxeIdentifierLiteral,
    value=
        safe_text
)
haxe_HaxeNullLiteral_strategy = st.builds(
    haxe_HaxeNullLiteral,
)
haxe_HaxeBooleanLiteral_strategy = st.builds(
    haxe_HaxeBooleanLiteral,
    value=
        st.booleans()
)
haxe_HaxeNumberLiteral_strategy = st.builds(
    haxe_HaxeNumberLiteral,
    value=
        safe_text
)
haxe_HaxeStringLiteral_strategy = st.builds(
    haxe_HaxeStringLiteral,
    escapedValue=
        safe_text
)
HaxeExpressionStatement_strategy = st.builds(
    HaxeExpressionStatement,
)
haxe_HaxeThrowExpression_strategy = st.builds(
    haxe_HaxeThrowExpression,
)
haxe_HaxeReturn_strategy = st.builds(
    haxe_HaxeReturn,
)
HaxeBinaryExpression_strategy = st.builds(
    HaxeBinaryExpression,
)
haxe_HaxeAssignment_strategy = st.builds(
    haxe_HaxeAssignment,
    operator=
        safe_text
)
haxe_HaxeInfixExpression_strategy = st.builds(
    haxe_HaxeInfixExpression,
    operator=
        safe_text
)
HaxeUnaryExpression_strategy = st.builds(
    HaxeUnaryExpression,
)
haxe_HaxePostfixExpression_strategy = st.builds(
    haxe_HaxePostfixExpression,
    isIncrement=
        st.booleans()
)
haxe_HaxePrefixExpression_strategy = st.builds(
    haxe_HaxePrefixExpression,
    operator=
        safe_text
)
haxe_HaxeSingleVariableDeclaration_strategy = st.builds(
    haxe_HaxeSingleVariableDeclaration,
    isOptional=
        st.booleans()
)
HaxeLoopStatement_strategy = st.builds(
    HaxeLoopStatement,
)
haxe_HaxeDoWhileStatement_strategy = st.builds(
    haxe_HaxeDoWhileStatement,
)
haxe_HaxeWhileStatement_strategy = st.builds(
    haxe_HaxeWhileStatement,
)
haxe_HaxeForStatement_strategy = st.builds(
    haxe_HaxeForStatement,
)
HaxeConditionalExpression_strategy = st.builds(
    HaxeConditionalExpression,
)
haxe_HaxeTernaryExpression_strategy = st.builds(
    haxe_HaxeTernaryExpression,
)
haxe_HaxeIfStatement_strategy = st.builds(
    haxe_HaxeIfStatement,
)
HaxeExpression_strategy = st.builds(
    HaxeExpression,
)
haxe_HaxeParenthizedExpression_strategy = st.builds(
    haxe_HaxeParenthizedExpression,
)
haxe_HaxeCatchClause_strategy = st.builds(
    haxe_HaxeCatchClause,
)
haxe_HaxeFieldAccess_strategy = st.builds(
    haxe_HaxeFieldAccess,
)
haxe_HaxeBlock_strategy = st.builds(
    haxe_HaxeBlock,
)
haxe_HaxeTypeCheckExpression_strategy = st.builds(
    haxe_HaxeTypeCheckExpression,
)
haxe_HaxeCallExpression_strategy = st.builds(
    haxe_HaxeCallExpression,
)
haxe_HaxePackageAccess_strategy = st.builds(
    haxe_HaxePackageAccess,
)
haxe_HaxeConstant_strategy = st.builds(
    haxe_HaxeConstant,
)
haxe_HaxeArrayInitializer_strategy = st.builds(
    haxe_HaxeArrayInitializer,
)
haxe_HaxeInExpression_strategy = st.builds(
    haxe_HaxeInExpression,
)
haxe_HaxeTypeAccess_strategy = st.builds(
    haxe_HaxeTypeAccess,
)
haxe_HaxeSingleVariableAccess_strategy = st.builds(
    haxe_HaxeSingleVariableAccess,
)
haxe_HaxeConditionalExpression_strategy = st.builds(
    haxe_HaxeConditionalExpression,
)
haxe_HaxeFunctionExpression_strategy = st.builds(
    haxe_HaxeFunctionExpression,
)
haxe_HaxeSwitch_strategy = st.builds(
    haxe_HaxeSwitch,
)
haxe_HaxeArrayCreation_strategy = st.builds(
    haxe_HaxeArrayCreation,
)
haxe_HaxeThisExpression_strategy = st.builds(
    haxe_HaxeThisExpression,
)
haxe_HaxeArrayAccess_strategy = st.builds(
    haxe_HaxeArrayAccess,
)
haxe_HaxeExpressionStatement_strategy = st.builds(
    haxe_HaxeExpressionStatement,
)
haxe_HaxeUnsafeCastExpression_strategy = st.builds(
    haxe_HaxeUnsafeCastExpression,
)
haxe_HaxeCase_strategy = st.builds(
    haxe_HaxeCase,
)
haxe_HaxeBreak_strategy = st.builds(
    haxe_HaxeBreak,
)
haxe_HaxeBinaryExpression_strategy = st.builds(
    haxe_HaxeBinaryExpression,
)
haxe_HaxeUnaryExpression_strategy = st.builds(
    haxe_HaxeUnaryExpression,
)
haxe_HaxeSuperMethodInvocation_strategy = st.builds(
    haxe_HaxeSuperMethodInvocation,
)
haxe_HaxeContinue_strategy = st.builds(
    haxe_HaxeContinue,
)
haxe_HaxeCastingExpression_strategy = st.builds(
    haxe_HaxeCastingExpression,
)
haxe_HaxeTryExpression_strategy = st.builds(
    haxe_HaxeTryExpression,
)
haxe_HaxeVariableDeclarationExpression_strategy = st.builds(
    haxe_HaxeVariableDeclarationExpression,
)
haxe_HaxeMethodInvocation_strategy = st.builds(
    haxe_HaxeMethodInvocation,
)
haxe_HaxeObjectDeclaration_strategy = st.builds(
    haxe_HaxeObjectDeclaration,
)
haxe_HaxeEmptyStatement_strategy = st.builds(
    haxe_HaxeEmptyStatement,
)
haxe_HaxeLoopStatement_strategy = st.builds(
    haxe_HaxeLoopStatement,
)
haxe_HaxePackage_strategy = st.builds(
    haxe_HaxePackage,
)
HaxeNamedElement_strategy = st.builds(
    HaxeNamedElement,
)
haxe_HaxeMetadata_strategy = st.builds(
    haxe_HaxeMetadata,
    compilerMetadata=
        st.booleans()
)
haxe_HaxeVariableDeclaration_strategy = st.builds(
    haxe_HaxeVariableDeclaration,
)
haxe_HaxeFieldDeclaration_strategy = st.builds(
    haxe_HaxeFieldDeclaration,
)
haxe_HaxeField_strategy = st.builds(
    haxe_HaxeField,
    isPrivate=
        st.booleans(),
    isStatic=
        st.booleans()
)
HaxeComment_strategy = st.builds(
    HaxeComment,
)
haxe_HaxeHaxedocComment_strategy = st.builds(
    haxe_HaxeHaxedocComment,
)
HaxeASTNode_strategy = st.builds(
    HaxeASTNode,
)
haxe_HaxeDependencyDeclaration_strategy = st.builds(
    haxe_HaxeDependencyDeclaration,
)
haxe_HaxeTextElement_strategy = st.builds(
    haxe_HaxeTextElement,
    text=
        safe_text
)
haxe_HaxeType_strategy = st.builds(
    haxe_HaxeType,
    extern=
        st.booleans(),
    private=
        st.booleans()
)
haxe_HaxeExpression_strategy = st.builds(
    haxe_HaxeExpression,
)
haxe_HaxeAbstractFunction_strategy = st.builds(
    haxe_HaxeAbstractFunction,
)
haxe_HaxeTagElement_strategy = st.builds(
    haxe_HaxeTagElement,
    tagName=
        safe_text
)
haxe_HaxeAbstractMethodInvocation_strategy = st.builds(
    haxe_HaxeAbstractMethodInvocation,
)
haxe_HaxeNamedElement_strategy = st.builds(
    haxe_HaxeNamedElement,
    name=
        safe_text
)
haxe_HaxeComment_strategy = st.builds(
    haxe_HaxeComment,
    enclosedByParent=
        st.booleans(),
    prefixOfParent=
        st.booleans(),
    content=
        safe_text,
    lineComment=
        st.booleans()
)
HaxeModelElement_strategy = st.builds(
    HaxeModelElement,
)
haxe_HaxeFieldContainer_strategy = st.builds(
    haxe_HaxeFieldContainer,
)
haxe_HaxePathReference_strategy = st.builds(
    haxe_HaxePathReference,
)
haxe_HaxeMetadataContainer_strategy = st.builds(
    haxe_HaxeMetadataContainer,
)
haxe_HaxeTypedElement_strategy = st.builds(
    haxe_HaxeTypedElement,
)
haxe_HaxeASTNode_strategy = st.builds(
    haxe_HaxeASTNode,
)
haxe_HaxeModelElement_strategy = st.builds(
    haxe_HaxeModelElement,
)
haxe_HaxeModule_strategy = st.builds(
    haxe_HaxeModule,
)
haxe_HaxePathReferentiable_strategy = st.builds(
    haxe_HaxePathReferentiable,
)
haxe_HaxeClass_strategy = st.builds(
    haxe_HaxeClass,
    isInterface=
        st.booleans()
)
haxe_HaxeModel_strategy = st.builds(
    haxe_HaxeModel,
    sourceFolder=
        safe_text,
    target=
        safe_text,
    name=
        safe_text,
    targetFolder=
        safe_text
)

@given(instance=HaxeDependencyDeclaration_strategy)
@settings(max_examples=50)
def test_haxedependencydeclaration_instantiation(instance):
    assert isinstance(instance, HaxeDependencyDeclaration)

@given(instance=haxe_HaxeUsingDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxeusingdeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeUsingDeclaration)

@given(instance=haxe_HaxeImportDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxeimportdeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeImportDeclaration)

@given(instance=HaxeAbstractOperation_strategy)
@settings(max_examples=50)
def test_haxeabstractoperation_instantiation(instance):
    assert isinstance(instance, HaxeAbstractOperation)

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

@given(instance=haxe_HaxeEnum_strategy)
@settings(max_examples=50)
def test_haxe_haxeenum_instantiation(instance):
    assert isinstance(instance, haxe_HaxeEnum)

@given(instance=haxe_HaxeAbstract_strategy)
@settings(max_examples=50)
def test_haxe_haxeabstract_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAbstract)

@given(instance=HaxeTypeAccess_strategy)
@settings(max_examples=50)
def test_haxetypeaccess_instantiation(instance):
    assert isinstance(instance, HaxeTypeAccess)

@given(instance=haxe_HaxeFunctionTypeAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxefunctiontypeaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeFunctionTypeAccess)

@given(instance=haxe_HaxeConstructor_strategy)
@settings(max_examples=50)
def test_haxe_haxeconstructor_instantiation(instance):
    assert isinstance(instance, haxe_HaxeConstructor)

@given(instance=haxe_HaxeAttribute_strategy)
@settings(max_examples=50)
def test_haxe_haxeattribute_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAttribute)



@given(instance=haxe_HaxeAttribute_strategy)
def test_haxe_haxeattribute_setterProperty_setter(instance):
    original = instance.setterProperty
    instance.setterProperty = original
    assert instance.setterProperty == original



@given(instance=haxe_HaxeAttribute_strategy)
def test_haxe_haxeattribute_getterProperty_setter(instance):
    original = instance.getterProperty
    instance.getterProperty = original
    assert instance.getterProperty == original

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

@given(instance=haxe_HaxeTypedef_strategy)
@settings(max_examples=50)
def test_haxe_haxetypedef_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTypedef)

@given(instance=haxe_HaxeClassifier_strategy)
@settings(max_examples=50)
def test_haxe_haxeclassifier_instantiation(instance):
    assert isinstance(instance, haxe_HaxeClassifier)

@given(instance=haxe_HaxeTypeParameter_strategy)
@settings(max_examples=50)
def test_haxe_haxetypeparameter_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTypeParameter)

@given(instance=HaxePathReferentiable_strategy)
@settings(max_examples=50)
def test_haxepathreferentiable_instantiation(instance):
    assert isinstance(instance, HaxePathReferentiable)

@given(instance=HaxeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxevariabledeclaration_instantiation(instance):
    assert isinstance(instance, HaxeVariableDeclaration)

@given(instance=haxe_HaxeEnumConstructor_strategy)
@settings(max_examples=50)
def test_haxe_haxeenumconstructor_instantiation(instance):
    assert isinstance(instance, haxe_HaxeEnumConstructor)

@given(instance=haxe_HaxeVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_haxe_haxevariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, haxe_HaxeVariableDeclarationFragment)

@given(instance=HaxePathReference_strategy)
@settings(max_examples=50)
def test_haxepathreference_instantiation(instance):
    assert isinstance(instance, HaxePathReference)

@given(instance=haxe_HaxeClassifierAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxeclassifieraccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeClassifierAccess)

@given(instance=HaxeMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxemethodinvocation_instantiation(instance):
    assert isinstance(instance, HaxeMethodInvocation)

@given(instance=haxe_HaxeSuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_haxe_haxesuperconstructorinvocation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeSuperConstructorInvocation)

@given(instance=HaxeAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxeabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, HaxeAbstractMethodInvocation)

@given(instance=HaxeTypedElement_strategy)
@settings(max_examples=50)
def test_haxetypedelement_instantiation(instance):
    assert isinstance(instance, HaxeTypedElement)

@given(instance=haxe_HaxeVariableDeclarationGroup_strategy)
@settings(max_examples=50)
def test_haxe_haxevariabledeclarationgroup_instantiation(instance):
    assert isinstance(instance, haxe_HaxeVariableDeclarationGroup)

@given(instance=haxe_HaxeOperation_strategy)
@settings(max_examples=50)
def test_haxe_haxeoperation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeOperation)



@given(instance=haxe_HaxeOperation_strategy)
def test_haxe_haxeoperation_macro_setter(instance):
    original = instance.macro
    instance.macro = original
    assert instance.macro == original

@given(instance=HaxeAbstractFunction_strategy)
@settings(max_examples=50)
def test_haxeabstractfunction_instantiation(instance):
    assert isinstance(instance, HaxeAbstractFunction)

@given(instance=haxe_HaxeAbstractOperation_strategy)
@settings(max_examples=50)
def test_haxe_haxeabstractoperation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAbstractOperation)



@given(instance=haxe_HaxeAbstractOperation_strategy)
def test_haxe_haxeabstractoperation_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original



@given(instance=haxe_HaxeAbstractOperation_strategy)
def test_haxe_haxeabstractoperation_overrides_setter(instance):
    original = instance.overrides
    instance.overrides = original
    assert instance.overrides == original

@given(instance=HaxeConstant_strategy)
@settings(max_examples=50)
def test_haxeconstant_instantiation(instance):
    assert isinstance(instance, HaxeConstant)

@given(instance=haxe_HaxeRegexLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxeregexliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeRegexLiteral)



@given(instance=haxe_HaxeRegexLiteral_strategy)
def test_haxe_haxeregexliteral_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=haxe_HaxeRegexLiteral_strategy)
def test_haxe_haxeregexliteral_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=haxe_HaxeIdentifierLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxeidentifierliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeIdentifierLiteral)



@given(instance=haxe_HaxeIdentifierLiteral_strategy)
def test_haxe_haxeidentifierliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe_HaxeNullLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxenullliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeNullLiteral)

@given(instance=haxe_HaxeBooleanLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxebooleanliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeBooleanLiteral)



@given(instance=haxe_HaxeBooleanLiteral_strategy)
def test_haxe_haxebooleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe_HaxeNumberLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxenumberliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeNumberLiteral)



@given(instance=haxe_HaxeNumberLiteral_strategy)
def test_haxe_haxenumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=haxe_HaxeStringLiteral_strategy)
@settings(max_examples=50)
def test_haxe_haxestringliteral_instantiation(instance):
    assert isinstance(instance, haxe_HaxeStringLiteral)



@given(instance=haxe_HaxeStringLiteral_strategy)
def test_haxe_haxestringliteral_escapedValue_setter(instance):
    original = instance.escapedValue
    instance.escapedValue = original
    assert instance.escapedValue == original

@given(instance=HaxeExpressionStatement_strategy)
@settings(max_examples=50)
def test_haxeexpressionstatement_instantiation(instance):
    assert isinstance(instance, HaxeExpressionStatement)

@given(instance=haxe_HaxeThrowExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxethrowexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeThrowExpression)

@given(instance=haxe_HaxeReturn_strategy)
@settings(max_examples=50)
def test_haxe_haxereturn_instantiation(instance):
    assert isinstance(instance, haxe_HaxeReturn)

@given(instance=HaxeBinaryExpression_strategy)
@settings(max_examples=50)
def test_haxebinaryexpression_instantiation(instance):
    assert isinstance(instance, HaxeBinaryExpression)

@given(instance=haxe_HaxeAssignment_strategy)
@settings(max_examples=50)
def test_haxe_haxeassignment_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAssignment)



@given(instance=haxe_HaxeAssignment_strategy)
def test_haxe_haxeassignment_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=haxe_HaxeInfixExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeinfixexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeInfixExpression)



@given(instance=haxe_HaxeInfixExpression_strategy)
def test_haxe_haxeinfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=HaxeUnaryExpression_strategy)
@settings(max_examples=50)
def test_haxeunaryexpression_instantiation(instance):
    assert isinstance(instance, HaxeUnaryExpression)

@given(instance=haxe_HaxePostfixExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxepostfixexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxePostfixExpression)



@given(instance=haxe_HaxePostfixExpression_strategy)
def test_haxe_haxepostfixexpression_isIncrement_setter(instance):
    original = instance.isIncrement
    instance.isIncrement = original
    assert instance.isIncrement == original

@given(instance=haxe_HaxePrefixExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeprefixexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxePrefixExpression)



@given(instance=haxe_HaxePrefixExpression_strategy)
def test_haxe_haxeprefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=haxe_HaxeSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxesinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeSingleVariableDeclaration)



@given(instance=haxe_HaxeSingleVariableDeclaration_strategy)
def test_haxe_haxesinglevariabledeclaration_isOptional_setter(instance):
    original = instance.isOptional
    instance.isOptional = original
    assert instance.isOptional == original

@given(instance=HaxeLoopStatement_strategy)
@settings(max_examples=50)
def test_haxeloopstatement_instantiation(instance):
    assert isinstance(instance, HaxeLoopStatement)

@given(instance=haxe_HaxeDoWhileStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxedowhilestatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeDoWhileStatement)

@given(instance=haxe_HaxeWhileStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxewhilestatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeWhileStatement)

@given(instance=haxe_HaxeForStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxeforstatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeForStatement)

@given(instance=HaxeConditionalExpression_strategy)
@settings(max_examples=50)
def test_haxeconditionalexpression_instantiation(instance):
    assert isinstance(instance, HaxeConditionalExpression)

@given(instance=haxe_HaxeTernaryExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeternaryexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTernaryExpression)

@given(instance=haxe_HaxeIfStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxeifstatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeIfStatement)

@given(instance=HaxeExpression_strategy)
@settings(max_examples=50)
def test_haxeexpression_instantiation(instance):
    assert isinstance(instance, HaxeExpression)

@given(instance=haxe_HaxeParenthizedExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeparenthizedexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeParenthizedExpression)

@given(instance=haxe_HaxeCatchClause_strategy)
@settings(max_examples=50)
def test_haxe_haxecatchclause_instantiation(instance):
    assert isinstance(instance, haxe_HaxeCatchClause)

@given(instance=haxe_HaxeFieldAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxefieldaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeFieldAccess)

@given(instance=haxe_HaxeBlock_strategy)
@settings(max_examples=50)
def test_haxe_haxeblock_instantiation(instance):
    assert isinstance(instance, haxe_HaxeBlock)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=haxe_HaxeBlock_strategy)
@settings(max_examples=30)
def test_haxe_haxeblock_isempty_changes_state(instance):
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
        assert has_statements, f"Function 'isEmpty' in haxe_HaxeBlock is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isEmpty' in haxe_HaxeBlock did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isEmpty' in haxe_HaxeBlock is not implemented or raised an error")

@given(instance=haxe_HaxeTypeCheckExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxetypecheckexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTypeCheckExpression)

@given(instance=haxe_HaxeCallExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxecallexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeCallExpression)

@given(instance=haxe_HaxePackageAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxepackageaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxePackageAccess)

@given(instance=haxe_HaxeConstant_strategy)
@settings(max_examples=50)
def test_haxe_haxeconstant_instantiation(instance):
    assert isinstance(instance, haxe_HaxeConstant)

@given(instance=haxe_HaxeArrayInitializer_strategy)
@settings(max_examples=50)
def test_haxe_haxearrayinitializer_instantiation(instance):
    assert isinstance(instance, haxe_HaxeArrayInitializer)

@given(instance=haxe_HaxeInExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeinexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeInExpression)

@given(instance=haxe_HaxeTypeAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxetypeaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTypeAccess)

@given(instance=haxe_HaxeSingleVariableAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxesinglevariableaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeSingleVariableAccess)

@given(instance=haxe_HaxeConditionalExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeconditionalexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeConditionalExpression)

@given(instance=haxe_HaxeFunctionExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxefunctionexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeFunctionExpression)

@given(instance=haxe_HaxeSwitch_strategy)
@settings(max_examples=50)
def test_haxe_haxeswitch_instantiation(instance):
    assert isinstance(instance, haxe_HaxeSwitch)

@given(instance=haxe_HaxeArrayCreation_strategy)
@settings(max_examples=50)
def test_haxe_haxearraycreation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeArrayCreation)

@given(instance=haxe_HaxeThisExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxethisexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeThisExpression)

@given(instance=haxe_HaxeArrayAccess_strategy)
@settings(max_examples=50)
def test_haxe_haxearrayaccess_instantiation(instance):
    assert isinstance(instance, haxe_HaxeArrayAccess)

@given(instance=haxe_HaxeExpressionStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxeexpressionstatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeExpressionStatement)

@given(instance=haxe_HaxeUnsafeCastExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeunsafecastexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeUnsafeCastExpression)

@given(instance=haxe_HaxeCase_strategy)
@settings(max_examples=50)
def test_haxe_haxecase_instantiation(instance):
    assert isinstance(instance, haxe_HaxeCase)

@given(instance=haxe_HaxeBreak_strategy)
@settings(max_examples=50)
def test_haxe_haxebreak_instantiation(instance):
    assert isinstance(instance, haxe_HaxeBreak)

@given(instance=haxe_HaxeBinaryExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxebinaryexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeBinaryExpression)

@given(instance=haxe_HaxeUnaryExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeunaryexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeUnaryExpression)

@given(instance=haxe_HaxeSuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe_haxesupermethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeSuperMethodInvocation)

@given(instance=haxe_HaxeContinue_strategy)
@settings(max_examples=50)
def test_haxe_haxecontinue_instantiation(instance):
    assert isinstance(instance, haxe_HaxeContinue)

@given(instance=haxe_HaxeCastingExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxecastingexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeCastingExpression)

@given(instance=haxe_HaxeTryExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxetryexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTryExpression)

@given(instance=haxe_HaxeVariableDeclarationExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxevariabledeclarationexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeVariableDeclarationExpression)

@given(instance=haxe_HaxeMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe_haxemethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeMethodInvocation)

@given(instance=haxe_HaxeObjectDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxeobjectdeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeObjectDeclaration)

@given(instance=haxe_HaxeEmptyStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxeemptystatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeEmptyStatement)

@given(instance=haxe_HaxeLoopStatement_strategy)
@settings(max_examples=50)
def test_haxe_haxeloopstatement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeLoopStatement)

@given(instance=haxe_HaxePackage_strategy)
@settings(max_examples=50)
def test_haxe_haxepackage_instantiation(instance):
    assert isinstance(instance, haxe_HaxePackage)

@given(instance=HaxeNamedElement_strategy)
@settings(max_examples=50)
def test_haxenamedelement_instantiation(instance):
    assert isinstance(instance, HaxeNamedElement)

@given(instance=haxe_HaxeMetadata_strategy)
@settings(max_examples=50)
def test_haxe_haxemetadata_instantiation(instance):
    assert isinstance(instance, haxe_HaxeMetadata)



@given(instance=haxe_HaxeMetadata_strategy)
def test_haxe_haxemetadata_compilerMetadata_setter(instance):
    original = instance.compilerMetadata
    instance.compilerMetadata = original
    assert instance.compilerMetadata == original

@given(instance=haxe_HaxeVariableDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxevariabledeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeVariableDeclaration)

@given(instance=haxe_HaxeFieldDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxefielddeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeFieldDeclaration)

@given(instance=haxe_HaxeField_strategy)
@settings(max_examples=50)
def test_haxe_haxefield_instantiation(instance):
    assert isinstance(instance, haxe_HaxeField)



@given(instance=haxe_HaxeField_strategy)
def test_haxe_haxefield_isPrivate_setter(instance):
    original = instance.isPrivate
    instance.isPrivate = original
    assert instance.isPrivate == original



@given(instance=haxe_HaxeField_strategy)
def test_haxe_haxefield_isStatic_setter(instance):
    original = instance.isStatic
    instance.isStatic = original
    assert instance.isStatic == original

@given(instance=HaxeComment_strategy)
@settings(max_examples=50)
def test_haxecomment_instantiation(instance):
    assert isinstance(instance, HaxeComment)

@given(instance=haxe_HaxeHaxedocComment_strategy)
@settings(max_examples=50)
def test_haxe_haxehaxedoccomment_instantiation(instance):
    assert isinstance(instance, haxe_HaxeHaxedocComment)

@given(instance=HaxeASTNode_strategy)
@settings(max_examples=50)
def test_haxeastnode_instantiation(instance):
    assert isinstance(instance, HaxeASTNode)

@given(instance=haxe_HaxeDependencyDeclaration_strategy)
@settings(max_examples=50)
def test_haxe_haxedependencydeclaration_instantiation(instance):
    assert isinstance(instance, haxe_HaxeDependencyDeclaration)

@given(instance=haxe_HaxeTextElement_strategy)
@settings(max_examples=50)
def test_haxe_haxetextelement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTextElement)



@given(instance=haxe_HaxeTextElement_strategy)
def test_haxe_haxetextelement_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=haxe_HaxeType_strategy)
@settings(max_examples=50)
def test_haxe_haxetype_instantiation(instance):
    assert isinstance(instance, haxe_HaxeType)



@given(instance=haxe_HaxeType_strategy)
def test_haxe_haxetype_extern_setter(instance):
    original = instance.extern
    instance.extern = original
    assert instance.extern == original



@given(instance=haxe_HaxeType_strategy)
def test_haxe_haxetype_private_setter(instance):
    original = instance.private
    instance.private = original
    assert instance.private == original

@given(instance=haxe_HaxeExpression_strategy)
@settings(max_examples=50)
def test_haxe_haxeexpression_instantiation(instance):
    assert isinstance(instance, haxe_HaxeExpression)

@given(instance=haxe_HaxeAbstractFunction_strategy)
@settings(max_examples=50)
def test_haxe_haxeabstractfunction_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAbstractFunction)

@given(instance=haxe_HaxeTagElement_strategy)
@settings(max_examples=50)
def test_haxe_haxetagelement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTagElement)



@given(instance=haxe_HaxeTagElement_strategy)
def test_haxe_haxetagelement_tagName_setter(instance):
    original = instance.tagName
    instance.tagName = original
    assert instance.tagName == original

@given(instance=haxe_HaxeAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_haxe_haxeabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, haxe_HaxeAbstractMethodInvocation)

@given(instance=haxe_HaxeNamedElement_strategy)
@settings(max_examples=50)
def test_haxe_haxenamedelement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeNamedElement)



@given(instance=haxe_HaxeNamedElement_strategy)
def test_haxe_haxenamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=haxe_HaxeComment_strategy)
@settings(max_examples=50)
def test_haxe_haxecomment_instantiation(instance):
    assert isinstance(instance, haxe_HaxeComment)



@given(instance=haxe_HaxeComment_strategy)
def test_haxe_haxecomment_enclosedByParent_setter(instance):
    original = instance.enclosedByParent
    instance.enclosedByParent = original
    assert instance.enclosedByParent == original



@given(instance=haxe_HaxeComment_strategy)
def test_haxe_haxecomment_prefixOfParent_setter(instance):
    original = instance.prefixOfParent
    instance.prefixOfParent = original
    assert instance.prefixOfParent == original



@given(instance=haxe_HaxeComment_strategy)
def test_haxe_haxecomment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=haxe_HaxeComment_strategy)
def test_haxe_haxecomment_lineComment_setter(instance):
    original = instance.lineComment
    instance.lineComment = original
    assert instance.lineComment == original

@given(instance=HaxeModelElement_strategy)
@settings(max_examples=50)
def test_haxemodelelement_instantiation(instance):
    assert isinstance(instance, HaxeModelElement)

@given(instance=haxe_HaxeFieldContainer_strategy)
@settings(max_examples=50)
def test_haxe_haxefieldcontainer_instantiation(instance):
    assert isinstance(instance, haxe_HaxeFieldContainer)

@given(instance=haxe_HaxePathReference_strategy)
@settings(max_examples=50)
def test_haxe_haxepathreference_instantiation(instance):
    assert isinstance(instance, haxe_HaxePathReference)

@given(instance=haxe_HaxeMetadataContainer_strategy)
@settings(max_examples=50)
def test_haxe_haxemetadatacontainer_instantiation(instance):
    assert isinstance(instance, haxe_HaxeMetadataContainer)

@given(instance=haxe_HaxeTypedElement_strategy)
@settings(max_examples=50)
def test_haxe_haxetypedelement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeTypedElement)

@given(instance=haxe_HaxeASTNode_strategy)
@settings(max_examples=50)
def test_haxe_haxeastnode_instantiation(instance):
    assert isinstance(instance, haxe_HaxeASTNode)

@given(instance=haxe_HaxeModelElement_strategy)
@settings(max_examples=50)
def test_haxe_haxemodelelement_instantiation(instance):
    assert isinstance(instance, haxe_HaxeModelElement)

@given(instance=haxe_HaxeModule_strategy)
@settings(max_examples=50)
def test_haxe_haxemodule_instantiation(instance):
    assert isinstance(instance, haxe_HaxeModule)

@given(instance=haxe_HaxePathReferentiable_strategy)
@settings(max_examples=50)
def test_haxe_haxepathreferentiable_instantiation(instance):
    assert isinstance(instance, haxe_HaxePathReferentiable)

@given(instance=haxe_HaxeClass_strategy)
@settings(max_examples=50)
def test_haxe_haxeclass_instantiation(instance):
    assert isinstance(instance, haxe_HaxeClass)



@given(instance=haxe_HaxeClass_strategy)
def test_haxe_haxeclass_isInterface_setter(instance):
    original = instance.isInterface
    instance.isInterface = original
    assert instance.isInterface == original

@given(instance=haxe_HaxeModel_strategy)
@settings(max_examples=50)
def test_haxe_haxemodel_instantiation(instance):
    assert isinstance(instance, haxe_HaxeModel)



@given(instance=haxe_HaxeModel_strategy)
def test_haxe_haxemodel_sourceFolder_setter(instance):
    original = instance.sourceFolder
    instance.sourceFolder = original
    assert instance.sourceFolder == original



@given(instance=haxe_HaxeModel_strategy)
def test_haxe_haxemodel_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original



@given(instance=haxe_HaxeModel_strategy)
def test_haxe_haxemodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=haxe_HaxeModel_strategy)
def test_haxe_haxemodel_targetFolder_setter(instance):
    original = instance.targetFolder
    instance.targetFolder = original
    assert instance.targetFolder == original
