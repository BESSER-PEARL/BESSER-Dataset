from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class States_traceSystem_GlobalState:

    pass
class traceSystem_States_ForkedToken_baseToken_State:

    pass
class activitydiagramConfiguration_TracedOffer:

    pass
class Events_traceSystem_BooleanBinaryExpression:

    pass
class Events_traceSystem_BooleanUnaryExpression:

    pass
class Events_traceSystem_IntegerComparisonExpression:

    pass
class Events_traceSystem_IntegerCalculationExpression:

    pass
class Events_traceSystem_IntegerExpression:

    pass
class activitydiagram_TracedDecisionNode:

    pass
class activitydiagram_TracedBooleanVariable:

    pass
class activitydiagram_TracedStringVariable:

    pass
class Events_traceSystem_Value:

    pass
class activitydiagram_TracedIntegerVariable:

    pass
class activitydiagram_TracedInitialNode:

    pass
class activitydiagram_TracedMergeNode:

    pass
class activitydiagram_TracedOpaqueAction:

    pass
class activitydiagram_TracedForkNode:

    pass
class activitydiagram_TracedActivityFinalNode:

    pass
class activitydiagram_TracedAction:

    pass
class activitydiagramConfiguration_TracedToken:

    pass
class activitydiagram_TracedControlNode:

    pass
class activitydiagram_TracedActivityEdge:

    pass
class activitydiagram_traceSystem_JoinNode:

    pass
class activitydiagram_traceSystem_InitialNode:

    pass
class traceSystem_activitydiagram_TracedNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


class activitydiagram_traceSystem_IntegerVariable:

    pass
class activitydiagram_traceSystem_DecisionNode:

    pass
class activitydiagram_traceSystem_MergeNode:

    pass
class activitydiagram_traceSystem_Value:

    pass
class activitydiagram_traceSystem_Activity:

    pass
class activitydiagram_traceSystem_ControlFlow:

    pass
class TracedActivityEdge:

    pass
class traceSystem_activitydiagram_TracedControlFlow(TracedActivityEdge):

    pass
class activitydiagram_traceSystem_ForkNode:

    pass
class TracedControlNode:

    pass
class traceSystem_activitydiagram_TracedInitialNode(TracedControlNode):

    pass
class traceSystem_activitydiagram_TracedDecisionNode(TracedControlNode):

    pass
class traceSystem_activitydiagram_TracedMergeNode(TracedControlNode):

    pass
class traceSystem_activitydiagram_TracedJoinNode(TracedControlNode):

    pass
class traceSystem_activitydiagram_TracedForkNode(TracedControlNode):

    pass
class activitydiagram_traceSystem_BooleanVariable:

    pass
class TracedNamedElement:

    pass
class traceSystem_activitydiagram_TracedActivityNode(TracedNamedElement):

    pass
class traceSystem_activitydiagram_TracedActivityEdge(TracedNamedElement):

    pass
class traceSystem_activitydiagram_TracedVariable(TracedNamedElement):

    pass
class traceSystem_activitydiagram_TracedActivity(TracedNamedElement):

    pass
class TracedActivityNode:

    pass
class traceSystem_activitydiagram_TracedControlNode(TracedActivityNode):

    pass
class traceSystem_activitydiagram_TracedExecutableNode(TracedActivityNode):

    pass
class activitydiagram_traceSystem_OpaqueAction:

    pass
class activitydiagram_traceSystem_Expression:

    pass
class TracedAction:

    pass
class traceSystem_activitydiagram_TracedOpaqueAction(TracedAction):

    pass
class activitydiagram_traceSystem_StringVariable:

    pass
class traceSystem_activitydiagram_TracedFinalNode(TracedControlNode):

    pass
class TracedExecutableNode:

    pass
class traceSystem_activitydiagram_TracedAction(TracedExecutableNode):

    pass
class activitydiagram_traceSystem_ActivityFinalNode:

    pass
class TracedFinalNode:

    pass
class traceSystem_activitydiagram_TracedActivityFinalNode(TracedFinalNode):

    pass
class TracedVariable:

    pass
class traceSystem_activitydiagram_TracedIntegerVariable(TracedVariable):

    pass
class traceSystem_activitydiagram_TracedStringVariable(TracedVariable):

    pass
class traceSystem_activitydiagram_TracedBooleanVariable(TracedVariable):

    pass
class traceSystem_activitydiagramConfiguration_TracedInput:

    pass
class traceSystem_activitydiagramConfiguration_TracedTrace:

    pass
class traceSystem_activitydiagramConfiguration_TracedInputValue:

    pass
class traceSystem_activitydiagramConfiguration_TracedOffer:

    pass
class traceSystem_activitydiagramConfiguration_TracedToken(ABC):

    pass
class TracedToken:

    pass
class traceSystem_activitydiagramConfiguration_TracedControlToken(TracedToken):

    pass
class traceSystem_activitydiagramConfiguration_TracedForkedToken(TracedToken):

    pass
class traceSystem_Traced_TracedObjects:

    pass
class activitydiagram_TracedJoinNode:

    pass
class activitydiagramConfiguration_TracedControlToken:

    pass
class activitydiagram_TracedControlFlow:

    pass
class traceSystem_States_ActivityEdge_offers_State:

    pass
class traceSystem_States_ActivityNode_running_State:

    def __init__(self, running: bool, runningTrace: "activitydiagram_TracedActivityNode" = None, activityNode_running_States: set["States_traceSystem_GlobalState"] = None):
        self.running = running
        self.runningTrace = runningTrace
        self.activityNode_running_States = activityNode_running_States if activityNode_running_States is not None else set()
        
        pass
    @property
    def running(self):
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running


    @property
    def runningTrace(self):
        return self.__runningTrace

    @runningTrace.setter
    def runningTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ActivityNode_running_State__runningTrace", None)
        self.__runningTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedActivityNode713"):
                opp_val = getattr(old_value, "TracedActivityNode713", None)
                if opp_val == self:
                    setattr(old_value, "TracedActivityNode713", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedActivityNode713"):
                opp_val = getattr(value, "TracedActivityNode713", None)
                setattr(value, "TracedActivityNode713", self)

    @property
    def activityNode_running_States(self):
        return self.__activityNode_running_States

    @activityNode_running_States.setter
    def activityNode_running_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ActivityNode_running_State__activityNode_running_States", None)
        self.__activityNode_running_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState715"):
                    opp_val = getattr(item, "GlobalState715", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState715", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState715"):
                    opp_val = getattr(item, "GlobalState715", None)
                    
                    setattr(item, "GlobalState715", self)
                    

class traceSystem_States_ActivityNode_heldTokens_State:

    pass
class activitydiagramConfiguration_TracedInput:

    pass
class traceSystem_States_Input_inputValues_State:

    pass
class traceSystem_States_Trace_executedNodes_State:

    pass
class traceSystem_States_Offer_offeredTokens_State:

    pass
class traceSystem_States_InputValue_variable_State:

    pass
class activitydiagramConfiguration_TracedInputValue:

    pass
class traceSystem_States_InputValue_value_State:

    pass
class activitydiagram_TracedVariable:

    pass
class States_traceSystem_Value:

    pass
class traceSystem_States_Variable_currentValue_State:

    pass
class activitydiagramConfiguration_TracedTrace:

    pass
class traceSystem_States_Activity_trace_State:

    pass
class activitydiagramConfiguration_TracedForkedToken:

    pass
class traceSystem_States_Token_holder_State:

    pass
class traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State:

    def __init__(self, baseTokenIsWithdrawn: bool, baseTokenIsWithdrawnTrace: "activitydiagramConfiguration_TracedForkedToken" = None, forkedToken_baseTokenIsWithdrawn_States: set["States_traceSystem_GlobalState"] = None):
        self.baseTokenIsWithdrawn = baseTokenIsWithdrawn
        self.baseTokenIsWithdrawnTrace = baseTokenIsWithdrawnTrace
        self.forkedToken_baseTokenIsWithdrawn_States = forkedToken_baseTokenIsWithdrawn_States if forkedToken_baseTokenIsWithdrawn_States is not None else set()
        
        pass
    @property
    def baseTokenIsWithdrawn(self):
        return self.__baseTokenIsWithdrawn

    @baseTokenIsWithdrawn.setter
    def baseTokenIsWithdrawn(self, baseTokenIsWithdrawn: bool):
        self.__baseTokenIsWithdrawn = baseTokenIsWithdrawn


    @property
    def baseTokenIsWithdrawnTrace(self):
        return self.__baseTokenIsWithdrawnTrace

    @baseTokenIsWithdrawnTrace.setter
    def baseTokenIsWithdrawnTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State__baseTokenIsWithdrawnTrace", None)
        self.__baseTokenIsWithdrawnTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedForkedToken662"):
                opp_val = getattr(old_value, "TracedForkedToken662", None)
                if opp_val == self:
                    setattr(old_value, "TracedForkedToken662", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedForkedToken662"):
                opp_val = getattr(value, "TracedForkedToken662", None)
                setattr(value, "TracedForkedToken662", self)

    @property
    def forkedToken_baseTokenIsWithdrawn_States(self):
        return self.__forkedToken_baseTokenIsWithdrawn_States

    @forkedToken_baseTokenIsWithdrawn_States.setter
    def forkedToken_baseTokenIsWithdrawn_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State__forkedToken_baseTokenIsWithdrawn_States", None)
        self.__forkedToken_baseTokenIsWithdrawn_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState664"):
                    opp_val = getattr(item, "GlobalState664", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState664", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState664"):
                    opp_val = getattr(item, "GlobalState664", None)
                    
                    setattr(item, "GlobalState664", self)
                    

class traceSystem_States_ForkedToken_remainingOffersCount_State:

    def __init__(self, remainingOffersCount: int, remainingOffersCountTrace: "activitydiagramConfiguration_TracedForkedToken" = None, forkedToken_remainingOffersCount_States: set["States_traceSystem_GlobalState"] = None):
        self.remainingOffersCount = remainingOffersCount
        self.remainingOffersCountTrace = remainingOffersCountTrace
        self.forkedToken_remainingOffersCount_States = forkedToken_remainingOffersCount_States if forkedToken_remainingOffersCount_States is not None else set()
        
        pass
    @property
    def remainingOffersCount(self):
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: int):
        self.__remainingOffersCount = remainingOffersCount


    @property
    def remainingOffersCountTrace(self):
        return self.__remainingOffersCountTrace

    @remainingOffersCountTrace.setter
    def remainingOffersCountTrace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ForkedToken_remainingOffersCount_State__remainingOffersCountTrace", None)
        self.__remainingOffersCountTrace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TracedForkedToken658"):
                opp_val = getattr(old_value, "TracedForkedToken658", None)
                if opp_val == self:
                    setattr(old_value, "TracedForkedToken658", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TracedForkedToken658"):
                opp_val = getattr(value, "TracedForkedToken658", None)
                setattr(value, "TracedForkedToken658", self)

    @property
    def forkedToken_remainingOffersCount_States(self):
        return self.__forkedToken_remainingOffersCount_States

    @forkedToken_remainingOffersCount_States.setter
    def forkedToken_remainingOffersCount_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_traceSystem_States_ForkedToken_remainingOffersCount_State__forkedToken_remainingOffersCount_States", None)
        self.__forkedToken_remainingOffersCount_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState660"):
                    opp_val = getattr(item, "GlobalState660", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState660", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState660"):
                    opp_val = getattr(item, "GlobalState660", None)
                    
                    setattr(item, "GlobalState660", self)
                    

class activitydiagram_TracedActivityNode:

    pass
class Offer_hasTokensEntryEventOccurrence:

    pass
class ForkedToken_withdraw_forkedTokenExitEventOccurrence:

    pass
class ForkedToken_withdraw_forkedTokenEntryEventOccurrence:

    pass
class Token_withdrawExitEventOccurrence:

    pass
class Token_withdrawEntryEventOccurrence:

    pass
class Token_transferExitEventOccurrence:

    pass
class Events_traceSystem_EObject:

    pass
class activitydiagram_TracedActivity:

    pass
class Offer_hasTokensExitEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateOREntryEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateANDExitEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateANDEntryEventOccurrence:

    pass
class BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence:

    pass
class BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence:

    pass
class BooleanUnaryExpression_evaluateNOTExitEventOccurrence:

    pass
class BooleanUnaryExpression_evaluateNOTEntryEventOccurrence:

    pass
class Token_transferEntryEventOccurrence:

    pass
class Token_isWithdrawnExitEventOccurrence:

    pass
class Token_isWithdrawnEntryEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateORExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence:

    pass
class BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence:

    pass
class BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATERExitEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateADDExitEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateADDEntryEventOccurrence:

    pass
class IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence:

    pass
class IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence:

    pass
class IntegerExpression_getOperandCurrentValuesExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence:

    pass
class IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence:

    pass
class IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence:

    pass
class StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence:

    pass
class StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence:

    pass
class StringVariable_setCurrentValue_stringVariableExitEventOccurrence:

    pass
class StringVariable_setCurrentValue_stringVariableEntryEventOccurrence:

    pass
class IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence:

    pass
class IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence:

    pass
class IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence:

    pass
class IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence:

    pass
class IntegerExpression_getOperandCurrentValuesEntryEventOccurrence:

    pass
class DecisionNode_fire_decisionNodeExitEventOccurrence:

    pass
class BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence:

    pass
class BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence:

    pass
class BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence:

    pass
class BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence:

    pass
class ForkNode_fire_forkNodeEntryEventOccurrence:

    pass
class ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence:

    pass
class ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence:

    pass
class InitialNode_fire_initialNodeExitEventOccurrence:

    pass
class InitialNode_fire_initialNodeEntryEventOccurrence:

    pass
class InitialNode_isReady_InitialNodeExitEventOccurrence:

    pass
class InitialNode_isReady_InitialNodeEntryEventOccurrence:

    pass
class OpaqueAction_doAction_opaqueActionExitEventOccurrence:

    pass
class OpaqueAction_doAction_opaqueActionEntryEventOccurrence:

    pass
class DecisionNode_fire_decisionNodeEntryEventOccurrence:

    pass
class MergeNode_hasOffers_mergeNodeExitEventOccurrence:

    pass
class MergeNode_hasOffers_mergeNodeEntryEventOccurrence:

    pass
class ForkNode_fire_forkNodeExitEventOccurrence:

    pass
class Action_sendOffers_actionExitEventOccurrence:

    pass
class Action_sendOffers_actionEntryEventOccurrence:

    pass
class ControlNode_fire_controlNodeExitEventOccurrence:

    pass
class ControlNode_fire_controlNodeEntryEventOccurrence:

    pass
class ControlNode_isReady_ControlNodeExitEventOccurrence:

    pass
class ControlNode_isReady_ControlNodeEntryEventOccurrence:

    pass
class ActivityEdge_hasOfferExitEventOccurrence:

    pass
class ActivityEdge_hasOfferEntryEventOccurrence:

    pass
class ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence:

    pass
class ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence:

    pass
class Action_fire_actionExitEventOccurrence:

    pass
class Action_fire_actionEntryEventOccurrence:

    pass
class Action_isReady_actionExitEventOccurrence:

    pass
class Action_isReady_actionEntryEventOccurrence:

    pass
class ActivityNode_hasOffersExitEventOccurrence:

    pass
class ActivityNode_hasOffersEntryEventOccurrence:

    pass
class ActivityNode_removeTokenExitEventOccurrence:

    pass
class ActivityNode_removeTokenEntryEventOccurrence:

    pass
class ActivityNode_addTokensExitEventOccurrence:

    pass
class ActivityNode_addTokensEntryEventOccurrence:

    pass
class ActivityNode_takeOfferedTokensExitEventOccurrence:

    pass
class ActivityNode_takeOfferedTokensEntryEventOccurrence:

    pass
class ActivityNode_sendOffersExitEventOccurrence:

    pass
class ActivityNode_sendOffersEntryEventOccurrence:

    pass
class ActivityNode_terminate_activityNodeExitEventOccurrence:

    pass
class ActivityEdge_sendOfferExitEventOccurrence:

    pass
class ActivityEdge_sendOfferEntryEventOccurrence:

    pass
class ActivityNode_isReadyExitEventOccurrence:

    pass
class ActivityNode_isReadyEntryEventOccurrence:

    pass
class Activity_fireNodeEntryEventOccurrence:

    pass
class Activity_getInitialNodeExitEventOccurrence:

    pass
class Activity_getInitialNodeEntryEventOccurrence:

    pass
class Activity_terminateExitEventOccurrence:

    pass
class Activity_terminateEntryEventOccurrence:

    pass
class Activity_selectNextNodeExitEventOccurrence:

    pass
class Activity_selectNextNodeEntryEventOccurrence:

    pass
class Activity_getEnabledNodesExitEventOccurrence:

    pass
class Activity_getEnabledNodesEntryEventOccurrence:

    pass
class Activity_fireInitialNodeExitEventOccurrence:

    pass
class Activity_fireInitialNodeEntryEventOccurrence:

    pass
class ActivityNode_terminate_activityNodeEntryEventOccurrence:

    pass
class ActivityNode_isRunningExitEventOccurrence:

    pass
class ActivityNode_isRunningEntryEventOccurrence:

    pass
class ActivityNode_run_activityNodeExitEventOccurrence:

    pass
class ActivityNode_run_activityNodeEntryEventOccurrence:

    pass
class Activity_fireNodeExitEventOccurrence:

    pass
class Activity_initializeEntryEventOccurrence:

    pass
class Activity_mainExitEventOccurrence:

    pass
class Activity_mainEntryEventOccurrence:

    pass
class traceSystem_Events_Events:

    pass
class Events_traceSystem_GlobalState:

    pass
class traceSystem_Events_EventOccurrence(ABC):

    pass
class traceSystem_IntegerCalculationExpression:

    pass
class traceSystem_IntegerValue:

    pass
class traceSystem_BooleanUnaryExpression:

    pass
class traceSystem_BooleanBinaryExpression:

    pass
class traceSystem_StringValue:

    pass
class traceSystem_IntegerComparisonExpression:

    pass
class traceSystem_BooleanValue:

    pass
class ActivityNode_running_State:

    pass
class ActivityNode_heldTokens_State:

    pass
class Activity_runNodesExitEventOccurrence:

    pass
class Activity_runNodesEntryEventOccurrence:

    pass
class Activity_runExitEventOccurrence:

    pass
class Activity_runEntryEventOccurrence:

    pass
class Activity_initializeExitEventOccurrence:

    pass
class InputValue_value_State:

    pass
class Variable_currentValue_State:

    pass
class Activity_trace_State:

    pass
class Offer_offeredTokens_State:

    pass
class Token_holder_State:

    pass
class ForkedToken_baseTokenIsWithdrawn_State:

    pass
class ForkedToken_remainingOffersCount_State:

    pass
class Input_inputValues_State:

    pass
class Trace_executedNodes_State:

    pass
class ActivityEdge_offers_State:

    pass
class InputValue_variable_State:

    pass
class Events:

    pass
class traceSystem_GlobalState:

    pass
class traceSystem_Trace:

    pass
class ForkedToken_baseToken_State:

    pass
class EventOccurrence:

    pass
class traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_fireNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Offer_hasTokensExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_fire_actionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_sendOffers_actionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_isWithdrawnEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_addTokensExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_fire_actionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_transferExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_isRunningExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_terminateEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_getInitialNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_isReady_actionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_runExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_isWithdrawnExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_runNodesExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Action_isReady_actionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_withdrawEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_initializeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_terminateExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_runNodesEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_withdrawExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_fireNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_mainExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_selectNextNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Token_transferEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Offer_hasTokensEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_isReadyExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_mainEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_initializeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_runEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence(EventOccurrence):

    pass
class traceSystem_StaticObjectsPools:

    pass
class TracedObjects:

    pass