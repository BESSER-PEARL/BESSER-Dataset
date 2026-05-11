import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CppFieldContainer,
    Metamodelo::Cpp::CppModel,
    CppPathReferentiable,
    CppModelElement,
    Metamodelo::Cpp::CppPathReference,
    Metamodelo::Cpp::CppPackage,
    CppNamedElement,
    Metamodelo::Cpp::CppPathReferentiable,
    Metamodelo::Cpp::CppClassFile,
    Metamodelo::Cpp::CppType,
    Metamodelo::Cpp::CppVariableDeclaration,
    Metamodelo::Cpp::CppFieldContainer,
    Metamodelo::Cpp::CppField,
    CppBinaryExpression,
    Metamodelo::Cpp::CppAssignamentStatement,
    CppUnaryExpression,
    Metamodelo::Cpp::CppPrefixExpression,
    Metamodelo::Cpp::CppPostfixExpression,
    Metamodelo::Cpp::CppInfixExpression,
    CppSelectionStatement,
    Metamodelo::Cpp::CppIfElseStatement,
    Metamodelo::Cpp::CppIfStatement,
    CppMethodInvocation,
    Metamodelo::Cpp::CppSuperConstructorInvocation,
    CppJumpStatement,
    Metamodelo::Cpp::CppGotoStatement,
    Metamodelo::Cpp::CppContinueStatement,
    Metamodelo::Cpp::CppReturnStatement,
    Metamodelo::Cpp::CppBreakStatement,
    CppIterationStatement,
    Metamodelo::Cpp::CppForStatement,
    Metamodelo::Cpp::CppDoWhileStatement,
    Metamodelo::Cpp::CppWhileStatement,
    CppExpression,
    Metamodelo::Cpp::CppUnaryExpression,
    Metamodelo::Cpp::CppBooleanLiteral,
    Metamodelo::Cpp::CppBinaryExpression,
    Metamodelo::Cpp::CppTryExpression,
    Metamodelo::Cpp::CppIterationStatement,
    Metamodelo::Cpp::CppThisExpression,
    Metamodelo::Cpp::CppThrowExpression,
    Metamodelo::Cpp::CppJumpStatement,
    Metamodelo::Cpp::CppSwitchExpression,
    Metamodelo::Cpp::CppFieldAccess,
    Metamodelo::Cpp::CppNullLiteral,
    Metamodelo::Cpp::CppVariableAccess,
    Metamodelo::Cpp::CppCastExpression,
    Metamodelo::Cpp::CppConstantExpression,
    Metamodelo::Cpp::CppRegexLiteral,
    Metamodelo::Cpp::CppCharacterLiteral,
    Metamodelo::Cpp::CppCase,
    Metamodelo::Cpp::CppDeclarationExpression,
    Metamodelo::Cpp::CppCatchClause,
    Metamodelo::Cpp::CppNumberLiteral,
    Metamodelo::Cpp::CppParenthizedExpression,
    Metamodelo::Cpp::CppLabeledStatement,
    Metamodelo::Cpp::CppArrayAccess,
    Metamodelo::Cpp::CppBlock,
    Metamodelo::Cpp::CppStringLiteral,
    Metamodelo::Cpp::CppSelectionStatement,
    Metamodelo::Cpp::CppArrayInitializer,
    CppTypedElement,
    Metamodelo::Cpp::CppVariableDeclarationGroup,
    CppField,
    CppVariableDeclaration,
    Metamodelo::Cpp::CppSingleVariableDeclaration,
    Metamodelo::Cpp::CppVariableDeclarationFragment,
    CppAbstractMethodInvocation,
    Metamodelo::Cpp::CppSuperMethodInvocation,
    Metamodelo::Cpp::CppMethodInvocation,
    Metamodelo::Cpp::CppAbstractMethodInvocation,
    CppMemberFunction,
    Metamodelo::Cpp::CppMethod,
    Metamodelo::Cpp::CppDestructor,
    Metamodelo::Cpp::CppConstructor,
    CppFunction,
    Metamodelo::Cpp::CppMemberFunction,
    Metamodelo::Cpp::CppTypedElement,
    CppClassifier,
    Metamodelo::Cpp::CppClass,
    CppPrimitiveType,
    Metamodelo::Cpp::CppLongType,
    Metamodelo::Cpp::CppUnsignedType,
    Metamodelo::Cpp::CppFloatType,
    Metamodelo::Cpp::CppVoidType,
    Metamodelo::Cpp::CppSignedType,
    Metamodelo::Cpp::CppShortType,
    Metamodelo::Cpp::CppDoubleType,
    Metamodelo::Cpp::CppCharType,
    Metamodelo::Cpp::CppIntType,
    Metamodelo::Cpp::CppBooleanType,
    CppType,
    Metamodelo::Cpp::CppFunction,
    Metamodelo::Cpp::CppClassifier,
    Metamodelo::Cpp::CppPrimitiveType,
    Metamodelo::Cpp::CppTypeParameter,
    Metamodelo::Cpp::CppTypeAccess,
    Metamodelo::Cpp::CppImportDeclaration,
    Metamodelo::Cpp::CppNamedElement,
    Metamodelo::Cpp::CppModelElement,
    Metamodelo::Cpp::CppComment,
    Metamodelo::Cpp::CppExpression,
    Metamodelo::Cpp::CppEnumConstructor,
    Metamodelo::Cpp::CppEnum,
    Metamodelo::Cpp::CppVariable,
    CppLinkageSpecifier,
    CppQualifierType,
    CppAssignmentOperator,
    CppStorageType,
    CppOperator,
    CppUnaryOperator,
    CppPostfixOperator,
    CppAccessSpecifier,
    CppClassKey,
    CppVarType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cppfieldcontainer_is_not_abstract():
    assert not inspect.isabstract(CppFieldContainer)


def test_cppfieldcontainer_constructor_exists():
    assert callable(CppFieldContainer.__init__)


def test_cppfieldcontainer_constructor_args():
    sig = inspect.signature(CppFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppmodel_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppModel)


def test_metamodelo::cpp::cppmodel_constructor_exists():
    assert callable(Metamodelo::Cpp::CppModel.__init__)


def test_metamodelo::cpp::cppmodel_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppModel.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "targetFolder" in params, "Missing parameter 'targetFolder'"
    assert "sourceFolder" in params, "Missing parameter 'sourceFolder'"

def test_metamodelo::cpp::cppmodel_has_name():
    assert hasattr(Metamodelo::Cpp::CppModel, "name")
    descriptor = None
    for klass in Metamodelo::Cpp::CppModel.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppmodel_has_targetFolder():
    assert hasattr(Metamodelo::Cpp::CppModel, "targetFolder")
    descriptor = None
    for klass in Metamodelo::Cpp::CppModel.__mro__:
        if "targetFolder" in klass.__dict__:
            descriptor = klass.__dict__["targetFolder"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppmodel_has_sourceFolder():
    assert hasattr(Metamodelo::Cpp::CppModel, "sourceFolder")
    descriptor = None
    for klass in Metamodelo::Cpp::CppModel.__mro__:
        if "sourceFolder" in klass.__dict__:
            descriptor = klass.__dict__["sourceFolder"]
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



def test_metamodelo::cpp::cpppathreference_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPathReference)


def test_metamodelo::cpp::cpppathreference_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPathReference.__init__)


def test_metamodelo::cpp::cpppathreference_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPathReference.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpppackage_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPackage)


def test_metamodelo::cpp::cpppackage_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPackage.__init__)


def test_metamodelo::cpp::cpppackage_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPackage.__init__)
    params = list(sig.parameters.keys())



def test_cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(CppNamedElement)


def test_cppnamedelement_constructor_exists():
    assert callable(CppNamedElement.__init__)


def test_cppnamedelement_constructor_args():
    sig = inspect.signature(CppNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpppathreferentiable_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPathReferentiable)


def test_metamodelo::cpp::cpppathreferentiable_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPathReferentiable.__init__)


def test_metamodelo::cpp::cpppathreferentiable_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPathReferentiable.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppclassfile_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppClassFile)


def test_metamodelo::cpp::cppclassfile_constructor_exists():
    assert callable(Metamodelo::Cpp::CppClassFile.__init__)


def test_metamodelo::cpp::cppclassfile_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppClassFile.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpptype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppType)


def test_metamodelo::cpp::cpptype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppType.__init__)


def test_metamodelo::cpp::cpptype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVariableDeclaration)


def test_metamodelo::cpp::cppvariabledeclaration_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVariableDeclaration.__init__)


def test_metamodelo::cpp::cppvariabledeclaration_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "vartype" in params, "Missing parameter 'vartype'"
    assert "isArray" in params, "Missing parameter 'isArray'"

def test_metamodelo::cpp::cppvariabledeclaration_has_vartype():
    assert hasattr(Metamodelo::Cpp::CppVariableDeclaration, "vartype")
    descriptor = None
    for klass in Metamodelo::Cpp::CppVariableDeclaration.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppvariabledeclaration_has_isArray():
    assert hasattr(Metamodelo::Cpp::CppVariableDeclaration, "isArray")
    descriptor = None
    for klass in Metamodelo::Cpp::CppVariableDeclaration.__mro__:
        if "isArray" in klass.__dict__:
            descriptor = klass.__dict__["isArray"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppfieldcontainer_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppFieldContainer)


def test_metamodelo::cpp::cppfieldcontainer_constructor_exists():
    assert callable(Metamodelo::Cpp::CppFieldContainer.__init__)


def test_metamodelo::cpp::cppfieldcontainer_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppFieldContainer.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppfield_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppField)


def test_metamodelo::cpp::cppfield_constructor_exists():
    assert callable(Metamodelo::Cpp::CppField.__init__)


def test_metamodelo::cpp::cppfield_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppField.__init__)
    params = list(sig.parameters.keys())
    assert "accessSpecifier" in params, "Missing parameter 'accessSpecifier'"

def test_metamodelo::cpp::cppfield_has_accessSpecifier():
    assert hasattr(Metamodelo::Cpp::CppField, "accessSpecifier")
    descriptor = None
    for klass in Metamodelo::Cpp::CppField.__mro__:
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



def test_metamodelo::cpp::cppassignamentstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppAssignamentStatement)


def test_metamodelo::cpp::cppassignamentstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppAssignamentStatement.__init__)


def test_metamodelo::cpp::cppassignamentstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppAssignamentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo::cpp::cppassignamentstatement_has_operator():
    assert hasattr(Metamodelo::Cpp::CppAssignamentStatement, "operator")
    descriptor = None
    for klass in Metamodelo::Cpp::CppAssignamentStatement.__mro__:
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



def test_metamodelo::cpp::cppprefixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPrefixExpression)


def test_metamodelo::cpp::cppprefixexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPrefixExpression.__init__)


def test_metamodelo::cpp::cppprefixexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPrefixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo::cpp::cppprefixexpression_has_operator():
    assert hasattr(Metamodelo::Cpp::CppPrefixExpression, "operator")
    descriptor = None
    for klass in Metamodelo::Cpp::CppPrefixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cpppostfixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPostfixExpression)


def test_metamodelo::cpp::cpppostfixexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPostfixExpression.__init__)


def test_metamodelo::cpp::cpppostfixexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPostfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo::cpp::cpppostfixexpression_has_operator():
    assert hasattr(Metamodelo::Cpp::CppPostfixExpression, "operator")
    descriptor = None
    for klass in Metamodelo::Cpp::CppPostfixExpression.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppinfixexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppInfixExpression)


def test_metamodelo::cpp::cppinfixexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppInfixExpression.__init__)


def test_metamodelo::cpp::cppinfixexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppInfixExpression.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_metamodelo::cpp::cppinfixexpression_has_operator():
    assert hasattr(Metamodelo::Cpp::CppInfixExpression, "operator")
    descriptor = None
    for klass in Metamodelo::Cpp::CppInfixExpression.__mro__:
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



def test_metamodelo::cpp::cppifelsestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppIfElseStatement)


def test_metamodelo::cpp::cppifelsestatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppIfElseStatement.__init__)


def test_metamodelo::cpp::cppifelsestatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppIfElseStatement.__init__)
    params = list(sig.parameters.keys())
    assert "inLine" in params, "Missing parameter 'inLine'"

def test_metamodelo::cpp::cppifelsestatement_has_inLine():
    assert hasattr(Metamodelo::Cpp::CppIfElseStatement, "inLine")
    descriptor = None
    for klass in Metamodelo::Cpp::CppIfElseStatement.__mro__:
        if "inLine" in klass.__dict__:
            descriptor = klass.__dict__["inLine"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppifstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppIfStatement)


def test_metamodelo::cpp::cppifstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppIfStatement.__init__)


def test_metamodelo::cpp::cppifstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppIfStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(CppMethodInvocation)


def test_cppmethodinvocation_constructor_exists():
    assert callable(CppMethodInvocation.__init__)


def test_cppmethodinvocation_constructor_args():
    sig = inspect.signature(CppMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppsuperconstructorinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSuperConstructorInvocation)


def test_metamodelo::cpp::cppsuperconstructorinvocation_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSuperConstructorInvocation.__init__)


def test_metamodelo::cpp::cppsuperconstructorinvocation_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSuperConstructorInvocation.__init__)
    params = list(sig.parameters.keys())



def test_cppjumpstatement_is_not_abstract():
    assert not inspect.isabstract(CppJumpStatement)


def test_cppjumpstatement_constructor_exists():
    assert callable(CppJumpStatement.__init__)


def test_cppjumpstatement_constructor_args():
    sig = inspect.signature(CppJumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppgotostatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppGotoStatement)


def test_metamodelo::cpp::cppgotostatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppGotoStatement.__init__)


def test_metamodelo::cpp::cppgotostatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppGotoStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppcontinuestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppContinueStatement)


def test_metamodelo::cpp::cppcontinuestatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppContinueStatement.__init__)


def test_metamodelo::cpp::cppcontinuestatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppreturnstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppReturnStatement)


def test_metamodelo::cpp::cppreturnstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppReturnStatement.__init__)


def test_metamodelo::cpp::cppreturnstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppbreakstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppBreakStatement)


def test_metamodelo::cpp::cppbreakstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppBreakStatement.__init__)


def test_metamodelo::cpp::cppbreakstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppBreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppiterationstatement_is_not_abstract():
    assert not inspect.isabstract(CppIterationStatement)


def test_cppiterationstatement_constructor_exists():
    assert callable(CppIterationStatement.__init__)


def test_cppiterationstatement_constructor_args():
    sig = inspect.signature(CppIterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppforstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppForStatement)


def test_metamodelo::cpp::cppforstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppForStatement.__init__)


def test_metamodelo::cpp::cppforstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppForStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppdowhilestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppDoWhileStatement)


def test_metamodelo::cpp::cppdowhilestatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppDoWhileStatement.__init__)


def test_metamodelo::cpp::cppdowhilestatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppDoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppwhilestatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppWhileStatement)


def test_metamodelo::cpp::cppwhilestatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppWhileStatement.__init__)


def test_metamodelo::cpp::cppwhilestatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_cppexpression_is_not_abstract():
    assert not inspect.isabstract(CppExpression)


def test_cppexpression_constructor_exists():
    assert callable(CppExpression.__init__)


def test_cppexpression_constructor_args():
    sig = inspect.signature(CppExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppunaryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppUnaryExpression)


def test_metamodelo::cpp::cppunaryexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppUnaryExpression.__init__)


def test_metamodelo::cpp::cppunaryexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppBooleanLiteral)


def test_metamodelo::cpp::cppbooleanliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppBooleanLiteral.__init__)


def test_metamodelo::cpp::cppbooleanliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "booleanValue" in params, "Missing parameter 'booleanValue'"

def test_metamodelo::cpp::cppbooleanliteral_has_booleanValue():
    assert hasattr(Metamodelo::Cpp::CppBooleanLiteral, "booleanValue")
    descriptor = None
    for klass in Metamodelo::Cpp::CppBooleanLiteral.__mro__:
        if "booleanValue" in klass.__dict__:
            descriptor = klass.__dict__["booleanValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppBinaryExpression)


def test_metamodelo::cpp::cppbinaryexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppBinaryExpression.__init__)


def test_metamodelo::cpp::cppbinaryexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpptryexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppTryExpression)


def test_metamodelo::cpp::cpptryexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppTryExpression.__init__)


def test_metamodelo::cpp::cpptryexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppTryExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppiterationstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppIterationStatement)


def test_metamodelo::cpp::cppiterationstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppIterationStatement.__init__)


def test_metamodelo::cpp::cppiterationstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppIterationStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppthisexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppThisExpression)


def test_metamodelo::cpp::cppthisexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppThisExpression.__init__)


def test_metamodelo::cpp::cppthisexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppThisExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppthrowexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppThrowExpression)


def test_metamodelo::cpp::cppthrowexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppThrowExpression.__init__)


def test_metamodelo::cpp::cppthrowexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppThrowExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppjumpstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppJumpStatement)


def test_metamodelo::cpp::cppjumpstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppJumpStatement.__init__)


def test_metamodelo::cpp::cppjumpstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppJumpStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppswitchexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSwitchExpression)


def test_metamodelo::cpp::cppswitchexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSwitchExpression.__init__)


def test_metamodelo::cpp::cppswitchexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSwitchExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppfieldaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppFieldAccess)


def test_metamodelo::cpp::cppfieldaccess_constructor_exists():
    assert callable(Metamodelo::Cpp::CppFieldAccess.__init__)


def test_metamodelo::cpp::cppfieldaccess_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppFieldAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppnullliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppNullLiteral)


def test_metamodelo::cpp::cppnullliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppNullLiteral.__init__)


def test_metamodelo::cpp::cppnullliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppNullLiteral.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvariableaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVariableAccess)


def test_metamodelo::cpp::cppvariableaccess_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVariableAccess.__init__)


def test_metamodelo::cpp::cppvariableaccess_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVariableAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppcastexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppCastExpression)


def test_metamodelo::cpp::cppcastexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppCastExpression.__init__)


def test_metamodelo::cpp::cppcastexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppCastExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppconstantexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppConstantExpression)


def test_metamodelo::cpp::cppconstantexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppConstantExpression.__init__)


def test_metamodelo::cpp::cppconstantexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppregexliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppRegexLiteral)


def test_metamodelo::cpp::cppregexliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppRegexLiteral.__init__)


def test_metamodelo::cpp::cppregexliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppRegexLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "pattern" in params, "Missing parameter 'pattern'"
    assert "options" in params, "Missing parameter 'options'"

def test_metamodelo::cpp::cppregexliteral_has_pattern():
    assert hasattr(Metamodelo::Cpp::CppRegexLiteral, "pattern")
    descriptor = None
    for klass in Metamodelo::Cpp::CppRegexLiteral.__mro__:
        if "pattern" in klass.__dict__:
            descriptor = klass.__dict__["pattern"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppregexliteral_has_options():
    assert hasattr(Metamodelo::Cpp::CppRegexLiteral, "options")
    descriptor = None
    for klass in Metamodelo::Cpp::CppRegexLiteral.__mro__:
        if "options" in klass.__dict__:
            descriptor = klass.__dict__["options"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppcharacterliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppCharacterLiteral)


def test_metamodelo::cpp::cppcharacterliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppCharacterLiteral.__init__)


def test_metamodelo::cpp::cppcharacterliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppCharacterLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "charValue" in params, "Missing parameter 'charValue'"

def test_metamodelo::cpp::cppcharacterliteral_has_charValue():
    assert hasattr(Metamodelo::Cpp::CppCharacterLiteral, "charValue")
    descriptor = None
    for klass in Metamodelo::Cpp::CppCharacterLiteral.__mro__:
        if "charValue" in klass.__dict__:
            descriptor = klass.__dict__["charValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppcase_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppCase)


def test_metamodelo::cpp::cppcase_constructor_exists():
    assert callable(Metamodelo::Cpp::CppCase.__init__)


def test_metamodelo::cpp::cppcase_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppCase.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppdeclarationexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppDeclarationExpression)


def test_metamodelo::cpp::cppdeclarationexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppDeclarationExpression.__init__)


def test_metamodelo::cpp::cppdeclarationexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppDeclarationExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppcatchclause_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppCatchClause)


def test_metamodelo::cpp::cppcatchclause_constructor_exists():
    assert callable(Metamodelo::Cpp::CppCatchClause.__init__)


def test_metamodelo::cpp::cppcatchclause_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppCatchClause.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppnumberliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppNumberLiteral)


def test_metamodelo::cpp::cppnumberliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppNumberLiteral.__init__)


def test_metamodelo::cpp::cppnumberliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "token" in params, "Missing parameter 'token'"

def test_metamodelo::cpp::cppnumberliteral_has_token():
    assert hasattr(Metamodelo::Cpp::CppNumberLiteral, "token")
    descriptor = None
    for klass in Metamodelo::Cpp::CppNumberLiteral.__mro__:
        if "token" in klass.__dict__:
            descriptor = klass.__dict__["token"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppparenthizedexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppParenthizedExpression)


def test_metamodelo::cpp::cppparenthizedexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppParenthizedExpression.__init__)


def test_metamodelo::cpp::cppparenthizedexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppParenthizedExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpplabeledstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppLabeledStatement)


def test_metamodelo::cpp::cpplabeledstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppLabeledStatement.__init__)


def test_metamodelo::cpp::cpplabeledstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppLabeledStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpparrayaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppArrayAccess)


def test_metamodelo::cpp::cpparrayaccess_constructor_exists():
    assert callable(Metamodelo::Cpp::CppArrayAccess.__init__)


def test_metamodelo::cpp::cpparrayaccess_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppArrayAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppblock_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppBlock)


def test_metamodelo::cpp::cppblock_constructor_exists():
    assert callable(Metamodelo::Cpp::CppBlock.__init__)


def test_metamodelo::cpp::cppblock_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppBlock.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppstringliteral_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppStringLiteral)


def test_metamodelo::cpp::cppstringliteral_constructor_exists():
    assert callable(Metamodelo::Cpp::CppStringLiteral.__init__)


def test_metamodelo::cpp::cppstringliteral_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppStringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "literalValue" in params, "Missing parameter 'literalValue'"

def test_metamodelo::cpp::cppstringliteral_has_literalValue():
    assert hasattr(Metamodelo::Cpp::CppStringLiteral, "literalValue")
    descriptor = None
    for klass in Metamodelo::Cpp::CppStringLiteral.__mro__:
        if "literalValue" in klass.__dict__:
            descriptor = klass.__dict__["literalValue"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppselectionstatement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSelectionStatement)


def test_metamodelo::cpp::cppselectionstatement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSelectionStatement.__init__)


def test_metamodelo::cpp::cppselectionstatement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSelectionStatement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpparrayinitializer_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppArrayInitializer)


def test_metamodelo::cpp::cpparrayinitializer_constructor_exists():
    assert callable(Metamodelo::Cpp::CppArrayInitializer.__init__)


def test_metamodelo::cpp::cpparrayinitializer_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppArrayInitializer.__init__)
    params = list(sig.parameters.keys())



def test_cpptypedelement_is_not_abstract():
    assert not inspect.isabstract(CppTypedElement)


def test_cpptypedelement_constructor_exists():
    assert callable(CppTypedElement.__init__)


def test_cpptypedelement_constructor_args():
    sig = inspect.signature(CppTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvariabledeclarationgroup_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVariableDeclarationGroup)


def test_metamodelo::cpp::cppvariabledeclarationgroup_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVariableDeclarationGroup.__init__)


def test_metamodelo::cpp::cppvariabledeclarationgroup_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVariableDeclarationGroup.__init__)
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



def test_metamodelo::cpp::cppsinglevariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSingleVariableDeclaration)


def test_metamodelo::cpp::cppsinglevariabledeclaration_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSingleVariableDeclaration.__init__)


def test_metamodelo::cpp::cppsinglevariabledeclaration_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSingleVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvariabledeclarationfragment_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVariableDeclarationFragment)


def test_metamodelo::cpp::cppvariabledeclarationfragment_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVariableDeclarationFragment.__init__)


def test_metamodelo::cpp::cppvariabledeclarationfragment_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVariableDeclarationFragment.__init__)
    params = list(sig.parameters.keys())



def test_cppabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(CppAbstractMethodInvocation)


def test_cppabstractmethodinvocation_constructor_exists():
    assert callable(CppAbstractMethodInvocation.__init__)


def test_cppabstractmethodinvocation_constructor_args():
    sig = inspect.signature(CppAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppsupermethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSuperMethodInvocation)


def test_metamodelo::cpp::cppsupermethodinvocation_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSuperMethodInvocation.__init__)


def test_metamodelo::cpp::cppsupermethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSuperMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppMethodInvocation)


def test_metamodelo::cpp::cppmethodinvocation_constructor_exists():
    assert callable(Metamodelo::Cpp::CppMethodInvocation.__init__)


def test_metamodelo::cpp::cppmethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppabstractmethodinvocation_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppAbstractMethodInvocation)


def test_metamodelo::cpp::cppabstractmethodinvocation_constructor_exists():
    assert callable(Metamodelo::Cpp::CppAbstractMethodInvocation.__init__)


def test_metamodelo::cpp::cppabstractmethodinvocation_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppAbstractMethodInvocation.__init__)
    params = list(sig.parameters.keys())



def test_cppmemberfunction_is_not_abstract():
    assert not inspect.isabstract(CppMemberFunction)


def test_cppmemberfunction_constructor_exists():
    assert callable(CppMemberFunction.__init__)


def test_cppmemberfunction_constructor_args():
    sig = inspect.signature(CppMemberFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppmethod_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppMethod)


def test_metamodelo::cpp::cppmethod_constructor_exists():
    assert callable(Metamodelo::Cpp::CppMethod.__init__)


def test_metamodelo::cpp::cppmethod_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppMethod.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "isPureVirtual" in params, "Missing parameter 'isPureVirtual'"

def test_metamodelo::cpp::cppmethod_has_isFinal():
    assert hasattr(Metamodelo::Cpp::CppMethod, "isFinal")
    descriptor = None
    for klass in Metamodelo::Cpp::CppMethod.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppmethod_has_isVirtual():
    assert hasattr(Metamodelo::Cpp::CppMethod, "isVirtual")
    descriptor = None
    for klass in Metamodelo::Cpp::CppMethod.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppmethod_has_isConst():
    assert hasattr(Metamodelo::Cpp::CppMethod, "isConst")
    descriptor = None
    for klass in Metamodelo::Cpp::CppMethod.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppmethod_has_isPureVirtual():
    assert hasattr(Metamodelo::Cpp::CppMethod, "isPureVirtual")
    descriptor = None
    for klass in Metamodelo::Cpp::CppMethod.__mro__:
        if "isPureVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isPureVirtual"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppdestructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppDestructor)


def test_metamodelo::cpp::cppdestructor_constructor_exists():
    assert callable(Metamodelo::Cpp::CppDestructor.__init__)


def test_metamodelo::cpp::cppdestructor_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppDestructor.__init__)
    params = list(sig.parameters.keys())
    assert "isVirtual" in params, "Missing parameter 'isVirtual'"

def test_metamodelo::cpp::cppdestructor_has_isVirtual():
    assert hasattr(Metamodelo::Cpp::CppDestructor, "isVirtual")
    descriptor = None
    for klass in Metamodelo::Cpp::CppDestructor.__mro__:
        if "isVirtual" in klass.__dict__:
            descriptor = klass.__dict__["isVirtual"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppconstructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppConstructor)


def test_metamodelo::cpp::cppconstructor_constructor_exists():
    assert callable(Metamodelo::Cpp::CppConstructor.__init__)


def test_metamodelo::cpp::cppconstructor_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppConstructor.__init__)
    params = list(sig.parameters.keys())



def test_cppfunction_is_not_abstract():
    assert not inspect.isabstract(CppFunction)


def test_cppfunction_constructor_exists():
    assert callable(CppFunction.__init__)


def test_cppfunction_constructor_args():
    sig = inspect.signature(CppFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppmemberfunction_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppMemberFunction)


def test_metamodelo::cpp::cppmemberfunction_constructor_exists():
    assert callable(Metamodelo::Cpp::CppMemberFunction.__init__)


def test_metamodelo::cpp::cppmemberfunction_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppMemberFunction.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpptypedelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppTypedElement)


def test_metamodelo::cpp::cpptypedelement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppTypedElement.__init__)


def test_metamodelo::cpp::cpptypedelement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppTypedElement.__init__)
    params = list(sig.parameters.keys())



def test_cppclassifier_is_not_abstract():
    assert not inspect.isabstract(CppClassifier)


def test_cppclassifier_constructor_exists():
    assert callable(CppClassifier.__init__)


def test_cppclassifier_constructor_args():
    sig = inspect.signature(CppClassifier.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppclass_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppClass)


def test_metamodelo::cpp::cppclass_constructor_exists():
    assert callable(Metamodelo::Cpp::CppClass.__init__)


def test_metamodelo::cpp::cppclass_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppClass.__init__)
    params = list(sig.parameters.keys())
    assert "isFinal" in params, "Missing parameter 'isFinal'"
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"
    assert "classkey" in params, "Missing parameter 'classkey'"
    assert "isGeneric" in params, "Missing parameter 'isGeneric'"

def test_metamodelo::cpp::cppclass_has_isFinal():
    assert hasattr(Metamodelo::Cpp::CppClass, "isFinal")
    descriptor = None
    for klass in Metamodelo::Cpp::CppClass.__mro__:
        if "isFinal" in klass.__dict__:
            descriptor = klass.__dict__["isFinal"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppclass_has_isAbstract():
    assert hasattr(Metamodelo::Cpp::CppClass, "isAbstract")
    descriptor = None
    for klass in Metamodelo::Cpp::CppClass.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppclass_has_classkey():
    assert hasattr(Metamodelo::Cpp::CppClass, "classkey")
    descriptor = None
    for klass in Metamodelo::Cpp::CppClass.__mro__:
        if "classkey" in klass.__dict__:
            descriptor = klass.__dict__["classkey"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppclass_has_isGeneric():
    assert hasattr(Metamodelo::Cpp::CppClass, "isGeneric")
    descriptor = None
    for klass in Metamodelo::Cpp::CppClass.__mro__:
        if "isGeneric" in klass.__dict__:
            descriptor = klass.__dict__["isGeneric"]
            break
    assert isinstance(descriptor, property)



def test_cppprimitivetype_is_not_abstract():
    assert not inspect.isabstract(CppPrimitiveType)


def test_cppprimitivetype_constructor_exists():
    assert callable(CppPrimitiveType.__init__)


def test_cppprimitivetype_constructor_args():
    sig = inspect.signature(CppPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpplongtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppLongType)


def test_metamodelo::cpp::cpplongtype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppLongType.__init__)


def test_metamodelo::cpp::cpplongtype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppLongType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppunsignedtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppUnsignedType)


def test_metamodelo::cpp::cppunsignedtype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppUnsignedType.__init__)


def test_metamodelo::cpp::cppunsignedtype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppUnsignedType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppfloattype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppFloatType)


def test_metamodelo::cpp::cppfloattype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppFloatType.__init__)


def test_metamodelo::cpp::cppfloattype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppFloatType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvoidtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVoidType)


def test_metamodelo::cpp::cppvoidtype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVoidType.__init__)


def test_metamodelo::cpp::cppvoidtype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVoidType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppsignedtype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppSignedType)


def test_metamodelo::cpp::cppsignedtype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppSignedType.__init__)


def test_metamodelo::cpp::cppsignedtype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppSignedType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppshorttype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppShortType)


def test_metamodelo::cpp::cppshorttype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppShortType.__init__)


def test_metamodelo::cpp::cppshorttype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppShortType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppdoubletype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppDoubleType)


def test_metamodelo::cpp::cppdoubletype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppDoubleType.__init__)


def test_metamodelo::cpp::cppdoubletype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppDoubleType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppchartype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppCharType)


def test_metamodelo::cpp::cppchartype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppCharType.__init__)


def test_metamodelo::cpp::cppchartype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppCharType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppinttype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppIntType)


def test_metamodelo::cpp::cppinttype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppIntType.__init__)


def test_metamodelo::cpp::cppinttype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppIntType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppbooleantype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppBooleanType)


def test_metamodelo::cpp::cppbooleantype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppBooleanType.__init__)


def test_metamodelo::cpp::cppbooleantype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppBooleanType.__init__)
    params = list(sig.parameters.keys())



def test_cpptype_is_not_abstract():
    assert not inspect.isabstract(CppType)


def test_cpptype_constructor_exists():
    assert callable(CppType.__init__)


def test_cpptype_constructor_args():
    sig = inspect.signature(CppType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppfunction_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppFunction)


def test_metamodelo::cpp::cppfunction_constructor_exists():
    assert callable(Metamodelo::Cpp::CppFunction.__init__)


def test_metamodelo::cpp::cppfunction_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppFunction.__init__)
    params = list(sig.parameters.keys())
    assert "isInline" in params, "Missing parameter 'isInline'"
    assert "isVarArg" in params, "Missing parameter 'isVarArg'"
    assert "linkage" in params, "Missing parameter 'linkage'"

def test_metamodelo::cpp::cppfunction_has_isInline():
    assert hasattr(Metamodelo::Cpp::CppFunction, "isInline")
    descriptor = None
    for klass in Metamodelo::Cpp::CppFunction.__mro__:
        if "isInline" in klass.__dict__:
            descriptor = klass.__dict__["isInline"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppfunction_has_isVarArg():
    assert hasattr(Metamodelo::Cpp::CppFunction, "isVarArg")
    descriptor = None
    for klass in Metamodelo::Cpp::CppFunction.__mro__:
        if "isVarArg" in klass.__dict__:
            descriptor = klass.__dict__["isVarArg"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppfunction_has_linkage():
    assert hasattr(Metamodelo::Cpp::CppFunction, "linkage")
    descriptor = None
    for klass in Metamodelo::Cpp::CppFunction.__mro__:
        if "linkage" in klass.__dict__:
            descriptor = klass.__dict__["linkage"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppclassifier_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppClassifier)


def test_metamodelo::cpp::cppclassifier_constructor_exists():
    assert callable(Metamodelo::Cpp::CppClassifier.__init__)


def test_metamodelo::cpp::cppclassifier_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppClassifier.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppprimitivetype_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppPrimitiveType)


def test_metamodelo::cpp::cppprimitivetype_constructor_exists():
    assert callable(Metamodelo::Cpp::CppPrimitiveType.__init__)


def test_metamodelo::cpp::cppprimitivetype_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppPrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpptypeparameter_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppTypeParameter)


def test_metamodelo::cpp::cpptypeparameter_constructor_exists():
    assert callable(Metamodelo::Cpp::CppTypeParameter.__init__)


def test_metamodelo::cpp::cpptypeparameter_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppTypeParameter.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cpptypeaccess_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppTypeAccess)


def test_metamodelo::cpp::cpptypeaccess_constructor_exists():
    assert callable(Metamodelo::Cpp::CppTypeAccess.__init__)


def test_metamodelo::cpp::cpptypeaccess_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppTypeAccess.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppimportdeclaration_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppImportDeclaration)


def test_metamodelo::cpp::cppimportdeclaration_constructor_exists():
    assert callable(Metamodelo::Cpp::CppImportDeclaration.__init__)


def test_metamodelo::cpp::cppimportdeclaration_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppnamedelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppNamedElement)


def test_metamodelo::cpp::cppnamedelement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppNamedElement.__init__)


def test_metamodelo::cpp::cppnamedelement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_metamodelo::cpp::cppnamedelement_has_name():
    assert hasattr(Metamodelo::Cpp::CppNamedElement, "name")
    descriptor = None
    for klass in Metamodelo::Cpp::CppNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppmodelelement_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppModelElement)


def test_metamodelo::cpp::cppmodelelement_constructor_exists():
    assert callable(Metamodelo::Cpp::CppModelElement.__init__)


def test_metamodelo::cpp::cppmodelelement_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppModelElement.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppcomment_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppComment)


def test_metamodelo::cpp::cppcomment_constructor_exists():
    assert callable(Metamodelo::Cpp::CppComment.__init__)


def test_metamodelo::cpp::cppcomment_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppComment.__init__)
    params = list(sig.parameters.keys())
    assert "multiLine" in params, "Missing parameter 'multiLine'"
    assert "singleLine" in params, "Missing parameter 'singleLine'"
    assert "content" in params, "Missing parameter 'content'"

def test_metamodelo::cpp::cppcomment_has_multiLine():
    assert hasattr(Metamodelo::Cpp::CppComment, "multiLine")
    descriptor = None
    for klass in Metamodelo::Cpp::CppComment.__mro__:
        if "multiLine" in klass.__dict__:
            descriptor = klass.__dict__["multiLine"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppcomment_has_singleLine():
    assert hasattr(Metamodelo::Cpp::CppComment, "singleLine")
    descriptor = None
    for klass in Metamodelo::Cpp::CppComment.__mro__:
        if "singleLine" in klass.__dict__:
            descriptor = klass.__dict__["singleLine"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppcomment_has_content():
    assert hasattr(Metamodelo::Cpp::CppComment, "content")
    descriptor = None
    for klass in Metamodelo::Cpp::CppComment.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_metamodelo::cpp::cppexpression_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppExpression)


def test_metamodelo::cpp::cppexpression_constructor_exists():
    assert callable(Metamodelo::Cpp::CppExpression.__init__)


def test_metamodelo::cpp::cppexpression_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppExpression.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppenumconstructor_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppEnumConstructor)


def test_metamodelo::cpp::cppenumconstructor_constructor_exists():
    assert callable(Metamodelo::Cpp::CppEnumConstructor.__init__)


def test_metamodelo::cpp::cppenumconstructor_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppEnumConstructor.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppenum_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppEnum)


def test_metamodelo::cpp::cppenum_constructor_exists():
    assert callable(Metamodelo::Cpp::CppEnum.__init__)


def test_metamodelo::cpp::cppenum_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppEnum.__init__)
    params = list(sig.parameters.keys())



def test_metamodelo::cpp::cppvariable_is_not_abstract():
    assert not inspect.isabstract(Metamodelo::Cpp::CppVariable)


def test_metamodelo::cpp::cppvariable_constructor_exists():
    assert callable(Metamodelo::Cpp::CppVariable.__init__)


def test_metamodelo::cpp::cppvariable_constructor_args():
    sig = inspect.signature(Metamodelo::Cpp::CppVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isConst" in params, "Missing parameter 'isConst'"
    assert "storage" in params, "Missing parameter 'storage'"

def test_metamodelo::cpp::cppvariable_has_isConst():
    assert hasattr(Metamodelo::Cpp::CppVariable, "isConst")
    descriptor = None
    for klass in Metamodelo::Cpp::CppVariable.__mro__:
        if "isConst" in klass.__dict__:
            descriptor = klass.__dict__["isConst"]
            break
    assert isinstance(descriptor, property)

def test_metamodelo::cpp::cppvariable_has_storage():
    assert hasattr(Metamodelo::Cpp::CppVariable, "storage")
    descriptor = None
    for klass in Metamodelo::Cpp::CppVariable.__mro__:
        if "storage" in klass.__dict__:
            descriptor = klass.__dict__["storage"]
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

def test_cppqualifiertype_exists():
    # Check that the Enumeration exists
    assert CppQualifierType is not None

def test_cppqualifiertype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppQualifierType]
    expected_literals = [
        "VOLATILE",
        "CONST",
        "ATOMIC",
        "RESTRICT",
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
        "OR_ASSIGN",
        "ASSIGN",
        "PLUS_ASSIGN",
        "MODULO_ASSIGN",
        "AND_ASSIGN",
        "MINUS_ASSIGN",
        "SHIFT_LEFT_ASSIGN",
        "SHIFT_RIGHT_ASSIGN",
        "DIVISSION_ASSIGN",
        "XOR_ASSIGN",
        "TIMES_ASSIGN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppAssignmentOperator"

def test_cppstoragetype_exists():
    # Check that the Enumeration exists
    assert CppStorageType is not None

def test_cppstoragetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppStorageType]
    expected_literals = [
        "REGISTER",
        "MUTABLE",
        "TYPEDEF",
        "STATIC",
        "THREAD_LOCAL",
        "AUTO",
        "EXTERN",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppStorageType"

def test_cppoperator_exists():
    # Check that the Enumeration exists
    assert CppOperator is not None

def test_cppoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppOperator]
    expected_literals = [
        "LESS_THAN",
        "XOR_EQ",
        "TIMES",
        "BIT_AND",
        "SHIFT_LEFT",
        "SHIFT_RIGHT",
        "NOT_EQUALS",
        "BIT_OR",
        "GREATER_EQUALS",
        "XOR",
        "GREATER_THAN",
        "LESS_EQUALS",
        "MINUS",
        "DIVISION",
        "OR",
        "EQUALS",
        "REMAINDER",
        "PLUS",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppOperator"

def test_cppunaryoperator_exists():
    # Check that the Enumeration exists
    assert CppUnaryOperator is not None

def test_cppunaryoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppUnaryOperator]
    expected_literals = [
        "NOT",
        "MINUS",
        "ASTERISK",
        "PLUS",
        "INCREMENT",
        "AMPERSAND",
        "DECREMENT",
        "BIT_NOT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppUnaryOperator"

def test_cpppostfixoperator_exists():
    # Check that the Enumeration exists
    assert CppPostfixOperator is not None

def test_cpppostfixoperator_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CppPostfixOperator]
    expected_literals = [
        "DECREMENT",
        "INCREMENT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CppPostfixOperator"

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
CppFieldContainer_strategy = st.builds(
    CppFieldContainer,
)
Metamodelo::Cpp::CppModel_strategy = st.builds(
    Metamodelo::Cpp::CppModel,
    name=
        safe_text,
    targetFolder=
        safe_text,
    sourceFolder=
        safe_text
)
CppPathReferentiable_strategy = st.builds(
    CppPathReferentiable,
)
CppModelElement_strategy = st.builds(
    CppModelElement,
)
Metamodelo::Cpp::CppPathReference_strategy = st.builds(
    Metamodelo::Cpp::CppPathReference,
)
Metamodelo::Cpp::CppPackage_strategy = st.builds(
    Metamodelo::Cpp::CppPackage,
)
CppNamedElement_strategy = st.builds(
    CppNamedElement,
)
Metamodelo::Cpp::CppPathReferentiable_strategy = st.builds(
    Metamodelo::Cpp::CppPathReferentiable,
)
Metamodelo::Cpp::CppClassFile_strategy = st.builds(
    Metamodelo::Cpp::CppClassFile,
)
Metamodelo::Cpp::CppType_strategy = st.builds(
    Metamodelo::Cpp::CppType,
)
Metamodelo::Cpp::CppVariableDeclaration_strategy = st.builds(
    Metamodelo::Cpp::CppVariableDeclaration,
    vartype=
        safe_text,
    isArray=
        st.booleans()
)
Metamodelo::Cpp::CppFieldContainer_strategy = st.builds(
    Metamodelo::Cpp::CppFieldContainer,
)
Metamodelo::Cpp::CppField_strategy = st.builds(
    Metamodelo::Cpp::CppField,
    accessSpecifier=
        safe_text
)
CppBinaryExpression_strategy = st.builds(
    CppBinaryExpression,
)
Metamodelo::Cpp::CppAssignamentStatement_strategy = st.builds(
    Metamodelo::Cpp::CppAssignamentStatement,
    operator=
        safe_text
)
CppUnaryExpression_strategy = st.builds(
    CppUnaryExpression,
)
Metamodelo::Cpp::CppPrefixExpression_strategy = st.builds(
    Metamodelo::Cpp::CppPrefixExpression,
    operator=
        safe_text
)
Metamodelo::Cpp::CppPostfixExpression_strategy = st.builds(
    Metamodelo::Cpp::CppPostfixExpression,
    operator=
        safe_text
)
Metamodelo::Cpp::CppInfixExpression_strategy = st.builds(
    Metamodelo::Cpp::CppInfixExpression,
    operator=
        safe_text
)
CppSelectionStatement_strategy = st.builds(
    CppSelectionStatement,
)
Metamodelo::Cpp::CppIfElseStatement_strategy = st.builds(
    Metamodelo::Cpp::CppIfElseStatement,
    inLine=
        st.booleans()
)
Metamodelo::Cpp::CppIfStatement_strategy = st.builds(
    Metamodelo::Cpp::CppIfStatement,
)
CppMethodInvocation_strategy = st.builds(
    CppMethodInvocation,
)
Metamodelo::Cpp::CppSuperConstructorInvocation_strategy = st.builds(
    Metamodelo::Cpp::CppSuperConstructorInvocation,
)
CppJumpStatement_strategy = st.builds(
    CppJumpStatement,
)
Metamodelo::Cpp::CppGotoStatement_strategy = st.builds(
    Metamodelo::Cpp::CppGotoStatement,
)
Metamodelo::Cpp::CppContinueStatement_strategy = st.builds(
    Metamodelo::Cpp::CppContinueStatement,
)
Metamodelo::Cpp::CppReturnStatement_strategy = st.builds(
    Metamodelo::Cpp::CppReturnStatement,
)
Metamodelo::Cpp::CppBreakStatement_strategy = st.builds(
    Metamodelo::Cpp::CppBreakStatement,
)
CppIterationStatement_strategy = st.builds(
    CppIterationStatement,
)
Metamodelo::Cpp::CppForStatement_strategy = st.builds(
    Metamodelo::Cpp::CppForStatement,
)
Metamodelo::Cpp::CppDoWhileStatement_strategy = st.builds(
    Metamodelo::Cpp::CppDoWhileStatement,
)
Metamodelo::Cpp::CppWhileStatement_strategy = st.builds(
    Metamodelo::Cpp::CppWhileStatement,
)
CppExpression_strategy = st.builds(
    CppExpression,
)
Metamodelo::Cpp::CppUnaryExpression_strategy = st.builds(
    Metamodelo::Cpp::CppUnaryExpression,
)
Metamodelo::Cpp::CppBooleanLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppBooleanLiteral,
    booleanValue=
        st.booleans()
)
Metamodelo::Cpp::CppBinaryExpression_strategy = st.builds(
    Metamodelo::Cpp::CppBinaryExpression,
)
Metamodelo::Cpp::CppTryExpression_strategy = st.builds(
    Metamodelo::Cpp::CppTryExpression,
)
Metamodelo::Cpp::CppIterationStatement_strategy = st.builds(
    Metamodelo::Cpp::CppIterationStatement,
)
Metamodelo::Cpp::CppThisExpression_strategy = st.builds(
    Metamodelo::Cpp::CppThisExpression,
)
Metamodelo::Cpp::CppThrowExpression_strategy = st.builds(
    Metamodelo::Cpp::CppThrowExpression,
)
Metamodelo::Cpp::CppJumpStatement_strategy = st.builds(
    Metamodelo::Cpp::CppJumpStatement,
)
Metamodelo::Cpp::CppSwitchExpression_strategy = st.builds(
    Metamodelo::Cpp::CppSwitchExpression,
)
Metamodelo::Cpp::CppFieldAccess_strategy = st.builds(
    Metamodelo::Cpp::CppFieldAccess,
)
Metamodelo::Cpp::CppNullLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppNullLiteral,
)
Metamodelo::Cpp::CppVariableAccess_strategy = st.builds(
    Metamodelo::Cpp::CppVariableAccess,
)
Metamodelo::Cpp::CppCastExpression_strategy = st.builds(
    Metamodelo::Cpp::CppCastExpression,
)
Metamodelo::Cpp::CppConstantExpression_strategy = st.builds(
    Metamodelo::Cpp::CppConstantExpression,
)
Metamodelo::Cpp::CppRegexLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppRegexLiteral,
    pattern=
        safe_text,
    options=
        safe_text
)
Metamodelo::Cpp::CppCharacterLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppCharacterLiteral,
    charValue=
        safe_text
)
Metamodelo::Cpp::CppCase_strategy = st.builds(
    Metamodelo::Cpp::CppCase,
)
Metamodelo::Cpp::CppDeclarationExpression_strategy = st.builds(
    Metamodelo::Cpp::CppDeclarationExpression,
)
Metamodelo::Cpp::CppCatchClause_strategy = st.builds(
    Metamodelo::Cpp::CppCatchClause,
)
Metamodelo::Cpp::CppNumberLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppNumberLiteral,
    token=
        safe_text
)
Metamodelo::Cpp::CppParenthizedExpression_strategy = st.builds(
    Metamodelo::Cpp::CppParenthizedExpression,
)
Metamodelo::Cpp::CppLabeledStatement_strategy = st.builds(
    Metamodelo::Cpp::CppLabeledStatement,
)
Metamodelo::Cpp::CppArrayAccess_strategy = st.builds(
    Metamodelo::Cpp::CppArrayAccess,
)
Metamodelo::Cpp::CppBlock_strategy = st.builds(
    Metamodelo::Cpp::CppBlock,
)
Metamodelo::Cpp::CppStringLiteral_strategy = st.builds(
    Metamodelo::Cpp::CppStringLiteral,
    literalValue=
        safe_text
)
Metamodelo::Cpp::CppSelectionStatement_strategy = st.builds(
    Metamodelo::Cpp::CppSelectionStatement,
)
Metamodelo::Cpp::CppArrayInitializer_strategy = st.builds(
    Metamodelo::Cpp::CppArrayInitializer,
)
CppTypedElement_strategy = st.builds(
    CppTypedElement,
)
Metamodelo::Cpp::CppVariableDeclarationGroup_strategy = st.builds(
    Metamodelo::Cpp::CppVariableDeclarationGroup,
)
CppField_strategy = st.builds(
    CppField,
)
CppVariableDeclaration_strategy = st.builds(
    CppVariableDeclaration,
)
Metamodelo::Cpp::CppSingleVariableDeclaration_strategy = st.builds(
    Metamodelo::Cpp::CppSingleVariableDeclaration,
)
Metamodelo::Cpp::CppVariableDeclarationFragment_strategy = st.builds(
    Metamodelo::Cpp::CppVariableDeclarationFragment,
)
CppAbstractMethodInvocation_strategy = st.builds(
    CppAbstractMethodInvocation,
)
Metamodelo::Cpp::CppSuperMethodInvocation_strategy = st.builds(
    Metamodelo::Cpp::CppSuperMethodInvocation,
)
Metamodelo::Cpp::CppMethodInvocation_strategy = st.builds(
    Metamodelo::Cpp::CppMethodInvocation,
)
Metamodelo::Cpp::CppAbstractMethodInvocation_strategy = st.builds(
    Metamodelo::Cpp::CppAbstractMethodInvocation,
)
CppMemberFunction_strategy = st.builds(
    CppMemberFunction,
)
Metamodelo::Cpp::CppMethod_strategy = st.builds(
    Metamodelo::Cpp::CppMethod,
    isFinal=
        st.booleans(),
    isVirtual=
        st.booleans(),
    isConst=
        st.booleans(),
    isPureVirtual=
        st.booleans()
)
Metamodelo::Cpp::CppDestructor_strategy = st.builds(
    Metamodelo::Cpp::CppDestructor,
    isVirtual=
        st.booleans()
)
Metamodelo::Cpp::CppConstructor_strategy = st.builds(
    Metamodelo::Cpp::CppConstructor,
)
CppFunction_strategy = st.builds(
    CppFunction,
)
Metamodelo::Cpp::CppMemberFunction_strategy = st.builds(
    Metamodelo::Cpp::CppMemberFunction,
)
Metamodelo::Cpp::CppTypedElement_strategy = st.builds(
    Metamodelo::Cpp::CppTypedElement,
)
CppClassifier_strategy = st.builds(
    CppClassifier,
)
Metamodelo::Cpp::CppClass_strategy = st.builds(
    Metamodelo::Cpp::CppClass,
    isFinal=
        st.booleans(),
    isAbstract=
        st.booleans(),
    classkey=
        safe_text,
    isGeneric=
        st.booleans()
)
CppPrimitiveType_strategy = st.builds(
    CppPrimitiveType,
)
Metamodelo::Cpp::CppLongType_strategy = st.builds(
    Metamodelo::Cpp::CppLongType,
)
Metamodelo::Cpp::CppUnsignedType_strategy = st.builds(
    Metamodelo::Cpp::CppUnsignedType,
)
Metamodelo::Cpp::CppFloatType_strategy = st.builds(
    Metamodelo::Cpp::CppFloatType,
)
Metamodelo::Cpp::CppVoidType_strategy = st.builds(
    Metamodelo::Cpp::CppVoidType,
)
Metamodelo::Cpp::CppSignedType_strategy = st.builds(
    Metamodelo::Cpp::CppSignedType,
)
Metamodelo::Cpp::CppShortType_strategy = st.builds(
    Metamodelo::Cpp::CppShortType,
)
Metamodelo::Cpp::CppDoubleType_strategy = st.builds(
    Metamodelo::Cpp::CppDoubleType,
)
Metamodelo::Cpp::CppCharType_strategy = st.builds(
    Metamodelo::Cpp::CppCharType,
)
Metamodelo::Cpp::CppIntType_strategy = st.builds(
    Metamodelo::Cpp::CppIntType,
)
Metamodelo::Cpp::CppBooleanType_strategy = st.builds(
    Metamodelo::Cpp::CppBooleanType,
)
CppType_strategy = st.builds(
    CppType,
)
Metamodelo::Cpp::CppFunction_strategy = st.builds(
    Metamodelo::Cpp::CppFunction,
    isInline=
        st.booleans(),
    isVarArg=
        st.booleans(),
    linkage=
        safe_text
)
Metamodelo::Cpp::CppClassifier_strategy = st.builds(
    Metamodelo::Cpp::CppClassifier,
)
Metamodelo::Cpp::CppPrimitiveType_strategy = st.builds(
    Metamodelo::Cpp::CppPrimitiveType,
)
Metamodelo::Cpp::CppTypeParameter_strategy = st.builds(
    Metamodelo::Cpp::CppTypeParameter,
)
Metamodelo::Cpp::CppTypeAccess_strategy = st.builds(
    Metamodelo::Cpp::CppTypeAccess,
)
Metamodelo::Cpp::CppImportDeclaration_strategy = st.builds(
    Metamodelo::Cpp::CppImportDeclaration,
)
Metamodelo::Cpp::CppNamedElement_strategy = st.builds(
    Metamodelo::Cpp::CppNamedElement,
    name=
        safe_text
)
Metamodelo::Cpp::CppModelElement_strategy = st.builds(
    Metamodelo::Cpp::CppModelElement,
)
Metamodelo::Cpp::CppComment_strategy = st.builds(
    Metamodelo::Cpp::CppComment,
    multiLine=
        st.booleans(),
    singleLine=
        st.booleans(),
    content=
        safe_text
)
Metamodelo::Cpp::CppExpression_strategy = st.builds(
    Metamodelo::Cpp::CppExpression,
)
Metamodelo::Cpp::CppEnumConstructor_strategy = st.builds(
    Metamodelo::Cpp::CppEnumConstructor,
)
Metamodelo::Cpp::CppEnum_strategy = st.builds(
    Metamodelo::Cpp::CppEnum,
)
Metamodelo::Cpp::CppVariable_strategy = st.builds(
    Metamodelo::Cpp::CppVariable,
    isConst=
        st.booleans(),
    storage=
        safe_text
)

@given(instance=CppFieldContainer_strategy)
@settings(max_examples=50)
def test_cppfieldcontainer_instantiation(instance):
    assert isinstance(instance, CppFieldContainer)

@given(instance=Metamodelo::Cpp::CppModel_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppmodel_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppModel)

@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_targetFolder_type(instance):
    assert isinstance(instance.targetFolder, str)


@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_targetFolder_setter(instance):
    original = instance.targetFolder
    instance.targetFolder = original
    assert instance.targetFolder == original

@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_sourceFolder_type(instance):
    assert isinstance(instance.sourceFolder, str)


@given(instance=Metamodelo::Cpp::CppModel_strategy)
def test_metamodelo::cpp::cppmodel_sourceFolder_setter(instance):
    original = instance.sourceFolder
    instance.sourceFolder = original
    assert instance.sourceFolder == original

@given(instance=CppPathReferentiable_strategy)
@settings(max_examples=50)
def test_cpppathreferentiable_instantiation(instance):
    assert isinstance(instance, CppPathReferentiable)

@given(instance=CppModelElement_strategy)
@settings(max_examples=50)
def test_cppmodelelement_instantiation(instance):
    assert isinstance(instance, CppModelElement)

@given(instance=Metamodelo::Cpp::CppPathReference_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpppathreference_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPathReference)

@given(instance=Metamodelo::Cpp::CppPackage_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpppackage_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPackage)

@given(instance=CppNamedElement_strategy)
@settings(max_examples=50)
def test_cppnamedelement_instantiation(instance):
    assert isinstance(instance, CppNamedElement)

@given(instance=Metamodelo::Cpp::CppPathReferentiable_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpppathreferentiable_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPathReferentiable)

@given(instance=Metamodelo::Cpp::CppClassFile_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppclassfile_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppClassFile)

@given(instance=Metamodelo::Cpp::CppType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpptype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppType)

@given(instance=Metamodelo::Cpp::CppVariableDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvariabledeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVariableDeclaration)

@given(instance=Metamodelo::Cpp::CppVariableDeclaration_strategy)
def test_metamodelo::cpp::cppvariabledeclaration_vartype_type(instance):
    assert isinstance(instance.vartype, str)


@given(instance=Metamodelo::Cpp::CppVariableDeclaration_strategy)
def test_metamodelo::cpp::cppvariabledeclaration_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original

@given(instance=Metamodelo::Cpp::CppVariableDeclaration_strategy)
def test_metamodelo::cpp::cppvariabledeclaration_isArray_type(instance):
    assert isinstance(instance.isArray, bool)


@given(instance=Metamodelo::Cpp::CppVariableDeclaration_strategy)
def test_metamodelo::cpp::cppvariabledeclaration_isArray_setter(instance):
    original = instance.isArray
    instance.isArray = original
    assert instance.isArray == original

@given(instance=Metamodelo::Cpp::CppFieldContainer_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppfieldcontainer_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppFieldContainer)

@given(instance=Metamodelo::Cpp::CppField_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppfield_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppField)

@given(instance=Metamodelo::Cpp::CppField_strategy)
def test_metamodelo::cpp::cppfield_accessSpecifier_type(instance):
    assert isinstance(instance.accessSpecifier, str)


@given(instance=Metamodelo::Cpp::CppField_strategy)
def test_metamodelo::cpp::cppfield_accessSpecifier_setter(instance):
    original = instance.accessSpecifier
    instance.accessSpecifier = original
    assert instance.accessSpecifier == original

@given(instance=CppBinaryExpression_strategy)
@settings(max_examples=50)
def test_cppbinaryexpression_instantiation(instance):
    assert isinstance(instance, CppBinaryExpression)

@given(instance=Metamodelo::Cpp::CppAssignamentStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppassignamentstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppAssignamentStatement)

@given(instance=Metamodelo::Cpp::CppAssignamentStatement_strategy)
def test_metamodelo::cpp::cppassignamentstatement_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Metamodelo::Cpp::CppAssignamentStatement_strategy)
def test_metamodelo::cpp::cppassignamentstatement_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CppUnaryExpression_strategy)
@settings(max_examples=50)
def test_cppunaryexpression_instantiation(instance):
    assert isinstance(instance, CppUnaryExpression)

@given(instance=Metamodelo::Cpp::CppPrefixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppprefixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPrefixExpression)

@given(instance=Metamodelo::Cpp::CppPrefixExpression_strategy)
def test_metamodelo::cpp::cppprefixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Metamodelo::Cpp::CppPrefixExpression_strategy)
def test_metamodelo::cpp::cppprefixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Metamodelo::Cpp::CppPostfixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpppostfixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPostfixExpression)

@given(instance=Metamodelo::Cpp::CppPostfixExpression_strategy)
def test_metamodelo::cpp::cpppostfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Metamodelo::Cpp::CppPostfixExpression_strategy)
def test_metamodelo::cpp::cpppostfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=Metamodelo::Cpp::CppInfixExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppinfixexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppInfixExpression)

@given(instance=Metamodelo::Cpp::CppInfixExpression_strategy)
def test_metamodelo::cpp::cppinfixexpression_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=Metamodelo::Cpp::CppInfixExpression_strategy)
def test_metamodelo::cpp::cppinfixexpression_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=CppSelectionStatement_strategy)
@settings(max_examples=50)
def test_cppselectionstatement_instantiation(instance):
    assert isinstance(instance, CppSelectionStatement)

@given(instance=Metamodelo::Cpp::CppIfElseStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppifelsestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppIfElseStatement)

@given(instance=Metamodelo::Cpp::CppIfElseStatement_strategy)
def test_metamodelo::cpp::cppifelsestatement_inLine_type(instance):
    assert isinstance(instance.inLine, bool)


@given(instance=Metamodelo::Cpp::CppIfElseStatement_strategy)
def test_metamodelo::cpp::cppifelsestatement_inLine_setter(instance):
    original = instance.inLine
    instance.inLine = original
    assert instance.inLine == original

@given(instance=Metamodelo::Cpp::CppIfStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppifstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppIfStatement)

@given(instance=CppMethodInvocation_strategy)
@settings(max_examples=50)
def test_cppmethodinvocation_instantiation(instance):
    assert isinstance(instance, CppMethodInvocation)

@given(instance=Metamodelo::Cpp::CppSuperConstructorInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppsuperconstructorinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSuperConstructorInvocation)

@given(instance=CppJumpStatement_strategy)
@settings(max_examples=50)
def test_cppjumpstatement_instantiation(instance):
    assert isinstance(instance, CppJumpStatement)

@given(instance=Metamodelo::Cpp::CppGotoStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppgotostatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppGotoStatement)

@given(instance=Metamodelo::Cpp::CppContinueStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcontinuestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppContinueStatement)

@given(instance=Metamodelo::Cpp::CppReturnStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppreturnstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppReturnStatement)

@given(instance=Metamodelo::Cpp::CppBreakStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppbreakstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppBreakStatement)

@given(instance=CppIterationStatement_strategy)
@settings(max_examples=50)
def test_cppiterationstatement_instantiation(instance):
    assert isinstance(instance, CppIterationStatement)

@given(instance=Metamodelo::Cpp::CppForStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppforstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppForStatement)

@given(instance=Metamodelo::Cpp::CppDoWhileStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppdowhilestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppDoWhileStatement)

@given(instance=Metamodelo::Cpp::CppWhileStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppwhilestatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppWhileStatement)

@given(instance=CppExpression_strategy)
@settings(max_examples=50)
def test_cppexpression_instantiation(instance):
    assert isinstance(instance, CppExpression)

@given(instance=Metamodelo::Cpp::CppUnaryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppunaryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppUnaryExpression)

@given(instance=Metamodelo::Cpp::CppBooleanLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppbooleanliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppBooleanLiteral)

@given(instance=Metamodelo::Cpp::CppBooleanLiteral_strategy)
def test_metamodelo::cpp::cppbooleanliteral_booleanValue_type(instance):
    assert isinstance(instance.booleanValue, bool)


@given(instance=Metamodelo::Cpp::CppBooleanLiteral_strategy)
def test_metamodelo::cpp::cppbooleanliteral_booleanValue_setter(instance):
    original = instance.booleanValue
    instance.booleanValue = original
    assert instance.booleanValue == original

@given(instance=Metamodelo::Cpp::CppBinaryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppbinaryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppBinaryExpression)

@given(instance=Metamodelo::Cpp::CppTryExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpptryexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppTryExpression)

@given(instance=Metamodelo::Cpp::CppIterationStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppiterationstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppIterationStatement)

@given(instance=Metamodelo::Cpp::CppThisExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppthisexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppThisExpression)

@given(instance=Metamodelo::Cpp::CppThrowExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppthrowexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppThrowExpression)

@given(instance=Metamodelo::Cpp::CppJumpStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppjumpstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppJumpStatement)

@given(instance=Metamodelo::Cpp::CppSwitchExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppswitchexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSwitchExpression)

@given(instance=Metamodelo::Cpp::CppFieldAccess_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppfieldaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppFieldAccess)

@given(instance=Metamodelo::Cpp::CppNullLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppnullliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppNullLiteral)

@given(instance=Metamodelo::Cpp::CppVariableAccess_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvariableaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVariableAccess)

@given(instance=Metamodelo::Cpp::CppCastExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcastexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppCastExpression)

@given(instance=Metamodelo::Cpp::CppConstantExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppconstantexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppConstantExpression)

@given(instance=Metamodelo::Cpp::CppRegexLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppregexliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppRegexLiteral)

@given(instance=Metamodelo::Cpp::CppRegexLiteral_strategy)
def test_metamodelo::cpp::cppregexliteral_pattern_type(instance):
    assert isinstance(instance.pattern, str)


@given(instance=Metamodelo::Cpp::CppRegexLiteral_strategy)
def test_metamodelo::cpp::cppregexliteral_pattern_setter(instance):
    original = instance.pattern
    instance.pattern = original
    assert instance.pattern == original

@given(instance=Metamodelo::Cpp::CppRegexLiteral_strategy)
def test_metamodelo::cpp::cppregexliteral_options_type(instance):
    assert isinstance(instance.options, str)


@given(instance=Metamodelo::Cpp::CppRegexLiteral_strategy)
def test_metamodelo::cpp::cppregexliteral_options_setter(instance):
    original = instance.options
    instance.options = original
    assert instance.options == original

@given(instance=Metamodelo::Cpp::CppCharacterLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcharacterliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppCharacterLiteral)

@given(instance=Metamodelo::Cpp::CppCharacterLiteral_strategy)
def test_metamodelo::cpp::cppcharacterliteral_charValue_type(instance):
    assert isinstance(instance.charValue, str)


@given(instance=Metamodelo::Cpp::CppCharacterLiteral_strategy)
def test_metamodelo::cpp::cppcharacterliteral_charValue_setter(instance):
    original = instance.charValue
    instance.charValue = original
    assert instance.charValue == original

@given(instance=Metamodelo::Cpp::CppCase_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcase_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppCase)

@given(instance=Metamodelo::Cpp::CppDeclarationExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppdeclarationexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppDeclarationExpression)

@given(instance=Metamodelo::Cpp::CppCatchClause_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcatchclause_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppCatchClause)

@given(instance=Metamodelo::Cpp::CppNumberLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppnumberliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppNumberLiteral)

@given(instance=Metamodelo::Cpp::CppNumberLiteral_strategy)
def test_metamodelo::cpp::cppnumberliteral_token_type(instance):
    assert isinstance(instance.token, str)


@given(instance=Metamodelo::Cpp::CppNumberLiteral_strategy)
def test_metamodelo::cpp::cppnumberliteral_token_setter(instance):
    original = instance.token
    instance.token = original
    assert instance.token == original

@given(instance=Metamodelo::Cpp::CppParenthizedExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppparenthizedexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppParenthizedExpression)

@given(instance=Metamodelo::Cpp::CppLabeledStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpplabeledstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppLabeledStatement)

@given(instance=Metamodelo::Cpp::CppArrayAccess_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpparrayaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppArrayAccess)

@given(instance=Metamodelo::Cpp::CppBlock_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppblock_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppBlock)

@given(instance=Metamodelo::Cpp::CppStringLiteral_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppstringliteral_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppStringLiteral)

@given(instance=Metamodelo::Cpp::CppStringLiteral_strategy)
def test_metamodelo::cpp::cppstringliteral_literalValue_type(instance):
    assert isinstance(instance.literalValue, str)


@given(instance=Metamodelo::Cpp::CppStringLiteral_strategy)
def test_metamodelo::cpp::cppstringliteral_literalValue_setter(instance):
    original = instance.literalValue
    instance.literalValue = original
    assert instance.literalValue == original

@given(instance=Metamodelo::Cpp::CppSelectionStatement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppselectionstatement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSelectionStatement)

@given(instance=Metamodelo::Cpp::CppArrayInitializer_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpparrayinitializer_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppArrayInitializer)

@given(instance=CppTypedElement_strategy)
@settings(max_examples=50)
def test_cpptypedelement_instantiation(instance):
    assert isinstance(instance, CppTypedElement)

@given(instance=Metamodelo::Cpp::CppVariableDeclarationGroup_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvariabledeclarationgroup_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVariableDeclarationGroup)

@given(instance=CppField_strategy)
@settings(max_examples=50)
def test_cppfield_instantiation(instance):
    assert isinstance(instance, CppField)

@given(instance=CppVariableDeclaration_strategy)
@settings(max_examples=50)
def test_cppvariabledeclaration_instantiation(instance):
    assert isinstance(instance, CppVariableDeclaration)

@given(instance=Metamodelo::Cpp::CppSingleVariableDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppsinglevariabledeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSingleVariableDeclaration)

@given(instance=Metamodelo::Cpp::CppVariableDeclarationFragment_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvariabledeclarationfragment_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVariableDeclarationFragment)

@given(instance=CppAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_cppabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, CppAbstractMethodInvocation)

@given(instance=Metamodelo::Cpp::CppSuperMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppsupermethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSuperMethodInvocation)

@given(instance=Metamodelo::Cpp::CppMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppmethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppMethodInvocation)

@given(instance=Metamodelo::Cpp::CppAbstractMethodInvocation_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppabstractmethodinvocation_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppAbstractMethodInvocation)

@given(instance=CppMemberFunction_strategy)
@settings(max_examples=50)
def test_cppmemberfunction_instantiation(instance):
    assert isinstance(instance, CppMemberFunction)

@given(instance=Metamodelo::Cpp::CppMethod_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppmethod_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppMethod)

@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, bool)


@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isPureVirtual_type(instance):
    assert isinstance(instance.isPureVirtual, bool)


@given(instance=Metamodelo::Cpp::CppMethod_strategy)
def test_metamodelo::cpp::cppmethod_isPureVirtual_setter(instance):
    original = instance.isPureVirtual
    instance.isPureVirtual = original
    assert instance.isPureVirtual == original

@given(instance=Metamodelo::Cpp::CppDestructor_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppdestructor_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppDestructor)

@given(instance=Metamodelo::Cpp::CppDestructor_strategy)
def test_metamodelo::cpp::cppdestructor_isVirtual_type(instance):
    assert isinstance(instance.isVirtual, bool)


@given(instance=Metamodelo::Cpp::CppDestructor_strategy)
def test_metamodelo::cpp::cppdestructor_isVirtual_setter(instance):
    original = instance.isVirtual
    instance.isVirtual = original
    assert instance.isVirtual == original

@given(instance=Metamodelo::Cpp::CppConstructor_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppconstructor_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppConstructor)

@given(instance=CppFunction_strategy)
@settings(max_examples=50)
def test_cppfunction_instantiation(instance):
    assert isinstance(instance, CppFunction)

@given(instance=Metamodelo::Cpp::CppMemberFunction_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppmemberfunction_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppMemberFunction)

@given(instance=Metamodelo::Cpp::CppTypedElement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpptypedelement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppTypedElement)

@given(instance=CppClassifier_strategy)
@settings(max_examples=50)
def test_cppclassifier_instantiation(instance):
    assert isinstance(instance, CppClassifier)

@given(instance=Metamodelo::Cpp::CppClass_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppclass_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppClass)

@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isFinal_type(instance):
    assert isinstance(instance.isFinal, bool)


@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isFinal_setter(instance):
    original = instance.isFinal
    instance.isFinal = original
    assert instance.isFinal == original

@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isAbstract_type(instance):
    assert isinstance(instance.isAbstract, bool)


@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_classkey_type(instance):
    assert isinstance(instance.classkey, str)


@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_classkey_setter(instance):
    original = instance.classkey
    instance.classkey = original
    assert instance.classkey == original

@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isGeneric_type(instance):
    assert isinstance(instance.isGeneric, bool)


@given(instance=Metamodelo::Cpp::CppClass_strategy)
def test_metamodelo::cpp::cppclass_isGeneric_setter(instance):
    original = instance.isGeneric
    instance.isGeneric = original
    assert instance.isGeneric == original

@given(instance=CppPrimitiveType_strategy)
@settings(max_examples=50)
def test_cppprimitivetype_instantiation(instance):
    assert isinstance(instance, CppPrimitiveType)

@given(instance=Metamodelo::Cpp::CppLongType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpplongtype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppLongType)

@given(instance=Metamodelo::Cpp::CppUnsignedType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppunsignedtype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppUnsignedType)

@given(instance=Metamodelo::Cpp::CppFloatType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppfloattype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppFloatType)

@given(instance=Metamodelo::Cpp::CppVoidType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvoidtype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVoidType)

@given(instance=Metamodelo::Cpp::CppSignedType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppsignedtype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppSignedType)

@given(instance=Metamodelo::Cpp::CppShortType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppshorttype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppShortType)

@given(instance=Metamodelo::Cpp::CppDoubleType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppdoubletype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppDoubleType)

@given(instance=Metamodelo::Cpp::CppCharType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppchartype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppCharType)

@given(instance=Metamodelo::Cpp::CppIntType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppinttype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppIntType)

@given(instance=Metamodelo::Cpp::CppBooleanType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppbooleantype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppBooleanType)

@given(instance=CppType_strategy)
@settings(max_examples=50)
def test_cpptype_instantiation(instance):
    assert isinstance(instance, CppType)

@given(instance=Metamodelo::Cpp::CppFunction_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppfunction_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppFunction)

@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_isInline_type(instance):
    assert isinstance(instance.isInline, bool)


@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_isInline_setter(instance):
    original = instance.isInline
    instance.isInline = original
    assert instance.isInline == original

@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_isVarArg_type(instance):
    assert isinstance(instance.isVarArg, bool)


@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_isVarArg_setter(instance):
    original = instance.isVarArg
    instance.isVarArg = original
    assert instance.isVarArg == original

@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_linkage_type(instance):
    assert isinstance(instance.linkage, str)


@given(instance=Metamodelo::Cpp::CppFunction_strategy)
def test_metamodelo::cpp::cppfunction_linkage_setter(instance):
    original = instance.linkage
    instance.linkage = original
    assert instance.linkage == original

@given(instance=Metamodelo::Cpp::CppClassifier_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppclassifier_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppClassifier)

@given(instance=Metamodelo::Cpp::CppPrimitiveType_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppprimitivetype_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppPrimitiveType)

@given(instance=Metamodelo::Cpp::CppTypeParameter_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpptypeparameter_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppTypeParameter)

@given(instance=Metamodelo::Cpp::CppTypeAccess_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cpptypeaccess_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppTypeAccess)

@given(instance=Metamodelo::Cpp::CppImportDeclaration_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppimportdeclaration_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppImportDeclaration)

@given(instance=Metamodelo::Cpp::CppNamedElement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppnamedelement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppNamedElement)

@given(instance=Metamodelo::Cpp::CppNamedElement_strategy)
def test_metamodelo::cpp::cppnamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Metamodelo::Cpp::CppNamedElement_strategy)
def test_metamodelo::cpp::cppnamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Metamodelo::Cpp::CppModelElement_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppmodelelement_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppModelElement)

@given(instance=Metamodelo::Cpp::CppComment_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppcomment_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppComment)

@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_multiLine_type(instance):
    assert isinstance(instance.multiLine, bool)


@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_multiLine_setter(instance):
    original = instance.multiLine
    instance.multiLine = original
    assert instance.multiLine == original

@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_singleLine_type(instance):
    assert isinstance(instance.singleLine, bool)


@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_singleLine_setter(instance):
    original = instance.singleLine
    instance.singleLine = original
    assert instance.singleLine == original

@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=Metamodelo::Cpp::CppComment_strategy)
def test_metamodelo::cpp::cppcomment_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=Metamodelo::Cpp::CppExpression_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppexpression_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppExpression)

@given(instance=Metamodelo::Cpp::CppEnumConstructor_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppenumconstructor_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppEnumConstructor)

@given(instance=Metamodelo::Cpp::CppEnum_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppenum_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppEnum)

@given(instance=Metamodelo::Cpp::CppVariable_strategy)
@settings(max_examples=50)
def test_metamodelo::cpp::cppvariable_instantiation(instance):
    assert isinstance(instance, Metamodelo::Cpp::CppVariable)

@given(instance=Metamodelo::Cpp::CppVariable_strategy)
def test_metamodelo::cpp::cppvariable_isConst_type(instance):
    assert isinstance(instance.isConst, bool)


@given(instance=Metamodelo::Cpp::CppVariable_strategy)
def test_metamodelo::cpp::cppvariable_isConst_setter(instance):
    original = instance.isConst
    instance.isConst = original
    assert instance.isConst == original

@given(instance=Metamodelo::Cpp::CppVariable_strategy)
def test_metamodelo::cpp::cppvariable_storage_type(instance):
    assert isinstance(instance.storage, str)


@given(instance=Metamodelo::Cpp::CppVariable_strategy)
def test_metamodelo::cpp::cppvariable_storage_setter(instance):
    original = instance.storage
    instance.storage = original
    assert instance.storage == original
