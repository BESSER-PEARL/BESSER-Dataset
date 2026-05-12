import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Events_trace_Value,
    activitydiagram_TracedIntegerVariable,
    activitydiagram_TracedDecisionNode,
    activitydiagram_TracedMergeNode,
    activitydiagram_TracedInitialNode,
    activitydiagram_TracedForkNode,
    activitydiagram_TracedActivityFinalNode,
    activitydiagram_TracedAction,
    activitydiagram_TracedOpaqueAction,
    activitydiagramConfiguration_TracedToken,
    activitydiagram_TracedControlNode,
    activitydiagram_TracedActivityEdge,
    activitydiagram_TracedActivityNode,
    trace_activitydiagramConfiguration_TracedOffer,
    trace_activitydiagramConfiguration_TracedInput,
    TracedToken,
    trace_activitydiagramConfiguration_TracedForkedToken,
    trace_activitydiagramConfiguration_TracedControlToken,
    trace_activitydiagramConfiguration_TracedToken,
    trace_activitydiagramConfiguration_TracedInputValue,
    activitydiagram_trace_DecisionNode,
    activitydiagram_trace_JoinNode,
    activitydiagram_trace_OpaqueAction,
    trace_activitydiagramConfiguration_TracedTrace,
    activitydiagram_trace_InitialNode,
    activitydiagram_trace_ForkNode,
    activitydiagram_trace_ActivityFinalNode,
    TracedFinalNode,
    trace_activitydiagram_TracedActivityFinalNode,
    TracedExecutableNode,
    activitydiagram_trace_Expression,
    trace_activitydiagram_TracedAction,
    TracedAction,
    trace_activitydiagram_TracedOpaqueAction,
    activitydiagram_trace_StringVariable,
    activitydiagram_trace_Activity,
    TracedNamedElement,
    trace_activitydiagram_TracedActivity,
    trace_activitydiagram_TracedActivityNode,
    trace_activitydiagram_TracedActivityEdge,
    activitydiagram_trace_IntegerVariable,
    TracedActivityNode,
    trace_activitydiagram_TracedControlNode,
    trace_activitydiagram_TracedExecutableNode,
    activitydiagram_trace_BooleanVariable,
    TracedVariable,
    trace_activitydiagram_TracedStringVariable,
    trace_activitydiagram_TracedIntegerVariable,
    trace_activitydiagram_TracedBooleanVariable,
    activitydiagram_trace_MergeNode,
    TracedControlNode,
    trace_activitydiagram_TracedForkNode,
    trace_activitydiagram_TracedInitialNode,
    trace_activitydiagram_TracedJoinNode,
    trace_activitydiagram_TracedDecisionNode,
    trace_activitydiagram_TracedFinalNode,
    trace_activitydiagram_TracedMergeNode,
    activitydiagram_trace_ControlFlow,
    TracedActivityEdge,
    trace_activitydiagram_TracedControlFlow,
    activitydiagram_TracedJoinNode,
    activitydiagram_trace_Value,
    trace_activitydiagram_TracedVariable,
    trace_activitydiagram_TracedNamedElement,
    activitydiagramConfiguration_TracedControlToken,
    activitydiagram_TracedControlFlow,
    trace_Traced_TracedObjects,
    activitydiagramConfiguration_TracedTrace,
    trace_States_Activity_trace_State,
    trace_States_ActivityNode_heldTokens_State,
    trace_States_ActivityNode_running_State,
    trace_States_Offer_offeredTokens_State,
    trace_States_Variable_currentValue_State,
    trace_States_Trace_executedNodes_State,
    trace_States_ForkedToken_baseTokenIsWithdrawn_State,
    trace_States_ForkedToken_baseToken_State,
    trace_States_ForkedToken_remainingOffersCount_State,
    activitydiagramConfiguration_TracedInput,
    trace_States_Input_inputValues_State,
    trace_States_Token_holder_State,
    trace_States_ActivityEdge_offers_State,
    activitydiagramConfiguration_TracedInputValue,
    States_trace_Value,
    trace_States_InputValue_value_State,
    activitydiagramConfiguration_TracedOffer,
    activitydiagramConfiguration_TracedForkedToken,
    activitydiagram_TracedVariable,
    trace_States_InputValue_variable_State,
    States_trace_GlobalState,
    Events_trace_BooleanBinaryExpression,
    Events_trace_BooleanUnaryExpression,
    Events_trace_IntegerComparisonExpression,
    Events_trace_IntegerExpression,
    activitydiagram_TracedBooleanVariable,
    Events_trace_IntegerCalculationExpression,
    activitydiagram_TracedStringVariable,
    Offer_hasTokensExitEventOccurrence,
    Events_trace_EObject,
    activitydiagram_TracedActivity,
    Token_isWithdrawnExitEventOccurrence,
    Token_isWithdrawnEntryEventOccurrence,
    BooleanBinaryExpression_evaluateORExitEventOccurrence,
    Offer_hasTokensEntryEventOccurrence,
    ForkedToken_withdraw_forkedTokenExitEventOccurrence,
    ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
    Token_withdrawExitEventOccurrence,
    Token_withdrawEntryEventOccurrence,
    Token_transferExitEventOccurrence,
    Token_transferEntryEventOccurrence,
    BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
    BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
    BooleanBinaryExpression_evaluateOREntryEventOccurrence,
    BooleanBinaryExpression_evaluateANDExitEventOccurrence,
    BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
    BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
    BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
    BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
    BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
    IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
    IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
    IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
    IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
    IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
    IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
    IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
    IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
    IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
    IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
    IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
    IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
    IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
    IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
    IntegerCalculationExpression_evaluateADDExitEventOccurrence,
    StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
    IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
    IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
    IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
    BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
    BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
    BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
    BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
    StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
    StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
    StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
    InitialNode_fire_initialNodeExitEventOccurrence,
    IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
    InitialNode_fire_initialNodeEntryEventOccurrence,
    IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
    IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
    DecisionNode_fire_decisionNodeExitEventOccurrence,
    DecisionNode_fire_decisionNodeEntryEventOccurrence,
    MergeNode_hasOffers_mergeNodeExitEventOccurrence,
    MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
    ForkNode_fire_forkNodeExitEventOccurrence,
    ForkNode_fire_forkNodeEntryEventOccurrence,
    ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
    ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
    Action_isReady_actionEntryEventOccurrence,
    Action_sendOffers_actionExitEventOccurrence,
    Action_sendOffers_actionEntryEventOccurrence,
    ControlNode_fire_controlNodeExitEventOccurrence,
    InitialNode_isReady_InitialNodeExitEventOccurrence,
    InitialNode_isReady_InitialNodeEntryEventOccurrence,
    OpaqueAction_doAction_opaqueActionExitEventOccurrence,
    OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
    Action_fire_actionExitEventOccurrence,
    Action_fire_actionEntryEventOccurrence,
    ActivityNode_isReadyExitEventOccurrence,
    Action_isReady_actionExitEventOccurrence,
    ActivityNode_isReadyEntryEventOccurrence,
    ControlNode_fire_controlNodeEntryEventOccurrence,
    ControlNode_isReady_ControlNodeExitEventOccurrence,
    ControlNode_isReady_ControlNodeEntryEventOccurrence,
    ActivityEdge_hasOfferExitEventOccurrence,
    ActivityEdge_hasOfferEntryEventOccurrence,
    ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
    ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
    ActivityEdge_sendOfferExitEventOccurrence,
    ActivityEdge_sendOfferEntryEventOccurrence,
    ActivityNode_isRunningExitEventOccurrence,
    ActivityNode_isRunningEntryEventOccurrence,
    ActivityNode_run_activityNodeExitEventOccurrence,
    ActivityNode_hasOffersExitEventOccurrence,
    ActivityNode_run_activityNodeEntryEventOccurrence,
    ActivityNode_hasOffersEntryEventOccurrence,
    ActivityNode_removeTokenExitEventOccurrence,
    ActivityNode_removeTokenEntryEventOccurrence,
    ActivityNode_addTokensExitEventOccurrence,
    ActivityNode_addTokensEntryEventOccurrence,
    ActivityNode_takeOfferedTokensExitEventOccurrence,
    ActivityNode_takeOfferedTokensEntryEventOccurrence,
    ActivityNode_sendOffersExitEventOccurrence,
    ActivityNode_sendOffersEntryEventOccurrence,
    ActivityNode_terminate_activityNodeExitEventOccurrence,
    ActivityNode_terminate_activityNodeEntryEventOccurrence,
    Activity_runNodesExitEventOccurrence,
    Activity_runNodesEntryEventOccurrence,
    Activity_runExitEventOccurrence,
    Activity_runEntryEventOccurrence,
    Activity_initializeExitEventOccurrence,
    Activity_initializeEntryEventOccurrence,
    Activity_fireNodeExitEventOccurrence,
    Activity_fireNodeEntryEventOccurrence,
    Activity_getInitialNodeExitEventOccurrence,
    Activity_getInitialNodeEntryEventOccurrence,
    Activity_terminateExitEventOccurrence,
    Activity_terminateEntryEventOccurrence,
    Activity_selectNextNodeExitEventOccurrence,
    Activity_selectNextNodeEntryEventOccurrence,
    Activity_getEnabledNodesExitEventOccurrence,
    Activity_getEnabledNodesEntryEventOccurrence,
    Activity_fireInitialNodeExitEventOccurrence,
    ActivityNode_heldTokens_State,
    Activity_fireInitialNodeEntryEventOccurrence,
    ActivityNode_running_State,
    Activity_mainExitEventOccurrence,
    Activity_mainEntryEventOccurrence,
    trace_Events_Events,
    Events_trace_GlobalState,
    trace_Events_EventOccurrence,
    trace_IntegerCalculationExpression,
    trace_BooleanUnaryExpression,
    trace_IntegerComparisonExpression,
    trace_BooleanValue,
    trace_IntegerValue,
    trace_StringValue,
    trace_BooleanBinaryExpression,
    Trace_executedNodes_State,
    Activity_trace_State,
    trace_Trace,
    Offer_offeredTokens_State,
    Variable_currentValue_State,
    ActivityEdge_offers_State,
    ForkedToken_baseTokenIsWithdrawn_State,
    ForkedToken_baseToken_State,
    ForkedToken_remainingOffersCount_State,
    Input_inputValues_State,
    Token_holder_State,
    InputValue_variable_State,
    InputValue_value_State,
    EventOccurrence,
    trace_Events_ActivityNode_isReadyEntryEventOccurrence,
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
    trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
    trace_Events_ControlNode_fire_controlNodeExitEventOccurrence,
    trace_Events_ActivityNode_isRunningExitEventOccurrence,
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
    trace_Events_Activity_fireInitialNodeExitEventOccurrence,
    trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
    trace_Events_ActivityNode_removeTokenExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
    trace_Events_Activity_fireNodeEntryEventOccurrence,
    trace_Events_Action_isReady_actionExitEventOccurrence,
    trace_Events_ForkNode_fire_forkNodeExitEventOccurrence,
    trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
    trace_Events_Activity_runNodesExitEventOccurrence,
    trace_Events_InitialNode_fire_initialNodeExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence,
    trace_Events_ActivityNode_isReadyExitEventOccurrence,
    trace_Events_Activity_mainEntryEventOccurrence,
    trace_Events_ActivityNode_sendOffersEntryEventOccurrence,
    trace_Events_Action_sendOffers_actionEntryEventOccurrence,
    trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence,
    trace_Events_Activity_fireNodeExitEventOccurrence,
    trace_Events_ActivityNode_addTokensExitEventOccurrence,
    trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
    trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence,
    trace_Events_Activity_runNodesEntryEventOccurrence,
    trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence,
    trace_Events_ActivityNode_hasOffersExitEventOccurrence,
    trace_Events_Activity_selectNextNodeEntryEventOccurrence,
    trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
    trace_Events_Activity_getEnabledNodesExitEventOccurrence,
    trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence,
    trace_Events_ActivityNode_removeTokenEntryEventOccurrence,
    trace_Events_Activity_terminateEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
    trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence,
    trace_Events_Token_withdrawExitEventOccurrence,
    trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
    trace_Events_Offer_hasTokensEntryEventOccurrence,
    trace_Events_Activity_runExitEventOccurrence,
    trace_Events_Activity_getInitialNodeExitEventOccurrence,
    trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence,
    trace_Events_Activity_initializeEntryEventOccurrence,
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
    trace_Events_ActivityNode_hasOffersEntryEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
    trace_Events_ActivityEdge_hasOfferEntryEventOccurrence,
    trace_Events_Activity_fireInitialNodeEntryEventOccurrence,
    trace_Events_Action_fire_actionEntryEventOccurrence,
    trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
    trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence,
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
    trace_Events_Activity_mainExitEventOccurrence,
    trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence,
    trace_Events_Activity_initializeExitEventOccurrence,
    trace_Events_ActivityNode_sendOffersExitEventOccurrence,
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
    trace_Events_Token_transferExitEventOccurrence,
    trace_Events_Activity_getEnabledNodesEntryEventOccurrence,
    trace_Events_ActivityEdge_hasOfferExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
    trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
    trace_Events_Token_transferEntryEventOccurrence,
    trace_Events_Action_sendOffers_actionExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
    trace_Events_ActivityNode_run_activityNodeExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
    trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence,
    trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
    trace_Events_Activity_runEntryEventOccurrence,
    trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence,
    trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence,
    trace_Events_Token_isWithdrawnEntryEventOccurrence,
    trace_Events_Activity_getInitialNodeEntryEventOccurrence,
    trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
    trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
    trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence,
    trace_Events_Token_isWithdrawnExitEventOccurrence,
    trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
    trace_Events_Action_isReady_actionEntryEventOccurrence,
    trace_Events_Activity_terminateExitEventOccurrence,
    trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
    trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
    trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence,
    trace_Events_ActivityNode_addTokensEntryEventOccurrence,
    trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
    trace_Events_Action_fire_actionExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
    trace_Events_ActivityEdge_sendOfferEntryEventOccurrence,
    trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence,
    trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
    trace_Events_Offer_hasTokensExitEventOccurrence,
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
    trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence,
    trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence,
    trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
    trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
    trace_Events_Token_withdrawEntryEventOccurrence,
    trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence,
    trace_Events_ActivityNode_isRunningEntryEventOccurrence,
    trace_Events_ActivityEdge_sendOfferExitEventOccurrence,
    trace_Events_Activity_selectNextNodeExitEventOccurrence,
    trace_StaticObjectsPools,
    TracedObjects,
    Events,
    trace_GlobalState,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_events_trace_value_is_not_abstract():
    assert not inspect.isabstract(Events_trace_Value)


def test_events_trace_value_constructor_exists():
    assert callable(Events_trace_Value.__init__)


def test_events_trace_value_constructor_args():
    sig = inspect.signature(Events_trace_Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedIntegerVariable)


def test_activitydiagram_tracedintegervariable_constructor_exists():
    assert callable(activitydiagram_TracedIntegerVariable.__init__)


def test_activitydiagram_tracedintegervariable_constructor_args():
    sig = inspect.signature(activitydiagram_TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedDecisionNode)


def test_activitydiagram_traceddecisionnode_constructor_exists():
    assert callable(activitydiagram_TracedDecisionNode.__init__)


def test_activitydiagram_traceddecisionnode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedMergeNode)


def test_activitydiagram_tracedmergenode_constructor_exists():
    assert callable(activitydiagram_TracedMergeNode.__init__)


def test_activitydiagram_tracedmergenode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedInitialNode)


def test_activitydiagram_tracedinitialnode_constructor_exists():
    assert callable(activitydiagram_TracedInitialNode.__init__)


def test_activitydiagram_tracedinitialnode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedForkNode)


def test_activitydiagram_tracedforknode_constructor_exists():
    assert callable(activitydiagram_TracedForkNode.__init__)


def test_activitydiagram_tracedforknode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedActivityFinalNode)


def test_activitydiagram_tracedactivityfinalnode_constructor_exists():
    assert callable(activitydiagram_TracedActivityFinalNode.__init__)


def test_activitydiagram_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedAction)


def test_activitydiagram_tracedaction_constructor_exists():
    assert callable(activitydiagram_TracedAction.__init__)


def test_activitydiagram_tracedaction_constructor_args():
    sig = inspect.signature(activitydiagram_TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedOpaqueAction)


def test_activitydiagram_tracedopaqueaction_constructor_exists():
    assert callable(activitydiagram_TracedOpaqueAction.__init__)


def test_activitydiagram_tracedopaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram_TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedToken)


def test_activitydiagramconfiguration_tracedtoken_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedToken.__init__)


def test_activitydiagramconfiguration_tracedtoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedControlNode)


def test_activitydiagram_tracedcontrolnode_constructor_exists():
    assert callable(activitydiagram_TracedControlNode.__init__)


def test_activitydiagram_tracedcontrolnode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedActivityEdge)


def test_activitydiagram_tracedactivityedge_constructor_exists():
    assert callable(activitydiagram_TracedActivityEdge.__init__)


def test_activitydiagram_tracedactivityedge_constructor_args():
    sig = inspect.signature(activitydiagram_TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedActivityNode)


def test_activitydiagram_tracedactivitynode_constructor_exists():
    assert callable(activitydiagram_TracedActivityNode.__init__)


def test_activitydiagram_tracedactivitynode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedoffer_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedOffer)


def test_trace_activitydiagramconfiguration_tracedoffer_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedOffer.__init__)


def test_trace_activitydiagramconfiguration_tracedoffer_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedinput_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedInput)


def test_trace_activitydiagramconfiguration_tracedinput_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedInput.__init__)


def test_trace_activitydiagramconfiguration_tracedinput_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(TracedToken)


def test_tracedtoken_constructor_exists():
    assert callable(TracedToken.__init__)


def test_tracedtoken_constructor_args():
    sig = inspect.signature(TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedForkedToken)


def test_trace_activitydiagramconfiguration_tracedforkedtoken_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedForkedToken.__init__)


def test_trace_activitydiagramconfiguration_tracedforkedtoken_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedControlToken)


def test_trace_activitydiagramconfiguration_tracedcontroltoken_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedControlToken.__init__)


def test_trace_activitydiagramconfiguration_tracedcontroltoken_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedToken)


def test_trace_activitydiagramconfiguration_tracedtoken_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedToken.__init__)


def test_trace_activitydiagramconfiguration_tracedtoken_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedInputValue)


def test_trace_activitydiagramconfiguration_tracedinputvalue_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedInputValue.__init__)


def test_trace_activitydiagramconfiguration_tracedinputvalue_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_DecisionNode)


def test_activitydiagram_trace_decisionnode_constructor_exists():
    assert callable(activitydiagram_trace_DecisionNode.__init__)


def test_activitydiagram_trace_decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_JoinNode)


def test_activitydiagram_trace_joinnode_constructor_exists():
    assert callable(activitydiagram_trace_JoinNode.__init__)


def test_activitydiagram_trace_joinnode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_OpaqueAction)


def test_activitydiagram_trace_opaqueaction_constructor_exists():
    assert callable(activitydiagram_trace_OpaqueAction.__init__)


def test_activitydiagram_trace_opaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram_trace_OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagramconfiguration_tracedtrace_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagramConfiguration_TracedTrace)


def test_trace_activitydiagramconfiguration_tracedtrace_constructor_exists():
    assert callable(trace_activitydiagramConfiguration_TracedTrace.__init__)


def test_trace_activitydiagramconfiguration_tracedtrace_constructor_args():
    sig = inspect.signature(trace_activitydiagramConfiguration_TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_InitialNode)


def test_activitydiagram_trace_initialnode_constructor_exists():
    assert callable(activitydiagram_trace_InitialNode.__init__)


def test_activitydiagram_trace_initialnode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_ForkNode)


def test_activitydiagram_trace_forknode_constructor_exists():
    assert callable(activitydiagram_trace_ForkNode.__init__)


def test_activitydiagram_trace_forknode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_ActivityFinalNode)


def test_activitydiagram_trace_activityfinalnode_constructor_exists():
    assert callable(activitydiagram_trace_ActivityFinalNode.__init__)


def test_activitydiagram_trace_activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedActivityFinalNode)


def test_trace_activitydiagram_tracedactivityfinalnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedActivityFinalNode.__init__)


def test_trace_activitydiagram_tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(TracedExecutableNode)


def test_tracedexecutablenode_constructor_exists():
    assert callable(TracedExecutableNode.__init__)


def test_tracedexecutablenode_constructor_args():
    sig = inspect.signature(TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_expression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_Expression)


def test_activitydiagram_trace_expression_constructor_exists():
    assert callable(activitydiagram_trace_Expression.__init__)


def test_activitydiagram_trace_expression_constructor_args():
    sig = inspect.signature(activitydiagram_trace_Expression.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedaction_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedAction)


def test_trace_activitydiagram_tracedaction_constructor_exists():
    assert callable(trace_activitydiagram_TracedAction.__init__)


def test_trace_activitydiagram_tracedaction_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedOpaqueAction)


def test_trace_activitydiagram_tracedopaqueaction_constructor_exists():
    assert callable(trace_activitydiagram_TracedOpaqueAction.__init__)


def test_trace_activitydiagram_tracedopaqueaction_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_stringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_StringVariable)


def test_activitydiagram_trace_stringvariable_constructor_exists():
    assert callable(activitydiagram_trace_StringVariable.__init__)


def test_activitydiagram_trace_stringvariable_constructor_args():
    sig = inspect.signature(activitydiagram_trace_StringVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_Activity)


def test_activitydiagram_trace_activity_constructor_exists():
    assert callable(activitydiagram_trace_Activity.__init__)


def test_activitydiagram_trace_activity_constructor_args():
    sig = inspect.signature(activitydiagram_trace_Activity.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedActivity)


def test_trace_activitydiagram_tracedactivity_constructor_exists():
    assert callable(trace_activitydiagram_TracedActivity.__init__)


def test_trace_activitydiagram_tracedactivity_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedActivityNode)


def test_trace_activitydiagram_tracedactivitynode_constructor_exists():
    assert callable(trace_activitydiagram_TracedActivityNode.__init__)


def test_trace_activitydiagram_tracedactivitynode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedActivityEdge)


def test_trace_activitydiagram_tracedactivityedge_constructor_exists():
    assert callable(trace_activitydiagram_TracedActivityEdge.__init__)


def test_trace_activitydiagram_tracedactivityedge_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_integervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_IntegerVariable)


def test_activitydiagram_trace_integervariable_constructor_exists():
    assert callable(activitydiagram_trace_IntegerVariable.__init__)


def test_activitydiagram_trace_integervariable_constructor_args():
    sig = inspect.signature(activitydiagram_trace_IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNode)


def test_tracedactivitynode_constructor_exists():
    assert callable(TracedActivityNode.__init__)


def test_tracedactivitynode_constructor_args():
    sig = inspect.signature(TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedControlNode)


def test_trace_activitydiagram_tracedcontrolnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedControlNode.__init__)


def test_trace_activitydiagram_tracedcontrolnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedExecutableNode)


def test_trace_activitydiagram_tracedexecutablenode_constructor_exists():
    assert callable(trace_activitydiagram_TracedExecutableNode.__init__)


def test_trace_activitydiagram_tracedexecutablenode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_BooleanVariable)


def test_activitydiagram_trace_booleanvariable_constructor_exists():
    assert callable(activitydiagram_trace_BooleanVariable.__init__)


def test_activitydiagram_trace_booleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram_trace_BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(TracedVariable)


def test_tracedvariable_constructor_exists():
    assert callable(TracedVariable.__init__)


def test_tracedvariable_constructor_args():
    sig = inspect.signature(TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedStringVariable)


def test_trace_activitydiagram_tracedstringvariable_constructor_exists():
    assert callable(trace_activitydiagram_TracedStringVariable.__init__)


def test_trace_activitydiagram_tracedstringvariable_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedIntegerVariable)


def test_trace_activitydiagram_tracedintegervariable_constructor_exists():
    assert callable(trace_activitydiagram_TracedIntegerVariable.__init__)


def test_trace_activitydiagram_tracedintegervariable_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedBooleanVariable)


def test_trace_activitydiagram_tracedbooleanvariable_constructor_exists():
    assert callable(trace_activitydiagram_TracedBooleanVariable.__init__)


def test_trace_activitydiagram_tracedbooleanvariable_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_MergeNode)


def test_activitydiagram_trace_mergenode_constructor_exists():
    assert callable(activitydiagram_trace_MergeNode.__init__)


def test_activitydiagram_trace_mergenode_constructor_args():
    sig = inspect.signature(activitydiagram_trace_MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedforknode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedForkNode)


def test_trace_activitydiagram_tracedforknode_constructor_exists():
    assert callable(trace_activitydiagram_TracedForkNode.__init__)


def test_trace_activitydiagram_tracedforknode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedInitialNode)


def test_trace_activitydiagram_tracedinitialnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedInitialNode.__init__)


def test_trace_activitydiagram_tracedinitialnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedJoinNode)


def test_trace_activitydiagram_tracedjoinnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedJoinNode.__init__)


def test_trace_activitydiagram_tracedjoinnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedDecisionNode)


def test_trace_activitydiagram_traceddecisionnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedDecisionNode.__init__)


def test_trace_activitydiagram_traceddecisionnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedFinalNode)


def test_trace_activitydiagram_tracedfinalnode_constructor_exists():
    assert callable(trace_activitydiagram_TracedFinalNode.__init__)


def test_trace_activitydiagram_tracedfinalnode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedMergeNode)


def test_trace_activitydiagram_tracedmergenode_constructor_exists():
    assert callable(trace_activitydiagram_TracedMergeNode.__init__)


def test_trace_activitydiagram_tracedmergenode_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_controlflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_ControlFlow)


def test_activitydiagram_trace_controlflow_constructor_exists():
    assert callable(activitydiagram_trace_ControlFlow.__init__)


def test_activitydiagram_trace_controlflow_constructor_args():
    sig = inspect.signature(activitydiagram_trace_ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(TracedActivityEdge)


def test_tracedactivityedge_constructor_exists():
    assert callable(TracedActivityEdge.__init__)


def test_tracedactivityedge_constructor_args():
    sig = inspect.signature(TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedControlFlow)


def test_trace_activitydiagram_tracedcontrolflow_constructor_exists():
    assert callable(trace_activitydiagram_TracedControlFlow.__init__)


def test_trace_activitydiagram_tracedcontrolflow_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedJoinNode)


def test_activitydiagram_tracedjoinnode_constructor_exists():
    assert callable(activitydiagram_TracedJoinNode.__init__)


def test_activitydiagram_tracedjoinnode_constructor_args():
    sig = inspect.signature(activitydiagram_TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_trace_value_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_trace_Value)


def test_activitydiagram_trace_value_constructor_exists():
    assert callable(activitydiagram_trace_Value.__init__)


def test_activitydiagram_trace_value_constructor_args():
    sig = inspect.signature(activitydiagram_trace_Value.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedVariable)


def test_trace_activitydiagram_tracedvariable_constructor_exists():
    assert callable(trace_activitydiagram_TracedVariable.__init__)


def test_trace_activitydiagram_tracedvariable_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace_activitydiagram_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(trace_activitydiagram_TracedNamedElement)


def test_trace_activitydiagram_tracednamedelement_constructor_exists():
    assert callable(trace_activitydiagram_TracedNamedElement.__init__)


def test_trace_activitydiagram_tracednamedelement_constructor_args():
    sig = inspect.signature(trace_activitydiagram_TracedNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace_activitydiagram_tracednamedelement_has_name():
    assert hasattr(trace_activitydiagram_TracedNamedElement, "name")
    descriptor = None
    for klass in trace_activitydiagram_TracedNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagramconfiguration_tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedControlToken)


def test_activitydiagramconfiguration_tracedcontroltoken_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedControlToken.__init__)


def test_activitydiagramconfiguration_tracedcontroltoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedControlFlow)


def test_activitydiagram_tracedcontrolflow_constructor_exists():
    assert callable(activitydiagram_TracedControlFlow.__init__)


def test_activitydiagram_tracedcontrolflow_constructor_args():
    sig = inspect.signature(activitydiagram_TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_trace_traced_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(trace_Traced_TracedObjects)


def test_trace_traced_tracedobjects_constructor_exists():
    assert callable(trace_Traced_TracedObjects.__init__)


def test_trace_traced_tracedobjects_constructor_args():
    sig = inspect.signature(trace_Traced_TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration_tracedtrace_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedTrace)


def test_activitydiagramconfiguration_tracedtrace_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedTrace.__init__)


def test_activitydiagramconfiguration_tracedtrace_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_activity_trace_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Activity_trace_State)


def test_trace_states_activity_trace_state_constructor_exists():
    assert callable(trace_States_Activity_trace_State.__init__)


def test_trace_states_activity_trace_state_constructor_args():
    sig = inspect.signature(trace_States_Activity_trace_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_activitynode_heldtokens_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ActivityNode_heldTokens_State)


def test_trace_states_activitynode_heldtokens_state_constructor_exists():
    assert callable(trace_States_ActivityNode_heldTokens_State.__init__)


def test_trace_states_activitynode_heldtokens_state_constructor_args():
    sig = inspect.signature(trace_States_ActivityNode_heldTokens_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_activitynode_running_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ActivityNode_running_State)


def test_trace_states_activitynode_running_state_constructor_exists():
    assert callable(trace_States_ActivityNode_running_State.__init__)


def test_trace_states_activitynode_running_state_constructor_args():
    sig = inspect.signature(trace_States_ActivityNode_running_State.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_trace_states_activitynode_running_state_has_running():
    assert hasattr(trace_States_ActivityNode_running_State, "running")
    descriptor = None
    for klass in trace_States_ActivityNode_running_State.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_trace_states_offer_offeredtokens_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Offer_offeredTokens_State)


def test_trace_states_offer_offeredtokens_state_constructor_exists():
    assert callable(trace_States_Offer_offeredTokens_State.__init__)


def test_trace_states_offer_offeredtokens_state_constructor_args():
    sig = inspect.signature(trace_States_Offer_offeredTokens_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_variable_currentvalue_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Variable_currentValue_State)


def test_trace_states_variable_currentvalue_state_constructor_exists():
    assert callable(trace_States_Variable_currentValue_State.__init__)


def test_trace_states_variable_currentvalue_state_constructor_args():
    sig = inspect.signature(trace_States_Variable_currentValue_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_trace_executednodes_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Trace_executedNodes_State)


def test_trace_states_trace_executednodes_state_constructor_exists():
    assert callable(trace_States_Trace_executedNodes_State.__init__)


def test_trace_states_trace_executednodes_state_constructor_args():
    sig = inspect.signature(trace_States_Trace_executedNodes_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_forkedtoken_basetokeniswithdrawn_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ForkedToken_baseTokenIsWithdrawn_State)


def test_trace_states_forkedtoken_basetokeniswithdrawn_state_constructor_exists():
    assert callable(trace_States_ForkedToken_baseTokenIsWithdrawn_State.__init__)


def test_trace_states_forkedtoken_basetokeniswithdrawn_state_constructor_args():
    sig = inspect.signature(trace_States_ForkedToken_baseTokenIsWithdrawn_State.__init__)
    params = list(sig.parameters.keys())
    assert "baseTokenIsWithdrawn" in params, "Missing parameter 'baseTokenIsWithdrawn'"

def test_trace_states_forkedtoken_basetokeniswithdrawn_state_has_baseTokenIsWithdrawn():
    assert hasattr(trace_States_ForkedToken_baseTokenIsWithdrawn_State, "baseTokenIsWithdrawn")
    descriptor = None
    for klass in trace_States_ForkedToken_baseTokenIsWithdrawn_State.__mro__:
        if "baseTokenIsWithdrawn" in klass.__dict__:
            descriptor = klass.__dict__["baseTokenIsWithdrawn"]
            break
    assert isinstance(descriptor, property)



def test_trace_states_forkedtoken_basetoken_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ForkedToken_baseToken_State)


def test_trace_states_forkedtoken_basetoken_state_constructor_exists():
    assert callable(trace_States_ForkedToken_baseToken_State.__init__)


def test_trace_states_forkedtoken_basetoken_state_constructor_args():
    sig = inspect.signature(trace_States_ForkedToken_baseToken_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_forkedtoken_remainingofferscount_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ForkedToken_remainingOffersCount_State)


def test_trace_states_forkedtoken_remainingofferscount_state_constructor_exists():
    assert callable(trace_States_ForkedToken_remainingOffersCount_State.__init__)


def test_trace_states_forkedtoken_remainingofferscount_state_constructor_args():
    sig = inspect.signature(trace_States_ForkedToken_remainingOffersCount_State.__init__)
    params = list(sig.parameters.keys())
    assert "remainingOffersCount" in params, "Missing parameter 'remainingOffersCount'"

def test_trace_states_forkedtoken_remainingofferscount_state_has_remainingOffersCount():
    assert hasattr(trace_States_ForkedToken_remainingOffersCount_State, "remainingOffersCount")
    descriptor = None
    for klass in trace_States_ForkedToken_remainingOffersCount_State.__mro__:
        if "remainingOffersCount" in klass.__dict__:
            descriptor = klass.__dict__["remainingOffersCount"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagramconfiguration_tracedinput_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedInput)


def test_activitydiagramconfiguration_tracedinput_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedInput.__init__)


def test_activitydiagramconfiguration_tracedinput_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_input_inputvalues_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Input_inputValues_State)


def test_trace_states_input_inputvalues_state_constructor_exists():
    assert callable(trace_States_Input_inputValues_State.__init__)


def test_trace_states_input_inputvalues_state_constructor_args():
    sig = inspect.signature(trace_States_Input_inputValues_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_token_holder_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_Token_holder_State)


def test_trace_states_token_holder_state_constructor_exists():
    assert callable(trace_States_Token_holder_State.__init__)


def test_trace_states_token_holder_state_constructor_args():
    sig = inspect.signature(trace_States_Token_holder_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_activityedge_offers_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_ActivityEdge_offers_State)


def test_trace_states_activityedge_offers_state_constructor_exists():
    assert callable(trace_States_ActivityEdge_offers_State.__init__)


def test_trace_states_activityedge_offers_state_constructor_args():
    sig = inspect.signature(trace_States_ActivityEdge_offers_State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration_tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedInputValue)


def test_activitydiagramconfiguration_tracedinputvalue_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedInputValue.__init__)


def test_activitydiagramconfiguration_tracedinputvalue_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_states_trace_value_is_not_abstract():
    assert not inspect.isabstract(States_trace_Value)


def test_states_trace_value_constructor_exists():
    assert callable(States_trace_Value.__init__)


def test_states_trace_value_constructor_args():
    sig = inspect.signature(States_trace_Value.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_inputvalue_value_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_InputValue_value_State)


def test_trace_states_inputvalue_value_state_constructor_exists():
    assert callable(trace_States_InputValue_value_State.__init__)


def test_trace_states_inputvalue_value_state_constructor_args():
    sig = inspect.signature(trace_States_InputValue_value_State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration_tracedoffer_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedOffer)


def test_activitydiagramconfiguration_tracedoffer_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedOffer.__init__)


def test_activitydiagramconfiguration_tracedoffer_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration_tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration_TracedForkedToken)


def test_activitydiagramconfiguration_tracedforkedtoken_constructor_exists():
    assert callable(activitydiagramConfiguration_TracedForkedToken.__init__)


def test_activitydiagramconfiguration_tracedforkedtoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration_TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedVariable)


def test_activitydiagram_tracedvariable_constructor_exists():
    assert callable(activitydiagram_TracedVariable.__init__)


def test_activitydiagram_tracedvariable_constructor_args():
    sig = inspect.signature(activitydiagram_TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace_states_inputvalue_variable_state_is_not_abstract():
    assert not inspect.isabstract(trace_States_InputValue_variable_State)


def test_trace_states_inputvalue_variable_state_constructor_exists():
    assert callable(trace_States_InputValue_variable_State.__init__)


def test_trace_states_inputvalue_variable_state_constructor_args():
    sig = inspect.signature(trace_States_InputValue_variable_State.__init__)
    params = list(sig.parameters.keys())



def test_states_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(States_trace_GlobalState)


def test_states_trace_globalstate_constructor_exists():
    assert callable(States_trace_GlobalState.__init__)


def test_states_trace_globalstate_constructor_args():
    sig = inspect.signature(States_trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events_trace_BooleanBinaryExpression)


def test_events_trace_booleanbinaryexpression_constructor_exists():
    assert callable(Events_trace_BooleanBinaryExpression.__init__)


def test_events_trace_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(Events_trace_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events_trace_BooleanUnaryExpression)


def test_events_trace_booleanunaryexpression_constructor_exists():
    assert callable(Events_trace_BooleanUnaryExpression.__init__)


def test_events_trace_booleanunaryexpression_constructor_args():
    sig = inspect.signature(Events_trace_BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(Events_trace_IntegerComparisonExpression)


def test_events_trace_integercomparisonexpression_constructor_exists():
    assert callable(Events_trace_IntegerComparisonExpression.__init__)


def test_events_trace_integercomparisonexpression_constructor_args():
    sig = inspect.signature(Events_trace_IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_integerexpression_is_not_abstract():
    assert not inspect.isabstract(Events_trace_IntegerExpression)


def test_events_trace_integerexpression_constructor_exists():
    assert callable(Events_trace_IntegerExpression.__init__)


def test_events_trace_integerexpression_constructor_args():
    sig = inspect.signature(Events_trace_IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedBooleanVariable)


def test_activitydiagram_tracedbooleanvariable_constructor_exists():
    assert callable(activitydiagram_TracedBooleanVariable.__init__)


def test_activitydiagram_tracedbooleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram_TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(Events_trace_IntegerCalculationExpression)


def test_events_trace_integercalculationexpression_constructor_exists():
    assert callable(Events_trace_IntegerCalculationExpression.__init__)


def test_events_trace_integercalculationexpression_constructor_args():
    sig = inspect.signature(Events_trace_IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedStringVariable)


def test_activitydiagram_tracedstringvariable_constructor_exists():
    assert callable(activitydiagram_TracedStringVariable.__init__)


def test_activitydiagram_tracedstringvariable_constructor_args():
    sig = inspect.signature(activitydiagram_TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_offer_hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Offer_hasTokensExitEventOccurrence)


def test_offer_hastokensexiteventoccurrence_constructor_exists():
    assert callable(Offer_hasTokensExitEventOccurrence.__init__)


def test_offer_hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(Offer_hasTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_eobject_is_not_abstract():
    assert not inspect.isabstract(Events_trace_EObject)


def test_events_trace_eobject_constructor_exists():
    assert callable(Events_trace_EObject.__init__)


def test_events_trace_eobject_constructor_args():
    sig = inspect.signature(Events_trace_EObject.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram_tracedactivity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram_TracedActivity)


def test_activitydiagram_tracedactivity_constructor_exists():
    assert callable(activitydiagram_TracedActivity.__init__)


def test_activitydiagram_tracedactivity_constructor_args():
    sig = inspect.signature(activitydiagram_TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_token_iswithdrawnexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_isWithdrawnExitEventOccurrence)


def test_token_iswithdrawnexiteventoccurrence_constructor_exists():
    assert callable(Token_isWithdrawnExitEventOccurrence.__init__)


def test_token_iswithdrawnexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token_isWithdrawnExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token_iswithdrawnentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_isWithdrawnEntryEventOccurrence)


def test_token_iswithdrawnentryeventoccurrence_constructor_exists():
    assert callable(Token_isWithdrawnEntryEventOccurrence.__init__)


def test_token_iswithdrawnentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token_isWithdrawnEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_evaluateorexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_evaluateORExitEventOccurrence)


def test_booleanbinaryexpression_evaluateorexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_evaluateORExitEventOccurrence.__init__)


def test_booleanbinaryexpression_evaluateorexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_evaluateORExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_offer_hastokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Offer_hasTokensEntryEventOccurrence)


def test_offer_hastokensentryeventoccurrence_constructor_exists():
    assert callable(Offer_hasTokensEntryEventOccurrence.__init__)


def test_offer_hastokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(Offer_hasTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_withdraw_forkedtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_withdraw_forkedTokenExitEventOccurrence)


def test_forkedtoken_withdraw_forkedtokenexiteventoccurrence_constructor_exists():
    assert callable(ForkedToken_withdraw_forkedTokenExitEventOccurrence.__init__)


def test_forkedtoken_withdraw_forkedtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(ForkedToken_withdraw_forkedTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_withdraw_forkedtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_withdraw_forkedTokenEntryEventOccurrence)


def test_forkedtoken_withdraw_forkedtokenentryeventoccurrence_constructor_exists():
    assert callable(ForkedToken_withdraw_forkedTokenEntryEventOccurrence.__init__)


def test_forkedtoken_withdraw_forkedtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(ForkedToken_withdraw_forkedTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token_withdrawexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_withdrawExitEventOccurrence)


def test_token_withdrawexiteventoccurrence_constructor_exists():
    assert callable(Token_withdrawExitEventOccurrence.__init__)


def test_token_withdrawexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token_withdrawExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token_withdrawentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_withdrawEntryEventOccurrence)


def test_token_withdrawentryeventoccurrence_constructor_exists():
    assert callable(Token_withdrawEntryEventOccurrence.__init__)


def test_token_withdrawentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token_withdrawEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token_transferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_transferExitEventOccurrence)


def test_token_transferexiteventoccurrence_constructor_exists():
    assert callable(Token_transferExitEventOccurrence.__init__)


def test_token_transferexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token_transferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token_transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token_transferEntryEventOccurrence)


def test_token_transferentryeventoccurrence_constructor_exists():
    assert callable(Token_transferEntryEventOccurrence.__init__)


def test_token_transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token_transferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression_evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)


def test_booleanunaryexpression_evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression_evaluateNOTEntryEventOccurrence.__init__)


def test_booleanunaryexpression_evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression_evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)


def test_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence.__init__)


def test_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_evaluateorentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_evaluateOREntryEventOccurrence)


def test_booleanbinaryexpression_evaluateorentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_evaluateOREntryEventOccurrence.__init__)


def test_booleanbinaryexpression_evaluateorentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_evaluateOREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_evaluateandexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_evaluateANDExitEventOccurrence)


def test_booleanbinaryexpression_evaluateandexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_evaluateANDExitEventOccurrence.__init__)


def test_booleanbinaryexpression_evaluateandexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_evaluateANDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_evaluateandentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_evaluateANDEntryEventOccurrence)


def test_booleanbinaryexpression_evaluateandentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_evaluateANDEntryEventOccurrence.__init__)


def test_booleanbinaryexpression_evaluateandentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_evaluateANDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)


def test_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence.__init__)


def test_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)


def test_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence.__init__)


def test_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression_evaluatenotexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression_evaluateNOTExitEventOccurrence)


def test_booleanunaryexpression_evaluatenotexiteventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression_evaluateNOTExitEventOccurrence.__init__)


def test_booleanunaryexpression_evaluatenotexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression_evaluateNOTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)


def test_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)


def test_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)


def test_integercomparisonexpression_evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence.__init__)


def test_integercomparisonexpression_evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)


def test_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence.__init__)


def test_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluategreaterexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)


def test_integercomparisonexpression_evaluategreaterexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateGREATERExitEventOccurrence.__init__)


def test_integercomparisonexpression_evaluategreaterexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateGREATERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluategreaterentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)


def test_integercomparisonexpression_evaluategreaterentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence.__init__)


def test_integercomparisonexpression_evaluategreaterentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)


def test_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)


def test_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluateequalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)


def test_integercomparisonexpression_evaluateequalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression_evaluateequalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluateequalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)


def test_integercomparisonexpression_evaluateequalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression_evaluateequalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)


def test_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence.__init__)


def test_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)


def test_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence.__init__)


def test_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_getoperandcurrentvaluesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression_getOperandCurrentValuesExitEventOccurrence)


def test_integerexpression_getoperandcurrentvaluesexiteventoccurrence_constructor_exists():
    assert callable(IntegerExpression_getOperandCurrentValuesExitEventOccurrence.__init__)


def test_integerexpression_getoperandcurrentvaluesexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerExpression_getOperandCurrentValuesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_evaluatesmallerentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)


def test_integercomparisonexpression_evaluatesmallerentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence.__init__)


def test_integercomparisonexpression_evaluatesmallerentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)


def test_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence.__init__)


def test_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)


def test_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence.__init__)


def test_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_evaluatesubtractexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)


def test_integercalculationexpression_evaluatesubtractexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence.__init__)


def test_integercalculationexpression_evaluatesubtractexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_evaluatesubtractentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)


def test_integercalculationexpression_evaluatesubtractentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence.__init__)


def test_integercalculationexpression_evaluatesubtractentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_evaluateaddexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_evaluateADDExitEventOccurrence)


def test_integercalculationexpression_evaluateaddexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_evaluateADDExitEventOccurrence.__init__)


def test_integercalculationexpression_evaluateaddexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_evaluateADDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)


def test_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_constructor_exists():
    assert callable(StringVariable_setCurrentValue_stringVariableEntryEventOccurrence.__init__)


def test_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable_setCurrentValue_stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression_evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression_evaluateADDEntryEventOccurrence)


def test_integercalculationexpression_evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression_evaluateADDEntryEventOccurrence.__init__)


def test_integercalculationexpression_evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression_evaluateADDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)


def test_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_constructor_exists():
    assert callable(IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence.__init__)


def test_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression_getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)


def test_integerexpression_getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(IntegerExpression_getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_integerexpression_getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerExpression_getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)


def test_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_constructor_exists():
    assert callable(BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence.__init__)


def test_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)


def test_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_constructor_exists():
    assert callable(BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence.__init__)


def test_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)


def test_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_constructor_exists():
    assert callable(BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence.__init__)


def test_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)


def test_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_constructor_exists():
    assert callable(BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence.__init__)


def test_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)


def test_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_constructor_exists():
    assert callable(StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence.__init__)


def test_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)


def test_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_constructor_exists():
    assert callable(StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence.__init__)


def test_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable_setCurrentValue_stringVariableExitEventOccurrence)


def test_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_constructor_exists():
    assert callable(StringVariable_setCurrentValue_stringVariableExitEventOccurrence.__init__)


def test_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable_setCurrentValue_stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode_fire_initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode_fire_initialNodeExitEventOccurrence)


def test_initialnode_fire_initialnodeexiteventoccurrence_constructor_exists():
    assert callable(InitialNode_fire_initialNodeExitEventOccurrence.__init__)


def test_initialnode_fire_initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode_fire_initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)


def test_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_constructor_exists():
    assert callable(IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence.__init__)


def test_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode_fire_initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode_fire_initialNodeEntryEventOccurrence)


def test_initialnode_fire_initialnodeentryeventoccurrence_constructor_exists():
    assert callable(InitialNode_fire_initialNodeEntryEventOccurrence.__init__)


def test_initialnode_fire_initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode_fire_initialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable_setcurrentvalue_integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)


def test_integervariable_setcurrentvalue_integervariableexiteventoccurrence_constructor_exists():
    assert callable(IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence.__init__)


def test_integervariable_setcurrentvalue_integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable_setcurrentvalue_integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)


def test_integervariable_setcurrentvalue_integervariableentryeventoccurrence_constructor_exists():
    assert callable(IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence.__init__)


def test_integervariable_setcurrentvalue_integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_decisionnode_fire_decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(DecisionNode_fire_decisionNodeExitEventOccurrence)


def test_decisionnode_fire_decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(DecisionNode_fire_decisionNodeExitEventOccurrence.__init__)


def test_decisionnode_fire_decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(DecisionNode_fire_decisionNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_decisionnode_fire_decisionnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(DecisionNode_fire_decisionNodeEntryEventOccurrence)


def test_decisionnode_fire_decisionnodeentryeventoccurrence_constructor_exists():
    assert callable(DecisionNode_fire_decisionNodeEntryEventOccurrence.__init__)


def test_decisionnode_fire_decisionnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(DecisionNode_fire_decisionNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_mergenode_hasoffers_mergenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(MergeNode_hasOffers_mergeNodeExitEventOccurrence)


def test_mergenode_hasoffers_mergenodeexiteventoccurrence_constructor_exists():
    assert callable(MergeNode_hasOffers_mergeNodeExitEventOccurrence.__init__)


def test_mergenode_hasoffers_mergenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(MergeNode_hasOffers_mergeNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_mergenode_hasoffers_mergenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(MergeNode_hasOffers_mergeNodeEntryEventOccurrence)


def test_mergenode_hasoffers_mergenodeentryeventoccurrence_constructor_exists():
    assert callable(MergeNode_hasOffers_mergeNodeEntryEventOccurrence.__init__)


def test_mergenode_hasoffers_mergenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(MergeNode_hasOffers_mergeNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forknode_fire_forknodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkNode_fire_forkNodeExitEventOccurrence)


def test_forknode_fire_forknodeexiteventoccurrence_constructor_exists():
    assert callable(ForkNode_fire_forkNodeExitEventOccurrence.__init__)


def test_forknode_fire_forknodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ForkNode_fire_forkNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forknode_fire_forknodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkNode_fire_forkNodeEntryEventOccurrence)


def test_forknode_fire_forknodeentryeventoccurrence_constructor_exists():
    assert callable(ForkNode_fire_forkNodeEntryEventOccurrence.__init__)


def test_forknode_fire_forknodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ForkNode_fire_forkNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)


def test_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence.__init__)


def test_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)


def test_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence.__init__)


def test_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_isready_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_isReady_actionEntryEventOccurrence)


def test_action_isready_actionentryeventoccurrence_constructor_exists():
    assert callable(Action_isReady_actionEntryEventOccurrence.__init__)


def test_action_isready_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action_isReady_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_sendoffers_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_sendOffers_actionExitEventOccurrence)


def test_action_sendoffers_actionexiteventoccurrence_constructor_exists():
    assert callable(Action_sendOffers_actionExitEventOccurrence.__init__)


def test_action_sendoffers_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action_sendOffers_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_sendoffers_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_sendOffers_actionEntryEventOccurrence)


def test_action_sendoffers_actionentryeventoccurrence_constructor_exists():
    assert callable(Action_sendOffers_actionEntryEventOccurrence.__init__)


def test_action_sendoffers_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action_sendOffers_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_fire_controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode_fire_controlNodeExitEventOccurrence)


def test_controlnode_fire_controlnodeexiteventoccurrence_constructor_exists():
    assert callable(ControlNode_fire_controlNodeExitEventOccurrence.__init__)


def test_controlnode_fire_controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode_fire_controlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode_isready_initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode_isReady_InitialNodeExitEventOccurrence)


def test_initialnode_isready_initialnodeexiteventoccurrence_constructor_exists():
    assert callable(InitialNode_isReady_InitialNodeExitEventOccurrence.__init__)


def test_initialnode_isready_initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode_isReady_InitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode_isready_initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode_isReady_InitialNodeEntryEventOccurrence)


def test_initialnode_isready_initialnodeentryeventoccurrence_constructor_exists():
    assert callable(InitialNode_isReady_InitialNodeEntryEventOccurrence.__init__)


def test_initialnode_isready_initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode_isReady_InitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_opaqueaction_doaction_opaqueactionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(OpaqueAction_doAction_opaqueActionExitEventOccurrence)


def test_opaqueaction_doaction_opaqueactionexiteventoccurrence_constructor_exists():
    assert callable(OpaqueAction_doAction_opaqueActionExitEventOccurrence.__init__)


def test_opaqueaction_doaction_opaqueactionexiteventoccurrence_constructor_args():
    sig = inspect.signature(OpaqueAction_doAction_opaqueActionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_opaqueaction_doaction_opaqueactionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(OpaqueAction_doAction_opaqueActionEntryEventOccurrence)


def test_opaqueaction_doaction_opaqueactionentryeventoccurrence_constructor_exists():
    assert callable(OpaqueAction_doAction_opaqueActionEntryEventOccurrence.__init__)


def test_opaqueaction_doaction_opaqueactionentryeventoccurrence_constructor_args():
    sig = inspect.signature(OpaqueAction_doAction_opaqueActionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_fire_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_fire_actionExitEventOccurrence)


def test_action_fire_actionexiteventoccurrence_constructor_exists():
    assert callable(Action_fire_actionExitEventOccurrence.__init__)


def test_action_fire_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action_fire_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_fire_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_fire_actionEntryEventOccurrence)


def test_action_fire_actionentryeventoccurrence_constructor_exists():
    assert callable(Action_fire_actionEntryEventOccurrence.__init__)


def test_action_fire_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action_fire_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_isReadyExitEventOccurrence)


def test_activitynode_isreadyexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_isReadyExitEventOccurrence.__init__)


def test_activitynode_isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action_isready_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action_isReady_actionExitEventOccurrence)


def test_action_isready_actionexiteventoccurrence_constructor_exists():
    assert callable(Action_isReady_actionExitEventOccurrence.__init__)


def test_action_isready_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action_isReady_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_isReadyEntryEventOccurrence)


def test_activitynode_isreadyentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_isReadyEntryEventOccurrence.__init__)


def test_activitynode_isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_isReadyEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_fire_controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode_fire_controlNodeEntryEventOccurrence)


def test_controlnode_fire_controlnodeentryeventoccurrence_constructor_exists():
    assert callable(ControlNode_fire_controlNodeEntryEventOccurrence.__init__)


def test_controlnode_fire_controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode_fire_controlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_isready_controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode_isReady_ControlNodeExitEventOccurrence)


def test_controlnode_isready_controlnodeexiteventoccurrence_constructor_exists():
    assert callable(ControlNode_isReady_ControlNodeExitEventOccurrence.__init__)


def test_controlnode_isready_controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode_isReady_ControlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode_isready_controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode_isReady_ControlNodeEntryEventOccurrence)


def test_controlnode_isready_controlnodeentryeventoccurrence_constructor_exists():
    assert callable(ControlNode_isReady_ControlNodeEntryEventOccurrence.__init__)


def test_controlnode_isready_controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode_isReady_ControlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_hasofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_hasOfferExitEventOccurrence)


def test_activityedge_hasofferexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge_hasOfferExitEventOccurrence.__init__)


def test_activityedge_hasofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_hasOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_hasofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_hasOfferEntryEventOccurrence)


def test_activityedge_hasofferentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge_hasOfferEntryEventOccurrence.__init__)


def test_activityedge_hasofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_hasOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)


def test_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence.__init__)


def test_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)


def test_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence.__init__)


def test_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_sendofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_sendOfferExitEventOccurrence)


def test_activityedge_sendofferexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge_sendOfferExitEventOccurrence.__init__)


def test_activityedge_sendofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_sendOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_sendofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_sendOfferEntryEventOccurrence)


def test_activityedge_sendofferentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge_sendOfferEntryEventOccurrence.__init__)


def test_activityedge_sendofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge_sendOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_isrunningexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_isRunningExitEventOccurrence)


def test_activitynode_isrunningexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_isRunningExitEventOccurrence.__init__)


def test_activitynode_isrunningexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_isRunningExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_isrunningentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_isRunningEntryEventOccurrence)


def test_activitynode_isrunningentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_isRunningEntryEventOccurrence.__init__)


def test_activitynode_isrunningentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_isRunningEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_run_activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_run_activityNodeExitEventOccurrence)


def test_activitynode_run_activitynodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_run_activityNodeExitEventOccurrence.__init__)


def test_activitynode_run_activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_run_activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_hasOffersExitEventOccurrence)


def test_activitynode_hasoffersexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_hasOffersExitEventOccurrence.__init__)


def test_activitynode_hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_hasOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_run_activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_run_activityNodeEntryEventOccurrence)


def test_activitynode_run_activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_run_activityNodeEntryEventOccurrence.__init__)


def test_activitynode_run_activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_run_activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_hasoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_hasOffersEntryEventOccurrence)


def test_activitynode_hasoffersentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_hasOffersEntryEventOccurrence.__init__)


def test_activitynode_hasoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_hasOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_removeTokenExitEventOccurrence)


def test_activitynode_removetokenexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_removeTokenExitEventOccurrence.__init__)


def test_activitynode_removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_removeTokenEntryEventOccurrence)


def test_activitynode_removetokenentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_removeTokenEntryEventOccurrence.__init__)


def test_activitynode_removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_addtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_addTokensExitEventOccurrence)


def test_activitynode_addtokensexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_addTokensExitEventOccurrence.__init__)


def test_activitynode_addtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_addTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_addtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_addTokensEntryEventOccurrence)


def test_activitynode_addtokensentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_addTokensEntryEventOccurrence.__init__)


def test_activitynode_addtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_addTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_takeofferedtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_takeOfferedTokensExitEventOccurrence)


def test_activitynode_takeofferedtokensexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_takeOfferedTokensExitEventOccurrence.__init__)


def test_activitynode_takeofferedtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_takeOfferedTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_takeofferedtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_takeOfferedTokensEntryEventOccurrence)


def test_activitynode_takeofferedtokensentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_takeOfferedTokensEntryEventOccurrence.__init__)


def test_activitynode_takeofferedtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_takeOfferedTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_sendoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_sendOffersExitEventOccurrence)


def test_activitynode_sendoffersexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_sendOffersExitEventOccurrence.__init__)


def test_activitynode_sendoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_sendOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_sendoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_sendOffersEntryEventOccurrence)


def test_activitynode_sendoffersentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_sendOffersEntryEventOccurrence.__init__)


def test_activitynode_sendoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_sendOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_terminate_activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_terminate_activityNodeExitEventOccurrence)


def test_activitynode_terminate_activitynodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode_terminate_activityNodeExitEventOccurrence.__init__)


def test_activitynode_terminate_activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_terminate_activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_terminate_activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_terminate_activityNodeEntryEventOccurrence)


def test_activitynode_terminate_activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode_terminate_activityNodeEntryEventOccurrence.__init__)


def test_activitynode_terminate_activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode_terminate_activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_runnodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_runNodesExitEventOccurrence)


def test_activity_runnodesexiteventoccurrence_constructor_exists():
    assert callable(Activity_runNodesExitEventOccurrence.__init__)


def test_activity_runnodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_runNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_runnodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_runNodesEntryEventOccurrence)


def test_activity_runnodesentryeventoccurrence_constructor_exists():
    assert callable(Activity_runNodesEntryEventOccurrence.__init__)


def test_activity_runnodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_runNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_runExitEventOccurrence)


def test_activity_runexiteventoccurrence_constructor_exists():
    assert callable(Activity_runExitEventOccurrence.__init__)


def test_activity_runexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_runEntryEventOccurrence)


def test_activity_runentryeventoccurrence_constructor_exists():
    assert callable(Activity_runEntryEventOccurrence.__init__)


def test_activity_runentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_initializeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_initializeExitEventOccurrence)


def test_activity_initializeexiteventoccurrence_constructor_exists():
    assert callable(Activity_initializeExitEventOccurrence.__init__)


def test_activity_initializeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_initializeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_initializeEntryEventOccurrence)


def test_activity_initializeentryeventoccurrence_constructor_exists():
    assert callable(Activity_initializeEntryEventOccurrence.__init__)


def test_activity_initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_initializeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_fireNodeExitEventOccurrence)


def test_activity_firenodeexiteventoccurrence_constructor_exists():
    assert callable(Activity_fireNodeExitEventOccurrence.__init__)


def test_activity_firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_firenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_fireNodeEntryEventOccurrence)


def test_activity_firenodeentryeventoccurrence_constructor_exists():
    assert callable(Activity_fireNodeEntryEventOccurrence.__init__)


def test_activity_firenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_fireNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_getinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_getInitialNodeExitEventOccurrence)


def test_activity_getinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity_getInitialNodeExitEventOccurrence.__init__)


def test_activity_getinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_getInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_getinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_getInitialNodeEntryEventOccurrence)


def test_activity_getinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity_getInitialNodeEntryEventOccurrence.__init__)


def test_activity_getinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_getInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_terminateexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_terminateExitEventOccurrence)


def test_activity_terminateexiteventoccurrence_constructor_exists():
    assert callable(Activity_terminateExitEventOccurrence.__init__)


def test_activity_terminateexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_terminateExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_terminateentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_terminateEntryEventOccurrence)


def test_activity_terminateentryeventoccurrence_constructor_exists():
    assert callable(Activity_terminateEntryEventOccurrence.__init__)


def test_activity_terminateentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_terminateEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_selectnextnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_selectNextNodeExitEventOccurrence)


def test_activity_selectnextnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity_selectNextNodeExitEventOccurrence.__init__)


def test_activity_selectnextnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_selectNextNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_selectnextnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_selectNextNodeEntryEventOccurrence)


def test_activity_selectnextnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity_selectNextNodeEntryEventOccurrence.__init__)


def test_activity_selectnextnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_selectNextNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_getenablednodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_getEnabledNodesExitEventOccurrence)


def test_activity_getenablednodesexiteventoccurrence_constructor_exists():
    assert callable(Activity_getEnabledNodesExitEventOccurrence.__init__)


def test_activity_getenablednodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_getEnabledNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_getenablednodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_getEnabledNodesEntryEventOccurrence)


def test_activity_getenablednodesentryeventoccurrence_constructor_exists():
    assert callable(Activity_getEnabledNodesEntryEventOccurrence.__init__)


def test_activity_getenablednodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_getEnabledNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_fireinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_fireInitialNodeExitEventOccurrence)


def test_activity_fireinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity_fireInitialNodeExitEventOccurrence.__init__)


def test_activity_fireinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_fireInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_heldtokens_state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_heldTokens_State)


def test_activitynode_heldtokens_state_constructor_exists():
    assert callable(ActivityNode_heldTokens_State.__init__)


def test_activitynode_heldtokens_state_constructor_args():
    sig = inspect.signature(ActivityNode_heldTokens_State.__init__)
    params = list(sig.parameters.keys())



def test_activity_fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_fireInitialNodeEntryEventOccurrence)


def test_activity_fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity_fireInitialNodeEntryEventOccurrence.__init__)


def test_activity_fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode_running_state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode_running_State)


def test_activitynode_running_state_constructor_exists():
    assert callable(ActivityNode_running_State.__init__)


def test_activitynode_running_state_constructor_args():
    sig = inspect.signature(ActivityNode_running_State.__init__)
    params = list(sig.parameters.keys())



def test_activity_mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_mainExitEventOccurrence)


def test_activity_mainexiteventoccurrence_constructor_exists():
    assert callable(Activity_mainExitEventOccurrence.__init__)


def test_activity_mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity_mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity_mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity_mainEntryEventOccurrence)


def test_activity_mainentryeventoccurrence_constructor_exists():
    assert callable(Activity_mainEntryEventOccurrence.__init__)


def test_activity_mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity_mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_events_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Events)


def test_trace_events_events_constructor_exists():
    assert callable(trace_Events_Events.__init__)


def test_trace_events_events_constructor_args():
    sig = inspect.signature(trace_Events_Events.__init__)
    params = list(sig.parameters.keys())



def test_events_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(Events_trace_GlobalState)


def test_events_trace_globalstate_constructor_exists():
    assert callable(Events_trace_GlobalState.__init__)


def test_events_trace_globalstate_constructor_args():
    sig = inspect.signature(Events_trace_GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_EventOccurrence)


def test_trace_events_eventoccurrence_constructor_exists():
    assert callable(trace_Events_EventOccurrence.__init__)


def test_trace_events_eventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(trace_IntegerCalculationExpression)


def test_trace_integercalculationexpression_constructor_exists():
    assert callable(trace_IntegerCalculationExpression.__init__)


def test_trace_integercalculationexpression_constructor_args():
    sig = inspect.signature(trace_IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace_booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(trace_BooleanUnaryExpression)


def test_trace_booleanunaryexpression_constructor_exists():
    assert callable(trace_BooleanUnaryExpression.__init__)


def test_trace_booleanunaryexpression_constructor_args():
    sig = inspect.signature(trace_BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace_integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(trace_IntegerComparisonExpression)


def test_trace_integercomparisonexpression_constructor_exists():
    assert callable(trace_IntegerComparisonExpression.__init__)


def test_trace_integercomparisonexpression_constructor_args():
    sig = inspect.signature(trace_IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(trace_BooleanValue)


def test_trace_booleanvalue_constructor_exists():
    assert callable(trace_BooleanValue.__init__)


def test_trace_booleanvalue_constructor_args():
    sig = inspect.signature(trace_BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_trace_integervalue_is_not_abstract():
    assert not inspect.isabstract(trace_IntegerValue)


def test_trace_integervalue_constructor_exists():
    assert callable(trace_IntegerValue.__init__)


def test_trace_integervalue_constructor_args():
    sig = inspect.signature(trace_IntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_trace_stringvalue_is_not_abstract():
    assert not inspect.isabstract(trace_StringValue)


def test_trace_stringvalue_constructor_exists():
    assert callable(trace_StringValue.__init__)


def test_trace_stringvalue_constructor_args():
    sig = inspect.signature(trace_StringValue.__init__)
    params = list(sig.parameters.keys())



def test_trace_booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(trace_BooleanBinaryExpression)


def test_trace_booleanbinaryexpression_constructor_exists():
    assert callable(trace_BooleanBinaryExpression.__init__)


def test_trace_booleanbinaryexpression_constructor_args():
    sig = inspect.signature(trace_BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace_executednodes_state_is_not_abstract():
    assert not inspect.isabstract(Trace_executedNodes_State)


def test_trace_executednodes_state_constructor_exists():
    assert callable(Trace_executedNodes_State.__init__)


def test_trace_executednodes_state_constructor_args():
    sig = inspect.signature(Trace_executedNodes_State.__init__)
    params = list(sig.parameters.keys())



def test_activity_trace_state_is_not_abstract():
    assert not inspect.isabstract(Activity_trace_State)


def test_activity_trace_state_constructor_exists():
    assert callable(Activity_trace_State.__init__)


def test_activity_trace_state_constructor_args():
    sig = inspect.signature(Activity_trace_State.__init__)
    params = list(sig.parameters.keys())



def test_trace_trace_is_not_abstract():
    assert not inspect.isabstract(trace_Trace)


def test_trace_trace_constructor_exists():
    assert callable(trace_Trace.__init__)


def test_trace_trace_constructor_args():
    sig = inspect.signature(trace_Trace.__init__)
    params = list(sig.parameters.keys())



def test_offer_offeredtokens_state_is_not_abstract():
    assert not inspect.isabstract(Offer_offeredTokens_State)


def test_offer_offeredtokens_state_constructor_exists():
    assert callable(Offer_offeredTokens_State.__init__)


def test_offer_offeredtokens_state_constructor_args():
    sig = inspect.signature(Offer_offeredTokens_State.__init__)
    params = list(sig.parameters.keys())



def test_variable_currentvalue_state_is_not_abstract():
    assert not inspect.isabstract(Variable_currentValue_State)


def test_variable_currentvalue_state_constructor_exists():
    assert callable(Variable_currentValue_State.__init__)


def test_variable_currentvalue_state_constructor_args():
    sig = inspect.signature(Variable_currentValue_State.__init__)
    params = list(sig.parameters.keys())



def test_activityedge_offers_state_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge_offers_State)


def test_activityedge_offers_state_constructor_exists():
    assert callable(ActivityEdge_offers_State.__init__)


def test_activityedge_offers_state_constructor_args():
    sig = inspect.signature(ActivityEdge_offers_State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_basetokeniswithdrawn_state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_baseTokenIsWithdrawn_State)


def test_forkedtoken_basetokeniswithdrawn_state_constructor_exists():
    assert callable(ForkedToken_baseTokenIsWithdrawn_State.__init__)


def test_forkedtoken_basetokeniswithdrawn_state_constructor_args():
    sig = inspect.signature(ForkedToken_baseTokenIsWithdrawn_State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_basetoken_state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_baseToken_State)


def test_forkedtoken_basetoken_state_constructor_exists():
    assert callable(ForkedToken_baseToken_State.__init__)


def test_forkedtoken_basetoken_state_constructor_args():
    sig = inspect.signature(ForkedToken_baseToken_State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken_remainingofferscount_state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken_remainingOffersCount_State)


def test_forkedtoken_remainingofferscount_state_constructor_exists():
    assert callable(ForkedToken_remainingOffersCount_State.__init__)


def test_forkedtoken_remainingofferscount_state_constructor_args():
    sig = inspect.signature(ForkedToken_remainingOffersCount_State.__init__)
    params = list(sig.parameters.keys())



def test_input_inputvalues_state_is_not_abstract():
    assert not inspect.isabstract(Input_inputValues_State)


def test_input_inputvalues_state_constructor_exists():
    assert callable(Input_inputValues_State.__init__)


def test_input_inputvalues_state_constructor_args():
    sig = inspect.signature(Input_inputValues_State.__init__)
    params = list(sig.parameters.keys())



def test_token_holder_state_is_not_abstract():
    assert not inspect.isabstract(Token_holder_State)


def test_token_holder_state_constructor_exists():
    assert callable(Token_holder_State.__init__)


def test_token_holder_state_constructor_args():
    sig = inspect.signature(Token_holder_State.__init__)
    params = list(sig.parameters.keys())



def test_inputvalue_variable_state_is_not_abstract():
    assert not inspect.isabstract(InputValue_variable_State)


def test_inputvalue_variable_state_constructor_exists():
    assert callable(InputValue_variable_State.__init__)


def test_inputvalue_variable_state_constructor_args():
    sig = inspect.signature(InputValue_variable_State.__init__)
    params = list(sig.parameters.keys())



def test_inputvalue_value_state_is_not_abstract():
    assert not inspect.isabstract(InputValue_value_State)


def test_inputvalue_value_state_constructor_exists():
    assert callable(InputValue_value_State.__init__)


def test_inputvalue_value_state_constructor_args():
    sig = inspect.signature(InputValue_value_State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_isReadyEntryEventOccurrence)


def test_trace_events_activitynode_isreadyentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_isReadyEntryEventOccurrence.__init__)


def test_trace_events_activitynode_isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_isReadyEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)


def test_trace_events_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence.__init__)


def test_trace_events_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)


def test_trace_events_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_evaluatesubtractexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)


def test_trace_events_integercalculationexpression_evaluatesubtractexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_evaluatesubtractexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)


def test_trace_events_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence.__init__)


def test_trace_events_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)


def test_trace_events_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence.__init__)


def test_trace_events_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_controlnode_fire_controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ControlNode_fire_controlNodeExitEventOccurrence)


def test_trace_events_controlnode_fire_controlnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ControlNode_fire_controlNodeExitEventOccurrence.__init__)


def test_trace_events_controlnode_fire_controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ControlNode_fire_controlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_isrunningexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_isRunningExitEventOccurrence)


def test_trace_events_activitynode_isrunningexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_isRunningExitEventOccurrence.__init__)


def test_trace_events_activitynode_isrunningexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_isRunningExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)


def test_trace_events_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence.__init__)


def test_trace_events_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_fireinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_fireInitialNodeExitEventOccurrence)


def test_trace_events_activity_fireinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_fireInitialNodeExitEventOccurrence.__init__)


def test_trace_events_activity_fireinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_fireInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integervariable_setcurrentvalue_integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)


def test_trace_events_integervariable_setcurrentvalue_integervariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence.__init__)


def test_trace_events_integervariable_setcurrentvalue_integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)


def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_removeTokenExitEventOccurrence)


def test_trace_events_activitynode_removetokenexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_removeTokenExitEventOccurrence.__init__)


def test_trace_events_activitynode_removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_firenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_fireNodeEntryEventOccurrence)


def test_trace_events_activity_firenodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_fireNodeEntryEventOccurrence.__init__)


def test_trace_events_activity_firenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_fireNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_isready_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_isReady_actionExitEventOccurrence)


def test_trace_events_action_isready_actionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_isReady_actionExitEventOccurrence.__init__)


def test_trace_events_action_isready_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_isReady_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_forknode_fire_forknodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ForkNode_fire_forkNodeExitEventOccurrence)


def test_trace_events_forknode_fire_forknodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ForkNode_fire_forkNodeExitEventOccurrence.__init__)


def test_trace_events_forknode_fire_forknodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ForkNode_fire_forkNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)


def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence.__init__)


def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_runnodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_runNodesExitEventOccurrence)


def test_trace_events_activity_runnodesexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_runNodesExitEventOccurrence.__init__)


def test_trace_events_activity_runnodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_runNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_initialnode_fire_initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_InitialNode_fire_initialNodeExitEventOccurrence)


def test_trace_events_initialnode_fire_initialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_InitialNode_fire_initialNodeExitEventOccurrence.__init__)


def test_trace_events_initialnode_fire_initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_InitialNode_fire_initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_evaluateandexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)


def test_trace_events_booleanbinaryexpression_evaluateandexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_evaluateandexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_isReadyExitEventOccurrence)


def test_trace_events_activitynode_isreadyexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_isReadyExitEventOccurrence.__init__)


def test_trace_events_activitynode_isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_mainEntryEventOccurrence)


def test_trace_events_activity_mainentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_mainEntryEventOccurrence.__init__)


def test_trace_events_activity_mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_sendoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_sendOffersEntryEventOccurrence)


def test_trace_events_activitynode_sendoffersentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_sendOffersEntryEventOccurrence.__init__)


def test_trace_events_activitynode_sendoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_sendOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_sendoffers_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_sendOffers_actionEntryEventOccurrence)


def test_trace_events_action_sendoffers_actionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_sendOffers_actionEntryEventOccurrence.__init__)


def test_trace_events_action_sendoffers_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_sendOffers_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_takeofferedtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)


def test_trace_events_activitynode_takeofferedtokensentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence.__init__)


def test_trace_events_activitynode_takeofferedtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_fireNodeExitEventOccurrence)


def test_trace_events_activity_firenodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_fireNodeExitEventOccurrence.__init__)


def test_trace_events_activity_firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_addtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_addTokensExitEventOccurrence)


def test_trace_events_activitynode_addtokensexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_addTokensExitEventOccurrence.__init__)


def test_trace_events_activitynode_addtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_addTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_mergenode_hasoffers_mergenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)


def test_trace_events_mergenode_hasoffers_mergenodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence.__init__)


def test_trace_events_mergenode_hasoffers_mergenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_forkedtoken_withdraw_forkedtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)


def test_trace_events_forkedtoken_withdraw_forkedtokenexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence.__init__)


def test_trace_events_forkedtoken_withdraw_forkedtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_runnodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_runNodesEntryEventOccurrence)


def test_trace_events_activity_runnodesentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_runNodesEntryEventOccurrence.__init__)


def test_trace_events_activity_runnodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_runNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_decisionnode_fire_decisionnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)


def test_trace_events_decisionnode_fire_decisionnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence.__init__)


def test_trace_events_decisionnode_fire_decisionnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_hasOffersExitEventOccurrence)


def test_trace_events_activitynode_hasoffersexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_hasOffersExitEventOccurrence.__init__)


def test_trace_events_activitynode_hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_hasOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_selectnextnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_selectNextNodeEntryEventOccurrence)


def test_trace_events_activity_selectnextnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_selectNextNodeEntryEventOccurrence.__init__)


def test_trace_events_activity_selectnextnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_selectNextNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_run_activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence)


def test_trace_events_activitynode_run_activitynodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence.__init__)


def test_trace_events_activitynode_run_activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_getenablednodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_getEnabledNodesExitEventOccurrence)


def test_trace_events_activity_getenablednodesexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_getEnabledNodesExitEventOccurrence.__init__)


def test_trace_events_activity_getenablednodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_getEnabledNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_mergenode_hasoffers_mergenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)


def test_trace_events_mergenode_hasoffers_mergenodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence.__init__)


def test_trace_events_mergenode_hasoffers_mergenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_removeTokenEntryEventOccurrence)


def test_trace_events_activitynode_removetokenentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_removeTokenEntryEventOccurrence.__init__)


def test_trace_events_activitynode_removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_terminateentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_terminateEntryEventOccurrence)


def test_trace_events_activity_terminateentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_terminateEntryEventOccurrence.__init__)


def test_trace_events_activity_terminateentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_terminateEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluategreaterexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluategreaterexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluategreaterexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)


def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence.__init__)


def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_initialnode_fire_initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence)


def test_trace_events_initialnode_fire_initialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence.__init__)


def test_trace_events_initialnode_fire_initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_withdrawexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_withdrawExitEventOccurrence)


def test_trace_events_token_withdrawexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_withdrawExitEventOccurrence.__init__)


def test_trace_events_token_withdrawexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_withdrawExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)


def test_trace_events_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence.__init__)


def test_trace_events_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluatesmallerentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluatesmallerentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluatesmallerentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluateequalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluateequalsentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluateequalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_offer_hastokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Offer_hasTokensEntryEventOccurrence)


def test_trace_events_offer_hastokensentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Offer_hasTokensEntryEventOccurrence.__init__)


def test_trace_events_offer_hastokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Offer_hasTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_runExitEventOccurrence)


def test_trace_events_activity_runexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_runExitEventOccurrence.__init__)


def test_trace_events_activity_runexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_getinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_getInitialNodeExitEventOccurrence)


def test_trace_events_activity_getinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_getInitialNodeExitEventOccurrence.__init__)


def test_trace_events_activity_getinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_getInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_controlnode_isready_controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)


def test_trace_events_controlnode_isready_controlnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence.__init__)


def test_trace_events_controlnode_isready_controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_initializeEntryEventOccurrence)


def test_trace_events_activity_initializeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_initializeEntryEventOccurrence.__init__)


def test_trace_events_activity_initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_initializeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)


def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_hasoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_hasOffersEntryEventOccurrence)


def test_trace_events_activitynode_hasoffersentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_hasOffersEntryEventOccurrence.__init__)


def test_trace_events_activitynode_hasoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_hasOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_evaluateorentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)


def test_trace_events_booleanbinaryexpression_evaluateorentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_evaluateorentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)


def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_evaluateandentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)


def test_trace_events_booleanbinaryexpression_evaluateandentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_evaluateandentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_hasofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_hasOfferEntryEventOccurrence)


def test_trace_events_activityedge_hasofferentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_hasOfferEntryEventOccurrence.__init__)


def test_trace_events_activityedge_hasofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_hasOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_fireInitialNodeEntryEventOccurrence)


def test_trace_events_activity_fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_fireInitialNodeEntryEventOccurrence.__init__)


def test_trace_events_activity_fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_fire_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_fire_actionEntryEventOccurrence)


def test_trace_events_action_fire_actionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_fire_actionEntryEventOccurrence.__init__)


def test_trace_events_action_fire_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_fire_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)


def test_trace_events_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence.__init__)


def test_trace_events_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_controlnode_isready_controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)


def test_trace_events_controlnode_isready_controlnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence.__init__)


def test_trace_events_controlnode_isready_controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)


def test_trace_events_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence.__init__)


def test_trace_events_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_mainExitEventOccurrence)


def test_trace_events_activity_mainexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_mainExitEventOccurrence.__init__)


def test_trace_events_activity_mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_forknode_fire_forknodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence)


def test_trace_events_forknode_fire_forknodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence.__init__)


def test_trace_events_forknode_fire_forknodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_initializeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_initializeExitEventOccurrence)


def test_trace_events_activity_initializeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_initializeExitEventOccurrence.__init__)


def test_trace_events_activity_initializeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_initializeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_sendoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_sendOffersExitEventOccurrence)


def test_trace_events_activitynode_sendoffersexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_sendOffersExitEventOccurrence.__init__)


def test_trace_events_activitynode_sendoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_sendOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)


def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence.__init__)


def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)


def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence.__init__)


def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_transferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_transferExitEventOccurrence)


def test_trace_events_token_transferexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_transferExitEventOccurrence.__init__)


def test_trace_events_token_transferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_transferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_getenablednodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_getEnabledNodesEntryEventOccurrence)


def test_trace_events_activity_getenablednodesentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_getEnabledNodesEntryEventOccurrence.__init__)


def test_trace_events_activity_getenablednodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_getEnabledNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_hasofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_hasOfferExitEventOccurrence)


def test_trace_events_activityedge_hasofferexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_hasOfferExitEventOccurrence.__init__)


def test_trace_events_activityedge_hasofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_hasOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)


def test_trace_events_integercalculationexpression_evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluateequalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluateequalsexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluateequalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)


def test_trace_events_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence.__init__)


def test_trace_events_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_transferEntryEventOccurrence)


def test_trace_events_token_transferentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_transferEntryEventOccurrence.__init__)


def test_trace_events_token_transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_transferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_sendoffers_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_sendOffers_actionExitEventOccurrence)


def test_trace_events_action_sendoffers_actionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_sendOffers_actionExitEventOccurrence.__init__)


def test_trace_events_action_sendoffers_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_sendOffers_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)


def test_trace_events_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_run_activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_run_activityNodeExitEventOccurrence)


def test_trace_events_activitynode_run_activitynodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_run_activityNodeExitEventOccurrence.__init__)


def test_trace_events_activitynode_run_activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_run_activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)


def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_controlnode_fire_controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence)


def test_trace_events_controlnode_fire_controlnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence.__init__)


def test_trace_events_controlnode_fire_controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)


def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence.__init__)


def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_runEntryEventOccurrence)


def test_trace_events_activity_runentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_runEntryEventOccurrence.__init__)


def test_trace_events_activity_runentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_takeofferedtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)


def test_trace_events_activitynode_takeofferedtokensexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence.__init__)


def test_trace_events_activitynode_takeofferedtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanbinaryexpression_evaluateorexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)


def test_trace_events_booleanbinaryexpression_evaluateorexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence.__init__)


def test_trace_events_booleanbinaryexpression_evaluateorexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_iswithdrawnentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_isWithdrawnEntryEventOccurrence)


def test_trace_events_token_iswithdrawnentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_isWithdrawnEntryEventOccurrence.__init__)


def test_trace_events_token_iswithdrawnentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_isWithdrawnEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_getinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_getInitialNodeEntryEventOccurrence)


def test_trace_events_activity_getinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_getInitialNodeEntryEventOccurrence.__init__)


def test_trace_events_activity_getinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_getInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanunaryexpression_evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)


def test_trace_events_booleanunaryexpression_evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence.__init__)


def test_trace_events_booleanunaryexpression_evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_opaqueaction_doaction_opaqueactionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)


def test_trace_events_opaqueaction_doaction_opaqueactionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence.__init__)


def test_trace_events_opaqueaction_doaction_opaqueactionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)


def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence.__init__)


def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_decisionnode_fire_decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)


def test_trace_events_decisionnode_fire_decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence.__init__)


def test_trace_events_decisionnode_fire_decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_iswithdrawnexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_isWithdrawnExitEventOccurrence)


def test_trace_events_token_iswithdrawnexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_isWithdrawnExitEventOccurrence.__init__)


def test_trace_events_token_iswithdrawnexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_isWithdrawnExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integerexpression_getoperandcurrentvaluesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)


def test_trace_events_integerexpression_getoperandcurrentvaluesexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence.__init__)


def test_trace_events_integerexpression_getoperandcurrentvaluesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_isready_actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_isReady_actionEntryEventOccurrence)


def test_trace_events_action_isready_actionentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_isReady_actionEntryEventOccurrence.__init__)


def test_trace_events_action_isready_actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_isReady_actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_terminateexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_terminateExitEventOccurrence)


def test_trace_events_activity_terminateexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_terminateExitEventOccurrence.__init__)


def test_trace_events_activity_terminateexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_terminateExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integerexpression_getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)


def test_trace_events_integerexpression_getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_trace_events_integerexpression_getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_forkedtoken_withdraw_forkedtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)


def test_trace_events_forkedtoken_withdraw_forkedtokenentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence.__init__)


def test_trace_events_forkedtoken_withdraw_forkedtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_initialnode_isready_initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)


def test_trace_events_initialnode_isready_initialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence.__init__)


def test_trace_events_initialnode_isready_initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_addtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_addTokensEntryEventOccurrence)


def test_trace_events_activitynode_addtokensentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_addTokensEntryEventOccurrence.__init__)


def test_trace_events_activitynode_addtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_addTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integervariable_setcurrentvalue_integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)


def test_trace_events_integervariable_setcurrentvalue_integervariableentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence.__init__)


def test_trace_events_integervariable_setcurrentvalue_integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)


def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence.__init__)


def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_action_fire_actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Action_fire_actionExitEventOccurrence)


def test_trace_events_action_fire_actionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Action_fire_actionExitEventOccurrence.__init__)


def test_trace_events_action_fire_actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Action_fire_actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluategreaterentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluategreaterentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluategreaterentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_sendofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_sendOfferEntryEventOccurrence)


def test_trace_events_activityedge_sendofferentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_sendOfferEntryEventOccurrence.__init__)


def test_trace_events_activityedge_sendofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_sendOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_initialnode_isready_initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)


def test_trace_events_initialnode_isready_initialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence.__init__)


def test_trace_events_initialnode_isready_initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_opaqueaction_doaction_opaqueactionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)


def test_trace_events_opaqueaction_doaction_opaqueactionexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence.__init__)


def test_trace_events_opaqueaction_doaction_opaqueactionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_evaluatesubtractentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)


def test_trace_events_integercalculationexpression_evaluatesubtractentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_evaluatesubtractentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_offer_hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Offer_hasTokensExitEventOccurrence)


def test_trace_events_offer_hastokensexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Offer_hasTokensExitEventOccurrence.__init__)


def test_trace_events_offer_hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Offer_hasTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)


def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence.__init__)


def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercalculationexpression_evaluateaddexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)


def test_trace_events_integercalculationexpression_evaluateaddexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence.__init__)


def test_trace_events_integercalculationexpression_evaluateaddexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_terminate_activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)


def test_trace_events_activitynode_terminate_activitynodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence.__init__)


def test_trace_events_activitynode_terminate_activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_integercomparisonexpression_evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)


def test_trace_events_integercomparisonexpression_evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence.__init__)


def test_trace_events_integercomparisonexpression_evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_booleanunaryexpression_evaluatenotexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)


def test_trace_events_booleanunaryexpression_evaluatenotexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence.__init__)


def test_trace_events_booleanunaryexpression_evaluatenotexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_token_withdrawentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Token_withdrawEntryEventOccurrence)


def test_trace_events_token_withdrawentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_Token_withdrawEntryEventOccurrence.__init__)


def test_trace_events_token_withdrawentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Token_withdrawEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_terminate_activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)


def test_trace_events_activitynode_terminate_activitynodeentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence.__init__)


def test_trace_events_activitynode_terminate_activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activitynode_isrunningentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityNode_isRunningEntryEventOccurrence)


def test_trace_events_activitynode_isrunningentryeventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityNode_isRunningEntryEventOccurrence.__init__)


def test_trace_events_activitynode_isrunningentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityNode_isRunningEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activityedge_sendofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_ActivityEdge_sendOfferExitEventOccurrence)


def test_trace_events_activityedge_sendofferexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_ActivityEdge_sendOfferExitEventOccurrence.__init__)


def test_trace_events_activityedge_sendofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_ActivityEdge_sendOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_events_activity_selectnextnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace_Events_Activity_selectNextNodeExitEventOccurrence)


def test_trace_events_activity_selectnextnodeexiteventoccurrence_constructor_exists():
    assert callable(trace_Events_Activity_selectNextNodeExitEventOccurrence.__init__)


def test_trace_events_activity_selectnextnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace_Events_Activity_selectNextNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace_staticobjectspools_is_not_abstract():
    assert not inspect.isabstract(trace_StaticObjectsPools)


def test_trace_staticobjectspools_constructor_exists():
    assert callable(trace_StaticObjectsPools.__init__)


def test_trace_staticobjectspools_constructor_args():
    sig = inspect.signature(trace_StaticObjectsPools.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(TracedObjects)


def test_tracedobjects_constructor_exists():
    assert callable(TracedObjects.__init__)


def test_tracedobjects_constructor_args():
    sig = inspect.signature(TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_events_constructor_exists():
    assert callable(Events.__init__)


def test_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())



def test_trace_globalstate_is_not_abstract():
    assert not inspect.isabstract(trace_GlobalState)


def test_trace_globalstate_constructor_exists():
    assert callable(trace_GlobalState.__init__)


def test_trace_globalstate_constructor_args():
    sig = inspect.signature(trace_GlobalState.__init__)
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
Events_trace_Value_strategy = st.builds(
    Events_trace_Value,
)
activitydiagram_TracedIntegerVariable_strategy = st.builds(
    activitydiagram_TracedIntegerVariable,
)
activitydiagram_TracedDecisionNode_strategy = st.builds(
    activitydiagram_TracedDecisionNode,
)
activitydiagram_TracedMergeNode_strategy = st.builds(
    activitydiagram_TracedMergeNode,
)
activitydiagram_TracedInitialNode_strategy = st.builds(
    activitydiagram_TracedInitialNode,
)
activitydiagram_TracedForkNode_strategy = st.builds(
    activitydiagram_TracedForkNode,
)
activitydiagram_TracedActivityFinalNode_strategy = st.builds(
    activitydiagram_TracedActivityFinalNode,
)
activitydiagram_TracedAction_strategy = st.builds(
    activitydiagram_TracedAction,
)
activitydiagram_TracedOpaqueAction_strategy = st.builds(
    activitydiagram_TracedOpaqueAction,
)
activitydiagramConfiguration_TracedToken_strategy = st.builds(
    activitydiagramConfiguration_TracedToken,
)
activitydiagram_TracedControlNode_strategy = st.builds(
    activitydiagram_TracedControlNode,
)
activitydiagram_TracedActivityEdge_strategy = st.builds(
    activitydiagram_TracedActivityEdge,
)
activitydiagram_TracedActivityNode_strategy = st.builds(
    activitydiagram_TracedActivityNode,
)
trace_activitydiagramConfiguration_TracedOffer_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedOffer,
)
trace_activitydiagramConfiguration_TracedInput_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedInput,
)
TracedToken_strategy = st.builds(
    TracedToken,
)
trace_activitydiagramConfiguration_TracedForkedToken_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedForkedToken,
)
trace_activitydiagramConfiguration_TracedControlToken_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedControlToken,
)
trace_activitydiagramConfiguration_TracedToken_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedToken,
)
trace_activitydiagramConfiguration_TracedInputValue_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedInputValue,
)
activitydiagram_trace_DecisionNode_strategy = st.builds(
    activitydiagram_trace_DecisionNode,
)
activitydiagram_trace_JoinNode_strategy = st.builds(
    activitydiagram_trace_JoinNode,
)
activitydiagram_trace_OpaqueAction_strategy = st.builds(
    activitydiagram_trace_OpaqueAction,
)
trace_activitydiagramConfiguration_TracedTrace_strategy = st.builds(
    trace_activitydiagramConfiguration_TracedTrace,
)
activitydiagram_trace_InitialNode_strategy = st.builds(
    activitydiagram_trace_InitialNode,
)
activitydiagram_trace_ForkNode_strategy = st.builds(
    activitydiagram_trace_ForkNode,
)
activitydiagram_trace_ActivityFinalNode_strategy = st.builds(
    activitydiagram_trace_ActivityFinalNode,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
trace_activitydiagram_TracedActivityFinalNode_strategy = st.builds(
    trace_activitydiagram_TracedActivityFinalNode,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
activitydiagram_trace_Expression_strategy = st.builds(
    activitydiagram_trace_Expression,
)
trace_activitydiagram_TracedAction_strategy = st.builds(
    trace_activitydiagram_TracedAction,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
trace_activitydiagram_TracedOpaqueAction_strategy = st.builds(
    trace_activitydiagram_TracedOpaqueAction,
)
activitydiagram_trace_StringVariable_strategy = st.builds(
    activitydiagram_trace_StringVariable,
)
activitydiagram_trace_Activity_strategy = st.builds(
    activitydiagram_trace_Activity,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
trace_activitydiagram_TracedActivity_strategy = st.builds(
    trace_activitydiagram_TracedActivity,
)
trace_activitydiagram_TracedActivityNode_strategy = st.builds(
    trace_activitydiagram_TracedActivityNode,
)
trace_activitydiagram_TracedActivityEdge_strategy = st.builds(
    trace_activitydiagram_TracedActivityEdge,
)
activitydiagram_trace_IntegerVariable_strategy = st.builds(
    activitydiagram_trace_IntegerVariable,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
trace_activitydiagram_TracedControlNode_strategy = st.builds(
    trace_activitydiagram_TracedControlNode,
)
trace_activitydiagram_TracedExecutableNode_strategy = st.builds(
    trace_activitydiagram_TracedExecutableNode,
)
activitydiagram_trace_BooleanVariable_strategy = st.builds(
    activitydiagram_trace_BooleanVariable,
)
TracedVariable_strategy = st.builds(
    TracedVariable,
)
trace_activitydiagram_TracedStringVariable_strategy = st.builds(
    trace_activitydiagram_TracedStringVariable,
)
trace_activitydiagram_TracedIntegerVariable_strategy = st.builds(
    trace_activitydiagram_TracedIntegerVariable,
)
trace_activitydiagram_TracedBooleanVariable_strategy = st.builds(
    trace_activitydiagram_TracedBooleanVariable,
)
activitydiagram_trace_MergeNode_strategy = st.builds(
    activitydiagram_trace_MergeNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
trace_activitydiagram_TracedForkNode_strategy = st.builds(
    trace_activitydiagram_TracedForkNode,
)
trace_activitydiagram_TracedInitialNode_strategy = st.builds(
    trace_activitydiagram_TracedInitialNode,
)
trace_activitydiagram_TracedJoinNode_strategy = st.builds(
    trace_activitydiagram_TracedJoinNode,
)
trace_activitydiagram_TracedDecisionNode_strategy = st.builds(
    trace_activitydiagram_TracedDecisionNode,
)
trace_activitydiagram_TracedFinalNode_strategy = st.builds(
    trace_activitydiagram_TracedFinalNode,
)
trace_activitydiagram_TracedMergeNode_strategy = st.builds(
    trace_activitydiagram_TracedMergeNode,
)
activitydiagram_trace_ControlFlow_strategy = st.builds(
    activitydiagram_trace_ControlFlow,
)
TracedActivityEdge_strategy = st.builds(
    TracedActivityEdge,
)
trace_activitydiagram_TracedControlFlow_strategy = st.builds(
    trace_activitydiagram_TracedControlFlow,
)
activitydiagram_TracedJoinNode_strategy = st.builds(
    activitydiagram_TracedJoinNode,
)
activitydiagram_trace_Value_strategy = st.builds(
    activitydiagram_trace_Value,
)
trace_activitydiagram_TracedVariable_strategy = st.builds(
    trace_activitydiagram_TracedVariable,
)
trace_activitydiagram_TracedNamedElement_strategy = st.builds(
    trace_activitydiagram_TracedNamedElement,
    name=
        safe_text
)
activitydiagramConfiguration_TracedControlToken_strategy = st.builds(
    activitydiagramConfiguration_TracedControlToken,
)
activitydiagram_TracedControlFlow_strategy = st.builds(
    activitydiagram_TracedControlFlow,
)
trace_Traced_TracedObjects_strategy = st.builds(
    trace_Traced_TracedObjects,
)
activitydiagramConfiguration_TracedTrace_strategy = st.builds(
    activitydiagramConfiguration_TracedTrace,
)
trace_States_Activity_trace_State_strategy = st.builds(
    trace_States_Activity_trace_State,
)
trace_States_ActivityNode_heldTokens_State_strategy = st.builds(
    trace_States_ActivityNode_heldTokens_State,
)
trace_States_ActivityNode_running_State_strategy = st.builds(
    trace_States_ActivityNode_running_State,
    running=
        st.booleans()
)
trace_States_Offer_offeredTokens_State_strategy = st.builds(
    trace_States_Offer_offeredTokens_State,
)
trace_States_Variable_currentValue_State_strategy = st.builds(
    trace_States_Variable_currentValue_State,
)
trace_States_Trace_executedNodes_State_strategy = st.builds(
    trace_States_Trace_executedNodes_State,
)
trace_States_ForkedToken_baseTokenIsWithdrawn_State_strategy = st.builds(
    trace_States_ForkedToken_baseTokenIsWithdrawn_State,
    baseTokenIsWithdrawn=
        st.booleans()
)
trace_States_ForkedToken_baseToken_State_strategy = st.builds(
    trace_States_ForkedToken_baseToken_State,
)
trace_States_ForkedToken_remainingOffersCount_State_strategy = st.builds(
    trace_States_ForkedToken_remainingOffersCount_State,
    remainingOffersCount=
        st.integers()
)
activitydiagramConfiguration_TracedInput_strategy = st.builds(
    activitydiagramConfiguration_TracedInput,
)
trace_States_Input_inputValues_State_strategy = st.builds(
    trace_States_Input_inputValues_State,
)
trace_States_Token_holder_State_strategy = st.builds(
    trace_States_Token_holder_State,
)
trace_States_ActivityEdge_offers_State_strategy = st.builds(
    trace_States_ActivityEdge_offers_State,
)
activitydiagramConfiguration_TracedInputValue_strategy = st.builds(
    activitydiagramConfiguration_TracedInputValue,
)
States_trace_Value_strategy = st.builds(
    States_trace_Value,
)
trace_States_InputValue_value_State_strategy = st.builds(
    trace_States_InputValue_value_State,
)
activitydiagramConfiguration_TracedOffer_strategy = st.builds(
    activitydiagramConfiguration_TracedOffer,
)
activitydiagramConfiguration_TracedForkedToken_strategy = st.builds(
    activitydiagramConfiguration_TracedForkedToken,
)
activitydiagram_TracedVariable_strategy = st.builds(
    activitydiagram_TracedVariable,
)
trace_States_InputValue_variable_State_strategy = st.builds(
    trace_States_InputValue_variable_State,
)
States_trace_GlobalState_strategy = st.builds(
    States_trace_GlobalState,
)
Events_trace_BooleanBinaryExpression_strategy = st.builds(
    Events_trace_BooleanBinaryExpression,
)
Events_trace_BooleanUnaryExpression_strategy = st.builds(
    Events_trace_BooleanUnaryExpression,
)
Events_trace_IntegerComparisonExpression_strategy = st.builds(
    Events_trace_IntegerComparisonExpression,
)
Events_trace_IntegerExpression_strategy = st.builds(
    Events_trace_IntegerExpression,
)
activitydiagram_TracedBooleanVariable_strategy = st.builds(
    activitydiagram_TracedBooleanVariable,
)
Events_trace_IntegerCalculationExpression_strategy = st.builds(
    Events_trace_IntegerCalculationExpression,
)
activitydiagram_TracedStringVariable_strategy = st.builds(
    activitydiagram_TracedStringVariable,
)
Offer_hasTokensExitEventOccurrence_strategy = st.builds(
    Offer_hasTokensExitEventOccurrence,
)
Events_trace_EObject_strategy = st.builds(
    Events_trace_EObject,
)
activitydiagram_TracedActivity_strategy = st.builds(
    activitydiagram_TracedActivity,
)
Token_isWithdrawnExitEventOccurrence_strategy = st.builds(
    Token_isWithdrawnExitEventOccurrence,
)
Token_isWithdrawnEntryEventOccurrence_strategy = st.builds(
    Token_isWithdrawnEntryEventOccurrence,
)
BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_evaluateORExitEventOccurrence,
)
Offer_hasTokensEntryEventOccurrence_strategy = st.builds(
    Offer_hasTokensEntryEventOccurrence,
)
ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy = st.builds(
    ForkedToken_withdraw_forkedTokenExitEventOccurrence,
)
ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy = st.builds(
    ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
)
Token_withdrawExitEventOccurrence_strategy = st.builds(
    Token_withdrawExitEventOccurrence,
)
Token_withdrawEntryEventOccurrence_strategy = st.builds(
    Token_withdrawEntryEventOccurrence,
)
Token_transferExitEventOccurrence_strategy = st.builds(
    Token_transferExitEventOccurrence,
)
Token_transferEntryEventOccurrence_strategy = st.builds(
    Token_transferEntryEventOccurrence,
)
BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
)
BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
)
BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_evaluateOREntryEventOccurrence,
)
BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_evaluateANDExitEventOccurrence,
)
BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
)
BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
)
BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
)
BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
)
IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
)
BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
)
IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
)
IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
)
IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
)
IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
)
IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
)
IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
)
IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
)
IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
)
IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(
    IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
)
IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
)
IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
)
IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
)
IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_evaluateADDExitEventOccurrence,
)
StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
)
IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
)
IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
)
IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
)
BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy = st.builds(
    BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
)
BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy = st.builds(
    BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
)
BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy = st.builds(
    BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
)
BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy = st.builds(
    BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
)
StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
)
StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
)
StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
)
InitialNode_fire_initialNodeExitEventOccurrence_strategy = st.builds(
    InitialNode_fire_initialNodeExitEventOccurrence,
)
IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
)
InitialNode_fire_initialNodeEntryEventOccurrence_strategy = st.builds(
    InitialNode_fire_initialNodeEntryEventOccurrence,
)
IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
)
IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
)
DecisionNode_fire_decisionNodeExitEventOccurrence_strategy = st.builds(
    DecisionNode_fire_decisionNodeExitEventOccurrence,
)
DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy = st.builds(
    DecisionNode_fire_decisionNodeEntryEventOccurrence,
)
MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy = st.builds(
    MergeNode_hasOffers_mergeNodeExitEventOccurrence,
)
MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy = st.builds(
    MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
)
ForkNode_fire_forkNodeExitEventOccurrence_strategy = st.builds(
    ForkNode_fire_forkNodeExitEventOccurrence,
)
ForkNode_fire_forkNodeEntryEventOccurrence_strategy = st.builds(
    ForkNode_fire_forkNodeEntryEventOccurrence,
)
ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy = st.builds(
    ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
)
ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
)
Action_isReady_actionEntryEventOccurrence_strategy = st.builds(
    Action_isReady_actionEntryEventOccurrence,
)
Action_sendOffers_actionExitEventOccurrence_strategy = st.builds(
    Action_sendOffers_actionExitEventOccurrence,
)
Action_sendOffers_actionEntryEventOccurrence_strategy = st.builds(
    Action_sendOffers_actionEntryEventOccurrence,
)
ControlNode_fire_controlNodeExitEventOccurrence_strategy = st.builds(
    ControlNode_fire_controlNodeExitEventOccurrence,
)
InitialNode_isReady_InitialNodeExitEventOccurrence_strategy = st.builds(
    InitialNode_isReady_InitialNodeExitEventOccurrence,
)
InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy = st.builds(
    InitialNode_isReady_InitialNodeEntryEventOccurrence,
)
OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy = st.builds(
    OpaqueAction_doAction_opaqueActionExitEventOccurrence,
)
OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy = st.builds(
    OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
)
Action_fire_actionExitEventOccurrence_strategy = st.builds(
    Action_fire_actionExitEventOccurrence,
)
Action_fire_actionEntryEventOccurrence_strategy = st.builds(
    Action_fire_actionEntryEventOccurrence,
)
ActivityNode_isReadyExitEventOccurrence_strategy = st.builds(
    ActivityNode_isReadyExitEventOccurrence,
)
Action_isReady_actionExitEventOccurrence_strategy = st.builds(
    Action_isReady_actionExitEventOccurrence,
)
ActivityNode_isReadyEntryEventOccurrence_strategy = st.builds(
    ActivityNode_isReadyEntryEventOccurrence,
)
ControlNode_fire_controlNodeEntryEventOccurrence_strategy = st.builds(
    ControlNode_fire_controlNodeEntryEventOccurrence,
)
ControlNode_isReady_ControlNodeExitEventOccurrence_strategy = st.builds(
    ControlNode_isReady_ControlNodeExitEventOccurrence,
)
ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy = st.builds(
    ControlNode_isReady_ControlNodeEntryEventOccurrence,
)
ActivityEdge_hasOfferExitEventOccurrence_strategy = st.builds(
    ActivityEdge_hasOfferExitEventOccurrence,
)
ActivityEdge_hasOfferEntryEventOccurrence_strategy = st.builds(
    ActivityEdge_hasOfferEntryEventOccurrence,
)
ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy = st.builds(
    ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
)
ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy = st.builds(
    ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
)
ActivityEdge_sendOfferExitEventOccurrence_strategy = st.builds(
    ActivityEdge_sendOfferExitEventOccurrence,
)
ActivityEdge_sendOfferEntryEventOccurrence_strategy = st.builds(
    ActivityEdge_sendOfferEntryEventOccurrence,
)
ActivityNode_isRunningExitEventOccurrence_strategy = st.builds(
    ActivityNode_isRunningExitEventOccurrence,
)
ActivityNode_isRunningEntryEventOccurrence_strategy = st.builds(
    ActivityNode_isRunningEntryEventOccurrence,
)
ActivityNode_run_activityNodeExitEventOccurrence_strategy = st.builds(
    ActivityNode_run_activityNodeExitEventOccurrence,
)
ActivityNode_hasOffersExitEventOccurrence_strategy = st.builds(
    ActivityNode_hasOffersExitEventOccurrence,
)
ActivityNode_run_activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode_run_activityNodeEntryEventOccurrence,
)
ActivityNode_hasOffersEntryEventOccurrence_strategy = st.builds(
    ActivityNode_hasOffersEntryEventOccurrence,
)
ActivityNode_removeTokenExitEventOccurrence_strategy = st.builds(
    ActivityNode_removeTokenExitEventOccurrence,
)
ActivityNode_removeTokenEntryEventOccurrence_strategy = st.builds(
    ActivityNode_removeTokenEntryEventOccurrence,
)
ActivityNode_addTokensExitEventOccurrence_strategy = st.builds(
    ActivityNode_addTokensExitEventOccurrence,
)
ActivityNode_addTokensEntryEventOccurrence_strategy = st.builds(
    ActivityNode_addTokensEntryEventOccurrence,
)
ActivityNode_takeOfferedTokensExitEventOccurrence_strategy = st.builds(
    ActivityNode_takeOfferedTokensExitEventOccurrence,
)
ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy = st.builds(
    ActivityNode_takeOfferedTokensEntryEventOccurrence,
)
ActivityNode_sendOffersExitEventOccurrence_strategy = st.builds(
    ActivityNode_sendOffersExitEventOccurrence,
)
ActivityNode_sendOffersEntryEventOccurrence_strategy = st.builds(
    ActivityNode_sendOffersEntryEventOccurrence,
)
ActivityNode_terminate_activityNodeExitEventOccurrence_strategy = st.builds(
    ActivityNode_terminate_activityNodeExitEventOccurrence,
)
ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode_terminate_activityNodeEntryEventOccurrence,
)
Activity_runNodesExitEventOccurrence_strategy = st.builds(
    Activity_runNodesExitEventOccurrence,
)
Activity_runNodesEntryEventOccurrence_strategy = st.builds(
    Activity_runNodesEntryEventOccurrence,
)
Activity_runExitEventOccurrence_strategy = st.builds(
    Activity_runExitEventOccurrence,
)
Activity_runEntryEventOccurrence_strategy = st.builds(
    Activity_runEntryEventOccurrence,
)
Activity_initializeExitEventOccurrence_strategy = st.builds(
    Activity_initializeExitEventOccurrence,
)
Activity_initializeEntryEventOccurrence_strategy = st.builds(
    Activity_initializeEntryEventOccurrence,
)
Activity_fireNodeExitEventOccurrence_strategy = st.builds(
    Activity_fireNodeExitEventOccurrence,
)
Activity_fireNodeEntryEventOccurrence_strategy = st.builds(
    Activity_fireNodeEntryEventOccurrence,
)
Activity_getInitialNodeExitEventOccurrence_strategy = st.builds(
    Activity_getInitialNodeExitEventOccurrence,
)
Activity_getInitialNodeEntryEventOccurrence_strategy = st.builds(
    Activity_getInitialNodeEntryEventOccurrence,
)
Activity_terminateExitEventOccurrence_strategy = st.builds(
    Activity_terminateExitEventOccurrence,
)
Activity_terminateEntryEventOccurrence_strategy = st.builds(
    Activity_terminateEntryEventOccurrence,
)
Activity_selectNextNodeExitEventOccurrence_strategy = st.builds(
    Activity_selectNextNodeExitEventOccurrence,
)
Activity_selectNextNodeEntryEventOccurrence_strategy = st.builds(
    Activity_selectNextNodeEntryEventOccurrence,
)
Activity_getEnabledNodesExitEventOccurrence_strategy = st.builds(
    Activity_getEnabledNodesExitEventOccurrence,
)
Activity_getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    Activity_getEnabledNodesEntryEventOccurrence,
)
Activity_fireInitialNodeExitEventOccurrence_strategy = st.builds(
    Activity_fireInitialNodeExitEventOccurrence,
)
ActivityNode_heldTokens_State_strategy = st.builds(
    ActivityNode_heldTokens_State,
)
Activity_fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    Activity_fireInitialNodeEntryEventOccurrence,
)
ActivityNode_running_State_strategy = st.builds(
    ActivityNode_running_State,
)
Activity_mainExitEventOccurrence_strategy = st.builds(
    Activity_mainExitEventOccurrence,
)
Activity_mainEntryEventOccurrence_strategy = st.builds(
    Activity_mainEntryEventOccurrence,
)
trace_Events_Events_strategy = st.builds(
    trace_Events_Events,
)
Events_trace_GlobalState_strategy = st.builds(
    Events_trace_GlobalState,
)
trace_Events_EventOccurrence_strategy = st.builds(
    trace_Events_EventOccurrence,
)
trace_IntegerCalculationExpression_strategy = st.builds(
    trace_IntegerCalculationExpression,
)
trace_BooleanUnaryExpression_strategy = st.builds(
    trace_BooleanUnaryExpression,
)
trace_IntegerComparisonExpression_strategy = st.builds(
    trace_IntegerComparisonExpression,
)
trace_BooleanValue_strategy = st.builds(
    trace_BooleanValue,
)
trace_IntegerValue_strategy = st.builds(
    trace_IntegerValue,
)
trace_StringValue_strategy = st.builds(
    trace_StringValue,
)
trace_BooleanBinaryExpression_strategy = st.builds(
    trace_BooleanBinaryExpression,
)
Trace_executedNodes_State_strategy = st.builds(
    Trace_executedNodes_State,
)
Activity_trace_State_strategy = st.builds(
    Activity_trace_State,
)
trace_Trace_strategy = st.builds(
    trace_Trace,
)
Offer_offeredTokens_State_strategy = st.builds(
    Offer_offeredTokens_State,
)
Variable_currentValue_State_strategy = st.builds(
    Variable_currentValue_State,
)
ActivityEdge_offers_State_strategy = st.builds(
    ActivityEdge_offers_State,
)
ForkedToken_baseTokenIsWithdrawn_State_strategy = st.builds(
    ForkedToken_baseTokenIsWithdrawn_State,
)
ForkedToken_baseToken_State_strategy = st.builds(
    ForkedToken_baseToken_State,
)
ForkedToken_remainingOffersCount_State_strategy = st.builds(
    ForkedToken_remainingOffersCount_State,
)
Input_inputValues_State_strategy = st.builds(
    Input_inputValues_State,
)
Token_holder_State_strategy = st.builds(
    Token_holder_State,
)
InputValue_variable_State_strategy = st.builds(
    InputValue_variable_State,
)
InputValue_value_State_strategy = st.builds(
    InputValue_value_State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
trace_Events_ActivityNode_isReadyEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_isReadyEntryEventOccurrence,
)
trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence,
)
trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence,
)
trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence,
)
trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ControlNode_fire_controlNodeExitEventOccurrence,
)
trace_Events_ActivityNode_isRunningExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_isRunningExitEventOccurrence,
)
trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence,
)
trace_Events_Activity_fireInitialNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_fireInitialNodeExitEventOccurrence,
)
trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence,
)
trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence,
)
trace_Events_ActivityNode_removeTokenExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_removeTokenExitEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence,
)
trace_Events_Activity_fireNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_fireNodeEntryEventOccurrence,
)
trace_Events_Action_isReady_actionExitEventOccurrence_strategy = st.builds(
    trace_Events_Action_isReady_actionExitEventOccurrence,
)
trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ForkNode_fire_forkNodeExitEventOccurrence,
)
trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence,
)
trace_Events_Activity_runNodesExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_runNodesExitEventOccurrence,
)
trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_InitialNode_fire_initialNodeExitEventOccurrence,
)
trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence,
)
trace_Events_ActivityNode_isReadyExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_isReadyExitEventOccurrence,
)
trace_Events_Activity_mainEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_mainEntryEventOccurrence,
)
trace_Events_ActivityNode_sendOffersEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_sendOffersEntryEventOccurrence,
)
trace_Events_Action_sendOffers_actionEntryEventOccurrence_strategy = st.builds(
    trace_Events_Action_sendOffers_actionEntryEventOccurrence,
)
trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence,
)
trace_Events_Activity_fireNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_fireNodeExitEventOccurrence,
)
trace_Events_ActivityNode_addTokensExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_addTokensExitEventOccurrence,
)
trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence,
)
trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy = st.builds(
    trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence,
)
trace_Events_Activity_runNodesEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_runNodesEntryEventOccurrence,
)
trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence,
)
trace_Events_ActivityNode_hasOffersExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_hasOffersExitEventOccurrence,
)
trace_Events_Activity_selectNextNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_selectNextNodeEntryEventOccurrence,
)
trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence,
)
trace_Events_Activity_getEnabledNodesExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_getEnabledNodesExitEventOccurrence,
)
trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence,
)
trace_Events_ActivityNode_removeTokenEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_removeTokenEntryEventOccurrence,
)
trace_Events_Activity_terminateEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_terminateEntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence,
)
trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence,
)
trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence,
)
trace_Events_Token_withdrawExitEventOccurrence_strategy = st.builds(
    trace_Events_Token_withdrawExitEventOccurrence,
)
trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence,
)
trace_Events_Offer_hasTokensEntryEventOccurrence_strategy = st.builds(
    trace_Events_Offer_hasTokensEntryEventOccurrence,
)
trace_Events_Activity_runExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_runExitEventOccurrence,
)
trace_Events_Activity_getInitialNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_getInitialNodeExitEventOccurrence,
)
trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence,
)
trace_Events_Activity_initializeEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_initializeEntryEventOccurrence,
)
trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence,
)
trace_Events_ActivityNode_hasOffersEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_hasOffersEntryEventOccurrence,
)
trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence,
)
trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence,
)
trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_hasOfferEntryEventOccurrence,
)
trace_Events_Activity_fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_fireInitialNodeEntryEventOccurrence,
)
trace_Events_Action_fire_actionEntryEventOccurrence_strategy = st.builds(
    trace_Events_Action_fire_actionEntryEventOccurrence,
)
trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence,
)
trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence,
)
trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence,
)
trace_Events_Activity_mainExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_mainExitEventOccurrence,
)
trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence,
)
trace_Events_Activity_initializeExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_initializeExitEventOccurrence,
)
trace_Events_ActivityNode_sendOffersExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_sendOffersExitEventOccurrence,
)
trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence,
)
trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence,
)
trace_Events_Token_transferExitEventOccurrence_strategy = st.builds(
    trace_Events_Token_transferExitEventOccurrence,
)
trace_Events_Activity_getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_getEnabledNodesEntryEventOccurrence,
)
trace_Events_ActivityEdge_hasOfferExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_hasOfferExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence,
)
trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence,
)
trace_Events_Token_transferEntryEventOccurrence_strategy = st.builds(
    trace_Events_Token_transferEntryEventOccurrence,
)
trace_Events_Action_sendOffers_actionExitEventOccurrence_strategy = st.builds(
    trace_Events_Action_sendOffers_actionExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence,
)
trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_run_activityNodeExitEventOccurrence,
)
trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence,
)
trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence,
)
trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence,
)
trace_Events_Activity_runEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_runEntryEventOccurrence,
)
trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence,
)
trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence,
)
trace_Events_Token_isWithdrawnEntryEventOccurrence_strategy = st.builds(
    trace_Events_Token_isWithdrawnEntryEventOccurrence,
)
trace_Events_Activity_getInitialNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_Activity_getInitialNodeEntryEventOccurrence,
)
trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence,
)
trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy = st.builds(
    trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence,
)
trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence,
)
trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence,
)
trace_Events_Token_isWithdrawnExitEventOccurrence_strategy = st.builds(
    trace_Events_Token_isWithdrawnExitEventOccurrence,
)
trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence,
)
trace_Events_Action_isReady_actionEntryEventOccurrence_strategy = st.builds(
    trace_Events_Action_isReady_actionEntryEventOccurrence,
)
trace_Events_Activity_terminateExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_terminateExitEventOccurrence,
)
trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence,
)
trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy = st.builds(
    trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence,
)
trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence,
)
trace_Events_ActivityNode_addTokensEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_addTokensEntryEventOccurrence,
)
trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence,
)
trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence,
)
trace_Events_Action_fire_actionExitEventOccurrence_strategy = st.builds(
    trace_Events_Action_fire_actionExitEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence,
)
trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_sendOfferEntryEventOccurrence,
)
trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence,
)
trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy = st.builds(
    trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence,
)
trace_Events_Offer_hasTokensExitEventOccurrence_strategy = st.builds(
    trace_Events_Offer_hasTokensExitEventOccurrence,
)
trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence,
)
trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence,
)
trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence,
)
trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence,
)
trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy = st.builds(
    trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence,
)
trace_Events_Token_withdrawEntryEventOccurrence_strategy = st.builds(
    trace_Events_Token_withdrawEntryEventOccurrence,
)
trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence,
)
trace_Events_ActivityNode_isRunningEntryEventOccurrence_strategy = st.builds(
    trace_Events_ActivityNode_isRunningEntryEventOccurrence,
)
trace_Events_ActivityEdge_sendOfferExitEventOccurrence_strategy = st.builds(
    trace_Events_ActivityEdge_sendOfferExitEventOccurrence,
)
trace_Events_Activity_selectNextNodeExitEventOccurrence_strategy = st.builds(
    trace_Events_Activity_selectNextNodeExitEventOccurrence,
)
trace_StaticObjectsPools_strategy = st.builds(
    trace_StaticObjectsPools,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)
Events_strategy = st.builds(
    Events,
)
trace_GlobalState_strategy = st.builds(
    trace_GlobalState,
)

@given(instance=Events_trace_Value_strategy)
@settings(max_examples=50)
def test_events_trace_value_instantiation(instance):
    assert isinstance(instance, Events_trace_Value)

@given(instance=activitydiagram_TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedintegervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedIntegerVariable)

@given(instance=activitydiagram_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedDecisionNode)

@given(instance=activitydiagram_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedmergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedMergeNode)

@given(instance=activitydiagram_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedInitialNode)

@given(instance=activitydiagram_TracedForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedforknode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedForkNode)

@given(instance=activitydiagram_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityFinalNode)

@given(instance=activitydiagram_TracedAction_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedaction_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedAction)

@given(instance=activitydiagram_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedOpaqueAction)

@given(instance=activitydiagramConfiguration_TracedToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedToken)

@given(instance=activitydiagram_TracedControlNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedControlNode)

@given(instance=activitydiagram_TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityEdge)

@given(instance=activitydiagram_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivityNode)

@given(instance=trace_activitydiagramConfiguration_TracedOffer_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedoffer_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedOffer)

@given(instance=trace_activitydiagramConfiguration_TracedInput_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedinput_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedInput)

@given(instance=TracedToken_strategy)
@settings(max_examples=50)
def test_tracedtoken_instantiation(instance):
    assert isinstance(instance, TracedToken)

@given(instance=trace_activitydiagramConfiguration_TracedForkedToken_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedForkedToken)

@given(instance=trace_activitydiagramConfiguration_TracedControlToken_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedControlToken)

@given(instance=trace_activitydiagramConfiguration_TracedToken_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedtoken_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedToken)

@given(instance=trace_activitydiagramConfiguration_TracedInputValue_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedinputvalue_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedInputValue)

@given(instance=activitydiagram_trace_DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_DecisionNode)

@given(instance=activitydiagram_trace_JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_JoinNode)

@given(instance=activitydiagram_trace_OpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_opaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_OpaqueAction)

@given(instance=trace_activitydiagramConfiguration_TracedTrace_strategy)
@settings(max_examples=50)
def test_trace_activitydiagramconfiguration_tracedtrace_instantiation(instance):
    assert isinstance(instance, trace_activitydiagramConfiguration_TracedTrace)

@given(instance=activitydiagram_trace_InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_InitialNode)

@given(instance=activitydiagram_trace_ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ForkNode)

@given(instance=activitydiagram_trace_ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ActivityFinalNode)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=trace_activitydiagram_TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityFinalNode)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=activitydiagram_trace_Expression_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_expression_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Expression)

@given(instance=trace_activitydiagram_TracedAction_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedaction_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedAction)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=trace_activitydiagram_TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedOpaqueAction)

@given(instance=activitydiagram_trace_StringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_stringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_StringVariable)

@given(instance=activitydiagram_trace_Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_activity_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Activity)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=trace_activitydiagram_TracedActivity_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedactivity_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivity)

@given(instance=trace_activitydiagram_TracedActivityNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityNode)

@given(instance=trace_activitydiagram_TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedActivityEdge)

@given(instance=activitydiagram_trace_IntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_integervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_IntegerVariable)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=trace_activitydiagram_TracedControlNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedControlNode)

@given(instance=trace_activitydiagram_TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedExecutableNode)

@given(instance=activitydiagram_trace_BooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_booleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_BooleanVariable)

@given(instance=TracedVariable_strategy)
@settings(max_examples=50)
def test_tracedvariable_instantiation(instance):
    assert isinstance(instance, TracedVariable)

@given(instance=trace_activitydiagram_TracedStringVariable_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedstringvariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedStringVariable)

@given(instance=trace_activitydiagram_TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedintegervariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedIntegerVariable)

@given(instance=trace_activitydiagram_TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedBooleanVariable)

@given(instance=activitydiagram_trace_MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_MergeNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=trace_activitydiagram_TracedForkNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedforknode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedForkNode)

@given(instance=trace_activitydiagram_TracedInitialNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedinitialnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedInitialNode)

@given(instance=trace_activitydiagram_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedJoinNode)

@given(instance=trace_activitydiagram_TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_traceddecisionnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedDecisionNode)

@given(instance=trace_activitydiagram_TracedFinalNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedFinalNode)

@given(instance=trace_activitydiagram_TracedMergeNode_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedmergenode_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedMergeNode)

@given(instance=activitydiagram_trace_ControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_controlflow_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_ControlFlow)

@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)

@given(instance=trace_activitydiagram_TracedControlFlow_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedControlFlow)

@given(instance=activitydiagram_TracedJoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedjoinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedJoinNode)

@given(instance=activitydiagram_trace_Value_strategy)
@settings(max_examples=50)
def test_activitydiagram_trace_value_instantiation(instance):
    assert isinstance(instance, activitydiagram_trace_Value)

@given(instance=trace_activitydiagram_TracedVariable_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracedvariable_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedVariable)

@given(instance=trace_activitydiagram_TracedNamedElement_strategy)
@settings(max_examples=50)
def test_trace_activitydiagram_tracednamedelement_instantiation(instance):
    assert isinstance(instance, trace_activitydiagram_TracedNamedElement)



@given(instance=trace_activitydiagram_TracedNamedElement_strategy)
def test_trace_activitydiagram_tracednamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activitydiagramConfiguration_TracedControlToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedControlToken)

@given(instance=activitydiagram_TracedControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedControlFlow)

@given(instance=trace_Traced_TracedObjects_strategy)
@settings(max_examples=50)
def test_trace_traced_tracedobjects_instantiation(instance):
    assert isinstance(instance, trace_Traced_TracedObjects)

@given(instance=activitydiagramConfiguration_TracedTrace_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedtrace_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedTrace)

@given(instance=trace_States_Activity_trace_State_strategy)
@settings(max_examples=50)
def test_trace_states_activity_trace_state_instantiation(instance):
    assert isinstance(instance, trace_States_Activity_trace_State)

@given(instance=trace_States_ActivityNode_heldTokens_State_strategy)
@settings(max_examples=50)
def test_trace_states_activitynode_heldtokens_state_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityNode_heldTokens_State)

@given(instance=trace_States_ActivityNode_running_State_strategy)
@settings(max_examples=50)
def test_trace_states_activitynode_running_state_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityNode_running_State)



@given(instance=trace_States_ActivityNode_running_State_strategy)
def test_trace_states_activitynode_running_state_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=trace_States_Offer_offeredTokens_State_strategy)
@settings(max_examples=50)
def test_trace_states_offer_offeredtokens_state_instantiation(instance):
    assert isinstance(instance, trace_States_Offer_offeredTokens_State)

@given(instance=trace_States_Variable_currentValue_State_strategy)
@settings(max_examples=50)
def test_trace_states_variable_currentvalue_state_instantiation(instance):
    assert isinstance(instance, trace_States_Variable_currentValue_State)

@given(instance=trace_States_Trace_executedNodes_State_strategy)
@settings(max_examples=50)
def test_trace_states_trace_executednodes_state_instantiation(instance):
    assert isinstance(instance, trace_States_Trace_executedNodes_State)

@given(instance=trace_States_ForkedToken_baseTokenIsWithdrawn_State_strategy)
@settings(max_examples=50)
def test_trace_states_forkedtoken_basetokeniswithdrawn_state_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_baseTokenIsWithdrawn_State)



@given(instance=trace_States_ForkedToken_baseTokenIsWithdrawn_State_strategy)
def test_trace_states_forkedtoken_basetokeniswithdrawn_state_baseTokenIsWithdrawn_setter(instance):
    original = instance.baseTokenIsWithdrawn
    instance.baseTokenIsWithdrawn = original
    assert instance.baseTokenIsWithdrawn == original

@given(instance=trace_States_ForkedToken_baseToken_State_strategy)
@settings(max_examples=50)
def test_trace_states_forkedtoken_basetoken_state_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_baseToken_State)

@given(instance=trace_States_ForkedToken_remainingOffersCount_State_strategy)
@settings(max_examples=50)
def test_trace_states_forkedtoken_remainingofferscount_state_instantiation(instance):
    assert isinstance(instance, trace_States_ForkedToken_remainingOffersCount_State)



@given(instance=trace_States_ForkedToken_remainingOffersCount_State_strategy)
def test_trace_states_forkedtoken_remainingofferscount_state_remainingOffersCount_setter(instance):
    original = instance.remainingOffersCount
    instance.remainingOffersCount = original
    assert instance.remainingOffersCount == original

@given(instance=activitydiagramConfiguration_TracedInput_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedinput_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedInput)

@given(instance=trace_States_Input_inputValues_State_strategy)
@settings(max_examples=50)
def test_trace_states_input_inputvalues_state_instantiation(instance):
    assert isinstance(instance, trace_States_Input_inputValues_State)

@given(instance=trace_States_Token_holder_State_strategy)
@settings(max_examples=50)
def test_trace_states_token_holder_state_instantiation(instance):
    assert isinstance(instance, trace_States_Token_holder_State)

@given(instance=trace_States_ActivityEdge_offers_State_strategy)
@settings(max_examples=50)
def test_trace_states_activityedge_offers_state_instantiation(instance):
    assert isinstance(instance, trace_States_ActivityEdge_offers_State)

@given(instance=activitydiagramConfiguration_TracedInputValue_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedinputvalue_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedInputValue)

@given(instance=States_trace_Value_strategy)
@settings(max_examples=50)
def test_states_trace_value_instantiation(instance):
    assert isinstance(instance, States_trace_Value)

@given(instance=trace_States_InputValue_value_State_strategy)
@settings(max_examples=50)
def test_trace_states_inputvalue_value_state_instantiation(instance):
    assert isinstance(instance, trace_States_InputValue_value_State)

@given(instance=activitydiagramConfiguration_TracedOffer_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedoffer_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedOffer)

@given(instance=activitydiagramConfiguration_TracedForkedToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration_tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration_TracedForkedToken)

@given(instance=activitydiagram_TracedVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedVariable)

@given(instance=trace_States_InputValue_variable_State_strategy)
@settings(max_examples=50)
def test_trace_states_inputvalue_variable_state_instantiation(instance):
    assert isinstance(instance, trace_States_InputValue_variable_State)

@given(instance=States_trace_GlobalState_strategy)
@settings(max_examples=50)
def test_states_trace_globalstate_instantiation(instance):
    assert isinstance(instance, States_trace_GlobalState)

@given(instance=Events_trace_BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_events_trace_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, Events_trace_BooleanBinaryExpression)

@given(instance=Events_trace_BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_events_trace_booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, Events_trace_BooleanUnaryExpression)

@given(instance=Events_trace_IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_events_trace_integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerComparisonExpression)

@given(instance=Events_trace_IntegerExpression_strategy)
@settings(max_examples=50)
def test_events_trace_integerexpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerExpression)

@given(instance=activitydiagram_TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedBooleanVariable)

@given(instance=Events_trace_IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_events_trace_integercalculationexpression_instantiation(instance):
    assert isinstance(instance, Events_trace_IntegerCalculationExpression)

@given(instance=activitydiagram_TracedStringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedstringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedStringVariable)

@given(instance=Offer_hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_offer_hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Offer_hasTokensExitEventOccurrence)

@given(instance=Events_trace_EObject_strategy)
@settings(max_examples=50)
def test_events_trace_eobject_instantiation(instance):
    assert isinstance(instance, Events_trace_EObject)

@given(instance=activitydiagram_TracedActivity_strategy)
@settings(max_examples=50)
def test_activitydiagram_tracedactivity_instantiation(instance):
    assert isinstance(instance, activitydiagram_TracedActivity)

@given(instance=Token_isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_iswithdrawnexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_isWithdrawnExitEventOccurrence)

@given(instance=Token_isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_iswithdrawnentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_isWithdrawnEntryEventOccurrence)

@given(instance=BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_evaluateorexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateORExitEventOccurrence)

@given(instance=Offer_hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_offer_hastokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Offer_hasTokensEntryEventOccurrence)

@given(instance=ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_forkedtoken_withdraw_forkedtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken_withdraw_forkedTokenExitEventOccurrence)

@given(instance=ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_forkedtoken_withdraw_forkedtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken_withdraw_forkedTokenEntryEventOccurrence)

@given(instance=Token_withdrawExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_withdrawexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_withdrawExitEventOccurrence)

@given(instance=Token_withdrawEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_withdrawentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_withdrawEntryEventOccurrence)

@given(instance=Token_transferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_transferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_transferExitEventOccurrence)

@given(instance=Token_transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token_transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token_transferEntryEventOccurrence)

@given(instance=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression_evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)

@given(instance=BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)

@given(instance=BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_evaluateorentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateOREntryEventOccurrence)

@given(instance=BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_evaluateandexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateANDExitEventOccurrence)

@given(instance=BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_evaluateandentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_evaluateANDEntryEventOccurrence)

@given(instance=BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)

@given(instance=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)

@given(instance=BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression_evaluatenotexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_evaluateNOTExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)

@given(instance=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluateequalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluateequalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)

@given(instance=IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)

@given(instance=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)

@given(instance=IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integerexpression_getoperandcurrentvaluesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression_getOperandCurrentValuesExitEventOccurrence)

@given(instance=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_evaluatesmallerentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)

@given(instance=IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)

@given(instance=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)

@given(instance=IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_evaluatesubtractexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)

@given(instance=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)

@given(instance=IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateADDExitEventOccurrence)

@given(instance=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)

@given(instance=IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression_evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression_evaluateADDEntryEventOccurrence)

@given(instance=IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)

@given(instance=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integerexpression_getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)

@given(instance=BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)

@given(instance=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)

@given(instance=BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)

@given(instance=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)

@given(instance=StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)

@given(instance=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)

@given(instance=StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable_setCurrentValue_stringVariableExitEventOccurrence)

@given(instance=InitialNode_fire_initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode_fire_initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_fire_initialNodeExitEventOccurrence)

@given(instance=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)

@given(instance=InitialNode_fire_initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode_fire_initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_fire_initialNodeEntryEventOccurrence)

@given(instance=IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable_setcurrentvalue_integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)

@given(instance=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable_setcurrentvalue_integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)

@given(instance=DecisionNode_fire_decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_decisionnode_fire_decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode_fire_decisionNodeExitEventOccurrence)

@given(instance=DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_decisionnode_fire_decisionnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode_fire_decisionNodeEntryEventOccurrence)

@given(instance=MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_mergenode_hasoffers_mergenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode_hasOffers_mergeNodeExitEventOccurrence)

@given(instance=MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_mergenode_hasoffers_mergenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode_hasOffers_mergeNodeEntryEventOccurrence)

@given(instance=ForkNode_fire_forkNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_forknode_fire_forknodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode_fire_forkNodeExitEventOccurrence)

@given(instance=ForkNode_fire_forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_forknode_fire_forknodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode_fire_forkNodeEntryEventOccurrence)

@given(instance=ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)

@given(instance=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)

@given(instance=Action_isReady_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_isready_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_isReady_actionEntryEventOccurrence)

@given(instance=Action_sendOffers_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_sendoffers_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_sendOffers_actionExitEventOccurrence)

@given(instance=Action_sendOffers_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_sendoffers_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_sendOffers_actionEntryEventOccurrence)

@given(instance=ControlNode_fire_controlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode_fire_controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_fire_controlNodeExitEventOccurrence)

@given(instance=InitialNode_isReady_InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode_isready_initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_isReady_InitialNodeExitEventOccurrence)

@given(instance=InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode_isready_initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode_isReady_InitialNodeEntryEventOccurrence)

@given(instance=OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_opaqueaction_doaction_opaqueactionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction_doAction_opaqueActionExitEventOccurrence)

@given(instance=OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_opaqueaction_doaction_opaqueactionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction_doAction_opaqueActionEntryEventOccurrence)

@given(instance=Action_fire_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_fire_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_fire_actionExitEventOccurrence)

@given(instance=Action_fire_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_fire_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_fire_actionEntryEventOccurrence)

@given(instance=ActivityNode_isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isReadyExitEventOccurrence)

@given(instance=Action_isReady_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action_isready_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action_isReady_actionExitEventOccurrence)

@given(instance=ActivityNode_isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isReadyEntryEventOccurrence)

@given(instance=ControlNode_fire_controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode_fire_controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_fire_controlNodeEntryEventOccurrence)

@given(instance=ControlNode_isReady_ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode_isready_controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_isReady_ControlNodeExitEventOccurrence)

@given(instance=ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode_isready_controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode_isReady_ControlNodeEntryEventOccurrence)

@given(instance=ActivityEdge_hasOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_hasofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_hasOfferExitEventOccurrence)

@given(instance=ActivityEdge_hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_hasofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_hasOfferEntryEventOccurrence)

@given(instance=ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)

@given(instance=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)

@given(instance=ActivityEdge_sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_sendOfferExitEventOccurrence)

@given(instance=ActivityEdge_sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge_sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge_sendOfferEntryEventOccurrence)

@given(instance=ActivityNode_isRunningExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_isrunningexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isRunningExitEventOccurrence)

@given(instance=ActivityNode_isRunningEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_isrunningentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_isRunningEntryEventOccurrence)

@given(instance=ActivityNode_run_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_run_activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_run_activityNodeExitEventOccurrence)

@given(instance=ActivityNode_hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_hasOffersExitEventOccurrence)

@given(instance=ActivityNode_run_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_run_activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_run_activityNodeEntryEventOccurrence)

@given(instance=ActivityNode_hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_hasoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_hasOffersEntryEventOccurrence)

@given(instance=ActivityNode_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_removeTokenExitEventOccurrence)

@given(instance=ActivityNode_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_removeTokenEntryEventOccurrence)

@given(instance=ActivityNode_addTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_addtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_addTokensExitEventOccurrence)

@given(instance=ActivityNode_addTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_addtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_addTokensEntryEventOccurrence)

@given(instance=ActivityNode_takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_takeofferedtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_takeOfferedTokensExitEventOccurrence)

@given(instance=ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_takeofferedtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_takeOfferedTokensEntryEventOccurrence)

@given(instance=ActivityNode_sendOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_sendoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_sendOffersExitEventOccurrence)

@given(instance=ActivityNode_sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_sendoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_sendOffersEntryEventOccurrence)

@given(instance=ActivityNode_terminate_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_terminate_activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_terminate_activityNodeExitEventOccurrence)

@given(instance=ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode_terminate_activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode_terminate_activityNodeEntryEventOccurrence)

@given(instance=Activity_runNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_runnodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runNodesExitEventOccurrence)

@given(instance=Activity_runNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_runnodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runNodesEntryEventOccurrence)

@given(instance=Activity_runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runExitEventOccurrence)

@given(instance=Activity_runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_runEntryEventOccurrence)

@given(instance=Activity_initializeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_initializeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_initializeExitEventOccurrence)

@given(instance=Activity_initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_initializeEntryEventOccurrence)

@given(instance=Activity_fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireNodeExitEventOccurrence)

@given(instance=Activity_fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_firenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireNodeEntryEventOccurrence)

@given(instance=Activity_getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_getinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getInitialNodeExitEventOccurrence)

@given(instance=Activity_getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_getinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getInitialNodeEntryEventOccurrence)

@given(instance=Activity_terminateExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_terminateexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_terminateExitEventOccurrence)

@given(instance=Activity_terminateEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_terminateentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_terminateEntryEventOccurrence)

@given(instance=Activity_selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_selectnextnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_selectNextNodeExitEventOccurrence)

@given(instance=Activity_selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_selectnextnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_selectNextNodeEntryEventOccurrence)

@given(instance=Activity_getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_getenablednodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getEnabledNodesExitEventOccurrence)

@given(instance=Activity_getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_getenablednodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_getEnabledNodesEntryEventOccurrence)

@given(instance=Activity_fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_fireinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireInitialNodeExitEventOccurrence)

@given(instance=ActivityNode_heldTokens_State_strategy)
@settings(max_examples=50)
def test_activitynode_heldtokens_state_instantiation(instance):
    assert isinstance(instance, ActivityNode_heldTokens_State)

@given(instance=Activity_fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_fireInitialNodeEntryEventOccurrence)

@given(instance=ActivityNode_running_State_strategy)
@settings(max_examples=50)
def test_activitynode_running_state_instantiation(instance):
    assert isinstance(instance, ActivityNode_running_State)

@given(instance=Activity_mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_mainExitEventOccurrence)

@given(instance=Activity_mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity_mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity_mainEntryEventOccurrence)

@given(instance=trace_Events_Events_strategy)
@settings(max_examples=50)
def test_trace_events_events_instantiation(instance):
    assert isinstance(instance, trace_Events_Events)

@given(instance=Events_trace_GlobalState_strategy)
@settings(max_examples=50)
def test_events_trace_globalstate_instantiation(instance):
    assert isinstance(instance, Events_trace_GlobalState)

@given(instance=trace_Events_EventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_eventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_EventOccurrence)

@given(instance=trace_IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_trace_integercalculationexpression_instantiation(instance):
    assert isinstance(instance, trace_IntegerCalculationExpression)

@given(instance=trace_BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_trace_booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, trace_BooleanUnaryExpression)

@given(instance=trace_IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_trace_integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, trace_IntegerComparisonExpression)

@given(instance=trace_BooleanValue_strategy)
@settings(max_examples=50)
def test_trace_booleanvalue_instantiation(instance):
    assert isinstance(instance, trace_BooleanValue)

@given(instance=trace_IntegerValue_strategy)
@settings(max_examples=50)
def test_trace_integervalue_instantiation(instance):
    assert isinstance(instance, trace_IntegerValue)

@given(instance=trace_StringValue_strategy)
@settings(max_examples=50)
def test_trace_stringvalue_instantiation(instance):
    assert isinstance(instance, trace_StringValue)

@given(instance=trace_BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_trace_booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, trace_BooleanBinaryExpression)

@given(instance=Trace_executedNodes_State_strategy)
@settings(max_examples=50)
def test_trace_executednodes_state_instantiation(instance):
    assert isinstance(instance, Trace_executedNodes_State)

@given(instance=Activity_trace_State_strategy)
@settings(max_examples=50)
def test_activity_trace_state_instantiation(instance):
    assert isinstance(instance, Activity_trace_State)

@given(instance=trace_Trace_strategy)
@settings(max_examples=50)
def test_trace_trace_instantiation(instance):
    assert isinstance(instance, trace_Trace)

@given(instance=Offer_offeredTokens_State_strategy)
@settings(max_examples=50)
def test_offer_offeredtokens_state_instantiation(instance):
    assert isinstance(instance, Offer_offeredTokens_State)

@given(instance=Variable_currentValue_State_strategy)
@settings(max_examples=50)
def test_variable_currentvalue_state_instantiation(instance):
    assert isinstance(instance, Variable_currentValue_State)

@given(instance=ActivityEdge_offers_State_strategy)
@settings(max_examples=50)
def test_activityedge_offers_state_instantiation(instance):
    assert isinstance(instance, ActivityEdge_offers_State)

@given(instance=ForkedToken_baseTokenIsWithdrawn_State_strategy)
@settings(max_examples=50)
def test_forkedtoken_basetokeniswithdrawn_state_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseTokenIsWithdrawn_State)

@given(instance=ForkedToken_baseToken_State_strategy)
@settings(max_examples=50)
def test_forkedtoken_basetoken_state_instantiation(instance):
    assert isinstance(instance, ForkedToken_baseToken_State)

@given(instance=ForkedToken_remainingOffersCount_State_strategy)
@settings(max_examples=50)
def test_forkedtoken_remainingofferscount_state_instantiation(instance):
    assert isinstance(instance, ForkedToken_remainingOffersCount_State)

@given(instance=Input_inputValues_State_strategy)
@settings(max_examples=50)
def test_input_inputvalues_state_instantiation(instance):
    assert isinstance(instance, Input_inputValues_State)

@given(instance=Token_holder_State_strategy)
@settings(max_examples=50)
def test_token_holder_state_instantiation(instance):
    assert isinstance(instance, Token_holder_State)

@given(instance=InputValue_variable_State_strategy)
@settings(max_examples=50)
def test_inputvalue_variable_state_instantiation(instance):
    assert isinstance(instance, InputValue_variable_State)

@given(instance=InputValue_value_State_strategy)
@settings(max_examples=50)
def test_inputvalue_value_state_instantiation(instance):
    assert isinstance(instance, InputValue_value_State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=trace_Events_ActivityNode_isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isReadyEntryEventOccurrence)

@given(instance=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_takeofferedtokens_activityedgeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_execute_integercalculationexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_evaluatesubtractexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)

@given(instance=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_takeofferedtokens_activityedgeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)

@given(instance=trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityfinalnode_fire_activityfinalnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)

@given(instance=trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_controlnode_fire_controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_fire_controlNodeExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_isRunningExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_isrunningexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isRunningExitEventOccurrence)

@given(instance=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integervariable_getcurrentvaluevalue_integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)

@given(instance=trace_Events_Activity_fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_fireinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireInitialNodeExitEventOccurrence)

@given(instance=trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integervariable_setcurrentvalue_integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_removeTokenExitEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluategreater_equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)

@given(instance=trace_Events_Activity_fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_firenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireNodeEntryEventOccurrence)

@given(instance=trace_Events_Action_isReady_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_isready_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_isReady_actionExitEventOccurrence)

@given(instance=trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_forknode_fire_forknodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkNode_fire_forkNodeExitEventOccurrence)

@given(instance=trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)

@given(instance=trace_Events_Activity_runNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_runnodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runNodesExitEventOccurrence)

@given(instance=trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_initialnode_fire_initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_fire_initialNodeExitEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_evaluateandexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isReadyExitEventOccurrence)

@given(instance=trace_Events_Activity_mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_mainEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_sendoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_sendOffersEntryEventOccurrence)

@given(instance=trace_Events_Action_sendOffers_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_sendoffers_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_sendOffers_actionEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_takeofferedtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)

@given(instance=trace_Events_Activity_fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireNodeExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_addTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_addtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_addTokensExitEventOccurrence)

@given(instance=trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_mergenode_hasoffers_mergenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)

@given(instance=trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_forkedtoken_withdraw_forkedtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)

@given(instance=trace_Events_Activity_runNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_runnodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runNodesEntryEventOccurrence)

@given(instance=trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_decisionnode_fire_decisionnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_hasOffersExitEventOccurrence)

@given(instance=trace_Events_Activity_selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_selectnextnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_selectNextNodeEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_run_activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluategreater_equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)

@given(instance=trace_Events_Activity_getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_getenablednodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getEnabledNodesExitEventOccurrence)

@given(instance=trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_mergenode_hasoffers_mergenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_removeTokenEntryEventOccurrence)

@given(instance=trace_Events_Activity_terminateEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_terminateentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_terminateEntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)

@given(instance=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)

@given(instance=trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_initialnode_fire_initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence)

@given(instance=trace_Events_Token_withdrawExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_withdrawexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_withdrawExitEventOccurrence)

@given(instance=trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_stringvariable_setcurrentvalue_stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluatesmallerentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluateequalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)

@given(instance=trace_Events_Offer_hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_offer_hastokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Offer_hasTokensEntryEventOccurrence)

@given(instance=trace_Events_Activity_runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runExitEventOccurrence)

@given(instance=trace_Events_Activity_getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_getinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getInitialNodeExitEventOccurrence)

@given(instance=trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_controlnode_isready_controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)

@given(instance=trace_Events_Activity_initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_initializeEntryEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_execute_booleanbinaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_hasoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_hasOffersEntryEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_evaluateorentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_evaluateandentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)

@given(instance=trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_hasofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_hasOfferEntryEventOccurrence)

@given(instance=trace_Events_Activity_fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_fireInitialNodeEntryEventOccurrence)

@given(instance=trace_Events_Action_fire_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_fire_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_fire_actionEntryEventOccurrence)

@given(instance=trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityfinalnode_fire_activityfinalnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)

@given(instance=trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_controlnode_isready_controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)

@given(instance=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integervariable_getcurrentvaluevalue_integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)

@given(instance=trace_Events_Activity_mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_mainExitEventOccurrence)

@given(instance=trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_forknode_fire_forknodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence)

@given(instance=trace_Events_Activity_initializeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_initializeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_initializeExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_sendOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_sendoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_sendOffersExitEventOccurrence)

@given(instance=trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)

@given(instance=trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanvariable_setcurrentvalue_boolenvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)

@given(instance=trace_Events_Token_transferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_transferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_transferExitEventOccurrence)

@given(instance=trace_Events_Activity_getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_getenablednodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getEnabledNodesEntryEventOccurrence)

@given(instance=trace_Events_ActivityEdge_hasOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_hasofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_hasOfferExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluateequalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)

@given(instance=trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_stringvariable_setcurrentvalue_stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)

@given(instance=trace_Events_Token_transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_transferEntryEventOccurrence)

@given(instance=trace_Events_Action_sendOffers_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_sendoffers_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_sendOffers_actionExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_execute_integercalculationexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_run_activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_run_activityNodeExitEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_execute_integercomparisionexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)

@given(instance=trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_controlnode_fire_controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence)

@given(instance=trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_stringvariable_getcurrentvaluevalue_stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)

@given(instance=trace_Events_Activity_runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_runEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_takeofferedtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)

@given(instance=trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanbinaryexpression_evaluateorexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)

@given(instance=trace_Events_Token_isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_iswithdrawnentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_isWithdrawnEntryEventOccurrence)

@given(instance=trace_Events_Activity_getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_getinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_getInitialNodeEntryEventOccurrence)

@given(instance=trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanunaryexpression_evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)

@given(instance=trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_opaqueaction_doaction_opaqueactionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)

@given(instance=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)

@given(instance=trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_decisionnode_fire_decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)

@given(instance=trace_Events_Token_isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_iswithdrawnexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_isWithdrawnExitEventOccurrence)

@given(instance=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integerexpression_getoperandcurrentvaluesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)

@given(instance=trace_Events_Action_isReady_actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_isready_actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_isReady_actionEntryEventOccurrence)

@given(instance=trace_Events_Activity_terminateExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_terminateexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_terminateExitEventOccurrence)

@given(instance=trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integerexpression_getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)

@given(instance=trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_forkedtoken_withdraw_forkedtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)

@given(instance=trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_initialnode_isready_initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_addTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_addtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_addTokensEntryEventOccurrence)

@given(instance=trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integervariable_setcurrentvalue_integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluatesmaller_equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)

@given(instance=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanunaryexpression_execute_booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)

@given(instance=trace_Events_Action_fire_actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_action_fire_actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Action_fire_actionExitEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)

@given(instance=trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_sendOfferEntryEventOccurrence)

@given(instance=trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_initialnode_isready_initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)

@given(instance=trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_opaqueaction_doaction_opaqueactionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)

@given(instance=trace_Events_Offer_hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_offer_hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Offer_hasTokensExitEventOccurrence)

@given(instance=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanvariable_getcurrentvaluevalue_booleanvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)

@given(instance=trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercalculationexpression_evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)

@given(instance=trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_terminate_activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)

@given(instance=trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_integercomparisonexpression_evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)

@given(instance=trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_booleanunaryexpression_evaluatenotexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)

@given(instance=trace_Events_Token_withdrawEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_token_withdrawentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Token_withdrawEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_terminate_activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)

@given(instance=trace_Events_ActivityNode_isRunningEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activitynode_isrunningentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityNode_isRunningEntryEventOccurrence)

@given(instance=trace_Events_ActivityEdge_sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activityedge_sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_ActivityEdge_sendOfferExitEventOccurrence)

@given(instance=trace_Events_Activity_selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace_events_activity_selectnextnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace_Events_Activity_selectNextNodeExitEventOccurrence)

@given(instance=trace_StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_trace_staticobjectspools_instantiation(instance):
    assert isinstance(instance, trace_StaticObjectsPools)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=trace_GlobalState_strategy)
@settings(max_examples=50)
def test_trace_globalstate_instantiation(instance):
    assert isinstance(instance, trace_GlobalState)
