from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class trace_activitydiagramConfiguration_TracedTrace:

    pass
class trace_activitydiagramConfiguration_TracedOffer:

    pass
class activitydiagram_trace_DecisionNode:

    pass
class activitydiagram_trace_JoinNode:

    pass
class activitydiagram_trace_OpaqueAction:

    pass
class activitydiagram_trace_Expression:

    pass
class TracedAction:

    pass
class trace_activitydiagram_TracedOpaqueAction(TracedAction):

    pass
class trace_activitydiagramConfiguration_TracedInput:

    pass
class TracedToken:

    pass
class trace_activitydiagramConfiguration_TracedForkedToken(TracedToken):

    pass
class trace_activitydiagramConfiguration_TracedControlToken(TracedToken):

    pass
class trace_activitydiagramConfiguration_TracedToken(ABC):

    pass
class trace_activitydiagramConfiguration_TracedInputValue:

    pass
class activitydiagram_trace_StringVariable:

    pass
class activitydiagram_trace_Activity:

    pass
class TracedNamedElement:

    pass
class trace_activitydiagram_TracedActivityNode(TracedNamedElement):

    pass
class trace_activitydiagram_TracedActivity(TracedNamedElement):

    pass
class trace_activitydiagram_TracedActivityEdge(TracedNamedElement):

    pass
class activitydiagram_trace_IntegerVariable:

    pass
class TracedActivityNode:

    pass
class trace_activitydiagram_TracedControlNode(TracedActivityNode):

    pass
class trace_activitydiagram_TracedExecutableNode(TracedActivityNode):

    pass
class activitydiagram_trace_BooleanVariable:

    pass
class TracedVariable:

    pass
class trace_activitydiagram_TracedStringVariable(TracedVariable):

    pass
class trace_activitydiagram_TracedIntegerVariable(TracedVariable):

    pass
class trace_activitydiagram_TracedBooleanVariable(TracedVariable):

    pass
class activitydiagram_trace_InitialNode:

    pass
class activitydiagram_trace_ForkNode:

    pass
class activitydiagram_trace_ActivityFinalNode:

    pass
class TracedFinalNode:

    pass
class trace_activitydiagram_TracedActivityFinalNode(TracedFinalNode):

    pass
class TracedExecutableNode:

    pass
class trace_activitydiagram_TracedAction(TracedExecutableNode):

    pass
class activitydiagram_trace_Value:

    pass
class trace_activitydiagram_TracedVariable(TracedNamedElement):

    pass
class trace_activitydiagram_TracedNamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class activitydiagram_trace_MergeNode:

    pass
class TracedControlNode:

    pass
class trace_activitydiagram_TracedForkNode(TracedControlNode):

    pass
class trace_activitydiagram_TracedInitialNode(TracedControlNode):

    pass
class trace_activitydiagram_TracedFinalNode(TracedControlNode):

    pass
class trace_activitydiagram_TracedDecisionNode(TracedControlNode):

    pass
class trace_activitydiagram_TracedJoinNode(TracedControlNode):

    pass
class trace_activitydiagram_TracedMergeNode(TracedControlNode):

    pass
class activitydiagram_trace_ControlFlow:

    pass
class TracedActivityEdge:

    pass
class trace_activitydiagram_TracedControlFlow(TracedActivityEdge):

    pass
class activitydiagram_TracedJoinNode:

    pass
class trace_States_Trace_executedNodes_State:

    pass
class activitydiagramConfiguration_TracedControlToken:

    pass
class activitydiagram_TracedControlFlow:

    pass
class trace_Traced_TracedObjects:

    pass
class trace_States_ActivityNode_heldTokens_State:

    pass
class trace_States_ActivityNode_running_State:

    def __init__(self, running: bool, activitydiagram714: "activitydiagram_TracedActivityNode" = None, activityNode_running_States: set["States_trace_GlobalState"] = None):
        self.running = running
        self.activitydiagram714 = activitydiagram714
        self.activityNode_running_States = activityNode_running_States if activityNode_running_States is not None else set()
        
    @property
    def running(self) -> bool:
        return self.__running

    @running.setter
    def running(self, running: bool):
        self.__running = running

    @property
    def activityNode_running_States(self):
        return self.__activityNode_running_States

    @activityNode_running_States.setter
    def activityNode_running_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ActivityNode_running_State__activityNode_running_States", None)
        self.__activityNode_running_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState717"):
                    opp_val = getattr(item, "GlobalState717", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState717", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState717"):
                    opp_val = getattr(item, "GlobalState717", None)
                    
                    setattr(item, "GlobalState717", self)
                    

    @property
    def activitydiagram714(self):
        return self.__activitydiagram714

    @activitydiagram714.setter
    def activitydiagram714(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ActivityNode_running_State__activitydiagram714", None)
        self.__activitydiagram714 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced715"):
                opp_val = getattr(old_value, "Traced715", None)
                if opp_val == self:
                    setattr(old_value, "Traced715", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced715"):
                opp_val = getattr(value, "Traced715", None)
                setattr(value, "Traced715", self)

class activitydiagramConfiguration_TracedTrace:

    pass
class trace_States_Activity_trace_State:

    pass
class trace_States_Variable_currentValue_State:

    pass
class trace_States_Offer_offeredTokens_State:

    pass
class trace_States_ForkedToken_remainingOffersCount_State:

    def __init__(self, remainingOffersCount: int, activitydiagramConfiguration677: "activitydiagramConfiguration_TracedForkedToken" = None, forkedToken_remainingOffersCount_States: set["States_trace_GlobalState"] = None):
        self.remainingOffersCount = remainingOffersCount
        self.activitydiagramConfiguration677 = activitydiagramConfiguration677
        self.forkedToken_remainingOffersCount_States = forkedToken_remainingOffersCount_States if forkedToken_remainingOffersCount_States is not None else set()
        
    @property
    def remainingOffersCount(self) -> int:
        return self.__remainingOffersCount

    @remainingOffersCount.setter
    def remainingOffersCount(self, remainingOffersCount: int):
        self.__remainingOffersCount = remainingOffersCount

    @property
    def forkedToken_remainingOffersCount_States(self):
        return self.__forkedToken_remainingOffersCount_States

    @forkedToken_remainingOffersCount_States.setter
    def forkedToken_remainingOffersCount_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ForkedToken_remainingOffersCount_State__forkedToken_remainingOffersCount_States", None)
        self.__forkedToken_remainingOffersCount_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState680"):
                    opp_val = getattr(item, "GlobalState680", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState680", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState680"):
                    opp_val = getattr(item, "GlobalState680", None)
                    
                    setattr(item, "GlobalState680", self)
                    

    @property
    def activitydiagramConfiguration677(self):
        return self.__activitydiagramConfiguration677

    @activitydiagramConfiguration677.setter
    def activitydiagramConfiguration677(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ForkedToken_remainingOffersCount_State__activitydiagramConfiguration677", None)
        self.__activitydiagramConfiguration677 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced678"):
                opp_val = getattr(old_value, "Traced678", None)
                if opp_val == self:
                    setattr(old_value, "Traced678", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced678"):
                opp_val = getattr(value, "Traced678", None)
                setattr(value, "Traced678", self)

class activitydiagramConfiguration_TracedInput:

    pass
class trace_States_Input_inputValues_State:

    pass
class trace_States_ActivityEdge_offers_State:

    pass
class trace_States_ForkedToken_baseTokenIsWithdrawn_State:

    def __init__(self, baseTokenIsWithdrawn: bool, activitydiagramConfiguration689: "activitydiagramConfiguration_TracedForkedToken" = None, forkedToken_baseTokenIsWithdrawn_States: set["States_trace_GlobalState"] = None):
        self.baseTokenIsWithdrawn = baseTokenIsWithdrawn
        self.activitydiagramConfiguration689 = activitydiagramConfiguration689
        self.forkedToken_baseTokenIsWithdrawn_States = forkedToken_baseTokenIsWithdrawn_States if forkedToken_baseTokenIsWithdrawn_States is not None else set()
        
    @property
    def baseTokenIsWithdrawn(self) -> bool:
        return self.__baseTokenIsWithdrawn

    @baseTokenIsWithdrawn.setter
    def baseTokenIsWithdrawn(self, baseTokenIsWithdrawn: bool):
        self.__baseTokenIsWithdrawn = baseTokenIsWithdrawn

    @property
    def forkedToken_baseTokenIsWithdrawn_States(self):
        return self.__forkedToken_baseTokenIsWithdrawn_States

    @forkedToken_baseTokenIsWithdrawn_States.setter
    def forkedToken_baseTokenIsWithdrawn_States(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ForkedToken_baseTokenIsWithdrawn_State__forkedToken_baseTokenIsWithdrawn_States", None)
        self.__forkedToken_baseTokenIsWithdrawn_States = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "GlobalState692"):
                    opp_val = getattr(item, "GlobalState692", None)
                    
                    if opp_val == self:
                        setattr(item, "GlobalState692", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "GlobalState692"):
                    opp_val = getattr(item, "GlobalState692", None)
                    
                    setattr(item, "GlobalState692", self)
                    

    @property
    def activitydiagramConfiguration689(self):
        return self.__activitydiagramConfiguration689

    @activitydiagramConfiguration689.setter
    def activitydiagramConfiguration689(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_trace_States_ForkedToken_baseTokenIsWithdrawn_State__activitydiagramConfiguration689", None)
        self.__activitydiagramConfiguration689 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Traced690"):
                opp_val = getattr(old_value, "Traced690", None)
                if opp_val == self:
                    setattr(old_value, "Traced690", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Traced690"):
                opp_val = getattr(value, "Traced690", None)
                setattr(value, "Traced690", self)

class trace_States_ForkedToken_baseToken_State:

    pass
class States_trace_Value:

    pass
class trace_States_InputValue_value_State:

    pass
class activitydiagramConfiguration_TracedOffer:

    pass
class trace_States_Token_holder_State:

    pass
class activitydiagram_TracedVariable:

    pass
class trace_States_InputValue_variable_State:

    pass
class States_trace_GlobalState:

    pass
class activitydiagramConfiguration_TracedInputValue:

    pass
class activitydiagramConfiguration_TracedForkedToken:

    pass
class Events_trace_BooleanBinaryExpression:

    pass
class Events_trace_BooleanUnaryExpression:

    pass
class Events_trace_IntegerComparisonExpression:

    pass
class Events_trace_IntegerCalculationExpression:

    pass
class activitydiagram_TracedBooleanVariable:

    pass
class Events_trace_IntegerExpression:

    pass
class Events_trace_Value:

    pass
class activitydiagram_TracedIntegerVariable:

    pass
class activitydiagram_TracedStringVariable:

    pass
class activitydiagram_TracedForkNode:

    pass
class activitydiagram_TracedActivityFinalNode:

    pass
class activitydiagram_TracedDecisionNode:

    pass
class activitydiagram_TracedMergeNode:

    pass
class activitydiagram_TracedOpaqueAction:

    pass
class activitydiagram_TracedInitialNode:

    pass
class activitydiagram_TracedControlNode:

    pass
class activitydiagram_TracedAction:

    pass
class activitydiagramConfiguration_TracedToken:

    pass
class activitydiagram_TracedActivityEdge:

    pass
class activitydiagram_TracedActivityNode:

    pass
class Events_trace_EObject:

    pass
class activitydiagram_TracedActivity:

    pass
class Offer_hasTokensExitEventOccurrence:

    pass
class Token_transferExitEventOccurrence:

    pass
class Token_transferEntryEventOccurrence:

    pass
class Token_isWithdrawnExitEventOccurrence:

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
class BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence:

    pass
class BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence:

    pass
class BooleanUnaryExpression_evaluateNOTExitEventOccurrence:

    pass
class BooleanUnaryExpression_evaluateNOTEntryEventOccurrence:

    pass
class Token_isWithdrawnEntryEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateORExitEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateOREntryEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateANDExitEventOccurrence:

    pass
class BooleanBinaryExpression_evaluateANDEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence:

    pass
class BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence:

    pass
class BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATERExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateADDExitEventOccurrence:

    pass
class IntegerCalculationExpression_evaluateADDEntryEventOccurrence:

    pass
class IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence:

    pass
class IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence:

    pass
class IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence:

    pass
class IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence:

    pass
class BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence:

    pass
class BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence:

    pass
class StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence:

    pass
class StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence:

    pass
class StringVariable_setCurrentValue_stringVariableExitEventOccurrence:

    pass
class IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence:

    pass
class IntegerExpression_getOperandCurrentValuesExitEventOccurrence:

    pass
class IntegerExpression_getOperandCurrentValuesEntryEventOccurrence:

    pass
class BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence:

    pass
class BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence:

    pass
class DecisionNode_fire_decisionNodeEntryEventOccurrence:

    pass
class MergeNode_hasOffers_mergeNodeExitEventOccurrence:

    pass
class MergeNode_hasOffers_mergeNodeEntryEventOccurrence:

    pass
class ForkNode_fire_forkNodeExitEventOccurrence:

    pass
class ForkNode_fire_forkNodeEntryEventOccurrence:

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
class DecisionNode_fire_decisionNodeExitEventOccurrence:

    pass
class OpaqueAction_doAction_opaqueActionExitEventOccurrence:

    pass
class OpaqueAction_doAction_opaqueActionEntryEventOccurrence:

    pass
class Action_fire_actionExitEventOccurrence:

    pass
class Action_fire_actionEntryEventOccurrence:

    pass
class Action_isReady_actionExitEventOccurrence:

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
class ControlNode_isReady_ControlNodeEntryEventOccurrence:

    pass
class ActivityEdge_hasOfferExitEventOccurrence:

    pass
class ActivityEdge_hasOfferEntryEventOccurrence:

    pass
class ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence:

    pass
class Action_isReady_actionEntryEventOccurrence:

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
class ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence:

    pass
class ActivityEdge_sendOfferExitEventOccurrence:

    pass
class ActivityEdge_sendOfferEntryEventOccurrence:

    pass
class ActivityNode_isReadyExitEventOccurrence:

    pass
class ActivityNode_isReadyEntryEventOccurrence:

    pass
class ActivityNode_hasOffersExitEventOccurrence:

    pass
class ActivityNode_hasOffersEntryEventOccurrence:

    pass
class ActivityNode_sendOffersEntryEventOccurrence:

    pass
class ActivityNode_terminate_activityNodeExitEventOccurrence:

    pass
class ActivityNode_terminate_activityNodeEntryEventOccurrence:

    pass
class ActivityNode_isRunningExitEventOccurrence:

    pass
class ActivityNode_isRunningEntryEventOccurrence:

    pass
class ActivityNode_run_activityNodeExitEventOccurrence:

    pass
class ActivityNode_takeOfferedTokensEntryEventOccurrence:

    pass
class ActivityNode_sendOffersExitEventOccurrence:

    pass
class Activity_getEnabledNodesExitEventOccurrence:

    pass
class Activity_getEnabledNodesEntryEventOccurrence:

    pass
class Activity_fireInitialNodeExitEventOccurrence:

    pass
class Activity_fireInitialNodeEntryEventOccurrence:

    pass
class Activity_runNodesExitEventOccurrence:

    pass
class Activity_runNodesEntryEventOccurrence:

    pass
class Activity_runExitEventOccurrence:

    pass
class Activity_runEntryEventOccurrence:

    pass
class ActivityNode_run_activityNodeEntryEventOccurrence:

    pass
class Activity_fireNodeExitEventOccurrence:

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
class trace_IntegerValue:

    pass
class trace_StringValue:

    pass
class trace_BooleanBinaryExpression:

    pass
class Trace_executedNodes_State:

    pass
class Activity_trace_State:

    pass
class ActivityNode_heldTokens_State:

    pass
class ActivityNode_running_State:

    pass
class Activity_initializeExitEventOccurrence:

    pass
class Activity_initializeEntryEventOccurrence:

    pass
class Activity_mainExitEventOccurrence:

    pass
class Activity_mainEntryEventOccurrence:

    pass
class trace_Events_Events:

    pass
class Events_trace_GlobalState:

    pass
class trace_Events_EventOccurrence(ABC):

    pass
class trace_IntegerCalculationExpression:

    pass
class trace_BooleanUnaryExpression:

    pass
class trace_IntegerComparisonExpression:

    pass
class trace_BooleanValue:

    pass
class Offer_offeredTokens_State:

    pass
class Variable_currentValue_State:

    pass
class ActivityEdge_offers_State:

    pass
class ForkedToken_baseTokenIsWithdrawn_State:

    pass
class ForkedToken_baseToken_State:

    pass
class ForkedToken_remainingOffersCount_State:

    pass
class Input_inputValues_State:

    pass
class Token_holder_State:

    pass
class InputValue_variable_State:

    pass
class InputValue_value_State:

    pass
class EventOccurrence:

    pass
class trace_Events_ActivityNode_sendOffersEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_selectNextNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_fireInitialNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_isRunningEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_hasOffersEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_fireNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_getInitialNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_isWithdrawnExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_hasOffersExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_hasOfferExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_sendOffersExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_sendOffers_actionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_getInitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_sendOfferEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_getEnabledNodesEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_runEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_transferEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_terminateEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_isWithdrawnEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_sendOffers_actionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_withdrawExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Offer_hasTokensEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_InitialNode_fire_initialNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_isReady_actionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_run_activityNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_hasOfferEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_fire_actionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_removeTokenEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_mainExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_isReadyEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_isReadyExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_terminateExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_addTokensExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_runNodesEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_sendOfferExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ControlNode_fire_controlNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_fire_actionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_selectNextNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_fireInitialNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_fireNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_initializeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_mainEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_transferExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_getEnabledNodesExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_addTokensEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_runExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_removeTokenExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Token_withdrawEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_ActivityNode_isRunningExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Offer_hasTokensExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_runNodesExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_ForkNode_fire_forkNodeExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_Activity_initializeEntryEventOccurrence(EventOccurrence):

    pass
class trace_Events_Action_isReady_actionExitEventOccurrence(EventOccurrence):

    pass
class trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence(EventOccurrence):

    pass
class trace_StaticObjectsPools:

    pass
class TracedObjects:

    pass
class Events:

    pass
class trace_GlobalState:

    pass
class trace_Trace:

    pass