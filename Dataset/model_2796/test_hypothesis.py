import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Metamodelo_Cpp_CppModelElement,
    CppFieldContainer,
    Metamodelo_Cpp_CppModel,
    CppPathReferentiable,
    CppModelElement,
    Metamodelo_Cpp_CppComment,
    Metamodelo_Cpp_CppExpression,
    Metamodelo_Cpp_CppPathReference,
    Metamodelo_Cpp_CppPackage,
    CppNamedElement,
    Metamodelo_Cpp_CppEnumConstructor,
    Metamodelo_Cpp_CppPathReferentiable,
    Metamodelo_Cpp_CppClassFile,
    Metamodelo_Cpp_CppType,
    Metamodelo_Cpp_CppVariableDeclaration,
    Metamodelo_Cpp_CppFieldContainer,
    Metamodelo_Cpp_CppField,
    CppBinaryExpression,
    Metamodelo_Cpp_CppAssignamentStatement,
    CppUnaryExpression,
    Metamodelo_Cpp_CppPrefixExpression,
    Metamodelo_Cpp_CppPostfixExpression,
    Metamodelo_Cpp_CppInfixExpression,
    CppSelectionStatement,
    Metamodelo_Cpp_CppIfElseStatement,
    Metamodelo_Cpp_CppIfStatement,
    CppMethodInvocation,
    Metamodelo_Cpp_CppSuperConstructorInvocation,
    CppJumpStatement,
    Metamodelo_Cpp_CppContinueStatement,
    Metamodelo_Cpp_CppReturnStatement,
    Metamodelo_Cpp_CppGotoStatement,
    Metamodelo_Cpp_CppBreakStatement,
    CppIterationStatement,
    Metamodelo_Cpp_CppForStatement,
    Metamodelo_Cpp_CppDoWhileStatement,
    Metamodelo_Cpp_CppWhileStatement,
    CppExpression,
    Metamodelo_Cpp_CppCatchClause,
    Metamodelo_Cpp_CppSelectionStatement,
    Metamodelo_Cpp_CppFieldAccess,
    Metamodelo_Cpp_CppThrowExpression,
    Metamodelo_Cpp_CppNullLiteral,
    Metamodelo_Cpp_CppParenthizedExpression,
    Metamodelo_Cpp_CppUnaryExpression,
    Metamodelo_Cpp_CppIterationStatement,
    Metamodelo_Cpp_CppSwitchExpression,
    Metamodelo_Cpp_CppArrayAccess,
    Metamodelo_Cpp_CppTryExpression,
    Metamodelo_Cpp_CppJumpStatement,
    Metamodelo_Cpp_CppConstantExpression,
    Metamodelo_Cpp_CppNumberLiteral,
    Metamodelo_Cpp_CppBlock,
    Metamodelo_Cpp_CppCharacterLiteral,
    Metamodelo_Cpp_CppDeclarationExpression,
    Metamodelo_Cpp_CppCase,
    Metamodelo_Cpp_CppBooleanLiteral,
    Metamodelo_Cpp_CppLabeledStatement,
    Metamodelo_Cpp_CppVariableAccess,
    Metamodelo_Cpp_CppBinaryExpression,
    Metamodelo_Cpp_CppThisExpression,
    Metamodelo_Cpp_CppStringLiteral,
    Metamodelo_Cpp_CppCastExpression,
    Metamodelo_Cpp_CppRegexLiteral,
    Metamodelo_Cpp_CppArrayInitializer,
    CppTypedElement,
    Metamodelo_Cpp_CppVariableDeclarationGroup,
    CppField,
    CppVariableDeclaration,
    Metamodelo_Cpp_CppSingleVariableDeclaration,
    Metamodelo_Cpp_CppVariableDeclarationFragment,
    CppAbstractMethodInvocation,
    Metamodelo_Cpp_CppSuperMethodInvocation,
    Metamodelo_Cpp_CppMethodInvocation,
    Metamodelo_Cpp_CppAbstractMethodInvocation,
    CppMemberFunction,
    Metamodelo_Cpp_CppMethod,
    Metamodelo_Cpp_CppDestructor,
    Metamodelo_Cpp_CppConstructor,
    CppFunction,
    Metamodelo_Cpp_CppMemberFunction,
    Metamodelo_Cpp_CppTypedElement,
    CppClassifier,
    Metamodelo_Cpp_CppClass,
    CppPrimitiveType,
    Metamodelo_Cpp_CppFloatType,
    Metamodelo_Cpp_CppUnsignedType,
    Metamodelo_Cpp_CppVoidType,
    Metamodelo_Cpp_CppSignedType,
    Metamodelo_Cpp_CppLongType,
    Metamodelo_Cpp_CppDoubleType,
    Metamodelo_Cpp_CppShortType,
    Metamodelo_Cpp_CppCharType,
    Metamodelo_Cpp_CppIntType,
    Metamodelo_Cpp_CppBooleanType,
    CppType,
    Metamodelo_Cpp_CppVariable,
    Metamodelo_Cpp_CppEnum,
    Metamodelo_Cpp_CppClassifier,
    Metamodelo_Cpp_CppFunction,
    Metamodelo_Cpp_CppPrimitiveType,
    Metamodelo_Cpp_CppTypeParameter,
    Metamodelo_Cpp_CppTypeAccess,
    Metamodelo_Cpp_CppImportDeclaration,
    Metamodelo_Cpp_CppNamedElement,
    CppLinkageSpecifier,
    CppClassKey,
    CppOperator,
    CppStorageType,
    CppAccessSpecifier,
    CppPostfixOperator,
    CppQualifierType,
    CppAssignmentOperator,
    CppVarType,
    CppUnaryOperator,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_metamodelo_cpp_cppmodelelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppModelElement)


def test_metamodelo_cpp_cppmodelelement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppModelElement.__init__)


def test_metamodelo_cpp_cppmodelelement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppModelElement.__init__)
    params = list(sig.parameters.keys())



def test_cppfieldcontainer_is_not_abstract():
    assert not inspect.isabstract(CppFieldContainer)


def test_cppfieldcontainer_constructor_exists():
    assert callable(CppFieldContainer.__init__)


def test_cppfieldcontainer_constructor_args():
    sig = inspect.signature(CppFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppmodel_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppModel)


def test_metamodelo_cpp_cppmodel_constructor_exists():
    assert callable(Metamodelo_Cpp_CppModel.__init__)


def test_metamodelo_cpp_cppmodel_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "sourceFolder" in params, "Missing parameter 'sourceFolder'"
    assert "targetFolder" in params, "Missing parameter 'targetFolder'"

def test_metamodelo_cpp_cppmodel_has_name():
    assert hasattr(Metamodelo_Cpp_CppModel, "name")
    descriptor = None
    for klass in Metamodelo_Cpp_CppModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppmodel_has_sourceFolder():
    assert hasattr(Metamodelo_Cpp_CppModel, "sourceFolder")
    descriptor = None
    for klass in Metamodelo_Cpp_CppModel.__mro__:
        if "sourceFolder" in klass.__dict__:
            descriptor = klass.__dict__["sourceFolder"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppmodel_has_targetFolder():
    assert hasattr(Metamodelo_Cpp_CppModel, "targetFolder")
    descriptor = None
    for klass in Metamodelo_Cpp_CppModel.__mro__:
        if "targetFolder" in klass.__dict__:
            descriptor = klass.__dict__["targetFolder"]
            break
    assert isinstance(descriptor, property)



def test_cpppathreferentiable_is_not_abstract():
    assert not inspect.isabstract(CppPathReferentiable)


def test_cpppathreferentiable_constructor_exists():
    assert callable(CppPathReferentiable.__init__)


def test_cpppathreferentiable_constructor_args():
    sig = inspect.signature(CppPathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_cppmodelelement_is_not_abstract():
    assert not inspect.isabstract(CppModelElement)


def test_cppmodelelement_constructor_exists():
    assert callable(CppModelElement.__init__)


def test_cppmodelelement_constructor_args():
    sig = inspect.signature(CppModelElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppcomment_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppComment)


def test_metamodelo_cpp_cppcomment_constructor_exists():
    assert callable(Metamodelo_Cpp_CppComment.__init__)


def test_metamodelo_cpp_cppcomment_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppComment.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"
    assert "multiLine" in params, "Missing parameter 'multiLine'"
    assert "singleLine" in params, "Missing parameter 'singleLine'"

def test_metamodelo_cpp_cppcomment_has_content():
    assert hasattr(Metamodelo_Cpp_CppComment, "content")
    descriptor = None
    for klass in Metamodelo_Cpp_CppComment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppcomment_has_multiLine():
    assert hasattr(Metamodelo_Cpp_CppComment, "multiLine")
    descriptor = None
    for klass in Metamodelo_Cpp_CppComment.__mro__:
        if "multiLine" in klass.__dict__:
            descriptor = klass.__dict__["multiLine"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppcomment_has_singleLine():
    assert hasattr(Metamodelo_Cpp_CppComment, "singleLine")
    descriptor = None
    for klass in Metamodelo_Cpp_CppComment.__mro__:
        if "singleLine" in klass.__dict__:
            descriptor = klass.__dict__["singleLine"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppExpression)


def test_metamodelo_cpp_cppexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppExpression.__init__)


def test_metamodelo_cpp_cppexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpppathreference_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPathReference)


def test_metamodelo_cpp_cpppathreference_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPathReference.__init__)


def test_metamodelo_cpp_cpppathreference_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPathReference.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpppackage_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPackage)


def test_metamodelo_cpp_cpppackage_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPackage.__init__)


def test_metamodelo_cpp_cpppackage_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPackage.__init__)
    params = list(sig.parameters.keys())



def test_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(CppNamedElement)


def test_cppnamedelement_constructor_exists():
    assert callable(CppNamedElement.__init__)


def test_cppnamedelement_constructor_args():
    sig = inspect.signature(CppNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppenumconstructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppEnumConstructor)


def test_metamodelo_cpp_cppenumconstructor_constructor_exists():
    assert callable(Metamodelo_Cpp_CppEnumConstructor.__init__)


def test_metamodelo_cpp_cppenumconstructor_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppEnumConstructor.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpppathreferentiable_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPathReferentiable)


def test_metamodelo_cpp_cpppathreferentiable_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPathReferentiable.__init__)


def test_metamodelo_cpp_cpppathreferentiable_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppclassfile_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppClassFile)


def test_metamodelo_cpp_cppclassfile_constructor_exists():
    assert callable(Metamodelo_Cpp_CppClassFile.__init__)


def test_metamodelo_cpp_cppclassfile_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppClassFile.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpptype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppType)


def test_metamodelo_cpp_cpptype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppType.__init__)


def test_metamodelo_cpp_cpptype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVariableDeclaration)


def test_metamodelo_cpp_cppvariabledeclaration_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVariableDeclaration.__init__)


def test_metamodelo_cpp_cppvariabledeclaration_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "vartype" in params, "Missing parameter 'vartype'"
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_metamodelo_cpp_cppvariabledeclaration_has_vartype():
    assert hasattr(Metamodelo_Cpp_CppVariableDeclaration, "vartype")
    descriptor = None
    for klass in Metamodelo_Cpp_CppVariableDeclaration.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppvariabledeclaration_has_isArray():
    assert hasattr(Metamodelo_Cpp_CppVariableDeclaration, "isArray")
    descriptor = None
    for klass in Metamodelo_Cpp_CppVariableDeclaration.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppfieldcontainer_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppFieldContainer)


def test_metamodelo_cpp_cppfieldcontainer_constructor_exists():
    assert callable(Metamodelo_Cpp_CppFieldContainer.__init__)


def test_metamodelo_cpp_cppfieldcontainer_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppfield_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppField)


def test_metamodelo_cpp_cppfield_constructor_exists():
    assert callable(Metamodelo_Cpp_CppField.__init__)


def test_metamodelo_cpp_cppfield_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppField.__init__)
    params = list(sig.parameters.keys())
    assert "accessSpecifier" in params, "Missing parameter 'accessSpecifier'"

def test_metamodelo_cpp_cppfield_has_accessSpecifier():
    assert hasattr(Metamodelo_Cpp_CppField, "accessSpecifier")
    descriptor = None
    for klass in Metamodelo_Cpp_CppField.__mro__:
        if "accessSpecifier" in klass.__dict__:
            descriptor = klass.__dict__["accessSpecifier"]
            break
    assert isinstance(descriptor, property)



def test_cppbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(CppBinaryExpression)


def test_cppbinaryexpression_constructor_exists():
    assert callable(CppBinaryExpression.__init__)


def test_cppbinaryexpression_constructor_args():
    sig = inspect.signature(CppBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppassignamentstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppAssignamentStatement)


def test_metamodelo_cpp_cppassignamentstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppAssignamentStatement.__init__)


def test_metamodelo_cpp_cppassignamentstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppAssignamentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo_cpp_cppassignamentstatement_has_operator():
    assert hasattr(Metamodelo_Cpp_CppAssignamentStatement, "operator")
    descriptor = None
    for klass in Metamodelo_Cpp_CppAssignamentStatement.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cppunaryexpression_is_not_abstract():
    assert not inspect.isabstract(CppUnaryExpression)


def test_cppunaryexpression_constructor_exists():
    assert callable(CppUnaryExpression.__init__)


def test_cppunaryexpression_constructor_args():
    sig = inspect.signature(CppUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppprefixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPrefixExpression)


def test_metamodelo_cpp_cppprefixexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPrefixExpression.__init__)


def test_metamodelo_cpp_cppprefixexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo_cpp_cppprefixexpression_has_operator():
    assert hasattr(Metamodelo_Cpp_CppPrefixExpression, "operator")
    descriptor = None
    for klass in Metamodelo_Cpp_CppPrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cpppostfixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPostfixExpression)


def test_metamodelo_cpp_cpppostfixexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPostfixExpression.__init__)


def test_metamodelo_cpp_cpppostfixexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo_cpp_cpppostfixexpression_has_operator():
    assert hasattr(Metamodelo_Cpp_CppPostfixExpression, "operator")
    descriptor = None
    for klass in Metamodelo_Cpp_CppPostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppinfixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppInfixExpression)


def test_metamodelo_cpp_cppinfixexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppInfixExpression.__init__)


def test_metamodelo_cpp_cppinfixexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppInfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo_cpp_cppinfixexpression_has_operator():
    assert hasattr(Metamodelo_Cpp_CppInfixExpression, "operator")
    descriptor = None
    for klass in Metamodelo_Cpp_CppInfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cppselectionstatement_is_not_abstract():
    assert not inspect.isabstract(CppSelectionStatement)


def test_cppselectionstatement_constructor_exists():
    assert callable(CppSelectionStatement.__init__)


def test_cppselectionstatement_constructor_args():
    sig = inspect.signature(CppSelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppifelsestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppIfElseStatement)


def test_metamodelo_cpp_cppifelsestatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppIfElseStatement.__init__)


def test_metamodelo_cpp_cppifelsestatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppIfElseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "inLine" in params, "Missing parameter 'inLine'"

def test_metamodelo_cpp_cppifelsestatement_has_inLine():
    assert hasattr(Metamodelo_Cpp_CppIfElseStatement, "inLine")
    descriptor = None
    for klass in Metamodelo_Cpp_CppIfElseStatement.__mro__:
        if "inLine" in klass.__dict__:
            descriptor = klass.__dict__["inLine"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppifstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppIfStatement)


def test_metamodelo_cpp_cppifstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppIfStatement.__init__)


def test_metamodelo_cpp_cppifstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(CppMethodInvocation)


def test_cppmethodinvocation_constructor_exists():
    assert callable(CppMethodInvocation.__init__)


def test_cppmethodinvocation_constructor_args():
    sig = inspect.signature(CppMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppsuperconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSuperConstructorInvocation)


def test_metamodelo_cpp_cppsuperconstructorinvocation_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSuperConstructorInvocation.__init__)


def test_metamodelo_cpp_cppsuperconstructorinvocation_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_cppjumpstatement_is_not_abstract():
    assert not inspect.isabstract(CppJumpStatement)


def test_cppjumpstatement_constructor_exists():
    assert callable(CppJumpStatement.__init__)


def test_cppjumpstatement_constructor_args():
    sig = inspect.signature(CppJumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppcontinuestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppContinueStatement)


def test_metamodelo_cpp_cppcontinuestatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppContinueStatement.__init__)


def test_metamodelo_cpp_cppcontinuestatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppreturnstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppReturnStatement)


def test_metamodelo_cpp_cppreturnstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppReturnStatement.__init__)


def test_metamodelo_cpp_cppreturnstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppgotostatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppGotoStatement)


def test_metamodelo_cpp_cppgotostatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppGotoStatement.__init__)


def test_metamodelo_cpp_cppgotostatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppGotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppbreakstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppBreakStatement)


def test_metamodelo_cpp_cppbreakstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppBreakStatement.__init__)


def test_metamodelo_cpp_cppbreakstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppBreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppiterationstatement_is_not_abstract():
    assert not inspect.isabstract(CppIterationStatement)


def test_cppiterationstatement_constructor_exists():
    assert callable(CppIterationStatement.__init__)


def test_cppiterationstatement_constructor_args():
    sig = inspect.signature(CppIterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppforstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppForStatement)


def test_metamodelo_cpp_cppforstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppForStatement.__init__)


def test_metamodelo_cpp_cppforstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppForStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppdowhilestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppDoWhileStatement)


def test_metamodelo_cpp_cppdowhilestatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppDoWhileStatement.__init__)


def test_metamodelo_cpp_cppdowhilestatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppDoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppwhilestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppWhileStatement)


def test_metamodelo_cpp_cppwhilestatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppWhileStatement.__init__)


def test_metamodelo_cpp_cppwhilestatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppexpression_is_not_abstract():
    assert not inspect.isabstract(CppExpression)


def test_cppexpression_constructor_exists():
    assert callable(CppExpression.__init__)


def test_cppexpression_constructor_args():
    sig = inspect.signature(CppExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppcatchclause_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppCatchClause)


def test_metamodelo_cpp_cppcatchclause_constructor_exists():
    assert callable(Metamodelo_Cpp_CppCatchClause.__init__)


def test_metamodelo_cpp_cppcatchclause_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppselectionstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSelectionStatement)


def test_metamodelo_cpp_cppselectionstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSelectionStatement.__init__)


def test_metamodelo_cpp_cppselectionstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppFieldAccess)


def test_metamodelo_cpp_cppfieldaccess_constructor_exists():
    assert callable(Metamodelo_Cpp_CppFieldAccess.__init__)


def test_metamodelo_cpp_cppfieldaccess_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppthrowexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppThrowExpression)


def test_metamodelo_cpp_cppthrowexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppThrowExpression.__init__)


def test_metamodelo_cpp_cppthrowexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppThrowExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppnullliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppNullLiteral)


def test_metamodelo_cpp_cppnullliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppNullLiteral.__init__)


def test_metamodelo_cpp_cppnullliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppparenthizedexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppParenthizedExpression)


def test_metamodelo_cpp_cppparenthizedexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppParenthizedExpression.__init__)


def test_metamodelo_cpp_cppparenthizedexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppParenthizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppunaryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppUnaryExpression)


def test_metamodelo_cpp_cppunaryexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppUnaryExpression.__init__)


def test_metamodelo_cpp_cppunaryexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppiterationstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppIterationStatement)


def test_metamodelo_cpp_cppiterationstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppIterationStatement.__init__)


def test_metamodelo_cpp_cppiterationstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppIterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppswitchexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSwitchExpression)


def test_metamodelo_cpp_cppswitchexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSwitchExpression.__init__)


def test_metamodelo_cpp_cppswitchexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpparrayaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppArrayAccess)


def test_metamodelo_cpp_cpparrayaccess_constructor_exists():
    assert callable(Metamodelo_Cpp_CppArrayAccess.__init__)


def test_metamodelo_cpp_cpparrayaccess_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpptryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppTryExpression)


def test_metamodelo_cpp_cpptryexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppTryExpression.__init__)


def test_metamodelo_cpp_cpptryexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppTryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppjumpstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppJumpStatement)


def test_metamodelo_cpp_cppjumpstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppJumpStatement.__init__)


def test_metamodelo_cpp_cppjumpstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppJumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppconstantexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppConstantExpression)


def test_metamodelo_cpp_cppconstantexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppConstantExpression.__init__)


def test_metamodelo_cpp_cppconstantexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppnumberliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppNumberLiteral)


def test_metamodelo_cpp_cppnumberliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppNumberLiteral.__init__)


def test_metamodelo_cpp_cppnumberliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_metamodelo_cpp_cppnumberliteral_has_token():
    assert hasattr(Metamodelo_Cpp_CppNumberLiteral, "token")
    descriptor = None
    for klass in Metamodelo_Cpp_CppNumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppblock_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppBlock)


def test_metamodelo_cpp_cppblock_constructor_exists():
    assert callable(Metamodelo_Cpp_CppBlock.__init__)


def test_metamodelo_cpp_cppblock_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppBlock.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppcharacterliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppCharacterLiteral)


def test_metamodelo_cpp_cppcharacterliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppCharacterLiteral.__init__)


def test_metamodelo_cpp_cppcharacterliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppCharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_metamodelo_cpp_cppcharacterliteral_has_charValue():
    assert hasattr(Metamodelo_Cpp_CppCharacterLiteral, "charValue")
    descriptor = None
    for klass in Metamodelo_Cpp_CppCharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppdeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppDeclarationExpression)


def test_metamodelo_cpp_cppdeclarationexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppDeclarationExpression.__init__)


def test_metamodelo_cpp_cppdeclarationexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppcase_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppCase)


def test_metamodelo_cpp_cppcase_constructor_exists():
    assert callable(Metamodelo_Cpp_CppCase.__init__)


def test_metamodelo_cpp_cppcase_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppCase.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppBooleanLiteral)


def test_metamodelo_cpp_cppbooleanliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppBooleanLiteral.__init__)


def test_metamodelo_cpp_cppbooleanliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_metamodelo_cpp_cppbooleanliteral_has_booleanValue():
    assert hasattr(Metamodelo_Cpp_CppBooleanLiteral, "booleanValue")
    descriptor = None
    for klass in Metamodelo_Cpp_CppBooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cpplabeledstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppLabeledStatement)


def test_metamodelo_cpp_cpplabeledstatement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppLabeledStatement.__init__)


def test_metamodelo_cpp_cpplabeledstatement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvariableaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVariableAccess)


def test_metamodelo_cpp_cppvariableaccess_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVariableAccess.__init__)


def test_metamodelo_cpp_cppvariableaccess_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppBinaryExpression)


def test_metamodelo_cpp_cppbinaryexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppBinaryExpression.__init__)


def test_metamodelo_cpp_cppbinaryexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppthisexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppThisExpression)


def test_metamodelo_cpp_cppthisexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppThisExpression.__init__)


def test_metamodelo_cpp_cppthisexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppstringliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppStringLiteral)


def test_metamodelo_cpp_cppstringliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppStringLiteral.__init__)


def test_metamodelo_cpp_cppstringliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_metamodelo_cpp_cppstringliteral_has_literalValue():
    assert hasattr(Metamodelo_Cpp_CppStringLiteral, "literalValue")
    descriptor = None
    for klass in Metamodelo_Cpp_CppStringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppcastexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppCastExpression)


def test_metamodelo_cpp_cppcastexpression_constructor_exists():
    assert callable(Metamodelo_Cpp_CppCastExpression.__init__)


def test_metamodelo_cpp_cppcastexpression_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppregexliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppRegexLiteral)


def test_metamodelo_cpp_cppregexliteral_constructor_exists():
    assert callable(Metamodelo_Cpp_CppRegexLiteral.__init__)


def test_metamodelo_cpp_cppregexliteral_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppRegexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "options" in params, "Missing parameter 'options'"
    assert "pattern" in params, "Missing parameter 'pattern'"

def test_metamodelo_cpp_cppregexliteral_has_options():
    assert hasattr(Metamodelo_Cpp_CppRegexLiteral, "options")
    descriptor = None
    for klass in Metamodelo_Cpp_CppRegexLiteral.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppregexliteral_has_pattern():
    assert hasattr(Metamodelo_Cpp_CppRegexLiteral, "pattern")
    descriptor = None
    for klass in Metamodelo_Cpp_CppRegexLiteral.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cpparrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppArrayInitializer)


def test_metamodelo_cpp_cpparrayinitializer_constructor_exists():
    assert callable(Metamodelo_Cpp_CppArrayInitializer.__init__)


def test_metamodelo_cpp_cpparrayinitializer_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_cpptypedelement_is_not_abstract():
    assert not inspect.isabstract(CppTypedElement)


def test_cpptypedelement_constructor_exists():
    assert callable(CppTypedElement.__init__)


def test_cpptypedelement_constructor_args():
    sig = inspect.signature(CppTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvariabledeclarationgroup_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVariableDeclarationGroup)


def test_metamodelo_cpp_cppvariabledeclarationgroup_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVariableDeclarationGroup.__init__)


def test_metamodelo_cpp_cppvariabledeclarationgroup_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVariableDeclarationGroup.__init__)
    params = list(sig.parameters.keys())



def test_cppfield_is_not_abstract():
    assert not inspect.isabstract(CppField)


def test_cppfield_constructor_exists():
    assert callable(CppField.__init__)


def test_cppfield_constructor_args():
    sig = inspect.signature(CppField.__init__)
    params = list(sig.parameters.keys())



def test_cppvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(CppVariableDeclaration)


def test_cppvariabledeclaration_constructor_exists():
    assert callable(CppVariableDeclaration.__init__)


def test_cppvariabledeclaration_constructor_args():
    sig = inspect.signature(CppVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSingleVariableDeclaration)


def test_metamodelo_cpp_cppsinglevariabledeclaration_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSingleVariableDeclaration.__init__)


def test_metamodelo_cpp_cppsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVariableDeclarationFragment)


def test_metamodelo_cpp_cppvariabledeclarationfragment_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVariableDeclarationFragment.__init__)


def test_metamodelo_cpp_cppvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_cppabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(CppAbstractMethodInvocation)


def test_cppabstractmethodinvocation_constructor_exists():
    assert callable(CppAbstractMethodInvocation.__init__)


def test_cppabstractmethodinvocation_constructor_args():
    sig = inspect.signature(CppAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppsupermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSuperMethodInvocation)


def test_metamodelo_cpp_cppsupermethodinvocation_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSuperMethodInvocation.__init__)


def test_metamodelo_cpp_cppsupermethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppMethodInvocation)


def test_metamodelo_cpp_cppmethodinvocation_constructor_exists():
    assert callable(Metamodelo_Cpp_CppMethodInvocation.__init__)


def test_metamodelo_cpp_cppmethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppAbstractMethodInvocation)


def test_metamodelo_cpp_cppabstractmethodinvocation_constructor_exists():
    assert callable(Metamodelo_Cpp_CppAbstractMethodInvocation.__init__)


def test_metamodelo_cpp_cppabstractmethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_cppmemberfunction_is_not_abstract():
    assert not inspect.isabstract(CppMemberFunction)


def test_cppmemberfunction_constructor_exists():
    assert callable(CppMemberFunction.__init__)


def test_cppmemberfunction_constructor_args():
    sig = inspect.signature(CppMemberFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppmethod_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppMethod)


def test_metamodelo_cpp_cppmethod_constructor_exists():
    assert callable(Metamodelo_Cpp_CppMethod.__init__)


def test_metamodelo_cpp_cppmethod_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isPureVirtual" in params, "Missing parameter 'isPureVirtual'"
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"

def test_metamodelo_cpp_cppmethod_has_isConst():
    assert hasattr(Metamodelo_Cpp_CppMethod, "isConst")
    descriptor = None
    for klass in Metamodelo_Cpp_CppMethod.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppmethod_has_isPureVirtual():
    assert hasattr(Metamodelo_Cpp_CppMethod, "isPureVirtual")
    descriptor = None
    for klass in Metamodelo_Cpp_CppMethod.__mro__:
        if "isPureVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isPureVirtual"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppmethod_has_isVirtual():
    assert hasattr(Metamodelo_Cpp_CppMethod, "isVirtual")
    descriptor = None
    for klass in Metamodelo_Cpp_CppMethod.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppmethod_has_isFinal():
    assert hasattr(Metamodelo_Cpp_CppMethod, "isFinal")
    descriptor = None
    for klass in Metamodelo_Cpp_CppMethod.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppdestructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppDestructor)


def test_metamodelo_cpp_cppdestructor_constructor_exists():
    assert callable(Metamodelo_Cpp_CppDestructor.__init__)


def test_metamodelo_cpp_cppdestructor_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppDestructor.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_metamodelo_cpp_cppdestructor_has_isVirtual():
    assert hasattr(Metamodelo_Cpp_CppDestructor, "isVirtual")
    descriptor = None
    for klass in Metamodelo_Cpp_CppDestructor.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppconstructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppConstructor)


def test_metamodelo_cpp_cppconstructor_constructor_exists():
    assert callable(Metamodelo_Cpp_CppConstructor.__init__)


def test_metamodelo_cpp_cppconstructor_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppConstructor.__init__)
    params = list(sig.parameters.keys())



def test_cppfunction_is_not_abstract():
    assert not inspect.isabstract(CppFunction)


def test_cppfunction_constructor_exists():
    assert callable(CppFunction.__init__)


def test_cppfunction_constructor_args():
    sig = inspect.signature(CppFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppmemberfunction_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppMemberFunction)


def test_metamodelo_cpp_cppmemberfunction_constructor_exists():
    assert callable(Metamodelo_Cpp_CppMemberFunction.__init__)


def test_metamodelo_cpp_cppmemberfunction_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppMemberFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpptypedelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppTypedElement)


def test_metamodelo_cpp_cpptypedelement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppTypedElement.__init__)


def test_metamodelo_cpp_cpptypedelement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppclassifier_is_not_abstract():
    assert not inspect.isabstract(CppClassifier)


def test_cppclassifier_constructor_exists():
    assert callable(CppClassifier.__init__)


def test_cppclassifier_constructor_args():
    sig = inspect.signature(CppClassifier.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppclass_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppClass)


def test_metamodelo_cpp_cppclass_constructor_exists():
    assert callable(Metamodelo_Cpp_CppClass.__init__)


def test_metamodelo_cpp_cppclass_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppClass.__init__)
    params = list(sig.parameters.keys())
    assert "classkey" in params, "Missing parameter 'classkey'"
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isGeneric" in params, "Missing parameter 'isGeneric'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_metamodelo_cpp_cppclass_has_classkey():
    assert hasattr(Metamodelo_Cpp_CppClass, "classkey")
    descriptor = None
    for klass in Metamodelo_Cpp_CppClass.__mro__:
        if "classkey" in klass.__dict__:
            descriptor = klass.__dict__["classkey"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppclass_has_isFinal():
    assert hasattr(Metamodelo_Cpp_CppClass, "isFinal")
    descriptor = None
    for klass in Metamodelo_Cpp_CppClass.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppclass_has_isGeneric():
    assert hasattr(Metamodelo_Cpp_CppClass, "isGeneric")
    descriptor = None
    for klass in Metamodelo_Cpp_CppClass.__mro__:
        if "isGeneric" in klass.__dict__:
            descriptor = klass.__dict__["isGeneric"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppclass_has_isAbstract():
    assert hasattr(Metamodelo_Cpp_CppClass, "isAbstract")
    descriptor = None
    for klass in Metamodelo_Cpp_CppClass.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_cppprimitivetype_is_not_abstract():
    assert not inspect.isabstract(CppPrimitiveType)


def test_cppprimitivetype_constructor_exists():
    assert callable(CppPrimitiveType.__init__)


def test_cppprimitivetype_constructor_args():
    sig = inspect.signature(CppPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppfloattype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppFloatType)


def test_metamodelo_cpp_cppfloattype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppFloatType.__init__)


def test_metamodelo_cpp_cppfloattype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppFloatType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppunsignedtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppUnsignedType)


def test_metamodelo_cpp_cppunsignedtype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppUnsignedType.__init__)


def test_metamodelo_cpp_cppunsignedtype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppUnsignedType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvoidtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVoidType)


def test_metamodelo_cpp_cppvoidtype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVoidType.__init__)


def test_metamodelo_cpp_cppvoidtype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVoidType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppsignedtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppSignedType)


def test_metamodelo_cpp_cppsignedtype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppSignedType.__init__)


def test_metamodelo_cpp_cppsignedtype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppSignedType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpplongtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppLongType)


def test_metamodelo_cpp_cpplongtype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppLongType.__init__)


def test_metamodelo_cpp_cpplongtype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppLongType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppdoubletype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppDoubleType)


def test_metamodelo_cpp_cppdoubletype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppDoubleType.__init__)


def test_metamodelo_cpp_cppdoubletype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppDoubleType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppshorttype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppShortType)


def test_metamodelo_cpp_cppshorttype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppShortType.__init__)


def test_metamodelo_cpp_cppshorttype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppShortType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppchartype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppCharType)


def test_metamodelo_cpp_cppchartype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppCharType.__init__)


def test_metamodelo_cpp_cppchartype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppCharType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppinttype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppIntType)


def test_metamodelo_cpp_cppinttype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppIntType.__init__)


def test_metamodelo_cpp_cppinttype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppIntType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppbooleantype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppBooleanType)


def test_metamodelo_cpp_cppbooleantype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppBooleanType.__init__)


def test_metamodelo_cpp_cppbooleantype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppBooleanType.__init__)
    params = list(sig.parameters.keys())



def test_cpptype_is_not_abstract():
    assert not inspect.isabstract(CppType)


def test_cpptype_constructor_exists():
    assert callable(CppType.__init__)


def test_cpptype_constructor_args():
    sig = inspect.signature(CppType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppvariable_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppVariable)


def test_metamodelo_cpp_cppvariable_constructor_exists():
    assert callable(Metamodelo_Cpp_CppVariable.__init__)


def test_metamodelo_cpp_cppvariable_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "storage" in params, "Missing parameter 'storage'"

def test_metamodelo_cpp_cppvariable_has_isConst():
    assert hasattr(Metamodelo_Cpp_CppVariable, "isConst")
    descriptor = None
    for klass in Metamodelo_Cpp_CppVariable.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppvariable_has_storage():
    assert hasattr(Metamodelo_Cpp_CppVariable, "storage")
    descriptor = None
    for klass in Metamodelo_Cpp_CppVariable.__mro__:
        if "storage" in klass.__dict__:
            descriptor = klass.__dict__["storage"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppenum_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppEnum)


def test_metamodelo_cpp_cppenum_constructor_exists():
    assert callable(Metamodelo_Cpp_CppEnum.__init__)


def test_metamodelo_cpp_cppenum_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppEnum.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppclassifier_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppClassifier)


def test_metamodelo_cpp_cppclassifier_constructor_exists():
    assert callable(Metamodelo_Cpp_CppClassifier.__init__)


def test_metamodelo_cpp_cppclassifier_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppClassifier.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppfunction_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppFunction)


def test_metamodelo_cpp_cppfunction_constructor_exists():
    assert callable(Metamodelo_Cpp_CppFunction.__init__)


def test_metamodelo_cpp_cppfunction_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppFunction.__init__)
    params = list(sig.parameters.keys())
    assert "isVarArg" in params, "Missing parameter 'isVarArg'"
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "linkage" in params, "Missing parameter 'linkage'"

def test_metamodelo_cpp_cppfunction_has_isVarArg():
    assert hasattr(Metamodelo_Cpp_CppFunction, "isVarArg")
    descriptor = None
    for klass in Metamodelo_Cpp_CppFunction.__mro__:
        if "isVarArg" in klass.__dict__:
            descriptor = klass.__dict__["isVarArg"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppfunction_has_isInline():
    assert hasattr(Metamodelo_Cpp_CppFunction, "isInline")
    descriptor = None
    for klass in Metamodelo_Cpp_CppFunction.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo_cpp_cppfunction_has_linkage():
    assert hasattr(Metamodelo_Cpp_CppFunction, "linkage")
    descriptor = None
    for klass in Metamodelo_Cpp_CppFunction.__mro__:
        if "linkage" in klass.__dict__:
            descriptor = klass.__dict__["linkage"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo_cpp_cppprimitivetype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppPrimitiveType)


def test_metamodelo_cpp_cppprimitivetype_constructor_exists():
    assert callable(Metamodelo_Cpp_CppPrimitiveType.__init__)


def test_metamodelo_cpp_cppprimitivetype_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpptypeparameter_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppTypeParameter)


def test_metamodelo_cpp_cpptypeparameter_constructor_exists():
    assert callable(Metamodelo_Cpp_CppTypeParameter.__init__)


def test_metamodelo_cpp_cpptypeparameter_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cpptypeaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppTypeAccess)


def test_metamodelo_cpp_cpptypeaccess_constructor_exists():
    assert callable(Metamodelo_Cpp_CppTypeAccess.__init__)


def test_metamodelo_cpp_cpptypeaccess_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppImportDeclaration)


def test_metamodelo_cpp_cppimportdeclaration_constructor_exists():
    assert callable(Metamodelo_Cpp_CppImportDeclaration.__init__)


def test_metamodelo_cpp_cppimportdeclaration_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo_cpp_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo_Cpp_CppNamedElement)


def test_metamodelo_cpp_cppnamedelement_constructor_exists():
    assert callable(Metamodelo_Cpp_CppNamedElement.__init__)


def test_metamodelo_cpp_cppnamedelement_constructor_args():
    sig = inspect.signature(Metamodelo_Cpp_CppNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodelo_cpp_cppnamedelement_has_name():
    assert hasattr(Metamodelo_Cpp_CppNamedElement, "name")
    descriptor = None
    for klass in Metamodelo_Cpp_CppNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cpplinkagespecifier_exists():
    # Check that the Enumeration exists
    assert CppLinkageSpecifier is not None

def test_cpplinkagespecifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppLinkageSpecifier]
    expected_literals = [
        "EXTERN",
        "STATIC",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppLinkageSpecifier"

def test_cppclasskey_exists():
    # Check that the Enumeration exists
    assert CppClassKey is not None

def test_cppclasskey_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppClassKey]
    expected_literals = [
        "UNION",
        "CLASS",
        "STRUCT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppClassKey"

def test_cppoperator_exists():
    # Check that the Enumeration exists
    assert CppOperator is not None

def test_cppoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppOperator]
    expected_literals = [
        "PLUS",
        "SHIFT_RIGHT",
        "TIMES",
        "GREATER_EQUALS",
        "LESS_THAN",
        "REMAINDER",
        "EQUALS",
        "SHIFT_LEFT",
        "XOR_EQ",
        "XOR",
        "OR",
        "BIT_OR",
        "LESS_EQUALS",
        "MINUS",
        "BIT_AND",
        "GREATER_THAN",
        "AND",
        "NOT_EQUALS",
        "DIVISION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppOperator"

def test_cppstoragetype_exists():
    # Check that the Enumeration exists
    assert CppStorageType is not None

def test_cppstoragetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppStorageType]
    expected_literals = [
        "TYPEDEF",
        "STATIC",
        "AUTO",
        "EXTERN",
        "REGISTER",
        "THREAD_LOCAL",
        "MUTABLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppStorageType"

def test_cppaccessspecifier_exists():
    # Check that the Enumeration exists
    assert CppAccessSpecifier is not None

def test_cppaccessspecifier_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppAccessSpecifier]
    expected_literals = [
        "PRIVATE",
        "PUBLIC",
        "PROTECTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppAccessSpecifier"

def test_cpppostfixoperator_exists():
    # Check that the Enumeration exists
    assert CppPostfixOperator is not None

def test_cpppostfixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppPostfixOperator]
    expected_literals = [
        "INCREMENT",
        "DECREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppPostfixOperator"

def test_cppqualifiertype_exists():
    # Check that the Enumeration exists
    assert CppQualifierType is not None

def test_cppqualifiertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppQualifierType]
    expected_literals = [
        "ATOMIC",
        "RESTRICT",
        "CONST",
        "VOLATILE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppQualifierType"

def test_cppassignmentoperator_exists():
    # Check that the Enumeration exists
    assert CppAssignmentOperator is not None

def test_cppassignmentoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppAssignmentOperator]
    expected_literals = [
        "DIVISSION_ASSIGN",
        "PLUS_ASSIGN",
        "SHIFT_RIGHT_ASSIGN",
        "MINUS_ASSIGN",
        "MODULO_ASSIGN",
        "ASSIGN",
        "TIMES_ASSIGN",
        "XOR_ASSIGN",
        "AND_ASSIGN",
        "SHIFT_LEFT_ASSIGN",
        "OR_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppAssignmentOperator"

def test_cppvartype_exists():
    # Check that the Enumeration exists
    assert CppVarType is not None

def test_cppvartype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppVarType]
    expected_literals = [
        "POINTER",
        "OBJECT",
        "REFERENCE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppVarType"

def test_cppunaryoperator_exists():
    # Check that the Enumeration exists
    assert CppUnaryOperator is not None

def test_cppunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppUnaryOperator]
    expected_literals = [
        "BIT_NOT",
        "DECREMENT",
        "AMPERSAND",
        "PLUS",
        "ASTERISK",
        "MINUS",
        "NOT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppUnaryOperator"


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
Metamodelo_Cpp_CppModelElement_strategy = st.builds(
    Metamodelo_Cpp_CppModelElement,
)
CppFieldContainer_strategy = st.builds(
    CppFieldContainer,
)
Metamodelo_Cpp_CppModel_strategy = st.builds(
    Metamodelo_Cpp_CppModel,
    name=
        safe_text,
    sourceFolder=
        safe_text,
    targetFolder=
        safe_text
)
CppPathReferentiable_strategy = st.builds(
    CppPathReferentiable,
)
CppModelElement_strategy = st.builds(
    CppModelElement,
)
Metamodelo_Cpp_CppComment_strategy = st.builds(
    Metamodelo_Cpp_CppComment,
    content=
        safe_text,
    multiLine=
        st.booleans(),
    singleLine=
        st.booleans()
)
Metamodelo_Cpp_CppExpression_strategy = st.builds(
    Metamodelo_Cpp_CppExpression,
)
Metamodelo_Cpp_CppPathReference_strategy = st.builds(
    Metamodelo_Cpp_CppPathReference,
)
Metamodelo_Cpp_CppPackage_strategy = st.builds(
    Metamodelo_Cpp_CppPackage,
)
CppNamedElement_strategy = st.builds(
    CppNamedElement,
)
Metamodelo_Cpp_CppEnumConstructor_strategy = st.builds(
    Metamodelo_Cpp_CppEnumConstructor,
)
Metamodelo_Cpp_CppPathReferentiable_strategy = st.builds(
    Metamodelo_Cpp_CppPathReferentiable,
)
Metamodelo_Cpp_CppClassFile_strategy = st.builds(
    Metamodelo_Cpp_CppClassFile,
)
Metamodelo_Cpp_CppType_strategy = st.builds(
    Metamodelo_Cpp_CppType,
)
Metamodelo_Cpp_CppVariableDeclaration_strategy = st.builds(
    Metamodelo_Cpp_CppVariableDeclaration,
    vartype=
        safe_text,
    isArray=
        st.booleans()
)
Metamodelo_Cpp_CppFieldContainer_strategy = st.builds(
    Metamodelo_Cpp_CppFieldContainer,
)
Metamodelo_Cpp_CppField_strategy = st.builds(
    Metamodelo_Cpp_CppField,
    accessSpecifier=
        safe_text
)
CppBinaryExpression_strategy = st.builds(
    CppBinaryExpression,
)
Metamodelo_Cpp_CppAssignamentStatement_strategy = st.builds(
    Metamodelo_Cpp_CppAssignamentStatement,
    operator=
        safe_text
)
CppUnaryExpression_strategy = st.builds(
    CppUnaryExpression,
)
Metamodelo_Cpp_CppPrefixExpression_strategy = st.builds(
    Metamodelo_Cpp_CppPrefixExpression,
    operator=
        safe_text
)
Metamodelo_Cpp_CppPostfixExpression_strategy = st.builds(
    Metamodelo_Cpp_CppPostfixExpression,
    operator=
        safe_text
)
Metamodelo_Cpp_CppInfixExpression_strategy = st.builds(
    Metamodelo_Cpp_CppInfixExpression,
    operator=
        safe_text
)
CppSelectionStatement_strategy = st.builds(
    CppSelectionStatement,
)
Metamodelo_Cpp_CppIfElseStatement_strategy = st.builds(
    Metamodelo_Cpp_CppIfElseStatement,
    inLine=
        st.booleans()
)
Metamodelo_Cpp_CppIfStatement_strategy = st.builds(
    Metamodelo_Cpp_CppIfStatement,
)
CppMethodInvocation_strategy = st.builds(
    CppMethodInvocation,
)
Metamodelo_Cpp_CppSuperConstructorInvocation_strategy = st.builds(
    Metamodelo_Cpp_CppSuperConstructorInvocation,
)
CppJumpStatement_strategy = st.builds(
    CppJumpStatement,
)
Metamodelo_Cpp_CppContinueStatement_strategy = st.builds(
    Metamodelo_Cpp_CppContinueStatement,
)
Metamodelo_Cpp_CppReturnStatement_strategy = st.builds(
    Metamodelo_Cpp_CppReturnStatement,
)
Metamodelo_Cpp_CppGotoStatement_strategy = st.builds(
    Metamodelo_Cpp_CppGotoStatement,
)
Metamodelo_Cpp_CppBreakStatement_strategy = st.builds(
    Metamodelo_Cpp_CppBreakStatement,
)
CppIterationStatement_strategy = st.builds(
    CppIterationStatement,
)
Metamodelo_Cpp_CppForStatement_strategy = st.builds(
    Metamodelo_Cpp_CppForStatement,
)
Metamodelo_Cpp_CppDoWhileStatement_strategy = st.builds(
    Metamodelo_Cpp_CppDoWhileStatement,
)
Metamodelo_Cpp_CppWhileStatement_strategy = st.builds(
    Metamodelo_Cpp_CppWhileStatement,
)
CppExpression_strategy = st.builds(
    CppExpression,
)
Metamodelo_Cpp_CppCatchClause_strategy = st.builds(
    Metamodelo_Cpp_CppCatchClause,
)
Metamodelo_Cpp_CppSelectionStatement_strategy = st.builds(
    Metamodelo_Cpp_CppSelectionStatement,
)
Metamodelo_Cpp_CppFieldAccess_strategy = st.builds(
    Metamodelo_Cpp_CppFieldAccess,
)
Metamodelo_Cpp_CppThrowExpression_strategy = st.builds(
    Metamodelo_Cpp_CppThrowExpression,
)
Metamodelo_Cpp_CppNullLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppNullLiteral,
)
Metamodelo_Cpp_CppParenthizedExpression_strategy = st.builds(
    Metamodelo_Cpp_CppParenthizedExpression,
)
Metamodelo_Cpp_CppUnaryExpression_strategy = st.builds(
    Metamodelo_Cpp_CppUnaryExpression,
)
Metamodelo_Cpp_CppIterationStatement_strategy = st.builds(
    Metamodelo_Cpp_CppIterationStatement,
)
Metamodelo_Cpp_CppSwitchExpression_strategy = st.builds(
    Metamodelo_Cpp_CppSwitchExpression,
)
Metamodelo_Cpp_CppArrayAccess_strategy = st.builds(
    Metamodelo_Cpp_CppArrayAccess,
)
Metamodelo_Cpp_CppTryExpression_strategy = st.builds(
    Metamodelo_Cpp_CppTryExpression,
)
Metamodelo_Cpp_CppJumpStatement_strategy = st.builds(
    Metamodelo_Cpp_CppJumpStatement,
)
Metamodelo_Cpp_CppConstantExpression_strategy = st.builds(
    Metamodelo_Cpp_CppConstantExpression,
)
Metamodelo_Cpp_CppNumberLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppNumberLiteral,
    token=
        safe_text
)
Metamodelo_Cpp_CppBlock_strategy = st.builds(
    Metamodelo_Cpp_CppBlock,
)
Metamodelo_Cpp_CppCharacterLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppCharacterLiteral,
    charValue=
        safe_text
)
Metamodelo_Cpp_CppDeclarationExpression_strategy = st.builds(
    Metamodelo_Cpp_CppDeclarationExpression,
)
Metamodelo_Cpp_CppCase_strategy = st.builds(
    Metamodelo_Cpp_CppCase,
)
Metamodelo_Cpp_CppBooleanLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppBooleanLiteral,
    booleanValue=
        st.booleans()
)
Metamodelo_Cpp_CppLabeledStatement_strategy = st.builds(
    Metamodelo_Cpp_CppLabeledStatement,
)
Metamodelo_Cpp_CppVariableAccess_strategy = st.builds(
    Metamodelo_Cpp_CppVariableAccess,
)
Metamodelo_Cpp_CppBinaryExpression_strategy = st.builds(
    Metamodelo_Cpp_CppBinaryExpression,
)
Metamodelo_Cpp_CppThisExpression_strategy = st.builds(
    Metamodelo_Cpp_CppThisExpression,
)
Metamodelo_Cpp_CppStringLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppStringLiteral,
    literalValue=
        safe_text
)
Metamodelo_Cpp_CppCastExpression_strategy = st.builds(
    Metamodelo_Cpp_CppCastExpression,
)
Metamodelo_Cpp_CppRegexLiteral_strategy = st.builds(
    Metamodelo_Cpp_CppRegexLiteral,
    options=
        safe_text,
    pattern=
        safe_text
)
Metamodelo_Cpp_CppArrayInitializer_strategy = st.builds(
    Metamodelo_Cpp_CppArrayInitializer,
)
CppTypedElement_strategy = st.builds(
    CppTypedElement,
)
Metamodelo_Cpp_CppVariableDeclarationGroup_strategy = st.builds(
    Metamodelo_Cpp_CppVariableDeclarationGroup,
)
CppField_strategy = st.builds(
    CppField,
)
CppVariableDeclaration_strategy = st.builds(
    CppVariableDeclaration,
)
Metamodelo_Cpp_CppSingleVariableDeclaration_strategy = st.builds(
    Metamodelo_Cpp_CppSingleVariableDeclaration,
)
Metamodelo_Cpp_CppVariableDeclarationFragment_strategy = st.builds(
    Metamodelo_Cpp_CppVariableDeclarationFragment,
)
CppAbstractMethodInvocation_strategy = st.builds(
    CppAbstractMethodInvocation,
)
Metamodelo_Cpp_CppSuperMethodInvocation_strategy = st.builds(
    Metamodelo_Cpp_CppSuperMethodInvocation,
)
Metamodelo_Cpp_CppMethodInvocation_strategy = st.builds(
    Metamodelo_Cpp_CppMethodInvocation,
)
Metamodelo_Cpp_CppAbstractMethodInvocation_strategy = st.builds(
    Metamodelo_Cpp_CppAbstractMethodInvocation,
)
CppMemberFunction_strategy = st.builds(
    CppMemberFunction,
)
Metamodelo_Cpp_CppMethod_strategy = st.builds(
    Metamodelo_Cpp_CppMethod,
    isConst=
        st.booleans(),
    isPureVirtual=
        st.booleans(),
    isVirtual=
        st.booleans(),
    isFinal=
        st.booleans()
)
Metamodelo_Cpp_CppDestructor_strategy = st.builds(
    Metamodelo_Cpp_CppDestructor,
    isVirtual=
        st.booleans()
)
Metamodelo_Cpp_CppConstructor_strategy = st.builds(
    Metamodelo_Cpp_CppConstructor,
)
CppFunction_strategy = st.builds(
    CppFunction,
)
Metamodelo_Cpp_CppMemberFunction_strategy = st.builds(
    Metamodelo_Cpp_CppMemberFunction,
)
Metamodelo_Cpp_CppTypedElement_strategy = st.builds(
    Metamodelo_Cpp_CppTypedElement,
)
CppClassifier_strategy = st.builds(
    CppClassifier,
)
Metamodelo_Cpp_CppClass_strategy = st.builds(
    Metamodelo_Cpp_CppClass,
    classkey=
        safe_text,
    isFinal=
        st.booleans(),
    isGeneric=
        st.booleans(),
    isAbstract=
        st.booleans()
)
CppPrimitiveType_strategy = st.builds(
    CppPrimitiveType,
)
Metamodelo_Cpp_CppFloatType_strategy = st.builds(
    Metamodelo_Cpp_CppFloatType,
)
Metamodelo_Cpp_CppUnsignedType_strategy = st.builds(
    Metamodelo_Cpp_CppUnsignedType,
)
Metamodelo_Cpp_CppVoidType_strategy = st.builds(
    Metamodelo_Cpp_CppVoidType,
)
Metamodelo_Cpp_CppSignedType_strategy = st.builds(
    Metamodelo_Cpp_CppSignedType,
)
Metamodelo_Cpp_CppLongType_strategy = st.builds(
    Metamodelo_Cpp_CppLongType,
)
Metamodelo_Cpp_CppDoubleType_strategy = st.builds(
    Metamodelo_Cpp_CppDoubleType,
)
Metamodelo_Cpp_CppShortType_strategy = st.builds(
    Metamodelo_Cpp_CppShortType,
)
Metamodelo_Cpp_CppCharType_strategy = st.builds(
    Metamodelo_Cpp_CppCharType,
)
Metamodelo_Cpp_CppIntType_strategy = st.builds(
    Metamodelo_Cpp_CppIntType,
)
Metamodelo_Cpp_CppBooleanType_strategy = st.builds(
    Metamodelo_Cpp_CppBooleanType,
)
CppType_strategy = st.builds(
    CppType,
)
Metamodelo_Cpp_CppVariable_strategy = st.builds(
    Metamodelo_Cpp_CppVariable,
    isConst=
        st.booleans(),
    storage=
        safe_text
)
Metamodelo_Cpp_CppEnum_strategy = st.builds(
    Metamodelo_Cpp_CppEnum,
)
Metamodelo_Cpp_CppClassifier_strategy = st.builds(
    Metamodelo_Cpp_CppClassifier,
)
Metamodelo_Cpp_CppFunction_strategy = st.builds(
    Metamodelo_Cpp_CppFunction,
    isVarArg=
        st.booleans(),
    isInline=
        st.booleans(),
    linkage=
        safe_text
)
Metamodelo_Cpp_CppPrimitiveType_strategy = st.builds(
    Metamodelo_Cpp_CppPrimitiveType,
)
Metamodelo_Cpp_CppTypeParameter_strategy = st.builds(
    Metamodelo_Cpp_CppTypeParameter,
)
Metamodelo_Cpp_CppTypeAccess_strategy = st.builds(
    Metamodelo_Cpp_CppTypeAccess,
)
Metamodelo_Cpp_CppImportDeclaration_strategy = st.builds(
    Metamodelo_Cpp_CppImportDeclaration,
)
Metamodelo_Cpp_CppNamedElement_strategy = st.builds(
    Metamodelo_Cpp_CppNamedElement,
    name=
        safe_text
)

@given(instance=Metamodelo_Cpp_CppModelElement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppmodelelement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppModelElement)

@given(instance=CppFieldContainer_strategy)
@settings(max_examples=50)
def test_cppfieldcontainer_instantiation(instance):
    assert isinstance(instance, CppFieldContainer)

@given(instance=Metamodelo_Cpp_CppModel_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppmodel_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppModel)



@given(instance=Metamodelo_Cpp_CppModel_strategy)
def test_metamodelo_cpp_cppmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Metamodelo_Cpp_CppModel_strategy)
def test_metamodelo_cpp_cppmodel_sourceFolder_setter(instance):
    original = instance.sourceFolder
    instance.sourceFolder = original
    assert instance.sourceFolder == original



@given(instance=Metamodelo_Cpp_CppModel_strategy)
def test_metamodelo_cpp_cppmodel_targetFolder_setter(instance):
    original = instance.targetFolder
    instance.targetFolder = original
    assert instance.targetFolder == original

@given(instance=CppPathReferentiable_strategy)
@settings(max_examples=50)
def test_cpppathreferentiable_instantiation(instance):
    assert isinstance(instance, CppPathReferentiable)

@given(instance=CppModelElement_strategy)
@settings(max_examples=50)
def test_cppmodelelement_instantiation(instance):
    assert isinstance(instance, CppModelElement)

@given(instance=Metamodelo_Cpp_CppComment_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcomment_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppComment)



@given(instance=Metamodelo_Cpp_CppComment_strategy)
def test_metamodelo_cpp_cppcomment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original



@given(instance=Metamodelo_Cpp_CppComment_strategy)
def test_metamodelo_cpp_cppcomment_multiLine_setter(instance):
    original = instance.multiLine
    instance.multiLine = original
    assert instance.multiLine == original



@given(instance=Metamodelo_Cpp_CppComment_strategy)
def test_metamodelo_cpp_cppcomment_singleLine_setter(instance):
    original = instance.singleLine
    instance.singleLine = original
    assert instance.singleLine == original

@given(instance=Metamodelo_Cpp_CppExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppExpression)

@given(instance=Metamodelo_Cpp_CppPathReference_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpppathreference_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPathReference)

@given(instance=Metamodelo_Cpp_CppPackage_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpppackage_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPackage)

@given(instance=CppNamedElement_strategy)
@settings(max_examples=50)
def test_cppnamedelement_instantiation(instance):
    assert isinstance(instance, CppNamedElement)

@given(instance=Metamodelo_Cpp_CppEnumConstructor_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppenumconstructor_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppEnumConstructor)

@given(instance=Metamodelo_Cpp_CppPathReferentiable_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpppathreferentiable_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPathReferentiable)

@given(instance=Metamodelo_Cpp_CppClassFile_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppclassfile_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppClassFile)

@given(instance=Metamodelo_Cpp_CppType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpptype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppType)

@given(instance=Metamodelo_Cpp_CppVariableDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvariabledeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVariableDeclaration)



@given(instance=Metamodelo_Cpp_CppVariableDeclaration_strategy)
def test_metamodelo_cpp_cppvariabledeclaration_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original



@given(instance=Metamodelo_Cpp_CppVariableDeclaration_strategy)
def test_metamodelo_cpp_cppvariabledeclaration_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=Metamodelo_Cpp_CppFieldContainer_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppfieldcontainer_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppFieldContainer)

@given(instance=Metamodelo_Cpp_CppField_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppfield_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppField)



@given(instance=Metamodelo_Cpp_CppField_strategy)
def test_metamodelo_cpp_cppfield_accessSpecifier_setter(instance):
    original = instance.accessSpecifier
    instance.accessSpecifier = original
    assert instance.accessSpecifier == original

@given(instance=CppBinaryExpression_strategy)
@settings(max_examples=50)
def test_cppbinaryexpression_instantiation(instance):
    assert isinstance(instance, CppBinaryExpression)

@given(instance=Metamodelo_Cpp_CppAssignamentStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppassignamentstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppAssignamentStatement)



@given(instance=Metamodelo_Cpp_CppAssignamentStatement_strategy)
def test_metamodelo_cpp_cppassignamentstatement_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CppUnaryExpression_strategy)
@settings(max_examples=50)
def test_cppunaryexpression_instantiation(instance):
    assert isinstance(instance, CppUnaryExpression)

@given(instance=Metamodelo_Cpp_CppPrefixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppprefixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPrefixExpression)



@given(instance=Metamodelo_Cpp_CppPrefixExpression_strategy)
def test_metamodelo_cpp_cppprefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Metamodelo_Cpp_CppPostfixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpppostfixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPostfixExpression)



@given(instance=Metamodelo_Cpp_CppPostfixExpression_strategy)
def test_metamodelo_cpp_cpppostfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Metamodelo_Cpp_CppInfixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppinfixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppInfixExpression)



@given(instance=Metamodelo_Cpp_CppInfixExpression_strategy)
def test_metamodelo_cpp_cppinfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CppSelectionStatement_strategy)
@settings(max_examples=50)
def test_cppselectionstatement_instantiation(instance):
    assert isinstance(instance, CppSelectionStatement)

@given(instance=Metamodelo_Cpp_CppIfElseStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppifelsestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppIfElseStatement)



@given(instance=Metamodelo_Cpp_CppIfElseStatement_strategy)
def test_metamodelo_cpp_cppifelsestatement_inLine_setter(instance):
    original = instance.inLine
    instance.inLine = original
    assert instance.inLine == original

@given(instance=Metamodelo_Cpp_CppIfStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppifstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppIfStatement)

@given(instance=CppMethodInvocation_strategy)
@settings(max_examples=50)
def test_cppmethodinvocation_instantiation(instance):
    assert isinstance(instance, CppMethodInvocation)

@given(instance=Metamodelo_Cpp_CppSuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppsuperconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSuperConstructorInvocation)

@given(instance=CppJumpStatement_strategy)
@settings(max_examples=50)
def test_cppjumpstatement_instantiation(instance):
    assert isinstance(instance, CppJumpStatement)

@given(instance=Metamodelo_Cpp_CppContinueStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcontinuestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppContinueStatement)

@given(instance=Metamodelo_Cpp_CppReturnStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppreturnstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppReturnStatement)

@given(instance=Metamodelo_Cpp_CppGotoStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppgotostatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppGotoStatement)

@given(instance=Metamodelo_Cpp_CppBreakStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppbreakstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppBreakStatement)

@given(instance=CppIterationStatement_strategy)
@settings(max_examples=50)
def test_cppiterationstatement_instantiation(instance):
    assert isinstance(instance, CppIterationStatement)

@given(instance=Metamodelo_Cpp_CppForStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppforstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppForStatement)

@given(instance=Metamodelo_Cpp_CppDoWhileStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppdowhilestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppDoWhileStatement)

@given(instance=Metamodelo_Cpp_CppWhileStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppwhilestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppWhileStatement)

@given(instance=CppExpression_strategy)
@settings(max_examples=50)
def test_cppexpression_instantiation(instance):
    assert isinstance(instance, CppExpression)

@given(instance=Metamodelo_Cpp_CppCatchClause_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcatchclause_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppCatchClause)

@given(instance=Metamodelo_Cpp_CppSelectionStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppselectionstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSelectionStatement)

@given(instance=Metamodelo_Cpp_CppFieldAccess_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppfieldaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppFieldAccess)

@given(instance=Metamodelo_Cpp_CppThrowExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppthrowexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppThrowExpression)

@given(instance=Metamodelo_Cpp_CppNullLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppnullliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppNullLiteral)

@given(instance=Metamodelo_Cpp_CppParenthizedExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppparenthizedexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppParenthizedExpression)

@given(instance=Metamodelo_Cpp_CppUnaryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppunaryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppUnaryExpression)

@given(instance=Metamodelo_Cpp_CppIterationStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppiterationstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppIterationStatement)

@given(instance=Metamodelo_Cpp_CppSwitchExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppswitchexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSwitchExpression)

@given(instance=Metamodelo_Cpp_CppArrayAccess_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpparrayaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppArrayAccess)

@given(instance=Metamodelo_Cpp_CppTryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpptryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppTryExpression)

@given(instance=Metamodelo_Cpp_CppJumpStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppjumpstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppJumpStatement)

@given(instance=Metamodelo_Cpp_CppConstantExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppconstantexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppConstantExpression)

@given(instance=Metamodelo_Cpp_CppNumberLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppnumberliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppNumberLiteral)



@given(instance=Metamodelo_Cpp_CppNumberLiteral_strategy)
def test_metamodelo_cpp_cppnumberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=Metamodelo_Cpp_CppBlock_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppblock_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppBlock)

@given(instance=Metamodelo_Cpp_CppCharacterLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcharacterliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppCharacterLiteral)



@given(instance=Metamodelo_Cpp_CppCharacterLiteral_strategy)
def test_metamodelo_cpp_cppcharacterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=Metamodelo_Cpp_CppDeclarationExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppdeclarationexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppDeclarationExpression)

@given(instance=Metamodelo_Cpp_CppCase_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcase_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppCase)

@given(instance=Metamodelo_Cpp_CppBooleanLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppbooleanliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppBooleanLiteral)



@given(instance=Metamodelo_Cpp_CppBooleanLiteral_strategy)
def test_metamodelo_cpp_cppbooleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=Metamodelo_Cpp_CppLabeledStatement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpplabeledstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppLabeledStatement)

@given(instance=Metamodelo_Cpp_CppVariableAccess_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvariableaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVariableAccess)

@given(instance=Metamodelo_Cpp_CppBinaryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppbinaryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppBinaryExpression)

@given(instance=Metamodelo_Cpp_CppThisExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppthisexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppThisExpression)

@given(instance=Metamodelo_Cpp_CppStringLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppstringliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppStringLiteral)



@given(instance=Metamodelo_Cpp_CppStringLiteral_strategy)
def test_metamodelo_cpp_cppstringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=Metamodelo_Cpp_CppCastExpression_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppcastexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppCastExpression)

@given(instance=Metamodelo_Cpp_CppRegexLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppregexliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppRegexLiteral)



@given(instance=Metamodelo_Cpp_CppRegexLiteral_strategy)
def test_metamodelo_cpp_cppregexliteral_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original



@given(instance=Metamodelo_Cpp_CppRegexLiteral_strategy)
def test_metamodelo_cpp_cppregexliteral_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=Metamodelo_Cpp_CppArrayInitializer_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpparrayinitializer_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppArrayInitializer)

@given(instance=CppTypedElement_strategy)
@settings(max_examples=50)
def test_cpptypedelement_instantiation(instance):
    assert isinstance(instance, CppTypedElement)

@given(instance=Metamodelo_Cpp_CppVariableDeclarationGroup_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvariabledeclarationgroup_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVariableDeclarationGroup)

@given(instance=CppField_strategy)
@settings(max_examples=50)
def test_cppfield_instantiation(instance):
    assert isinstance(instance, CppField)

@given(instance=CppVariableDeclaration_strategy)
@settings(max_examples=50)
def test_cppvariabledeclaration_instantiation(instance):
    assert isinstance(instance, CppVariableDeclaration)

@given(instance=Metamodelo_Cpp_CppSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSingleVariableDeclaration)

@given(instance=Metamodelo_Cpp_CppVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVariableDeclarationFragment)

@given(instance=CppAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_cppabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, CppAbstractMethodInvocation)

@given(instance=Metamodelo_Cpp_CppSuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppsupermethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSuperMethodInvocation)

@given(instance=Metamodelo_Cpp_CppMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppmethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppMethodInvocation)

@given(instance=Metamodelo_Cpp_CppAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppAbstractMethodInvocation)

@given(instance=CppMemberFunction_strategy)
@settings(max_examples=50)
def test_cppmemberfunction_instantiation(instance):
    assert isinstance(instance, CppMemberFunction)

@given(instance=Metamodelo_Cpp_CppMethod_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppmethod_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppMethod)



@given(instance=Metamodelo_Cpp_CppMethod_strategy)
def test_metamodelo_cpp_cppmethod_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original



@given(instance=Metamodelo_Cpp_CppMethod_strategy)
def test_metamodelo_cpp_cppmethod_isPureVirtual_setter(instance):
    original = instance.isPureVirtual
    instance.isPureVirtual = original
    assert instance.isPureVirtual == original



@given(instance=Metamodelo_Cpp_CppMethod_strategy)
def test_metamodelo_cpp_cppmethod_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original



@given(instance=Metamodelo_Cpp_CppMethod_strategy)
def test_metamodelo_cpp_cppmethod_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=Metamodelo_Cpp_CppDestructor_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppdestructor_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppDestructor)



@given(instance=Metamodelo_Cpp_CppDestructor_strategy)
def test_metamodelo_cpp_cppdestructor_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=Metamodelo_Cpp_CppConstructor_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppconstructor_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppConstructor)

@given(instance=CppFunction_strategy)
@settings(max_examples=50)
def test_cppfunction_instantiation(instance):
    assert isinstance(instance, CppFunction)

@given(instance=Metamodelo_Cpp_CppMemberFunction_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppmemberfunction_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppMemberFunction)

@given(instance=Metamodelo_Cpp_CppTypedElement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpptypedelement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppTypedElement)

@given(instance=CppClassifier_strategy)
@settings(max_examples=50)
def test_cppclassifier_instantiation(instance):
    assert isinstance(instance, CppClassifier)

@given(instance=Metamodelo_Cpp_CppClass_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppclass_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppClass)



@given(instance=Metamodelo_Cpp_CppClass_strategy)
def test_metamodelo_cpp_cppclass_classkey_setter(instance):
    original = instance.classkey
    instance.classkey = original
    assert instance.classkey == original



@given(instance=Metamodelo_Cpp_CppClass_strategy)
def test_metamodelo_cpp_cppclass_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original



@given(instance=Metamodelo_Cpp_CppClass_strategy)
def test_metamodelo_cpp_cppclass_isGeneric_setter(instance):
    original = instance.isGeneric
    instance.isGeneric = original
    assert instance.isGeneric == original



@given(instance=Metamodelo_Cpp_CppClass_strategy)
def test_metamodelo_cpp_cppclass_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=CppPrimitiveType_strategy)
@settings(max_examples=50)
def test_cppprimitivetype_instantiation(instance):
    assert isinstance(instance, CppPrimitiveType)

@given(instance=Metamodelo_Cpp_CppFloatType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppfloattype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppFloatType)

@given(instance=Metamodelo_Cpp_CppUnsignedType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppunsignedtype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppUnsignedType)

@given(instance=Metamodelo_Cpp_CppVoidType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvoidtype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVoidType)

@given(instance=Metamodelo_Cpp_CppSignedType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppsignedtype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppSignedType)

@given(instance=Metamodelo_Cpp_CppLongType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpplongtype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppLongType)

@given(instance=Metamodelo_Cpp_CppDoubleType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppdoubletype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppDoubleType)

@given(instance=Metamodelo_Cpp_CppShortType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppshorttype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppShortType)

@given(instance=Metamodelo_Cpp_CppCharType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppchartype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppCharType)

@given(instance=Metamodelo_Cpp_CppIntType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppinttype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppIntType)

@given(instance=Metamodelo_Cpp_CppBooleanType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppbooleantype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppBooleanType)

@given(instance=CppType_strategy)
@settings(max_examples=50)
def test_cpptype_instantiation(instance):
    assert isinstance(instance, CppType)

@given(instance=Metamodelo_Cpp_CppVariable_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppvariable_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppVariable)



@given(instance=Metamodelo_Cpp_CppVariable_strategy)
def test_metamodelo_cpp_cppvariable_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original



@given(instance=Metamodelo_Cpp_CppVariable_strategy)
def test_metamodelo_cpp_cppvariable_storage_setter(instance):
    original = instance.storage
    instance.storage = original
    assert instance.storage == original

@given(instance=Metamodelo_Cpp_CppEnum_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppenum_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppEnum)

@given(instance=Metamodelo_Cpp_CppClassifier_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppclassifier_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppClassifier)

@given(instance=Metamodelo_Cpp_CppFunction_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppfunction_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppFunction)



@given(instance=Metamodelo_Cpp_CppFunction_strategy)
def test_metamodelo_cpp_cppfunction_isVarArg_setter(instance):
    original = instance.isVarArg
    instance.isVarArg = original
    assert instance.isVarArg == original



@given(instance=Metamodelo_Cpp_CppFunction_strategy)
def test_metamodelo_cpp_cppfunction_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original



@given(instance=Metamodelo_Cpp_CppFunction_strategy)
def test_metamodelo_cpp_cppfunction_linkage_setter(instance):
    original = instance.linkage
    instance.linkage = original
    assert instance.linkage == original

@given(instance=Metamodelo_Cpp_CppPrimitiveType_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppprimitivetype_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppPrimitiveType)

@given(instance=Metamodelo_Cpp_CppTypeParameter_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpptypeparameter_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppTypeParameter)

@given(instance=Metamodelo_Cpp_CppTypeAccess_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cpptypeaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppTypeAccess)

@given(instance=Metamodelo_Cpp_CppImportDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppimportdeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppImportDeclaration)

@given(instance=Metamodelo_Cpp_CppNamedElement_strategy)
@settings(max_examples=50)
def test_metamodelo_cpp_cppnamedelement_instantiation(instance):
    assert isinstance(instance, Metamodelo_Cpp_CppNamedElement)



@given(instance=Metamodelo_Cpp_CppNamedElement_strategy)
def test_metamodelo_cpp_cppnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
