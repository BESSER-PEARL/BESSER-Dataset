import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    cal_AstOutputPattern,
    cal_AstMemberAccess,
    cal_AstVariableReference,
    AstStatement,
    cal_AstStatementWhile,
    cal_AstStatementIf,
    cal_AstStatementCall,
    cal_AstStatementAssign,
    cal_AstInequality,
    cal_AstTag,
    cal_AstExternalProcedure,
    cal_AstStatement,
    AstExternalProcedure,
    cal_AstInputPattern,
    cal_AstTransition,
    cal_AstState,
    cal_AstProcedure,
    AstExternalFunction,
    cal_AstExternalFunction,
    cal_AstPriority,
    cal_AstSchedule,
    cal_AstAction,
    cal_AstConnectionAttribute,
    cal_AstActorVariableReference,
    cal_AstTypeDefinitionParameter,
    cal_AstType,
    cal_AstStructure,
    cal_AstActorVariable,
    AstAbstractActor,
    cal_AstActor,
    cal_AstExternalActor,
    cal_AstNetwork,
    cal_AstConnection,
    cal_AstExpression,
    cal_AstAssignParameter,
    cal_AstTypeName,
    cal_AstAnnotation,
    cal_EObject,
    cal_AstVariable,
    cal_AstFunction,
    cal_Import,
    cal_AstEntity,
    cal_AstPort,
    cal_AstAbstractActor,
    AstUnit,
    AstPackage,
    cal_AstUnit,
    AstTop,
    cal_AstNamespace,
    cal_AstPackage,
    cal_AstTop,
    AstAction,
    cal_AstInitialize,
    cal_AstAnnotationArgument,
    cal_AstTypeParameterList,
    AstExpressionLiteral,
    cal_AstExpressionInteger,
    cal_AstExpressionFloat,
    cal_AstExpressionString,
    cal_AstExpressionBoolean,
    cal_AstTypeParam,
    cal_AstGenerator,
    AstExpression,
    cal_AstExpressionIf,
    cal_AstExpressionUnary,
    cal_AstExpressionBinary,
    cal_AstExpressionList,
    cal_AstExpressionCall,
    cal_AstExpressionLiteral,
    cal_AstExpressionVariable,
    cal_AstStatementBlock,
    cal_AstForeachGenerator,
    cal_AstStatementForeach,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cal_astoutputpattern_is_not_abstract():
    assert not inspect.isabstract(cal_AstOutputPattern)


def test_cal_astoutputpattern_constructor_exists():
    assert callable(cal_AstOutputPattern.__init__)


def test_cal_astoutputpattern_constructor_args():
    sig = inspect.signature(cal_AstOutputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal_astmemberaccess_is_not_abstract():
    assert not inspect.isabstract(cal_AstMemberAccess)


def test_cal_astmemberaccess_constructor_exists():
    assert callable(cal_AstMemberAccess.__init__)


def test_cal_astmemberaccess_constructor_args():
    sig = inspect.signature(cal_AstMemberAccess.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astmemberaccess_has_name():
    assert hasattr(cal_AstMemberAccess, "name")
    descriptor = None
    for klass in cal_AstMemberAccess.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astvariablereference_is_not_abstract():
    assert not inspect.isabstract(cal_AstVariableReference)


def test_cal_astvariablereference_constructor_exists():
    assert callable(cal_AstVariableReference.__init__)


def test_cal_astvariablereference_constructor_args():
    sig = inspect.signature(cal_AstVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_aststatement_is_not_abstract():
    assert not inspect.isabstract(AstStatement)


def test_aststatement_constructor_exists():
    assert callable(AstStatement.__init__)


def test_aststatement_constructor_args():
    sig = inspect.signature(AstStatement.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementwhile_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementWhile)


def test_cal_aststatementwhile_constructor_exists():
    assert callable(cal_AstStatementWhile.__init__)


def test_cal_aststatementwhile_constructor_args():
    sig = inspect.signature(cal_AstStatementWhile.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementif_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementIf)


def test_cal_aststatementif_constructor_exists():
    assert callable(cal_AstStatementIf.__init__)


def test_cal_aststatementif_constructor_args():
    sig = inspect.signature(cal_AstStatementIf.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementcall_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementCall)


def test_cal_aststatementcall_constructor_exists():
    assert callable(cal_AstStatementCall.__init__)


def test_cal_aststatementcall_constructor_args():
    sig = inspect.signature(cal_AstStatementCall.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementassign_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementAssign)


def test_cal_aststatementassign_constructor_exists():
    assert callable(cal_AstStatementAssign.__init__)


def test_cal_aststatementassign_constructor_args():
    sig = inspect.signature(cal_AstStatementAssign.__init__)
    params = list(sig.parameters.keys())



def test_cal_astinequality_is_not_abstract():
    assert not inspect.isabstract(cal_AstInequality)


def test_cal_astinequality_constructor_exists():
    assert callable(cal_AstInequality.__init__)


def test_cal_astinequality_constructor_args():
    sig = inspect.signature(cal_AstInequality.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttag_is_not_abstract():
    assert not inspect.isabstract(cal_AstTag)


def test_cal_asttag_constructor_exists():
    assert callable(cal_AstTag.__init__)


def test_cal_asttag_constructor_args():
    sig = inspect.signature(cal_AstTag.__init__)
    params = list(sig.parameters.keys())
    assert "identifiers" in params, "Missing parameter 'identifiers'"

def test_cal_asttag_has_identifiers():
    assert hasattr(cal_AstTag, "identifiers")
    descriptor = None
    for klass in cal_AstTag.__mro__:
        if "identifiers" in klass.__dict__:
            descriptor = klass.__dict__["identifiers"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexternalprocedure_is_not_abstract():
    assert not inspect.isabstract(cal_AstExternalProcedure)


def test_cal_astexternalprocedure_constructor_exists():
    assert callable(cal_AstExternalProcedure.__init__)


def test_cal_astexternalprocedure_constructor_args():
    sig = inspect.signature(cal_AstExternalProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatement_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatement)


def test_cal_aststatement_constructor_exists():
    assert callable(cal_AstStatement.__init__)


def test_cal_aststatement_constructor_args():
    sig = inspect.signature(cal_AstStatement.__init__)
    params = list(sig.parameters.keys())



def test_astexternalprocedure_is_not_abstract():
    assert not inspect.isabstract(AstExternalProcedure)


def test_astexternalprocedure_constructor_exists():
    assert callable(AstExternalProcedure.__init__)


def test_astexternalprocedure_constructor_args():
    sig = inspect.signature(AstExternalProcedure.__init__)
    params = list(sig.parameters.keys())



def test_cal_astinputpattern_is_not_abstract():
    assert not inspect.isabstract(cal_AstInputPattern)


def test_cal_astinputpattern_constructor_exists():
    assert callable(cal_AstInputPattern.__init__)


def test_cal_astinputpattern_constructor_args():
    sig = inspect.signature(cal_AstInputPattern.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttransition_is_not_abstract():
    assert not inspect.isabstract(cal_AstTransition)


def test_cal_asttransition_constructor_exists():
    assert callable(cal_AstTransition.__init__)


def test_cal_asttransition_constructor_args():
    sig = inspect.signature(cal_AstTransition.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststate_is_not_abstract():
    assert not inspect.isabstract(cal_AstState)


def test_cal_aststate_constructor_exists():
    assert callable(cal_AstState.__init__)


def test_cal_aststate_constructor_args():
    sig = inspect.signature(cal_AstState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_aststate_has_name():
    assert hasattr(cal_AstState, "name")
    descriptor = None
    for klass in cal_AstState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astprocedure_is_not_abstract():
    assert not inspect.isabstract(cal_AstProcedure)


def test_cal_astprocedure_constructor_exists():
    assert callable(cal_AstProcedure.__init__)


def test_cal_astprocedure_constructor_args():
    sig = inspect.signature(cal_AstProcedure.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astprocedure_has_name():
    assert hasattr(cal_AstProcedure, "name")
    descriptor = None
    for klass in cal_AstProcedure.__mro__:
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



def test_cal_astexternalfunction_is_not_abstract():
    assert not inspect.isabstract(cal_AstExternalFunction)


def test_cal_astexternalfunction_constructor_exists():
    assert callable(cal_AstExternalFunction.__init__)


def test_cal_astexternalfunction_constructor_args():
    sig = inspect.signature(cal_AstExternalFunction.__init__)
    params = list(sig.parameters.keys())



def test_cal_astpriority_is_not_abstract():
    assert not inspect.isabstract(cal_AstPriority)


def test_cal_astpriority_constructor_exists():
    assert callable(cal_AstPriority.__init__)


def test_cal_astpriority_constructor_args():
    sig = inspect.signature(cal_AstPriority.__init__)
    params = list(sig.parameters.keys())



def test_cal_astschedule_is_not_abstract():
    assert not inspect.isabstract(cal_AstSchedule)


def test_cal_astschedule_constructor_exists():
    assert callable(cal_AstSchedule.__init__)


def test_cal_astschedule_constructor_args():
    sig = inspect.signature(cal_AstSchedule.__init__)
    params = list(sig.parameters.keys())



def test_cal_astaction_is_not_abstract():
    assert not inspect.isabstract(cal_AstAction)


def test_cal_astaction_constructor_exists():
    assert callable(cal_AstAction.__init__)


def test_cal_astaction_constructor_args():
    sig = inspect.signature(cal_AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal_astconnectionattribute_is_not_abstract():
    assert not inspect.isabstract(cal_AstConnectionAttribute)


def test_cal_astconnectionattribute_constructor_exists():
    assert callable(cal_AstConnectionAttribute.__init__)


def test_cal_astconnectionattribute_constructor_args():
    sig = inspect.signature(cal_AstConnectionAttribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astconnectionattribute_has_name():
    assert hasattr(cal_AstConnectionAttribute, "name")
    descriptor = None
    for klass in cal_AstConnectionAttribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astactorvariablereference_is_not_abstract():
    assert not inspect.isabstract(cal_AstActorVariableReference)


def test_cal_astactorvariablereference_constructor_exists():
    assert callable(cal_AstActorVariableReference.__init__)


def test_cal_astactorvariablereference_constructor_args():
    sig = inspect.signature(cal_AstActorVariableReference.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttypedefinitionparameter_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeDefinitionParameter)


def test_cal_asttypedefinitionparameter_constructor_exists():
    assert callable(cal_AstTypeDefinitionParameter.__init__)


def test_cal_asttypedefinitionparameter_constructor_args():
    sig = inspect.signature(cal_AstTypeDefinitionParameter.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttype_is_not_abstract():
    assert not inspect.isabstract(cal_AstType)


def test_cal_asttype_constructor_exists():
    assert callable(cal_AstType.__init__)


def test_cal_asttype_constructor_args():
    sig = inspect.signature(cal_AstType.__init__)
    params = list(sig.parameters.keys())
    assert "builtin" in params, "Missing parameter 'builtin'"

def test_cal_asttype_has_builtin():
    assert hasattr(cal_AstType, "builtin")
    descriptor = None
    for klass in cal_AstType.__mro__:
        if "builtin" in klass.__dict__:
            descriptor = klass.__dict__["builtin"]
            break
    assert isinstance(descriptor, property)



def test_cal_aststructure_is_not_abstract():
    assert not inspect.isabstract(cal_AstStructure)


def test_cal_aststructure_constructor_exists():
    assert callable(cal_AstStructure.__init__)


def test_cal_aststructure_constructor_args():
    sig = inspect.signature(cal_AstStructure.__init__)
    params = list(sig.parameters.keys())



def test_cal_astactorvariable_is_not_abstract():
    assert not inspect.isabstract(cal_AstActorVariable)


def test_cal_astactorvariable_constructor_exists():
    assert callable(cal_AstActorVariable.__init__)


def test_cal_astactorvariable_constructor_args():
    sig = inspect.signature(cal_AstActorVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astactorvariable_has_name():
    assert hasattr(cal_AstActorVariable, "name")
    descriptor = None
    for klass in cal_AstActorVariable.__mro__:
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



def test_cal_astactor_is_not_abstract():
    assert not inspect.isabstract(cal_AstActor)


def test_cal_astactor_constructor_exists():
    assert callable(cal_AstActor.__init__)


def test_cal_astactor_constructor_args():
    sig = inspect.signature(cal_AstActor.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexternalactor_is_not_abstract():
    assert not inspect.isabstract(cal_AstExternalActor)


def test_cal_astexternalactor_constructor_exists():
    assert callable(cal_AstExternalActor.__init__)


def test_cal_astexternalactor_constructor_args():
    sig = inspect.signature(cal_AstExternalActor.__init__)
    params = list(sig.parameters.keys())



def test_cal_astnetwork_is_not_abstract():
    assert not inspect.isabstract(cal_AstNetwork)


def test_cal_astnetwork_constructor_exists():
    assert callable(cal_AstNetwork.__init__)


def test_cal_astnetwork_constructor_args():
    sig = inspect.signature(cal_AstNetwork.__init__)
    params = list(sig.parameters.keys())



def test_cal_astconnection_is_not_abstract():
    assert not inspect.isabstract(cal_AstConnection)


def test_cal_astconnection_constructor_exists():
    assert callable(cal_AstConnection.__init__)


def test_cal_astconnection_constructor_args():
    sig = inspect.signature(cal_AstConnection.__init__)
    params = list(sig.parameters.keys())
    assert "outPort" in params, "Missing parameter 'outPort'"
    assert "inPort" in params, "Missing parameter 'inPort'"

def test_cal_astconnection_has_outPort():
    assert hasattr(cal_AstConnection, "outPort")
    descriptor = None
    for klass in cal_AstConnection.__mro__:
        if "outPort" in klass.__dict__:
            descriptor = klass.__dict__["outPort"]
            break
    assert isinstance(descriptor, property)

def test_cal_astconnection_has_inPort():
    assert hasattr(cal_AstConnection, "inPort")
    descriptor = None
    for klass in cal_AstConnection.__mro__:
        if "inPort" in klass.__dict__:
            descriptor = klass.__dict__["inPort"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpression_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpression)


def test_cal_astexpression_constructor_exists():
    assert callable(cal_AstExpression.__init__)


def test_cal_astexpression_constructor_args():
    sig = inspect.signature(cal_AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal_astassignparameter_is_not_abstract():
    assert not inspect.isabstract(cal_AstAssignParameter)


def test_cal_astassignparameter_constructor_exists():
    assert callable(cal_AstAssignParameter.__init__)


def test_cal_astassignparameter_constructor_args():
    sig = inspect.signature(cal_AstAssignParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astassignparameter_has_name():
    assert hasattr(cal_AstAssignParameter, "name")
    descriptor = None
    for klass in cal_AstAssignParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_asttypename_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeName)


def test_cal_asttypename_constructor_exists():
    assert callable(cal_AstTypeName.__init__)


def test_cal_asttypename_constructor_args():
    sig = inspect.signature(cal_AstTypeName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_asttypename_has_name():
    assert hasattr(cal_AstTypeName, "name")
    descriptor = None
    for klass in cal_AstTypeName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astannotation_is_not_abstract():
    assert not inspect.isabstract(cal_AstAnnotation)


def test_cal_astannotation_constructor_exists():
    assert callable(cal_AstAnnotation.__init__)


def test_cal_astannotation_constructor_args():
    sig = inspect.signature(cal_AstAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astannotation_has_name():
    assert hasattr(cal_AstAnnotation, "name")
    descriptor = None
    for klass in cal_AstAnnotation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_eobject_is_not_abstract():
    assert not inspect.isabstract(cal_EObject)


def test_cal_eobject_constructor_exists():
    assert callable(cal_EObject.__init__)


def test_cal_eobject_constructor_args():
    sig = inspect.signature(cal_EObject.__init__)
    params = list(sig.parameters.keys())



def test_cal_astvariable_is_not_abstract():
    assert not inspect.isabstract(cal_AstVariable)


def test_cal_astvariable_constructor_exists():
    assert callable(cal_AstVariable.__init__)


def test_cal_astvariable_constructor_args():
    sig = inspect.signature(cal_AstVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "constant" in params, "Missing parameter 'constant'"

def test_cal_astvariable_has_name():
    assert hasattr(cal_AstVariable, "name")
    descriptor = None
    for klass in cal_AstVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_cal_astvariable_has_constant():
    assert hasattr(cal_AstVariable, "constant")
    descriptor = None
    for klass in cal_AstVariable.__mro__:
        if "constant" in klass.__dict__:
            descriptor = klass.__dict__["constant"]
            break
    assert isinstance(descriptor, property)



def test_cal_astfunction_is_not_abstract():
    assert not inspect.isabstract(cal_AstFunction)


def test_cal_astfunction_constructor_exists():
    assert callable(cal_AstFunction.__init__)


def test_cal_astfunction_constructor_args():
    sig = inspect.signature(cal_AstFunction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astfunction_has_name():
    assert hasattr(cal_AstFunction, "name")
    descriptor = None
    for klass in cal_AstFunction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_import_is_not_abstract():
    assert not inspect.isabstract(cal_Import)


def test_cal_import_constructor_exists():
    assert callable(cal_Import.__init__)


def test_cal_import_constructor_args():
    sig = inspect.signature(cal_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_cal_import_has_importedNamespace():
    assert hasattr(cal_Import, "importedNamespace")
    descriptor = None
    for klass in cal_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_cal_astentity_is_not_abstract():
    assert not inspect.isabstract(cal_AstEntity)


def test_cal_astentity_constructor_exists():
    assert callable(cal_AstEntity.__init__)


def test_cal_astentity_constructor_args():
    sig = inspect.signature(cal_AstEntity.__init__)
    params = list(sig.parameters.keys())



def test_cal_astport_is_not_abstract():
    assert not inspect.isabstract(cal_AstPort)


def test_cal_astport_constructor_exists():
    assert callable(cal_AstPort.__init__)


def test_cal_astport_constructor_args():
    sig = inspect.signature(cal_AstPort.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astport_has_name():
    assert hasattr(cal_AstPort, "name")
    descriptor = None
    for klass in cal_AstPort.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astabstractactor_is_not_abstract():
    assert not inspect.isabstract(cal_AstAbstractActor)


def test_cal_astabstractactor_constructor_exists():
    assert callable(cal_AstAbstractActor.__init__)


def test_cal_astabstractactor_constructor_args():
    sig = inspect.signature(cal_AstAbstractActor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astabstractactor_has_name():
    assert hasattr(cal_AstAbstractActor, "name")
    descriptor = None
    for klass in cal_AstAbstractActor.__mro__:
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



def test_cal_astunit_is_not_abstract():
    assert not inspect.isabstract(cal_AstUnit)


def test_cal_astunit_constructor_exists():
    assert callable(cal_AstUnit.__init__)


def test_cal_astunit_constructor_args():
    sig = inspect.signature(cal_AstUnit.__init__)
    params = list(sig.parameters.keys())



def test_asttop_is_not_abstract():
    assert not inspect.isabstract(AstTop)


def test_asttop_constructor_exists():
    assert callable(AstTop.__init__)


def test_asttop_constructor_args():
    sig = inspect.signature(AstTop.__init__)
    params = list(sig.parameters.keys())



def test_cal_astnamespace_is_not_abstract():
    assert not inspect.isabstract(cal_AstNamespace)


def test_cal_astnamespace_constructor_exists():
    assert callable(cal_AstNamespace.__init__)


def test_cal_astnamespace_constructor_args():
    sig = inspect.signature(cal_AstNamespace.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astnamespace_has_name():
    assert hasattr(cal_AstNamespace, "name")
    descriptor = None
    for klass in cal_AstNamespace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astpackage_is_not_abstract():
    assert not inspect.isabstract(cal_AstPackage)


def test_cal_astpackage_constructor_exists():
    assert callable(cal_AstPackage.__init__)


def test_cal_astpackage_constructor_args():
    sig = inspect.signature(cal_AstPackage.__init__)
    params = list(sig.parameters.keys())



def test_cal_asttop_is_not_abstract():
    assert not inspect.isabstract(cal_AstTop)


def test_cal_asttop_constructor_exists():
    assert callable(cal_AstTop.__init__)


def test_cal_asttop_constructor_args():
    sig = inspect.signature(cal_AstTop.__init__)
    params = list(sig.parameters.keys())



def test_astaction_is_not_abstract():
    assert not inspect.isabstract(AstAction)


def test_astaction_constructor_exists():
    assert callable(AstAction.__init__)


def test_astaction_constructor_args():
    sig = inspect.signature(AstAction.__init__)
    params = list(sig.parameters.keys())



def test_cal_astinitialize_is_not_abstract():
    assert not inspect.isabstract(cal_AstInitialize)


def test_cal_astinitialize_constructor_exists():
    assert callable(cal_AstInitialize.__init__)


def test_cal_astinitialize_constructor_args():
    sig = inspect.signature(cal_AstInitialize.__init__)
    params = list(sig.parameters.keys())



def test_cal_astannotationargument_is_not_abstract():
    assert not inspect.isabstract(cal_AstAnnotationArgument)


def test_cal_astannotationargument_constructor_exists():
    assert callable(cal_AstAnnotationArgument.__init__)


def test_cal_astannotationargument_constructor_args():
    sig = inspect.signature(cal_AstAnnotationArgument.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "name" in params, "Missing parameter 'name'"

def test_cal_astannotationargument_has_value():
    assert hasattr(cal_AstAnnotationArgument, "value")
    descriptor = None
    for klass in cal_AstAnnotationArgument.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cal_astannotationargument_has_name():
    assert hasattr(cal_AstAnnotationArgument, "name")
    descriptor = None
    for klass in cal_AstAnnotationArgument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_asttypeparameterlist_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeParameterList)


def test_cal_asttypeparameterlist_constructor_exists():
    assert callable(cal_AstTypeParameterList.__init__)


def test_cal_asttypeparameterlist_constructor_args():
    sig = inspect.signature(cal_AstTypeParameterList.__init__)
    params = list(sig.parameters.keys())



def test_astexpressionliteral_is_not_abstract():
    assert not inspect.isabstract(AstExpressionLiteral)


def test_astexpressionliteral_constructor_exists():
    assert callable(AstExpressionLiteral.__init__)


def test_astexpressionliteral_constructor_args():
    sig = inspect.signature(AstExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressioninteger_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionInteger)


def test_cal_astexpressioninteger_constructor_exists():
    assert callable(cal_AstExpressionInteger.__init__)


def test_cal_astexpressioninteger_constructor_args():
    sig = inspect.signature(cal_AstExpressionInteger.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_astexpressioninteger_has_value():
    assert hasattr(cal_AstExpressionInteger, "value")
    descriptor = None
    for klass in cal_AstExpressionInteger.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpressionfloat_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionFloat)


def test_cal_astexpressionfloat_constructor_exists():
    assert callable(cal_AstExpressionFloat.__init__)


def test_cal_astexpressionfloat_constructor_args():
    sig = inspect.signature(cal_AstExpressionFloat.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_astexpressionfloat_has_value():
    assert hasattr(cal_AstExpressionFloat, "value")
    descriptor = None
    for klass in cal_AstExpressionFloat.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpressionstring_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionString)


def test_cal_astexpressionstring_constructor_exists():
    assert callable(cal_AstExpressionString.__init__)


def test_cal_astexpressionstring_constructor_args():
    sig = inspect.signature(cal_AstExpressionString.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_astexpressionstring_has_value():
    assert hasattr(cal_AstExpressionString, "value")
    descriptor = None
    for klass in cal_AstExpressionString.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpressionboolean_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionBoolean)


def test_cal_astexpressionboolean_constructor_exists():
    assert callable(cal_AstExpressionBoolean.__init__)


def test_cal_astexpressionboolean_constructor_args():
    sig = inspect.signature(cal_AstExpressionBoolean.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_cal_astexpressionboolean_has_value():
    assert hasattr(cal_AstExpressionBoolean, "value")
    descriptor = None
    for klass in cal_AstExpressionBoolean.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_cal_asttypeparam_is_not_abstract():
    assert not inspect.isabstract(cal_AstTypeParam)


def test_cal_asttypeparam_constructor_exists():
    assert callable(cal_AstTypeParam.__init__)


def test_cal_asttypeparam_constructor_args():
    sig = inspect.signature(cal_AstTypeParam.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_cal_asttypeparam_has_name():
    assert hasattr(cal_AstTypeParam, "name")
    descriptor = None
    for klass in cal_AstTypeParam.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cal_astgenerator_is_not_abstract():
    assert not inspect.isabstract(cal_AstGenerator)


def test_cal_astgenerator_constructor_exists():
    assert callable(cal_AstGenerator.__init__)


def test_cal_astgenerator_constructor_args():
    sig = inspect.signature(cal_AstGenerator.__init__)
    params = list(sig.parameters.keys())



def test_astexpression_is_not_abstract():
    assert not inspect.isabstract(AstExpression)


def test_astexpression_constructor_exists():
    assert callable(AstExpression.__init__)


def test_astexpression_constructor_args():
    sig = inspect.signature(AstExpression.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressionif_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionIf)


def test_cal_astexpressionif_constructor_exists():
    assert callable(cal_AstExpressionIf.__init__)


def test_cal_astexpressionif_constructor_args():
    sig = inspect.signature(cal_AstExpressionIf.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressionunary_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionUnary)


def test_cal_astexpressionunary_constructor_exists():
    assert callable(cal_AstExpressionUnary.__init__)


def test_cal_astexpressionunary_constructor_args():
    sig = inspect.signature(cal_AstExpressionUnary.__init__)
    params = list(sig.parameters.keys())
    assert "unaryOperator" in params, "Missing parameter 'unaryOperator'"

def test_cal_astexpressionunary_has_unaryOperator():
    assert hasattr(cal_AstExpressionUnary, "unaryOperator")
    descriptor = None
    for klass in cal_AstExpressionUnary.__mro__:
        if "unaryOperator" in klass.__dict__:
            descriptor = klass.__dict__["unaryOperator"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpressionbinary_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionBinary)


def test_cal_astexpressionbinary_constructor_exists():
    assert callable(cal_AstExpressionBinary.__init__)


def test_cal_astexpressionbinary_constructor_args():
    sig = inspect.signature(cal_AstExpressionBinary.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"

def test_cal_astexpressionbinary_has_operator():
    assert hasattr(cal_AstExpressionBinary, "operator")
    descriptor = None
    for klass in cal_AstExpressionBinary.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_cal_astexpressionlist_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionList)


def test_cal_astexpressionlist_constructor_exists():
    assert callable(cal_AstExpressionList.__init__)


def test_cal_astexpressionlist_constructor_args():
    sig = inspect.signature(cal_AstExpressionList.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressioncall_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionCall)


def test_cal_astexpressioncall_constructor_exists():
    assert callable(cal_AstExpressionCall.__init__)


def test_cal_astexpressioncall_constructor_args():
    sig = inspect.signature(cal_AstExpressionCall.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressionliteral_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionLiteral)


def test_cal_astexpressionliteral_constructor_exists():
    assert callable(cal_AstExpressionLiteral.__init__)


def test_cal_astexpressionliteral_constructor_args():
    sig = inspect.signature(cal_AstExpressionLiteral.__init__)
    params = list(sig.parameters.keys())



def test_cal_astexpressionvariable_is_not_abstract():
    assert not inspect.isabstract(cal_AstExpressionVariable)


def test_cal_astexpressionvariable_constructor_exists():
    assert callable(cal_AstExpressionVariable.__init__)


def test_cal_astexpressionvariable_constructor_args():
    sig = inspect.signature(cal_AstExpressionVariable.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementblock_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementBlock)


def test_cal_aststatementblock_constructor_exists():
    assert callable(cal_AstStatementBlock.__init__)


def test_cal_aststatementblock_constructor_args():
    sig = inspect.signature(cal_AstStatementBlock.__init__)
    params = list(sig.parameters.keys())



def test_cal_astforeachgenerator_is_not_abstract():
    assert not inspect.isabstract(cal_AstForeachGenerator)


def test_cal_astforeachgenerator_constructor_exists():
    assert callable(cal_AstForeachGenerator.__init__)


def test_cal_astforeachgenerator_constructor_args():
    sig = inspect.signature(cal_AstForeachGenerator.__init__)
    params = list(sig.parameters.keys())



def test_cal_aststatementforeach_is_not_abstract():
    assert not inspect.isabstract(cal_AstStatementForeach)


def test_cal_aststatementforeach_constructor_exists():
    assert callable(cal_AstStatementForeach.__init__)


def test_cal_aststatementforeach_constructor_args():
    sig = inspect.signature(cal_AstStatementForeach.__init__)
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
cal_AstOutputPattern_strategy = st.builds(
    cal_AstOutputPattern,
)
cal_AstMemberAccess_strategy = st.builds(
    cal_AstMemberAccess,
    name=
        safe_text
)
cal_AstVariableReference_strategy = st.builds(
    cal_AstVariableReference,
)
AstStatement_strategy = st.builds(
    AstStatement,
)
cal_AstStatementWhile_strategy = st.builds(
    cal_AstStatementWhile,
)
cal_AstStatementIf_strategy = st.builds(
    cal_AstStatementIf,
)
cal_AstStatementCall_strategy = st.builds(
    cal_AstStatementCall,
)
cal_AstStatementAssign_strategy = st.builds(
    cal_AstStatementAssign,
)
cal_AstInequality_strategy = st.builds(
    cal_AstInequality,
)
cal_AstTag_strategy = st.builds(
    cal_AstTag,
    identifiers=
        safe_text
)
cal_AstExternalProcedure_strategy = st.builds(
    cal_AstExternalProcedure,
)
cal_AstStatement_strategy = st.builds(
    cal_AstStatement,
)
AstExternalProcedure_strategy = st.builds(
    AstExternalProcedure,
)
cal_AstInputPattern_strategy = st.builds(
    cal_AstInputPattern,
)
cal_AstTransition_strategy = st.builds(
    cal_AstTransition,
)
cal_AstState_strategy = st.builds(
    cal_AstState,
    name=
        safe_text
)
cal_AstProcedure_strategy = st.builds(
    cal_AstProcedure,
    name=
        safe_text
)
AstExternalFunction_strategy = st.builds(
    AstExternalFunction,
)
cal_AstExternalFunction_strategy = st.builds(
    cal_AstExternalFunction,
)
cal_AstPriority_strategy = st.builds(
    cal_AstPriority,
)
cal_AstSchedule_strategy = st.builds(
    cal_AstSchedule,
)
cal_AstAction_strategy = st.builds(
    cal_AstAction,
)
cal_AstConnectionAttribute_strategy = st.builds(
    cal_AstConnectionAttribute,
    name=
        safe_text
)
cal_AstActorVariableReference_strategy = st.builds(
    cal_AstActorVariableReference,
)
cal_AstTypeDefinitionParameter_strategy = st.builds(
    cal_AstTypeDefinitionParameter,
)
cal_AstType_strategy = st.builds(
    cal_AstType,
    builtin=
        safe_text
)
cal_AstStructure_strategy = st.builds(
    cal_AstStructure,
)
cal_AstActorVariable_strategy = st.builds(
    cal_AstActorVariable,
    name=
        safe_text
)
AstAbstractActor_strategy = st.builds(
    AstAbstractActor,
)
cal_AstActor_strategy = st.builds(
    cal_AstActor,
)
cal_AstExternalActor_strategy = st.builds(
    cal_AstExternalActor,
)
cal_AstNetwork_strategy = st.builds(
    cal_AstNetwork,
)
cal_AstConnection_strategy = st.builds(
    cal_AstConnection,
    outPort=
        safe_text,
    inPort=
        safe_text
)
cal_AstExpression_strategy = st.builds(
    cal_AstExpression,
)
cal_AstAssignParameter_strategy = st.builds(
    cal_AstAssignParameter,
    name=
        safe_text
)
cal_AstTypeName_strategy = st.builds(
    cal_AstTypeName,
    name=
        safe_text
)
cal_AstAnnotation_strategy = st.builds(
    cal_AstAnnotation,
    name=
        safe_text
)
cal_EObject_strategy = st.builds(
    cal_EObject,
)
cal_AstVariable_strategy = st.builds(
    cal_AstVariable,
    name=
        safe_text,
    constant=
        st.booleans()
)
cal_AstFunction_strategy = st.builds(
    cal_AstFunction,
    name=
        safe_text
)
cal_Import_strategy = st.builds(
    cal_Import,
    importedNamespace=
        safe_text
)
cal_AstEntity_strategy = st.builds(
    cal_AstEntity,
)
cal_AstPort_strategy = st.builds(
    cal_AstPort,
    name=
        safe_text
)
cal_AstAbstractActor_strategy = st.builds(
    cal_AstAbstractActor,
    name=
        safe_text
)
AstUnit_strategy = st.builds(
    AstUnit,
)
AstPackage_strategy = st.builds(
    AstPackage,
)
cal_AstUnit_strategy = st.builds(
    cal_AstUnit,
)
AstTop_strategy = st.builds(
    AstTop,
)
cal_AstNamespace_strategy = st.builds(
    cal_AstNamespace,
    name=
        safe_text
)
cal_AstPackage_strategy = st.builds(
    cal_AstPackage,
)
cal_AstTop_strategy = st.builds(
    cal_AstTop,
)
AstAction_strategy = st.builds(
    AstAction,
)
cal_AstInitialize_strategy = st.builds(
    cal_AstInitialize,
)
cal_AstAnnotationArgument_strategy = st.builds(
    cal_AstAnnotationArgument,
    value=
        safe_text,
    name=
        safe_text
)
cal_AstTypeParameterList_strategy = st.builds(
    cal_AstTypeParameterList,
)
AstExpressionLiteral_strategy = st.builds(
    AstExpressionLiteral,
)
cal_AstExpressionInteger_strategy = st.builds(
    cal_AstExpressionInteger,
    value=
        safe_text
)
cal_AstExpressionFloat_strategy = st.builds(
    cal_AstExpressionFloat,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
cal_AstExpressionString_strategy = st.builds(
    cal_AstExpressionString,
    value=
        safe_text
)
cal_AstExpressionBoolean_strategy = st.builds(
    cal_AstExpressionBoolean,
    value=
        st.booleans()
)
cal_AstTypeParam_strategy = st.builds(
    cal_AstTypeParam,
    name=
        safe_text
)
cal_AstGenerator_strategy = st.builds(
    cal_AstGenerator,
)
AstExpression_strategy = st.builds(
    AstExpression,
)
cal_AstExpressionIf_strategy = st.builds(
    cal_AstExpressionIf,
)
cal_AstExpressionUnary_strategy = st.builds(
    cal_AstExpressionUnary,
    unaryOperator=
        safe_text
)
cal_AstExpressionBinary_strategy = st.builds(
    cal_AstExpressionBinary,
    operator=
        safe_text
)
cal_AstExpressionList_strategy = st.builds(
    cal_AstExpressionList,
)
cal_AstExpressionCall_strategy = st.builds(
    cal_AstExpressionCall,
)
cal_AstExpressionLiteral_strategy = st.builds(
    cal_AstExpressionLiteral,
)
cal_AstExpressionVariable_strategy = st.builds(
    cal_AstExpressionVariable,
)
cal_AstStatementBlock_strategy = st.builds(
    cal_AstStatementBlock,
)
cal_AstForeachGenerator_strategy = st.builds(
    cal_AstForeachGenerator,
)
cal_AstStatementForeach_strategy = st.builds(
    cal_AstStatementForeach,
)

@given(instance=cal_AstOutputPattern_strategy)
@settings(max_examples=50)
def test_cal_astoutputpattern_instantiation(instance):
    assert isinstance(instance, cal_AstOutputPattern)

@given(instance=cal_AstMemberAccess_strategy)
@settings(max_examples=50)
def test_cal_astmemberaccess_instantiation(instance):
    assert isinstance(instance, cal_AstMemberAccess)



@given(instance=cal_AstMemberAccess_strategy)
def test_cal_astmemberaccess_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstVariableReference_strategy)
@settings(max_examples=50)
def test_cal_astvariablereference_instantiation(instance):
    assert isinstance(instance, cal_AstVariableReference)

@given(instance=AstStatement_strategy)
@settings(max_examples=50)
def test_aststatement_instantiation(instance):
    assert isinstance(instance, AstStatement)

@given(instance=cal_AstStatementWhile_strategy)
@settings(max_examples=50)
def test_cal_aststatementwhile_instantiation(instance):
    assert isinstance(instance, cal_AstStatementWhile)

@given(instance=cal_AstStatementIf_strategy)
@settings(max_examples=50)
def test_cal_aststatementif_instantiation(instance):
    assert isinstance(instance, cal_AstStatementIf)

@given(instance=cal_AstStatementCall_strategy)
@settings(max_examples=50)
def test_cal_aststatementcall_instantiation(instance):
    assert isinstance(instance, cal_AstStatementCall)

@given(instance=cal_AstStatementAssign_strategy)
@settings(max_examples=50)
def test_cal_aststatementassign_instantiation(instance):
    assert isinstance(instance, cal_AstStatementAssign)

@given(instance=cal_AstInequality_strategy)
@settings(max_examples=50)
def test_cal_astinequality_instantiation(instance):
    assert isinstance(instance, cal_AstInequality)

@given(instance=cal_AstTag_strategy)
@settings(max_examples=50)
def test_cal_asttag_instantiation(instance):
    assert isinstance(instance, cal_AstTag)



@given(instance=cal_AstTag_strategy)
def test_cal_asttag_identifiers_setter(instance):
    original = instance.identifiers
    instance.identifiers = original
    assert instance.identifiers == original

@given(instance=cal_AstExternalProcedure_strategy)
@settings(max_examples=50)
def test_cal_astexternalprocedure_instantiation(instance):
    assert isinstance(instance, cal_AstExternalProcedure)

@given(instance=cal_AstStatement_strategy)
@settings(max_examples=50)
def test_cal_aststatement_instantiation(instance):
    assert isinstance(instance, cal_AstStatement)

@given(instance=AstExternalProcedure_strategy)
@settings(max_examples=50)
def test_astexternalprocedure_instantiation(instance):
    assert isinstance(instance, AstExternalProcedure)

@given(instance=cal_AstInputPattern_strategy)
@settings(max_examples=50)
def test_cal_astinputpattern_instantiation(instance):
    assert isinstance(instance, cal_AstInputPattern)

@given(instance=cal_AstTransition_strategy)
@settings(max_examples=50)
def test_cal_asttransition_instantiation(instance):
    assert isinstance(instance, cal_AstTransition)

@given(instance=cal_AstState_strategy)
@settings(max_examples=50)
def test_cal_aststate_instantiation(instance):
    assert isinstance(instance, cal_AstState)



@given(instance=cal_AstState_strategy)
def test_cal_aststate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstProcedure_strategy)
@settings(max_examples=50)
def test_cal_astprocedure_instantiation(instance):
    assert isinstance(instance, cal_AstProcedure)



@given(instance=cal_AstProcedure_strategy)
def test_cal_astprocedure_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstExternalFunction_strategy)
@settings(max_examples=50)
def test_astexternalfunction_instantiation(instance):
    assert isinstance(instance, AstExternalFunction)

@given(instance=cal_AstExternalFunction_strategy)
@settings(max_examples=50)
def test_cal_astexternalfunction_instantiation(instance):
    assert isinstance(instance, cal_AstExternalFunction)

@given(instance=cal_AstPriority_strategy)
@settings(max_examples=50)
def test_cal_astpriority_instantiation(instance):
    assert isinstance(instance, cal_AstPriority)

@given(instance=cal_AstSchedule_strategy)
@settings(max_examples=50)
def test_cal_astschedule_instantiation(instance):
    assert isinstance(instance, cal_AstSchedule)

@given(instance=cal_AstAction_strategy)
@settings(max_examples=50)
def test_cal_astaction_instantiation(instance):
    assert isinstance(instance, cal_AstAction)

@given(instance=cal_AstConnectionAttribute_strategy)
@settings(max_examples=50)
def test_cal_astconnectionattribute_instantiation(instance):
    assert isinstance(instance, cal_AstConnectionAttribute)



@given(instance=cal_AstConnectionAttribute_strategy)
def test_cal_astconnectionattribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstActorVariableReference_strategy)
@settings(max_examples=50)
def test_cal_astactorvariablereference_instantiation(instance):
    assert isinstance(instance, cal_AstActorVariableReference)

@given(instance=cal_AstTypeDefinitionParameter_strategy)
@settings(max_examples=50)
def test_cal_asttypedefinitionparameter_instantiation(instance):
    assert isinstance(instance, cal_AstTypeDefinitionParameter)

@given(instance=cal_AstType_strategy)
@settings(max_examples=50)
def test_cal_asttype_instantiation(instance):
    assert isinstance(instance, cal_AstType)



@given(instance=cal_AstType_strategy)
def test_cal_asttype_builtin_setter(instance):
    original = instance.builtin
    instance.builtin = original
    assert instance.builtin == original

@given(instance=cal_AstStructure_strategy)
@settings(max_examples=50)
def test_cal_aststructure_instantiation(instance):
    assert isinstance(instance, cal_AstStructure)

@given(instance=cal_AstActorVariable_strategy)
@settings(max_examples=50)
def test_cal_astactorvariable_instantiation(instance):
    assert isinstance(instance, cal_AstActorVariable)



@given(instance=cal_AstActorVariable_strategy)
def test_cal_astactorvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=AstAbstractActor_strategy)
@settings(max_examples=50)
def test_astabstractactor_instantiation(instance):
    assert isinstance(instance, AstAbstractActor)

@given(instance=cal_AstActor_strategy)
@settings(max_examples=50)
def test_cal_astactor_instantiation(instance):
    assert isinstance(instance, cal_AstActor)

@given(instance=cal_AstExternalActor_strategy)
@settings(max_examples=50)
def test_cal_astexternalactor_instantiation(instance):
    assert isinstance(instance, cal_AstExternalActor)

@given(instance=cal_AstNetwork_strategy)
@settings(max_examples=50)
def test_cal_astnetwork_instantiation(instance):
    assert isinstance(instance, cal_AstNetwork)

@given(instance=cal_AstConnection_strategy)
@settings(max_examples=50)
def test_cal_astconnection_instantiation(instance):
    assert isinstance(instance, cal_AstConnection)



@given(instance=cal_AstConnection_strategy)
def test_cal_astconnection_outPort_setter(instance):
    original = instance.outPort
    instance.outPort = original
    assert instance.outPort == original



@given(instance=cal_AstConnection_strategy)
def test_cal_astconnection_inPort_setter(instance):
    original = instance.inPort
    instance.inPort = original
    assert instance.inPort == original

@given(instance=cal_AstExpression_strategy)
@settings(max_examples=50)
def test_cal_astexpression_instantiation(instance):
    assert isinstance(instance, cal_AstExpression)

@given(instance=cal_AstAssignParameter_strategy)
@settings(max_examples=50)
def test_cal_astassignparameter_instantiation(instance):
    assert isinstance(instance, cal_AstAssignParameter)



@given(instance=cal_AstAssignParameter_strategy)
def test_cal_astassignparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstTypeName_strategy)
@settings(max_examples=50)
def test_cal_asttypename_instantiation(instance):
    assert isinstance(instance, cal_AstTypeName)



@given(instance=cal_AstTypeName_strategy)
def test_cal_asttypename_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstAnnotation_strategy)
@settings(max_examples=50)
def test_cal_astannotation_instantiation(instance):
    assert isinstance(instance, cal_AstAnnotation)



@given(instance=cal_AstAnnotation_strategy)
def test_cal_astannotation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_EObject_strategy)
@settings(max_examples=50)
def test_cal_eobject_instantiation(instance):
    assert isinstance(instance, cal_EObject)

@given(instance=cal_AstVariable_strategy)
@settings(max_examples=50)
def test_cal_astvariable_instantiation(instance):
    assert isinstance(instance, cal_AstVariable)



@given(instance=cal_AstVariable_strategy)
def test_cal_astvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=cal_AstVariable_strategy)
def test_cal_astvariable_constant_setter(instance):
    original = instance.constant
    instance.constant = original
    assert instance.constant == original

@given(instance=cal_AstFunction_strategy)
@settings(max_examples=50)
def test_cal_astfunction_instantiation(instance):
    assert isinstance(instance, cal_AstFunction)



@given(instance=cal_AstFunction_strategy)
def test_cal_astfunction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_Import_strategy)
@settings(max_examples=50)
def test_cal_import_instantiation(instance):
    assert isinstance(instance, cal_Import)



@given(instance=cal_Import_strategy)
def test_cal_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=cal_AstEntity_strategy)
@settings(max_examples=50)
def test_cal_astentity_instantiation(instance):
    assert isinstance(instance, cal_AstEntity)

@given(instance=cal_AstPort_strategy)
@settings(max_examples=50)
def test_cal_astport_instantiation(instance):
    assert isinstance(instance, cal_AstPort)



@given(instance=cal_AstPort_strategy)
def test_cal_astport_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstAbstractActor_strategy)
@settings(max_examples=50)
def test_cal_astabstractactor_instantiation(instance):
    assert isinstance(instance, cal_AstAbstractActor)



@given(instance=cal_AstAbstractActor_strategy)
def test_cal_astabstractactor_name_setter(instance):
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

@given(instance=cal_AstUnit_strategy)
@settings(max_examples=50)
def test_cal_astunit_instantiation(instance):
    assert isinstance(instance, cal_AstUnit)

@given(instance=AstTop_strategy)
@settings(max_examples=50)
def test_asttop_instantiation(instance):
    assert isinstance(instance, AstTop)

@given(instance=cal_AstNamespace_strategy)
@settings(max_examples=50)
def test_cal_astnamespace_instantiation(instance):
    assert isinstance(instance, cal_AstNamespace)



@given(instance=cal_AstNamespace_strategy)
def test_cal_astnamespace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstPackage_strategy)
@settings(max_examples=50)
def test_cal_astpackage_instantiation(instance):
    assert isinstance(instance, cal_AstPackage)

@given(instance=cal_AstTop_strategy)
@settings(max_examples=50)
def test_cal_asttop_instantiation(instance):
    assert isinstance(instance, cal_AstTop)

@given(instance=AstAction_strategy)
@settings(max_examples=50)
def test_astaction_instantiation(instance):
    assert isinstance(instance, AstAction)

@given(instance=cal_AstInitialize_strategy)
@settings(max_examples=50)
def test_cal_astinitialize_instantiation(instance):
    assert isinstance(instance, cal_AstInitialize)

@given(instance=cal_AstAnnotationArgument_strategy)
@settings(max_examples=50)
def test_cal_astannotationargument_instantiation(instance):
    assert isinstance(instance, cal_AstAnnotationArgument)



@given(instance=cal_AstAnnotationArgument_strategy)
def test_cal_astannotationargument_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=cal_AstAnnotationArgument_strategy)
def test_cal_astannotationargument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstTypeParameterList_strategy)
@settings(max_examples=50)
def test_cal_asttypeparameterlist_instantiation(instance):
    assert isinstance(instance, cal_AstTypeParameterList)

@given(instance=AstExpressionLiteral_strategy)
@settings(max_examples=50)
def test_astexpressionliteral_instantiation(instance):
    assert isinstance(instance, AstExpressionLiteral)

@given(instance=cal_AstExpressionInteger_strategy)
@settings(max_examples=50)
def test_cal_astexpressioninteger_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionInteger)



@given(instance=cal_AstExpressionInteger_strategy)
def test_cal_astexpressioninteger_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_AstExpressionFloat_strategy)
@settings(max_examples=50)
def test_cal_astexpressionfloat_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionFloat)



@given(instance=cal_AstExpressionFloat_strategy)
def test_cal_astexpressionfloat_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_AstExpressionString_strategy)
@settings(max_examples=50)
def test_cal_astexpressionstring_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionString)



@given(instance=cal_AstExpressionString_strategy)
def test_cal_astexpressionstring_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_AstExpressionBoolean_strategy)
@settings(max_examples=50)
def test_cal_astexpressionboolean_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionBoolean)



@given(instance=cal_AstExpressionBoolean_strategy)
def test_cal_astexpressionboolean_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=cal_AstTypeParam_strategy)
@settings(max_examples=50)
def test_cal_asttypeparam_instantiation(instance):
    assert isinstance(instance, cal_AstTypeParam)



@given(instance=cal_AstTypeParam_strategy)
def test_cal_asttypeparam_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=cal_AstGenerator_strategy)
@settings(max_examples=50)
def test_cal_astgenerator_instantiation(instance):
    assert isinstance(instance, cal_AstGenerator)

@given(instance=AstExpression_strategy)
@settings(max_examples=50)
def test_astexpression_instantiation(instance):
    assert isinstance(instance, AstExpression)

@given(instance=cal_AstExpressionIf_strategy)
@settings(max_examples=50)
def test_cal_astexpressionif_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionIf)

@given(instance=cal_AstExpressionUnary_strategy)
@settings(max_examples=50)
def test_cal_astexpressionunary_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionUnary)



@given(instance=cal_AstExpressionUnary_strategy)
def test_cal_astexpressionunary_unaryOperator_setter(instance):
    original = instance.unaryOperator
    instance.unaryOperator = original
    assert instance.unaryOperator == original

@given(instance=cal_AstExpressionBinary_strategy)
@settings(max_examples=50)
def test_cal_astexpressionbinary_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionBinary)



@given(instance=cal_AstExpressionBinary_strategy)
def test_cal_astexpressionbinary_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=cal_AstExpressionList_strategy)
@settings(max_examples=50)
def test_cal_astexpressionlist_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionList)

@given(instance=cal_AstExpressionCall_strategy)
@settings(max_examples=50)
def test_cal_astexpressioncall_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionCall)

@given(instance=cal_AstExpressionLiteral_strategy)
@settings(max_examples=50)
def test_cal_astexpressionliteral_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionLiteral)

@given(instance=cal_AstExpressionVariable_strategy)
@settings(max_examples=50)
def test_cal_astexpressionvariable_instantiation(instance):
    assert isinstance(instance, cal_AstExpressionVariable)

@given(instance=cal_AstStatementBlock_strategy)
@settings(max_examples=50)
def test_cal_aststatementblock_instantiation(instance):
    assert isinstance(instance, cal_AstStatementBlock)

@given(instance=cal_AstForeachGenerator_strategy)
@settings(max_examples=50)
def test_cal_astforeachgenerator_instantiation(instance):
    assert isinstance(instance, cal_AstForeachGenerator)

@given(instance=cal_AstStatementForeach_strategy)
@settings(max_examples=50)
def test_cal_aststatementforeach_instantiation(instance):
    assert isinstance(instance, cal_AstStatementForeach)
