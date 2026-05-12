import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ecdarText_EObject,
    ETExpression,
    ecdarText_ETArrayExpression,
    ecdarText_ETDivideExpression,
    ecdarText_ETImplyExpression,
    ecdarText_ETPreIncrementExpression,
    ecdarText_ETSubtractExpression,
    ecdarText_ETMultiplicationAssignmentExpression,
    ecdarText_ETMinExpression,
    ecdarText_ETPostDecrementExpression,
    ecdarText_ETLogicNotExpression,
    ecdarText_ETLogicOrExpression,
    ecdarText_ETDivisionAssignmentExpression,
    ecdarText_ETLessEqualExpression,
    ecdarText_ETBooleanLiteral,
    ecdarText_ETPostIncrementExpression,
    ecdarText_ETBitXORAssignmentExpression,
    ecdarText_ETExistsExpression,
    ecdarText_ETMultiplyExpression,
    ecdarText_ETMaxExpression,
    ecdarText_ETBitLeftAssignmentExpression,
    ecdarText_ETBitAndAssignmentExpression,
    ecdarText_ETNumberLiteral,
    ecdarText_ETModuloAssignmentExpression,
    ecdarText_ETAssignmentExpression,
    ecdarText_ETReference,
    ecdarText_ETLessExpression,
    ecdarText_ETMinusExpression,
    ecdarText_ETBitAndExpression,
    ecdarText_ETGreaterEqualExpression,
    ecdarText_ETStructExpression,
    ecdarText_ETGreaterExpression,
    ecdarText_ETSubtractionAssignmentExpression,
    ecdarText_ETUnequalExpression,
    ecdarText_ETBitRightExpression,
    ecdarText_ETBitLeftExpression,
    ecdarText_ETBitXORExpression,
    ecdarText_ETConditionalExpression,
    ecdarText_ETBitOrAssignmentExpression,
    ecdarText_ETLogicAndExpression,
    ecdarText_ETPreDecrementExpression,
    ecdarText_ETModuloExpression,
    ecdarText_ETAddExpression,
    ecdarText_ETBitRightAssignmentExpression,
    ecdarText_ETEqualExpression,
    ecdarText_ETBitOrExpression,
    ecdarText_ETForallExpression,
    ecdarText_ETAdditionAssignmentExpression,
    ETSpecificationExpression,
    ecdarText_ETSpecificationCompositionExpression,
    ecdarText_ETSpecificationReference,
    ecdarText_ETSpecificationConjunctionExpression,
    ecdarText_ETSpecificationDisjunctionExpression,
    ecdarText_ETSpecificationInstantiation,
    ecdarText_ETEdge,
    ecdarText_ETLocation,
    ecdarText_ETParameter,
    ETSpecificationDefinition,
    ecdarText_ETSpecificationTemplate,
    ecdarText_ETSpecificationBody,
    ETSpecification,
    ecdarText_ETSpecificationDefinition,
    ecdarText_ETSpecificationBinding,
    ecdarText_ETSpecificationExpression,
    ecdarText_ETIO,
    ecdarText_ETSelect,
    ecdarText_ETFieldDeclaration,
    ETActionType,
    ecdarText_ETOutputType,
    ecdarText_ETInputType,
    ETTypeIdentifier,
    ecdarText_ETClockType,
    ecdarText_ETTypeReference,
    ecdarText_ETStructType,
    ecdarText_ETActionType,
    ecdarText_ETScalarType,
    ecdarText_ETBooleanType,
    ecdarText_ETIntegerType,
    ecdarText_ETTypeID,
    ETInitialiser,
    ecdarText_ETMultiInitialiser,
    ecdarText_ETSingleInitialiser,
    ecdarText_ETFieldID,
    ecdarText_ETVariableID,
    ETDeclaration,
    ecdarText_ETTypeDeclaration,
    ecdarText_ETVariableDeclaration,
    ecdarText_ETTypeIdentifier,
    ecdarText_ETTypeModifiers,
    ecdarText_ETType,
    ecdarText_ETDeclaration,
    ecdarText_ETExpression,
    ecdarText_ETArrayDeclaration,
    ecdarText_ETSpecification,
    ecdarText_ETDeclarations,
    ecdarText_ETImport,
    ecdarText_ETFile,
    ecdarText_ETInitialiser,
    ETIOType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecdartext_eobject_is_not_abstract():
    assert not inspect.isabstract(ecdarText_EObject)


def test_ecdartext_eobject_constructor_exists():
    assert callable(ecdarText_EObject.__init__)


def test_ecdartext_eobject_constructor_args():
    sig = inspect.signature(ecdarText_EObject.__init__)
    params = list(sig.parameters.keys())



def test_etexpression_is_not_abstract():
    assert not inspect.isabstract(ETExpression)


def test_etexpression_constructor_exists():
    assert callable(ETExpression.__init__)


def test_etexpression_constructor_args():
    sig = inspect.signature(ETExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etarrayexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETArrayExpression)


def test_ecdartext_etarrayexpression_constructor_exists():
    assert callable(ecdarText_ETArrayExpression.__init__)


def test_ecdartext_etarrayexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etdivideexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETDivideExpression)


def test_ecdartext_etdivideexpression_constructor_exists():
    assert callable(ecdarText_ETDivideExpression.__init__)


def test_ecdartext_etdivideexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETDivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etimplyexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETImplyExpression)


def test_ecdartext_etimplyexpression_constructor_exists():
    assert callable(ecdarText_ETImplyExpression.__init__)


def test_ecdartext_etimplyexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etpreincrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETPreIncrementExpression)


def test_ecdartext_etpreincrementexpression_constructor_exists():
    assert callable(ecdarText_ETPreIncrementExpression.__init__)


def test_ecdartext_etpreincrementexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETPreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSubtractExpression)


def test_ecdartext_etsubtractexpression_constructor_exists():
    assert callable(ecdarText_ETSubtractExpression.__init__)


def test_ecdartext_etsubtractexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etmultiplicationassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMultiplicationAssignmentExpression)


def test_ecdartext_etmultiplicationassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETMultiplicationAssignmentExpression.__init__)


def test_ecdartext_etmultiplicationassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETMultiplicationAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etminexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMinExpression)


def test_ecdartext_etminexpression_constructor_exists():
    assert callable(ecdarText_ETMinExpression.__init__)


def test_ecdartext_etminexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETMinExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etpostdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETPostDecrementExpression)


def test_ecdartext_etpostdecrementexpression_constructor_exists():
    assert callable(ecdarText_ETPostDecrementExpression.__init__)


def test_ecdartext_etpostdecrementexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETPostDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etlogicnotexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLogicNotExpression)


def test_ecdartext_etlogicnotexpression_constructor_exists():
    assert callable(ecdarText_ETLogicNotExpression.__init__)


def test_ecdartext_etlogicnotexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETLogicNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etlogicorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLogicOrExpression)


def test_ecdartext_etlogicorexpression_constructor_exists():
    assert callable(ecdarText_ETLogicOrExpression.__init__)


def test_ecdartext_etlogicorexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETLogicOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etdivisionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETDivisionAssignmentExpression)


def test_ecdartext_etdivisionassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETDivisionAssignmentExpression.__init__)


def test_ecdartext_etdivisionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETDivisionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etlessequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLessEqualExpression)


def test_ecdartext_etlessequalexpression_constructor_exists():
    assert callable(ecdarText_ETLessEqualExpression.__init__)


def test_ecdartext_etlessequalexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETLessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBooleanLiteral)


def test_ecdartext_etbooleanliteral_constructor_exists():
    assert callable(ecdarText_ETBooleanLiteral.__init__)


def test_ecdartext_etbooleanliteral_constructor_args():
    sig = inspect.signature(ecdarText_ETBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ecdartext_etbooleanliteral_has_value():
    assert hasattr(ecdarText_ETBooleanLiteral, "value")
    descriptor = None
    for klass in ecdarText_ETBooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etpostincrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETPostIncrementExpression)


def test_ecdartext_etpostincrementexpression_constructor_exists():
    assert callable(ecdarText_ETPostIncrementExpression.__init__)


def test_ecdartext_etpostincrementexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETPostIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitxorassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitXORAssignmentExpression)


def test_ecdartext_etbitxorassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETBitXORAssignmentExpression.__init__)


def test_ecdartext_etbitxorassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitXORAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etexistsexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETExistsExpression)


def test_ecdartext_etexistsexpression_constructor_exists():
    assert callable(ecdarText_ETExistsExpression.__init__)


def test_ecdartext_etexistsexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETExistsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etexistsexpression_has_name():
    assert hasattr(ecdarText_ETExistsExpression, "name")
    descriptor = None
    for klass in ecdarText_ETExistsExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etmultiplyexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMultiplyExpression)


def test_ecdartext_etmultiplyexpression_constructor_exists():
    assert callable(ecdarText_ETMultiplyExpression.__init__)


def test_ecdartext_etmultiplyexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETMultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etmaxexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMaxExpression)


def test_ecdartext_etmaxexpression_constructor_exists():
    assert callable(ecdarText_ETMaxExpression.__init__)


def test_ecdartext_etmaxexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETMaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitleftassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitLeftAssignmentExpression)


def test_ecdartext_etbitleftassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETBitLeftAssignmentExpression.__init__)


def test_ecdartext_etbitleftassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitLeftAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitandassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitAndAssignmentExpression)


def test_ecdartext_etbitandassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETBitAndAssignmentExpression.__init__)


def test_ecdartext_etbitandassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitAndAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etnumberliteral_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETNumberLiteral)


def test_ecdartext_etnumberliteral_constructor_exists():
    assert callable(ecdarText_ETNumberLiteral.__init__)


def test_ecdartext_etnumberliteral_constructor_args():
    sig = inspect.signature(ecdarText_ETNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ecdartext_etnumberliteral_has_value():
    assert hasattr(ecdarText_ETNumberLiteral, "value")
    descriptor = None
    for klass in ecdarText_ETNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etmoduloassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETModuloAssignmentExpression)


def test_ecdartext_etmoduloassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETModuloAssignmentExpression.__init__)


def test_ecdartext_etmoduloassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETModuloAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETAssignmentExpression)


def test_ecdartext_etassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETAssignmentExpression.__init__)


def test_ecdartext_etassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etreference_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETReference)


def test_ecdartext_etreference_constructor_exists():
    assert callable(ecdarText_ETReference.__init__)


def test_ecdartext_etreference_constructor_args():
    sig = inspect.signature(ecdarText_ETReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etlessexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLessExpression)


def test_ecdartext_etlessexpression_constructor_exists():
    assert callable(ecdarText_ETLessExpression.__init__)


def test_ecdartext_etlessexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETLessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etminusexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMinusExpression)


def test_ecdartext_etminusexpression_constructor_exists():
    assert callable(ecdarText_ETMinusExpression.__init__)


def test_ecdartext_etminusexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitandexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitAndExpression)


def test_ecdartext_etbitandexpression_constructor_exists():
    assert callable(ecdarText_ETBitAndExpression.__init__)


def test_ecdartext_etbitandexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etgreaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETGreaterEqualExpression)


def test_ecdartext_etgreaterequalexpression_constructor_exists():
    assert callable(ecdarText_ETGreaterEqualExpression.__init__)


def test_ecdartext_etgreaterequalexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETGreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etstructexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETStructExpression)


def test_ecdartext_etstructexpression_constructor_exists():
    assert callable(ecdarText_ETStructExpression.__init__)


def test_ecdartext_etstructexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETStructExpression.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_ecdartext_etstructexpression_has_right():
    assert hasattr(ecdarText_ETStructExpression, "right")
    descriptor = None
    for klass in ecdarText_ETStructExpression.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etgreaterexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETGreaterExpression)


def test_ecdartext_etgreaterexpression_constructor_exists():
    assert callable(ecdarText_ETGreaterExpression.__init__)


def test_ecdartext_etgreaterexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETGreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etsubtractionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSubtractionAssignmentExpression)


def test_ecdartext_etsubtractionassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETSubtractionAssignmentExpression.__init__)


def test_ecdartext_etsubtractionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSubtractionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etunequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETUnequalExpression)


def test_ecdartext_etunequalexpression_constructor_exists():
    assert callable(ecdarText_ETUnequalExpression.__init__)


def test_ecdartext_etunequalexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETUnequalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitrightexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitRightExpression)


def test_ecdartext_etbitrightexpression_constructor_exists():
    assert callable(ecdarText_ETBitRightExpression.__init__)


def test_ecdartext_etbitrightexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitRightExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitleftexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitLeftExpression)


def test_ecdartext_etbitleftexpression_constructor_exists():
    assert callable(ecdarText_ETBitLeftExpression.__init__)


def test_ecdartext_etbitleftexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitLeftExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitxorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitXORExpression)


def test_ecdartext_etbitxorexpression_constructor_exists():
    assert callable(ecdarText_ETBitXORExpression.__init__)


def test_ecdartext_etbitxorexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitXORExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETConditionalExpression)


def test_ecdartext_etconditionalexpression_constructor_exists():
    assert callable(ecdarText_ETConditionalExpression.__init__)


def test_ecdartext_etconditionalexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitorassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitOrAssignmentExpression)


def test_ecdartext_etbitorassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETBitOrAssignmentExpression.__init__)


def test_ecdartext_etbitorassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitOrAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etlogicandexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLogicAndExpression)


def test_ecdartext_etlogicandexpression_constructor_exists():
    assert callable(ecdarText_ETLogicAndExpression.__init__)


def test_ecdartext_etlogicandexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETLogicAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etpredecrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETPreDecrementExpression)


def test_ecdartext_etpredecrementexpression_constructor_exists():
    assert callable(ecdarText_ETPreDecrementExpression.__init__)


def test_ecdartext_etpredecrementexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETPreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etmoduloexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETModuloExpression)


def test_ecdartext_etmoduloexpression_constructor_exists():
    assert callable(ecdarText_ETModuloExpression.__init__)


def test_ecdartext_etmoduloexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETModuloExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etaddexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETAddExpression)


def test_ecdartext_etaddexpression_constructor_exists():
    assert callable(ecdarText_ETAddExpression.__init__)


def test_ecdartext_etaddexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETAddExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitrightassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitRightAssignmentExpression)


def test_ecdartext_etbitrightassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETBitRightAssignmentExpression.__init__)


def test_ecdartext_etbitrightassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitRightAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETEqualExpression)


def test_ecdartext_etequalexpression_constructor_exists():
    assert callable(ecdarText_ETEqualExpression.__init__)


def test_ecdartext_etequalexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbitorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBitOrExpression)


def test_ecdartext_etbitorexpression_constructor_exists():
    assert callable(ecdarText_ETBitOrExpression.__init__)


def test_ecdartext_etbitorexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETBitOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etforallexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETForallExpression)


def test_ecdartext_etforallexpression_constructor_exists():
    assert callable(ecdarText_ETForallExpression.__init__)


def test_ecdartext_etforallexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETForallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etforallexpression_has_name():
    assert hasattr(ecdarText_ETForallExpression, "name")
    descriptor = None
    for klass in ecdarText_ETForallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etadditionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETAdditionAssignmentExpression)


def test_ecdartext_etadditionassignmentexpression_constructor_exists():
    assert callable(ecdarText_ETAdditionAssignmentExpression.__init__)


def test_ecdartext_etadditionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETAdditionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_etspecificationexpression_is_not_abstract():
    assert not inspect.isabstract(ETSpecificationExpression)


def test_etspecificationexpression_constructor_exists():
    assert callable(ETSpecificationExpression.__init__)


def test_etspecificationexpression_constructor_args():
    sig = inspect.signature(ETSpecificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationcompositionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationCompositionExpression)


def test_ecdartext_etspecificationcompositionexpression_constructor_exists():
    assert callable(ecdarText_ETSpecificationCompositionExpression.__init__)


def test_ecdartext_etspecificationcompositionexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationCompositionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationreference_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationReference)


def test_ecdartext_etspecificationreference_constructor_exists():
    assert callable(ecdarText_ETSpecificationReference.__init__)


def test_ecdartext_etspecificationreference_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationconjunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationConjunctionExpression)


def test_ecdartext_etspecificationconjunctionexpression_constructor_exists():
    assert callable(ecdarText_ETSpecificationConjunctionExpression.__init__)


def test_ecdartext_etspecificationconjunctionexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationConjunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationdisjunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationDisjunctionExpression)


def test_ecdartext_etspecificationdisjunctionexpression_constructor_exists():
    assert callable(ecdarText_ETSpecificationDisjunctionExpression.__init__)


def test_ecdartext_etspecificationdisjunctionexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationDisjunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationinstantiation_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationInstantiation)


def test_ecdartext_etspecificationinstantiation_constructor_exists():
    assert callable(ecdarText_ETSpecificationInstantiation.__init__)


def test_ecdartext_etspecificationinstantiation_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etedge_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETEdge)


def test_ecdartext_etedge_constructor_exists():
    assert callable(ecdarText_ETEdge.__init__)


def test_ecdartext_etedge_constructor_args():
    sig = inspect.signature(ecdarText_ETEdge.__init__)
    params = list(sig.parameters.keys())
    assert "controllable" in params, "Missing parameter 'controllable'"

def test_ecdartext_etedge_has_controllable():
    assert hasattr(ecdarText_ETEdge, "controllable")
    descriptor = None
    for klass in ecdarText_ETEdge.__mro__:
        if "controllable" in klass.__dict__:
            descriptor = klass.__dict__["controllable"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etlocation_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETLocation)


def test_ecdartext_etlocation_constructor_exists():
    assert callable(ecdarText_ETLocation.__init__)


def test_ecdartext_etlocation_constructor_args():
    sig = inspect.signature(ecdarText_ETLocation.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "universal" in params, "Missing parameter 'universal'"
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etlocation_has_urgent():
    assert hasattr(ecdarText_ETLocation, "urgent")
    descriptor = None
    for klass in ecdarText_ETLocation.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_etlocation_has_universal():
    assert hasattr(ecdarText_ETLocation, "universal")
    descriptor = None
    for klass in ecdarText_ETLocation.__mro__:
        if "universal" in klass.__dict__:
            descriptor = klass.__dict__["universal"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_etlocation_has_name():
    assert hasattr(ecdarText_ETLocation, "name")
    descriptor = None
    for klass in ecdarText_ETLocation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etparameter_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETParameter)


def test_ecdartext_etparameter_constructor_exists():
    assert callable(ecdarText_ETParameter.__init__)


def test_ecdartext_etparameter_constructor_args():
    sig = inspect.signature(ecdarText_ETParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ioType" in params, "Missing parameter 'ioType'"

def test_ecdartext_etparameter_has_name():
    assert hasattr(ecdarText_ETParameter, "name")
    descriptor = None
    for klass in ecdarText_ETParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_etparameter_has_ioType():
    assert hasattr(ecdarText_ETParameter, "ioType")
    descriptor = None
    for klass in ecdarText_ETParameter.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)



def test_etspecificationdefinition_is_not_abstract():
    assert not inspect.isabstract(ETSpecificationDefinition)


def test_etspecificationdefinition_constructor_exists():
    assert callable(ETSpecificationDefinition.__init__)


def test_etspecificationdefinition_constructor_args():
    sig = inspect.signature(ETSpecificationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationtemplate_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationTemplate)


def test_ecdartext_etspecificationtemplate_constructor_exists():
    assert callable(ecdarText_ETSpecificationTemplate.__init__)


def test_ecdartext_etspecificationtemplate_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationbody_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationBody)


def test_ecdartext_etspecificationbody_constructor_exists():
    assert callable(ecdarText_ETSpecificationBody.__init__)


def test_ecdartext_etspecificationbody_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationBody.__init__)
    params = list(sig.parameters.keys())



def test_etspecification_is_not_abstract():
    assert not inspect.isabstract(ETSpecification)


def test_etspecification_constructor_exists():
    assert callable(ETSpecification.__init__)


def test_etspecification_constructor_args():
    sig = inspect.signature(ETSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationdefinition_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationDefinition)


def test_ecdartext_etspecificationdefinition_constructor_exists():
    assert callable(ecdarText_ETSpecificationDefinition.__init__)


def test_ecdartext_etspecificationdefinition_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationbinding_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationBinding)


def test_ecdartext_etspecificationbinding_constructor_exists():
    assert callable(ecdarText_ETSpecificationBinding.__init__)


def test_ecdartext_etspecificationbinding_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationBinding.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecificationexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecificationExpression)


def test_ecdartext_etspecificationexpression_constructor_exists():
    assert callable(ecdarText_ETSpecificationExpression.__init__)


def test_ecdartext_etspecificationexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etio_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETIO)


def test_ecdartext_etio_constructor_exists():
    assert callable(ecdarText_ETIO.__init__)


def test_ecdartext_etio_constructor_args():
    sig = inspect.signature(ecdarText_ETIO.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ecdartext_etio_has_type():
    assert hasattr(ecdarText_ETIO, "type")
    descriptor = None
    for klass in ecdarText_ETIO.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etselect_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSelect)


def test_ecdartext_etselect_constructor_exists():
    assert callable(ecdarText_ETSelect.__init__)


def test_ecdartext_etselect_constructor_args():
    sig = inspect.signature(ecdarText_ETSelect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etselect_has_name():
    assert hasattr(ecdarText_ETSelect, "name")
    descriptor = None
    for klass in ecdarText_ETSelect.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETFieldDeclaration)


def test_ecdartext_etfielddeclaration_constructor_exists():
    assert callable(ecdarText_ETFieldDeclaration.__init__)


def test_ecdartext_etfielddeclaration_constructor_args():
    sig = inspect.signature(ecdarText_ETFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_etactiontype_is_not_abstract():
    assert not inspect.isabstract(ETActionType)


def test_etactiontype_constructor_exists():
    assert callable(ETActionType.__init__)


def test_etactiontype_constructor_args():
    sig = inspect.signature(ETActionType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etoutputtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETOutputType)


def test_ecdartext_etoutputtype_constructor_exists():
    assert callable(ecdarText_ETOutputType.__init__)


def test_ecdartext_etoutputtype_constructor_args():
    sig = inspect.signature(ecdarText_ETOutputType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etinputtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETInputType)


def test_ecdartext_etinputtype_constructor_exists():
    assert callable(ecdarText_ETInputType.__init__)


def test_ecdartext_etinputtype_constructor_args():
    sig = inspect.signature(ecdarText_ETInputType.__init__)
    params = list(sig.parameters.keys())



def test_ettypeidentifier_is_not_abstract():
    assert not inspect.isabstract(ETTypeIdentifier)


def test_ettypeidentifier_constructor_exists():
    assert callable(ETTypeIdentifier.__init__)


def test_ettypeidentifier_constructor_args():
    sig = inspect.signature(ETTypeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etclocktype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETClockType)


def test_ecdartext_etclocktype_constructor_exists():
    assert callable(ecdarText_ETClockType.__init__)


def test_ecdartext_etclocktype_constructor_args():
    sig = inspect.signature(ecdarText_ETClockType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_ettypereference_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETTypeReference)


def test_ecdartext_ettypereference_constructor_exists():
    assert callable(ecdarText_ETTypeReference.__init__)


def test_ecdartext_ettypereference_constructor_args():
    sig = inspect.signature(ecdarText_ETTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etstructtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETStructType)


def test_ecdartext_etstructtype_constructor_exists():
    assert callable(ecdarText_ETStructType.__init__)


def test_ecdartext_etstructtype_constructor_args():
    sig = inspect.signature(ecdarText_ETStructType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etactiontype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETActionType)


def test_ecdartext_etactiontype_constructor_exists():
    assert callable(ecdarText_ETActionType.__init__)


def test_ecdartext_etactiontype_constructor_args():
    sig = inspect.signature(ecdarText_ETActionType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etscalartype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETScalarType)


def test_ecdartext_etscalartype_constructor_exists():
    assert callable(ecdarText_ETScalarType.__init__)


def test_ecdartext_etscalartype_constructor_args():
    sig = inspect.signature(ecdarText_ETScalarType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etbooleantype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETBooleanType)


def test_ecdartext_etbooleantype_constructor_exists():
    assert callable(ecdarText_ETBooleanType.__init__)


def test_ecdartext_etbooleantype_constructor_args():
    sig = inspect.signature(ecdarText_ETBooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etintegertype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETIntegerType)


def test_ecdartext_etintegertype_constructor_exists():
    assert callable(ecdarText_ETIntegerType.__init__)


def test_ecdartext_etintegertype_constructor_args():
    sig = inspect.signature(ecdarText_ETIntegerType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_ettypeid_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETTypeID)


def test_ecdartext_ettypeid_constructor_exists():
    assert callable(ecdarText_ETTypeID.__init__)


def test_ecdartext_ettypeid_constructor_args():
    sig = inspect.signature(ecdarText_ETTypeID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_ettypeid_has_name():
    assert hasattr(ecdarText_ETTypeID, "name")
    descriptor = None
    for klass in ecdarText_ETTypeID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etinitialiser_is_not_abstract():
    assert not inspect.isabstract(ETInitialiser)


def test_etinitialiser_constructor_exists():
    assert callable(ETInitialiser.__init__)


def test_etinitialiser_constructor_args():
    sig = inspect.signature(ETInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etmultiinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETMultiInitialiser)


def test_ecdartext_etmultiinitialiser_constructor_exists():
    assert callable(ecdarText_ETMultiInitialiser.__init__)


def test_ecdartext_etmultiinitialiser_constructor_args():
    sig = inspect.signature(ecdarText_ETMultiInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etsingleinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSingleInitialiser)


def test_ecdartext_etsingleinitialiser_constructor_exists():
    assert callable(ecdarText_ETSingleInitialiser.__init__)


def test_ecdartext_etsingleinitialiser_constructor_args():
    sig = inspect.signature(ecdarText_ETSingleInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etfieldid_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETFieldID)


def test_ecdartext_etfieldid_constructor_exists():
    assert callable(ecdarText_ETFieldID.__init__)


def test_ecdartext_etfieldid_constructor_args():
    sig = inspect.signature(ecdarText_ETFieldID.__init__)
    params = list(sig.parameters.keys())
    assert "ioType" in params, "Missing parameter 'ioType'"
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etfieldid_has_ioType():
    assert hasattr(ecdarText_ETFieldID, "ioType")
    descriptor = None
    for klass in ecdarText_ETFieldID.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_etfieldid_has_name():
    assert hasattr(ecdarText_ETFieldID, "name")
    descriptor = None
    for klass in ecdarText_ETFieldID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etvariableid_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETVariableID)


def test_ecdartext_etvariableid_constructor_exists():
    assert callable(ecdarText_ETVariableID.__init__)


def test_ecdartext_etvariableid_constructor_args():
    sig = inspect.signature(ecdarText_ETVariableID.__init__)
    params = list(sig.parameters.keys())
    assert "ioType" in params, "Missing parameter 'ioType'"
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etvariableid_has_ioType():
    assert hasattr(ecdarText_ETVariableID, "ioType")
    descriptor = None
    for klass in ecdarText_ETVariableID.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_etvariableid_has_name():
    assert hasattr(ecdarText_ETVariableID, "name")
    descriptor = None
    for klass in ecdarText_ETVariableID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_etdeclaration_is_not_abstract():
    assert not inspect.isabstract(ETDeclaration)


def test_etdeclaration_constructor_exists():
    assert callable(ETDeclaration.__init__)


def test_etdeclaration_constructor_args():
    sig = inspect.signature(ETDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_ettypedeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETTypeDeclaration)


def test_ecdartext_ettypedeclaration_constructor_exists():
    assert callable(ecdarText_ETTypeDeclaration.__init__)


def test_ecdartext_ettypedeclaration_constructor_args():
    sig = inspect.signature(ecdarText_ETTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETVariableDeclaration)


def test_ecdartext_etvariabledeclaration_constructor_exists():
    assert callable(ecdarText_ETVariableDeclaration.__init__)


def test_ecdartext_etvariabledeclaration_constructor_args():
    sig = inspect.signature(ecdarText_ETVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_ettypeidentifier_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETTypeIdentifier)


def test_ecdartext_ettypeidentifier_constructor_exists():
    assert callable(ecdarText_ETTypeIdentifier.__init__)


def test_ecdartext_ettypeidentifier_constructor_args():
    sig = inspect.signature(ecdarText_ETTypeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_ettypemodifiers_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETTypeModifiers)


def test_ecdartext_ettypemodifiers_constructor_exists():
    assert callable(ecdarText_ETTypeModifiers.__init__)


def test_ecdartext_ettypemodifiers_constructor_args():
    sig = inspect.signature(ecdarText_ETTypeModifiers.__init__)
    params = list(sig.parameters.keys())
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "meta" in params, "Missing parameter 'meta'"
    assert "const" in params, "Missing parameter 'const'"

def test_ecdartext_ettypemodifiers_has_urgent():
    assert hasattr(ecdarText_ETTypeModifiers, "urgent")
    descriptor = None
    for klass in ecdarText_ETTypeModifiers.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_ettypemodifiers_has_meta():
    assert hasattr(ecdarText_ETTypeModifiers, "meta")
    descriptor = None
    for klass in ecdarText_ETTypeModifiers.__mro__:
        if "meta" in klass.__dict__:
            descriptor = klass.__dict__["meta"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext_ettypemodifiers_has_const():
    assert hasattr(ecdarText_ETTypeModifiers, "const")
    descriptor = None
    for klass in ecdarText_ETTypeModifiers.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_ettype_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETType)


def test_ecdartext_ettype_constructor_exists():
    assert callable(ecdarText_ETType.__init__)


def test_ecdartext_ettype_constructor_args():
    sig = inspect.signature(ecdarText_ETType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etdeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETDeclaration)


def test_ecdartext_etdeclaration_constructor_exists():
    assert callable(ecdarText_ETDeclaration.__init__)


def test_ecdartext_etdeclaration_constructor_args():
    sig = inspect.signature(ecdarText_ETDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETExpression)


def test_ecdartext_etexpression_constructor_exists():
    assert callable(ecdarText_ETExpression.__init__)


def test_ecdartext_etexpression_constructor_args():
    sig = inspect.signature(ecdarText_ETExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etarraydeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETArrayDeclaration)


def test_ecdartext_etarraydeclaration_constructor_exists():
    assert callable(ecdarText_ETArrayDeclaration.__init__)


def test_ecdartext_etarraydeclaration_constructor_args():
    sig = inspect.signature(ecdarText_ETArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etspecification_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETSpecification)


def test_ecdartext_etspecification_constructor_exists():
    assert callable(ecdarText_ETSpecification.__init__)


def test_ecdartext_etspecification_constructor_args():
    sig = inspect.signature(ecdarText_ETSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext_etspecification_has_name():
    assert hasattr(ecdarText_ETSpecification, "name")
    descriptor = None
    for klass in ecdarText_ETSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etdeclarations_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETDeclarations)


def test_ecdartext_etdeclarations_constructor_exists():
    assert callable(ecdarText_ETDeclarations.__init__)


def test_ecdartext_etdeclarations_constructor_args():
    sig = inspect.signature(ecdarText_ETDeclarations.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etimport_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETImport)


def test_ecdartext_etimport_constructor_exists():
    assert callable(ecdarText_ETImport.__init__)


def test_ecdartext_etimport_constructor_args():
    sig = inspect.signature(ecdarText_ETImport.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ecdartext_etimport_has_importedNamespace():
    assert hasattr(ecdarText_ETImport, "importedNamespace")
    descriptor = None
    for klass in ecdarText_ETImport.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext_etfile_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETFile)


def test_ecdartext_etfile_constructor_exists():
    assert callable(ecdarText_ETFile.__init__)


def test_ecdartext_etfile_constructor_args():
    sig = inspect.signature(ecdarText_ETFile.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext_etinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText_ETInitialiser)


def test_ecdartext_etinitialiser_constructor_exists():
    assert callable(ecdarText_ETInitialiser.__init__)


def test_ecdartext_etinitialiser_constructor_args():
    sig = inspect.signature(ecdarText_ETInitialiser.__init__)
    params = list(sig.parameters.keys())

def test_etiotype_exists():
    # Check that the Enumeration exists
    assert ETIOType is not None

def test_etiotype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ETIOType]
    expected_literals = [
        "OUTPUT",
        "INPUT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ETIOType"


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
ecdarText_EObject_strategy = st.builds(
    ecdarText_EObject,
)
ETExpression_strategy = st.builds(
    ETExpression,
)
ecdarText_ETArrayExpression_strategy = st.builds(
    ecdarText_ETArrayExpression,
)
ecdarText_ETDivideExpression_strategy = st.builds(
    ecdarText_ETDivideExpression,
)
ecdarText_ETImplyExpression_strategy = st.builds(
    ecdarText_ETImplyExpression,
)
ecdarText_ETPreIncrementExpression_strategy = st.builds(
    ecdarText_ETPreIncrementExpression,
)
ecdarText_ETSubtractExpression_strategy = st.builds(
    ecdarText_ETSubtractExpression,
)
ecdarText_ETMultiplicationAssignmentExpression_strategy = st.builds(
    ecdarText_ETMultiplicationAssignmentExpression,
)
ecdarText_ETMinExpression_strategy = st.builds(
    ecdarText_ETMinExpression,
)
ecdarText_ETPostDecrementExpression_strategy = st.builds(
    ecdarText_ETPostDecrementExpression,
)
ecdarText_ETLogicNotExpression_strategy = st.builds(
    ecdarText_ETLogicNotExpression,
)
ecdarText_ETLogicOrExpression_strategy = st.builds(
    ecdarText_ETLogicOrExpression,
)
ecdarText_ETDivisionAssignmentExpression_strategy = st.builds(
    ecdarText_ETDivisionAssignmentExpression,
)
ecdarText_ETLessEqualExpression_strategy = st.builds(
    ecdarText_ETLessEqualExpression,
)
ecdarText_ETBooleanLiteral_strategy = st.builds(
    ecdarText_ETBooleanLiteral,
    value=
        safe_text
)
ecdarText_ETPostIncrementExpression_strategy = st.builds(
    ecdarText_ETPostIncrementExpression,
)
ecdarText_ETBitXORAssignmentExpression_strategy = st.builds(
    ecdarText_ETBitXORAssignmentExpression,
)
ecdarText_ETExistsExpression_strategy = st.builds(
    ecdarText_ETExistsExpression,
    name=
        safe_text
)
ecdarText_ETMultiplyExpression_strategy = st.builds(
    ecdarText_ETMultiplyExpression,
)
ecdarText_ETMaxExpression_strategy = st.builds(
    ecdarText_ETMaxExpression,
)
ecdarText_ETBitLeftAssignmentExpression_strategy = st.builds(
    ecdarText_ETBitLeftAssignmentExpression,
)
ecdarText_ETBitAndAssignmentExpression_strategy = st.builds(
    ecdarText_ETBitAndAssignmentExpression,
)
ecdarText_ETNumberLiteral_strategy = st.builds(
    ecdarText_ETNumberLiteral,
    value=
        st.integers()
)
ecdarText_ETModuloAssignmentExpression_strategy = st.builds(
    ecdarText_ETModuloAssignmentExpression,
)
ecdarText_ETAssignmentExpression_strategy = st.builds(
    ecdarText_ETAssignmentExpression,
)
ecdarText_ETReference_strategy = st.builds(
    ecdarText_ETReference,
)
ecdarText_ETLessExpression_strategy = st.builds(
    ecdarText_ETLessExpression,
)
ecdarText_ETMinusExpression_strategy = st.builds(
    ecdarText_ETMinusExpression,
)
ecdarText_ETBitAndExpression_strategy = st.builds(
    ecdarText_ETBitAndExpression,
)
ecdarText_ETGreaterEqualExpression_strategy = st.builds(
    ecdarText_ETGreaterEqualExpression,
)
ecdarText_ETStructExpression_strategy = st.builds(
    ecdarText_ETStructExpression,
    right=
        safe_text
)
ecdarText_ETGreaterExpression_strategy = st.builds(
    ecdarText_ETGreaterExpression,
)
ecdarText_ETSubtractionAssignmentExpression_strategy = st.builds(
    ecdarText_ETSubtractionAssignmentExpression,
)
ecdarText_ETUnequalExpression_strategy = st.builds(
    ecdarText_ETUnequalExpression,
)
ecdarText_ETBitRightExpression_strategy = st.builds(
    ecdarText_ETBitRightExpression,
)
ecdarText_ETBitLeftExpression_strategy = st.builds(
    ecdarText_ETBitLeftExpression,
)
ecdarText_ETBitXORExpression_strategy = st.builds(
    ecdarText_ETBitXORExpression,
)
ecdarText_ETConditionalExpression_strategy = st.builds(
    ecdarText_ETConditionalExpression,
)
ecdarText_ETBitOrAssignmentExpression_strategy = st.builds(
    ecdarText_ETBitOrAssignmentExpression,
)
ecdarText_ETLogicAndExpression_strategy = st.builds(
    ecdarText_ETLogicAndExpression,
)
ecdarText_ETPreDecrementExpression_strategy = st.builds(
    ecdarText_ETPreDecrementExpression,
)
ecdarText_ETModuloExpression_strategy = st.builds(
    ecdarText_ETModuloExpression,
)
ecdarText_ETAddExpression_strategy = st.builds(
    ecdarText_ETAddExpression,
)
ecdarText_ETBitRightAssignmentExpression_strategy = st.builds(
    ecdarText_ETBitRightAssignmentExpression,
)
ecdarText_ETEqualExpression_strategy = st.builds(
    ecdarText_ETEqualExpression,
)
ecdarText_ETBitOrExpression_strategy = st.builds(
    ecdarText_ETBitOrExpression,
)
ecdarText_ETForallExpression_strategy = st.builds(
    ecdarText_ETForallExpression,
    name=
        safe_text
)
ecdarText_ETAdditionAssignmentExpression_strategy = st.builds(
    ecdarText_ETAdditionAssignmentExpression,
)
ETSpecificationExpression_strategy = st.builds(
    ETSpecificationExpression,
)
ecdarText_ETSpecificationCompositionExpression_strategy = st.builds(
    ecdarText_ETSpecificationCompositionExpression,
)
ecdarText_ETSpecificationReference_strategy = st.builds(
    ecdarText_ETSpecificationReference,
)
ecdarText_ETSpecificationConjunctionExpression_strategy = st.builds(
    ecdarText_ETSpecificationConjunctionExpression,
)
ecdarText_ETSpecificationDisjunctionExpression_strategy = st.builds(
    ecdarText_ETSpecificationDisjunctionExpression,
)
ecdarText_ETSpecificationInstantiation_strategy = st.builds(
    ecdarText_ETSpecificationInstantiation,
)
ecdarText_ETEdge_strategy = st.builds(
    ecdarText_ETEdge,
    controllable=
        st.booleans()
)
ecdarText_ETLocation_strategy = st.builds(
    ecdarText_ETLocation,
    urgent=
        st.booleans(),
    universal=
        st.booleans(),
    name=
        safe_text
)
ecdarText_ETParameter_strategy = st.builds(
    ecdarText_ETParameter,
    name=
        safe_text,
    ioType=
        safe_text
)
ETSpecificationDefinition_strategy = st.builds(
    ETSpecificationDefinition,
)
ecdarText_ETSpecificationTemplate_strategy = st.builds(
    ecdarText_ETSpecificationTemplate,
)
ecdarText_ETSpecificationBody_strategy = st.builds(
    ecdarText_ETSpecificationBody,
)
ETSpecification_strategy = st.builds(
    ETSpecification,
)
ecdarText_ETSpecificationDefinition_strategy = st.builds(
    ecdarText_ETSpecificationDefinition,
)
ecdarText_ETSpecificationBinding_strategy = st.builds(
    ecdarText_ETSpecificationBinding,
)
ecdarText_ETSpecificationExpression_strategy = st.builds(
    ecdarText_ETSpecificationExpression,
)
ecdarText_ETIO_strategy = st.builds(
    ecdarText_ETIO,
    type=
        safe_text
)
ecdarText_ETSelect_strategy = st.builds(
    ecdarText_ETSelect,
    name=
        safe_text
)
ecdarText_ETFieldDeclaration_strategy = st.builds(
    ecdarText_ETFieldDeclaration,
)
ETActionType_strategy = st.builds(
    ETActionType,
)
ecdarText_ETOutputType_strategy = st.builds(
    ecdarText_ETOutputType,
)
ecdarText_ETInputType_strategy = st.builds(
    ecdarText_ETInputType,
)
ETTypeIdentifier_strategy = st.builds(
    ETTypeIdentifier,
)
ecdarText_ETClockType_strategy = st.builds(
    ecdarText_ETClockType,
)
ecdarText_ETTypeReference_strategy = st.builds(
    ecdarText_ETTypeReference,
)
ecdarText_ETStructType_strategy = st.builds(
    ecdarText_ETStructType,
)
ecdarText_ETActionType_strategy = st.builds(
    ecdarText_ETActionType,
)
ecdarText_ETScalarType_strategy = st.builds(
    ecdarText_ETScalarType,
)
ecdarText_ETBooleanType_strategy = st.builds(
    ecdarText_ETBooleanType,
)
ecdarText_ETIntegerType_strategy = st.builds(
    ecdarText_ETIntegerType,
)
ecdarText_ETTypeID_strategy = st.builds(
    ecdarText_ETTypeID,
    name=
        safe_text
)
ETInitialiser_strategy = st.builds(
    ETInitialiser,
)
ecdarText_ETMultiInitialiser_strategy = st.builds(
    ecdarText_ETMultiInitialiser,
)
ecdarText_ETSingleInitialiser_strategy = st.builds(
    ecdarText_ETSingleInitialiser,
)
ecdarText_ETFieldID_strategy = st.builds(
    ecdarText_ETFieldID,
    ioType=
        safe_text,
    name=
        safe_text
)
ecdarText_ETVariableID_strategy = st.builds(
    ecdarText_ETVariableID,
    ioType=
        safe_text,
    name=
        safe_text
)
ETDeclaration_strategy = st.builds(
    ETDeclaration,
)
ecdarText_ETTypeDeclaration_strategy = st.builds(
    ecdarText_ETTypeDeclaration,
)
ecdarText_ETVariableDeclaration_strategy = st.builds(
    ecdarText_ETVariableDeclaration,
)
ecdarText_ETTypeIdentifier_strategy = st.builds(
    ecdarText_ETTypeIdentifier,
)
ecdarText_ETTypeModifiers_strategy = st.builds(
    ecdarText_ETTypeModifiers,
    urgent=
        st.booleans(),
    meta=
        st.booleans(),
    const=
        st.booleans()
)
ecdarText_ETType_strategy = st.builds(
    ecdarText_ETType,
)
ecdarText_ETDeclaration_strategy = st.builds(
    ecdarText_ETDeclaration,
)
ecdarText_ETExpression_strategy = st.builds(
    ecdarText_ETExpression,
)
ecdarText_ETArrayDeclaration_strategy = st.builds(
    ecdarText_ETArrayDeclaration,
)
ecdarText_ETSpecification_strategy = st.builds(
    ecdarText_ETSpecification,
    name=
        safe_text
)
ecdarText_ETDeclarations_strategy = st.builds(
    ecdarText_ETDeclarations,
)
ecdarText_ETImport_strategy = st.builds(
    ecdarText_ETImport,
    importedNamespace=
        safe_text
)
ecdarText_ETFile_strategy = st.builds(
    ecdarText_ETFile,
)
ecdarText_ETInitialiser_strategy = st.builds(
    ecdarText_ETInitialiser,
)

@given(instance=ecdarText_EObject_strategy)
@settings(max_examples=50)
def test_ecdartext_eobject_instantiation(instance):
    assert isinstance(instance, ecdarText_EObject)

@given(instance=ETExpression_strategy)
@settings(max_examples=50)
def test_etexpression_instantiation(instance):
    assert isinstance(instance, ETExpression)

@given(instance=ecdarText_ETArrayExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etarrayexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETArrayExpression)

@given(instance=ecdarText_ETDivideExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etdivideexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETDivideExpression)

@given(instance=ecdarText_ETImplyExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etimplyexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETImplyExpression)

@given(instance=ecdarText_ETPreIncrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etpreincrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETPreIncrementExpression)

@given(instance=ecdarText_ETSubtractExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etsubtractexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSubtractExpression)

@given(instance=ecdarText_ETMultiplicationAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etmultiplicationassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMultiplicationAssignmentExpression)

@given(instance=ecdarText_ETMinExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etminexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMinExpression)

@given(instance=ecdarText_ETPostDecrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etpostdecrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETPostDecrementExpression)

@given(instance=ecdarText_ETLogicNotExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etlogicnotexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLogicNotExpression)

@given(instance=ecdarText_ETLogicOrExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etlogicorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLogicOrExpression)

@given(instance=ecdarText_ETDivisionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etdivisionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETDivisionAssignmentExpression)

@given(instance=ecdarText_ETLessEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etlessequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLessEqualExpression)

@given(instance=ecdarText_ETBooleanLiteral_strategy)
@settings(max_examples=50)
def test_ecdartext_etbooleanliteral_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBooleanLiteral)



@given(instance=ecdarText_ETBooleanLiteral_strategy)
def test_ecdartext_etbooleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecdarText_ETPostIncrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etpostincrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETPostIncrementExpression)

@given(instance=ecdarText_ETBitXORAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitxorassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitXORAssignmentExpression)

@given(instance=ecdarText_ETExistsExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etexistsexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETExistsExpression)



@given(instance=ecdarText_ETExistsExpression_strategy)
def test_ecdartext_etexistsexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETMultiplyExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etmultiplyexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMultiplyExpression)

@given(instance=ecdarText_ETMaxExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etmaxexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMaxExpression)

@given(instance=ecdarText_ETBitLeftAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitleftassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitLeftAssignmentExpression)

@given(instance=ecdarText_ETBitAndAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitandassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitAndAssignmentExpression)

@given(instance=ecdarText_ETNumberLiteral_strategy)
@settings(max_examples=50)
def test_ecdartext_etnumberliteral_instantiation(instance):
    assert isinstance(instance, ecdarText_ETNumberLiteral)



@given(instance=ecdarText_ETNumberLiteral_strategy)
def test_ecdartext_etnumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecdarText_ETModuloAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etmoduloassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETModuloAssignmentExpression)

@given(instance=ecdarText_ETAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETAssignmentExpression)

@given(instance=ecdarText_ETReference_strategy)
@settings(max_examples=50)
def test_ecdartext_etreference_instantiation(instance):
    assert isinstance(instance, ecdarText_ETReference)

@given(instance=ecdarText_ETLessExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etlessexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLessExpression)

@given(instance=ecdarText_ETMinusExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etminusexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMinusExpression)

@given(instance=ecdarText_ETBitAndExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitandexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitAndExpression)

@given(instance=ecdarText_ETGreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etgreaterequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETGreaterEqualExpression)

@given(instance=ecdarText_ETStructExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etstructexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETStructExpression)



@given(instance=ecdarText_ETStructExpression_strategy)
def test_ecdartext_etstructexpression_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=ecdarText_ETGreaterExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etgreaterexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETGreaterExpression)

@given(instance=ecdarText_ETSubtractionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etsubtractionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSubtractionAssignmentExpression)

@given(instance=ecdarText_ETUnequalExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etunequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETUnequalExpression)

@given(instance=ecdarText_ETBitRightExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitrightexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitRightExpression)

@given(instance=ecdarText_ETBitLeftExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitleftexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitLeftExpression)

@given(instance=ecdarText_ETBitXORExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitxorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitXORExpression)

@given(instance=ecdarText_ETConditionalExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etconditionalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETConditionalExpression)

@given(instance=ecdarText_ETBitOrAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitorassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitOrAssignmentExpression)

@given(instance=ecdarText_ETLogicAndExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etlogicandexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLogicAndExpression)

@given(instance=ecdarText_ETPreDecrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etpredecrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETPreDecrementExpression)

@given(instance=ecdarText_ETModuloExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etmoduloexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETModuloExpression)

@given(instance=ecdarText_ETAddExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etaddexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETAddExpression)

@given(instance=ecdarText_ETBitRightAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitrightassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitRightAssignmentExpression)

@given(instance=ecdarText_ETEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETEqualExpression)

@given(instance=ecdarText_ETBitOrExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etbitorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBitOrExpression)

@given(instance=ecdarText_ETForallExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etforallexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETForallExpression)



@given(instance=ecdarText_ETForallExpression_strategy)
def test_ecdartext_etforallexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETAdditionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etadditionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETAdditionAssignmentExpression)

@given(instance=ETSpecificationExpression_strategy)
@settings(max_examples=50)
def test_etspecificationexpression_instantiation(instance):
    assert isinstance(instance, ETSpecificationExpression)

@given(instance=ecdarText_ETSpecificationCompositionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationcompositionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationCompositionExpression)

@given(instance=ecdarText_ETSpecificationReference_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationreference_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationReference)

@given(instance=ecdarText_ETSpecificationConjunctionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationconjunctionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationConjunctionExpression)

@given(instance=ecdarText_ETSpecificationDisjunctionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationdisjunctionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationDisjunctionExpression)

@given(instance=ecdarText_ETSpecificationInstantiation_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationinstantiation_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationInstantiation)

@given(instance=ecdarText_ETEdge_strategy)
@settings(max_examples=50)
def test_ecdartext_etedge_instantiation(instance):
    assert isinstance(instance, ecdarText_ETEdge)



@given(instance=ecdarText_ETEdge_strategy)
def test_ecdartext_etedge_controllable_setter(instance):
    original = instance.controllable
    instance.controllable = original
    assert instance.controllable == original

@given(instance=ecdarText_ETLocation_strategy)
@settings(max_examples=50)
def test_ecdartext_etlocation_instantiation(instance):
    assert isinstance(instance, ecdarText_ETLocation)



@given(instance=ecdarText_ETLocation_strategy)
def test_ecdartext_etlocation_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=ecdarText_ETLocation_strategy)
def test_ecdartext_etlocation_universal_setter(instance):
    original = instance.universal
    instance.universal = original
    assert instance.universal == original



@given(instance=ecdarText_ETLocation_strategy)
def test_ecdartext_etlocation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETParameter_strategy)
@settings(max_examples=50)
def test_ecdartext_etparameter_instantiation(instance):
    assert isinstance(instance, ecdarText_ETParameter)



@given(instance=ecdarText_ETParameter_strategy)
def test_ecdartext_etparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=ecdarText_ETParameter_strategy)
def test_ecdartext_etparameter_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original

@given(instance=ETSpecificationDefinition_strategy)
@settings(max_examples=50)
def test_etspecificationdefinition_instantiation(instance):
    assert isinstance(instance, ETSpecificationDefinition)

@given(instance=ecdarText_ETSpecificationTemplate_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationtemplate_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationTemplate)

@given(instance=ecdarText_ETSpecificationBody_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationbody_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationBody)

@given(instance=ETSpecification_strategy)
@settings(max_examples=50)
def test_etspecification_instantiation(instance):
    assert isinstance(instance, ETSpecification)

@given(instance=ecdarText_ETSpecificationDefinition_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationdefinition_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationDefinition)

@given(instance=ecdarText_ETSpecificationBinding_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationbinding_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationBinding)

@given(instance=ecdarText_ETSpecificationExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecificationexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecificationExpression)

@given(instance=ecdarText_ETIO_strategy)
@settings(max_examples=50)
def test_ecdartext_etio_instantiation(instance):
    assert isinstance(instance, ecdarText_ETIO)



@given(instance=ecdarText_ETIO_strategy)
def test_ecdartext_etio_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ecdarText_ETSelect_strategy)
@settings(max_examples=50)
def test_ecdartext_etselect_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSelect)



@given(instance=ecdarText_ETSelect_strategy)
def test_ecdartext_etselect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETFieldDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext_etfielddeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText_ETFieldDeclaration)

@given(instance=ETActionType_strategy)
@settings(max_examples=50)
def test_etactiontype_instantiation(instance):
    assert isinstance(instance, ETActionType)

@given(instance=ecdarText_ETOutputType_strategy)
@settings(max_examples=50)
def test_ecdartext_etoutputtype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETOutputType)

@given(instance=ecdarText_ETInputType_strategy)
@settings(max_examples=50)
def test_ecdartext_etinputtype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETInputType)

@given(instance=ETTypeIdentifier_strategy)
@settings(max_examples=50)
def test_ettypeidentifier_instantiation(instance):
    assert isinstance(instance, ETTypeIdentifier)

@given(instance=ecdarText_ETClockType_strategy)
@settings(max_examples=50)
def test_ecdartext_etclocktype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETClockType)

@given(instance=ecdarText_ETTypeReference_strategy)
@settings(max_examples=50)
def test_ecdartext_ettypereference_instantiation(instance):
    assert isinstance(instance, ecdarText_ETTypeReference)

@given(instance=ecdarText_ETStructType_strategy)
@settings(max_examples=50)
def test_ecdartext_etstructtype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETStructType)

@given(instance=ecdarText_ETActionType_strategy)
@settings(max_examples=50)
def test_ecdartext_etactiontype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETActionType)

@given(instance=ecdarText_ETScalarType_strategy)
@settings(max_examples=50)
def test_ecdartext_etscalartype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETScalarType)

@given(instance=ecdarText_ETBooleanType_strategy)
@settings(max_examples=50)
def test_ecdartext_etbooleantype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETBooleanType)

@given(instance=ecdarText_ETIntegerType_strategy)
@settings(max_examples=50)
def test_ecdartext_etintegertype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETIntegerType)

@given(instance=ecdarText_ETTypeID_strategy)
@settings(max_examples=50)
def test_ecdartext_ettypeid_instantiation(instance):
    assert isinstance(instance, ecdarText_ETTypeID)



@given(instance=ecdarText_ETTypeID_strategy)
def test_ecdartext_ettypeid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ETInitialiser_strategy)
@settings(max_examples=50)
def test_etinitialiser_instantiation(instance):
    assert isinstance(instance, ETInitialiser)

@given(instance=ecdarText_ETMultiInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext_etmultiinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText_ETMultiInitialiser)

@given(instance=ecdarText_ETSingleInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext_etsingleinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSingleInitialiser)

@given(instance=ecdarText_ETFieldID_strategy)
@settings(max_examples=50)
def test_ecdartext_etfieldid_instantiation(instance):
    assert isinstance(instance, ecdarText_ETFieldID)



@given(instance=ecdarText_ETFieldID_strategy)
def test_ecdartext_etfieldid_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original



@given(instance=ecdarText_ETFieldID_strategy)
def test_ecdartext_etfieldid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETVariableID_strategy)
@settings(max_examples=50)
def test_ecdartext_etvariableid_instantiation(instance):
    assert isinstance(instance, ecdarText_ETVariableID)



@given(instance=ecdarText_ETVariableID_strategy)
def test_ecdartext_etvariableid_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original



@given(instance=ecdarText_ETVariableID_strategy)
def test_ecdartext_etvariableid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ETDeclaration_strategy)
@settings(max_examples=50)
def test_etdeclaration_instantiation(instance):
    assert isinstance(instance, ETDeclaration)

@given(instance=ecdarText_ETTypeDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext_ettypedeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText_ETTypeDeclaration)

@given(instance=ecdarText_ETVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext_etvariabledeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText_ETVariableDeclaration)

@given(instance=ecdarText_ETTypeIdentifier_strategy)
@settings(max_examples=50)
def test_ecdartext_ettypeidentifier_instantiation(instance):
    assert isinstance(instance, ecdarText_ETTypeIdentifier)

@given(instance=ecdarText_ETTypeModifiers_strategy)
@settings(max_examples=50)
def test_ecdartext_ettypemodifiers_instantiation(instance):
    assert isinstance(instance, ecdarText_ETTypeModifiers)



@given(instance=ecdarText_ETTypeModifiers_strategy)
def test_ecdartext_ettypemodifiers_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original



@given(instance=ecdarText_ETTypeModifiers_strategy)
def test_ecdartext_ettypemodifiers_meta_setter(instance):
    original = instance.meta
    instance.meta = original
    assert instance.meta == original



@given(instance=ecdarText_ETTypeModifiers_strategy)
def test_ecdartext_ettypemodifiers_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=ecdarText_ETType_strategy)
@settings(max_examples=50)
def test_ecdartext_ettype_instantiation(instance):
    assert isinstance(instance, ecdarText_ETType)

@given(instance=ecdarText_ETDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext_etdeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText_ETDeclaration)

@given(instance=ecdarText_ETExpression_strategy)
@settings(max_examples=50)
def test_ecdartext_etexpression_instantiation(instance):
    assert isinstance(instance, ecdarText_ETExpression)

@given(instance=ecdarText_ETArrayDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext_etarraydeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText_ETArrayDeclaration)

@given(instance=ecdarText_ETSpecification_strategy)
@settings(max_examples=50)
def test_ecdartext_etspecification_instantiation(instance):
    assert isinstance(instance, ecdarText_ETSpecification)



@given(instance=ecdarText_ETSpecification_strategy)
def test_ecdartext_etspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText_ETDeclarations_strategy)
@settings(max_examples=50)
def test_ecdartext_etdeclarations_instantiation(instance):
    assert isinstance(instance, ecdarText_ETDeclarations)

@given(instance=ecdarText_ETImport_strategy)
@settings(max_examples=50)
def test_ecdartext_etimport_instantiation(instance):
    assert isinstance(instance, ecdarText_ETImport)



@given(instance=ecdarText_ETImport_strategy)
def test_ecdartext_etimport_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ecdarText_ETFile_strategy)
@settings(max_examples=50)
def test_ecdartext_etfile_instantiation(instance):
    assert isinstance(instance, ecdarText_ETFile)

@given(instance=ecdarText_ETInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext_etinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText_ETInitialiser)
