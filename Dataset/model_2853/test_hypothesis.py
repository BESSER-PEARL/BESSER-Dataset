import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    cal::AstConnection,
    cal::AstExpression,
    cal::AstAssignParameter,
    cal::AstTypeName,
    cal::AstAnnotation,
    cal::EObject,
    cal::AstVariable,
    cal::Import,
    cal::AstEntity,
    cal::AstPort,
    cal::AstAbstractActor,
    AstUnit,
    AstPackage,
    cal::AstUnit,
    AstTop,
    cal::AstNamespace,
    cal::AstPackage,
    cal::AstTop,
    AstAction,
    cal::AstInitialize,
    cal::AstAnnotationArgument,
    cal::AstTypeParameterList,
    AstExpressionLiteral,
    cal::AstExpressionInteger,
    cal::AstExpressionString,
    cal::AstExpressionFloat,
    cal::AstExpressionBoolean,
    cal::AstTypeParam,
    cal::AstGenerator,
    AstExpression,
    cal::AstExpressionUnary,
    cal::AstExpressionBinary,
    cal::AstExpressionIf,
    cal::AstExpressionList,
    cal::AstExpressionCall,
    cal::AstExpressionLiteral,
    cal::AstExpressionVariable,
    cal::AstForeachGenerator,
    cal::AstOutputPattern,
    cal::AstMemberAccess,
    cal::AstVariableReference,
    AstStatement,
    cal::AstStatementIf,
    cal::AstStatementForeach,
    cal::AstStatementBlock,
    cal::AstStatementWhile,
    cal::AstStatementCall,
    cal::AstStatementAssign,
    cal::AstInequality,
    cal::AstTag,
    cal::AstExternalProcedure,
    cal::AstStatement,
    AstExternalProcedure,
    cal::AstInputPattern,
    cal::AstTransition,
    cal::AstState,
    cal::AstProcedure,
    AstExternalFunction,
    cal::AstFunction,
    cal::AstExternalFunction,
    cal::AstPriority,
    cal::AstSchedule,
    cal::AstAction,
    cal::AstConnectionAttribute,
    cal::AstActorVariableReference,
    cal::AstTypeDefinitionParameter,
    cal::AstType,
    cal::AstStructure,
    cal::AstActorVariable,
    AstAbstractActor,
    cal::AstActor,
    cal::AstExternalActor,
    cal::AstNetwork,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cal::astconnection_is_not_abstract():
    assert not inspect.isabstract(cal::AstConnection)


def test_cal::astconnection_constructor_exists():
    assert callable(cal::AstConnection.__init__)


def test_cal::astconnection_constructor_args():
    sig = inspect.signature(cal::AstConnection.__init__)
    params = list(sig.parameters.keys())
    assert "outPort" in params, "Missing parameter 'outPort'"
    assert "inPort" in params, "Missing parameter 'inPort'"

def test_cal::astconnection_has_outPort():
    assert hasattr(cal::AstConnection, "outPort")
    descriptor = None
    for klass in cal::AstConnection.__mro__:
        if "outPort" in klass.__dict__:
            descriptor = klass.__dict__["outPort"]
            break
    assert isinstance(descriptor, property)

def test_cal::astconnection_has_inPort():
    assert hasattr(cal::AstConnection, "inPort")
    descriptor = None
    for klass in cal::AstConnection.__mro__:
        if "inPort" in klass.__dict__:
            descriptor = klass.__dict__["inPort"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpression_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpression)


def test_cal::astexpression_constructor_exists():
    assert callable(cal::AstExpression.__init__)


def test_cal::astexpression_constructor_args():
    sig = inspect.signature(cal::AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal::astassignparameter_is_not_abstract():
    assert not inspect.isabstract(cal::AstAssignParameter)


def test_cal::astassignparameter_constructor_exists():
    assert callable(cal::AstAssignParameter.__init__)


def test_cal::astassignparameter_constructor_args():
    sig = inspect.signature(cal::AstAssignParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astassignparameter_has_name():
    assert hasattr(cal::AstAssignParameter, "name")
    descriptor = None
    for klass in cal::AstAssignParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::asttypename_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeName)


def test_cal::asttypename_constructor_exists():
    assert callable(cal::AstTypeName.__init__)


def test_cal::asttypename_constructor_args():
    sig = inspect.signature(cal::AstTypeName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::asttypename_has_name():
    assert hasattr(cal::AstTypeName, "name")
    descriptor = None
    for klass in cal::AstTypeName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astannotation_is_not_abstract():
    assert not inspect.isabstract(cal::AstAnnotation)


def test_cal::astannotation_constructor_exists():
    assert callable(cal::AstAnnotation.__init__)


def test_cal::astannotation_constructor_args():
    sig = inspect.signature(cal::AstAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astannotation_has_name():
    assert hasattr(cal::AstAnnotation, "name")
    descriptor = None
    for klass in cal::AstAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::eobject_is_not_abstract():
    assert not inspect.isabstract(cal::EObject)


def test_cal::eobject_constructor_exists():
    assert callable(cal::EObject.__init__)


def test_cal::eobject_constructor_args():
    sig = inspect.signature(cal::EObject.__init__)
    params = list(sig.parameters.keys())



def test_cal::astvariable_is_not_abstract():
    assert not inspect.isabstract(cal::AstVariable)


def test_cal::astvariable_constructor_exists():
    assert callable(cal::AstVariable.__init__)


def test_cal::astvariable_constructor_args():
    sig = inspect.signature(cal::AstVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_cal::astvariable_has_name():
    assert hasattr(cal::AstVariable, "name")
    descriptor = None
    for klass in cal::AstVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal::astvariable_has_constant():
    assert hasattr(cal::AstVariable, "constant")
    descriptor = None
    for klass in cal::AstVariable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_cal::import_is_not_abstract():
    assert not inspect.isabstract(cal::Import)


def test_cal::import_constructor_exists():
    assert callable(cal::Import.__init__)


def test_cal::import_constructor_args():
    sig = inspect.signature(cal::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_cal::import_has_importedNamespace():
    assert hasattr(cal::Import, "importedNamespace")
    descriptor = None
    for klass in cal::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cal::astentity_is_not_abstract():
    assert not inspect.isabstract(cal::AstEntity)


def test_cal::astentity_constructor_exists():
    assert callable(cal::AstEntity.__init__)


def test_cal::astentity_constructor_args():
    sig = inspect.signature(cal::AstEntity.__init__)
    params = list(sig.parameters.keys())



def test_cal::astport_is_not_abstract():
    assert not inspect.isabstract(cal::AstPort)


def test_cal::astport_constructor_exists():
    assert callable(cal::AstPort.__init__)


def test_cal::astport_constructor_args():
    sig = inspect.signature(cal::AstPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astport_has_name():
    assert hasattr(cal::AstPort, "name")
    descriptor = None
    for klass in cal::AstPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astabstractactor_is_not_abstract():
    assert not inspect.isabstract(cal::AstAbstractActor)


def test_cal::astabstractactor_constructor_exists():
    assert callable(cal::AstAbstractActor.__init__)


def test_cal::astabstractactor_constructor_args():
    sig = inspect.signature(cal::AstAbstractActor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astabstractactor_has_name():
    assert hasattr(cal::AstAbstractActor, "name")
    descriptor = None
    for klass in cal::AstAbstractActor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_astunit_is_not_abstract():
    assert not inspect.isabstract(AstUnit)


def test_astunit_constructor_exists():
    assert callable(AstUnit.__init__)


def test_astunit_constructor_args():
    sig = inspect.signature(AstUnit.__init__)
    params = list(sig.parameters.keys())



def test_astpackage_is_not_abstract():
    assert not inspect.isabstract(AstPackage)


def test_astpackage_constructor_exists():
    assert callable(AstPackage.__init__)


def test_astpackage_constructor_args():
    sig = inspect.signature(AstPackage.__init__)
    params = list(sig.parameters.keys())



def test_cal::astunit_is_not_abstract():
    assert not inspect.isabstract(cal::AstUnit)


def test_cal::astunit_constructor_exists():
    assert callable(cal::AstUnit.__init__)


def test_cal::astunit_constructor_args():
    sig = inspect.signature(cal::AstUnit.__init__)
    params = list(sig.parameters.keys())



def test_asttop_is_not_abstract():
    assert not inspect.isabstract(AstTop)


def test_asttop_constructor_exists():
    assert callable(AstTop.__init__)


def test_asttop_constructor_args():
    sig = inspect.signature(AstTop.__init__)
    params = list(sig.parameters.keys())



def test_cal::astnamespace_is_not_abstract():
    assert not inspect.isabstract(cal::AstNamespace)


def test_cal::astnamespace_constructor_exists():
    assert callable(cal::AstNamespace.__init__)


def test_cal::astnamespace_constructor_args():
    sig = inspect.signature(cal::AstNamespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astnamespace_has_name():
    assert hasattr(cal::AstNamespace, "name")
    descriptor = None
    for klass in cal::AstNamespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astpackage_is_not_abstract():
    assert not inspect.isabstract(cal::AstPackage)


def test_cal::astpackage_constructor_exists():
    assert callable(cal::AstPackage.__init__)


def test_cal::astpackage_constructor_args():
    sig = inspect.signature(cal::AstPackage.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttop_is_not_abstract():
    assert not inspect.isabstract(cal::AstTop)


def test_cal::asttop_constructor_exists():
    assert callable(cal::AstTop.__init__)


def test_cal::asttop_constructor_args():
    sig = inspect.signature(cal::AstTop.__init__)
    params = list(sig.parameters.keys())



def test_astaction_is_not_abstract():
    assert not inspect.isabstract(AstAction)


def test_astaction_constructor_exists():
    assert callable(AstAction.__init__)


def test_astaction_constructor_args():
    sig = inspect.signature(AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal::astinitialize_is_not_abstract():
    assert not inspect.isabstract(cal::AstInitialize)


def test_cal::astinitialize_constructor_exists():
    assert callable(cal::AstInitialize.__init__)


def test_cal::astinitialize_constructor_args():
    sig = inspect.signature(cal::AstInitialize.__init__)
    params = list(sig.parameters.keys())



def test_cal::astannotationargument_is_not_abstract():
    assert not inspect.isabstract(cal::AstAnnotationArgument)


def test_cal::astannotationargument_constructor_exists():
    assert callable(cal::AstAnnotationArgument.__init__)


def test_cal::astannotationargument_constructor_args():
    sig = inspect.signature(cal::AstAnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_cal::astannotationargument_has_name():
    assert hasattr(cal::AstAnnotationArgument, "name")
    descriptor = None
    for klass in cal::AstAnnotationArgument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal::astannotationargument_has_value():
    assert hasattr(cal::AstAnnotationArgument, "value")
    descriptor = None
    for klass in cal::AstAnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::asttypeparameterlist_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeParameterList)


def test_cal::asttypeparameterlist_constructor_exists():
    assert callable(cal::AstTypeParameterList.__init__)


def test_cal::asttypeparameterlist_constructor_args():
    sig = inspect.signature(cal::AstTypeParameterList.__init__)
    params = list(sig.parameters.keys())



def test_astexpressionliteral_is_not_abstract():
    assert not inspect.isabstract(AstExpressionLiteral)


def test_astexpressionliteral_constructor_exists():
    assert callable(AstExpressionLiteral.__init__)


def test_astexpressionliteral_constructor_args():
    sig = inspect.signature(AstExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressioninteger_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionInteger)


def test_cal::astexpressioninteger_constructor_exists():
    assert callable(cal::AstExpressionInteger.__init__)


def test_cal::astexpressioninteger_constructor_args():
    sig = inspect.signature(cal::AstExpressionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::astexpressioninteger_has_value():
    assert hasattr(cal::AstExpressionInteger, "value")
    descriptor = None
    for klass in cal::AstExpressionInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpressionstring_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionString)


def test_cal::astexpressionstring_constructor_exists():
    assert callable(cal::AstExpressionString.__init__)


def test_cal::astexpressionstring_constructor_args():
    sig = inspect.signature(cal::AstExpressionString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::astexpressionstring_has_value():
    assert hasattr(cal::AstExpressionString, "value")
    descriptor = None
    for klass in cal::AstExpressionString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpressionfloat_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionFloat)


def test_cal::astexpressionfloat_constructor_exists():
    assert callable(cal::AstExpressionFloat.__init__)


def test_cal::astexpressionfloat_constructor_args():
    sig = inspect.signature(cal::AstExpressionFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::astexpressionfloat_has_value():
    assert hasattr(cal::AstExpressionFloat, "value")
    descriptor = None
    for klass in cal::AstExpressionFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpressionboolean_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionBoolean)


def test_cal::astexpressionboolean_constructor_exists():
    assert callable(cal::AstExpressionBoolean.__init__)


def test_cal::astexpressionboolean_constructor_args():
    sig = inspect.signature(cal::AstExpressionBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal::astexpressionboolean_has_value():
    assert hasattr(cal::AstExpressionBoolean, "value")
    descriptor = None
    for klass in cal::AstExpressionBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal::asttypeparam_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeParam)


def test_cal::asttypeparam_constructor_exists():
    assert callable(cal::AstTypeParam.__init__)


def test_cal::asttypeparam_constructor_args():
    sig = inspect.signature(cal::AstTypeParam.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::asttypeparam_has_name():
    assert hasattr(cal::AstTypeParam, "name")
    descriptor = None
    for klass in cal::AstTypeParam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astgenerator_is_not_abstract():
    assert not inspect.isabstract(cal::AstGenerator)


def test_cal::astgenerator_constructor_exists():
    assert callable(cal::AstGenerator.__init__)


def test_cal::astgenerator_constructor_args():
    sig = inspect.signature(cal::AstGenerator.__init__)
    params = list(sig.parameters.keys())



def test_astexpression_is_not_abstract():
    assert not inspect.isabstract(AstExpression)


def test_astexpression_constructor_exists():
    assert callable(AstExpression.__init__)


def test_astexpression_constructor_args():
    sig = inspect.signature(AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressionunary_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionUnary)


def test_cal::astexpressionunary_constructor_exists():
    assert callable(cal::AstExpressionUnary.__init__)


def test_cal::astexpressionunary_constructor_args():
    sig = inspect.signature(cal::AstExpressionUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal::astexpressionunary_has_unaryOperator():
    assert hasattr(cal::AstExpressionUnary, "unaryOperator")
    descriptor = None
    for klass in cal::AstExpressionUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpressionbinary_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionBinary)


def test_cal::astexpressionbinary_constructor_exists():
    assert callable(cal::AstExpressionBinary.__init__)


def test_cal::astexpressionbinary_constructor_args():
    sig = inspect.signature(cal::AstExpressionBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal::astexpressionbinary_has_operator():
    assert hasattr(cal::AstExpressionBinary, "operator")
    descriptor = None
    for klass in cal::AstExpressionBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexpressionif_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionIf)


def test_cal::astexpressionif_constructor_exists():
    assert callable(cal::AstExpressionIf.__init__)


def test_cal::astexpressionif_constructor_args():
    sig = inspect.signature(cal::AstExpressionIf.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressionlist_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionList)


def test_cal::astexpressionlist_constructor_exists():
    assert callable(cal::AstExpressionList.__init__)


def test_cal::astexpressionlist_constructor_args():
    sig = inspect.signature(cal::AstExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressioncall_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionCall)


def test_cal::astexpressioncall_constructor_exists():
    assert callable(cal::AstExpressionCall.__init__)


def test_cal::astexpressioncall_constructor_args():
    sig = inspect.signature(cal::AstExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressionliteral_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionLiteral)


def test_cal::astexpressionliteral_constructor_exists():
    assert callable(cal::AstExpressionLiteral.__init__)


def test_cal::astexpressionliteral_constructor_args():
    sig = inspect.signature(cal::AstExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexpressionvariable_is_not_abstract():
    assert not inspect.isabstract(cal::AstExpressionVariable)


def test_cal::astexpressionvariable_constructor_exists():
    assert callable(cal::AstExpressionVariable.__init__)


def test_cal::astexpressionvariable_constructor_args():
    sig = inspect.signature(cal::AstExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_cal::astforeachgenerator_is_not_abstract():
    assert not inspect.isabstract(cal::AstForeachGenerator)


def test_cal::astforeachgenerator_constructor_exists():
    assert callable(cal::AstForeachGenerator.__init__)


def test_cal::astforeachgenerator_constructor_args():
    sig = inspect.signature(cal::AstForeachGenerator.__init__)
    params = list(sig.parameters.keys())



def test_cal::astoutputpattern_is_not_abstract():
    assert not inspect.isabstract(cal::AstOutputPattern)


def test_cal::astoutputpattern_constructor_exists():
    assert callable(cal::AstOutputPattern.__init__)


def test_cal::astoutputpattern_constructor_args():
    sig = inspect.signature(cal::AstOutputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal::astmemberaccess_is_not_abstract():
    assert not inspect.isabstract(cal::AstMemberAccess)


def test_cal::astmemberaccess_constructor_exists():
    assert callable(cal::AstMemberAccess.__init__)


def test_cal::astmemberaccess_constructor_args():
    sig = inspect.signature(cal::AstMemberAccess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astmemberaccess_has_name():
    assert hasattr(cal::AstMemberAccess, "name")
    descriptor = None
    for klass in cal::AstMemberAccess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astvariablereference_is_not_abstract():
    assert not inspect.isabstract(cal::AstVariableReference)


def test_cal::astvariablereference_constructor_exists():
    assert callable(cal::AstVariableReference.__init__)


def test_cal::astvariablereference_constructor_args():
    sig = inspect.signature(cal::AstVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_aststatement_is_not_abstract():
    assert not inspect.isabstract(AstStatement)


def test_aststatement_constructor_exists():
    assert callable(AstStatement.__init__)


def test_aststatement_constructor_args():
    sig = inspect.signature(AstStatement.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementif_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementIf)


def test_cal::aststatementif_constructor_exists():
    assert callable(cal::AstStatementIf.__init__)


def test_cal::aststatementif_constructor_args():
    sig = inspect.signature(cal::AstStatementIf.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementforeach_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementForeach)


def test_cal::aststatementforeach_constructor_exists():
    assert callable(cal::AstStatementForeach.__init__)


def test_cal::aststatementforeach_constructor_args():
    sig = inspect.signature(cal::AstStatementForeach.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementblock_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementBlock)


def test_cal::aststatementblock_constructor_exists():
    assert callable(cal::AstStatementBlock.__init__)


def test_cal::aststatementblock_constructor_args():
    sig = inspect.signature(cal::AstStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementwhile_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementWhile)


def test_cal::aststatementwhile_constructor_exists():
    assert callable(cal::AstStatementWhile.__init__)


def test_cal::aststatementwhile_constructor_args():
    sig = inspect.signature(cal::AstStatementWhile.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementcall_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementCall)


def test_cal::aststatementcall_constructor_exists():
    assert callable(cal::AstStatementCall.__init__)


def test_cal::aststatementcall_constructor_args():
    sig = inspect.signature(cal::AstStatementCall.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatementassign_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatementAssign)


def test_cal::aststatementassign_constructor_exists():
    assert callable(cal::AstStatementAssign.__init__)


def test_cal::aststatementassign_constructor_args():
    sig = inspect.signature(cal::AstStatementAssign.__init__)
    params = list(sig.parameters.keys())



def test_cal::astinequality_is_not_abstract():
    assert not inspect.isabstract(cal::AstInequality)


def test_cal::astinequality_constructor_exists():
    assert callable(cal::AstInequality.__init__)


def test_cal::astinequality_constructor_args():
    sig = inspect.signature(cal::AstInequality.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttag_is_not_abstract():
    assert not inspect.isabstract(cal::AstTag)


def test_cal::asttag_constructor_exists():
    assert callable(cal::AstTag.__init__)


def test_cal::asttag_constructor_args():
    sig = inspect.signature(cal::AstTag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_cal::asttag_has_identifiers():
    assert hasattr(cal::AstTag, "identifiers")
    descriptor = None
    for klass in cal::AstTag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexternalprocedure_is_not_abstract():
    assert not inspect.isabstract(cal::AstExternalProcedure)


def test_cal::astexternalprocedure_constructor_exists():
    assert callable(cal::AstExternalProcedure.__init__)


def test_cal::astexternalprocedure_constructor_args():
    sig = inspect.signature(cal::AstExternalProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststatement_is_not_abstract():
    assert not inspect.isabstract(cal::AstStatement)


def test_cal::aststatement_constructor_exists():
    assert callable(cal::AstStatement.__init__)


def test_cal::aststatement_constructor_args():
    sig = inspect.signature(cal::AstStatement.__init__)
    params = list(sig.parameters.keys())



def test_astexternalprocedure_is_not_abstract():
    assert not inspect.isabstract(AstExternalProcedure)


def test_astexternalprocedure_constructor_exists():
    assert callable(AstExternalProcedure.__init__)


def test_astexternalprocedure_constructor_args():
    sig = inspect.signature(AstExternalProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cal::astinputpattern_is_not_abstract():
    assert not inspect.isabstract(cal::AstInputPattern)


def test_cal::astinputpattern_constructor_exists():
    assert callable(cal::AstInputPattern.__init__)


def test_cal::astinputpattern_constructor_args():
    sig = inspect.signature(cal::AstInputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttransition_is_not_abstract():
    assert not inspect.isabstract(cal::AstTransition)


def test_cal::asttransition_constructor_exists():
    assert callable(cal::AstTransition.__init__)


def test_cal::asttransition_constructor_args():
    sig = inspect.signature(cal::AstTransition.__init__)
    params = list(sig.parameters.keys())



def test_cal::aststate_is_not_abstract():
    assert not inspect.isabstract(cal::AstState)


def test_cal::aststate_constructor_exists():
    assert callable(cal::AstState.__init__)


def test_cal::aststate_constructor_args():
    sig = inspect.signature(cal::AstState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::aststate_has_name():
    assert hasattr(cal::AstState, "name")
    descriptor = None
    for klass in cal::AstState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astprocedure_is_not_abstract():
    assert not inspect.isabstract(cal::AstProcedure)


def test_cal::astprocedure_constructor_exists():
    assert callable(cal::AstProcedure.__init__)


def test_cal::astprocedure_constructor_args():
    sig = inspect.signature(cal::AstProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astprocedure_has_name():
    assert hasattr(cal::AstProcedure, "name")
    descriptor = None
    for klass in cal::AstProcedure.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_astexternalfunction_is_not_abstract():
    assert not inspect.isabstract(AstExternalFunction)


def test_astexternalfunction_constructor_exists():
    assert callable(AstExternalFunction.__init__)


def test_astexternalfunction_constructor_args():
    sig = inspect.signature(AstExternalFunction.__init__)
    params = list(sig.parameters.keys())



def test_cal::astfunction_is_not_abstract():
    assert not inspect.isabstract(cal::AstFunction)


def test_cal::astfunction_constructor_exists():
    assert callable(cal::AstFunction.__init__)


def test_cal::astfunction_constructor_args():
    sig = inspect.signature(cal::AstFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astfunction_has_name():
    assert hasattr(cal::AstFunction, "name")
    descriptor = None
    for klass in cal::AstFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astexternalfunction_is_not_abstract():
    assert not inspect.isabstract(cal::AstExternalFunction)


def test_cal::astexternalfunction_constructor_exists():
    assert callable(cal::AstExternalFunction.__init__)


def test_cal::astexternalfunction_constructor_args():
    sig = inspect.signature(cal::AstExternalFunction.__init__)
    params = list(sig.parameters.keys())



def test_cal::astpriority_is_not_abstract():
    assert not inspect.isabstract(cal::AstPriority)


def test_cal::astpriority_constructor_exists():
    assert callable(cal::AstPriority.__init__)


def test_cal::astpriority_constructor_args():
    sig = inspect.signature(cal::AstPriority.__init__)
    params = list(sig.parameters.keys())



def test_cal::astschedule_is_not_abstract():
    assert not inspect.isabstract(cal::AstSchedule)


def test_cal::astschedule_constructor_exists():
    assert callable(cal::AstSchedule.__init__)


def test_cal::astschedule_constructor_args():
    sig = inspect.signature(cal::AstSchedule.__init__)
    params = list(sig.parameters.keys())



def test_cal::astaction_is_not_abstract():
    assert not inspect.isabstract(cal::AstAction)


def test_cal::astaction_constructor_exists():
    assert callable(cal::AstAction.__init__)


def test_cal::astaction_constructor_args():
    sig = inspect.signature(cal::AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal::astconnectionattribute_is_not_abstract():
    assert not inspect.isabstract(cal::AstConnectionAttribute)


def test_cal::astconnectionattribute_constructor_exists():
    assert callable(cal::AstConnectionAttribute.__init__)


def test_cal::astconnectionattribute_constructor_args():
    sig = inspect.signature(cal::AstConnectionAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astconnectionattribute_has_name():
    assert hasattr(cal::AstConnectionAttribute, "name")
    descriptor = None
    for klass in cal::AstConnectionAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal::astactorvariablereference_is_not_abstract():
    assert not inspect.isabstract(cal::AstActorVariableReference)


def test_cal::astactorvariablereference_constructor_exists():
    assert callable(cal::AstActorVariableReference.__init__)


def test_cal::astactorvariablereference_constructor_args():
    sig = inspect.signature(cal::AstActorVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttypedefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(cal::AstTypeDefinitionParameter)


def test_cal::asttypedefinitionparameter_constructor_exists():
    assert callable(cal::AstTypeDefinitionParameter.__init__)


def test_cal::asttypedefinitionparameter_constructor_args():
    sig = inspect.signature(cal::AstTypeDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_cal::asttype_is_not_abstract():
    assert not inspect.isabstract(cal::AstType)


def test_cal::asttype_constructor_exists():
    assert callable(cal::AstType.__init__)


def test_cal::asttype_constructor_args():
    sig = inspect.signature(cal::AstType.__init__)
    params = list(sig.parameters.keys())
    assert "builtin" in params, "Missing parameter 'builtin'"

def test_cal::asttype_has_builtin():
    assert hasattr(cal::AstType, "builtin")
    descriptor = None
    for klass in cal::AstType.__mro__:
        if "builtin" in klass.__dict__:
            descriptor = klass.__dict__["builtin"]
            break
    assert isinstance(descriptor, property)



def test_cal::aststructure_is_not_abstract():
    assert not inspect.isabstract(cal::AstStructure)


def test_cal::aststructure_constructor_exists():
    assert callable(cal::AstStructure.__init__)


def test_cal::aststructure_constructor_args():
    sig = inspect.signature(cal::AstStructure.__init__)
    params = list(sig.parameters.keys())



def test_cal::astactorvariable_is_not_abstract():
    assert not inspect.isabstract(cal::AstActorVariable)


def test_cal::astactorvariable_constructor_exists():
    assert callable(cal::AstActorVariable.__init__)


def test_cal::astactorvariable_constructor_args():
    sig = inspect.signature(cal::AstActorVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal::astactorvariable_has_name():
    assert hasattr(cal::AstActorVariable, "name")
    descriptor = None
    for klass in cal::AstActorVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_astabstractactor_is_not_abstract():
    assert not inspect.isabstract(AstAbstractActor)


def test_astabstractactor_constructor_exists():
    assert callable(AstAbstractActor.__init__)


def test_astabstractactor_constructor_args():
    sig = inspect.signature(AstAbstractActor.__init__)
    params = list(sig.parameters.keys())



def test_cal::astactor_is_not_abstract():
    assert not inspect.isabstract(cal::AstActor)


def test_cal::astactor_constructor_exists():
    assert callable(cal::AstActor.__init__)


def test_cal::astactor_constructor_args():
    sig = inspect.signature(cal::AstActor.__init__)
    params = list(sig.parameters.keys())



def test_cal::astexternalactor_is_not_abstract():
    assert not inspect.isabstract(cal::AstExternalActor)


def test_cal::astexternalactor_constructor_exists():
    assert callable(cal::AstExternalActor.__init__)


def test_cal::astexternalactor_constructor_args():
    sig = inspect.signature(cal::AstExternalActor.__init__)
    params = list(sig.parameters.keys())



def test_cal::astnetwork_is_not_abstract():
    assert not inspect.isabstract(cal::AstNetwork)


def test_cal::astnetwork_constructor_exists():
    assert callable(cal::AstNetwork.__init__)


def test_cal::astnetwork_constructor_args():
    sig = inspect.signature(cal::AstNetwork.__init__)
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
cal::AstConnection_strategy = st.builds(
    cal::AstConnection,
    outPort=
        safe_text,
    inPort=
        safe_text
)
cal::AstExpression_strategy = st.builds(
    cal::AstExpression,
)
cal::AstAssignParameter_strategy = st.builds(
    cal::AstAssignParameter,
    name=
        safe_text
)
cal::AstTypeName_strategy = st.builds(
    cal::AstTypeName,
    name=
        safe_text
)
cal::AstAnnotation_strategy = st.builds(
    cal::AstAnnotation,
    name=
        safe_text
)
cal::EObject_strategy = st.builds(
    cal::EObject,
)
cal::AstVariable_strategy = st.builds(
    cal::AstVariable,
    name=
        safe_text,
    constant=
        st.booleans()
)
cal::Import_strategy = st.builds(
    cal::Import,
    importedNamespace=
        safe_text
)
cal::AstEntity_strategy = st.builds(
    cal::AstEntity,
)
cal::AstPort_strategy = st.builds(
    cal::AstPort,
    name=
        safe_text
)
cal::AstAbstractActor_strategy = st.builds(
    cal::AstAbstractActor,
    name=
        safe_text
)
AstUnit_strategy = st.builds(
    AstUnit,
)
AstPackage_strategy = st.builds(
    AstPackage,
)
cal::AstUnit_strategy = st.builds(
    cal::AstUnit,
)
AstTop_strategy = st.builds(
    AstTop,
)
cal::AstNamespace_strategy = st.builds(
    cal::AstNamespace,
    name=
        safe_text
)
cal::AstPackage_strategy = st.builds(
    cal::AstPackage,
)
cal::AstTop_strategy = st.builds(
    cal::AstTop,
)
AstAction_strategy = st.builds(
    AstAction,
)
cal::AstInitialize_strategy = st.builds(
    cal::AstInitialize,
)
cal::AstAnnotationArgument_strategy = st.builds(
    cal::AstAnnotationArgument,
    name=
        safe_text,
    value=
        safe_text
)
cal::AstTypeParameterList_strategy = st.builds(
    cal::AstTypeParameterList,
)
AstExpressionLiteral_strategy = st.builds(
    AstExpressionLiteral,
)
cal::AstExpressionInteger_strategy = st.builds(
    cal::AstExpressionInteger,
    value=
        safe_text
)
cal::AstExpressionString_strategy = st.builds(
    cal::AstExpressionString,
    value=
        safe_text
)
cal::AstExpressionFloat_strategy = st.builds(
    cal::AstExpressionFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cal::AstExpressionBoolean_strategy = st.builds(
    cal::AstExpressionBoolean,
    value=
        st.booleans()
)
cal::AstTypeParam_strategy = st.builds(
    cal::AstTypeParam,
    name=
        safe_text
)
cal::AstGenerator_strategy = st.builds(
    cal::AstGenerator,
)
AstExpression_strategy = st.builds(
    AstExpression,
)
cal::AstExpressionUnary_strategy = st.builds(
    cal::AstExpressionUnary,
    unaryOperator=
        safe_text
)
cal::AstExpressionBinary_strategy = st.builds(
    cal::AstExpressionBinary,
    operator=
        safe_text
)
cal::AstExpressionIf_strategy = st.builds(
    cal::AstExpressionIf,
)
cal::AstExpressionList_strategy = st.builds(
    cal::AstExpressionList,
)
cal::AstExpressionCall_strategy = st.builds(
    cal::AstExpressionCall,
)
cal::AstExpressionLiteral_strategy = st.builds(
    cal::AstExpressionLiteral,
)
cal::AstExpressionVariable_strategy = st.builds(
    cal::AstExpressionVariable,
)
cal::AstForeachGenerator_strategy = st.builds(
    cal::AstForeachGenerator,
)
cal::AstOutputPattern_strategy = st.builds(
    cal::AstOutputPattern,
)
cal::AstMemberAccess_strategy = st.builds(
    cal::AstMemberAccess,
    name=
        safe_text
)
cal::AstVariableReference_strategy = st.builds(
    cal::AstVariableReference,
)
AstStatement_strategy = st.builds(
    AstStatement,
)
cal::AstStatementIf_strategy = st.builds(
    cal::AstStatementIf,
)
cal::AstStatementForeach_strategy = st.builds(
    cal::AstStatementForeach,
)
cal::AstStatementBlock_strategy = st.builds(
    cal::AstStatementBlock,
)
cal::AstStatementWhile_strategy = st.builds(
    cal::AstStatementWhile,
)
cal::AstStatementCall_strategy = st.builds(
    cal::AstStatementCall,
)
cal::AstStatementAssign_strategy = st.builds(
    cal::AstStatementAssign,
)
cal::AstInequality_strategy = st.builds(
    cal::AstInequality,
)
cal::AstTag_strategy = st.builds(
    cal::AstTag,
    identifiers=
        safe_text
)
cal::AstExternalProcedure_strategy = st.builds(
    cal::AstExternalProcedure,
)
cal::AstStatement_strategy = st.builds(
    cal::AstStatement,
)
AstExternalProcedure_strategy = st.builds(
    AstExternalProcedure,
)
cal::AstInputPattern_strategy = st.builds(
    cal::AstInputPattern,
)
cal::AstTransition_strategy = st.builds(
    cal::AstTransition,
)
cal::AstState_strategy = st.builds(
    cal::AstState,
    name=
        safe_text
)
cal::AstProcedure_strategy = st.builds(
    cal::AstProcedure,
    name=
        safe_text
)
AstExternalFunction_strategy = st.builds(
    AstExternalFunction,
)
cal::AstFunction_strategy = st.builds(
    cal::AstFunction,
    name=
        safe_text
)
cal::AstExternalFunction_strategy = st.builds(
    cal::AstExternalFunction,
)
cal::AstPriority_strategy = st.builds(
    cal::AstPriority,
)
cal::AstSchedule_strategy = st.builds(
    cal::AstSchedule,
)
cal::AstAction_strategy = st.builds(
    cal::AstAction,
)
cal::AstConnectionAttribute_strategy = st.builds(
    cal::AstConnectionAttribute,
    name=
        safe_text
)
cal::AstActorVariableReference_strategy = st.builds(
    cal::AstActorVariableReference,
)
cal::AstTypeDefinitionParameter_strategy = st.builds(
    cal::AstTypeDefinitionParameter,
)
cal::AstType_strategy = st.builds(
    cal::AstType,
    builtin=
        safe_text
)
cal::AstStructure_strategy = st.builds(
    cal::AstStructure,
)
cal::AstActorVariable_strategy = st.builds(
    cal::AstActorVariable,
    name=
        safe_text
)
AstAbstractActor_strategy = st.builds(
    AstAbstractActor,
)
cal::AstActor_strategy = st.builds(
    cal::AstActor,
)
cal::AstExternalActor_strategy = st.builds(
    cal::AstExternalActor,
)
cal::AstNetwork_strategy = st.builds(
    cal::AstNetwork,
)

@given(instance=cal::AstConnection_strategy)
@settings(max_examples=50)
def test_cal::astconnection_instantiation(instance):
    assert isinstance(instance, cal::AstConnection)

@given(instance=cal::AstConnection_strategy)
def test_cal::astconnection_outPort_type(instance):
    assert isinstance(instance.outPort, str)


@given(instance=cal::AstConnection_strategy)
def test_cal::astconnection_outPort_setter(instance):
    original = instance.outPort
    instance.outPort = original
    assert instance.outPort == original

@given(instance=cal::AstConnection_strategy)
def test_cal::astconnection_inPort_type(instance):
    assert isinstance(instance.inPort, str)


@given(instance=cal::AstConnection_strategy)
def test_cal::astconnection_inPort_setter(instance):
    original = instance.inPort
    instance.inPort = original
    assert instance.inPort == original

@given(instance=cal::AstExpression_strategy)
@settings(max_examples=50)
def test_cal::astexpression_instantiation(instance):
    assert isinstance(instance, cal::AstExpression)

@given(instance=cal::AstAssignParameter_strategy)
@settings(max_examples=50)
def test_cal::astassignparameter_instantiation(instance):
    assert isinstance(instance, cal::AstAssignParameter)

@given(instance=cal::AstAssignParameter_strategy)
def test_cal::astassignparameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstAssignParameter_strategy)
def test_cal::astassignparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstTypeName_strategy)
@settings(max_examples=50)
def test_cal::asttypename_instantiation(instance):
    assert isinstance(instance, cal::AstTypeName)

@given(instance=cal::AstTypeName_strategy)
def test_cal::asttypename_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstTypeName_strategy)
def test_cal::asttypename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstAnnotation_strategy)
@settings(max_examples=50)
def test_cal::astannotation_instantiation(instance):
    assert isinstance(instance, cal::AstAnnotation)

@given(instance=cal::AstAnnotation_strategy)
def test_cal::astannotation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstAnnotation_strategy)
def test_cal::astannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::EObject_strategy)
@settings(max_examples=50)
def test_cal::eobject_instantiation(instance):
    assert isinstance(instance, cal::EObject)

@given(instance=cal::AstVariable_strategy)
@settings(max_examples=50)
def test_cal::astvariable_instantiation(instance):
    assert isinstance(instance, cal::AstVariable)

@given(instance=cal::AstVariable_strategy)
def test_cal::astvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstVariable_strategy)
def test_cal::astvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstVariable_strategy)
def test_cal::astvariable_constant_type(instance):
    assert isinstance(instance.constant, bool)


@given(instance=cal::AstVariable_strategy)
def test_cal::astvariable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=cal::Import_strategy)
@settings(max_examples=50)
def test_cal::import_instantiation(instance):
    assert isinstance(instance, cal::Import)

@given(instance=cal::Import_strategy)
def test_cal::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=cal::Import_strategy)
def test_cal::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=cal::AstEntity_strategy)
@settings(max_examples=50)
def test_cal::astentity_instantiation(instance):
    assert isinstance(instance, cal::AstEntity)

@given(instance=cal::AstPort_strategy)
@settings(max_examples=50)
def test_cal::astport_instantiation(instance):
    assert isinstance(instance, cal::AstPort)

@given(instance=cal::AstPort_strategy)
def test_cal::astport_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstPort_strategy)
def test_cal::astport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstAbstractActor_strategy)
@settings(max_examples=50)
def test_cal::astabstractactor_instantiation(instance):
    assert isinstance(instance, cal::AstAbstractActor)

@given(instance=cal::AstAbstractActor_strategy)
def test_cal::astabstractactor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstAbstractActor_strategy)
def test_cal::astabstractactor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstUnit_strategy)
@settings(max_examples=50)
def test_astunit_instantiation(instance):
    assert isinstance(instance, AstUnit)

@given(instance=AstPackage_strategy)
@settings(max_examples=50)
def test_astpackage_instantiation(instance):
    assert isinstance(instance, AstPackage)

@given(instance=cal::AstUnit_strategy)
@settings(max_examples=50)
def test_cal::astunit_instantiation(instance):
    assert isinstance(instance, cal::AstUnit)

@given(instance=AstTop_strategy)
@settings(max_examples=50)
def test_asttop_instantiation(instance):
    assert isinstance(instance, AstTop)

@given(instance=cal::AstNamespace_strategy)
@settings(max_examples=50)
def test_cal::astnamespace_instantiation(instance):
    assert isinstance(instance, cal::AstNamespace)

@given(instance=cal::AstNamespace_strategy)
def test_cal::astnamespace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstNamespace_strategy)
def test_cal::astnamespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstPackage_strategy)
@settings(max_examples=50)
def test_cal::astpackage_instantiation(instance):
    assert isinstance(instance, cal::AstPackage)

@given(instance=cal::AstTop_strategy)
@settings(max_examples=50)
def test_cal::asttop_instantiation(instance):
    assert isinstance(instance, cal::AstTop)

@given(instance=AstAction_strategy)
@settings(max_examples=50)
def test_astaction_instantiation(instance):
    assert isinstance(instance, AstAction)

@given(instance=cal::AstInitialize_strategy)
@settings(max_examples=50)
def test_cal::astinitialize_instantiation(instance):
    assert isinstance(instance, cal::AstInitialize)

@given(instance=cal::AstAnnotationArgument_strategy)
@settings(max_examples=50)
def test_cal::astannotationargument_instantiation(instance):
    assert isinstance(instance, cal::AstAnnotationArgument)

@given(instance=cal::AstAnnotationArgument_strategy)
def test_cal::astannotationargument_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstAnnotationArgument_strategy)
def test_cal::astannotationargument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstAnnotationArgument_strategy)
def test_cal::astannotationargument_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::AstAnnotationArgument_strategy)
def test_cal::astannotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::AstTypeParameterList_strategy)
@settings(max_examples=50)
def test_cal::asttypeparameterlist_instantiation(instance):
    assert isinstance(instance, cal::AstTypeParameterList)

@given(instance=AstExpressionLiteral_strategy)
@settings(max_examples=50)
def test_astexpressionliteral_instantiation(instance):
    assert isinstance(instance, AstExpressionLiteral)

@given(instance=cal::AstExpressionInteger_strategy)
@settings(max_examples=50)
def test_cal::astexpressioninteger_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionInteger)

@given(instance=cal::AstExpressionInteger_strategy)
def test_cal::astexpressioninteger_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::AstExpressionInteger_strategy)
def test_cal::astexpressioninteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::AstExpressionString_strategy)
@settings(max_examples=50)
def test_cal::astexpressionstring_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionString)

@given(instance=cal::AstExpressionString_strategy)
def test_cal::astexpressionstring_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=cal::AstExpressionString_strategy)
def test_cal::astexpressionstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::AstExpressionFloat_strategy)
@settings(max_examples=50)
def test_cal::astexpressionfloat_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionFloat)

@given(instance=cal::AstExpressionFloat_strategy)
def test_cal::astexpressionfloat_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=cal::AstExpressionFloat_strategy)
def test_cal::astexpressionfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::AstExpressionBoolean_strategy)
@settings(max_examples=50)
def test_cal::astexpressionboolean_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionBoolean)

@given(instance=cal::AstExpressionBoolean_strategy)
def test_cal::astexpressionboolean_value_type(instance):
    assert isinstance(instance.value, bool)


@given(instance=cal::AstExpressionBoolean_strategy)
def test_cal::astexpressionboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal::AstTypeParam_strategy)
@settings(max_examples=50)
def test_cal::asttypeparam_instantiation(instance):
    assert isinstance(instance, cal::AstTypeParam)

@given(instance=cal::AstTypeParam_strategy)
def test_cal::asttypeparam_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstTypeParam_strategy)
def test_cal::asttypeparam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstGenerator_strategy)
@settings(max_examples=50)
def test_cal::astgenerator_instantiation(instance):
    assert isinstance(instance, cal::AstGenerator)

@given(instance=AstExpression_strategy)
@settings(max_examples=50)
def test_astexpression_instantiation(instance):
    assert isinstance(instance, AstExpression)

@given(instance=cal::AstExpressionUnary_strategy)
@settings(max_examples=50)
def test_cal::astexpressionunary_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionUnary)

@given(instance=cal::AstExpressionUnary_strategy)
def test_cal::astexpressionunary_unaryOperator_type(instance):
    assert isinstance(instance.unaryOperator, str)


@given(instance=cal::AstExpressionUnary_strategy)
def test_cal::astexpressionunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal::AstExpressionBinary_strategy)
@settings(max_examples=50)
def test_cal::astexpressionbinary_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionBinary)

@given(instance=cal::AstExpressionBinary_strategy)
def test_cal::astexpressionbinary_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=cal::AstExpressionBinary_strategy)
def test_cal::astexpressionbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal::AstExpressionIf_strategy)
@settings(max_examples=50)
def test_cal::astexpressionif_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionIf)

@given(instance=cal::AstExpressionList_strategy)
@settings(max_examples=50)
def test_cal::astexpressionlist_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionList)

@given(instance=cal::AstExpressionCall_strategy)
@settings(max_examples=50)
def test_cal::astexpressioncall_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionCall)

@given(instance=cal::AstExpressionLiteral_strategy)
@settings(max_examples=50)
def test_cal::astexpressionliteral_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionLiteral)

@given(instance=cal::AstExpressionVariable_strategy)
@settings(max_examples=50)
def test_cal::astexpressionvariable_instantiation(instance):
    assert isinstance(instance, cal::AstExpressionVariable)

@given(instance=cal::AstForeachGenerator_strategy)
@settings(max_examples=50)
def test_cal::astforeachgenerator_instantiation(instance):
    assert isinstance(instance, cal::AstForeachGenerator)

@given(instance=cal::AstOutputPattern_strategy)
@settings(max_examples=50)
def test_cal::astoutputpattern_instantiation(instance):
    assert isinstance(instance, cal::AstOutputPattern)

@given(instance=cal::AstMemberAccess_strategy)
@settings(max_examples=50)
def test_cal::astmemberaccess_instantiation(instance):
    assert isinstance(instance, cal::AstMemberAccess)

@given(instance=cal::AstMemberAccess_strategy)
def test_cal::astmemberaccess_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstMemberAccess_strategy)
def test_cal::astmemberaccess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstVariableReference_strategy)
@settings(max_examples=50)
def test_cal::astvariablereference_instantiation(instance):
    assert isinstance(instance, cal::AstVariableReference)

@given(instance=AstStatement_strategy)
@settings(max_examples=50)
def test_aststatement_instantiation(instance):
    assert isinstance(instance, AstStatement)

@given(instance=cal::AstStatementIf_strategy)
@settings(max_examples=50)
def test_cal::aststatementif_instantiation(instance):
    assert isinstance(instance, cal::AstStatementIf)

@given(instance=cal::AstStatementForeach_strategy)
@settings(max_examples=50)
def test_cal::aststatementforeach_instantiation(instance):
    assert isinstance(instance, cal::AstStatementForeach)

@given(instance=cal::AstStatementBlock_strategy)
@settings(max_examples=50)
def test_cal::aststatementblock_instantiation(instance):
    assert isinstance(instance, cal::AstStatementBlock)

@given(instance=cal::AstStatementWhile_strategy)
@settings(max_examples=50)
def test_cal::aststatementwhile_instantiation(instance):
    assert isinstance(instance, cal::AstStatementWhile)

@given(instance=cal::AstStatementCall_strategy)
@settings(max_examples=50)
def test_cal::aststatementcall_instantiation(instance):
    assert isinstance(instance, cal::AstStatementCall)

@given(instance=cal::AstStatementAssign_strategy)
@settings(max_examples=50)
def test_cal::aststatementassign_instantiation(instance):
    assert isinstance(instance, cal::AstStatementAssign)

@given(instance=cal::AstInequality_strategy)
@settings(max_examples=50)
def test_cal::astinequality_instantiation(instance):
    assert isinstance(instance, cal::AstInequality)

@given(instance=cal::AstTag_strategy)
@settings(max_examples=50)
def test_cal::asttag_instantiation(instance):
    assert isinstance(instance, cal::AstTag)

@given(instance=cal::AstTag_strategy)
def test_cal::asttag_identifiers_type(instance):
    assert isinstance(instance.identifiers, str)


@given(instance=cal::AstTag_strategy)
def test_cal::asttag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=cal::AstExternalProcedure_strategy)
@settings(max_examples=50)
def test_cal::astexternalprocedure_instantiation(instance):
    assert isinstance(instance, cal::AstExternalProcedure)

@given(instance=cal::AstStatement_strategy)
@settings(max_examples=50)
def test_cal::aststatement_instantiation(instance):
    assert isinstance(instance, cal::AstStatement)

@given(instance=AstExternalProcedure_strategy)
@settings(max_examples=50)
def test_astexternalprocedure_instantiation(instance):
    assert isinstance(instance, AstExternalProcedure)

@given(instance=cal::AstInputPattern_strategy)
@settings(max_examples=50)
def test_cal::astinputpattern_instantiation(instance):
    assert isinstance(instance, cal::AstInputPattern)

@given(instance=cal::AstTransition_strategy)
@settings(max_examples=50)
def test_cal::asttransition_instantiation(instance):
    assert isinstance(instance, cal::AstTransition)

@given(instance=cal::AstState_strategy)
@settings(max_examples=50)
def test_cal::aststate_instantiation(instance):
    assert isinstance(instance, cal::AstState)

@given(instance=cal::AstState_strategy)
def test_cal::aststate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstState_strategy)
def test_cal::aststate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstProcedure_strategy)
@settings(max_examples=50)
def test_cal::astprocedure_instantiation(instance):
    assert isinstance(instance, cal::AstProcedure)

@given(instance=cal::AstProcedure_strategy)
def test_cal::astprocedure_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstProcedure_strategy)
def test_cal::astprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstExternalFunction_strategy)
@settings(max_examples=50)
def test_astexternalfunction_instantiation(instance):
    assert isinstance(instance, AstExternalFunction)

@given(instance=cal::AstFunction_strategy)
@settings(max_examples=50)
def test_cal::astfunction_instantiation(instance):
    assert isinstance(instance, cal::AstFunction)

@given(instance=cal::AstFunction_strategy)
def test_cal::astfunction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstFunction_strategy)
def test_cal::astfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstExternalFunction_strategy)
@settings(max_examples=50)
def test_cal::astexternalfunction_instantiation(instance):
    assert isinstance(instance, cal::AstExternalFunction)

@given(instance=cal::AstPriority_strategy)
@settings(max_examples=50)
def test_cal::astpriority_instantiation(instance):
    assert isinstance(instance, cal::AstPriority)

@given(instance=cal::AstSchedule_strategy)
@settings(max_examples=50)
def test_cal::astschedule_instantiation(instance):
    assert isinstance(instance, cal::AstSchedule)

@given(instance=cal::AstAction_strategy)
@settings(max_examples=50)
def test_cal::astaction_instantiation(instance):
    assert isinstance(instance, cal::AstAction)

@given(instance=cal::AstConnectionAttribute_strategy)
@settings(max_examples=50)
def test_cal::astconnectionattribute_instantiation(instance):
    assert isinstance(instance, cal::AstConnectionAttribute)

@given(instance=cal::AstConnectionAttribute_strategy)
def test_cal::astconnectionattribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstConnectionAttribute_strategy)
def test_cal::astconnectionattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal::AstActorVariableReference_strategy)
@settings(max_examples=50)
def test_cal::astactorvariablereference_instantiation(instance):
    assert isinstance(instance, cal::AstActorVariableReference)

@given(instance=cal::AstTypeDefinitionParameter_strategy)
@settings(max_examples=50)
def test_cal::asttypedefinitionparameter_instantiation(instance):
    assert isinstance(instance, cal::AstTypeDefinitionParameter)

@given(instance=cal::AstType_strategy)
@settings(max_examples=50)
def test_cal::asttype_instantiation(instance):
    assert isinstance(instance, cal::AstType)

@given(instance=cal::AstType_strategy)
def test_cal::asttype_builtin_type(instance):
    assert isinstance(instance.builtin, str)


@given(instance=cal::AstType_strategy)
def test_cal::asttype_builtin_setter(instance):
    original = instance.builtin
    instance.builtin = original
    assert instance.builtin == original

@given(instance=cal::AstStructure_strategy)
@settings(max_examples=50)
def test_cal::aststructure_instantiation(instance):
    assert isinstance(instance, cal::AstStructure)

@given(instance=cal::AstActorVariable_strategy)
@settings(max_examples=50)
def test_cal::astactorvariable_instantiation(instance):
    assert isinstance(instance, cal::AstActorVariable)

@given(instance=cal::AstActorVariable_strategy)
def test_cal::astactorvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=cal::AstActorVariable_strategy)
def test_cal::astactorvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstAbstractActor_strategy)
@settings(max_examples=50)
def test_astabstractactor_instantiation(instance):
    assert isinstance(instance, AstAbstractActor)

@given(instance=cal::AstActor_strategy)
@settings(max_examples=50)
def test_cal::astactor_instantiation(instance):
    assert isinstance(instance, cal::AstActor)

@given(instance=cal::AstExternalActor_strategy)
@settings(max_examples=50)
def test_cal::astexternalactor_instantiation(instance):
    assert isinstance(instance, cal::AstExternalActor)

@given(instance=cal::AstNetwork_strategy)
@settings(max_examples=50)
def test_cal::astnetwork_instantiation(instance):
    assert isinstance(instance, cal::AstNetwork)
