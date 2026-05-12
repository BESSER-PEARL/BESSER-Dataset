import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    executionTrace_StoryPatternObjectConstraintEvaluation,
    executionTrace_VariableChanged,
    executionTrace_VariableDeleted,
    executionTrace_VariableCreated,
    executionTrace_StoryPatternConstraintViolated,
    executionTrace_StoryPatternConstraintHolds,
    executionTrace_StoryPatternConstraintEvaluation,
    executionTrace_StoryPatternObjectConstraintViolated,
    executionTrace_StoryPatternObjectConstraintHolds,
    executionTrace_LinkCheckFailed,
    executionTrace_LinkCheckSuccessful,
    executionTrace_LinkCheck,
    executionTrace_TraversingLink,
    executionTrace_InstanceLinkDeletion,
    executionTrace_InstanceLinkCreation,
    executionTrace_InstanceObjectDeletion,
    executionTrace_InstanceObjectCreation,
    executionTrace_StoryPatternApplication,
    executionTrace_StoryPatternMatching,
    executionTrace_StoryPatternInitialization,
    Execution,
    executionTrace_StoryPatternObjectExecution,
    executionTrace_ActivityNodeExecution,
    executionTrace_ExpressionEvaluation,
    executionTrace_StoryPatternExecution,
    executionTrace_AttributeValueSet,
    executionTrace_InstanceObjectModification,
    executionTrace_ActivityEdgeTraversal,
    executionTrace_VariableModification,
    executionTrace_InstanceLinkModification,
    executionTrace_ActivityExecution,
    executionTrace_StoryPatternLinkExecution,
    executionTrace_StoryPatternObjectBindingRevoked,
    executionTrace_StoryPatternObjectNotBound,
    executionTrace_StoryPatternObjectBound,
    executionTrace_Execution,
    executionTrace_ExecutionTrace,
    executionTrace_MapEntry,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_executiontrace_storypatternobjectconstraintevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectConstraintEvaluation)


def test_executiontrace_storypatternobjectconstraintevaluation_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectConstraintEvaluation.__init__)


def test_executiontrace_storypatternobjectconstraintevaluation_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectConstraintEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_variablechanged_is_not_abstract():
    assert not inspect.isabstract(executionTrace_VariableChanged)


def test_executiontrace_variablechanged_constructor_exists():
    assert callable(executionTrace_VariableChanged.__init__)


def test_executiontrace_variablechanged_constructor_args():
    sig = inspect.signature(executionTrace_VariableChanged.__init__)
    params = list(sig.parameters.keys())
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_executiontrace_variablechanged_has_oldValue():
    assert hasattr(executionTrace_VariableChanged, "oldValue")
    descriptor = None
    for klass in executionTrace_VariableChanged.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_variabledeleted_is_not_abstract():
    assert not inspect.isabstract(executionTrace_VariableDeleted)


def test_executiontrace_variabledeleted_constructor_exists():
    assert callable(executionTrace_VariableDeleted.__init__)


def test_executiontrace_variabledeleted_constructor_args():
    sig = inspect.signature(executionTrace_VariableDeleted.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_variablecreated_is_not_abstract():
    assert not inspect.isabstract(executionTrace_VariableCreated)


def test_executiontrace_variablecreated_constructor_exists():
    assert callable(executionTrace_VariableCreated.__init__)


def test_executiontrace_variablecreated_constructor_args():
    sig = inspect.signature(executionTrace_VariableCreated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternconstraintviolated_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternConstraintViolated)


def test_executiontrace_storypatternconstraintviolated_constructor_exists():
    assert callable(executionTrace_StoryPatternConstraintViolated.__init__)


def test_executiontrace_storypatternconstraintviolated_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternConstraintViolated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternconstraintholds_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternConstraintHolds)


def test_executiontrace_storypatternconstraintholds_constructor_exists():
    assert callable(executionTrace_StoryPatternConstraintHolds.__init__)


def test_executiontrace_storypatternconstraintholds_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternConstraintHolds.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternconstraintevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternConstraintEvaluation)


def test_executiontrace_storypatternconstraintevaluation_constructor_exists():
    assert callable(executionTrace_StoryPatternConstraintEvaluation.__init__)


def test_executiontrace_storypatternconstraintevaluation_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternConstraintEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternobjectconstraintviolated_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectConstraintViolated)


def test_executiontrace_storypatternobjectconstraintviolated_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectConstraintViolated.__init__)


def test_executiontrace_storypatternobjectconstraintviolated_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectConstraintViolated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternobjectconstraintholds_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectConstraintHolds)


def test_executiontrace_storypatternobjectconstraintholds_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectConstraintHolds.__init__)


def test_executiontrace_storypatternobjectconstraintholds_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectConstraintHolds.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_linkcheckfailed_is_not_abstract():
    assert not inspect.isabstract(executionTrace_LinkCheckFailed)


def test_executiontrace_linkcheckfailed_constructor_exists():
    assert callable(executionTrace_LinkCheckFailed.__init__)


def test_executiontrace_linkcheckfailed_constructor_args():
    sig = inspect.signature(executionTrace_LinkCheckFailed.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_linkchecksuccessful_is_not_abstract():
    assert not inspect.isabstract(executionTrace_LinkCheckSuccessful)


def test_executiontrace_linkchecksuccessful_constructor_exists():
    assert callable(executionTrace_LinkCheckSuccessful.__init__)


def test_executiontrace_linkchecksuccessful_constructor_args():
    sig = inspect.signature(executionTrace_LinkCheckSuccessful.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_linkcheck_is_not_abstract():
    assert not inspect.isabstract(executionTrace_LinkCheck)


def test_executiontrace_linkcheck_constructor_exists():
    assert callable(executionTrace_LinkCheck.__init__)


def test_executiontrace_linkcheck_constructor_args():
    sig = inspect.signature(executionTrace_LinkCheck.__init__)
    params = list(sig.parameters.keys())
    assert "targetObject" in params, "Missing parameter 'targetObject'"

def test_executiontrace_linkcheck_has_targetObject():
    assert hasattr(executionTrace_LinkCheck, "targetObject")
    descriptor = None
    for klass in executionTrace_LinkCheck.__mro__:
        if "targetObject" in klass.__dict__:
            descriptor = klass.__dict__["targetObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_traversinglink_is_not_abstract():
    assert not inspect.isabstract(executionTrace_TraversingLink)


def test_executiontrace_traversinglink_constructor_exists():
    assert callable(executionTrace_TraversingLink.__init__)


def test_executiontrace_traversinglink_constructor_args():
    sig = inspect.signature(executionTrace_TraversingLink.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_instancelinkdeletion_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceLinkDeletion)


def test_executiontrace_instancelinkdeletion_constructor_exists():
    assert callable(executionTrace_InstanceLinkDeletion.__init__)


def test_executiontrace_instancelinkdeletion_constructor_args():
    sig = inspect.signature(executionTrace_InstanceLinkDeletion.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_instancelinkcreation_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceLinkCreation)


def test_executiontrace_instancelinkcreation_constructor_exists():
    assert callable(executionTrace_InstanceLinkCreation.__init__)


def test_executiontrace_instancelinkcreation_constructor_args():
    sig = inspect.signature(executionTrace_InstanceLinkCreation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_instanceobjectdeletion_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceObjectDeletion)


def test_executiontrace_instanceobjectdeletion_constructor_exists():
    assert callable(executionTrace_InstanceObjectDeletion.__init__)


def test_executiontrace_instanceobjectdeletion_constructor_args():
    sig = inspect.signature(executionTrace_InstanceObjectDeletion.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_instanceobjectcreation_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceObjectCreation)


def test_executiontrace_instanceobjectcreation_constructor_exists():
    assert callable(executionTrace_InstanceObjectCreation.__init__)


def test_executiontrace_instanceobjectcreation_constructor_args():
    sig = inspect.signature(executionTrace_InstanceObjectCreation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternapplication_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternApplication)


def test_executiontrace_storypatternapplication_constructor_exists():
    assert callable(executionTrace_StoryPatternApplication.__init__)


def test_executiontrace_storypatternapplication_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternApplication.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternmatching_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternMatching)


def test_executiontrace_storypatternmatching_constructor_exists():
    assert callable(executionTrace_StoryPatternMatching.__init__)


def test_executiontrace_storypatternmatching_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternMatching.__init__)
    params = list(sig.parameters.keys())
    assert "successful" in params, "Missing parameter 'successful'"

def test_executiontrace_storypatternmatching_has_successful():
    assert hasattr(executionTrace_StoryPatternMatching, "successful")
    descriptor = None
    for klass in executionTrace_StoryPatternMatching.__mro__:
        if "successful" in klass.__dict__:
            descriptor = klass.__dict__["successful"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_storypatterninitialization_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternInitialization)


def test_executiontrace_storypatterninitialization_constructor_exists():
    assert callable(executionTrace_StoryPatternInitialization.__init__)


def test_executiontrace_storypatterninitialization_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternInitialization.__init__)
    params = list(sig.parameters.keys())



def test_execution_is_not_abstract():
    assert not inspect.isabstract(Execution)


def test_execution_constructor_exists():
    assert callable(Execution.__init__)


def test_execution_constructor_args():
    sig = inspect.signature(Execution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternobjectexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectExecution)


def test_executiontrace_storypatternobjectexecution_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectExecution.__init__)


def test_executiontrace_storypatternobjectexecution_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_activitynodeexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_ActivityNodeExecution)


def test_executiontrace_activitynodeexecution_constructor_exists():
    assert callable(executionTrace_ActivityNodeExecution.__init__)


def test_executiontrace_activitynodeexecution_constructor_args():
    sig = inspect.signature(executionTrace_ActivityNodeExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_expressionevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace_ExpressionEvaluation)


def test_executiontrace_expressionevaluation_constructor_exists():
    assert callable(executionTrace_ExpressionEvaluation.__init__)


def test_executiontrace_expressionevaluation_constructor_args():
    sig = inspect.signature(executionTrace_ExpressionEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "result" in params, "Missing parameter 'result'"

def test_executiontrace_expressionevaluation_has_result():
    assert hasattr(executionTrace_ExpressionEvaluation, "result")
    descriptor = None
    for klass in executionTrace_ExpressionEvaluation.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_storypatternexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternExecution)


def test_executiontrace_storypatternexecution_constructor_exists():
    assert callable(executionTrace_StoryPatternExecution.__init__)


def test_executiontrace_storypatternexecution_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_attributevalueset_is_not_abstract():
    assert not inspect.isabstract(executionTrace_AttributeValueSet)


def test_executiontrace_attributevalueset_constructor_exists():
    assert callable(executionTrace_AttributeValueSet.__init__)


def test_executiontrace_attributevalueset_constructor_args():
    sig = inspect.signature(executionTrace_AttributeValueSet.__init__)
    params = list(sig.parameters.keys())
    assert "instanceObject" in params, "Missing parameter 'instanceObject'"
    assert "newValue" in params, "Missing parameter 'newValue'"

def test_executiontrace_attributevalueset_has_instanceObject():
    assert hasattr(executionTrace_AttributeValueSet, "instanceObject")
    descriptor = None
    for klass in executionTrace_AttributeValueSet.__mro__:
        if "instanceObject" in klass.__dict__:
            descriptor = klass.__dict__["instanceObject"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_attributevalueset_has_newValue():
    assert hasattr(executionTrace_AttributeValueSet, "newValue")
    descriptor = None
    for klass in executionTrace_AttributeValueSet.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_instanceobjectmodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceObjectModification)


def test_executiontrace_instanceobjectmodification_constructor_exists():
    assert callable(executionTrace_InstanceObjectModification.__init__)


def test_executiontrace_instanceobjectmodification_constructor_args():
    sig = inspect.signature(executionTrace_InstanceObjectModification.__init__)
    params = list(sig.parameters.keys())
    assert "instanceObject" in params, "Missing parameter 'instanceObject'"

def test_executiontrace_instanceobjectmodification_has_instanceObject():
    assert hasattr(executionTrace_InstanceObjectModification, "instanceObject")
    descriptor = None
    for klass in executionTrace_InstanceObjectModification.__mro__:
        if "instanceObject" in klass.__dict__:
            descriptor = klass.__dict__["instanceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_activityedgetraversal_is_not_abstract():
    assert not inspect.isabstract(executionTrace_ActivityEdgeTraversal)


def test_executiontrace_activityedgetraversal_constructor_exists():
    assert callable(executionTrace_ActivityEdgeTraversal.__init__)


def test_executiontrace_activityedgetraversal_constructor_args():
    sig = inspect.signature(executionTrace_ActivityEdgeTraversal.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_variablemodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace_VariableModification)


def test_executiontrace_variablemodification_constructor_exists():
    assert callable(executionTrace_VariableModification.__init__)


def test_executiontrace_variablemodification_constructor_args():
    sig = inspect.signature(executionTrace_VariableModification.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_executiontrace_variablemodification_has_value():
    assert hasattr(executionTrace_VariableModification, "value")
    descriptor = None
    for klass in executionTrace_VariableModification.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_variablemodification_has_variableName():
    assert hasattr(executionTrace_VariableModification, "variableName")
    descriptor = None
    for klass in executionTrace_VariableModification.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_instancelinkmodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace_InstanceLinkModification)


def test_executiontrace_instancelinkmodification_constructor_exists():
    assert callable(executionTrace_InstanceLinkModification.__init__)


def test_executiontrace_instancelinkmodification_constructor_args():
    sig = inspect.signature(executionTrace_InstanceLinkModification.__init__)
    params = list(sig.parameters.keys())
    assert "targetInstanceObject" in params, "Missing parameter 'targetInstanceObject'"
    assert "sourceInstanceObject" in params, "Missing parameter 'sourceInstanceObject'"

def test_executiontrace_instancelinkmodification_has_targetInstanceObject():
    assert hasattr(executionTrace_InstanceLinkModification, "targetInstanceObject")
    descriptor = None
    for klass in executionTrace_InstanceLinkModification.__mro__:
        if "targetInstanceObject" in klass.__dict__:
            descriptor = klass.__dict__["targetInstanceObject"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_instancelinkmodification_has_sourceInstanceObject():
    assert hasattr(executionTrace_InstanceLinkModification, "sourceInstanceObject")
    descriptor = None
    for klass in executionTrace_InstanceLinkModification.__mro__:
        if "sourceInstanceObject" in klass.__dict__:
            descriptor = klass.__dict__["sourceInstanceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_activityexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_ActivityExecution)


def test_executiontrace_activityexecution_constructor_exists():
    assert callable(executionTrace_ActivityExecution.__init__)


def test_executiontrace_activityexecution_constructor_args():
    sig = inspect.signature(executionTrace_ActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternlinkexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternLinkExecution)


def test_executiontrace_storypatternlinkexecution_constructor_exists():
    assert callable(executionTrace_StoryPatternLinkExecution.__init__)


def test_executiontrace_storypatternlinkexecution_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternLinkExecution.__init__)
    params = list(sig.parameters.keys())
    assert "sourceObject" in params, "Missing parameter 'sourceObject'"

def test_executiontrace_storypatternlinkexecution_has_sourceObject():
    assert hasattr(executionTrace_StoryPatternLinkExecution, "sourceObject")
    descriptor = None
    for klass in executionTrace_StoryPatternLinkExecution.__mro__:
        if "sourceObject" in klass.__dict__:
            descriptor = klass.__dict__["sourceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_storypatternobjectbindingrevoked_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectBindingRevoked)


def test_executiontrace_storypatternobjectbindingrevoked_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectBindingRevoked.__init__)


def test_executiontrace_storypatternobjectbindingrevoked_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectBindingRevoked.__init__)
    params = list(sig.parameters.keys())
    assert "previousValue" in params, "Missing parameter 'previousValue'"

def test_executiontrace_storypatternobjectbindingrevoked_has_previousValue():
    assert hasattr(executionTrace_StoryPatternObjectBindingRevoked, "previousValue")
    descriptor = None
    for klass in executionTrace_StoryPatternObjectBindingRevoked.__mro__:
        if "previousValue" in klass.__dict__:
            descriptor = klass.__dict__["previousValue"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_storypatternobjectnotbound_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectNotBound)


def test_executiontrace_storypatternobjectnotbound_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectNotBound.__init__)


def test_executiontrace_storypatternobjectnotbound_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectNotBound.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace_storypatternobjectbound_is_not_abstract():
    assert not inspect.isabstract(executionTrace_StoryPatternObjectBound)


def test_executiontrace_storypatternobjectbound_constructor_exists():
    assert callable(executionTrace_StoryPatternObjectBound.__init__)


def test_executiontrace_storypatternobjectbound_constructor_args():
    sig = inspect.signature(executionTrace_StoryPatternObjectBound.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_executiontrace_storypatternobjectbound_has_value():
    assert hasattr(executionTrace_StoryPatternObjectBound, "value")
    descriptor = None
    for klass in executionTrace_StoryPatternObjectBound.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_execution_is_not_abstract():
    assert not inspect.isabstract(executionTrace_Execution)


def test_executiontrace_execution_constructor_exists():
    assert callable(executionTrace_Execution.__init__)


def test_executiontrace_execution_constructor_args():
    sig = inspect.signature(executionTrace_Execution.__init__)
    params = list(sig.parameters.keys())
    assert "executionFinishedTimeStamp" in params, "Missing parameter 'executionFinishedTimeStamp'"
    assert "executionTimeMsec" in params, "Missing parameter 'executionTimeMsec'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"
    assert "executionStartedTimeStamp" in params, "Missing parameter 'executionStartedTimeStamp'"

def test_executiontrace_execution_has_executionFinishedTimeStamp():
    assert hasattr(executionTrace_Execution, "executionFinishedTimeStamp")
    descriptor = None
    for klass in executionTrace_Execution.__mro__:
        if "executionFinishedTimeStamp" in klass.__dict__:
            descriptor = klass.__dict__["executionFinishedTimeStamp"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_execution_has_executionTimeMsec():
    assert hasattr(executionTrace_Execution, "executionTimeMsec")
    descriptor = None
    for klass in executionTrace_Execution.__mro__:
        if "executionTimeMsec" in klass.__dict__:
            descriptor = klass.__dict__["executionTimeMsec"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_execution_has_executionTime():
    assert hasattr(executionTrace_Execution, "executionTime")
    descriptor = None
    for klass in executionTrace_Execution.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_execution_has_executionStartedTimeStamp():
    assert hasattr(executionTrace_Execution, "executionStartedTimeStamp")
    descriptor = None
    for klass in executionTrace_Execution.__mro__:
        if "executionStartedTimeStamp" in klass.__dict__:
            descriptor = klass.__dict__["executionStartedTimeStamp"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_executiontrace_is_not_abstract():
    assert not inspect.isabstract(executionTrace_ExecutionTrace)


def test_executiontrace_executiontrace_constructor_exists():
    assert callable(executionTrace_ExecutionTrace.__init__)


def test_executiontrace_executiontrace_constructor_args():
    sig = inspect.signature(executionTrace_ExecutionTrace.__init__)
    params = list(sig.parameters.keys())
    assert "totalExecutionTimeMsec" in params, "Missing parameter 'totalExecutionTimeMsec'"
    assert "totalExecutionTime" in params, "Missing parameter 'totalExecutionTime'"
    assert "description" in params, "Missing parameter 'description'"

def test_executiontrace_executiontrace_has_totalExecutionTimeMsec():
    assert hasattr(executionTrace_ExecutionTrace, "totalExecutionTimeMsec")
    descriptor = None
    for klass in executionTrace_ExecutionTrace.__mro__:
        if "totalExecutionTimeMsec" in klass.__dict__:
            descriptor = klass.__dict__["totalExecutionTimeMsec"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_executiontrace_has_totalExecutionTime():
    assert hasattr(executionTrace_ExecutionTrace, "totalExecutionTime")
    descriptor = None
    for klass in executionTrace_ExecutionTrace.__mro__:
        if "totalExecutionTime" in klass.__dict__:
            descriptor = klass.__dict__["totalExecutionTime"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_executiontrace_has_description():
    assert hasattr(executionTrace_ExecutionTrace, "description")
    descriptor = None
    for klass in executionTrace_ExecutionTrace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace_mapentry_is_not_abstract():
    assert not inspect.isabstract(executionTrace_MapEntry)


def test_executiontrace_mapentry_constructor_exists():
    assert callable(executionTrace_MapEntry.__init__)


def test_executiontrace_mapentry_constructor_args():
    sig = inspect.signature(executionTrace_MapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_executiontrace_mapentry_has_key():
    assert hasattr(executionTrace_MapEntry, "key")
    descriptor = None
    for klass in executionTrace_MapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace_mapentry_has_value():
    assert hasattr(executionTrace_MapEntry, "value")
    descriptor = None
    for klass in executionTrace_MapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)


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
executionTrace_StoryPatternObjectConstraintEvaluation_strategy = st.builds(
    executionTrace_StoryPatternObjectConstraintEvaluation,
)
executionTrace_VariableChanged_strategy = st.builds(
    executionTrace_VariableChanged,
    oldValue=
        safe_text
)
executionTrace_VariableDeleted_strategy = st.builds(
    executionTrace_VariableDeleted,
)
executionTrace_VariableCreated_strategy = st.builds(
    executionTrace_VariableCreated,
)
executionTrace_StoryPatternConstraintViolated_strategy = st.builds(
    executionTrace_StoryPatternConstraintViolated,
)
executionTrace_StoryPatternConstraintHolds_strategy = st.builds(
    executionTrace_StoryPatternConstraintHolds,
)
executionTrace_StoryPatternConstraintEvaluation_strategy = st.builds(
    executionTrace_StoryPatternConstraintEvaluation,
)
executionTrace_StoryPatternObjectConstraintViolated_strategy = st.builds(
    executionTrace_StoryPatternObjectConstraintViolated,
)
executionTrace_StoryPatternObjectConstraintHolds_strategy = st.builds(
    executionTrace_StoryPatternObjectConstraintHolds,
)
executionTrace_LinkCheckFailed_strategy = st.builds(
    executionTrace_LinkCheckFailed,
)
executionTrace_LinkCheckSuccessful_strategy = st.builds(
    executionTrace_LinkCheckSuccessful,
)
executionTrace_LinkCheck_strategy = st.builds(
    executionTrace_LinkCheck,
    targetObject=
        safe_text
)
executionTrace_TraversingLink_strategy = st.builds(
    executionTrace_TraversingLink,
)
executionTrace_InstanceLinkDeletion_strategy = st.builds(
    executionTrace_InstanceLinkDeletion,
)
executionTrace_InstanceLinkCreation_strategy = st.builds(
    executionTrace_InstanceLinkCreation,
)
executionTrace_InstanceObjectDeletion_strategy = st.builds(
    executionTrace_InstanceObjectDeletion,
)
executionTrace_InstanceObjectCreation_strategy = st.builds(
    executionTrace_InstanceObjectCreation,
)
executionTrace_StoryPatternApplication_strategy = st.builds(
    executionTrace_StoryPatternApplication,
)
executionTrace_StoryPatternMatching_strategy = st.builds(
    executionTrace_StoryPatternMatching,
    successful=
        st.booleans()
)
executionTrace_StoryPatternInitialization_strategy = st.builds(
    executionTrace_StoryPatternInitialization,
)
Execution_strategy = st.builds(
    Execution,
)
executionTrace_StoryPatternObjectExecution_strategy = st.builds(
    executionTrace_StoryPatternObjectExecution,
)
executionTrace_ActivityNodeExecution_strategy = st.builds(
    executionTrace_ActivityNodeExecution,
)
executionTrace_ExpressionEvaluation_strategy = st.builds(
    executionTrace_ExpressionEvaluation,
    result=
        safe_text
)
executionTrace_StoryPatternExecution_strategy = st.builds(
    executionTrace_StoryPatternExecution,
)
executionTrace_AttributeValueSet_strategy = st.builds(
    executionTrace_AttributeValueSet,
    instanceObject=
        safe_text,
    newValue=
        safe_text
)
executionTrace_InstanceObjectModification_strategy = st.builds(
    executionTrace_InstanceObjectModification,
    instanceObject=
        safe_text
)
executionTrace_ActivityEdgeTraversal_strategy = st.builds(
    executionTrace_ActivityEdgeTraversal,
)
executionTrace_VariableModification_strategy = st.builds(
    executionTrace_VariableModification,
    value=
        safe_text,
    variableName=
        safe_text
)
executionTrace_InstanceLinkModification_strategy = st.builds(
    executionTrace_InstanceLinkModification,
    targetInstanceObject=
        safe_text,
    sourceInstanceObject=
        safe_text
)
executionTrace_ActivityExecution_strategy = st.builds(
    executionTrace_ActivityExecution,
)
executionTrace_StoryPatternLinkExecution_strategy = st.builds(
    executionTrace_StoryPatternLinkExecution,
    sourceObject=
        safe_text
)
executionTrace_StoryPatternObjectBindingRevoked_strategy = st.builds(
    executionTrace_StoryPatternObjectBindingRevoked,
    previousValue=
        safe_text
)
executionTrace_StoryPatternObjectNotBound_strategy = st.builds(
    executionTrace_StoryPatternObjectNotBound,
)
executionTrace_StoryPatternObjectBound_strategy = st.builds(
    executionTrace_StoryPatternObjectBound,
    value=
        safe_text
)
executionTrace_Execution_strategy = st.builds(
    executionTrace_Execution,
    executionFinishedTimeStamp=
        safe_text,
    executionTimeMsec=
        safe_text,
    executionTime=
        safe_text,
    executionStartedTimeStamp=
        safe_text
)
executionTrace_ExecutionTrace_strategy = st.builds(
    executionTrace_ExecutionTrace,
    totalExecutionTimeMsec=
        safe_text,
    totalExecutionTime=
        safe_text,
    description=
        safe_text
)
executionTrace_MapEntry_strategy = st.builds(
    executionTrace_MapEntry,
    key=
        safe_text,
    value=
        safe_text
)

@given(instance=executionTrace_StoryPatternObjectConstraintEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectconstraintevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintEvaluation)

@given(instance=executionTrace_VariableChanged_strategy)
@settings(max_examples=50)
def test_executiontrace_variablechanged_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableChanged)



@given(instance=executionTrace_VariableChanged_strategy)
def test_executiontrace_variablechanged_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=executionTrace_VariableDeleted_strategy)
@settings(max_examples=50)
def test_executiontrace_variabledeleted_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableDeleted)

@given(instance=executionTrace_VariableCreated_strategy)
@settings(max_examples=50)
def test_executiontrace_variablecreated_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableCreated)

@given(instance=executionTrace_StoryPatternConstraintViolated_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternconstraintviolated_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintViolated)

@given(instance=executionTrace_StoryPatternConstraintHolds_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternconstraintholds_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintHolds)

@given(instance=executionTrace_StoryPatternConstraintEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternconstraintevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternConstraintEvaluation)

@given(instance=executionTrace_StoryPatternObjectConstraintViolated_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectconstraintviolated_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintViolated)

@given(instance=executionTrace_StoryPatternObjectConstraintHolds_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectconstraintholds_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectConstraintHolds)

@given(instance=executionTrace_LinkCheckFailed_strategy)
@settings(max_examples=50)
def test_executiontrace_linkcheckfailed_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheckFailed)

@given(instance=executionTrace_LinkCheckSuccessful_strategy)
@settings(max_examples=50)
def test_executiontrace_linkchecksuccessful_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheckSuccessful)

@given(instance=executionTrace_LinkCheck_strategy)
@settings(max_examples=50)
def test_executiontrace_linkcheck_instantiation(instance):
    assert isinstance(instance, executionTrace_LinkCheck)



@given(instance=executionTrace_LinkCheck_strategy)
def test_executiontrace_linkcheck_targetObject_setter(instance):
    original = instance.targetObject
    instance.targetObject = original
    assert instance.targetObject == original

@given(instance=executionTrace_TraversingLink_strategy)
@settings(max_examples=50)
def test_executiontrace_traversinglink_instantiation(instance):
    assert isinstance(instance, executionTrace_TraversingLink)

@given(instance=executionTrace_InstanceLinkDeletion_strategy)
@settings(max_examples=50)
def test_executiontrace_instancelinkdeletion_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkDeletion)

@given(instance=executionTrace_InstanceLinkCreation_strategy)
@settings(max_examples=50)
def test_executiontrace_instancelinkcreation_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkCreation)

@given(instance=executionTrace_InstanceObjectDeletion_strategy)
@settings(max_examples=50)
def test_executiontrace_instanceobjectdeletion_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectDeletion)

@given(instance=executionTrace_InstanceObjectCreation_strategy)
@settings(max_examples=50)
def test_executiontrace_instanceobjectcreation_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectCreation)

@given(instance=executionTrace_StoryPatternApplication_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternapplication_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternApplication)

@given(instance=executionTrace_StoryPatternMatching_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternmatching_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternMatching)



@given(instance=executionTrace_StoryPatternMatching_strategy)
def test_executiontrace_storypatternmatching_successful_setter(instance):
    original = instance.successful
    instance.successful = original
    assert instance.successful == original

@given(instance=executionTrace_StoryPatternInitialization_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatterninitialization_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternInitialization)

@given(instance=Execution_strategy)
@settings(max_examples=50)
def test_execution_instantiation(instance):
    assert isinstance(instance, Execution)

@given(instance=executionTrace_StoryPatternObjectExecution_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectexecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectExecution)

@given(instance=executionTrace_ActivityNodeExecution_strategy)
@settings(max_examples=50)
def test_executiontrace_activitynodeexecution_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityNodeExecution)

@given(instance=executionTrace_ExpressionEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace_expressionevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace_ExpressionEvaluation)



@given(instance=executionTrace_ExpressionEvaluation_strategy)
def test_executiontrace_expressionevaluation_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original

@given(instance=executionTrace_StoryPatternExecution_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternexecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternExecution)

@given(instance=executionTrace_AttributeValueSet_strategy)
@settings(max_examples=50)
def test_executiontrace_attributevalueset_instantiation(instance):
    assert isinstance(instance, executionTrace_AttributeValueSet)



@given(instance=executionTrace_AttributeValueSet_strategy)
def test_executiontrace_attributevalueset_instanceObject_setter(instance):
    original = instance.instanceObject
    instance.instanceObject = original
    assert instance.instanceObject == original



@given(instance=executionTrace_AttributeValueSet_strategy)
def test_executiontrace_attributevalueset_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=executionTrace_InstanceObjectModification_strategy)
@settings(max_examples=50)
def test_executiontrace_instanceobjectmodification_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceObjectModification)



@given(instance=executionTrace_InstanceObjectModification_strategy)
def test_executiontrace_instanceobjectmodification_instanceObject_setter(instance):
    original = instance.instanceObject
    instance.instanceObject = original
    assert instance.instanceObject == original

@given(instance=executionTrace_ActivityEdgeTraversal_strategy)
@settings(max_examples=50)
def test_executiontrace_activityedgetraversal_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityEdgeTraversal)

@given(instance=executionTrace_VariableModification_strategy)
@settings(max_examples=50)
def test_executiontrace_variablemodification_instantiation(instance):
    assert isinstance(instance, executionTrace_VariableModification)



@given(instance=executionTrace_VariableModification_strategy)
def test_executiontrace_variablemodification_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=executionTrace_VariableModification_strategy)
def test_executiontrace_variablemodification_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=executionTrace_InstanceLinkModification_strategy)
@settings(max_examples=50)
def test_executiontrace_instancelinkmodification_instantiation(instance):
    assert isinstance(instance, executionTrace_InstanceLinkModification)



@given(instance=executionTrace_InstanceLinkModification_strategy)
def test_executiontrace_instancelinkmodification_targetInstanceObject_setter(instance):
    original = instance.targetInstanceObject
    instance.targetInstanceObject = original
    assert instance.targetInstanceObject == original



@given(instance=executionTrace_InstanceLinkModification_strategy)
def test_executiontrace_instancelinkmodification_sourceInstanceObject_setter(instance):
    original = instance.sourceInstanceObject
    instance.sourceInstanceObject = original
    assert instance.sourceInstanceObject == original

@given(instance=executionTrace_ActivityExecution_strategy)
@settings(max_examples=50)
def test_executiontrace_activityexecution_instantiation(instance):
    assert isinstance(instance, executionTrace_ActivityExecution)

@given(instance=executionTrace_StoryPatternLinkExecution_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternlinkexecution_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternLinkExecution)



@given(instance=executionTrace_StoryPatternLinkExecution_strategy)
def test_executiontrace_storypatternlinkexecution_sourceObject_setter(instance):
    original = instance.sourceObject
    instance.sourceObject = original
    assert instance.sourceObject == original

@given(instance=executionTrace_StoryPatternObjectBindingRevoked_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectbindingrevoked_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectBindingRevoked)



@given(instance=executionTrace_StoryPatternObjectBindingRevoked_strategy)
def test_executiontrace_storypatternobjectbindingrevoked_previousValue_setter(instance):
    original = instance.previousValue
    instance.previousValue = original
    assert instance.previousValue == original

@given(instance=executionTrace_StoryPatternObjectNotBound_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectnotbound_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectNotBound)

@given(instance=executionTrace_StoryPatternObjectBound_strategy)
@settings(max_examples=50)
def test_executiontrace_storypatternobjectbound_instantiation(instance):
    assert isinstance(instance, executionTrace_StoryPatternObjectBound)



@given(instance=executionTrace_StoryPatternObjectBound_strategy)
def test_executiontrace_storypatternobjectbound_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=executionTrace_Execution_strategy)
@settings(max_examples=50)
def test_executiontrace_execution_instantiation(instance):
    assert isinstance(instance, executionTrace_Execution)



@given(instance=executionTrace_Execution_strategy)
def test_executiontrace_execution_executionFinishedTimeStamp_setter(instance):
    original = instance.executionFinishedTimeStamp
    instance.executionFinishedTimeStamp = original
    assert instance.executionFinishedTimeStamp == original



@given(instance=executionTrace_Execution_strategy)
def test_executiontrace_execution_executionTimeMsec_setter(instance):
    original = instance.executionTimeMsec
    instance.executionTimeMsec = original
    assert instance.executionTimeMsec == original



@given(instance=executionTrace_Execution_strategy)
def test_executiontrace_execution_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original



@given(instance=executionTrace_Execution_strategy)
def test_executiontrace_execution_executionStartedTimeStamp_setter(instance):
    original = instance.executionStartedTimeStamp
    instance.executionStartedTimeStamp = original
    assert instance.executionStartedTimeStamp == original

@given(instance=executionTrace_ExecutionTrace_strategy)
@settings(max_examples=50)
def test_executiontrace_executiontrace_instantiation(instance):
    assert isinstance(instance, executionTrace_ExecutionTrace)



@given(instance=executionTrace_ExecutionTrace_strategy)
def test_executiontrace_executiontrace_totalExecutionTimeMsec_setter(instance):
    original = instance.totalExecutionTimeMsec
    instance.totalExecutionTimeMsec = original
    assert instance.totalExecutionTimeMsec == original



@given(instance=executionTrace_ExecutionTrace_strategy)
def test_executiontrace_executiontrace_totalExecutionTime_setter(instance):
    original = instance.totalExecutionTime
    instance.totalExecutionTime = original
    assert instance.totalExecutionTime == original



@given(instance=executionTrace_ExecutionTrace_strategy)
def test_executiontrace_executiontrace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=executionTrace_MapEntry_strategy)
@settings(max_examples=50)
def test_executiontrace_mapentry_instantiation(instance):
    assert isinstance(instance, executionTrace_MapEntry)



@given(instance=executionTrace_MapEntry_strategy)
def test_executiontrace_mapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original



@given(instance=executionTrace_MapEntry_strategy)
def test_executiontrace_mapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
