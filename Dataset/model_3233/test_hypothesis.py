import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecdarText::EObject,
    ETExpression,
    ecdarText::ETBitAndExpression,
    ecdarText::ETAdditionAssignmentExpression,
    ecdarText::ETConditionalExpression,
    ecdarText::ETAssignmentExpression,
    ecdarText::ETModuloAssignmentExpression,
    ecdarText::ETGreaterEqualExpression,
    ecdarText::ETAddExpression,
    ecdarText::ETPreDecrementExpression,
    ecdarText::ETBitRightExpression,
    ecdarText::ETBitOrAssignmentExpression,
    ecdarText::ETLogicAndExpression,
    ecdarText::ETBooleanLiteral,
    ecdarText::ETExistsExpression,
    ecdarText::ETBitXORExpression,
    ecdarText::ETBitOrExpression,
    ecdarText::ETLogicNotExpression,
    ecdarText::ETMultiplicationAssignmentExpression,
    ecdarText::ETNumberLiteral,
    ecdarText::ETMinExpression,
    ecdarText::ETSubtractExpression,
    ecdarText::ETImplyExpression,
    ecdarText::ETPreIncrementExpression,
    ecdarText::ETPostDecrementExpression,
    ecdarText::ETMultiplyExpression,
    ecdarText::ETMinusExpression,
    ecdarText::ETBitLeftAssignmentExpression,
    ecdarText::ETModuloExpression,
    ecdarText::ETBitLeftExpression,
    ecdarText::ETMaxExpression,
    ecdarText::ETStructExpression,
    ecdarText::ETBitXORAssignmentExpression,
    ecdarText::ETLogicOrExpression,
    ecdarText::ETLessEqualExpression,
    ecdarText::ETArrayExpression,
    ecdarText::ETEqualExpression,
    ecdarText::ETDivideExpression,
    ecdarText::ETLessExpression,
    ecdarText::ETBitRightAssignmentExpression,
    ecdarText::ETBitAndAssignmentExpression,
    ecdarText::ETGreaterExpression,
    ecdarText::ETReference,
    ecdarText::ETUnequalExpression,
    ecdarText::ETPostIncrementExpression,
    ecdarText::ETDivisionAssignmentExpression,
    ecdarText::ETForallExpression,
    ecdarText::ETSubtractionAssignmentExpression,
    ETSpecificationExpression,
    ecdarText::ETSpecificationInstantiation,
    ecdarText::ETSpecificationReference,
    ecdarText::ETSpecificationConjunctionExpression,
    ecdarText::ETSpecificationDisjunctionExpression,
    ecdarText::ETIO,
    ecdarText::ETSelect,
    ecdarText::ETEdge,
    ecdarText::ETSpecificationCompositionExpression,
    ecdarText::ETLocation,
    ecdarText::ETParameter,
    ETSpecificationDefinition,
    ecdarText::ETSpecificationTemplate,
    ecdarText::ETSpecificationBody,
    ETSpecification,
    ecdarText::ETSpecificationDefinition,
    ecdarText::ETSpecificationBinding,
    ecdarText::ETSpecificationExpression,
    ecdarText::ETFieldID,
    ecdarText::ETFieldDeclaration,
    ETActionType,
    ecdarText::ETOutputType,
    ecdarText::ETInputType,
    ETTypeIdentifier,
    ecdarText::ETActionType,
    ecdarText::ETBooleanType,
    ecdarText::ETStructType,
    ecdarText::ETScalarType,
    ecdarText::ETTypeReference,
    ecdarText::ETClockType,
    ecdarText::ETIntegerType,
    ETInitialiser,
    ecdarText::ETMultiInitialiser,
    ecdarText::ETSingleInitialiser,
    ecdarText::ETInitialiser,
    ecdarText::ETVariableID,
    ETDeclaration,
    ecdarText::ETVariableDeclaration,
    ecdarText::ETTypeIdentifier,
    ecdarText::ETTypeModifiers,
    ecdarText::ETType,
    ecdarText::ETDeclaration,
    ecdarText::ETExpression,
    ecdarText::ETArrayDeclaration,
    ecdarText::ETTypeID,
    ecdarText::ETTypeDeclaration,
    ecdarText::ETImport,
    ecdarText::ETFile,
    ecdarText::ETSpecification,
    ecdarText::ETDeclarations,
    ETIOType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecdartext::eobject_is_not_abstract():
    assert not inspect.isabstract(ecdarText::EObject)


def test_ecdartext::eobject_constructor_exists():
    assert callable(ecdarText::EObject.__init__)


def test_ecdartext::eobject_constructor_args():
    sig = inspect.signature(ecdarText::EObject.__init__)
    params = list(sig.parameters.keys())



def test_etexpression_is_not_abstract():
    assert not inspect.isabstract(ETExpression)


def test_etexpression_constructor_exists():
    assert callable(ETExpression.__init__)


def test_etexpression_constructor_args():
    sig = inspect.signature(ETExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitandexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitAndExpression)


def test_ecdartext::etbitandexpression_constructor_exists():
    assert callable(ecdarText::ETBitAndExpression.__init__)


def test_ecdartext::etbitandexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etadditionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETAdditionAssignmentExpression)


def test_ecdartext::etadditionassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETAdditionAssignmentExpression.__init__)


def test_ecdartext::etadditionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETAdditionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etconditionalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETConditionalExpression)


def test_ecdartext::etconditionalexpression_constructor_exists():
    assert callable(ecdarText::ETConditionalExpression.__init__)


def test_ecdartext::etconditionalexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETConditionalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETAssignmentExpression)


def test_ecdartext::etassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETAssignmentExpression.__init__)


def test_ecdartext::etassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmoduloassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETModuloAssignmentExpression)


def test_ecdartext::etmoduloassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETModuloAssignmentExpression.__init__)


def test_ecdartext::etmoduloassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETModuloAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etgreaterequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETGreaterEqualExpression)


def test_ecdartext::etgreaterequalexpression_constructor_exists():
    assert callable(ecdarText::ETGreaterEqualExpression.__init__)


def test_ecdartext::etgreaterequalexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETGreaterEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etaddexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETAddExpression)


def test_ecdartext::etaddexpression_constructor_exists():
    assert callable(ecdarText::ETAddExpression.__init__)


def test_ecdartext::etaddexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETAddExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etpredecrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETPreDecrementExpression)


def test_ecdartext::etpredecrementexpression_constructor_exists():
    assert callable(ecdarText::ETPreDecrementExpression.__init__)


def test_ecdartext::etpredecrementexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETPreDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitrightexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitRightExpression)


def test_ecdartext::etbitrightexpression_constructor_exists():
    assert callable(ecdarText::ETBitRightExpression.__init__)


def test_ecdartext::etbitrightexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitRightExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitorassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitOrAssignmentExpression)


def test_ecdartext::etbitorassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETBitOrAssignmentExpression.__init__)


def test_ecdartext::etbitorassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitOrAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlogicandexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLogicAndExpression)


def test_ecdartext::etlogicandexpression_constructor_exists():
    assert callable(ecdarText::ETLogicAndExpression.__init__)


def test_ecdartext::etlogicandexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETLogicAndExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbooleanliteral_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBooleanLiteral)


def test_ecdartext::etbooleanliteral_constructor_exists():
    assert callable(ecdarText::ETBooleanLiteral.__init__)


def test_ecdartext::etbooleanliteral_constructor_args():
    sig = inspect.signature(ecdarText::ETBooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ecdartext::etbooleanliteral_has_value():
    assert hasattr(ecdarText::ETBooleanLiteral, "value")
    descriptor = None
    for klass in ecdarText::ETBooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etexistsexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETExistsExpression)


def test_ecdartext::etexistsexpression_constructor_exists():
    assert callable(ecdarText::ETExistsExpression.__init__)


def test_ecdartext::etexistsexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETExistsExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::etexistsexpression_has_name():
    assert hasattr(ecdarText::ETExistsExpression, "name")
    descriptor = None
    for klass in ecdarText::ETExistsExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etbitxorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitXORExpression)


def test_ecdartext::etbitxorexpression_constructor_exists():
    assert callable(ecdarText::ETBitXORExpression.__init__)


def test_ecdartext::etbitxorexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitXORExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitOrExpression)


def test_ecdartext::etbitorexpression_constructor_exists():
    assert callable(ecdarText::ETBitOrExpression.__init__)


def test_ecdartext::etbitorexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlogicnotexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLogicNotExpression)


def test_ecdartext::etlogicnotexpression_constructor_exists():
    assert callable(ecdarText::ETLogicNotExpression.__init__)


def test_ecdartext::etlogicnotexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETLogicNotExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmultiplicationassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMultiplicationAssignmentExpression)


def test_ecdartext::etmultiplicationassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETMultiplicationAssignmentExpression.__init__)


def test_ecdartext::etmultiplicationassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETMultiplicationAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etnumberliteral_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETNumberLiteral)


def test_ecdartext::etnumberliteral_constructor_exists():
    assert callable(ecdarText::ETNumberLiteral.__init__)


def test_ecdartext::etnumberliteral_constructor_args():
    sig = inspect.signature(ecdarText::ETNumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_ecdartext::etnumberliteral_has_value():
    assert hasattr(ecdarText::ETNumberLiteral, "value")
    descriptor = None
    for klass in ecdarText::ETNumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etminexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMinExpression)


def test_ecdartext::etminexpression_constructor_exists():
    assert callable(ecdarText::ETMinExpression.__init__)


def test_ecdartext::etminexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETMinExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etsubtractexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSubtractExpression)


def test_ecdartext::etsubtractexpression_constructor_exists():
    assert callable(ecdarText::ETSubtractExpression.__init__)


def test_ecdartext::etsubtractexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSubtractExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etimplyexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETImplyExpression)


def test_ecdartext::etimplyexpression_constructor_exists():
    assert callable(ecdarText::ETImplyExpression.__init__)


def test_ecdartext::etimplyexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETImplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etpreincrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETPreIncrementExpression)


def test_ecdartext::etpreincrementexpression_constructor_exists():
    assert callable(ecdarText::ETPreIncrementExpression.__init__)


def test_ecdartext::etpreincrementexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETPreIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etpostdecrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETPostDecrementExpression)


def test_ecdartext::etpostdecrementexpression_constructor_exists():
    assert callable(ecdarText::ETPostDecrementExpression.__init__)


def test_ecdartext::etpostdecrementexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETPostDecrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmultiplyexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMultiplyExpression)


def test_ecdartext::etmultiplyexpression_constructor_exists():
    assert callable(ecdarText::ETMultiplyExpression.__init__)


def test_ecdartext::etmultiplyexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETMultiplyExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etminusexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMinusExpression)


def test_ecdartext::etminusexpression_constructor_exists():
    assert callable(ecdarText::ETMinusExpression.__init__)


def test_ecdartext::etminusexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETMinusExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitleftassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitLeftAssignmentExpression)


def test_ecdartext::etbitleftassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETBitLeftAssignmentExpression.__init__)


def test_ecdartext::etbitleftassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitLeftAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmoduloexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETModuloExpression)


def test_ecdartext::etmoduloexpression_constructor_exists():
    assert callable(ecdarText::ETModuloExpression.__init__)


def test_ecdartext::etmoduloexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETModuloExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitleftexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitLeftExpression)


def test_ecdartext::etbitleftexpression_constructor_exists():
    assert callable(ecdarText::ETBitLeftExpression.__init__)


def test_ecdartext::etbitleftexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitLeftExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmaxexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMaxExpression)


def test_ecdartext::etmaxexpression_constructor_exists():
    assert callable(ecdarText::ETMaxExpression.__init__)


def test_ecdartext::etmaxexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETMaxExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etstructexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETStructExpression)


def test_ecdartext::etstructexpression_constructor_exists():
    assert callable(ecdarText::ETStructExpression.__init__)


def test_ecdartext::etstructexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETStructExpression.__init__)
    params = list(sig.parameters.keys())
    assert "right" in params, "Missing parameter 'right'"

def test_ecdartext::etstructexpression_has_right():
    assert hasattr(ecdarText::ETStructExpression, "right")
    descriptor = None
    for klass in ecdarText::ETStructExpression.__mro__:
        if "right" in klass.__dict__:
            descriptor = klass.__dict__["right"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etbitxorassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitXORAssignmentExpression)


def test_ecdartext::etbitxorassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETBitXORAssignmentExpression.__init__)


def test_ecdartext::etbitxorassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitXORAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlogicorexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLogicOrExpression)


def test_ecdartext::etlogicorexpression_constructor_exists():
    assert callable(ecdarText::ETLogicOrExpression.__init__)


def test_ecdartext::etlogicorexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETLogicOrExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlessequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLessEqualExpression)


def test_ecdartext::etlessequalexpression_constructor_exists():
    assert callable(ecdarText::ETLessEqualExpression.__init__)


def test_ecdartext::etlessequalexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETLessEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etarrayexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETArrayExpression)


def test_ecdartext::etarrayexpression_constructor_exists():
    assert callable(ecdarText::ETArrayExpression.__init__)


def test_ecdartext::etarrayexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETEqualExpression)


def test_ecdartext::etequalexpression_constructor_exists():
    assert callable(ecdarText::ETEqualExpression.__init__)


def test_ecdartext::etequalexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETEqualExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etdivideexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETDivideExpression)


def test_ecdartext::etdivideexpression_constructor_exists():
    assert callable(ecdarText::ETDivideExpression.__init__)


def test_ecdartext::etdivideexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETDivideExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlessexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLessExpression)


def test_ecdartext::etlessexpression_constructor_exists():
    assert callable(ecdarText::ETLessExpression.__init__)


def test_ecdartext::etlessexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETLessExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitrightassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitRightAssignmentExpression)


def test_ecdartext::etbitrightassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETBitRightAssignmentExpression.__init__)


def test_ecdartext::etbitrightassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitRightAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbitandassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBitAndAssignmentExpression)


def test_ecdartext::etbitandassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETBitAndAssignmentExpression.__init__)


def test_ecdartext::etbitandassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETBitAndAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etgreaterexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETGreaterExpression)


def test_ecdartext::etgreaterexpression_constructor_exists():
    assert callable(ecdarText::ETGreaterExpression.__init__)


def test_ecdartext::etgreaterexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETGreaterExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etreference_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETReference)


def test_ecdartext::etreference_constructor_exists():
    assert callable(ecdarText::ETReference.__init__)


def test_ecdartext::etreference_constructor_args():
    sig = inspect.signature(ecdarText::ETReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etunequalexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETUnequalExpression)


def test_ecdartext::etunequalexpression_constructor_exists():
    assert callable(ecdarText::ETUnequalExpression.__init__)


def test_ecdartext::etunequalexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETUnequalExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etpostincrementexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETPostIncrementExpression)


def test_ecdartext::etpostincrementexpression_constructor_exists():
    assert callable(ecdarText::ETPostIncrementExpression.__init__)


def test_ecdartext::etpostincrementexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETPostIncrementExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etdivisionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETDivisionAssignmentExpression)


def test_ecdartext::etdivisionassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETDivisionAssignmentExpression.__init__)


def test_ecdartext::etdivisionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETDivisionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etforallexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETForallExpression)


def test_ecdartext::etforallexpression_constructor_exists():
    assert callable(ecdarText::ETForallExpression.__init__)


def test_ecdartext::etforallexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETForallExpression.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::etforallexpression_has_name():
    assert hasattr(ecdarText::ETForallExpression, "name")
    descriptor = None
    for klass in ecdarText::ETForallExpression.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etsubtractionassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSubtractionAssignmentExpression)


def test_ecdartext::etsubtractionassignmentexpression_constructor_exists():
    assert callable(ecdarText::ETSubtractionAssignmentExpression.__init__)


def test_ecdartext::etsubtractionassignmentexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSubtractionAssignmentExpression.__init__)
    params = list(sig.parameters.keys())



def test_etspecificationexpression_is_not_abstract():
    assert not inspect.isabstract(ETSpecificationExpression)


def test_etspecificationexpression_constructor_exists():
    assert callable(ETSpecificationExpression.__init__)


def test_etspecificationexpression_constructor_args():
    sig = inspect.signature(ETSpecificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationinstantiation_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationInstantiation)


def test_ecdartext::etspecificationinstantiation_constructor_exists():
    assert callable(ecdarText::ETSpecificationInstantiation.__init__)


def test_ecdartext::etspecificationinstantiation_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationInstantiation.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationreference_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationReference)


def test_ecdartext::etspecificationreference_constructor_exists():
    assert callable(ecdarText::ETSpecificationReference.__init__)


def test_ecdartext::etspecificationreference_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationconjunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationConjunctionExpression)


def test_ecdartext::etspecificationconjunctionexpression_constructor_exists():
    assert callable(ecdarText::ETSpecificationConjunctionExpression.__init__)


def test_ecdartext::etspecificationconjunctionexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationConjunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationdisjunctionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationDisjunctionExpression)


def test_ecdartext::etspecificationdisjunctionexpression_constructor_exists():
    assert callable(ecdarText::ETSpecificationDisjunctionExpression.__init__)


def test_ecdartext::etspecificationdisjunctionexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationDisjunctionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etio_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETIO)


def test_ecdartext::etio_constructor_exists():
    assert callable(ecdarText::ETIO.__init__)


def test_ecdartext::etio_constructor_args():
    sig = inspect.signature(ecdarText::ETIO.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_ecdartext::etio_has_type():
    assert hasattr(ecdarText::ETIO, "type")
    descriptor = None
    for klass in ecdarText::ETIO.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etselect_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSelect)


def test_ecdartext::etselect_constructor_exists():
    assert callable(ecdarText::ETSelect.__init__)


def test_ecdartext::etselect_constructor_args():
    sig = inspect.signature(ecdarText::ETSelect.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::etselect_has_name():
    assert hasattr(ecdarText::ETSelect, "name")
    descriptor = None
    for klass in ecdarText::ETSelect.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etedge_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETEdge)


def test_ecdartext::etedge_constructor_exists():
    assert callable(ecdarText::ETEdge.__init__)


def test_ecdartext::etedge_constructor_args():
    sig = inspect.signature(ecdarText::ETEdge.__init__)
    params = list(sig.parameters.keys())
    assert "controllable" in params, "Missing parameter 'controllable'"

def test_ecdartext::etedge_has_controllable():
    assert hasattr(ecdarText::ETEdge, "controllable")
    descriptor = None
    for klass in ecdarText::ETEdge.__mro__:
        if "controllable" in klass.__dict__:
            descriptor = klass.__dict__["controllable"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etspecificationcompositionexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationCompositionExpression)


def test_ecdartext::etspecificationcompositionexpression_constructor_exists():
    assert callable(ecdarText::ETSpecificationCompositionExpression.__init__)


def test_ecdartext::etspecificationcompositionexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationCompositionExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etlocation_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETLocation)


def test_ecdartext::etlocation_constructor_exists():
    assert callable(ecdarText::ETLocation.__init__)


def test_ecdartext::etlocation_constructor_args():
    sig = inspect.signature(ecdarText::ETLocation.__init__)
    params = list(sig.parameters.keys())
    assert "universal" in params, "Missing parameter 'universal'"
    assert "urgent" in params, "Missing parameter 'urgent'"
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::etlocation_has_universal():
    assert hasattr(ecdarText::ETLocation, "universal")
    descriptor = None
    for klass in ecdarText::ETLocation.__mro__:
        if "universal" in klass.__dict__:
            descriptor = klass.__dict__["universal"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::etlocation_has_urgent():
    assert hasattr(ecdarText::ETLocation, "urgent")
    descriptor = None
    for klass in ecdarText::ETLocation.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::etlocation_has_name():
    assert hasattr(ecdarText::ETLocation, "name")
    descriptor = None
    for klass in ecdarText::ETLocation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etparameter_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETParameter)


def test_ecdartext::etparameter_constructor_exists():
    assert callable(ecdarText::ETParameter.__init__)


def test_ecdartext::etparameter_constructor_args():
    sig = inspect.signature(ecdarText::ETParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ioType" in params, "Missing parameter 'ioType'"

def test_ecdartext::etparameter_has_name():
    assert hasattr(ecdarText::ETParameter, "name")
    descriptor = None
    for klass in ecdarText::ETParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::etparameter_has_ioType():
    assert hasattr(ecdarText::ETParameter, "ioType")
    descriptor = None
    for klass in ecdarText::ETParameter.__mro__:
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



def test_ecdartext::etspecificationtemplate_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationTemplate)


def test_ecdartext::etspecificationtemplate_constructor_exists():
    assert callable(ecdarText::ETSpecificationTemplate.__init__)


def test_ecdartext::etspecificationtemplate_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationTemplate.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationbody_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationBody)


def test_ecdartext::etspecificationbody_constructor_exists():
    assert callable(ecdarText::ETSpecificationBody.__init__)


def test_ecdartext::etspecificationbody_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationBody.__init__)
    params = list(sig.parameters.keys())



def test_etspecification_is_not_abstract():
    assert not inspect.isabstract(ETSpecification)


def test_etspecification_constructor_exists():
    assert callable(ETSpecification.__init__)


def test_etspecification_constructor_args():
    sig = inspect.signature(ETSpecification.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationdefinition_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationDefinition)


def test_ecdartext::etspecificationdefinition_constructor_exists():
    assert callable(ecdarText::ETSpecificationDefinition.__init__)


def test_ecdartext::etspecificationdefinition_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationDefinition.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationbinding_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationBinding)


def test_ecdartext::etspecificationbinding_constructor_exists():
    assert callable(ecdarText::ETSpecificationBinding.__init__)


def test_ecdartext::etspecificationbinding_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationBinding.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecificationexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecificationExpression)


def test_ecdartext::etspecificationexpression_constructor_exists():
    assert callable(ecdarText::ETSpecificationExpression.__init__)


def test_ecdartext::etspecificationexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecificationExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etfieldid_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETFieldID)


def test_ecdartext::etfieldid_constructor_exists():
    assert callable(ecdarText::ETFieldID.__init__)


def test_ecdartext::etfieldid_constructor_args():
    sig = inspect.signature(ecdarText::ETFieldID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ioType" in params, "Missing parameter 'ioType'"

def test_ecdartext::etfieldid_has_name():
    assert hasattr(ecdarText::ETFieldID, "name")
    descriptor = None
    for klass in ecdarText::ETFieldID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::etfieldid_has_ioType():
    assert hasattr(ecdarText::ETFieldID, "ioType")
    descriptor = None
    for klass in ecdarText::ETFieldID.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etfielddeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETFieldDeclaration)


def test_ecdartext::etfielddeclaration_constructor_exists():
    assert callable(ecdarText::ETFieldDeclaration.__init__)


def test_ecdartext::etfielddeclaration_constructor_args():
    sig = inspect.signature(ecdarText::ETFieldDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_etactiontype_is_not_abstract():
    assert not inspect.isabstract(ETActionType)


def test_etactiontype_constructor_exists():
    assert callable(ETActionType.__init__)


def test_etactiontype_constructor_args():
    sig = inspect.signature(ETActionType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etoutputtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETOutputType)


def test_ecdartext::etoutputtype_constructor_exists():
    assert callable(ecdarText::ETOutputType.__init__)


def test_ecdartext::etoutputtype_constructor_args():
    sig = inspect.signature(ecdarText::ETOutputType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etinputtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETInputType)


def test_ecdartext::etinputtype_constructor_exists():
    assert callable(ecdarText::ETInputType.__init__)


def test_ecdartext::etinputtype_constructor_args():
    sig = inspect.signature(ecdarText::ETInputType.__init__)
    params = list(sig.parameters.keys())



def test_ettypeidentifier_is_not_abstract():
    assert not inspect.isabstract(ETTypeIdentifier)


def test_ettypeidentifier_constructor_exists():
    assert callable(ETTypeIdentifier.__init__)


def test_ettypeidentifier_constructor_args():
    sig = inspect.signature(ETTypeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etactiontype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETActionType)


def test_ecdartext::etactiontype_constructor_exists():
    assert callable(ecdarText::ETActionType.__init__)


def test_ecdartext::etactiontype_constructor_args():
    sig = inspect.signature(ecdarText::ETActionType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etbooleantype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETBooleanType)


def test_ecdartext::etbooleantype_constructor_exists():
    assert callable(ecdarText::ETBooleanType.__init__)


def test_ecdartext::etbooleantype_constructor_args():
    sig = inspect.signature(ecdarText::ETBooleanType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etstructtype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETStructType)


def test_ecdartext::etstructtype_constructor_exists():
    assert callable(ecdarText::ETStructType.__init__)


def test_ecdartext::etstructtype_constructor_args():
    sig = inspect.signature(ecdarText::ETStructType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etscalartype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETScalarType)


def test_ecdartext::etscalartype_constructor_exists():
    assert callable(ecdarText::ETScalarType.__init__)


def test_ecdartext::etscalartype_constructor_args():
    sig = inspect.signature(ecdarText::ETScalarType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::ettypereference_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETTypeReference)


def test_ecdartext::ettypereference_constructor_exists():
    assert callable(ecdarText::ETTypeReference.__init__)


def test_ecdartext::ettypereference_constructor_args():
    sig = inspect.signature(ecdarText::ETTypeReference.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etclocktype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETClockType)


def test_ecdartext::etclocktype_constructor_exists():
    assert callable(ecdarText::ETClockType.__init__)


def test_ecdartext::etclocktype_constructor_args():
    sig = inspect.signature(ecdarText::ETClockType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etintegertype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETIntegerType)


def test_ecdartext::etintegertype_constructor_exists():
    assert callable(ecdarText::ETIntegerType.__init__)


def test_ecdartext::etintegertype_constructor_args():
    sig = inspect.signature(ecdarText::ETIntegerType.__init__)
    params = list(sig.parameters.keys())



def test_etinitialiser_is_not_abstract():
    assert not inspect.isabstract(ETInitialiser)


def test_etinitialiser_constructor_exists():
    assert callable(ETInitialiser.__init__)


def test_etinitialiser_constructor_args():
    sig = inspect.signature(ETInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etmultiinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETMultiInitialiser)


def test_ecdartext::etmultiinitialiser_constructor_exists():
    assert callable(ecdarText::ETMultiInitialiser.__init__)


def test_ecdartext::etmultiinitialiser_constructor_args():
    sig = inspect.signature(ecdarText::ETMultiInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etsingleinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSingleInitialiser)


def test_ecdartext::etsingleinitialiser_constructor_exists():
    assert callable(ecdarText::ETSingleInitialiser.__init__)


def test_ecdartext::etsingleinitialiser_constructor_args():
    sig = inspect.signature(ecdarText::ETSingleInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etinitialiser_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETInitialiser)


def test_ecdartext::etinitialiser_constructor_exists():
    assert callable(ecdarText::ETInitialiser.__init__)


def test_ecdartext::etinitialiser_constructor_args():
    sig = inspect.signature(ecdarText::ETInitialiser.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etvariableid_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETVariableID)


def test_ecdartext::etvariableid_constructor_exists():
    assert callable(ecdarText::ETVariableID.__init__)


def test_ecdartext::etvariableid_constructor_args():
    sig = inspect.signature(ecdarText::ETVariableID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ioType" in params, "Missing parameter 'ioType'"

def test_ecdartext::etvariableid_has_name():
    assert hasattr(ecdarText::ETVariableID, "name")
    descriptor = None
    for klass in ecdarText::ETVariableID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::etvariableid_has_ioType():
    assert hasattr(ecdarText::ETVariableID, "ioType")
    descriptor = None
    for klass in ecdarText::ETVariableID.__mro__:
        if "ioType" in klass.__dict__:
            descriptor = klass.__dict__["ioType"]
            break
    assert isinstance(descriptor, property)



def test_etdeclaration_is_not_abstract():
    assert not inspect.isabstract(ETDeclaration)


def test_etdeclaration_constructor_exists():
    assert callable(ETDeclaration.__init__)


def test_etdeclaration_constructor_args():
    sig = inspect.signature(ETDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etvariabledeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETVariableDeclaration)


def test_ecdartext::etvariabledeclaration_constructor_exists():
    assert callable(ecdarText::ETVariableDeclaration.__init__)


def test_ecdartext::etvariabledeclaration_constructor_args():
    sig = inspect.signature(ecdarText::ETVariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::ettypeidentifier_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETTypeIdentifier)


def test_ecdartext::ettypeidentifier_constructor_exists():
    assert callable(ecdarText::ETTypeIdentifier.__init__)


def test_ecdartext::ettypeidentifier_constructor_args():
    sig = inspect.signature(ecdarText::ETTypeIdentifier.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::ettypemodifiers_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETTypeModifiers)


def test_ecdartext::ettypemodifiers_constructor_exists():
    assert callable(ecdarText::ETTypeModifiers.__init__)


def test_ecdartext::ettypemodifiers_constructor_args():
    sig = inspect.signature(ecdarText::ETTypeModifiers.__init__)
    params = list(sig.parameters.keys())
    assert "const" in params, "Missing parameter 'const'"
    assert "meta" in params, "Missing parameter 'meta'"
    assert "urgent" in params, "Missing parameter 'urgent'"

def test_ecdartext::ettypemodifiers_has_const():
    assert hasattr(ecdarText::ETTypeModifiers, "const")
    descriptor = None
    for klass in ecdarText::ETTypeModifiers.__mro__:
        if "const" in klass.__dict__:
            descriptor = klass.__dict__["const"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::ettypemodifiers_has_meta():
    assert hasattr(ecdarText::ETTypeModifiers, "meta")
    descriptor = None
    for klass in ecdarText::ETTypeModifiers.__mro__:
        if "meta" in klass.__dict__:
            descriptor = klass.__dict__["meta"]
            break
    assert isinstance(descriptor, property)

def test_ecdartext::ettypemodifiers_has_urgent():
    assert hasattr(ecdarText::ETTypeModifiers, "urgent")
    descriptor = None
    for klass in ecdarText::ETTypeModifiers.__mro__:
        if "urgent" in klass.__dict__:
            descriptor = klass.__dict__["urgent"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::ettype_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETType)


def test_ecdartext::ettype_constructor_exists():
    assert callable(ecdarText::ETType.__init__)


def test_ecdartext::ettype_constructor_args():
    sig = inspect.signature(ecdarText::ETType.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etdeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETDeclaration)


def test_ecdartext::etdeclaration_constructor_exists():
    assert callable(ecdarText::ETDeclaration.__init__)


def test_ecdartext::etdeclaration_constructor_args():
    sig = inspect.signature(ecdarText::ETDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etexpression_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETExpression)


def test_ecdartext::etexpression_constructor_exists():
    assert callable(ecdarText::ETExpression.__init__)


def test_ecdartext::etexpression_constructor_args():
    sig = inspect.signature(ecdarText::ETExpression.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etarraydeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETArrayDeclaration)


def test_ecdartext::etarraydeclaration_constructor_exists():
    assert callable(ecdarText::ETArrayDeclaration.__init__)


def test_ecdartext::etarraydeclaration_constructor_args():
    sig = inspect.signature(ecdarText::ETArrayDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::ettypeid_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETTypeID)


def test_ecdartext::ettypeid_constructor_exists():
    assert callable(ecdarText::ETTypeID.__init__)


def test_ecdartext::ettypeid_constructor_args():
    sig = inspect.signature(ecdarText::ETTypeID.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::ettypeid_has_name():
    assert hasattr(ecdarText::ETTypeID, "name")
    descriptor = None
    for klass in ecdarText::ETTypeID.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::ettypedeclaration_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETTypeDeclaration)


def test_ecdartext::ettypedeclaration_constructor_exists():
    assert callable(ecdarText::ETTypeDeclaration.__init__)


def test_ecdartext::ettypedeclaration_constructor_args():
    sig = inspect.signature(ecdarText::ETTypeDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etimport_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETImport)


def test_ecdartext::etimport_constructor_exists():
    assert callable(ecdarText::ETImport.__init__)


def test_ecdartext::etimport_constructor_args():
    sig = inspect.signature(ecdarText::ETImport.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_ecdartext::etimport_has_importedNamespace():
    assert hasattr(ecdarText::ETImport, "importedNamespace")
    descriptor = None
    for klass in ecdarText::ETImport.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etfile_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETFile)


def test_ecdartext::etfile_constructor_exists():
    assert callable(ecdarText::ETFile.__init__)


def test_ecdartext::etfile_constructor_args():
    sig = inspect.signature(ecdarText::ETFile.__init__)
    params = list(sig.parameters.keys())



def test_ecdartext::etspecification_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETSpecification)


def test_ecdartext::etspecification_constructor_exists():
    assert callable(ecdarText::ETSpecification.__init__)


def test_ecdartext::etspecification_constructor_args():
    sig = inspect.signature(ecdarText::ETSpecification.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecdartext::etspecification_has_name():
    assert hasattr(ecdarText::ETSpecification, "name")
    descriptor = None
    for klass in ecdarText::ETSpecification.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_ecdartext::etdeclarations_is_not_abstract():
    assert not inspect.isabstract(ecdarText::ETDeclarations)


def test_ecdartext::etdeclarations_constructor_exists():
    assert callable(ecdarText::ETDeclarations.__init__)


def test_ecdartext::etdeclarations_constructor_args():
    sig = inspect.signature(ecdarText::ETDeclarations.__init__)
    params = list(sig.parameters.keys())

def test_etiotype_exists():
    # Check that the Enumeration exists
    assert ETIOType is not None

def test_etiotype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ETIOType]
    expected_literals = [
        "INPUT",
        "OUTPUT",
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
ecdarText::EObject_strategy = st.builds(
    ecdarText::EObject,
)
ETExpression_strategy = st.builds(
    ETExpression,
)
ecdarText::ETBitAndExpression_strategy = st.builds(
    ecdarText::ETBitAndExpression,
)
ecdarText::ETAdditionAssignmentExpression_strategy = st.builds(
    ecdarText::ETAdditionAssignmentExpression,
)
ecdarText::ETConditionalExpression_strategy = st.builds(
    ecdarText::ETConditionalExpression,
)
ecdarText::ETAssignmentExpression_strategy = st.builds(
    ecdarText::ETAssignmentExpression,
)
ecdarText::ETModuloAssignmentExpression_strategy = st.builds(
    ecdarText::ETModuloAssignmentExpression,
)
ecdarText::ETGreaterEqualExpression_strategy = st.builds(
    ecdarText::ETGreaterEqualExpression,
)
ecdarText::ETAddExpression_strategy = st.builds(
    ecdarText::ETAddExpression,
)
ecdarText::ETPreDecrementExpression_strategy = st.builds(
    ecdarText::ETPreDecrementExpression,
)
ecdarText::ETBitRightExpression_strategy = st.builds(
    ecdarText::ETBitRightExpression,
)
ecdarText::ETBitOrAssignmentExpression_strategy = st.builds(
    ecdarText::ETBitOrAssignmentExpression,
)
ecdarText::ETLogicAndExpression_strategy = st.builds(
    ecdarText::ETLogicAndExpression,
)
ecdarText::ETBooleanLiteral_strategy = st.builds(
    ecdarText::ETBooleanLiteral,
    value=
        safe_text
)
ecdarText::ETExistsExpression_strategy = st.builds(
    ecdarText::ETExistsExpression,
    name=
        safe_text
)
ecdarText::ETBitXORExpression_strategy = st.builds(
    ecdarText::ETBitXORExpression,
)
ecdarText::ETBitOrExpression_strategy = st.builds(
    ecdarText::ETBitOrExpression,
)
ecdarText::ETLogicNotExpression_strategy = st.builds(
    ecdarText::ETLogicNotExpression,
)
ecdarText::ETMultiplicationAssignmentExpression_strategy = st.builds(
    ecdarText::ETMultiplicationAssignmentExpression,
)
ecdarText::ETNumberLiteral_strategy = st.builds(
    ecdarText::ETNumberLiteral,
    value=
        st.integers()
)
ecdarText::ETMinExpression_strategy = st.builds(
    ecdarText::ETMinExpression,
)
ecdarText::ETSubtractExpression_strategy = st.builds(
    ecdarText::ETSubtractExpression,
)
ecdarText::ETImplyExpression_strategy = st.builds(
    ecdarText::ETImplyExpression,
)
ecdarText::ETPreIncrementExpression_strategy = st.builds(
    ecdarText::ETPreIncrementExpression,
)
ecdarText::ETPostDecrementExpression_strategy = st.builds(
    ecdarText::ETPostDecrementExpression,
)
ecdarText::ETMultiplyExpression_strategy = st.builds(
    ecdarText::ETMultiplyExpression,
)
ecdarText::ETMinusExpression_strategy = st.builds(
    ecdarText::ETMinusExpression,
)
ecdarText::ETBitLeftAssignmentExpression_strategy = st.builds(
    ecdarText::ETBitLeftAssignmentExpression,
)
ecdarText::ETModuloExpression_strategy = st.builds(
    ecdarText::ETModuloExpression,
)
ecdarText::ETBitLeftExpression_strategy = st.builds(
    ecdarText::ETBitLeftExpression,
)
ecdarText::ETMaxExpression_strategy = st.builds(
    ecdarText::ETMaxExpression,
)
ecdarText::ETStructExpression_strategy = st.builds(
    ecdarText::ETStructExpression,
    right=
        safe_text
)
ecdarText::ETBitXORAssignmentExpression_strategy = st.builds(
    ecdarText::ETBitXORAssignmentExpression,
)
ecdarText::ETLogicOrExpression_strategy = st.builds(
    ecdarText::ETLogicOrExpression,
)
ecdarText::ETLessEqualExpression_strategy = st.builds(
    ecdarText::ETLessEqualExpression,
)
ecdarText::ETArrayExpression_strategy = st.builds(
    ecdarText::ETArrayExpression,
)
ecdarText::ETEqualExpression_strategy = st.builds(
    ecdarText::ETEqualExpression,
)
ecdarText::ETDivideExpression_strategy = st.builds(
    ecdarText::ETDivideExpression,
)
ecdarText::ETLessExpression_strategy = st.builds(
    ecdarText::ETLessExpression,
)
ecdarText::ETBitRightAssignmentExpression_strategy = st.builds(
    ecdarText::ETBitRightAssignmentExpression,
)
ecdarText::ETBitAndAssignmentExpression_strategy = st.builds(
    ecdarText::ETBitAndAssignmentExpression,
)
ecdarText::ETGreaterExpression_strategy = st.builds(
    ecdarText::ETGreaterExpression,
)
ecdarText::ETReference_strategy = st.builds(
    ecdarText::ETReference,
)
ecdarText::ETUnequalExpression_strategy = st.builds(
    ecdarText::ETUnequalExpression,
)
ecdarText::ETPostIncrementExpression_strategy = st.builds(
    ecdarText::ETPostIncrementExpression,
)
ecdarText::ETDivisionAssignmentExpression_strategy = st.builds(
    ecdarText::ETDivisionAssignmentExpression,
)
ecdarText::ETForallExpression_strategy = st.builds(
    ecdarText::ETForallExpression,
    name=
        safe_text
)
ecdarText::ETSubtractionAssignmentExpression_strategy = st.builds(
    ecdarText::ETSubtractionAssignmentExpression,
)
ETSpecificationExpression_strategy = st.builds(
    ETSpecificationExpression,
)
ecdarText::ETSpecificationInstantiation_strategy = st.builds(
    ecdarText::ETSpecificationInstantiation,
)
ecdarText::ETSpecificationReference_strategy = st.builds(
    ecdarText::ETSpecificationReference,
)
ecdarText::ETSpecificationConjunctionExpression_strategy = st.builds(
    ecdarText::ETSpecificationConjunctionExpression,
)
ecdarText::ETSpecificationDisjunctionExpression_strategy = st.builds(
    ecdarText::ETSpecificationDisjunctionExpression,
)
ecdarText::ETIO_strategy = st.builds(
    ecdarText::ETIO,
    type=
        safe_text
)
ecdarText::ETSelect_strategy = st.builds(
    ecdarText::ETSelect,
    name=
        safe_text
)
ecdarText::ETEdge_strategy = st.builds(
    ecdarText::ETEdge,
    controllable=
        st.booleans()
)
ecdarText::ETSpecificationCompositionExpression_strategy = st.builds(
    ecdarText::ETSpecificationCompositionExpression,
)
ecdarText::ETLocation_strategy = st.builds(
    ecdarText::ETLocation,
    universal=
        st.booleans(),
    urgent=
        st.booleans(),
    name=
        safe_text
)
ecdarText::ETParameter_strategy = st.builds(
    ecdarText::ETParameter,
    name=
        safe_text,
    ioType=
        safe_text
)
ETSpecificationDefinition_strategy = st.builds(
    ETSpecificationDefinition,
)
ecdarText::ETSpecificationTemplate_strategy = st.builds(
    ecdarText::ETSpecificationTemplate,
)
ecdarText::ETSpecificationBody_strategy = st.builds(
    ecdarText::ETSpecificationBody,
)
ETSpecification_strategy = st.builds(
    ETSpecification,
)
ecdarText::ETSpecificationDefinition_strategy = st.builds(
    ecdarText::ETSpecificationDefinition,
)
ecdarText::ETSpecificationBinding_strategy = st.builds(
    ecdarText::ETSpecificationBinding,
)
ecdarText::ETSpecificationExpression_strategy = st.builds(
    ecdarText::ETSpecificationExpression,
)
ecdarText::ETFieldID_strategy = st.builds(
    ecdarText::ETFieldID,
    name=
        safe_text,
    ioType=
        safe_text
)
ecdarText::ETFieldDeclaration_strategy = st.builds(
    ecdarText::ETFieldDeclaration,
)
ETActionType_strategy = st.builds(
    ETActionType,
)
ecdarText::ETOutputType_strategy = st.builds(
    ecdarText::ETOutputType,
)
ecdarText::ETInputType_strategy = st.builds(
    ecdarText::ETInputType,
)
ETTypeIdentifier_strategy = st.builds(
    ETTypeIdentifier,
)
ecdarText::ETActionType_strategy = st.builds(
    ecdarText::ETActionType,
)
ecdarText::ETBooleanType_strategy = st.builds(
    ecdarText::ETBooleanType,
)
ecdarText::ETStructType_strategy = st.builds(
    ecdarText::ETStructType,
)
ecdarText::ETScalarType_strategy = st.builds(
    ecdarText::ETScalarType,
)
ecdarText::ETTypeReference_strategy = st.builds(
    ecdarText::ETTypeReference,
)
ecdarText::ETClockType_strategy = st.builds(
    ecdarText::ETClockType,
)
ecdarText::ETIntegerType_strategy = st.builds(
    ecdarText::ETIntegerType,
)
ETInitialiser_strategy = st.builds(
    ETInitialiser,
)
ecdarText::ETMultiInitialiser_strategy = st.builds(
    ecdarText::ETMultiInitialiser,
)
ecdarText::ETSingleInitialiser_strategy = st.builds(
    ecdarText::ETSingleInitialiser,
)
ecdarText::ETInitialiser_strategy = st.builds(
    ecdarText::ETInitialiser,
)
ecdarText::ETVariableID_strategy = st.builds(
    ecdarText::ETVariableID,
    name=
        safe_text,
    ioType=
        safe_text
)
ETDeclaration_strategy = st.builds(
    ETDeclaration,
)
ecdarText::ETVariableDeclaration_strategy = st.builds(
    ecdarText::ETVariableDeclaration,
)
ecdarText::ETTypeIdentifier_strategy = st.builds(
    ecdarText::ETTypeIdentifier,
)
ecdarText::ETTypeModifiers_strategy = st.builds(
    ecdarText::ETTypeModifiers,
    const=
        st.booleans(),
    meta=
        st.booleans(),
    urgent=
        st.booleans()
)
ecdarText::ETType_strategy = st.builds(
    ecdarText::ETType,
)
ecdarText::ETDeclaration_strategy = st.builds(
    ecdarText::ETDeclaration,
)
ecdarText::ETExpression_strategy = st.builds(
    ecdarText::ETExpression,
)
ecdarText::ETArrayDeclaration_strategy = st.builds(
    ecdarText::ETArrayDeclaration,
)
ecdarText::ETTypeID_strategy = st.builds(
    ecdarText::ETTypeID,
    name=
        safe_text
)
ecdarText::ETTypeDeclaration_strategy = st.builds(
    ecdarText::ETTypeDeclaration,
)
ecdarText::ETImport_strategy = st.builds(
    ecdarText::ETImport,
    importedNamespace=
        safe_text
)
ecdarText::ETFile_strategy = st.builds(
    ecdarText::ETFile,
)
ecdarText::ETSpecification_strategy = st.builds(
    ecdarText::ETSpecification,
    name=
        safe_text
)
ecdarText::ETDeclarations_strategy = st.builds(
    ecdarText::ETDeclarations,
)

@given(instance=ecdarText::EObject_strategy)
@settings(max_examples=50)
def test_ecdartext::eobject_instantiation(instance):
    assert isinstance(instance, ecdarText::EObject)

@given(instance=ETExpression_strategy)
@settings(max_examples=50)
def test_etexpression_instantiation(instance):
    assert isinstance(instance, ETExpression)

@given(instance=ecdarText::ETBitAndExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitandexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitAndExpression)

@given(instance=ecdarText::ETAdditionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etadditionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETAdditionAssignmentExpression)

@given(instance=ecdarText::ETConditionalExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etconditionalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETConditionalExpression)

@given(instance=ecdarText::ETAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETAssignmentExpression)

@given(instance=ecdarText::ETModuloAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etmoduloassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETModuloAssignmentExpression)

@given(instance=ecdarText::ETGreaterEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etgreaterequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETGreaterEqualExpression)

@given(instance=ecdarText::ETAddExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etaddexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETAddExpression)

@given(instance=ecdarText::ETPreDecrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etpredecrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETPreDecrementExpression)

@given(instance=ecdarText::ETBitRightExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitrightexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitRightExpression)

@given(instance=ecdarText::ETBitOrAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitorassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitOrAssignmentExpression)

@given(instance=ecdarText::ETLogicAndExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etlogicandexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLogicAndExpression)

@given(instance=ecdarText::ETBooleanLiteral_strategy)
@settings(max_examples=50)
def test_ecdartext::etbooleanliteral_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBooleanLiteral)

@given(instance=ecdarText::ETBooleanLiteral_strategy)
def test_ecdartext::etbooleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=ecdarText::ETBooleanLiteral_strategy)
def test_ecdartext::etbooleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecdarText::ETExistsExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etexistsexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETExistsExpression)

@given(instance=ecdarText::ETExistsExpression_strategy)
def test_ecdartext::etexistsexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETExistsExpression_strategy)
def test_ecdartext::etexistsexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETBitXORExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitxorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitXORExpression)

@given(instance=ecdarText::ETBitOrExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitOrExpression)

@given(instance=ecdarText::ETLogicNotExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etlogicnotexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLogicNotExpression)

@given(instance=ecdarText::ETMultiplicationAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etmultiplicationassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMultiplicationAssignmentExpression)

@given(instance=ecdarText::ETNumberLiteral_strategy)
@settings(max_examples=50)
def test_ecdartext::etnumberliteral_instantiation(instance):
    assert isinstance(instance, ecdarText::ETNumberLiteral)

@given(instance=ecdarText::ETNumberLiteral_strategy)
def test_ecdartext::etnumberliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ecdarText::ETNumberLiteral_strategy)
def test_ecdartext::etnumberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecdarText::ETMinExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etminexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMinExpression)

@given(instance=ecdarText::ETSubtractExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etsubtractexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSubtractExpression)

@given(instance=ecdarText::ETImplyExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etimplyexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETImplyExpression)

@given(instance=ecdarText::ETPreIncrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etpreincrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETPreIncrementExpression)

@given(instance=ecdarText::ETPostDecrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etpostdecrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETPostDecrementExpression)

@given(instance=ecdarText::ETMultiplyExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etmultiplyexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMultiplyExpression)

@given(instance=ecdarText::ETMinusExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etminusexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMinusExpression)

@given(instance=ecdarText::ETBitLeftAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitleftassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitLeftAssignmentExpression)

@given(instance=ecdarText::ETModuloExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etmoduloexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETModuloExpression)

@given(instance=ecdarText::ETBitLeftExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitleftexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitLeftExpression)

@given(instance=ecdarText::ETMaxExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etmaxexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMaxExpression)

@given(instance=ecdarText::ETStructExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etstructexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETStructExpression)

@given(instance=ecdarText::ETStructExpression_strategy)
def test_ecdartext::etstructexpression_right_type(instance):
    assert isinstance(instance.right, str)


@given(instance=ecdarText::ETStructExpression_strategy)
def test_ecdartext::etstructexpression_right_setter(instance):
    original = instance.right
    instance.right = original
    assert instance.right == original

@given(instance=ecdarText::ETBitXORAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitxorassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitXORAssignmentExpression)

@given(instance=ecdarText::ETLogicOrExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etlogicorexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLogicOrExpression)

@given(instance=ecdarText::ETLessEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etlessequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLessEqualExpression)

@given(instance=ecdarText::ETArrayExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etarrayexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETArrayExpression)

@given(instance=ecdarText::ETEqualExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETEqualExpression)

@given(instance=ecdarText::ETDivideExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etdivideexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETDivideExpression)

@given(instance=ecdarText::ETLessExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etlessexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLessExpression)

@given(instance=ecdarText::ETBitRightAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitrightassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitRightAssignmentExpression)

@given(instance=ecdarText::ETBitAndAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etbitandassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBitAndAssignmentExpression)

@given(instance=ecdarText::ETGreaterExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etgreaterexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETGreaterExpression)

@given(instance=ecdarText::ETReference_strategy)
@settings(max_examples=50)
def test_ecdartext::etreference_instantiation(instance):
    assert isinstance(instance, ecdarText::ETReference)

@given(instance=ecdarText::ETUnequalExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etunequalexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETUnequalExpression)

@given(instance=ecdarText::ETPostIncrementExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etpostincrementexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETPostIncrementExpression)

@given(instance=ecdarText::ETDivisionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etdivisionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETDivisionAssignmentExpression)

@given(instance=ecdarText::ETForallExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etforallexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETForallExpression)

@given(instance=ecdarText::ETForallExpression_strategy)
def test_ecdartext::etforallexpression_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETForallExpression_strategy)
def test_ecdartext::etforallexpression_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETSubtractionAssignmentExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etsubtractionassignmentexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSubtractionAssignmentExpression)

@given(instance=ETSpecificationExpression_strategy)
@settings(max_examples=50)
def test_etspecificationexpression_instantiation(instance):
    assert isinstance(instance, ETSpecificationExpression)

@given(instance=ecdarText::ETSpecificationInstantiation_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationinstantiation_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationInstantiation)

@given(instance=ecdarText::ETSpecificationReference_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationreference_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationReference)

@given(instance=ecdarText::ETSpecificationConjunctionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationconjunctionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationConjunctionExpression)

@given(instance=ecdarText::ETSpecificationDisjunctionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationdisjunctionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationDisjunctionExpression)

@given(instance=ecdarText::ETIO_strategy)
@settings(max_examples=50)
def test_ecdartext::etio_instantiation(instance):
    assert isinstance(instance, ecdarText::ETIO)

@given(instance=ecdarText::ETIO_strategy)
def test_ecdartext::etio_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=ecdarText::ETIO_strategy)
def test_ecdartext::etio_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=ecdarText::ETSelect_strategy)
@settings(max_examples=50)
def test_ecdartext::etselect_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSelect)

@given(instance=ecdarText::ETSelect_strategy)
def test_ecdartext::etselect_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETSelect_strategy)
def test_ecdartext::etselect_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETEdge_strategy)
@settings(max_examples=50)
def test_ecdartext::etedge_instantiation(instance):
    assert isinstance(instance, ecdarText::ETEdge)

@given(instance=ecdarText::ETEdge_strategy)
def test_ecdartext::etedge_controllable_type(instance):
    assert isinstance(instance.controllable, bool)


@given(instance=ecdarText::ETEdge_strategy)
def test_ecdartext::etedge_controllable_setter(instance):
    original = instance.controllable
    instance.controllable = original
    assert instance.controllable == original

@given(instance=ecdarText::ETSpecificationCompositionExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationcompositionexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationCompositionExpression)

@given(instance=ecdarText::ETLocation_strategy)
@settings(max_examples=50)
def test_ecdartext::etlocation_instantiation(instance):
    assert isinstance(instance, ecdarText::ETLocation)

@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_universal_type(instance):
    assert isinstance(instance.universal, bool)


@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_universal_setter(instance):
    original = instance.universal
    instance.universal = original
    assert instance.universal == original

@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_urgent_type(instance):
    assert isinstance(instance.urgent, bool)


@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETLocation_strategy)
def test_ecdartext::etlocation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETParameter_strategy)
@settings(max_examples=50)
def test_ecdartext::etparameter_instantiation(instance):
    assert isinstance(instance, ecdarText::ETParameter)

@given(instance=ecdarText::ETParameter_strategy)
def test_ecdartext::etparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETParameter_strategy)
def test_ecdartext::etparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETParameter_strategy)
def test_ecdartext::etparameter_ioType_type(instance):
    assert isinstance(instance.ioType, str)


@given(instance=ecdarText::ETParameter_strategy)
def test_ecdartext::etparameter_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original

@given(instance=ETSpecificationDefinition_strategy)
@settings(max_examples=50)
def test_etspecificationdefinition_instantiation(instance):
    assert isinstance(instance, ETSpecificationDefinition)

@given(instance=ecdarText::ETSpecificationTemplate_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationtemplate_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationTemplate)

@given(instance=ecdarText::ETSpecificationBody_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationbody_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationBody)

@given(instance=ETSpecification_strategy)
@settings(max_examples=50)
def test_etspecification_instantiation(instance):
    assert isinstance(instance, ETSpecification)

@given(instance=ecdarText::ETSpecificationDefinition_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationdefinition_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationDefinition)

@given(instance=ecdarText::ETSpecificationBinding_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationbinding_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationBinding)

@given(instance=ecdarText::ETSpecificationExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecificationexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecificationExpression)

@given(instance=ecdarText::ETFieldID_strategy)
@settings(max_examples=50)
def test_ecdartext::etfieldid_instantiation(instance):
    assert isinstance(instance, ecdarText::ETFieldID)

@given(instance=ecdarText::ETFieldID_strategy)
def test_ecdartext::etfieldid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETFieldID_strategy)
def test_ecdartext::etfieldid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETFieldID_strategy)
def test_ecdartext::etfieldid_ioType_type(instance):
    assert isinstance(instance.ioType, str)


@given(instance=ecdarText::ETFieldID_strategy)
def test_ecdartext::etfieldid_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original

@given(instance=ecdarText::ETFieldDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext::etfielddeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText::ETFieldDeclaration)

@given(instance=ETActionType_strategy)
@settings(max_examples=50)
def test_etactiontype_instantiation(instance):
    assert isinstance(instance, ETActionType)

@given(instance=ecdarText::ETOutputType_strategy)
@settings(max_examples=50)
def test_ecdartext::etoutputtype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETOutputType)

@given(instance=ecdarText::ETInputType_strategy)
@settings(max_examples=50)
def test_ecdartext::etinputtype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETInputType)

@given(instance=ETTypeIdentifier_strategy)
@settings(max_examples=50)
def test_ettypeidentifier_instantiation(instance):
    assert isinstance(instance, ETTypeIdentifier)

@given(instance=ecdarText::ETActionType_strategy)
@settings(max_examples=50)
def test_ecdartext::etactiontype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETActionType)

@given(instance=ecdarText::ETBooleanType_strategy)
@settings(max_examples=50)
def test_ecdartext::etbooleantype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETBooleanType)

@given(instance=ecdarText::ETStructType_strategy)
@settings(max_examples=50)
def test_ecdartext::etstructtype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETStructType)

@given(instance=ecdarText::ETScalarType_strategy)
@settings(max_examples=50)
def test_ecdartext::etscalartype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETScalarType)

@given(instance=ecdarText::ETTypeReference_strategy)
@settings(max_examples=50)
def test_ecdartext::ettypereference_instantiation(instance):
    assert isinstance(instance, ecdarText::ETTypeReference)

@given(instance=ecdarText::ETClockType_strategy)
@settings(max_examples=50)
def test_ecdartext::etclocktype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETClockType)

@given(instance=ecdarText::ETIntegerType_strategy)
@settings(max_examples=50)
def test_ecdartext::etintegertype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETIntegerType)

@given(instance=ETInitialiser_strategy)
@settings(max_examples=50)
def test_etinitialiser_instantiation(instance):
    assert isinstance(instance, ETInitialiser)

@given(instance=ecdarText::ETMultiInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext::etmultiinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText::ETMultiInitialiser)

@given(instance=ecdarText::ETSingleInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext::etsingleinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSingleInitialiser)

@given(instance=ecdarText::ETInitialiser_strategy)
@settings(max_examples=50)
def test_ecdartext::etinitialiser_instantiation(instance):
    assert isinstance(instance, ecdarText::ETInitialiser)

@given(instance=ecdarText::ETVariableID_strategy)
@settings(max_examples=50)
def test_ecdartext::etvariableid_instantiation(instance):
    assert isinstance(instance, ecdarText::ETVariableID)

@given(instance=ecdarText::ETVariableID_strategy)
def test_ecdartext::etvariableid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETVariableID_strategy)
def test_ecdartext::etvariableid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETVariableID_strategy)
def test_ecdartext::etvariableid_ioType_type(instance):
    assert isinstance(instance.ioType, str)


@given(instance=ecdarText::ETVariableID_strategy)
def test_ecdartext::etvariableid_ioType_setter(instance):
    original = instance.ioType
    instance.ioType = original
    assert instance.ioType == original

@given(instance=ETDeclaration_strategy)
@settings(max_examples=50)
def test_etdeclaration_instantiation(instance):
    assert isinstance(instance, ETDeclaration)

@given(instance=ecdarText::ETVariableDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext::etvariabledeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText::ETVariableDeclaration)

@given(instance=ecdarText::ETTypeIdentifier_strategy)
@settings(max_examples=50)
def test_ecdartext::ettypeidentifier_instantiation(instance):
    assert isinstance(instance, ecdarText::ETTypeIdentifier)

@given(instance=ecdarText::ETTypeModifiers_strategy)
@settings(max_examples=50)
def test_ecdartext::ettypemodifiers_instantiation(instance):
    assert isinstance(instance, ecdarText::ETTypeModifiers)

@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_const_type(instance):
    assert isinstance(instance.const, bool)


@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_const_setter(instance):
    original = instance.const
    instance.const = original
    assert instance.const == original

@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_meta_type(instance):
    assert isinstance(instance.meta, bool)


@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_meta_setter(instance):
    original = instance.meta
    instance.meta = original
    assert instance.meta == original

@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_urgent_type(instance):
    assert isinstance(instance.urgent, bool)


@given(instance=ecdarText::ETTypeModifiers_strategy)
def test_ecdartext::ettypemodifiers_urgent_setter(instance):
    original = instance.urgent
    instance.urgent = original
    assert instance.urgent == original

@given(instance=ecdarText::ETType_strategy)
@settings(max_examples=50)
def test_ecdartext::ettype_instantiation(instance):
    assert isinstance(instance, ecdarText::ETType)

@given(instance=ecdarText::ETDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext::etdeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText::ETDeclaration)

@given(instance=ecdarText::ETExpression_strategy)
@settings(max_examples=50)
def test_ecdartext::etexpression_instantiation(instance):
    assert isinstance(instance, ecdarText::ETExpression)

@given(instance=ecdarText::ETArrayDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext::etarraydeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText::ETArrayDeclaration)

@given(instance=ecdarText::ETTypeID_strategy)
@settings(max_examples=50)
def test_ecdartext::ettypeid_instantiation(instance):
    assert isinstance(instance, ecdarText::ETTypeID)

@given(instance=ecdarText::ETTypeID_strategy)
def test_ecdartext::ettypeid_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETTypeID_strategy)
def test_ecdartext::ettypeid_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETTypeDeclaration_strategy)
@settings(max_examples=50)
def test_ecdartext::ettypedeclaration_instantiation(instance):
    assert isinstance(instance, ecdarText::ETTypeDeclaration)

@given(instance=ecdarText::ETImport_strategy)
@settings(max_examples=50)
def test_ecdartext::etimport_instantiation(instance):
    assert isinstance(instance, ecdarText::ETImport)

@given(instance=ecdarText::ETImport_strategy)
def test_ecdartext::etimport_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=ecdarText::ETImport_strategy)
def test_ecdartext::etimport_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=ecdarText::ETFile_strategy)
@settings(max_examples=50)
def test_ecdartext::etfile_instantiation(instance):
    assert isinstance(instance, ecdarText::ETFile)

@given(instance=ecdarText::ETSpecification_strategy)
@settings(max_examples=50)
def test_ecdartext::etspecification_instantiation(instance):
    assert isinstance(instance, ecdarText::ETSpecification)

@given(instance=ecdarText::ETSpecification_strategy)
def test_ecdartext::etspecification_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecdarText::ETSpecification_strategy)
def test_ecdartext::etspecification_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecdarText::ETDeclarations_strategy)
@settings(max_examples=50)
def test_ecdartext::etdeclarations_instantiation(instance):
    assert isinstance(instance, ecdarText::ETDeclarations)
