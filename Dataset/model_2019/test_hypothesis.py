import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Execution,
    executionTrace::ActivityNodeExecution,
    executionTrace::ActivityExecution,
    executionTrace::StoryPatternLinkExecution,
    executionTrace::StoryPatternObjectBindingRevoked,
    executionTrace::StoryPatternObjectNotBound,
    executionTrace::StoryPatternObjectBound,
    executionTrace::Execution,
    executionTrace::ExecutionTrace,
    executionTrace::MapEntry,
    executionTrace::StoryPatternObjectConstraintEvaluation,
    executionTrace::VariableChanged,
    executionTrace::VariableDeleted,
    executionTrace::VariableCreated,
    executionTrace::VariableModification,
    executionTrace::AttributeValueSet,
    executionTrace::StoryPatternConstraintViolated,
    executionTrace::StoryPatternConstraintHolds,
    executionTrace::StoryPatternConstraintEvaluation,
    executionTrace::StoryPatternObjectConstraintViolated,
    executionTrace::StoryPatternObjectConstraintHolds,
    executionTrace::InstanceObjectModification,
    executionTrace::ExpressionEvaluation,
    executionTrace::LinkCheckFailed,
    executionTrace::LinkCheckSuccessful,
    executionTrace::LinkCheck,
    executionTrace::TraversingLink,
    executionTrace::InstanceLinkDeletion,
    executionTrace::InstanceLinkCreation,
    executionTrace::InstanceLinkModification,
    executionTrace::InstanceObjectDeletion,
    executionTrace::InstanceObjectCreation,
    executionTrace::StoryPatternObjectExecution,
    executionTrace::StoryPatternApplication,
    executionTrace::StoryPatternMatching,
    executionTrace::StoryPatternInitialization,
    executionTrace::StoryPatternExecution,
    executionTrace::ActivityEdgeTraversal,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_execution_is_not_abstract():
    assert not inspect.isabstract(Execution)


def test_execution_constructor_exists():
    assert callable(Execution.__init__)


def test_execution_constructor_args():
    sig = inspect.signature(Execution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::activitynodeexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::ActivityNodeExecution)


def test_executiontrace::activitynodeexecution_constructor_exists():
    assert callable(executionTrace::ActivityNodeExecution.__init__)


def test_executiontrace::activitynodeexecution_constructor_args():
    sig = inspect.signature(executionTrace::ActivityNodeExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::activityexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::ActivityExecution)


def test_executiontrace::activityexecution_constructor_exists():
    assert callable(executionTrace::ActivityExecution.__init__)


def test_executiontrace::activityexecution_constructor_args():
    sig = inspect.signature(executionTrace::ActivityExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternlinkexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternLinkExecution)


def test_executiontrace::storypatternlinkexecution_constructor_exists():
    assert callable(executionTrace::StoryPatternLinkExecution.__init__)


def test_executiontrace::storypatternlinkexecution_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternLinkExecution.__init__)
    params = list(sig.parameters.keys())
    assert "sourceObject" in params, "Missing parameter 'sourceObject'"

def test_executiontrace::storypatternlinkexecution_has_sourceObject():
    assert hasattr(executionTrace::StoryPatternLinkExecution, "sourceObject")
    descriptor = None
    for klass in executionTrace::StoryPatternLinkExecution.__mro__:
        if "sourceObject" in klass.__dict__:
            descriptor = klass.__dict__["sourceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::storypatternobjectbindingrevoked_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectBindingRevoked)


def test_executiontrace::storypatternobjectbindingrevoked_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectBindingRevoked.__init__)


def test_executiontrace::storypatternobjectbindingrevoked_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectBindingRevoked.__init__)
    params = list(sig.parameters.keys())
    assert "previousValue" in params, "Missing parameter 'previousValue'"

def test_executiontrace::storypatternobjectbindingrevoked_has_previousValue():
    assert hasattr(executionTrace::StoryPatternObjectBindingRevoked, "previousValue")
    descriptor = None
    for klass in executionTrace::StoryPatternObjectBindingRevoked.__mro__:
        if "previousValue" in klass.__dict__:
            descriptor = klass.__dict__["previousValue"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::storypatternobjectnotbound_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectNotBound)


def test_executiontrace::storypatternobjectnotbound_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectNotBound.__init__)


def test_executiontrace::storypatternobjectnotbound_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectNotBound.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternobjectbound_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectBound)


def test_executiontrace::storypatternobjectbound_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectBound.__init__)


def test_executiontrace::storypatternobjectbound_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectBound.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_executiontrace::storypatternobjectbound_has_value():
    assert hasattr(executionTrace::StoryPatternObjectBound, "value")
    descriptor = None
    for klass in executionTrace::StoryPatternObjectBound.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::execution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::Execution)


def test_executiontrace::execution_constructor_exists():
    assert callable(executionTrace::Execution.__init__)


def test_executiontrace::execution_constructor_args():
    sig = inspect.signature(executionTrace::Execution.__init__)
    params = list(sig.parameters.keys())
    assert "executionFinishedTimeStamp" in params, "Missing parameter 'executionFinishedTimeStamp'"
    assert "executionStartedTimeStamp" in params, "Missing parameter 'executionStartedTimeStamp'"
    assert "executionTimeMsec" in params, "Missing parameter 'executionTimeMsec'"
    assert "executionTime" in params, "Missing parameter 'executionTime'"

def test_executiontrace::execution_has_executionFinishedTimeStamp():
    assert hasattr(executionTrace::Execution, "executionFinishedTimeStamp")
    descriptor = None
    for klass in executionTrace::Execution.__mro__:
        if "executionFinishedTimeStamp" in klass.__dict__:
            descriptor = klass.__dict__["executionFinishedTimeStamp"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::execution_has_executionStartedTimeStamp():
    assert hasattr(executionTrace::Execution, "executionStartedTimeStamp")
    descriptor = None
    for klass in executionTrace::Execution.__mro__:
        if "executionStartedTimeStamp" in klass.__dict__:
            descriptor = klass.__dict__["executionStartedTimeStamp"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::execution_has_executionTimeMsec():
    assert hasattr(executionTrace::Execution, "executionTimeMsec")
    descriptor = None
    for klass in executionTrace::Execution.__mro__:
        if "executionTimeMsec" in klass.__dict__:
            descriptor = klass.__dict__["executionTimeMsec"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::execution_has_executionTime():
    assert hasattr(executionTrace::Execution, "executionTime")
    descriptor = None
    for klass in executionTrace::Execution.__mro__:
        if "executionTime" in klass.__dict__:
            descriptor = klass.__dict__["executionTime"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::executiontrace_is_not_abstract():
    assert not inspect.isabstract(executionTrace::ExecutionTrace)


def test_executiontrace::executiontrace_constructor_exists():
    assert callable(executionTrace::ExecutionTrace.__init__)


def test_executiontrace::executiontrace_constructor_args():
    sig = inspect.signature(executionTrace::ExecutionTrace.__init__)
    params = list(sig.parameters.keys())
    assert "totalExecutionTimeMsec" in params, "Missing parameter 'totalExecutionTimeMsec'"
    assert "description" in params, "Missing parameter 'description'"
    assert "totalExecutionTime" in params, "Missing parameter 'totalExecutionTime'"

def test_executiontrace::executiontrace_has_totalExecutionTimeMsec():
    assert hasattr(executionTrace::ExecutionTrace, "totalExecutionTimeMsec")
    descriptor = None
    for klass in executionTrace::ExecutionTrace.__mro__:
        if "totalExecutionTimeMsec" in klass.__dict__:
            descriptor = klass.__dict__["totalExecutionTimeMsec"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::executiontrace_has_description():
    assert hasattr(executionTrace::ExecutionTrace, "description")
    descriptor = None
    for klass in executionTrace::ExecutionTrace.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::executiontrace_has_totalExecutionTime():
    assert hasattr(executionTrace::ExecutionTrace, "totalExecutionTime")
    descriptor = None
    for klass in executionTrace::ExecutionTrace.__mro__:
        if "totalExecutionTime" in klass.__dict__:
            descriptor = klass.__dict__["totalExecutionTime"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::mapentry_is_not_abstract():
    assert not inspect.isabstract(executionTrace::MapEntry)


def test_executiontrace::mapentry_constructor_exists():
    assert callable(executionTrace::MapEntry.__init__)


def test_executiontrace::mapentry_constructor_args():
    sig = inspect.signature(executionTrace::MapEntry.__init__)
    params = list(sig.parameters.keys())
    assert "key" in params, "Missing parameter 'key'"
    assert "value" in params, "Missing parameter 'value'"

def test_executiontrace::mapentry_has_key():
    assert hasattr(executionTrace::MapEntry, "key")
    descriptor = None
    for klass in executionTrace::MapEntry.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::mapentry_has_value():
    assert hasattr(executionTrace::MapEntry, "value")
    descriptor = None
    for klass in executionTrace::MapEntry.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::storypatternobjectconstraintevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectConstraintEvaluation)


def test_executiontrace::storypatternobjectconstraintevaluation_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectConstraintEvaluation.__init__)


def test_executiontrace::storypatternobjectconstraintevaluation_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectConstraintEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::variablechanged_is_not_abstract():
    assert not inspect.isabstract(executionTrace::VariableChanged)


def test_executiontrace::variablechanged_constructor_exists():
    assert callable(executionTrace::VariableChanged.__init__)


def test_executiontrace::variablechanged_constructor_args():
    sig = inspect.signature(executionTrace::VariableChanged.__init__)
    params = list(sig.parameters.keys())
    assert "oldValue" in params, "Missing parameter 'oldValue'"

def test_executiontrace::variablechanged_has_oldValue():
    assert hasattr(executionTrace::VariableChanged, "oldValue")
    descriptor = None
    for klass in executionTrace::VariableChanged.__mro__:
        if "oldValue" in klass.__dict__:
            descriptor = klass.__dict__["oldValue"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::variabledeleted_is_not_abstract():
    assert not inspect.isabstract(executionTrace::VariableDeleted)


def test_executiontrace::variabledeleted_constructor_exists():
    assert callable(executionTrace::VariableDeleted.__init__)


def test_executiontrace::variabledeleted_constructor_args():
    sig = inspect.signature(executionTrace::VariableDeleted.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::variablecreated_is_not_abstract():
    assert not inspect.isabstract(executionTrace::VariableCreated)


def test_executiontrace::variablecreated_constructor_exists():
    assert callable(executionTrace::VariableCreated.__init__)


def test_executiontrace::variablecreated_constructor_args():
    sig = inspect.signature(executionTrace::VariableCreated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::variablemodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace::VariableModification)


def test_executiontrace::variablemodification_constructor_exists():
    assert callable(executionTrace::VariableModification.__init__)


def test_executiontrace::variablemodification_constructor_args():
    sig = inspect.signature(executionTrace::VariableModification.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "variableName" in params, "Missing parameter 'variableName'"

def test_executiontrace::variablemodification_has_value():
    assert hasattr(executionTrace::VariableModification, "value")
    descriptor = None
    for klass in executionTrace::VariableModification.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::variablemodification_has_variableName():
    assert hasattr(executionTrace::VariableModification, "variableName")
    descriptor = None
    for klass in executionTrace::VariableModification.__mro__:
        if "variableName" in klass.__dict__:
            descriptor = klass.__dict__["variableName"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::attributevalueset_is_not_abstract():
    assert not inspect.isabstract(executionTrace::AttributeValueSet)


def test_executiontrace::attributevalueset_constructor_exists():
    assert callable(executionTrace::AttributeValueSet.__init__)


def test_executiontrace::attributevalueset_constructor_args():
    sig = inspect.signature(executionTrace::AttributeValueSet.__init__)
    params = list(sig.parameters.keys())
    assert "newValue" in params, "Missing parameter 'newValue'"
    assert "instanceObject" in params, "Missing parameter 'instanceObject'"

def test_executiontrace::attributevalueset_has_newValue():
    assert hasattr(executionTrace::AttributeValueSet, "newValue")
    descriptor = None
    for klass in executionTrace::AttributeValueSet.__mro__:
        if "newValue" in klass.__dict__:
            descriptor = klass.__dict__["newValue"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::attributevalueset_has_instanceObject():
    assert hasattr(executionTrace::AttributeValueSet, "instanceObject")
    descriptor = None
    for klass in executionTrace::AttributeValueSet.__mro__:
        if "instanceObject" in klass.__dict__:
            descriptor = klass.__dict__["instanceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::storypatternconstraintviolated_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternConstraintViolated)


def test_executiontrace::storypatternconstraintviolated_constructor_exists():
    assert callable(executionTrace::StoryPatternConstraintViolated.__init__)


def test_executiontrace::storypatternconstraintviolated_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternConstraintViolated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternconstraintholds_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternConstraintHolds)


def test_executiontrace::storypatternconstraintholds_constructor_exists():
    assert callable(executionTrace::StoryPatternConstraintHolds.__init__)


def test_executiontrace::storypatternconstraintholds_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternConstraintHolds.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternconstraintevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternConstraintEvaluation)


def test_executiontrace::storypatternconstraintevaluation_constructor_exists():
    assert callable(executionTrace::StoryPatternConstraintEvaluation.__init__)


def test_executiontrace::storypatternconstraintevaluation_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternConstraintEvaluation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternobjectconstraintviolated_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectConstraintViolated)


def test_executiontrace::storypatternobjectconstraintviolated_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectConstraintViolated.__init__)


def test_executiontrace::storypatternobjectconstraintviolated_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectConstraintViolated.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternobjectconstraintholds_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectConstraintHolds)


def test_executiontrace::storypatternobjectconstraintholds_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectConstraintHolds.__init__)


def test_executiontrace::storypatternobjectconstraintholds_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectConstraintHolds.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::instanceobjectmodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceObjectModification)


def test_executiontrace::instanceobjectmodification_constructor_exists():
    assert callable(executionTrace::InstanceObjectModification.__init__)


def test_executiontrace::instanceobjectmodification_constructor_args():
    sig = inspect.signature(executionTrace::InstanceObjectModification.__init__)
    params = list(sig.parameters.keys())
    assert "instanceObject" in params, "Missing parameter 'instanceObject'"

def test_executiontrace::instanceobjectmodification_has_instanceObject():
    assert hasattr(executionTrace::InstanceObjectModification, "instanceObject")
    descriptor = None
    for klass in executionTrace::InstanceObjectModification.__mro__:
        if "instanceObject" in klass.__dict__:
            descriptor = klass.__dict__["instanceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::expressionevaluation_is_not_abstract():
    assert not inspect.isabstract(executionTrace::ExpressionEvaluation)


def test_executiontrace::expressionevaluation_constructor_exists():
    assert callable(executionTrace::ExpressionEvaluation.__init__)


def test_executiontrace::expressionevaluation_constructor_args():
    sig = inspect.signature(executionTrace::ExpressionEvaluation.__init__)
    params = list(sig.parameters.keys())
    assert "result" in params, "Missing parameter 'result'"

def test_executiontrace::expressionevaluation_has_result():
    assert hasattr(executionTrace::ExpressionEvaluation, "result")
    descriptor = None
    for klass in executionTrace::ExpressionEvaluation.__mro__:
        if "result" in klass.__dict__:
            descriptor = klass.__dict__["result"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::linkcheckfailed_is_not_abstract():
    assert not inspect.isabstract(executionTrace::LinkCheckFailed)


def test_executiontrace::linkcheckfailed_constructor_exists():
    assert callable(executionTrace::LinkCheckFailed.__init__)


def test_executiontrace::linkcheckfailed_constructor_args():
    sig = inspect.signature(executionTrace::LinkCheckFailed.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::linkchecksuccessful_is_not_abstract():
    assert not inspect.isabstract(executionTrace::LinkCheckSuccessful)


def test_executiontrace::linkchecksuccessful_constructor_exists():
    assert callable(executionTrace::LinkCheckSuccessful.__init__)


def test_executiontrace::linkchecksuccessful_constructor_args():
    sig = inspect.signature(executionTrace::LinkCheckSuccessful.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::linkcheck_is_not_abstract():
    assert not inspect.isabstract(executionTrace::LinkCheck)


def test_executiontrace::linkcheck_constructor_exists():
    assert callable(executionTrace::LinkCheck.__init__)


def test_executiontrace::linkcheck_constructor_args():
    sig = inspect.signature(executionTrace::LinkCheck.__init__)
    params = list(sig.parameters.keys())
    assert "targetObject" in params, "Missing parameter 'targetObject'"

def test_executiontrace::linkcheck_has_targetObject():
    assert hasattr(executionTrace::LinkCheck, "targetObject")
    descriptor = None
    for klass in executionTrace::LinkCheck.__mro__:
        if "targetObject" in klass.__dict__:
            descriptor = klass.__dict__["targetObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::traversinglink_is_not_abstract():
    assert not inspect.isabstract(executionTrace::TraversingLink)


def test_executiontrace::traversinglink_constructor_exists():
    assert callable(executionTrace::TraversingLink.__init__)


def test_executiontrace::traversinglink_constructor_args():
    sig = inspect.signature(executionTrace::TraversingLink.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::instancelinkdeletion_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceLinkDeletion)


def test_executiontrace::instancelinkdeletion_constructor_exists():
    assert callable(executionTrace::InstanceLinkDeletion.__init__)


def test_executiontrace::instancelinkdeletion_constructor_args():
    sig = inspect.signature(executionTrace::InstanceLinkDeletion.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::instancelinkcreation_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceLinkCreation)


def test_executiontrace::instancelinkcreation_constructor_exists():
    assert callable(executionTrace::InstanceLinkCreation.__init__)


def test_executiontrace::instancelinkcreation_constructor_args():
    sig = inspect.signature(executionTrace::InstanceLinkCreation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::instancelinkmodification_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceLinkModification)


def test_executiontrace::instancelinkmodification_constructor_exists():
    assert callable(executionTrace::InstanceLinkModification.__init__)


def test_executiontrace::instancelinkmodification_constructor_args():
    sig = inspect.signature(executionTrace::InstanceLinkModification.__init__)
    params = list(sig.parameters.keys())
    assert "targetInstanceObject" in params, "Missing parameter 'targetInstanceObject'"
    assert "sourceInstanceObject" in params, "Missing parameter 'sourceInstanceObject'"

def test_executiontrace::instancelinkmodification_has_targetInstanceObject():
    assert hasattr(executionTrace::InstanceLinkModification, "targetInstanceObject")
    descriptor = None
    for klass in executionTrace::InstanceLinkModification.__mro__:
        if "targetInstanceObject" in klass.__dict__:
            descriptor = klass.__dict__["targetInstanceObject"]
            break
    assert isinstance(descriptor, property)

def test_executiontrace::instancelinkmodification_has_sourceInstanceObject():
    assert hasattr(executionTrace::InstanceLinkModification, "sourceInstanceObject")
    descriptor = None
    for klass in executionTrace::InstanceLinkModification.__mro__:
        if "sourceInstanceObject" in klass.__dict__:
            descriptor = klass.__dict__["sourceInstanceObject"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::instanceobjectdeletion_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceObjectDeletion)


def test_executiontrace::instanceobjectdeletion_constructor_exists():
    assert callable(executionTrace::InstanceObjectDeletion.__init__)


def test_executiontrace::instanceobjectdeletion_constructor_args():
    sig = inspect.signature(executionTrace::InstanceObjectDeletion.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::instanceobjectcreation_is_not_abstract():
    assert not inspect.isabstract(executionTrace::InstanceObjectCreation)


def test_executiontrace::instanceobjectcreation_constructor_exists():
    assert callable(executionTrace::InstanceObjectCreation.__init__)


def test_executiontrace::instanceobjectcreation_constructor_args():
    sig = inspect.signature(executionTrace::InstanceObjectCreation.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternobjectexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternObjectExecution)


def test_executiontrace::storypatternobjectexecution_constructor_exists():
    assert callable(executionTrace::StoryPatternObjectExecution.__init__)


def test_executiontrace::storypatternobjectexecution_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternObjectExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternapplication_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternApplication)


def test_executiontrace::storypatternapplication_constructor_exists():
    assert callable(executionTrace::StoryPatternApplication.__init__)


def test_executiontrace::storypatternapplication_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternApplication.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternmatching_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternMatching)


def test_executiontrace::storypatternmatching_constructor_exists():
    assert callable(executionTrace::StoryPatternMatching.__init__)


def test_executiontrace::storypatternmatching_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternMatching.__init__)
    params = list(sig.parameters.keys())
    assert "successful" in params, "Missing parameter 'successful'"

def test_executiontrace::storypatternmatching_has_successful():
    assert hasattr(executionTrace::StoryPatternMatching, "successful")
    descriptor = None
    for klass in executionTrace::StoryPatternMatching.__mro__:
        if "successful" in klass.__dict__:
            descriptor = klass.__dict__["successful"]
            break
    assert isinstance(descriptor, property)



def test_executiontrace::storypatterninitialization_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternInitialization)


def test_executiontrace::storypatterninitialization_constructor_exists():
    assert callable(executionTrace::StoryPatternInitialization.__init__)


def test_executiontrace::storypatterninitialization_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternInitialization.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::storypatternexecution_is_not_abstract():
    assert not inspect.isabstract(executionTrace::StoryPatternExecution)


def test_executiontrace::storypatternexecution_constructor_exists():
    assert callable(executionTrace::StoryPatternExecution.__init__)


def test_executiontrace::storypatternexecution_constructor_args():
    sig = inspect.signature(executionTrace::StoryPatternExecution.__init__)
    params = list(sig.parameters.keys())



def test_executiontrace::activityedgetraversal_is_not_abstract():
    assert not inspect.isabstract(executionTrace::ActivityEdgeTraversal)


def test_executiontrace::activityedgetraversal_constructor_exists():
    assert callable(executionTrace::ActivityEdgeTraversal.__init__)


def test_executiontrace::activityedgetraversal_constructor_args():
    sig = inspect.signature(executionTrace::ActivityEdgeTraversal.__init__)
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
Execution_strategy = st.builds(
    Execution,
)
executionTrace::ActivityNodeExecution_strategy = st.builds(
    executionTrace::ActivityNodeExecution,
)
executionTrace::ActivityExecution_strategy = st.builds(
    executionTrace::ActivityExecution,
)
executionTrace::StoryPatternLinkExecution_strategy = st.builds(
    executionTrace::StoryPatternLinkExecution,
    sourceObject=
        safe_text
)
executionTrace::StoryPatternObjectBindingRevoked_strategy = st.builds(
    executionTrace::StoryPatternObjectBindingRevoked,
    previousValue=
        safe_text
)
executionTrace::StoryPatternObjectNotBound_strategy = st.builds(
    executionTrace::StoryPatternObjectNotBound,
)
executionTrace::StoryPatternObjectBound_strategy = st.builds(
    executionTrace::StoryPatternObjectBound,
    value=
        safe_text
)
executionTrace::Execution_strategy = st.builds(
    executionTrace::Execution,
    executionFinishedTimeStamp=
        safe_text,
    executionStartedTimeStamp=
        safe_text,
    executionTimeMsec=
        safe_text,
    executionTime=
        safe_text
)
executionTrace::ExecutionTrace_strategy = st.builds(
    executionTrace::ExecutionTrace,
    totalExecutionTimeMsec=
        safe_text,
    description=
        safe_text,
    totalExecutionTime=
        safe_text
)
executionTrace::MapEntry_strategy = st.builds(
    executionTrace::MapEntry,
    key=
        safe_text,
    value=
        safe_text
)
executionTrace::StoryPatternObjectConstraintEvaluation_strategy = st.builds(
    executionTrace::StoryPatternObjectConstraintEvaluation,
)
executionTrace::VariableChanged_strategy = st.builds(
    executionTrace::VariableChanged,
    oldValue=
        safe_text
)
executionTrace::VariableDeleted_strategy = st.builds(
    executionTrace::VariableDeleted,
)
executionTrace::VariableCreated_strategy = st.builds(
    executionTrace::VariableCreated,
)
executionTrace::VariableModification_strategy = st.builds(
    executionTrace::VariableModification,
    value=
        safe_text,
    variableName=
        safe_text
)
executionTrace::AttributeValueSet_strategy = st.builds(
    executionTrace::AttributeValueSet,
    newValue=
        safe_text,
    instanceObject=
        safe_text
)
executionTrace::StoryPatternConstraintViolated_strategy = st.builds(
    executionTrace::StoryPatternConstraintViolated,
)
executionTrace::StoryPatternConstraintHolds_strategy = st.builds(
    executionTrace::StoryPatternConstraintHolds,
)
executionTrace::StoryPatternConstraintEvaluation_strategy = st.builds(
    executionTrace::StoryPatternConstraintEvaluation,
)
executionTrace::StoryPatternObjectConstraintViolated_strategy = st.builds(
    executionTrace::StoryPatternObjectConstraintViolated,
)
executionTrace::StoryPatternObjectConstraintHolds_strategy = st.builds(
    executionTrace::StoryPatternObjectConstraintHolds,
)
executionTrace::InstanceObjectModification_strategy = st.builds(
    executionTrace::InstanceObjectModification,
    instanceObject=
        safe_text
)
executionTrace::ExpressionEvaluation_strategy = st.builds(
    executionTrace::ExpressionEvaluation,
    result=
        safe_text
)
executionTrace::LinkCheckFailed_strategy = st.builds(
    executionTrace::LinkCheckFailed,
)
executionTrace::LinkCheckSuccessful_strategy = st.builds(
    executionTrace::LinkCheckSuccessful,
)
executionTrace::LinkCheck_strategy = st.builds(
    executionTrace::LinkCheck,
    targetObject=
        safe_text
)
executionTrace::TraversingLink_strategy = st.builds(
    executionTrace::TraversingLink,
)
executionTrace::InstanceLinkDeletion_strategy = st.builds(
    executionTrace::InstanceLinkDeletion,
)
executionTrace::InstanceLinkCreation_strategy = st.builds(
    executionTrace::InstanceLinkCreation,
)
executionTrace::InstanceLinkModification_strategy = st.builds(
    executionTrace::InstanceLinkModification,
    targetInstanceObject=
        safe_text,
    sourceInstanceObject=
        safe_text
)
executionTrace::InstanceObjectDeletion_strategy = st.builds(
    executionTrace::InstanceObjectDeletion,
)
executionTrace::InstanceObjectCreation_strategy = st.builds(
    executionTrace::InstanceObjectCreation,
)
executionTrace::StoryPatternObjectExecution_strategy = st.builds(
    executionTrace::StoryPatternObjectExecution,
)
executionTrace::StoryPatternApplication_strategy = st.builds(
    executionTrace::StoryPatternApplication,
)
executionTrace::StoryPatternMatching_strategy = st.builds(
    executionTrace::StoryPatternMatching,
    successful=
        st.booleans()
)
executionTrace::StoryPatternInitialization_strategy = st.builds(
    executionTrace::StoryPatternInitialization,
)
executionTrace::StoryPatternExecution_strategy = st.builds(
    executionTrace::StoryPatternExecution,
)
executionTrace::ActivityEdgeTraversal_strategy = st.builds(
    executionTrace::ActivityEdgeTraversal,
)

@given(instance=Execution_strategy)
@settings(max_examples=50)
def test_execution_instantiation(instance):
    assert isinstance(instance, Execution)

@given(instance=executionTrace::ActivityNodeExecution_strategy)
@settings(max_examples=50)
def test_executiontrace::activitynodeexecution_instantiation(instance):
    assert isinstance(instance, executionTrace::ActivityNodeExecution)

@given(instance=executionTrace::ActivityExecution_strategy)
@settings(max_examples=50)
def test_executiontrace::activityexecution_instantiation(instance):
    assert isinstance(instance, executionTrace::ActivityExecution)

@given(instance=executionTrace::StoryPatternLinkExecution_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternlinkexecution_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternLinkExecution)

@given(instance=executionTrace::StoryPatternLinkExecution_strategy)
def test_executiontrace::storypatternlinkexecution_sourceObject_type(instance):
    assert isinstance(instance.sourceObject, str)


@given(instance=executionTrace::StoryPatternLinkExecution_strategy)
def test_executiontrace::storypatternlinkexecution_sourceObject_setter(instance):
    original = instance.sourceObject
    instance.sourceObject = original
    assert instance.sourceObject == original

@given(instance=executionTrace::StoryPatternObjectBindingRevoked_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectbindingrevoked_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectBindingRevoked)

@given(instance=executionTrace::StoryPatternObjectBindingRevoked_strategy)
def test_executiontrace::storypatternobjectbindingrevoked_previousValue_type(instance):
    assert isinstance(instance.previousValue, str)


@given(instance=executionTrace::StoryPatternObjectBindingRevoked_strategy)
def test_executiontrace::storypatternobjectbindingrevoked_previousValue_setter(instance):
    original = instance.previousValue
    instance.previousValue = original
    assert instance.previousValue == original

@given(instance=executionTrace::StoryPatternObjectNotBound_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectnotbound_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectNotBound)

@given(instance=executionTrace::StoryPatternObjectBound_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectbound_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectBound)

@given(instance=executionTrace::StoryPatternObjectBound_strategy)
def test_executiontrace::storypatternobjectbound_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=executionTrace::StoryPatternObjectBound_strategy)
def test_executiontrace::storypatternobjectbound_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=executionTrace::Execution_strategy)
@settings(max_examples=50)
def test_executiontrace::execution_instantiation(instance):
    assert isinstance(instance, executionTrace::Execution)

@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionFinishedTimeStamp_type(instance):
    assert isinstance(instance.executionFinishedTimeStamp, str)


@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionFinishedTimeStamp_setter(instance):
    original = instance.executionFinishedTimeStamp
    instance.executionFinishedTimeStamp = original
    assert instance.executionFinishedTimeStamp == original

@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionStartedTimeStamp_type(instance):
    assert isinstance(instance.executionStartedTimeStamp, str)


@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionStartedTimeStamp_setter(instance):
    original = instance.executionStartedTimeStamp
    instance.executionStartedTimeStamp = original
    assert instance.executionStartedTimeStamp == original

@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionTimeMsec_type(instance):
    assert isinstance(instance.executionTimeMsec, str)


@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionTimeMsec_setter(instance):
    original = instance.executionTimeMsec
    instance.executionTimeMsec = original
    assert instance.executionTimeMsec == original

@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionTime_type(instance):
    assert isinstance(instance.executionTime, str)


@given(instance=executionTrace::Execution_strategy)
def test_executiontrace::execution_executionTime_setter(instance):
    original = instance.executionTime
    instance.executionTime = original
    assert instance.executionTime == original

@given(instance=executionTrace::ExecutionTrace_strategy)
@settings(max_examples=50)
def test_executiontrace::executiontrace_instantiation(instance):
    assert isinstance(instance, executionTrace::ExecutionTrace)

@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_totalExecutionTimeMsec_type(instance):
    assert isinstance(instance.totalExecutionTimeMsec, str)


@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_totalExecutionTimeMsec_setter(instance):
    original = instance.totalExecutionTimeMsec
    instance.totalExecutionTimeMsec = original
    assert instance.totalExecutionTimeMsec == original

@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_totalExecutionTime_type(instance):
    assert isinstance(instance.totalExecutionTime, str)


@given(instance=executionTrace::ExecutionTrace_strategy)
def test_executiontrace::executiontrace_totalExecutionTime_setter(instance):
    original = instance.totalExecutionTime
    instance.totalExecutionTime = original
    assert instance.totalExecutionTime == original

@given(instance=executionTrace::MapEntry_strategy)
@settings(max_examples=50)
def test_executiontrace::mapentry_instantiation(instance):
    assert isinstance(instance, executionTrace::MapEntry)

@given(instance=executionTrace::MapEntry_strategy)
def test_executiontrace::mapentry_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=executionTrace::MapEntry_strategy)
def test_executiontrace::mapentry_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=executionTrace::MapEntry_strategy)
def test_executiontrace::mapentry_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=executionTrace::MapEntry_strategy)
def test_executiontrace::mapentry_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=executionTrace::StoryPatternObjectConstraintEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectconstraintevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectConstraintEvaluation)

@given(instance=executionTrace::VariableChanged_strategy)
@settings(max_examples=50)
def test_executiontrace::variablechanged_instantiation(instance):
    assert isinstance(instance, executionTrace::VariableChanged)

@given(instance=executionTrace::VariableChanged_strategy)
def test_executiontrace::variablechanged_oldValue_type(instance):
    assert isinstance(instance.oldValue, str)


@given(instance=executionTrace::VariableChanged_strategy)
def test_executiontrace::variablechanged_oldValue_setter(instance):
    original = instance.oldValue
    instance.oldValue = original
    assert instance.oldValue == original

@given(instance=executionTrace::VariableDeleted_strategy)
@settings(max_examples=50)
def test_executiontrace::variabledeleted_instantiation(instance):
    assert isinstance(instance, executionTrace::VariableDeleted)

@given(instance=executionTrace::VariableCreated_strategy)
@settings(max_examples=50)
def test_executiontrace::variablecreated_instantiation(instance):
    assert isinstance(instance, executionTrace::VariableCreated)

@given(instance=executionTrace::VariableModification_strategy)
@settings(max_examples=50)
def test_executiontrace::variablemodification_instantiation(instance):
    assert isinstance(instance, executionTrace::VariableModification)

@given(instance=executionTrace::VariableModification_strategy)
def test_executiontrace::variablemodification_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=executionTrace::VariableModification_strategy)
def test_executiontrace::variablemodification_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=executionTrace::VariableModification_strategy)
def test_executiontrace::variablemodification_variableName_type(instance):
    assert isinstance(instance.variableName, str)


@given(instance=executionTrace::VariableModification_strategy)
def test_executiontrace::variablemodification_variableName_setter(instance):
    original = instance.variableName
    instance.variableName = original
    assert instance.variableName == original

@given(instance=executionTrace::AttributeValueSet_strategy)
@settings(max_examples=50)
def test_executiontrace::attributevalueset_instantiation(instance):
    assert isinstance(instance, executionTrace::AttributeValueSet)

@given(instance=executionTrace::AttributeValueSet_strategy)
def test_executiontrace::attributevalueset_newValue_type(instance):
    assert isinstance(instance.newValue, str)


@given(instance=executionTrace::AttributeValueSet_strategy)
def test_executiontrace::attributevalueset_newValue_setter(instance):
    original = instance.newValue
    instance.newValue = original
    assert instance.newValue == original

@given(instance=executionTrace::AttributeValueSet_strategy)
def test_executiontrace::attributevalueset_instanceObject_type(instance):
    assert isinstance(instance.instanceObject, str)


@given(instance=executionTrace::AttributeValueSet_strategy)
def test_executiontrace::attributevalueset_instanceObject_setter(instance):
    original = instance.instanceObject
    instance.instanceObject = original
    assert instance.instanceObject == original

@given(instance=executionTrace::StoryPatternConstraintViolated_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternconstraintviolated_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternConstraintViolated)

@given(instance=executionTrace::StoryPatternConstraintHolds_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternconstraintholds_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternConstraintHolds)

@given(instance=executionTrace::StoryPatternConstraintEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternconstraintevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternConstraintEvaluation)

@given(instance=executionTrace::StoryPatternObjectConstraintViolated_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectconstraintviolated_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectConstraintViolated)

@given(instance=executionTrace::StoryPatternObjectConstraintHolds_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectconstraintholds_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectConstraintHolds)

@given(instance=executionTrace::InstanceObjectModification_strategy)
@settings(max_examples=50)
def test_executiontrace::instanceobjectmodification_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceObjectModification)

@given(instance=executionTrace::InstanceObjectModification_strategy)
def test_executiontrace::instanceobjectmodification_instanceObject_type(instance):
    assert isinstance(instance.instanceObject, str)


@given(instance=executionTrace::InstanceObjectModification_strategy)
def test_executiontrace::instanceobjectmodification_instanceObject_setter(instance):
    original = instance.instanceObject
    instance.instanceObject = original
    assert instance.instanceObject == original

@given(instance=executionTrace::ExpressionEvaluation_strategy)
@settings(max_examples=50)
def test_executiontrace::expressionevaluation_instantiation(instance):
    assert isinstance(instance, executionTrace::ExpressionEvaluation)

@given(instance=executionTrace::ExpressionEvaluation_strategy)
def test_executiontrace::expressionevaluation_result_type(instance):
    assert isinstance(instance.result, str)


@given(instance=executionTrace::ExpressionEvaluation_strategy)
def test_executiontrace::expressionevaluation_result_setter(instance):
    original = instance.result
    instance.result = original
    assert instance.result == original

@given(instance=executionTrace::LinkCheckFailed_strategy)
@settings(max_examples=50)
def test_executiontrace::linkcheckfailed_instantiation(instance):
    assert isinstance(instance, executionTrace::LinkCheckFailed)

@given(instance=executionTrace::LinkCheckSuccessful_strategy)
@settings(max_examples=50)
def test_executiontrace::linkchecksuccessful_instantiation(instance):
    assert isinstance(instance, executionTrace::LinkCheckSuccessful)

@given(instance=executionTrace::LinkCheck_strategy)
@settings(max_examples=50)
def test_executiontrace::linkcheck_instantiation(instance):
    assert isinstance(instance, executionTrace::LinkCheck)

@given(instance=executionTrace::LinkCheck_strategy)
def test_executiontrace::linkcheck_targetObject_type(instance):
    assert isinstance(instance.targetObject, str)


@given(instance=executionTrace::LinkCheck_strategy)
def test_executiontrace::linkcheck_targetObject_setter(instance):
    original = instance.targetObject
    instance.targetObject = original
    assert instance.targetObject == original

@given(instance=executionTrace::TraversingLink_strategy)
@settings(max_examples=50)
def test_executiontrace::traversinglink_instantiation(instance):
    assert isinstance(instance, executionTrace::TraversingLink)

@given(instance=executionTrace::InstanceLinkDeletion_strategy)
@settings(max_examples=50)
def test_executiontrace::instancelinkdeletion_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceLinkDeletion)

@given(instance=executionTrace::InstanceLinkCreation_strategy)
@settings(max_examples=50)
def test_executiontrace::instancelinkcreation_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceLinkCreation)

@given(instance=executionTrace::InstanceLinkModification_strategy)
@settings(max_examples=50)
def test_executiontrace::instancelinkmodification_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceLinkModification)

@given(instance=executionTrace::InstanceLinkModification_strategy)
def test_executiontrace::instancelinkmodification_targetInstanceObject_type(instance):
    assert isinstance(instance.targetInstanceObject, str)


@given(instance=executionTrace::InstanceLinkModification_strategy)
def test_executiontrace::instancelinkmodification_targetInstanceObject_setter(instance):
    original = instance.targetInstanceObject
    instance.targetInstanceObject = original
    assert instance.targetInstanceObject == original

@given(instance=executionTrace::InstanceLinkModification_strategy)
def test_executiontrace::instancelinkmodification_sourceInstanceObject_type(instance):
    assert isinstance(instance.sourceInstanceObject, str)


@given(instance=executionTrace::InstanceLinkModification_strategy)
def test_executiontrace::instancelinkmodification_sourceInstanceObject_setter(instance):
    original = instance.sourceInstanceObject
    instance.sourceInstanceObject = original
    assert instance.sourceInstanceObject == original

@given(instance=executionTrace::InstanceObjectDeletion_strategy)
@settings(max_examples=50)
def test_executiontrace::instanceobjectdeletion_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceObjectDeletion)

@given(instance=executionTrace::InstanceObjectCreation_strategy)
@settings(max_examples=50)
def test_executiontrace::instanceobjectcreation_instantiation(instance):
    assert isinstance(instance, executionTrace::InstanceObjectCreation)

@given(instance=executionTrace::StoryPatternObjectExecution_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternobjectexecution_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternObjectExecution)

@given(instance=executionTrace::StoryPatternApplication_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternapplication_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternApplication)

@given(instance=executionTrace::StoryPatternMatching_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternmatching_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternMatching)

@given(instance=executionTrace::StoryPatternMatching_strategy)
def test_executiontrace::storypatternmatching_successful_type(instance):
    assert isinstance(instance.successful, bool)


@given(instance=executionTrace::StoryPatternMatching_strategy)
def test_executiontrace::storypatternmatching_successful_setter(instance):
    original = instance.successful
    instance.successful = original
    assert instance.successful == original

@given(instance=executionTrace::StoryPatternInitialization_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatterninitialization_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternInitialization)

@given(instance=executionTrace::StoryPatternExecution_strategy)
@settings(max_examples=50)
def test_executiontrace::storypatternexecution_instantiation(instance):
    assert isinstance(instance, executionTrace::StoryPatternExecution)

@given(instance=executionTrace::ActivityEdgeTraversal_strategy)
@settings(max_examples=50)
def test_executiontrace::activityedgetraversal_instantiation(instance):
    assert isinstance(instance, executionTrace::ActivityEdgeTraversal)
