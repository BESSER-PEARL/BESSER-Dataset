####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
trace_Trace = Class(name="trace::Trace")
trace_GlobalState = Class(name="trace::GlobalState")
Events = Class(name="Events")
TracedObjects = Class(name="TracedObjects")
trace_StaticObjectsPools = Class(name="trace::StaticObjectsPools")
EventOccurrence = Class(name="EventOccurrence")
InputValue_value_State = Class(name="InputValue::value::State")
InputValue_variable_State = Class(name="InputValue::variable::State")
Token_holder_State = Class(name="Token::holder::State")
Input_inputValues_State = Class(name="Input::inputValues::State")
ForkedToken_remainingOffersCount_State = Class(name="ForkedToken::remainingOffersCount::State")
ForkedToken_baseToken_State = Class(name="ForkedToken::baseToken::State")
ForkedToken_baseTokenIsWithdrawn_State = Class(name="ForkedToken::baseTokenIsWithdrawn::State")
ActivityEdge_offers_State = Class(name="ActivityEdge::offers::State")
Variable_currentValue_State = Class(name="Variable::currentValue::State")
Offer_offeredTokens_State = Class(name="Offer::offeredTokens::State")
trace_BooleanValue = Class(name="trace::BooleanValue")
trace_IntegerComparisonExpression = Class(name="trace::IntegerComparisonExpression")
trace_BooleanUnaryExpression = Class(name="trace::BooleanUnaryExpression")
trace_IntegerCalculationExpression = Class(name="trace::IntegerCalculationExpression")
trace_Events_EventOccurrence = Class(name="trace::Events::EventOccurrence", is_abstract=True)
Events_trace_GlobalState = Class(name="Events::trace::GlobalState")
trace_Events_Events = Class(name="trace::Events::Events")
Activity_mainEntryEventOccurrence = Class(name="Activity::mainEntryEventOccurrence")
Activity_mainExitEventOccurrence = Class(name="Activity::mainExitEventOccurrence")
Activity_initializeEntryEventOccurrence = Class(name="Activity::initializeEntryEventOccurrence")
Activity_initializeExitEventOccurrence = Class(name="Activity::initializeExitEventOccurrence")
ActivityNode_running_State = Class(name="ActivityNode::running::State")
ActivityNode_heldTokens_State = Class(name="ActivityNode::heldTokens::State")
Activity_trace_State = Class(name="Activity::trace::State")
Trace_executedNodes_State = Class(name="Trace::executedNodes::State")
trace_BooleanBinaryExpression = Class(name="trace::BooleanBinaryExpression")
trace_StringValue = Class(name="trace::StringValue")
trace_IntegerValue = Class(name="trace::IntegerValue")
Activity_selectNextNodeEntryEventOccurrence = Class(name="Activity::selectNextNodeEntryEventOccurrence")
Activity_selectNextNodeExitEventOccurrence = Class(name="Activity::selectNextNodeExitEventOccurrence")
Activity_terminateEntryEventOccurrence = Class(name="Activity::terminateEntryEventOccurrence")
Activity_terminateExitEventOccurrence = Class(name="Activity::terminateExitEventOccurrence")
Activity_getInitialNodeEntryEventOccurrence = Class(name="Activity::getInitialNodeEntryEventOccurrence")
Activity_getInitialNodeExitEventOccurrence = Class(name="Activity::getInitialNodeExitEventOccurrence")
Activity_fireNodeEntryEventOccurrence = Class(name="Activity::fireNodeEntryEventOccurrence")
Activity_fireNodeExitEventOccurrence = Class(name="Activity::fireNodeExitEventOccurrence")
ActivityNode_run_activityNodeEntryEventOccurrence = Class(name="ActivityNode::run::activityNodeEntryEventOccurrence")
Activity_runEntryEventOccurrence = Class(name="Activity::runEntryEventOccurrence")
Activity_runExitEventOccurrence = Class(name="Activity::runExitEventOccurrence")
Activity_runNodesEntryEventOccurrence = Class(name="Activity::runNodesEntryEventOccurrence")
Activity_runNodesExitEventOccurrence = Class(name="Activity::runNodesExitEventOccurrence")
Activity_fireInitialNodeEntryEventOccurrence = Class(name="Activity::fireInitialNodeEntryEventOccurrence")
Activity_fireInitialNodeExitEventOccurrence = Class(name="Activity::fireInitialNodeExitEventOccurrence")
Activity_getEnabledNodesEntryEventOccurrence = Class(name="Activity::getEnabledNodesEntryEventOccurrence")
Activity_getEnabledNodesExitEventOccurrence = Class(name="Activity::getEnabledNodesExitEventOccurrence")
ActivityNode_sendOffersExitEventOccurrence = Class(name="ActivityNode::sendOffersExitEventOccurrence")
ActivityNode_takeOfferedTokensEntryEventOccurrence = Class(name="ActivityNode::takeOfferedTokensEntryEventOccurrence")
ActivityNode_run_activityNodeExitEventOccurrence = Class(name="ActivityNode::run::activityNodeExitEventOccurrence")
ActivityNode_isRunningEntryEventOccurrence = Class(name="ActivityNode::isRunningEntryEventOccurrence")
ActivityNode_isRunningExitEventOccurrence = Class(name="ActivityNode::isRunningExitEventOccurrence")
ActivityNode_terminate_activityNodeEntryEventOccurrence = Class(name="ActivityNode::terminate::activityNodeEntryEventOccurrence")
ActivityNode_terminate_activityNodeExitEventOccurrence = Class(name="ActivityNode::terminate::activityNodeExitEventOccurrence")
ActivityNode_sendOffersEntryEventOccurrence = Class(name="ActivityNode::sendOffersEntryEventOccurrence")
ActivityNode_hasOffersEntryEventOccurrence = Class(name="ActivityNode::hasOffersEntryEventOccurrence")
ActivityNode_hasOffersExitEventOccurrence = Class(name="ActivityNode::hasOffersExitEventOccurrence")
ActivityNode_isReadyEntryEventOccurrence = Class(name="ActivityNode::isReadyEntryEventOccurrence")
ActivityNode_isReadyExitEventOccurrence = Class(name="ActivityNode::isReadyExitEventOccurrence")
ActivityEdge_sendOfferEntryEventOccurrence = Class(name="ActivityEdge::sendOfferEntryEventOccurrence")
ActivityEdge_sendOfferExitEventOccurrence = Class(name="ActivityEdge::sendOfferExitEventOccurrence")
ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence = Class(name="ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence")
ActivityNode_takeOfferedTokensExitEventOccurrence = Class(name="ActivityNode::takeOfferedTokensExitEventOccurrence")
ActivityNode_addTokensEntryEventOccurrence = Class(name="ActivityNode::addTokensEntryEventOccurrence")
ActivityNode_addTokensExitEventOccurrence = Class(name="ActivityNode::addTokensExitEventOccurrence")
ActivityNode_removeTokenEntryEventOccurrence = Class(name="ActivityNode::removeTokenEntryEventOccurrence")
ActivityNode_removeTokenExitEventOccurrence = Class(name="ActivityNode::removeTokenExitEventOccurrence")
ControlNode_isReady_ControlNodeExitEventOccurrence = Class(name="ControlNode::isReady::ControlNodeExitEventOccurrence")
ControlNode_fire_controlNodeEntryEventOccurrence = Class(name="ControlNode::fire::controlNodeEntryEventOccurrence")
ControlNode_fire_controlNodeExitEventOccurrence = Class(name="ControlNode::fire::controlNodeExitEventOccurrence")
Action_sendOffers_actionEntryEventOccurrence = Class(name="Action::sendOffers::actionEntryEventOccurrence")
Action_sendOffers_actionExitEventOccurrence = Class(name="Action::sendOffers::actionExitEventOccurrence")
Action_isReady_actionEntryEventOccurrence = Class(name="Action::isReady::actionEntryEventOccurrence")
ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence = Class(name="ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence")
ActivityEdge_hasOfferEntryEventOccurrence = Class(name="ActivityEdge::hasOfferEntryEventOccurrence")
ActivityEdge_hasOfferExitEventOccurrence = Class(name="ActivityEdge::hasOfferExitEventOccurrence")
ControlNode_isReady_ControlNodeEntryEventOccurrence = Class(name="ControlNode::isReady::ControlNodeEntryEventOccurrence")
InitialNode_isReady_InitialNodeEntryEventOccurrence = Class(name="InitialNode::isReady::InitialNodeEntryEventOccurrence")
InitialNode_isReady_InitialNodeExitEventOccurrence = Class(name="InitialNode::isReady::InitialNodeExitEventOccurrence")
InitialNode_fire_initialNodeEntryEventOccurrence = Class(name="InitialNode::fire::initialNodeEntryEventOccurrence")
InitialNode_fire_initialNodeExitEventOccurrence = Class(name="InitialNode::fire::initialNodeExitEventOccurrence")
ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence = Class(name="ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence")
ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence = Class(name="ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence")
Action_isReady_actionExitEventOccurrence = Class(name="Action::isReady::actionExitEventOccurrence")
Action_fire_actionEntryEventOccurrence = Class(name="Action::fire::actionEntryEventOccurrence")
Action_fire_actionExitEventOccurrence = Class(name="Action::fire::actionExitEventOccurrence")
OpaqueAction_doAction_opaqueActionEntryEventOccurrence = Class(name="OpaqueAction::doAction::opaqueActionEntryEventOccurrence")
OpaqueAction_doAction_opaqueActionExitEventOccurrence = Class(name="OpaqueAction::doAction::opaqueActionExitEventOccurrence")
DecisionNode_fire_decisionNodeExitEventOccurrence = Class(name="DecisionNode::fire::decisionNodeExitEventOccurrence")
IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence = Class(name="IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence")
IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence = Class(name="IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence")
IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence = Class(name="IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence")
IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence = Class(name="IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence")
StringVariable_setCurrentValue_stringVariableEntryEventOccurrence = Class(name="StringVariable::setCurrentValue::stringVariableEntryEventOccurrence")
ForkNode_fire_forkNodeEntryEventOccurrence = Class(name="ForkNode::fire::forkNodeEntryEventOccurrence")
ForkNode_fire_forkNodeExitEventOccurrence = Class(name="ForkNode::fire::forkNodeExitEventOccurrence")
MergeNode_hasOffers_mergeNodeEntryEventOccurrence = Class(name="MergeNode::hasOffers::mergeNodeEntryEventOccurrence")
MergeNode_hasOffers_mergeNodeExitEventOccurrence = Class(name="MergeNode::hasOffers::mergeNodeExitEventOccurrence")
DecisionNode_fire_decisionNodeEntryEventOccurrence = Class(name="DecisionNode::fire::decisionNodeEntryEventOccurrence")
BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence = Class(name="BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence")
BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence = Class(name="BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence")
IntegerExpression_getOperandCurrentValuesEntryEventOccurrence = Class(name="IntegerExpression::getOperandCurrentValuesEntryEventOccurrence")
IntegerExpression_getOperandCurrentValuesExitEventOccurrence = Class(name="IntegerExpression::getOperandCurrentValuesExitEventOccurrence")
IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence = Class(name="IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence")
StringVariable_setCurrentValue_stringVariableExitEventOccurrence = Class(name="StringVariable::setCurrentValue::stringVariableExitEventOccurrence")
StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence = Class(name="StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence")
StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence = Class(name="StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence")
BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence = Class(name="BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence")
BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence = Class(name="BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence")
IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence = Class(name="IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence")
IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence = Class(name="IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence")
IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence")
IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence")
IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence")
IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence = Class(name="IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence")
IntegerCalculationExpression_evaluateADDEntryEventOccurrence = Class(name="IntegerCalculationExpression::evaluateADDEntryEventOccurrence")
IntegerCalculationExpression_evaluateADDExitEventOccurrence = Class(name="IntegerCalculationExpression::evaluateADDExitEventOccurrence")
IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence = Class(name="IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence")
IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence = Class(name="IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence")
IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence")
IntegerComparisonExpression_evaluateGREATERExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATERExitEventOccurrence")
BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence = Class(name="BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence")
BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence = Class(name="BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence")
IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence")
IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence")
BooleanBinaryExpression_evaluateANDEntryEventOccurrence = Class(name="BooleanBinaryExpression::evaluateANDEntryEventOccurrence")
BooleanBinaryExpression_evaluateANDExitEventOccurrence = Class(name="BooleanBinaryExpression::evaluateANDExitEventOccurrence")
BooleanBinaryExpression_evaluateOREntryEventOccurrence = Class(name="BooleanBinaryExpression::evaluateOREntryEventOccurrence")
BooleanBinaryExpression_evaluateORExitEventOccurrence = Class(name="BooleanBinaryExpression::evaluateORExitEventOccurrence")
Token_isWithdrawnEntryEventOccurrence = Class(name="Token::isWithdrawnEntryEventOccurrence")
BooleanUnaryExpression_evaluateNOTEntryEventOccurrence = Class(name="BooleanUnaryExpression::evaluateNOTEntryEventOccurrence")
BooleanUnaryExpression_evaluateNOTExitEventOccurrence = Class(name="BooleanUnaryExpression::evaluateNOTExitEventOccurrence")
BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence = Class(name="BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence")
BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence = Class(name="BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence")
Token_withdrawEntryEventOccurrence = Class(name="Token::withdrawEntryEventOccurrence")
Token_withdrawExitEventOccurrence = Class(name="Token::withdrawExitEventOccurrence")
ForkedToken_withdraw_forkedTokenEntryEventOccurrence = Class(name="ForkedToken::withdraw::forkedTokenEntryEventOccurrence")
ForkedToken_withdraw_forkedTokenExitEventOccurrence = Class(name="ForkedToken::withdraw::forkedTokenExitEventOccurrence")
Offer_hasTokensEntryEventOccurrence = Class(name="Offer::hasTokensEntryEventOccurrence")
Token_isWithdrawnExitEventOccurrence = Class(name="Token::isWithdrawnExitEventOccurrence")
Token_transferEntryEventOccurrence = Class(name="Token::transferEntryEventOccurrence")
Token_transferExitEventOccurrence = Class(name="Token::transferExitEventOccurrence")
trace_Events_Activity_initializeExitEventOccurrence = Class(name="trace::Events::Activity::initializeExitEventOccurrence")
trace_Events_Activity_runEntryEventOccurrence = Class(name="trace::Events::Activity::runEntryEventOccurrence")
trace_Events_Activity_runExitEventOccurrence = Class(name="trace::Events::Activity::runExitEventOccurrence")
trace_Events_Activity_runNodesEntryEventOccurrence = Class(name="trace::Events::Activity::runNodesEntryEventOccurrence")
trace_Events_Activity_runNodesExitEventOccurrence = Class(name="trace::Events::Activity::runNodesExitEventOccurrence")
Offer_hasTokensExitEventOccurrence = Class(name="Offer::hasTokensExitEventOccurrence")
trace_Events_Activity_mainEntryEventOccurrence = Class(name="trace::Events::Activity::mainEntryEventOccurrence")
activitydiagram_TracedActivity = Class(name="activitydiagram::TracedActivity")
Events_trace_EObject = Class(name="Events::trace::EObject")
trace_Events_Activity_mainExitEventOccurrence = Class(name="trace::Events::Activity::mainExitEventOccurrence")
trace_Events_Activity_initializeEntryEventOccurrence = Class(name="trace::Events::Activity::initializeEntryEventOccurrence")
trace_Events_Activity_selectNextNodeExitEventOccurrence = Class(name="trace::Events::Activity::selectNextNodeExitEventOccurrence")
trace_Events_Activity_terminateEntryEventOccurrence = Class(name="trace::Events::Activity::terminateEntryEventOccurrence")
trace_Events_Activity_terminateExitEventOccurrence = Class(name="trace::Events::Activity::terminateExitEventOccurrence")
trace_Events_Activity_getInitialNodeEntryEventOccurrence = Class(name="trace::Events::Activity::getInitialNodeEntryEventOccurrence")
trace_Events_Activity_getInitialNodeExitEventOccurrence = Class(name="trace::Events::Activity::getInitialNodeExitEventOccurrence")
trace_Events_Activity_fireInitialNodeEntryEventOccurrence = Class(name="trace::Events::Activity::fireInitialNodeEntryEventOccurrence")
trace_Events_Activity_fireInitialNodeExitEventOccurrence = Class(name="trace::Events::Activity::fireInitialNodeExitEventOccurrence")
trace_Events_Activity_getEnabledNodesEntryEventOccurrence = Class(name="trace::Events::Activity::getEnabledNodesEntryEventOccurrence")
trace_Events_Activity_getEnabledNodesExitEventOccurrence = Class(name="trace::Events::Activity::getEnabledNodesExitEventOccurrence")
trace_Events_Activity_selectNextNodeEntryEventOccurrence = Class(name="trace::Events::Activity::selectNextNodeEntryEventOccurrence")
trace_Events_ActivityNode_isRunningEntryEventOccurrence = Class(name="trace::Events::ActivityNode::isRunningEntryEventOccurrence")
trace_Events_ActivityNode_isRunningExitEventOccurrence = Class(name="trace::Events::ActivityNode::isRunningExitEventOccurrence")
trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence = Class(name="trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence")
trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence = Class(name="trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence")
trace_Events_ActivityNode_sendOffersEntryEventOccurrence = Class(name="trace::Events::ActivityNode::sendOffersEntryEventOccurrence")
trace_Events_Activity_fireNodeEntryEventOccurrence = Class(name="trace::Events::Activity::fireNodeEntryEventOccurrence")
trace_Events_Activity_fireNodeExitEventOccurrence = Class(name="trace::Events::Activity::fireNodeExitEventOccurrence")
trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence = Class(name="trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence")
activitydiagram_TracedActivityNode = Class(name="activitydiagram::TracedActivityNode")
trace_Events_ActivityNode_run_activityNodeExitEventOccurrence = Class(name="trace::Events::ActivityNode::run::activityNodeExitEventOccurrence")
trace_Events_ActivityNode_addTokensExitEventOccurrence = Class(name="trace::Events::ActivityNode::addTokensExitEventOccurrence")
trace_Events_ActivityNode_removeTokenEntryEventOccurrence = Class(name="trace::Events::ActivityNode::removeTokenEntryEventOccurrence")
trace_Events_ActivityNode_removeTokenExitEventOccurrence = Class(name="trace::Events::ActivityNode::removeTokenExitEventOccurrence")
trace_Events_ActivityNode_hasOffersEntryEventOccurrence = Class(name="trace::Events::ActivityNode::hasOffersEntryEventOccurrence")
trace_Events_ActivityNode_sendOffersExitEventOccurrence = Class(name="trace::Events::ActivityNode::sendOffersExitEventOccurrence")
trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence = Class(name="trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence")
trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence = Class(name="trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence")
trace_Events_ActivityNode_addTokensEntryEventOccurrence = Class(name="trace::Events::ActivityNode::addTokensEntryEventOccurrence")
activitydiagram_TracedActivityEdge = Class(name="activitydiagram::TracedActivityEdge")
trace_Events_ActivityEdge_sendOfferExitEventOccurrence = Class(name="trace::Events::ActivityEdge::sendOfferExitEventOccurrence")
trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence = Class(name="trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence")
trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence = Class(name="trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence")
trace_Events_ActivityEdge_hasOfferEntryEventOccurrence = Class(name="trace::Events::ActivityEdge::hasOfferEntryEventOccurrence")
trace_Events_ActivityNode_hasOffersExitEventOccurrence = Class(name="trace::Events::ActivityNode::hasOffersExitEventOccurrence")
trace_Events_ActivityNode_isReadyEntryEventOccurrence = Class(name="trace::Events::ActivityNode::isReadyEntryEventOccurrence")
trace_Events_ActivityNode_isReadyExitEventOccurrence = Class(name="trace::Events::ActivityNode::isReadyExitEventOccurrence")
trace_Events_ActivityEdge_sendOfferEntryEventOccurrence = Class(name="trace::Events::ActivityEdge::sendOfferEntryEventOccurrence")
activitydiagramConfiguration_TracedToken = Class(name="activitydiagramConfiguration::TracedToken")
trace_Events_ControlNode_fire_controlNodeExitEventOccurrence = Class(name="trace::Events::ControlNode::fire::controlNodeExitEventOccurrence")
trace_Events_Action_sendOffers_actionEntryEventOccurrence = Class(name="trace::Events::Action::sendOffers::actionEntryEventOccurrence")
activitydiagram_TracedAction = Class(name="activitydiagram::TracedAction")
trace_Events_Action_sendOffers_actionExitEventOccurrence = Class(name="trace::Events::Action::sendOffers::actionExitEventOccurrence")
trace_Events_Action_isReady_actionEntryEventOccurrence = Class(name="trace::Events::Action::isReady::actionEntryEventOccurrence")
trace_Events_Action_isReady_actionExitEventOccurrence = Class(name="trace::Events::Action::isReady::actionExitEventOccurrence")
trace_Events_ActivityEdge_hasOfferExitEventOccurrence = Class(name="trace::Events::ActivityEdge::hasOfferExitEventOccurrence")
trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence = Class(name="trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence")
activitydiagram_TracedControlNode = Class(name="activitydiagram::TracedControlNode")
trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence = Class(name="trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence")
trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence = Class(name="trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence")
trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence = Class(name="trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence")
activitydiagram_TracedInitialNode = Class(name="activitydiagram::TracedInitialNode")
trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence = Class(name="trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence")
trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence = Class(name="trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence")
trace_Events_InitialNode_fire_initialNodeExitEventOccurrence = Class(name="trace::Events::InitialNode::fire::initialNodeExitEventOccurrence")
trace_Events_Action_fire_actionEntryEventOccurrence = Class(name="trace::Events::Action::fire::actionEntryEventOccurrence")
trace_Events_Action_fire_actionExitEventOccurrence = Class(name="trace::Events::Action::fire::actionExitEventOccurrence")
trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence = Class(name="trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence")
activitydiagram_TracedOpaqueAction = Class(name="activitydiagram::TracedOpaqueAction")
trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence = Class(name="trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence")
trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence = Class(name="trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence")
activitydiagram_TracedMergeNode = Class(name="activitydiagram::TracedMergeNode")
trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence = Class(name="trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence")
trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence = Class(name="trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence")
activitydiagram_TracedDecisionNode = Class(name="activitydiagram::TracedDecisionNode")
trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence = Class(name="trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence")
trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence = Class(name="trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence")
activitydiagram_TracedActivityFinalNode = Class(name="activitydiagram::TracedActivityFinalNode")
trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence = Class(name="trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence")
trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence = Class(name="trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence")
activitydiagram_TracedForkNode = Class(name="activitydiagram::TracedForkNode")
trace_Events_ForkNode_fire_forkNodeExitEventOccurrence = Class(name="trace::Events::ForkNode::fire::forkNodeExitEventOccurrence")
trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence = Class(name="trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence")
activitydiagram_TracedStringVariable = Class(name="activitydiagram::TracedStringVariable")
trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence = Class(name="trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence")
trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence = Class(name="trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence")
trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence = Class(name="trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence")
trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence = Class(name="trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence")
activitydiagram_TracedIntegerVariable = Class(name="activitydiagram::TracedIntegerVariable")
Events_trace_Value = Class(name="Events::trace::Value")
trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence = Class(name="trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence")
trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence = Class(name="trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence")
trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence = Class(name="trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence")
trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence = Class(name="trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence")
trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence = Class(name="trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence")
trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence = Class(name="trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence")
trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence = Class(name="trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence")
Events_trace_IntegerExpression = Class(name="Events::trace::IntegerExpression")
trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence = Class(name="trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence")
activitydiagram_TracedBooleanVariable = Class(name="activitydiagram::TracedBooleanVariable")
trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence")
trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence")
trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence")
trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence")
trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence = Class(name="trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence")
trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence")
Events_trace_IntegerCalculationExpression = Class(name="Events::trace::IntegerCalculationExpression")
trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence")
trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence = Class(name="trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence")
Events_trace_IntegerComparisonExpression = Class(name="Events::trace::IntegerComparisonExpression")
trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence")
trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence = Class(name="trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence")
Events_trace_BooleanUnaryExpression = Class(name="Events::trace::BooleanUnaryExpression")
trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence = Class(name="trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence")
trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence = Class(name="trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence")
trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence = Class(name="trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence")
trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence = Class(name="trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence")
trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence")
trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence")
trace_Events_Token_isWithdrawnEntryEventOccurrence = Class(name="trace::Events::Token::isWithdrawnEntryEventOccurrence")
trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence")
Events_trace_BooleanBinaryExpression = Class(name="Events::trace::BooleanBinaryExpression")
trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence")
trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence")
trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence = Class(name="trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence")
trace_Events_Token_withdrawEntryEventOccurrence = Class(name="trace::Events::Token::withdrawEntryEventOccurrence")
trace_Events_Token_withdrawExitEventOccurrence = Class(name="trace::Events::Token::withdrawExitEventOccurrence")
trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence = Class(name="trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence")
activitydiagramConfiguration_TracedForkedToken = Class(name="activitydiagramConfiguration::TracedForkedToken")
trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence = Class(name="trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence")
trace_Events_Token_isWithdrawnExitEventOccurrence = Class(name="trace::Events::Token::isWithdrawnExitEventOccurrence")
trace_Events_Token_transferEntryEventOccurrence = Class(name="trace::Events::Token::transferEntryEventOccurrence")
trace_Events_Token_transferExitEventOccurrence = Class(name="trace::Events::Token::transferExitEventOccurrence")
activitydiagramConfiguration_TracedInputValue = Class(name="activitydiagramConfiguration::TracedInputValue")
States_trace_GlobalState = Class(name="States::trace::GlobalState")
trace_States_InputValue_variable_State = Class(name="trace::States::InputValue::variable::State")
activitydiagram_TracedVariable = Class(name="activitydiagram::TracedVariable")
trace_States_Token_holder_State = Class(name="trace::States::Token::holder::State")
trace_Events_Offer_hasTokensEntryEventOccurrence = Class(name="trace::Events::Offer::hasTokensEntryEventOccurrence")
activitydiagramConfiguration_TracedOffer = Class(name="activitydiagramConfiguration::TracedOffer")
trace_Events_Offer_hasTokensExitEventOccurrence = Class(name="trace::Events::Offer::hasTokensExitEventOccurrence")
trace_States_InputValue_value_State = Class(name="trace::States::InputValue::value::State")
States_trace_Value = Class(name="States::trace::Value")
trace_States_ForkedToken_baseToken_State = Class(name="trace::States::ForkedToken::baseToken::State")
trace_States_ForkedToken_baseTokenIsWithdrawn_State = Class(name="trace::States::ForkedToken::baseTokenIsWithdrawn::State")
trace_States_ActivityEdge_offers_State = Class(name="trace::States::ActivityEdge::offers::State")
trace_States_Input_inputValues_State = Class(name="trace::States::Input::inputValues::State")
activitydiagramConfiguration_TracedInput = Class(name="activitydiagramConfiguration::TracedInput")
trace_States_ForkedToken_remainingOffersCount_State = Class(name="trace::States::ForkedToken::remainingOffersCount::State")
trace_States_Offer_offeredTokens_State = Class(name="trace::States::Offer::offeredTokens::State")
trace_States_Variable_currentValue_State = Class(name="trace::States::Variable::currentValue::State")
trace_States_Activity_trace_State = Class(name="trace::States::Activity::trace::State")
activitydiagramConfiguration_TracedTrace = Class(name="activitydiagramConfiguration::TracedTrace")
trace_States_ActivityNode_running_State = Class(name="trace::States::ActivityNode::running::State")
trace_States_ActivityNode_heldTokens_State = Class(name="trace::States::ActivityNode::heldTokens::State")
trace_Traced_TracedObjects = Class(name="trace::Traced::TracedObjects")
activitydiagram_TracedControlFlow = Class(name="activitydiagram::TracedControlFlow")
activitydiagramConfiguration_TracedControlToken = Class(name="activitydiagramConfiguration::TracedControlToken")
trace_States_Trace_executedNodes_State = Class(name="trace::States::Trace::executedNodes::State")
activitydiagram_TracedJoinNode = Class(name="activitydiagram::TracedJoinNode")
trace_activitydiagram_TracedControlFlow = Class(name="trace::activitydiagram::TracedControlFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
activitydiagram_trace_ControlFlow = Class(name="activitydiagram::trace::ControlFlow")
trace_activitydiagram_TracedMergeNode = Class(name="trace::activitydiagram::TracedMergeNode")
TracedControlNode = Class(name="TracedControlNode")
activitydiagram_trace_MergeNode = Class(name="activitydiagram::trace::MergeNode")
trace_activitydiagram_TracedNamedElement = Class(name="trace::activitydiagram::TracedNamedElement", is_abstract=True)
trace_activitydiagram_TracedVariable = Class(name="trace::activitydiagram::TracedVariable", is_abstract=True)
activitydiagram_trace_Value = Class(name="activitydiagram::trace::Value")
trace_activitydiagram_TracedAction = Class(name="trace::activitydiagram::TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
trace_activitydiagram_TracedActivityFinalNode = Class(name="trace::activitydiagram::TracedActivityFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
activitydiagram_trace_ActivityFinalNode = Class(name="activitydiagram::trace::ActivityFinalNode")
trace_activitydiagram_TracedForkNode = Class(name="trace::activitydiagram::TracedForkNode")
activitydiagram_trace_ForkNode = Class(name="activitydiagram::trace::ForkNode")
trace_activitydiagram_TracedInitialNode = Class(name="trace::activitydiagram::TracedInitialNode")
activitydiagram_trace_InitialNode = Class(name="activitydiagram::trace::InitialNode")
trace_activitydiagram_TracedBooleanVariable = Class(name="trace::activitydiagram::TracedBooleanVariable")
TracedVariable = Class(name="TracedVariable")
activitydiagram_trace_BooleanVariable = Class(name="activitydiagram::trace::BooleanVariable")
trace_activitydiagram_TracedExecutableNode = Class(name="trace::activitydiagram::TracedExecutableNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
trace_activitydiagram_TracedIntegerVariable = Class(name="trace::activitydiagram::TracedIntegerVariable")
activitydiagram_trace_IntegerVariable = Class(name="activitydiagram::trace::IntegerVariable")
trace_activitydiagram_TracedActivityEdge = Class(name="trace::activitydiagram::TracedActivityEdge", is_abstract=True)
TracedNamedElement = Class(name="TracedNamedElement")
trace_activitydiagram_TracedActivity = Class(name="trace::activitydiagram::TracedActivity")
activitydiagram_trace_Activity = Class(name="activitydiagram::trace::Activity")
trace_activitydiagram_TracedStringVariable = Class(name="trace::activitydiagram::TracedStringVariable")
activitydiagram_trace_StringVariable = Class(name="activitydiagram::trace::StringVariable")
trace_activitydiagram_TracedActivityNode = Class(name="trace::activitydiagram::TracedActivityNode", is_abstract=True)
trace_activitydiagramConfiguration_TracedInputValue = Class(name="trace::activitydiagramConfiguration::TracedInputValue")
trace_activitydiagramConfiguration_TracedToken = Class(name="trace::activitydiagramConfiguration::TracedToken", is_abstract=True)
trace_activitydiagramConfiguration_TracedControlToken = Class(name="trace::activitydiagramConfiguration::TracedControlToken")
TracedToken = Class(name="TracedToken")
trace_activitydiagramConfiguration_TracedInput = Class(name="trace::activitydiagramConfiguration::TracedInput")
trace_activitydiagramConfiguration_TracedForkedToken = Class(name="trace::activitydiagramConfiguration::TracedForkedToken")
trace_activitydiagram_TracedOpaqueAction = Class(name="trace::activitydiagram::TracedOpaqueAction")
TracedAction = Class(name="TracedAction")
activitydiagram_trace_Expression = Class(name="activitydiagram::trace::Expression")
activitydiagram_trace_OpaqueAction = Class(name="activitydiagram::trace::OpaqueAction")
trace_activitydiagram_TracedJoinNode = Class(name="trace::activitydiagram::TracedJoinNode")
activitydiagram_trace_JoinNode = Class(name="activitydiagram::trace::JoinNode")
trace_activitydiagram_TracedDecisionNode = Class(name="trace::activitydiagram::TracedDecisionNode")
activitydiagram_trace_DecisionNode = Class(name="activitydiagram::trace::DecisionNode")
trace_activitydiagram_TracedFinalNode = Class(name="trace::activitydiagram::TracedFinalNode", is_abstract=True)
trace_activitydiagram_TracedControlNode = Class(name="trace::activitydiagram::TracedControlNode", is_abstract=True)
trace_activitydiagramConfiguration_TracedOffer = Class(name="trace::activitydiagramConfiguration::TracedOffer")
trace_activitydiagramConfiguration_TracedTrace = Class(name="trace::activitydiagramConfiguration::TracedTrace")

# trace_Trace class attributes and methods

# trace_GlobalState class attributes and methods

# Events class attributes and methods

# TracedObjects class attributes and methods

# trace_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# InputValue_value_State class attributes and methods

# InputValue_variable_State class attributes and methods

# Token_holder_State class attributes and methods

# Input_inputValues_State class attributes and methods

# ForkedToken_remainingOffersCount_State class attributes and methods

# ForkedToken_baseToken_State class attributes and methods

# ForkedToken_baseTokenIsWithdrawn_State class attributes and methods

# ActivityEdge_offers_State class attributes and methods

# Variable_currentValue_State class attributes and methods

# Offer_offeredTokens_State class attributes and methods

# trace_BooleanValue class attributes and methods

# trace_IntegerComparisonExpression class attributes and methods

# trace_BooleanUnaryExpression class attributes and methods

# trace_IntegerCalculationExpression class attributes and methods

# trace_Events_EventOccurrence class attributes and methods

# Events_trace_GlobalState class attributes and methods

# trace_Events_Events class attributes and methods

# Activity_mainEntryEventOccurrence class attributes and methods

# Activity_mainExitEventOccurrence class attributes and methods

# Activity_initializeEntryEventOccurrence class attributes and methods

# Activity_initializeExitEventOccurrence class attributes and methods

# ActivityNode_running_State class attributes and methods

# ActivityNode_heldTokens_State class attributes and methods

# Activity_trace_State class attributes and methods

# Trace_executedNodes_State class attributes and methods

# trace_BooleanBinaryExpression class attributes and methods

# trace_StringValue class attributes and methods

# trace_IntegerValue class attributes and methods

# Activity_selectNextNodeEntryEventOccurrence class attributes and methods

# Activity_selectNextNodeExitEventOccurrence class attributes and methods

# Activity_terminateEntryEventOccurrence class attributes and methods

# Activity_terminateExitEventOccurrence class attributes and methods

# Activity_getInitialNodeEntryEventOccurrence class attributes and methods

# Activity_getInitialNodeExitEventOccurrence class attributes and methods

# Activity_fireNodeEntryEventOccurrence class attributes and methods

# Activity_fireNodeExitEventOccurrence class attributes and methods

# ActivityNode_run_activityNodeEntryEventOccurrence class attributes and methods

# Activity_runEntryEventOccurrence class attributes and methods

# Activity_runExitEventOccurrence class attributes and methods

# Activity_runNodesEntryEventOccurrence class attributes and methods

# Activity_runNodesExitEventOccurrence class attributes and methods

# Activity_fireInitialNodeEntryEventOccurrence class attributes and methods

# Activity_fireInitialNodeExitEventOccurrence class attributes and methods

# Activity_getEnabledNodesEntryEventOccurrence class attributes and methods

# Activity_getEnabledNodesExitEventOccurrence class attributes and methods

# ActivityNode_sendOffersExitEventOccurrence class attributes and methods

# ActivityNode_takeOfferedTokensEntryEventOccurrence class attributes and methods

# ActivityNode_run_activityNodeExitEventOccurrence class attributes and methods

# ActivityNode_isRunningEntryEventOccurrence class attributes and methods

# ActivityNode_isRunningExitEventOccurrence class attributes and methods

# ActivityNode_terminate_activityNodeEntryEventOccurrence class attributes and methods

# ActivityNode_terminate_activityNodeExitEventOccurrence class attributes and methods

# ActivityNode_sendOffersEntryEventOccurrence class attributes and methods

# ActivityNode_hasOffersEntryEventOccurrence class attributes and methods

# ActivityNode_hasOffersExitEventOccurrence class attributes and methods

# ActivityNode_isReadyEntryEventOccurrence class attributes and methods

# ActivityNode_isReadyExitEventOccurrence class attributes and methods

# ActivityEdge_sendOfferEntryEventOccurrence class attributes and methods

# ActivityEdge_sendOfferExitEventOccurrence class attributes and methods

# ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence class attributes and methods

# ActivityNode_takeOfferedTokensExitEventOccurrence class attributes and methods

# ActivityNode_addTokensEntryEventOccurrence class attributes and methods

# ActivityNode_addTokensExitEventOccurrence class attributes and methods

# ActivityNode_removeTokenEntryEventOccurrence class attributes and methods

# ActivityNode_removeTokenExitEventOccurrence class attributes and methods

# ControlNode_isReady_ControlNodeExitEventOccurrence class attributes and methods

# ControlNode_fire_controlNodeEntryEventOccurrence class attributes and methods

# ControlNode_fire_controlNodeExitEventOccurrence class attributes and methods

# Action_sendOffers_actionEntryEventOccurrence class attributes and methods

# Action_sendOffers_actionExitEventOccurrence class attributes and methods

# Action_isReady_actionEntryEventOccurrence class attributes and methods

# ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence class attributes and methods

# ActivityEdge_hasOfferEntryEventOccurrence class attributes and methods

# ActivityEdge_hasOfferExitEventOccurrence class attributes and methods

# ControlNode_isReady_ControlNodeEntryEventOccurrence class attributes and methods

# InitialNode_isReady_InitialNodeEntryEventOccurrence class attributes and methods

# InitialNode_isReady_InitialNodeExitEventOccurrence class attributes and methods

# InitialNode_fire_initialNodeEntryEventOccurrence class attributes and methods

# InitialNode_fire_initialNodeExitEventOccurrence class attributes and methods

# ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence class attributes and methods

# ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence class attributes and methods

# Action_isReady_actionExitEventOccurrence class attributes and methods

# Action_fire_actionEntryEventOccurrence class attributes and methods

# Action_fire_actionExitEventOccurrence class attributes and methods

# OpaqueAction_doAction_opaqueActionEntryEventOccurrence class attributes and methods

# OpaqueAction_doAction_opaqueActionExitEventOccurrence class attributes and methods

# DecisionNode_fire_decisionNodeExitEventOccurrence class attributes and methods

# IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence class attributes and methods

# IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence class attributes and methods

# IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence class attributes and methods

# IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence class attributes and methods

# StringVariable_setCurrentValue_stringVariableEntryEventOccurrence class attributes and methods

# ForkNode_fire_forkNodeEntryEventOccurrence class attributes and methods

# ForkNode_fire_forkNodeExitEventOccurrence class attributes and methods

# MergeNode_hasOffers_mergeNodeEntryEventOccurrence class attributes and methods

# MergeNode_hasOffers_mergeNodeExitEventOccurrence class attributes and methods

# DecisionNode_fire_decisionNodeEntryEventOccurrence class attributes and methods

# BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence class attributes and methods

# BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence class attributes and methods

# IntegerExpression_getOperandCurrentValuesEntryEventOccurrence class attributes and methods

# IntegerExpression_getOperandCurrentValuesExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence class attributes and methods

# StringVariable_setCurrentValue_stringVariableExitEventOccurrence class attributes and methods

# StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence class attributes and methods

# StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence class attributes and methods

# BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence class attributes and methods

# BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence class attributes and methods

# IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateADDEntryEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateADDExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATERExitEventOccurrence class attributes and methods

# BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence class attributes and methods

# BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateANDEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateANDExitEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateOREntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateORExitEventOccurrence class attributes and methods

# Token_isWithdrawnEntryEventOccurrence class attributes and methods

# BooleanUnaryExpression_evaluateNOTEntryEventOccurrence class attributes and methods

# BooleanUnaryExpression_evaluateNOTExitEventOccurrence class attributes and methods

# BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence class attributes and methods

# Token_withdrawEntryEventOccurrence class attributes and methods

# Token_withdrawExitEventOccurrence class attributes and methods

# ForkedToken_withdraw_forkedTokenEntryEventOccurrence class attributes and methods

# ForkedToken_withdraw_forkedTokenExitEventOccurrence class attributes and methods

# Offer_hasTokensEntryEventOccurrence class attributes and methods

# Token_isWithdrawnExitEventOccurrence class attributes and methods

# Token_transferEntryEventOccurrence class attributes and methods

# Token_transferExitEventOccurrence class attributes and methods

# trace_Events_Activity_initializeExitEventOccurrence class attributes and methods

# trace_Events_Activity_runEntryEventOccurrence class attributes and methods

# trace_Events_Activity_runExitEventOccurrence class attributes and methods

# trace_Events_Activity_runNodesEntryEventOccurrence class attributes and methods

# trace_Events_Activity_runNodesExitEventOccurrence class attributes and methods

# Offer_hasTokensExitEventOccurrence class attributes and methods

# trace_Events_Activity_mainEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivity class attributes and methods

# Events_trace_EObject class attributes and methods

# trace_Events_Activity_mainExitEventOccurrence class attributes and methods

# trace_Events_Activity_initializeEntryEventOccurrence class attributes and methods

# trace_Events_Activity_selectNextNodeExitEventOccurrence class attributes and methods

# trace_Events_Activity_terminateEntryEventOccurrence class attributes and methods

# trace_Events_Activity_terminateExitEventOccurrence class attributes and methods

# trace_Events_Activity_getInitialNodeEntryEventOccurrence class attributes and methods

# trace_Events_Activity_getInitialNodeExitEventOccurrence class attributes and methods

# trace_Events_Activity_fireInitialNodeEntryEventOccurrence class attributes and methods

# trace_Events_Activity_fireInitialNodeExitEventOccurrence class attributes and methods

# trace_Events_Activity_getEnabledNodesEntryEventOccurrence class attributes and methods

# trace_Events_Activity_getEnabledNodesExitEventOccurrence class attributes and methods

# trace_Events_Activity_selectNextNodeEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_isRunningEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_isRunningExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_sendOffersEntryEventOccurrence class attributes and methods

# trace_Events_Activity_fireNodeEntryEventOccurrence class attributes and methods

# trace_Events_Activity_fireNodeExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityNode class attributes and methods

# trace_Events_ActivityNode_run_activityNodeExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_addTokensExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_removeTokenEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_removeTokenExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_hasOffersEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_sendOffersExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_addTokensEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityEdge class attributes and methods

# trace_Events_ActivityEdge_sendOfferExitEventOccurrence class attributes and methods

# trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence class attributes and methods

# trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence class attributes and methods

# trace_Events_ActivityEdge_hasOfferEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_hasOffersExitEventOccurrence class attributes and methods

# trace_Events_ActivityNode_isReadyEntryEventOccurrence class attributes and methods

# trace_Events_ActivityNode_isReadyExitEventOccurrence class attributes and methods

# trace_Events_ActivityEdge_sendOfferEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedToken class attributes and methods

# trace_Events_ControlNode_fire_controlNodeExitEventOccurrence class attributes and methods

# trace_Events_Action_sendOffers_actionEntryEventOccurrence class attributes and methods

# activitydiagram_TracedAction class attributes and methods

# trace_Events_Action_sendOffers_actionExitEventOccurrence class attributes and methods

# trace_Events_Action_isReady_actionEntryEventOccurrence class attributes and methods

# trace_Events_Action_isReady_actionExitEventOccurrence class attributes and methods

# trace_Events_ActivityEdge_hasOfferExitEventOccurrence class attributes and methods

# trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedControlNode class attributes and methods

# trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence class attributes and methods

# trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence class attributes and methods

# trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedInitialNode class attributes and methods

# trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence class attributes and methods

# trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence class attributes and methods

# trace_Events_InitialNode_fire_initialNodeExitEventOccurrence class attributes and methods

# trace_Events_Action_fire_actionEntryEventOccurrence class attributes and methods

# trace_Events_Action_fire_actionExitEventOccurrence class attributes and methods

# trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence class attributes and methods

# activitydiagram_TracedOpaqueAction class attributes and methods

# trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence class attributes and methods

# trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedMergeNode class attributes and methods

# trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence class attributes and methods

# trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedDecisionNode class attributes and methods

# trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence class attributes and methods

# trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityFinalNode class attributes and methods

# trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence class attributes and methods

# trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedForkNode class attributes and methods

# trace_Events_ForkNode_fire_forkNodeExitEventOccurrence class attributes and methods

# trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedStringVariable class attributes and methods

# trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence class attributes and methods

# trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence class attributes and methods

# trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence class attributes and methods

# trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedIntegerVariable class attributes and methods

# Events_trace_Value class attributes and methods

# trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence class attributes and methods

# trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence class attributes and methods

# trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence class attributes and methods

# trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence class attributes and methods

# trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence class attributes and methods

# trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence class attributes and methods

# trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence class attributes and methods

# Events_trace_IntegerExpression class attributes and methods

# trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedBooleanVariable class attributes and methods

# trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence class attributes and methods

# trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence class attributes and methods

# trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence class attributes and methods

# trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence class attributes and methods

# trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence class attributes and methods

# Events_trace_IntegerCalculationExpression class attributes and methods

# trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence class attributes and methods

# trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence class attributes and methods

# Events_trace_IntegerComparisonExpression class attributes and methods

# trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence class attributes and methods

# trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence class attributes and methods

# Events_trace_BooleanUnaryExpression class attributes and methods

# trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence class attributes and methods

# trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence class attributes and methods

# trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence class attributes and methods

# trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence class attributes and methods

# trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence class attributes and methods

# trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence class attributes and methods

# trace_Events_Token_isWithdrawnEntryEventOccurrence class attributes and methods

# trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence class attributes and methods

# Events_trace_BooleanBinaryExpression class attributes and methods

# trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence class attributes and methods

# trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence class attributes and methods

# trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence class attributes and methods

# trace_Events_Token_withdrawEntryEventOccurrence class attributes and methods

# trace_Events_Token_withdrawExitEventOccurrence class attributes and methods

# trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedForkedToken class attributes and methods

# trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence class attributes and methods

# trace_Events_Token_isWithdrawnExitEventOccurrence class attributes and methods

# trace_Events_Token_transferEntryEventOccurrence class attributes and methods

# trace_Events_Token_transferExitEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedInputValue class attributes and methods

# States_trace_GlobalState class attributes and methods

# trace_States_InputValue_variable_State class attributes and methods

# activitydiagram_TracedVariable class attributes and methods

# trace_States_Token_holder_State class attributes and methods

# trace_Events_Offer_hasTokensEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedOffer class attributes and methods

# trace_Events_Offer_hasTokensExitEventOccurrence class attributes and methods

# trace_States_InputValue_value_State class attributes and methods

# States_trace_Value class attributes and methods

# trace_States_ForkedToken_baseToken_State class attributes and methods

# trace_States_ForkedToken_baseTokenIsWithdrawn_State class attributes and methods
trace_States_ForkedToken_baseTokenIsWithdrawn_State_baseTokenIsWithdrawn: Property = Property(name="baseTokenIsWithdrawn", type=BooleanType)
trace_States_ForkedToken_baseTokenIsWithdrawn_State.attributes={trace_States_ForkedToken_baseTokenIsWithdrawn_State_baseTokenIsWithdrawn}

# trace_States_ActivityEdge_offers_State class attributes and methods

# trace_States_Input_inputValues_State class attributes and methods

# activitydiagramConfiguration_TracedInput class attributes and methods

# trace_States_ForkedToken_remainingOffersCount_State class attributes and methods
trace_States_ForkedToken_remainingOffersCount_State_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
trace_States_ForkedToken_remainingOffersCount_State.attributes={trace_States_ForkedToken_remainingOffersCount_State_remainingOffersCount}

# trace_States_Offer_offeredTokens_State class attributes and methods

# trace_States_Variable_currentValue_State class attributes and methods

# trace_States_Activity_trace_State class attributes and methods

# activitydiagramConfiguration_TracedTrace class attributes and methods

# trace_States_ActivityNode_running_State class attributes and methods
trace_States_ActivityNode_running_State_running: Property = Property(name="running", type=BooleanType)
trace_States_ActivityNode_running_State.attributes={trace_States_ActivityNode_running_State_running}

# trace_States_ActivityNode_heldTokens_State class attributes and methods

# trace_Traced_TracedObjects class attributes and methods

# activitydiagram_TracedControlFlow class attributes and methods

# activitydiagramConfiguration_TracedControlToken class attributes and methods

# trace_States_Trace_executedNodes_State class attributes and methods

# activitydiagram_TracedJoinNode class attributes and methods

# trace_activitydiagram_TracedControlFlow class attributes and methods

# TracedActivityEdge class attributes and methods

# activitydiagram_trace_ControlFlow class attributes and methods

# trace_activitydiagram_TracedMergeNode class attributes and methods

# TracedControlNode class attributes and methods

# activitydiagram_trace_MergeNode class attributes and methods

# trace_activitydiagram_TracedNamedElement class attributes and methods
trace_activitydiagram_TracedNamedElement_name: Property = Property(name="name", type=StringType)
trace_activitydiagram_TracedNamedElement.attributes={trace_activitydiagram_TracedNamedElement_name}

# trace_activitydiagram_TracedVariable class attributes and methods

# activitydiagram_trace_Value class attributes and methods

# trace_activitydiagram_TracedAction class attributes and methods

# TracedExecutableNode class attributes and methods

# trace_activitydiagram_TracedActivityFinalNode class attributes and methods

# TracedFinalNode class attributes and methods

# activitydiagram_trace_ActivityFinalNode class attributes and methods

# trace_activitydiagram_TracedForkNode class attributes and methods

# activitydiagram_trace_ForkNode class attributes and methods

# trace_activitydiagram_TracedInitialNode class attributes and methods

# activitydiagram_trace_InitialNode class attributes and methods

# trace_activitydiagram_TracedBooleanVariable class attributes and methods

# TracedVariable class attributes and methods

# activitydiagram_trace_BooleanVariable class attributes and methods

# trace_activitydiagram_TracedExecutableNode class attributes and methods

# TracedActivityNode class attributes and methods

# trace_activitydiagram_TracedIntegerVariable class attributes and methods

# activitydiagram_trace_IntegerVariable class attributes and methods

# trace_activitydiagram_TracedActivityEdge class attributes and methods

# TracedNamedElement class attributes and methods

# trace_activitydiagram_TracedActivity class attributes and methods

# activitydiagram_trace_Activity class attributes and methods

# trace_activitydiagram_TracedStringVariable class attributes and methods

# activitydiagram_trace_StringVariable class attributes and methods

# trace_activitydiagram_TracedActivityNode class attributes and methods

# trace_activitydiagramConfiguration_TracedInputValue class attributes and methods

# trace_activitydiagramConfiguration_TracedToken class attributes and methods

# trace_activitydiagramConfiguration_TracedControlToken class attributes and methods

# TracedToken class attributes and methods

# trace_activitydiagramConfiguration_TracedInput class attributes and methods

# trace_activitydiagramConfiguration_TracedForkedToken class attributes and methods

# trace_activitydiagram_TracedOpaqueAction class attributes and methods

# TracedAction class attributes and methods

# activitydiagram_trace_Expression class attributes and methods

# activitydiagram_trace_OpaqueAction class attributes and methods

# trace_activitydiagram_TracedJoinNode class attributes and methods

# activitydiagram_trace_JoinNode class attributes and methods

# trace_activitydiagram_TracedDecisionNode class attributes and methods

# activitydiagram_trace_DecisionNode class attributes and methods

# trace_activitydiagram_TracedFinalNode class attributes and methods

# trace_activitydiagram_TracedControlNode class attributes and methods

# trace_activitydiagramConfiguration_TracedOffer class attributes and methods

# trace_activitydiagramConfiguration_TracedTrace class attributes and methods

# Relationships
globalTrace0: BinaryAssociation = BinaryAssociation(
    name="globalTrace0",
    ends={
        Property(name="trace_GlobalState", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace", type=trace_GlobalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="Events", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace2", type=Events, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tracedObjects3: BinaryAssociation = BinaryAssociation(
    name="tracedObjects3",
    ends={
        Property(name="TracedObjects", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace4", type=TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticObjectsPools5: BinaryAssociation = BinaryAssociation(
    name="staticObjectsPools5",
    ends={
        Property(name="trace_StaticObjectsPools", type=trace_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Trace6", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eventsTriggeredDuringState7: BinaryAssociation = BinaryAssociation(
    name="eventsTriggeredDuringState7",
    ends={
        Property(name="Events8", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="EventOccurrence", type=EventOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
inputValue_value_States9: BinaryAssociation = BinaryAssociation(
    name="inputValue_value_States9",
    ends={
        Property(name="States", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_value_State", type=InputValue_value_State, multiplicity=Multiplicity(0, 9999))
    }
)
inputValue_variable_States10: BinaryAssociation = BinaryAssociation(
    name="inputValue_variable_States10",
    ends={
        Property(name="States11", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_variable_State", type=InputValue_variable_State, multiplicity=Multiplicity(0, 9999))
    }
)
token_holder_States12: BinaryAssociation = BinaryAssociation(
    name="token_holder_States12",
    ends={
        Property(name="States13", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_State", type=Token_holder_State, multiplicity=Multiplicity(0, 9999))
    }
)
input_inputValues_States14: BinaryAssociation = BinaryAssociation(
    name="input_inputValues_States14",
    ends={
        Property(name="States15", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Input_inputValues_State", type=Input_inputValues_State, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_remainingOffersCount_States16: BinaryAssociation = BinaryAssociation(
    name="forkedToken_remainingOffersCount_States16",
    ends={
        Property(name="States17", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_State", type=ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseToken_States18: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseToken_States18",
    ends={
        Property(name="States19", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_State", type=ForkedToken_baseToken_State, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseTokenIsWithdrawn_States20: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseTokenIsWithdrawn_States20",
    ends={
        Property(name="States21", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_State", type=ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdge_offers_States22: BinaryAssociation = BinaryAssociation(
    name="activityEdge_offers_States22",
    ends={
        Property(name="States23", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge_offers_State", type=ActivityEdge_offers_State, multiplicity=Multiplicity(0, 9999))
    }
)
variable_currentValue_States24: BinaryAssociation = BinaryAssociation(
    name="variable_currentValue_States24",
    ends={
        Property(name="States25", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable_currentValue_State", type=Variable_currentValue_State, multiplicity=Multiplicity(0, 9999))
    }
)
pool_BooleanValues42: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanValues42",
    ends={
        Property(name="trace_BooleanValue", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools43", type=trace_BooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerComparisonExpressions44: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerComparisonExpressions44",
    ends={
        Property(name="trace_IntegerComparisonExpression", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools45", type=trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_BooleanUnaryExpressions46: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanUnaryExpressions46",
    ends={
        Property(name="trace_BooleanUnaryExpression", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools47", type=trace_BooleanUnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerCalculationExpressions48: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerCalculationExpressions48",
    ends={
        Property(name="trace_IntegerCalculationExpression", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools49", type=trace_IntegerCalculationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered50: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered50",
    ends={
        Property(name="GlobalState", type=trace_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_trace_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
Activity_mainEntryEventOccurrence_Trace51: BinaryAssociation = BinaryAssociation(
    name="Activity_mainEntryEventOccurrence_Trace51",
    ends={
        Property(name="Activity_mainEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events", type=Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_mainExitEventOccurrence_Trace52: BinaryAssociation = BinaryAssociation(
    name="Activity_mainExitEventOccurrence_Trace52",
    ends={
        Property(name="Activity_mainExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events53", type=Activity_mainExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_initializeEntryEventOccurrence_Trace54: BinaryAssociation = BinaryAssociation(
    name="Activity_initializeEntryEventOccurrence_Trace54",
    ends={
        Property(name="Activity_initializeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events55", type=Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_initializeExitEventOccurrence_Trace56: BinaryAssociation = BinaryAssociation(
    name="Activity_initializeExitEventOccurrence_Trace56",
    ends={
        Property(name="Activity_initializeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events57", type=Activity_initializeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offer_offeredTokens_States26: BinaryAssociation = BinaryAssociation(
    name="offer_offeredTokens_States26",
    ends={
        Property(name="States27", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_State", type=Offer_offeredTokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityNode_running_States28: BinaryAssociation = BinaryAssociation(
    name="activityNode_running_States28",
    ends={
        Property(name="States29", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_running_State", type=ActivityNode_running_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityNode_heldTokens_States30: BinaryAssociation = BinaryAssociation(
    name="activityNode_heldTokens_States30",
    ends={
        Property(name="States31", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_heldTokens_State", type=ActivityNode_heldTokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
activity_trace_States32: BinaryAssociation = BinaryAssociation(
    name="activity_trace_States32",
    ends={
        Property(name="States33", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity_trace_State", type=Activity_trace_State, multiplicity=Multiplicity(0, 9999))
    }
)
trace_executedNodes_States34: BinaryAssociation = BinaryAssociation(
    name="trace_executedNodes_States34",
    ends={
        Property(name="States35", type=trace_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_executedNodes_State", type=Trace_executedNodes_State, multiplicity=Multiplicity(0, 9999))
    }
)
pool_BooleanBinaryExpressions36: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanBinaryExpressions36",
    ends={
        Property(name="trace_BooleanBinaryExpression", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools37", type=trace_BooleanBinaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_StringValues38: BinaryAssociation = BinaryAssociation(
    name="pool_StringValues38",
    ends={
        Property(name="trace_StringValue", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools39", type=trace_StringValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerValues40: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerValues40",
    ends={
        Property(name="trace_IntegerValue", type=trace_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_StaticObjectsPools41", type=trace_IntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_selectNextNodeEntryEventOccurrence_Trace74: BinaryAssociation = BinaryAssociation(
    name="Activity_selectNextNodeEntryEventOccurrence_Trace74",
    ends={
        Property(name="Activity_selectNextNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events75", type=Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_selectNextNodeExitEventOccurrence_Trace76: BinaryAssociation = BinaryAssociation(
    name="Activity_selectNextNodeExitEventOccurrence_Trace76",
    ends={
        Property(name="Activity_selectNextNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events77", type=Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_terminateEntryEventOccurrence_Trace78: BinaryAssociation = BinaryAssociation(
    name="Activity_terminateEntryEventOccurrence_Trace78",
    ends={
        Property(name="Activity_terminateEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events79", type=Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_terminateExitEventOccurrence_Trace80: BinaryAssociation = BinaryAssociation(
    name="Activity_terminateExitEventOccurrence_Trace80",
    ends={
        Property(name="Activity_terminateExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events81", type=Activity_terminateExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getInitialNodeEntryEventOccurrence_Trace82: BinaryAssociation = BinaryAssociation(
    name="Activity_getInitialNodeEntryEventOccurrence_Trace82",
    ends={
        Property(name="Activity_getInitialNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events83", type=Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getInitialNodeExitEventOccurrence_Trace84: BinaryAssociation = BinaryAssociation(
    name="Activity_getInitialNodeExitEventOccurrence_Trace84",
    ends={
        Property(name="Activity_getInitialNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events85", type=Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireNodeEntryEventOccurrence_Trace86: BinaryAssociation = BinaryAssociation(
    name="Activity_fireNodeEntryEventOccurrence_Trace86",
    ends={
        Property(name="Activity_fireNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events87", type=Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireNodeExitEventOccurrence_Trace88: BinaryAssociation = BinaryAssociation(
    name="Activity_fireNodeExitEventOccurrence_Trace88",
    ends={
        Property(name="Activity_fireNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events89", type=Activity_fireNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_run_activityNodeEntryEventOccurrence_Trace90: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_run_activityNodeEntryEventOccurrence_Trace90",
    ends={
        Property(name="ActivityNode_run_activityNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events91", type=ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runEntryEventOccurrence_Trace58: BinaryAssociation = BinaryAssociation(
    name="Activity_runEntryEventOccurrence_Trace58",
    ends={
        Property(name="Activity_runEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events59", type=Activity_runEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runExitEventOccurrence_Trace60: BinaryAssociation = BinaryAssociation(
    name="Activity_runExitEventOccurrence_Trace60",
    ends={
        Property(name="Activity_runExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events61", type=Activity_runExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runNodesEntryEventOccurrence_Trace62: BinaryAssociation = BinaryAssociation(
    name="Activity_runNodesEntryEventOccurrence_Trace62",
    ends={
        Property(name="Activity_runNodesEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events63", type=Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runNodesExitEventOccurrence_Trace64: BinaryAssociation = BinaryAssociation(
    name="Activity_runNodesExitEventOccurrence_Trace64",
    ends={
        Property(name="Activity_runNodesExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events65", type=Activity_runNodesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireInitialNodeEntryEventOccurrence_Trace66: BinaryAssociation = BinaryAssociation(
    name="Activity_fireInitialNodeEntryEventOccurrence_Trace66",
    ends={
        Property(name="Activity_fireInitialNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events67", type=Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireInitialNodeExitEventOccurrence_Trace68: BinaryAssociation = BinaryAssociation(
    name="Activity_fireInitialNodeExitEventOccurrence_Trace68",
    ends={
        Property(name="Activity_fireInitialNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events69", type=Activity_fireInitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getEnabledNodesEntryEventOccurrence_Trace70: BinaryAssociation = BinaryAssociation(
    name="Activity_getEnabledNodesEntryEventOccurrence_Trace70",
    ends={
        Property(name="Activity_getEnabledNodesEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events71", type=Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getEnabledNodesExitEventOccurrence_Trace72: BinaryAssociation = BinaryAssociation(
    name="Activity_getEnabledNodesExitEventOccurrence_Trace72",
    ends={
        Property(name="Activity_getEnabledNodesExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events73", type=Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_sendOffersEntryEventOccurrence_Trace102: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_sendOffersEntryEventOccurrence_Trace102",
    ends={
        Property(name="ActivityNode_sendOffersEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events103", type=ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_sendOffersExitEventOccurrence_Trace104: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_sendOffersExitEventOccurrence_Trace104",
    ends={
        Property(name="ActivityNode_sendOffersExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events105", type=ActivityNode_sendOffersExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106",
    ends={
        Property(name="ActivityNode_takeOfferedTokensEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events107", type=ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_run_activityNodeExitEventOccurrence_Trace92: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_run_activityNodeExitEventOccurrence_Trace92",
    ends={
        Property(name="ActivityNode_run_activityNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events93", type=ActivityNode_run_activityNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isRunningEntryEventOccurrence_Trace94: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isRunningEntryEventOccurrence_Trace94",
    ends={
        Property(name="ActivityNode_isRunningEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events95", type=ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isRunningExitEventOccurrence_Trace96: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isRunningExitEventOccurrence_Trace96",
    ends={
        Property(name="ActivityNode_isRunningExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events97", type=ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98",
    ends={
        Property(name="ActivityNode_terminate_activityNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events99", type=ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100",
    ends={
        Property(name="ActivityNode_terminate_activityNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events101", type=ActivityNode_terminate_activityNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_hasOffersEntryEventOccurrence_Trace118: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_hasOffersEntryEventOccurrence_Trace118",
    ends={
        Property(name="ActivityNode_hasOffersEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events119", type=ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_hasOffersExitEventOccurrence_Trace120: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_hasOffersExitEventOccurrence_Trace120",
    ends={
        Property(name="ActivityNode_hasOffersExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events121", type=ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isReadyEntryEventOccurrence_Trace122: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isReadyEntryEventOccurrence_Trace122",
    ends={
        Property(name="ActivityNode_isReadyEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events123", type=ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isReadyExitEventOccurrence_Trace124: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isReadyExitEventOccurrence_Trace124",
    ends={
        Property(name="ActivityNode_isReadyExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events125", type=ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_sendOfferEntryEventOccurrence_Trace126: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_sendOfferEntryEventOccurrence_Trace126",
    ends={
        Property(name="ActivityEdge_sendOfferEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events127", type=ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_sendOfferExitEventOccurrence_Trace128: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_sendOfferExitEventOccurrence_Trace128",
    ends={
        Property(name="ActivityEdge_sendOfferExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events129", type=ActivityEdge_sendOfferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108",
    ends={
        Property(name="ActivityNode_takeOfferedTokensExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events109", type=ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_addTokensEntryEventOccurrence_Trace110: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_addTokensEntryEventOccurrence_Trace110",
    ends={
        Property(name="ActivityNode_addTokensEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events111", type=ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_addTokensExitEventOccurrence_Trace112: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_addTokensExitEventOccurrence_Trace112",
    ends={
        Property(name="ActivityNode_addTokensExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events113", type=ActivityNode_addTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_removeTokenEntryEventOccurrence_Trace114: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_removeTokenEntryEventOccurrence_Trace114",
    ends={
        Property(name="ActivityNode_removeTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events115", type=ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_removeTokenExitEventOccurrence_Trace116: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_removeTokenExitEventOccurrence_Trace116",
    ends={
        Property(name="ActivityNode_removeTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events117", type=ActivityNode_removeTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140: BinaryAssociation = BinaryAssociation(
    name="ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140",
    ends={
        Property(name="ControlNode_isReady_ControlNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events141", type=ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_fire_controlNodeEntryEventOccurrence_Trace142: BinaryAssociation = BinaryAssociation(
    name="ControlNode_fire_controlNodeEntryEventOccurrence_Trace142",
    ends={
        Property(name="ControlNode_fire_controlNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events143", type=ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_fire_controlNodeExitEventOccurrence_Trace144: BinaryAssociation = BinaryAssociation(
    name="ControlNode_fire_controlNodeExitEventOccurrence_Trace144",
    ends={
        Property(name="ControlNode_fire_controlNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events145", type=ControlNode_fire_controlNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_sendOffers_actionEntryEventOccurrence_Trace146: BinaryAssociation = BinaryAssociation(
    name="Action_sendOffers_actionEntryEventOccurrence_Trace146",
    ends={
        Property(name="Action_sendOffers_actionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events147", type=Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_sendOffers_actionExitEventOccurrence_Trace148: BinaryAssociation = BinaryAssociation(
    name="Action_sendOffers_actionExitEventOccurrence_Trace148",
    ends={
        Property(name="Action_sendOffers_actionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events149", type=Action_sendOffers_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_isReady_actionEntryEventOccurrence_Trace150: BinaryAssociation = BinaryAssociation(
    name="Action_isReady_actionEntryEventOccurrence_Trace150",
    ends={
        Property(name="Action_isReady_actionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events151", type=Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events131", type=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events133", type=ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_hasOfferEntryEventOccurrence_Trace134: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_hasOfferEntryEventOccurrence_Trace134",
    ends={
        Property(name="ActivityEdge_hasOfferEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events135", type=ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_hasOfferExitEventOccurrence_Trace136: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_hasOfferExitEventOccurrence_Trace136",
    ends={
        Property(name="ActivityEdge_hasOfferExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events137", type=ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138: BinaryAssociation = BinaryAssociation(
    name="ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138",
    ends={
        Property(name="ControlNode_isReady_ControlNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events139", type=ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162: BinaryAssociation = BinaryAssociation(
    name="InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162",
    ends={
        Property(name="InitialNode_isReady_InitialNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events163", type=InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164: BinaryAssociation = BinaryAssociation(
    name="InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164",
    ends={
        Property(name="InitialNode_isReady_InitialNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events165", type=InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_fire_initialNodeEntryEventOccurrence_Trace166: BinaryAssociation = BinaryAssociation(
    name="InitialNode_fire_initialNodeEntryEventOccurrence_Trace166",
    ends={
        Property(name="InitialNode_fire_initialNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events167", type=InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_fire_initialNodeExitEventOccurrence_Trace168: BinaryAssociation = BinaryAssociation(
    name="InitialNode_fire_initialNodeExitEventOccurrence_Trace168",
    ends={
        Property(name="InitialNode_fire_initialNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events169", type=InitialNode_fire_initialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170: BinaryAssociation = BinaryAssociation(
    name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events171", type=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172: BinaryAssociation = BinaryAssociation(
    name="ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events173", type=ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_isReady_actionExitEventOccurrence_Trace152: BinaryAssociation = BinaryAssociation(
    name="Action_isReady_actionExitEventOccurrence_Trace152",
    ends={
        Property(name="Action_isReady_actionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events153", type=Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_fire_actionEntryEventOccurrence_Trace154: BinaryAssociation = BinaryAssociation(
    name="Action_fire_actionEntryEventOccurrence_Trace154",
    ends={
        Property(name="Action_fire_actionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events155", type=Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_fire_actionExitEventOccurrence_Trace156: BinaryAssociation = BinaryAssociation(
    name="Action_fire_actionExitEventOccurrence_Trace156",
    ends={
        Property(name="Action_fire_actionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events157", type=Action_fire_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158: BinaryAssociation = BinaryAssociation(
    name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events159", type=OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160: BinaryAssociation = BinaryAssociation(
    name="OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events161", type=OpaqueAction_doAction_opaqueActionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184: BinaryAssociation = BinaryAssociation(
    name="DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184",
    ends={
        Property(name="DecisionNode_fire_decisionNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events185", type=DecisionNode_fire_decisionNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events187", type=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events189", type=IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events191", type=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events193", type=IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194: BinaryAssociation = BinaryAssociation(
    name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events195", type=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkNode_fire_forkNodeEntryEventOccurrence_Trace174: BinaryAssociation = BinaryAssociation(
    name="ForkNode_fire_forkNodeEntryEventOccurrence_Trace174",
    ends={
        Property(name="ForkNode_fire_forkNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events175", type=ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkNode_fire_forkNodeExitEventOccurrence_Trace176: BinaryAssociation = BinaryAssociation(
    name="ForkNode_fire_forkNodeExitEventOccurrence_Trace176",
    ends={
        Property(name="ForkNode_fire_forkNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events177", type=ForkNode_fire_forkNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178: BinaryAssociation = BinaryAssociation(
    name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events179", type=MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180: BinaryAssociation = BinaryAssociation(
    name="MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events181", type=MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182: BinaryAssociation = BinaryAssociation(
    name="DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182",
    ends={
        Property(name="DecisionNode_fire_decisionNodeEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events183", type=DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events207", type=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events209", type=BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210: BinaryAssociation = BinaryAssociation(
    name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events211", type=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212: BinaryAssociation = BinaryAssociation(
    name="IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events213", type=IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events215", type=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196: BinaryAssociation = BinaryAssociation(
    name="StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events197", type=StringVariable_setCurrentValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198: BinaryAssociation = BinaryAssociation(
    name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events199", type=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200: BinaryAssociation = BinaryAssociation(
    name="StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events201", type=StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events203", type=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events205", type=BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events227", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events229", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events231", type=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events233", type=IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events235", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events217", type=IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events219", type=IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events221", type=IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events223", type=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events225", type=IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events245", type=IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events247", type=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATERExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events249", type=IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events251", type=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events253", type=BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events237", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events239", type=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events241", type=IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events243", type=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events263", type=BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events265", type=BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266",
    ends={
        Property(name="BooleanBinaryExpression_evaluateOREntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events267", type=BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268",
    ends={
        Property(name="BooleanBinaryExpression_evaluateORExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events269", type=BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events255", type=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events257", type=BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events259", type=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events261", type=BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_withdrawEntryEventOccurrence_Trace278: BinaryAssociation = BinaryAssociation(
    name="Token_withdrawEntryEventOccurrence_Trace278",
    ends={
        Property(name="Token_withdrawEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events279", type=Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_withdrawExitEventOccurrence_Trace280: BinaryAssociation = BinaryAssociation(
    name="Token_withdrawExitEventOccurrence_Trace280",
    ends={
        Property(name="Token_withdrawExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events281", type=Token_withdrawExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282: BinaryAssociation = BinaryAssociation(
    name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events283", type=ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284: BinaryAssociation = BinaryAssociation(
    name="ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events285", type=ForkedToken_withdraw_forkedTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Offer_hasTokensEntryEventOccurrence_Trace286: BinaryAssociation = BinaryAssociation(
    name="Offer_hasTokensEntryEventOccurrence_Trace286",
    ends={
        Property(name="Offer_hasTokensEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events287", type=Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_isWithdrawnEntryEventOccurrence_Trace270: BinaryAssociation = BinaryAssociation(
    name="Token_isWithdrawnEntryEventOccurrence_Trace270",
    ends={
        Property(name="Token_isWithdrawnEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events271", type=Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_isWithdrawnExitEventOccurrence_Trace272: BinaryAssociation = BinaryAssociation(
    name="Token_isWithdrawnExitEventOccurrence_Trace272",
    ends={
        Property(name="Token_isWithdrawnExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events273", type=Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_transferEntryEventOccurrence_Trace274: BinaryAssociation = BinaryAssociation(
    name="Token_transferEntryEventOccurrence_Trace274",
    ends={
        Property(name="Token_transferEntryEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events275", type=Token_transferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_transferExitEventOccurrence_Trace276: BinaryAssociation = BinaryAssociation(
    name="Token_transferExitEventOccurrence_Trace276",
    ends={
        Property(name="Token_transferExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events277", type=Token_transferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam295: BinaryAssociation = BinaryAssociation(
    name="thisParam295",
    ends={
        Property(name="activitydiagram_TracedActivity296", type=trace_Events_Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_initializeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inputValuesParam297: BinaryAssociation = BinaryAssociation(
    name="inputValuesParam297",
    ends={
        Property(name="Events_trace_EObject299", type=trace_Events_Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_initializeEntryEventOccurrence298", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent300: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent300",
    ends={
        Property(name="Activity_initializeEntryEventOccurrence301", type=trace_Events_Activity_initializeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_initializeExitEventOccurrence", type=Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam302: BinaryAssociation = BinaryAssociation(
    name="thisParam302",
    ends={
        Property(name="activitydiagram_TracedActivity303", type=trace_Events_Activity_runEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_runEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent304: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent304",
    ends={
        Property(name="Activity_runEntryEventOccurrence305", type=trace_Events_Activity_runExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_runExitEventOccurrence", type=Activity_runEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam306: BinaryAssociation = BinaryAssociation(
    name="thisParam306",
    ends={
        Property(name="activitydiagram_TracedActivity307", type=trace_Events_Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_runNodesEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent308: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent308",
    ends={
        Property(name="Activity_runNodesEntryEventOccurrence309", type=trace_Events_Activity_runNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_runNodesExitEventOccurrence", type=Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
Offer_hasTokensExitEventOccurrence_Trace288: BinaryAssociation = BinaryAssociation(
    name="Offer_hasTokensExitEventOccurrence_Trace288",
    ends={
        Property(name="Offer_hasTokensExitEventOccurrence", type=trace_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Events289", type=Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam290: BinaryAssociation = BinaryAssociation(
    name="thisParam290",
    ends={
        Property(name="activitydiagram_TracedActivity", type=trace_Events_Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_mainEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inputValuesParam291: BinaryAssociation = BinaryAssociation(
    name="inputValuesParam291",
    ends={
        Property(name="Events_trace_EObject", type=trace_Events_Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_mainEntryEventOccurrence292", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent293: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent293",
    ends={
        Property(name="Activity_mainEntryEventOccurrence294", type=trace_Events_Activity_mainExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_mainExitEventOccurrence", type=Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam321: BinaryAssociation = BinaryAssociation(
    name="thisParam321",
    ends={
        Property(name="activitydiagram_TracedActivity322", type=trace_Events_Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_selectNextNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
activityNodesParam323: BinaryAssociation = BinaryAssociation(
    name="activityNodesParam323",
    ends={
        Property(name="Events_trace_EObject325", type=trace_Events_Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_selectNextNodeEntryEventOccurrence324", type=Events_trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent326: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent326",
    ends={
        Property(name="Activity_selectNextNodeEntryEventOccurrence327", type=trace_Events_Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_selectNextNodeExitEventOccurrence", type=Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
selectedNodeReturn328: BinaryAssociation = BinaryAssociation(
    name="selectedNodeReturn328",
    ends={
        Property(name="Events_trace_EObject330", type=trace_Events_Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_selectNextNodeExitEventOccurrence329", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam331: BinaryAssociation = BinaryAssociation(
    name="thisParam331",
    ends={
        Property(name="activitydiagram_TracedActivity332", type=trace_Events_Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_terminateEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent333: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent333",
    ends={
        Property(name="Activity_terminateEntryEventOccurrence334", type=trace_Events_Activity_terminateExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_terminateExitEventOccurrence", type=Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam335: BinaryAssociation = BinaryAssociation(
    name="thisParam335",
    ends={
        Property(name="activitydiagram_TracedActivity336", type=trace_Events_Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getInitialNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
thisParam310: BinaryAssociation = BinaryAssociation(
    name="thisParam310",
    ends={
        Property(name="activitydiagram_TracedActivity311", type=trace_Events_Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_fireInitialNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent312: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent312",
    ends={
        Property(name="Activity_fireInitialNodeEntryEventOccurrence313", type=trace_Events_Activity_fireInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_fireInitialNodeExitEventOccurrence", type=Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam314: BinaryAssociation = BinaryAssociation(
    name="thisParam314",
    ends={
        Property(name="activitydiagram_TracedActivity315", type=trace_Events_Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getEnabledNodesEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent316: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent316",
    ends={
        Property(name="Activity_getEnabledNodesEntryEventOccurrence317", type=trace_Events_Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getEnabledNodesExitEventOccurrence", type=Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
enabledNodesReturn318: BinaryAssociation = BinaryAssociation(
    name="enabledNodesReturn318",
    ends={
        Property(name="Events_trace_EObject320", type=trace_Events_Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getEnabledNodesExitEventOccurrence319", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent350: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent350",
    ends={
        Property(name="ActivityNode_run_activityNodeEntryEventOccurrence351", type=trace_Events_ActivityNode_run_activityNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_run_activityNodeExitEventOccurrence", type=ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam352: BinaryAssociation = BinaryAssociation(
    name="thisParam352",
    ends={
        Property(name="activitydiagram_TracedActivityNode353", type=trace_Events_ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isRunningEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent354: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent354",
    ends={
        Property(name="ActivityNode_isRunningEntryEventOccurrence355", type=trace_Events_ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isRunningExitEventOccurrence", type=ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isRunningReturn356: BinaryAssociation = BinaryAssociation(
    name="isRunningReturn356",
    ends={
        Property(name="Events_trace_EObject358", type=trace_Events_ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isRunningExitEventOccurrence357", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam359: BinaryAssociation = BinaryAssociation(
    name="thisParam359",
    ends={
        Property(name="activitydiagram_TracedActivityNode360", type=trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent361: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent361",
    ends={
        Property(name="ActivityNode_terminate_activityNodeEntryEventOccurrence362", type=trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence", type=ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam363: BinaryAssociation = BinaryAssociation(
    name="thisParam363",
    ends={
        Property(name="activitydiagram_TracedActivityNode364", type=trace_Events_ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_sendOffersEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent337: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent337",
    ends={
        Property(name="Activity_getInitialNodeEntryEventOccurrence338", type=trace_Events_Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getInitialNodeExitEventOccurrence", type=Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
initialNodeReturn339: BinaryAssociation = BinaryAssociation(
    name="initialNodeReturn339",
    ends={
        Property(name="Events_trace_EObject341", type=trace_Events_Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_getInitialNodeExitEventOccurrence340", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam342: BinaryAssociation = BinaryAssociation(
    name="thisParam342",
    ends={
        Property(name="activitydiagram_TracedActivity343", type=trace_Events_Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_fireNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
nodeParam344: BinaryAssociation = BinaryAssociation(
    name="nodeParam344",
    ends={
        Property(name="Events_trace_EObject346", type=trace_Events_Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_fireNodeEntryEventOccurrence345", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent347: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent347",
    ends={
        Property(name="Activity_fireNodeEntryEventOccurrence348", type=trace_Events_Activity_fireNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Activity_fireNodeExitEventOccurrence", type=Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam349: BinaryAssociation = BinaryAssociation(
    name="thisParam349",
    ends={
        Property(name="activitydiagram_TracedActivityNode", type=trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam379: BinaryAssociation = BinaryAssociation(
    name="tokensParam379",
    ends={
        Property(name="Events_trace_EObject381", type=trace_Events_ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_addTokensEntryEventOccurrence380", type=Events_trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent382: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent382",
    ends={
        Property(name="ActivityNode_addTokensEntryEventOccurrence383", type=trace_Events_ActivityNode_addTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_addTokensExitEventOccurrence", type=ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam384: BinaryAssociation = BinaryAssociation(
    name="thisParam384",
    ends={
        Property(name="activitydiagram_TracedActivityNode385", type=trace_Events_ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_removeTokenEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
tokenParam386: BinaryAssociation = BinaryAssociation(
    name="tokenParam386",
    ends={
        Property(name="Events_trace_EObject388", type=trace_Events_ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_removeTokenEntryEventOccurrence387", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent389: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent389",
    ends={
        Property(name="ActivityNode_removeTokenEntryEventOccurrence390", type=trace_Events_ActivityNode_removeTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_removeTokenExitEventOccurrence", type=ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam365: BinaryAssociation = BinaryAssociation(
    name="tokensParam365",
    ends={
        Property(name="Events_trace_EObject367", type=trace_Events_ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_sendOffersEntryEventOccurrence366", type=Events_trace_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent368: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent368",
    ends={
        Property(name="ActivityNode_sendOffersEntryEventOccurrence369", type=trace_Events_ActivityNode_sendOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_sendOffersExitEventOccurrence", type=ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam370: BinaryAssociation = BinaryAssociation(
    name="thisParam370",
    ends={
        Property(name="activitydiagram_TracedActivityNode371", type=trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent372: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent372",
    ends={
        Property(name="ActivityNode_takeOfferedTokensEntryEventOccurrence373", type=trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence", type=ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensReturn374: BinaryAssociation = BinaryAssociation(
    name="tokensReturn374",
    ends={
        Property(name="Events_trace_EObject376", type=trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence375", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam377: BinaryAssociation = BinaryAssociation(
    name="thisParam377",
    ends={
        Property(name="activitydiagram_TracedActivityNode378", type=trace_Events_ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_addTokensEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
thisParam405: BinaryAssociation = BinaryAssociation(
    name="thisParam405",
    ends={
        Property(name="activitydiagram_TracedActivityEdge", type=trace_Events_ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_sendOfferEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam406: BinaryAssociation = BinaryAssociation(
    name="tokensParam406",
    ends={
        Property(name="Events_trace_EObject408", type=trace_Events_ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_sendOfferEntryEventOccurrence407", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent409: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent409",
    ends={
        Property(name="ActivityEdge_sendOfferEntryEventOccurrence410", type=trace_Events_ActivityEdge_sendOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_sendOfferExitEventOccurrence", type=ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam411: BinaryAssociation = BinaryAssociation(
    name="thisParam411",
    ends={
        Property(name="activitydiagram_TracedActivityEdge412", type=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent413: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent413",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence414", type=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence", type=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensReturn415: BinaryAssociation = BinaryAssociation(
    name="tokensReturn415",
    ends={
        Property(name="Events_trace_EObject417", type=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence416", type=Events_trace_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam418: BinaryAssociation = BinaryAssociation(
    name="thisParam418",
    ends={
        Property(name="activitydiagram_TracedActivityEdge419", type=trace_Events_ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_hasOfferEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
thisParam391: BinaryAssociation = BinaryAssociation(
    name="thisParam391",
    ends={
        Property(name="activitydiagram_TracedActivityNode392", type=trace_Events_ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_hasOffersEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent393: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent393",
    ends={
        Property(name="ActivityNode_hasOffersEntryEventOccurrence394", type=trace_Events_ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_hasOffersExitEventOccurrence", type=ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn395: BinaryAssociation = BinaryAssociation(
    name="returnReturn395",
    ends={
        Property(name="Events_trace_EObject397", type=trace_Events_ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_hasOffersExitEventOccurrence396", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam398: BinaryAssociation = BinaryAssociation(
    name="thisParam398",
    ends={
        Property(name="activitydiagram_TracedActivityNode399", type=trace_Events_ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isReadyEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent400: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent400",
    ends={
        Property(name="ActivityNode_isReadyEntryEventOccurrence401", type=trace_Events_ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isReadyExitEventOccurrence", type=ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn402: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn402",
    ends={
        Property(name="Events_trace_EObject404", type=trace_Events_ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityNode_isReadyExitEventOccurrence403", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam431: BinaryAssociation = BinaryAssociation(
    name="thisParam431",
    ends={
        Property(name="trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence", type=activitydiagram_TracedControlNode, multiplicity=Multiplicity(0, 1)),
        Property(name="activitydiagram_TracedControlNode432", type=trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1))
    }
)
tokensParam433: BinaryAssociation = BinaryAssociation(
    name="tokensParam433",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken", type=trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence434", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent435: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent435",
    ends={
        Property(name="ControlNode_fire_controlNodeEntryEventOccurrence436", type=trace_Events_ControlNode_fire_controlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ControlNode_fire_controlNodeExitEventOccurrence", type=ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam437: BinaryAssociation = BinaryAssociation(
    name="thisParam437",
    ends={
        Property(name="activitydiagram_TracedAction", type=trace_Events_Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_sendOffers_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent438: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent438",
    ends={
        Property(name="Action_sendOffers_actionEntryEventOccurrence439", type=trace_Events_Action_sendOffers_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_sendOffers_actionExitEventOccurrence", type=Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam440: BinaryAssociation = BinaryAssociation(
    name="thisParam440",
    ends={
        Property(name="activitydiagram_TracedAction441", type=trace_Events_Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_isReady_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent442: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent442",
    ends={
        Property(name="Action_isReady_actionEntryEventOccurrence443", type=trace_Events_Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_isReady_actionExitEventOccurrence", type=Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent420: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent420",
    ends={
        Property(name="ActivityEdge_hasOfferEntryEventOccurrence421", type=trace_Events_ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_hasOfferExitEventOccurrence", type=ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
hasOfferReturn422: BinaryAssociation = BinaryAssociation(
    name="hasOfferReturn422",
    ends={
        Property(name="Events_trace_EObject424", type=trace_Events_ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityEdge_hasOfferExitEventOccurrence423", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam425: BinaryAssociation = BinaryAssociation(
    name="thisParam425",
    ends={
        Property(name="activitydiagram_TracedControlNode", type=trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence", type=activitydiagram_TracedControlNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent426: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent426",
    ends={
        Property(name="ControlNode_isReady_ControlNodeEntryEventOccurrence427", type=trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence", type=ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn428: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn428",
    ends={
        Property(name="Events_trace_EObject430", type=trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence429", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent455: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent455",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence456", type=trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence", type=OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam457: BinaryAssociation = BinaryAssociation(
    name="thisParam457",
    ends={
        Property(name="activitydiagram_TracedInitialNode", type=trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent458: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent458",
    ends={
        Property(name="InitialNode_isReady_InitialNodeEntryEventOccurrence459", type=trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence", type=InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn460: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn460",
    ends={
        Property(name="Events_trace_EObject462", type=trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence461", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam463: BinaryAssociation = BinaryAssociation(
    name="thisParam463",
    ends={
        Property(name="activitydiagram_TracedInitialNode464", type=trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam465: BinaryAssociation = BinaryAssociation(
    name="tokensParam465",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken467", type=trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence466", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent468: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent468",
    ends={
        Property(name="InitialNode_fire_initialNodeEntryEventOccurrence469", type=trace_Events_InitialNode_fire_initialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_InitialNode_fire_initialNodeExitEventOccurrence", type=InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn444: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn444",
    ends={
        Property(name="Events_trace_EObject446", type=trace_Events_Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_isReady_actionExitEventOccurrence445", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam447: BinaryAssociation = BinaryAssociation(
    name="thisParam447",
    ends={
        Property(name="activitydiagram_TracedAction448", type=trace_Events_Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_fire_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam449: BinaryAssociation = BinaryAssociation(
    name="tokensParam449",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken451", type=trace_Events_Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_fire_actionEntryEventOccurrence450", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent452: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent452",
    ends={
        Property(name="Action_fire_actionEntryEventOccurrence453", type=trace_Events_Action_fire_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Action_fire_actionExitEventOccurrence", type=Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam454: BinaryAssociation = BinaryAssociation(
    name="thisParam454",
    ends={
        Property(name="activitydiagram_TracedOpaqueAction", type=trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence", type=activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent480: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent480",
    ends={
        Property(name="ForkNode_fire_forkNodeEntryEventOccurrence481", type=trace_Events_ForkNode_fire_forkNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ForkNode_fire_forkNodeExitEventOccurrence", type=ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam482: BinaryAssociation = BinaryAssociation(
    name="thisParam482",
    ends={
        Property(name="activitydiagram_TracedMergeNode", type=trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence", type=activitydiagram_TracedMergeNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent483: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent483",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence484", type=trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence", type=MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn485: BinaryAssociation = BinaryAssociation(
    name="returnReturn485",
    ends={
        Property(name="Events_trace_EObject487", type=trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence486", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam488: BinaryAssociation = BinaryAssociation(
    name="thisParam488",
    ends={
        Property(name="activitydiagram_TracedDecisionNode", type=trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence", type=activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam489: BinaryAssociation = BinaryAssociation(
    name="tokensParam489",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken491", type=trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence490", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam470: BinaryAssociation = BinaryAssociation(
    name="thisParam470",
    ends={
        Property(name="activitydiagram_TracedActivityFinalNode", type=trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence", type=activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam471: BinaryAssociation = BinaryAssociation(
    name="tokensParam471",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken473", type=trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence472", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent474: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent474",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence475", type=trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence", type=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam476: BinaryAssociation = BinaryAssociation(
    name="thisParam476",
    ends={
        Property(name="activitydiagram_TracedForkNode", type=trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence", type=activitydiagram_TracedForkNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam477: BinaryAssociation = BinaryAssociation(
    name="tokensParam477",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken479", type=trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence478", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
valueReturn503: BinaryAssociation = BinaryAssociation(
    name="valueReturn503",
    ends={
        Property(name="Events_trace_EObject505", type=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence504", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam506: BinaryAssociation = BinaryAssociation(
    name="thisParam506",
    ends={
        Property(name="activitydiagram_TracedStringVariable", type=trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 1))
    }
)
valueParam507: BinaryAssociation = BinaryAssociation(
    name="valueParam507",
    ends={
        Property(name="Events_trace_Value509", type=trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence508", type=Events_trace_Value, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent510: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent510",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence511", type=trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence", type=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam512: BinaryAssociation = BinaryAssociation(
    name="thisParam512",
    ends={
        Property(name="activitydiagram_TracedStringVariable513", type=trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent492: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent492",
    ends={
        Property(name="DecisionNode_fire_decisionNodeEntryEventOccurrence493", type=trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence", type=DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam494: BinaryAssociation = BinaryAssociation(
    name="thisParam494",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable", type=trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
valueParam495: BinaryAssociation = BinaryAssociation(
    name="valueParam495",
    ends={
        Property(name="Events_trace_Value", type=trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence496", type=Events_trace_Value, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent497: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent497",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence498", type=trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence", type=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam499: BinaryAssociation = BinaryAssociation(
    name="thisParam499",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable500", type=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent501: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent501",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence502", type=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence", type=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
valueParam520: BinaryAssociation = BinaryAssociation(
    name="valueParam520",
    ends={
        Property(name="Events_trace_Value522", type=trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence521", type=Events_trace_Value, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent523: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent523",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence524", type=trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence", type=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam525: BinaryAssociation = BinaryAssociation(
    name="thisParam525",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable526", type=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent527: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent527",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence528", type=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence", type=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
valueReturn529: BinaryAssociation = BinaryAssociation(
    name="valueReturn529",
    ends={
        Property(name="Events_trace_EObject531", type=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence530", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam532: BinaryAssociation = BinaryAssociation(
    name="thisParam532",
    ends={
        Property(name="Events_trace_IntegerExpression", type=trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence", type=Events_trace_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent514: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent514",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence515", type=trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence", type=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
valueReturn516: BinaryAssociation = BinaryAssociation(
    name="valueReturn516",
    ends={
        Property(name="Events_trace_EObject518", type=trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence517", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam519: BinaryAssociation = BinaryAssociation(
    name="thisParam519",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable", type=trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
thisParam544: BinaryAssociation = BinaryAssociation(
    name="thisParam544",
    ends={
        Property(name="Events_trace_IntegerCalculationExpression545", type=trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence", type=Events_trace_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent546: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent546",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence547", type=trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence", type=IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn548: BinaryAssociation = BinaryAssociation(
    name="resultReturn548",
    ends={
        Property(name="Events_trace_EObject550", type=trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence549", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam551: BinaryAssociation = BinaryAssociation(
    name="thisParam551",
    ends={
        Property(name="Events_trace_IntegerCalculationExpression552", type=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence", type=Events_trace_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent553: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent553",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence554", type=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence", type=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn555: BinaryAssociation = BinaryAssociation(
    name="resultReturn555",
    ends={
        Property(name="Events_trace_EObject557", type=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence556", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent533: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent533",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence534", type=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence", type=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
operand1ValueReturn535: BinaryAssociation = BinaryAssociation(
    name="operand1ValueReturn535",
    ends={
        Property(name="Events_trace_EObject537", type=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence536", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
operand2ValueReturn538: BinaryAssociation = BinaryAssociation(
    name="operand2ValueReturn538",
    ends={
        Property(name="Events_trace_EObject540", type=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence539", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam541: BinaryAssociation = BinaryAssociation(
    name="thisParam541",
    ends={
        Property(name="Events_trace_IntegerCalculationExpression", type=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence", type=Events_trace_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent542: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent542",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence543", type=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence", type=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam568: BinaryAssociation = BinaryAssociation(
    name="thisParam568",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression569", type=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent570: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent570",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence571", type=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn572: BinaryAssociation = BinaryAssociation(
    name="resultReturn572",
    ends={
        Property(name="Events_trace_EObject574", type=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence573", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam575: BinaryAssociation = BinaryAssociation(
    name="thisParam575",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression576", type=trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent577: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent577",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence578", type=trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn579: BinaryAssociation = BinaryAssociation(
    name="resultReturn579",
    ends={
        Property(name="Events_trace_EObject581", type=trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence580", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam558: BinaryAssociation = BinaryAssociation(
    name="thisParam558",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression", type=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent559: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent559",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence560", type=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam561: BinaryAssociation = BinaryAssociation(
    name="thisParam561",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression562", type=trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent563: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent563",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence564", type=trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence", type=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn565: BinaryAssociation = BinaryAssociation(
    name="resultReturn565",
    ends={
        Property(name="Events_trace_EObject567", type=trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence566", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent591: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent591",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence592", type=trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence", type=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn593: BinaryAssociation = BinaryAssociation(
    name="resultReturn593",
    ends={
        Property(name="Events_trace_EObject595", type=trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence594", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam596: BinaryAssociation = BinaryAssociation(
    name="thisParam596",
    ends={
        Property(name="Events_trace_BooleanUnaryExpression", type=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence", type=Events_trace_BooleanUnaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent597: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent597",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence598", type=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence", type=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam599: BinaryAssociation = BinaryAssociation(
    name="thisParam599",
    ends={
        Property(name="Events_trace_BooleanUnaryExpression600", type=trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence", type=Events_trace_BooleanUnaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent601: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent601",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence602", type=trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence", type=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam582: BinaryAssociation = BinaryAssociation(
    name="thisParam582",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression583", type=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent584: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent584",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence585", type=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn586: BinaryAssociation = BinaryAssociation(
    name="resultReturn586",
    ends={
        Property(name="Events_trace_EObject588", type=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence587", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam589: BinaryAssociation = BinaryAssociation(
    name="thisParam589",
    ends={
        Property(name="Events_trace_IntegerComparisonExpression590", type=trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence", type=Events_trace_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent611: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent611",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence612", type=trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence", type=BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn613: BinaryAssociation = BinaryAssociation(
    name="resultReturn613",
    ends={
        Property(name="Events_trace_EObject615", type=trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence614", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam616: BinaryAssociation = BinaryAssociation(
    name="thisParam616",
    ends={
        Property(name="Events_trace_BooleanBinaryExpression617", type=trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence", type=Events_trace_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent618: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent618",
    ends={
        Property(name="BooleanBinaryExpression_evaluateOREntryEventOccurrence619", type=trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence", type=BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn620: BinaryAssociation = BinaryAssociation(
    name="resultReturn620",
    ends={
        Property(name="Events_trace_EObject622", type=trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence621", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam623: BinaryAssociation = BinaryAssociation(
    name="thisParam623",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken624", type=trace_Events_Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_isWithdrawnEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn603: BinaryAssociation = BinaryAssociation(
    name="resultReturn603",
    ends={
        Property(name="Events_trace_EObject605", type=trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence604", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam606: BinaryAssociation = BinaryAssociation(
    name="thisParam606",
    ends={
        Property(name="Events_trace_BooleanBinaryExpression", type=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence", type=Events_trace_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent607: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent607",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence608", type=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence", type=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam609: BinaryAssociation = BinaryAssociation(
    name="thisParam609",
    ends={
        Property(name="Events_trace_BooleanBinaryExpression610", type=trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence", type=Events_trace_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent635: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent635",
    ends={
        Property(name="Token_transferEntryEventOccurrence636", type=trace_Events_Token_transferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_transferExitEventOccurrence", type=Token_transferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
transferredTokenReturn637: BinaryAssociation = BinaryAssociation(
    name="transferredTokenReturn637",
    ends={
        Property(name="Events_trace_EObject639", type=trace_Events_Token_transferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_transferExitEventOccurrence638", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam640: BinaryAssociation = BinaryAssociation(
    name="thisParam640",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken641", type=trace_Events_Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_withdrawEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent642: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent642",
    ends={
        Property(name="Token_withdrawEntryEventOccurrence643", type=trace_Events_Token_withdrawExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_withdrawExitEventOccurrence", type=Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam644: BinaryAssociation = BinaryAssociation(
    name="thisParam644",
    ends={
        Property(name="activitydiagramConfiguration_TracedForkedToken", type=trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent625: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent625",
    ends={
        Property(name="Token_isWithdrawnEntryEventOccurrence626", type=trace_Events_Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_isWithdrawnExitEventOccurrence", type=Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isWithdrawnReturn627: BinaryAssociation = BinaryAssociation(
    name="isWithdrawnReturn627",
    ends={
        Property(name="Events_trace_EObject629", type=trace_Events_Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_isWithdrawnExitEventOccurrence628", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam630: BinaryAssociation = BinaryAssociation(
    name="thisParam630",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken631", type=trace_Events_Token_transferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_transferEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
holderParam632: BinaryAssociation = BinaryAssociation(
    name="holderParam632",
    ends={
        Property(name="Events_trace_EObject634", type=trace_Events_Token_transferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Token_transferEntryEventOccurrence633", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
value653: BinaryAssociation = BinaryAssociation(
    name="value653",
    ends={
        Property(name="trace_States_InputValue_value_State", type=States_trace_Value, multiplicity=Multiplicity(1, 1)),
        Property(name="States_trace_Value", type=trace_States_InputValue_value_State, multiplicity=Multiplicity(1, 1))
    }
)
parent654: BinaryAssociation = BinaryAssociation(
    name="parent654",
    ends={
        Property(name="Traced", type=trace_States_InputValue_value_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1))
    }
)
globalStates655: BinaryAssociation = BinaryAssociation(
    name="globalStates655",
    ends={
        Property(name="GlobalState656", type=trace_States_InputValue_value_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inputValue_value_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
variable657: BinaryAssociation = BinaryAssociation(
    name="variable657",
    ends={
        Property(name="activitydiagram_TracedVariable", type=trace_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_InputValue_variable_State", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
parent658: BinaryAssociation = BinaryAssociation(
    name="parent658",
    ends={
        Property(name="Traced660", type=trace_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration659", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1))
    }
)
globalStates661: BinaryAssociation = BinaryAssociation(
    name="globalStates661",
    ends={
        Property(name="GlobalState662", type=trace_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inputValue_variable_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
holder663: BinaryAssociation = BinaryAssociation(
    name="holder663",
    ends={
        Property(name="activitydiagram_TracedActivityNode664", type=trace_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Token_holder_State", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent645: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent645",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence646", type=trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence", type=ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam647: BinaryAssociation = BinaryAssociation(
    name="thisParam647",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer", type=trace_Events_Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Offer_hasTokensEntryEventOccurrence", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent648: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent648",
    ends={
        Property(name="Offer_hasTokensEntryEventOccurrence649", type=trace_Events_Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Offer_hasTokensExitEventOccurrence", type=Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
hasTokensReturn650: BinaryAssociation = BinaryAssociation(
    name="hasTokensReturn650",
    ends={
        Property(name="Events_trace_EObject652", type=trace_Events_Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Events_Offer_hasTokensExitEventOccurrence651", type=Events_trace_EObject, multiplicity=Multiplicity(1, 1))
    }
)
baseToken681: BinaryAssociation = BinaryAssociation(
    name="baseToken681",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken682", type=trace_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_ForkedToken_baseToken_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
parent683: BinaryAssociation = BinaryAssociation(
    name="parent683",
    ends={
        Property(name="Traced685", type=trace_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration684", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates686: BinaryAssociation = BinaryAssociation(
    name="globalStates686",
    ends={
        Property(name="GlobalState687", type=trace_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseToken_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent688: BinaryAssociation = BinaryAssociation(
    name="parent688",
    ends={
        Property(name="Traced690", type=trace_States_ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration689", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates691: BinaryAssociation = BinaryAssociation(
    name="globalStates691",
    ends={
        Property(name="GlobalState692", type=trace_States_ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseTokenIsWithdrawn_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
offers693: BinaryAssociation = BinaryAssociation(
    name="offers693",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer694", type=trace_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_ActivityEdge_offers_State", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 9999))
    }
)
parent695: BinaryAssociation = BinaryAssociation(
    name="parent695",
    ends={
        Property(name="Traced696", type=trace_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
parent665: BinaryAssociation = BinaryAssociation(
    name="parent665",
    ends={
        Property(name="Traced667", type=trace_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration666", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates668: BinaryAssociation = BinaryAssociation(
    name="globalStates668",
    ends={
        Property(name="GlobalState669", type=trace_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="token_holder_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
inputValues670: BinaryAssociation = BinaryAssociation(
    name="inputValues670",
    ends={
        Property(name="activitydiagramConfiguration_TracedInputValue", type=trace_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Input_inputValues_State", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent671: BinaryAssociation = BinaryAssociation(
    name="parent671",
    ends={
        Property(name="Traced673", type=trace_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration672", type=activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(1, 1))
    }
)
globalStates674: BinaryAssociation = BinaryAssociation(
    name="globalStates674",
    ends={
        Property(name="GlobalState675", type=trace_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="input_inputValues_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent676: BinaryAssociation = BinaryAssociation(
    name="parent676",
    ends={
        Property(name="Traced678", type=trace_States_ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration677", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates679: BinaryAssociation = BinaryAssociation(
    name="globalStates679",
    ends={
        Property(name="GlobalState680", type=trace_States_ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_remainingOffersCount_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
globalStates704: BinaryAssociation = BinaryAssociation(
    name="globalStates704",
    ends={
        Property(name="variable_currentValue_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999)),
        Property(name="GlobalState705", type=trace_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1))
    }
)
offeredTokens706: BinaryAssociation = BinaryAssociation(
    name="offeredTokens706",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken707", type=trace_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Offer_offeredTokens_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent708: BinaryAssociation = BinaryAssociation(
    name="parent708",
    ends={
        Property(name="Traced710", type=trace_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration709", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(1, 1))
    }
)
globalStates711: BinaryAssociation = BinaryAssociation(
    name="globalStates711",
    ends={
        Property(name="GlobalState712", type=trace_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="offer_offeredTokens_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
globalStates697: BinaryAssociation = BinaryAssociation(
    name="globalStates697",
    ends={
        Property(name="GlobalState698", type=trace_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdge_offers_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
currentValue699: BinaryAssociation = BinaryAssociation(
    name="currentValue699",
    ends={
        Property(name="States_trace_Value700", type=trace_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Variable_currentValue_State", type=States_trace_Value, multiplicity=Multiplicity(1, 1))
    }
)
parent701: BinaryAssociation = BinaryAssociation(
    name="parent701",
    ends={
        Property(name="Traced703", type=trace_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram702", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
heldTokens718: BinaryAssociation = BinaryAssociation(
    name="heldTokens718",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken719", type=trace_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_ActivityNode_heldTokens_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent720: BinaryAssociation = BinaryAssociation(
    name="parent720",
    ends={
        Property(name="Traced722", type=trace_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram721", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
globalStates723: BinaryAssociation = BinaryAssociation(
    name="globalStates723",
    ends={
        Property(name="GlobalState724", type=trace_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNode_heldTokens_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent713: BinaryAssociation = BinaryAssociation(
    name="parent713",
    ends={
        Property(name="Traced715", type=trace_States_ActivityNode_running_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram714", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
globalStates716: BinaryAssociation = BinaryAssociation(
    name="globalStates716",
    ends={
        Property(name="GlobalState717", type=trace_States_ActivityNode_running_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNode_running_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
activitydiagram_tracedControlFlows738: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedControlFlows738",
    ends={
        Property(name="activitydiagram_TracedControlFlow", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects", type=activitydiagram_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedInputValues739: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedInputValues739",
    ends={
        Property(name="activitydiagramConfiguration_TracedInputValue741", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects740", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedMergeNodes742: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedMergeNodes742",
    ends={
        Property(name="activitydiagram_TracedMergeNode744", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects743", type=activitydiagram_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedBooleanVariables745: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedBooleanVariables745",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable747", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects746", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedControlTokens748: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedControlTokens748",
    ends={
        Property(name="activitydiagramConfiguration_TracedControlToken", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects749", type=activitydiagramConfiguration_TracedControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedInputs750: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedInputs750",
    ends={
        Property(name="activitydiagramConfiguration_TracedInput", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects751", type=activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedIntegerVariables752: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedIntegerVariables752",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable754", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects753", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trace725: BinaryAssociation = BinaryAssociation(
    name="trace725",
    ends={
        Property(name="activitydiagramConfiguration_TracedTrace", type=trace_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Activity_trace_State", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1))
    }
)
parent726: BinaryAssociation = BinaryAssociation(
    name="parent726",
    ends={
        Property(name="Traced728", type=trace_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram727", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1))
    }
)
globalStates729: BinaryAssociation = BinaryAssociation(
    name="globalStates729",
    ends={
        Property(name="GlobalState730", type=trace_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_trace_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
executedNodes731: BinaryAssociation = BinaryAssociation(
    name="executedNodes731",
    ends={
        Property(name="activitydiagram_TracedActivityNode732", type=trace_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_States_Trace_executedNodes_State", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parent733: BinaryAssociation = BinaryAssociation(
    name="parent733",
    ends={
        Property(name="Traced735", type=trace_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration734", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1))
    }
)
globalStates736: BinaryAssociation = BinaryAssociation(
    name="globalStates736",
    ends={
        Property(name="GlobalState737", type=trace_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_executedNodes_States", type=States_trace_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
activitydiagram_tracedOpaqueActions776: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedOpaqueActions776",
    ends={
        Property(name="activitydiagram_TracedOpaqueAction778", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects777", type=activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedJoinNodes779: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedJoinNodes779",
    ends={
        Property(name="activitydiagram_TracedJoinNode", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects780", type=activitydiagram_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedDecisionNodes781: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedDecisionNodes781",
    ends={
        Property(name="activitydiagram_TracedDecisionNode783", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects782", type=activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedTraces784: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedTraces784",
    ends={
        Property(name="activitydiagramConfiguration_TracedTrace786", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects785", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard787: BinaryAssociation = BinaryAssociation(
    name="guard787",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable788", type=trace_activitydiagram_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedControlFlow", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
originalObject789: BinaryAssociation = BinaryAssociation(
    name="originalObject789",
    ends={
        Property(name="activitydiagram_trace_ControlFlow", type=trace_activitydiagram_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedControlFlow790", type=activitydiagram_trace_ControlFlow, multiplicity=Multiplicity(0, 1))
    }
)
originalObject791: BinaryAssociation = BinaryAssociation(
    name="originalObject791",
    ends={
        Property(name="activitydiagram_trace_MergeNode", type=trace_activitydiagram_TracedMergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedMergeNode", type=activitydiagram_trace_MergeNode, multiplicity=Multiplicity(0, 1))
    }
)
activitydiagramConfiguration_tracedForkedTokens755: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedForkedTokens755",
    ends={
        Property(name="activitydiagramConfiguration_TracedForkedToken757", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects756", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedActivityFinalNodes758: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedActivityFinalNodes758",
    ends={
        Property(name="activitydiagram_TracedActivityFinalNode760", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects759", type=activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedOffers761: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedOffers761",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer763", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects762", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedForkNodes764: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedForkNodes764",
    ends={
        Property(name="activitydiagram_TracedForkNode766", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects765", type=activitydiagram_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedInitialNodes767: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedInitialNodes767",
    ends={
        Property(name="activitydiagram_TracedInitialNode769", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects768", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedActivitys770: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedActivitys770",
    ends={
        Property(name="activitydiagram_TracedActivity772", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects771", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedStringVariables773: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedStringVariables773",
    ends={
        Property(name="activitydiagram_TracedStringVariable775", type=trace_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_Traced_TracedObjects774", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue802: BinaryAssociation = BinaryAssociation(
    name="initialValue802",
    ends={
        Property(name="activitydiagram_trace_Value", type=trace_activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedVariable", type=activitydiagram_trace_Value, multiplicity=Multiplicity(0, 1))
    }
)
currentValueTrace803: BinaryAssociation = BinaryAssociation(
    name="currentValueTrace803",
    ends={
        Property(name="States805", type=trace_activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable_currentValue_State804", type=Variable_currentValue_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject806: BinaryAssociation = BinaryAssociation(
    name="originalObject806",
    ends={
        Property(name="activitydiagram_trace_ActivityFinalNode", type=trace_activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityFinalNode", type=activitydiagram_trace_ActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject807: BinaryAssociation = BinaryAssociation(
    name="originalObject807",
    ends={
        Property(name="activitydiagram_trace_ForkNode", type=trace_activitydiagram_TracedForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedForkNode", type=activitydiagram_trace_ForkNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject792: BinaryAssociation = BinaryAssociation(
    name="originalObject792",
    ends={
        Property(name="activitydiagram_trace_BooleanVariable", type=trace_activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedBooleanVariable", type=activitydiagram_trace_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
originalObject793: BinaryAssociation = BinaryAssociation(
    name="originalObject793",
    ends={
        Property(name="activitydiagram_trace_IntegerVariable", type=trace_activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedIntegerVariable", type=activitydiagram_trace_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
source794: BinaryAssociation = BinaryAssociation(
    name="source794",
    ends={
        Property(name="activitydiagram_TracedActivityNode795", type=trace_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityEdge", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target796: BinaryAssociation = BinaryAssociation(
    name="target796",
    ends={
        Property(name="activitydiagram_TracedActivityNode798", type=trace_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityEdge797", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offersTrace799: BinaryAssociation = BinaryAssociation(
    name="offersTrace799",
    ends={
        Property(name="States801", type=trace_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge_offers_State800", type=ActivityEdge_offers_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heldTokensTrace820: BinaryAssociation = BinaryAssociation(
    name="heldTokensTrace820",
    ends={
        Property(name="States822", type=trace_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_heldTokens_State821", type=ActivityNode_heldTokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes823: BinaryAssociation = BinaryAssociation(
    name="nodes823",
    ends={
        Property(name="activitydiagram_TracedActivityNode824", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivity", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
edges825: BinaryAssociation = BinaryAssociation(
    name="edges825",
    ends={
        Property(name="activitydiagram_TracedActivityEdge827", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivity826", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
locals828: BinaryAssociation = BinaryAssociation(
    name="locals828",
    ends={
        Property(name="activitydiagram_TracedVariable830", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivity829", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
inputs831: BinaryAssociation = BinaryAssociation(
    name="inputs831",
    ends={
        Property(name="activitydiagram_TracedVariable833", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivity832", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject834: BinaryAssociation = BinaryAssociation(
    name="originalObject834",
    ends={
        Property(name="activitydiagram_trace_Activity", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivity835", type=activitydiagram_trace_Activity, multiplicity=Multiplicity(0, 1))
    }
)
traceTrace836: BinaryAssociation = BinaryAssociation(
    name="traceTrace836",
    ends={
        Property(name="States838", type=trace_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity_trace_State837", type=Activity_trace_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject808: BinaryAssociation = BinaryAssociation(
    name="originalObject808",
    ends={
        Property(name="activitydiagram_trace_InitialNode", type=trace_activitydiagram_TracedInitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedInitialNode", type=activitydiagram_trace_InitialNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject839: BinaryAssociation = BinaryAssociation(
    name="originalObject839",
    ends={
        Property(name="activitydiagram_trace_StringVariable", type=trace_activitydiagram_TracedStringVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedStringVariable", type=activitydiagram_trace_StringVariable, multiplicity=Multiplicity(0, 1))
    }
)
outgoing809: BinaryAssociation = BinaryAssociation(
    name="outgoing809",
    ends={
        Property(name="activitydiagram_TracedActivityEdge810", type=trace_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityNode", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming811: BinaryAssociation = BinaryAssociation(
    name="incoming811",
    ends={
        Property(name="activitydiagram_TracedActivityEdge813", type=trace_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityNode812", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity814: BinaryAssociation = BinaryAssociation(
    name="activity814",
    ends={
        Property(name="activitydiagram_TracedActivity816", type=trace_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedActivityNode815", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1))
    }
)
runningTrace817: BinaryAssociation = BinaryAssociation(
    name="runningTrace817",
    ends={
        Property(name="States819", type=trace_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_running_State818", type=ActivityNode_running_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueTrace845: BinaryAssociation = BinaryAssociation(
    name="valueTrace845",
    ends={
        Property(name="States847", type=trace_activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_value_State846", type=InputValue_value_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableTrace848: BinaryAssociation = BinaryAssociation(
    name="variableTrace848",
    ends={
        Property(name="States850", type=trace_activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_variable_State849", type=InputValue_variable_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
holderTrace851: BinaryAssociation = BinaryAssociation(
    name="holderTrace851",
    ends={
        Property(name="States853", type=trace_activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_State852", type=Token_holder_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputValuesTrace854: BinaryAssociation = BinaryAssociation(
    name="inputValuesTrace854",
    ends={
        Property(name="States856", type=trace_activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(1, 1)),
        Property(name="Input_inputValues_State855", type=Input_inputValues_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
remainingOffersCountTrace857: BinaryAssociation = BinaryAssociation(
    name="remainingOffersCountTrace857",
    ends={
        Property(name="States859", type=trace_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_State858", type=ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenTrace860: BinaryAssociation = BinaryAssociation(
    name="baseTokenTrace860",
    ends={
        Property(name="States862", type=trace_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_State861", type=ForkedToken_baseToken_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenIsWithdrawnTrace863: BinaryAssociation = BinaryAssociation(
    name="baseTokenIsWithdrawnTrace863",
    ends={
        Property(name="States865", type=trace_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_State864", type=ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions840: BinaryAssociation = BinaryAssociation(
    name="expressions840",
    ends={
        Property(name="activitydiagram_trace_Expression", type=trace_activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedOpaqueAction", type=activitydiagram_trace_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject841: BinaryAssociation = BinaryAssociation(
    name="originalObject841",
    ends={
        Property(name="activitydiagram_trace_OpaqueAction", type=trace_activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedOpaqueAction842", type=activitydiagram_trace_OpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
originalObject843: BinaryAssociation = BinaryAssociation(
    name="originalObject843",
    ends={
        Property(name="activitydiagram_trace_JoinNode", type=trace_activitydiagram_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedJoinNode", type=activitydiagram_trace_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject844: BinaryAssociation = BinaryAssociation(
    name="originalObject844",
    ends={
        Property(name="activitydiagram_trace_DecisionNode", type=trace_activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_activitydiagram_TracedDecisionNode", type=activitydiagram_trace_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
offeredTokensTrace866: BinaryAssociation = BinaryAssociation(
    name="offeredTokensTrace866",
    ends={
        Property(name="States868", type=trace_activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_State867", type=Offer_offeredTokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
executedNodesTrace869: BinaryAssociation = BinaryAssociation(
    name="executedNodesTrace869",
    ends={
        Property(name="States871", type=trace_activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_executedNodes_State870", type=Trace_executedNodes_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_trace_Events_Activity_initializeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_initializeExitEventOccurrence)
gen_trace_Events_Activity_runEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_runEntryEventOccurrence)
gen_trace_Events_Activity_runExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_runExitEventOccurrence)
gen_trace_Events_Activity_runNodesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_runNodesEntryEventOccurrence)
gen_trace_Events_Activity_runNodesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_runNodesExitEventOccurrence)
gen_trace_Events_Activity_mainEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_mainEntryEventOccurrence)
gen_trace_Events_Activity_mainExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_mainExitEventOccurrence)
gen_trace_Events_Activity_initializeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_initializeEntryEventOccurrence)
gen_trace_Events_Activity_selectNextNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_selectNextNodeExitEventOccurrence)
gen_trace_Events_Activity_terminateEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_terminateEntryEventOccurrence)
gen_trace_Events_Activity_terminateExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_terminateExitEventOccurrence)
gen_trace_Events_Activity_getInitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_getInitialNodeEntryEventOccurrence)
gen_trace_Events_Activity_getInitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_getInitialNodeExitEventOccurrence)
gen_trace_Events_Activity_fireInitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_fireInitialNodeEntryEventOccurrence)
gen_trace_Events_Activity_fireInitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_fireInitialNodeExitEventOccurrence)
gen_trace_Events_Activity_getEnabledNodesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_getEnabledNodesEntryEventOccurrence)
gen_trace_Events_Activity_getEnabledNodesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_getEnabledNodesExitEventOccurrence)
gen_trace_Events_Activity_selectNextNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_selectNextNodeEntryEventOccurrence)
gen_trace_Events_ActivityNode_isRunningEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_isRunningEntryEventOccurrence)
gen_trace_Events_ActivityNode_isRunningExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_isRunningExitEventOccurrence)
gen_trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)
gen_trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)
gen_trace_Events_ActivityNode_sendOffersEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_sendOffersEntryEventOccurrence)
gen_trace_Events_Activity_fireNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_fireNodeEntryEventOccurrence)
gen_trace_Events_Activity_fireNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Activity_fireNodeExitEventOccurrence)
gen_trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence)
gen_trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_run_activityNodeExitEventOccurrence)
gen_trace_Events_ActivityNode_addTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_addTokensExitEventOccurrence)
gen_trace_Events_ActivityNode_removeTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_removeTokenEntryEventOccurrence)
gen_trace_Events_ActivityNode_removeTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_removeTokenExitEventOccurrence)
gen_trace_Events_ActivityNode_hasOffersEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_hasOffersEntryEventOccurrence)
gen_trace_Events_ActivityNode_sendOffersExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_sendOffersExitEventOccurrence)
gen_trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)
gen_trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)
gen_trace_Events_ActivityNode_addTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_addTokensEntryEventOccurrence)
gen_trace_Events_ActivityEdge_sendOfferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_sendOfferExitEventOccurrence)
gen_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)
gen_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)
gen_trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_hasOfferEntryEventOccurrence)
gen_trace_Events_ActivityNode_hasOffersExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_hasOffersExitEventOccurrence)
gen_trace_Events_ActivityNode_isReadyEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_isReadyEntryEventOccurrence)
gen_trace_Events_ActivityNode_isReadyExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityNode_isReadyExitEventOccurrence)
gen_trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_sendOfferEntryEventOccurrence)
gen_trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ControlNode_fire_controlNodeExitEventOccurrence)
gen_trace_Events_Action_sendOffers_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_sendOffers_actionEntryEventOccurrence)
gen_trace_Events_Action_sendOffers_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_sendOffers_actionExitEventOccurrence)
gen_trace_Events_Action_isReady_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_isReady_actionEntryEventOccurrence)
gen_trace_Events_Action_isReady_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_isReady_actionExitEventOccurrence)
gen_trace_Events_ActivityEdge_hasOfferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityEdge_hasOfferExitEventOccurrence)
gen_trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)
gen_trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)
gen_trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence)
gen_trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)
gen_trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)
gen_trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence)
gen_trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_InitialNode_fire_initialNodeExitEventOccurrence)
gen_trace_Events_Action_fire_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_fire_actionEntryEventOccurrence)
gen_trace_Events_Action_fire_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Action_fire_actionExitEventOccurrence)
gen_trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)
gen_trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)
gen_trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)
gen_trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)
gen_trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)
gen_trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)
gen_trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)
gen_trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)
gen_trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence)
gen_trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ForkNode_fire_forkNodeExitEventOccurrence)
gen_trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)
gen_trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)
gen_trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)
gen_trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)
gen_trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)
gen_trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)
gen_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)
gen_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)
gen_trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)
gen_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)
gen_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)
gen_trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)
gen_trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)
gen_trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)
gen_trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)
gen_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)
gen_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)
gen_trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)
gen_trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)
gen_trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)
gen_trace_Events_Token_isWithdrawnEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_isWithdrawnEntryEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)
gen_trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)
gen_trace_Events_Token_withdrawEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_withdrawEntryEventOccurrence)
gen_trace_Events_Token_withdrawExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_withdrawExitEventOccurrence)
gen_trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)
gen_trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)
gen_trace_Events_Token_isWithdrawnExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_isWithdrawnExitEventOccurrence)
gen_trace_Events_Token_transferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_transferEntryEventOccurrence)
gen_trace_Events_Token_transferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Token_transferExitEventOccurrence)
gen_trace_Events_Offer_hasTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Offer_hasTokensEntryEventOccurrence)
gen_trace_Events_Offer_hasTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=trace_Events_Offer_hasTokensExitEventOccurrence)
gen_trace_activitydiagram_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=trace_activitydiagram_TracedControlFlow)
gen_trace_activitydiagram_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedMergeNode)
gen_trace_activitydiagram_TracedVariable_TracedNamedElement = Generalization(general=TracedNamedElement, specific=trace_activitydiagram_TracedVariable)
gen_trace_activitydiagram_TracedAction_TracedExecutableNode = Generalization(general=TracedExecutableNode, specific=trace_activitydiagram_TracedAction)
gen_trace_activitydiagram_TracedActivityFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=trace_activitydiagram_TracedActivityFinalNode)
gen_trace_activitydiagram_TracedForkNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedForkNode)
gen_trace_activitydiagram_TracedInitialNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedInitialNode)
gen_trace_activitydiagram_TracedBooleanVariable_TracedVariable = Generalization(general=TracedVariable, specific=trace_activitydiagram_TracedBooleanVariable)
gen_trace_activitydiagram_TracedExecutableNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=trace_activitydiagram_TracedExecutableNode)
gen_trace_activitydiagram_TracedIntegerVariable_TracedVariable = Generalization(general=TracedVariable, specific=trace_activitydiagram_TracedIntegerVariable)
gen_trace_activitydiagram_TracedActivityEdge_TracedNamedElement = Generalization(general=TracedNamedElement, specific=trace_activitydiagram_TracedActivityEdge)
gen_trace_activitydiagram_TracedActivity_TracedNamedElement = Generalization(general=TracedNamedElement, specific=trace_activitydiagram_TracedActivity)
gen_trace_activitydiagram_TracedStringVariable_TracedVariable = Generalization(general=TracedVariable, specific=trace_activitydiagram_TracedStringVariable)
gen_trace_activitydiagram_TracedActivityNode_TracedNamedElement = Generalization(general=TracedNamedElement, specific=trace_activitydiagram_TracedActivityNode)
gen_trace_activitydiagramConfiguration_TracedControlToken_TracedToken = Generalization(general=TracedToken, specific=trace_activitydiagramConfiguration_TracedControlToken)
gen_trace_activitydiagramConfiguration_TracedForkedToken_TracedToken = Generalization(general=TracedToken, specific=trace_activitydiagramConfiguration_TracedForkedToken)
gen_trace_activitydiagram_TracedOpaqueAction_TracedAction = Generalization(general=TracedAction, specific=trace_activitydiagram_TracedOpaqueAction)
gen_trace_activitydiagram_TracedJoinNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedJoinNode)
gen_trace_activitydiagram_TracedDecisionNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedDecisionNode)
gen_trace_activitydiagram_TracedFinalNode_TracedControlNode = Generalization(general=TracedControlNode, specific=trace_activitydiagram_TracedFinalNode)
gen_trace_activitydiagram_TracedControlNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=trace_activitydiagram_TracedControlNode)

# Domain Model
domain_model = DomainModel(
    name="trace",
    types={trace_Trace, trace_GlobalState, Events, TracedObjects, trace_StaticObjectsPools, EventOccurrence, InputValue_value_State, InputValue_variable_State, Token_holder_State, Input_inputValues_State, ForkedToken_remainingOffersCount_State, ForkedToken_baseToken_State, ForkedToken_baseTokenIsWithdrawn_State, ActivityEdge_offers_State, Variable_currentValue_State, Offer_offeredTokens_State, trace_BooleanValue, trace_IntegerComparisonExpression, trace_BooleanUnaryExpression, trace_IntegerCalculationExpression, trace_Events_EventOccurrence, Events_trace_GlobalState, trace_Events_Events, Activity_mainEntryEventOccurrence, Activity_mainExitEventOccurrence, Activity_initializeEntryEventOccurrence, Activity_initializeExitEventOccurrence, ActivityNode_running_State, ActivityNode_heldTokens_State, Activity_trace_State, Trace_executedNodes_State, trace_BooleanBinaryExpression, trace_StringValue, trace_IntegerValue, Activity_selectNextNodeEntryEventOccurrence, Activity_selectNextNodeExitEventOccurrence, Activity_terminateEntryEventOccurrence, Activity_terminateExitEventOccurrence, Activity_getInitialNodeEntryEventOccurrence, Activity_getInitialNodeExitEventOccurrence, Activity_fireNodeEntryEventOccurrence, Activity_fireNodeExitEventOccurrence, ActivityNode_run_activityNodeEntryEventOccurrence, Activity_runEntryEventOccurrence, Activity_runExitEventOccurrence, Activity_runNodesEntryEventOccurrence, Activity_runNodesExitEventOccurrence, Activity_fireInitialNodeEntryEventOccurrence, Activity_fireInitialNodeExitEventOccurrence, Activity_getEnabledNodesEntryEventOccurrence, Activity_getEnabledNodesExitEventOccurrence, ActivityNode_sendOffersExitEventOccurrence, ActivityNode_takeOfferedTokensEntryEventOccurrence, ActivityNode_run_activityNodeExitEventOccurrence, ActivityNode_isRunningEntryEventOccurrence, ActivityNode_isRunningExitEventOccurrence, ActivityNode_terminate_activityNodeEntryEventOccurrence, ActivityNode_terminate_activityNodeExitEventOccurrence, ActivityNode_sendOffersEntryEventOccurrence, ActivityNode_hasOffersEntryEventOccurrence, ActivityNode_hasOffersExitEventOccurrence, ActivityNode_isReadyEntryEventOccurrence, ActivityNode_isReadyExitEventOccurrence, ActivityEdge_sendOfferEntryEventOccurrence, ActivityEdge_sendOfferExitEventOccurrence, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, ActivityNode_takeOfferedTokensExitEventOccurrence, ActivityNode_addTokensEntryEventOccurrence, ActivityNode_addTokensExitEventOccurrence, ActivityNode_removeTokenEntryEventOccurrence, ActivityNode_removeTokenExitEventOccurrence, ControlNode_isReady_ControlNodeExitEventOccurrence, ControlNode_fire_controlNodeEntryEventOccurrence, ControlNode_fire_controlNodeExitEventOccurrence, Action_sendOffers_actionEntryEventOccurrence, Action_sendOffers_actionExitEventOccurrence, Action_isReady_actionEntryEventOccurrence, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, ActivityEdge_hasOfferEntryEventOccurrence, ActivityEdge_hasOfferExitEventOccurrence, ControlNode_isReady_ControlNodeEntryEventOccurrence, InitialNode_isReady_InitialNodeEntryEventOccurrence, InitialNode_isReady_InitialNodeExitEventOccurrence, InitialNode_fire_initialNodeEntryEventOccurrence, InitialNode_fire_initialNodeExitEventOccurrence, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, Action_isReady_actionExitEventOccurrence, Action_fire_actionEntryEventOccurrence, Action_fire_actionExitEventOccurrence, OpaqueAction_doAction_opaqueActionEntryEventOccurrence, OpaqueAction_doAction_opaqueActionExitEventOccurrence, DecisionNode_fire_decisionNodeExitEventOccurrence, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, ForkNode_fire_forkNodeEntryEventOccurrence, ForkNode_fire_forkNodeExitEventOccurrence, MergeNode_hasOffers_mergeNodeEntryEventOccurrence, MergeNode_hasOffers_mergeNodeExitEventOccurrence, DecisionNode_fire_decisionNodeEntryEventOccurrence, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, IntegerExpression_getOperandCurrentValuesExitEventOccurrence, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, StringVariable_setCurrentValue_stringVariableExitEventOccurrence, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, IntegerCalculationExpression_evaluateADDEntryEventOccurrence, IntegerCalculationExpression_evaluateADDExitEventOccurrence, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, BooleanBinaryExpression_evaluateANDEntryEventOccurrence, BooleanBinaryExpression_evaluateANDExitEventOccurrence, BooleanBinaryExpression_evaluateOREntryEventOccurrence, BooleanBinaryExpression_evaluateORExitEventOccurrence, Token_isWithdrawnEntryEventOccurrence, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, BooleanUnaryExpression_evaluateNOTExitEventOccurrence, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, Token_withdrawEntryEventOccurrence, Token_withdrawExitEventOccurrence, ForkedToken_withdraw_forkedTokenEntryEventOccurrence, ForkedToken_withdraw_forkedTokenExitEventOccurrence, Offer_hasTokensEntryEventOccurrence, Token_isWithdrawnExitEventOccurrence, Token_transferEntryEventOccurrence, Token_transferExitEventOccurrence, trace_Events_Activity_initializeExitEventOccurrence, trace_Events_Activity_runEntryEventOccurrence, trace_Events_Activity_runExitEventOccurrence, trace_Events_Activity_runNodesEntryEventOccurrence, trace_Events_Activity_runNodesExitEventOccurrence, Offer_hasTokensExitEventOccurrence, trace_Events_Activity_mainEntryEventOccurrence, activitydiagram_TracedActivity, Events_trace_EObject, trace_Events_Activity_mainExitEventOccurrence, trace_Events_Activity_initializeEntryEventOccurrence, trace_Events_Activity_selectNextNodeExitEventOccurrence, trace_Events_Activity_terminateEntryEventOccurrence, trace_Events_Activity_terminateExitEventOccurrence, trace_Events_Activity_getInitialNodeEntryEventOccurrence, trace_Events_Activity_getInitialNodeExitEventOccurrence, trace_Events_Activity_fireInitialNodeEntryEventOccurrence, trace_Events_Activity_fireInitialNodeExitEventOccurrence, trace_Events_Activity_getEnabledNodesEntryEventOccurrence, trace_Events_Activity_getEnabledNodesExitEventOccurrence, trace_Events_Activity_selectNextNodeEntryEventOccurrence, trace_Events_ActivityNode_isRunningEntryEventOccurrence, trace_Events_ActivityNode_isRunningExitEventOccurrence, trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence, trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence, trace_Events_ActivityNode_sendOffersEntryEventOccurrence, trace_Events_Activity_fireNodeEntryEventOccurrence, trace_Events_Activity_fireNodeExitEventOccurrence, trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence, activitydiagram_TracedActivityNode, trace_Events_ActivityNode_run_activityNodeExitEventOccurrence, trace_Events_ActivityNode_addTokensExitEventOccurrence, trace_Events_ActivityNode_removeTokenEntryEventOccurrence, trace_Events_ActivityNode_removeTokenExitEventOccurrence, trace_Events_ActivityNode_hasOffersEntryEventOccurrence, trace_Events_ActivityNode_sendOffersExitEventOccurrence, trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence, trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, trace_Events_ActivityNode_addTokensEntryEventOccurrence, activitydiagram_TracedActivityEdge, trace_Events_ActivityEdge_sendOfferExitEventOccurrence, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, trace_Events_ActivityEdge_hasOfferEntryEventOccurrence, trace_Events_ActivityNode_hasOffersExitEventOccurrence, trace_Events_ActivityNode_isReadyEntryEventOccurrence, trace_Events_ActivityNode_isReadyExitEventOccurrence, trace_Events_ActivityEdge_sendOfferEntryEventOccurrence, activitydiagramConfiguration_TracedToken, trace_Events_ControlNode_fire_controlNodeExitEventOccurrence, trace_Events_Action_sendOffers_actionEntryEventOccurrence, activitydiagram_TracedAction, trace_Events_Action_sendOffers_actionExitEventOccurrence, trace_Events_Action_isReady_actionEntryEventOccurrence, trace_Events_Action_isReady_actionExitEventOccurrence, trace_Events_ActivityEdge_hasOfferExitEventOccurrence, trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence, activitydiagram_TracedControlNode, trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence, trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence, activitydiagram_TracedInitialNode, trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence, trace_Events_InitialNode_fire_initialNodeExitEventOccurrence, trace_Events_Action_fire_actionEntryEventOccurrence, trace_Events_Action_fire_actionExitEventOccurrence, trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence, activitydiagram_TracedOpaqueAction, trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence, trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence, activitydiagram_TracedMergeNode, trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, activitydiagram_TracedDecisionNode, trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence, trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, activitydiagram_TracedActivityFinalNode, trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence, activitydiagram_TracedForkNode, trace_Events_ForkNode_fire_forkNodeExitEventOccurrence, trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, activitydiagram_TracedStringVariable, trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence, trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, activitydiagram_TracedIntegerVariable, Events_trace_Value, trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, Events_trace_IntegerExpression, trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, activitydiagram_TracedBooleanVariable, trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, Events_trace_IntegerCalculationExpression, trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, Events_trace_IntegerComparisonExpression, trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, Events_trace_BooleanUnaryExpression, trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence, trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, trace_Events_Token_isWithdrawnEntryEventOccurrence, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, Events_trace_BooleanBinaryExpression, trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence, trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, trace_Events_Token_withdrawEntryEventOccurrence, trace_Events_Token_withdrawExitEventOccurrence, trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence, activitydiagramConfiguration_TracedForkedToken, trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence, trace_Events_Token_isWithdrawnExitEventOccurrence, trace_Events_Token_transferEntryEventOccurrence, trace_Events_Token_transferExitEventOccurrence, activitydiagramConfiguration_TracedInputValue, States_trace_GlobalState, trace_States_InputValue_variable_State, activitydiagram_TracedVariable, trace_States_Token_holder_State, trace_Events_Offer_hasTokensEntryEventOccurrence, activitydiagramConfiguration_TracedOffer, trace_Events_Offer_hasTokensExitEventOccurrence, trace_States_InputValue_value_State, States_trace_Value, trace_States_ForkedToken_baseToken_State, trace_States_ForkedToken_baseTokenIsWithdrawn_State, trace_States_ActivityEdge_offers_State, trace_States_Input_inputValues_State, activitydiagramConfiguration_TracedInput, trace_States_ForkedToken_remainingOffersCount_State, trace_States_Offer_offeredTokens_State, trace_States_Variable_currentValue_State, trace_States_Activity_trace_State, activitydiagramConfiguration_TracedTrace, trace_States_ActivityNode_running_State, trace_States_ActivityNode_heldTokens_State, trace_Traced_TracedObjects, activitydiagram_TracedControlFlow, activitydiagramConfiguration_TracedControlToken, trace_States_Trace_executedNodes_State, activitydiagram_TracedJoinNode, trace_activitydiagram_TracedControlFlow, TracedActivityEdge, activitydiagram_trace_ControlFlow, trace_activitydiagram_TracedMergeNode, TracedControlNode, activitydiagram_trace_MergeNode, trace_activitydiagram_TracedNamedElement, trace_activitydiagram_TracedVariable, activitydiagram_trace_Value, trace_activitydiagram_TracedAction, TracedExecutableNode, trace_activitydiagram_TracedActivityFinalNode, TracedFinalNode, activitydiagram_trace_ActivityFinalNode, trace_activitydiagram_TracedForkNode, activitydiagram_trace_ForkNode, trace_activitydiagram_TracedInitialNode, activitydiagram_trace_InitialNode, trace_activitydiagram_TracedBooleanVariable, TracedVariable, activitydiagram_trace_BooleanVariable, trace_activitydiagram_TracedExecutableNode, TracedActivityNode, trace_activitydiagram_TracedIntegerVariable, activitydiagram_trace_IntegerVariable, trace_activitydiagram_TracedActivityEdge, TracedNamedElement, trace_activitydiagram_TracedActivity, activitydiagram_trace_Activity, trace_activitydiagram_TracedStringVariable, activitydiagram_trace_StringVariable, trace_activitydiagram_TracedActivityNode, trace_activitydiagramConfiguration_TracedInputValue, trace_activitydiagramConfiguration_TracedToken, trace_activitydiagramConfiguration_TracedControlToken, TracedToken, trace_activitydiagramConfiguration_TracedInput, trace_activitydiagramConfiguration_TracedForkedToken, trace_activitydiagram_TracedOpaqueAction, TracedAction, activitydiagram_trace_Expression, activitydiagram_trace_OpaqueAction, trace_activitydiagram_TracedJoinNode, activitydiagram_trace_JoinNode, trace_activitydiagram_TracedDecisionNode, activitydiagram_trace_DecisionNode, trace_activitydiagram_TracedFinalNode, trace_activitydiagram_TracedControlNode, trace_activitydiagramConfiguration_TracedOffer, trace_activitydiagramConfiguration_TracedTrace},
    associations={globalTrace0, events1, tracedObjects3, staticObjectsPools5, eventsTriggeredDuringState7, inputValue_value_States9, inputValue_variable_States10, token_holder_States12, input_inputValues_States14, forkedToken_remainingOffersCount_States16, forkedToken_baseToken_States18, forkedToken_baseTokenIsWithdrawn_States20, activityEdge_offers_States22, variable_currentValue_States24, pool_BooleanValues42, pool_IntegerComparisonExpressions44, pool_BooleanUnaryExpressions46, pool_IntegerCalculationExpressions48, stateDuringWhichTriggered50, Activity_mainEntryEventOccurrence_Trace51, Activity_mainExitEventOccurrence_Trace52, Activity_initializeEntryEventOccurrence_Trace54, Activity_initializeExitEventOccurrence_Trace56, offer_offeredTokens_States26, activityNode_running_States28, activityNode_heldTokens_States30, activity_trace_States32, trace_executedNodes_States34, pool_BooleanBinaryExpressions36, pool_StringValues38, pool_IntegerValues40, Activity_selectNextNodeEntryEventOccurrence_Trace74, Activity_selectNextNodeExitEventOccurrence_Trace76, Activity_terminateEntryEventOccurrence_Trace78, Activity_terminateExitEventOccurrence_Trace80, Activity_getInitialNodeEntryEventOccurrence_Trace82, Activity_getInitialNodeExitEventOccurrence_Trace84, Activity_fireNodeEntryEventOccurrence_Trace86, Activity_fireNodeExitEventOccurrence_Trace88, ActivityNode_run_activityNodeEntryEventOccurrence_Trace90, Activity_runEntryEventOccurrence_Trace58, Activity_runExitEventOccurrence_Trace60, Activity_runNodesEntryEventOccurrence_Trace62, Activity_runNodesExitEventOccurrence_Trace64, Activity_fireInitialNodeEntryEventOccurrence_Trace66, Activity_fireInitialNodeExitEventOccurrence_Trace68, Activity_getEnabledNodesEntryEventOccurrence_Trace70, Activity_getEnabledNodesExitEventOccurrence_Trace72, ActivityNode_sendOffersEntryEventOccurrence_Trace102, ActivityNode_sendOffersExitEventOccurrence_Trace104, ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106, ActivityNode_run_activityNodeExitEventOccurrence_Trace92, ActivityNode_isRunningEntryEventOccurrence_Trace94, ActivityNode_isRunningExitEventOccurrence_Trace96, ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98, ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100, ActivityNode_hasOffersEntryEventOccurrence_Trace118, ActivityNode_hasOffersExitEventOccurrence_Trace120, ActivityNode_isReadyEntryEventOccurrence_Trace122, ActivityNode_isReadyExitEventOccurrence_Trace124, ActivityEdge_sendOfferEntryEventOccurrence_Trace126, ActivityEdge_sendOfferExitEventOccurrence_Trace128, ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108, ActivityNode_addTokensEntryEventOccurrence_Trace110, ActivityNode_addTokensExitEventOccurrence_Trace112, ActivityNode_removeTokenEntryEventOccurrence_Trace114, ActivityNode_removeTokenExitEventOccurrence_Trace116, ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140, ControlNode_fire_controlNodeEntryEventOccurrence_Trace142, ControlNode_fire_controlNodeExitEventOccurrence_Trace144, Action_sendOffers_actionEntryEventOccurrence_Trace146, Action_sendOffers_actionExitEventOccurrence_Trace148, Action_isReady_actionEntryEventOccurrence_Trace150, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132, ActivityEdge_hasOfferEntryEventOccurrence_Trace134, ActivityEdge_hasOfferExitEventOccurrence_Trace136, ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138, InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162, InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164, InitialNode_fire_initialNodeEntryEventOccurrence_Trace166, InitialNode_fire_initialNodeExitEventOccurrence_Trace168, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172, Action_isReady_actionExitEventOccurrence_Trace152, Action_fire_actionEntryEventOccurrence_Trace154, Action_fire_actionExitEventOccurrence_Trace156, OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158, OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160, DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194, ForkNode_fire_forkNodeEntryEventOccurrence_Trace174, ForkNode_fire_forkNodeExitEventOccurrence_Trace176, MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178, MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180, DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210, IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214, StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216, IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218, IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242, BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262, BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264, BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266, BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254, BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260, Token_withdrawEntryEventOccurrence_Trace278, Token_withdrawExitEventOccurrence_Trace280, ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282, ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284, Offer_hasTokensEntryEventOccurrence_Trace286, Token_isWithdrawnEntryEventOccurrence_Trace270, Token_isWithdrawnExitEventOccurrence_Trace272, Token_transferEntryEventOccurrence_Trace274, Token_transferExitEventOccurrence_Trace276, thisParam295, inputValuesParam297, correspondingEntryEvent300, thisParam302, correspondingEntryEvent304, thisParam306, correspondingEntryEvent308, Offer_hasTokensExitEventOccurrence_Trace288, thisParam290, inputValuesParam291, correspondingEntryEvent293, thisParam321, activityNodesParam323, correspondingEntryEvent326, selectedNodeReturn328, thisParam331, correspondingEntryEvent333, thisParam335, thisParam310, correspondingEntryEvent312, thisParam314, correspondingEntryEvent316, enabledNodesReturn318, correspondingEntryEvent350, thisParam352, correspondingEntryEvent354, isRunningReturn356, thisParam359, correspondingEntryEvent361, thisParam363, correspondingEntryEvent337, initialNodeReturn339, thisParam342, nodeParam344, correspondingEntryEvent347, thisParam349, tokensParam379, correspondingEntryEvent382, thisParam384, tokenParam386, correspondingEntryEvent389, tokensParam365, correspondingEntryEvent368, thisParam370, correspondingEntryEvent372, tokensReturn374, thisParam377, thisParam405, tokensParam406, correspondingEntryEvent409, thisParam411, correspondingEntryEvent413, tokensReturn415, thisParam418, thisParam391, correspondingEntryEvent393, returnReturn395, thisParam398, correspondingEntryEvent400, isReadyReturn402, thisParam431, tokensParam433, correspondingEntryEvent435, thisParam437, correspondingEntryEvent438, thisParam440, correspondingEntryEvent442, correspondingEntryEvent420, hasOfferReturn422, thisParam425, correspondingEntryEvent426, isReadyReturn428, correspondingEntryEvent455, thisParam457, correspondingEntryEvent458, isReadyReturn460, thisParam463, tokensParam465, correspondingEntryEvent468, isReadyReturn444, thisParam447, tokensParam449, correspondingEntryEvent452, thisParam454, correspondingEntryEvent480, thisParam482, correspondingEntryEvent483, returnReturn485, thisParam488, tokensParam489, thisParam470, tokensParam471, correspondingEntryEvent474, thisParam476, tokensParam477, valueReturn503, thisParam506, valueParam507, correspondingEntryEvent510, thisParam512, correspondingEntryEvent492, thisParam494, valueParam495, correspondingEntryEvent497, thisParam499, correspondingEntryEvent501, valueParam520, correspondingEntryEvent523, thisParam525, correspondingEntryEvent527, valueReturn529, thisParam532, correspondingEntryEvent514, valueReturn516, thisParam519, thisParam544, correspondingEntryEvent546, resultReturn548, thisParam551, correspondingEntryEvent553, resultReturn555, correspondingEntryEvent533, operand1ValueReturn535, operand2ValueReturn538, thisParam541, correspondingEntryEvent542, thisParam568, correspondingEntryEvent570, resultReturn572, thisParam575, correspondingEntryEvent577, resultReturn579, thisParam558, correspondingEntryEvent559, thisParam561, correspondingEntryEvent563, resultReturn565, correspondingEntryEvent591, resultReturn593, thisParam596, correspondingEntryEvent597, thisParam599, correspondingEntryEvent601, thisParam582, correspondingEntryEvent584, resultReturn586, thisParam589, correspondingEntryEvent611, resultReturn613, thisParam616, correspondingEntryEvent618, resultReturn620, thisParam623, resultReturn603, thisParam606, correspondingEntryEvent607, thisParam609, correspondingEntryEvent635, transferredTokenReturn637, thisParam640, correspondingEntryEvent642, thisParam644, correspondingEntryEvent625, isWithdrawnReturn627, thisParam630, holderParam632, value653, parent654, globalStates655, variable657, parent658, globalStates661, holder663, correspondingEntryEvent645, thisParam647, correspondingEntryEvent648, hasTokensReturn650, baseToken681, parent683, globalStates686, parent688, globalStates691, offers693, parent695, parent665, globalStates668, inputValues670, parent671, globalStates674, parent676, globalStates679, globalStates704, offeredTokens706, parent708, globalStates711, globalStates697, currentValue699, parent701, heldTokens718, parent720, globalStates723, parent713, globalStates716, activitydiagram_tracedControlFlows738, activitydiagramConfiguration_tracedInputValues739, activitydiagram_tracedMergeNodes742, activitydiagram_tracedBooleanVariables745, activitydiagramConfiguration_tracedControlTokens748, activitydiagramConfiguration_tracedInputs750, activitydiagram_tracedIntegerVariables752, trace725, parent726, globalStates729, executedNodes731, parent733, globalStates736, activitydiagram_tracedOpaqueActions776, activitydiagram_tracedJoinNodes779, activitydiagram_tracedDecisionNodes781, activitydiagramConfiguration_tracedTraces784, guard787, originalObject789, originalObject791, activitydiagramConfiguration_tracedForkedTokens755, activitydiagram_tracedActivityFinalNodes758, activitydiagramConfiguration_tracedOffers761, activitydiagram_tracedForkNodes764, activitydiagram_tracedInitialNodes767, activitydiagram_tracedActivitys770, activitydiagram_tracedStringVariables773, initialValue802, currentValueTrace803, originalObject806, originalObject807, originalObject792, originalObject793, source794, target796, offersTrace799, heldTokensTrace820, nodes823, edges825, locals828, inputs831, originalObject834, traceTrace836, originalObject808, originalObject839, outgoing809, incoming811, activity814, runningTrace817, valueTrace845, variableTrace848, holderTrace851, inputValuesTrace854, remainingOffersCountTrace857, baseTokenTrace860, baseTokenIsWithdrawnTrace863, expressions840, originalObject841, originalObject843, originalObject844, offeredTokensTrace866, executedNodesTrace869},
    generalizations={gen_trace_Events_Activity_initializeExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_runEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_runExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_runNodesEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_runNodesExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_mainEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_mainExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_initializeEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_selectNextNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_terminateEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_terminateExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_getInitialNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_getInitialNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_fireInitialNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_fireInitialNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_getEnabledNodesEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_getEnabledNodesExitEventOccurrence_EventOccurrence, gen_trace_Events_Activity_selectNextNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_isRunningEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_isRunningExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_sendOffersEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_fireNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_Activity_fireNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_run_activityNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_run_activityNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_addTokensExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_removeTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_removeTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_hasOffersEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_sendOffersExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_addTokensEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_sendOfferExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_hasOfferEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_hasOffersExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_isReadyEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityNode_isReadyExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_sendOfferEntryEventOccurrence_EventOccurrence, gen_trace_Events_ControlNode_fire_controlNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_Action_sendOffers_actionEntryEventOccurrence_EventOccurrence, gen_trace_Events_Action_sendOffers_actionExitEventOccurrence_EventOccurrence, gen_trace_Events_Action_isReady_actionEntryEventOccurrence_EventOccurrence, gen_trace_Events_Action_isReady_actionExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityEdge_hasOfferExitEventOccurrence_EventOccurrence, gen_trace_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ControlNode_fire_controlNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_InitialNode_fire_initialNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_InitialNode_fire_initialNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_Action_fire_actionEntryEventOccurrence_EventOccurrence, gen_trace_Events_Action_fire_actionExitEventOccurrence_EventOccurrence, gen_trace_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_EventOccurrence, gen_trace_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_EventOccurrence, gen_trace_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_ForkNode_fire_forkNodeEntryEventOccurrence_EventOccurrence, gen_trace_Events_ForkNode_fire_forkNodeExitEventOccurrence_EventOccurrence, gen_trace_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_EventOccurrence, gen_trace_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_EventOccurrence, gen_trace_Events_Token_isWithdrawnEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_EventOccurrence, gen_trace_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_EventOccurrence, gen_trace_Events_Token_withdrawEntryEventOccurrence_EventOccurrence, gen_trace_Events_Token_withdrawExitEventOccurrence_EventOccurrence, gen_trace_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_EventOccurrence, gen_trace_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_EventOccurrence, gen_trace_Events_Token_isWithdrawnExitEventOccurrence_EventOccurrence, gen_trace_Events_Token_transferEntryEventOccurrence_EventOccurrence, gen_trace_Events_Token_transferExitEventOccurrence_EventOccurrence, gen_trace_Events_Offer_hasTokensEntryEventOccurrence_EventOccurrence, gen_trace_Events_Offer_hasTokensExitEventOccurrence_EventOccurrence, gen_trace_activitydiagram_TracedControlFlow_TracedActivityEdge, gen_trace_activitydiagram_TracedMergeNode_TracedControlNode, gen_trace_activitydiagram_TracedVariable_TracedNamedElement, gen_trace_activitydiagram_TracedAction_TracedExecutableNode, gen_trace_activitydiagram_TracedActivityFinalNode_TracedFinalNode, gen_trace_activitydiagram_TracedForkNode_TracedControlNode, gen_trace_activitydiagram_TracedInitialNode_TracedControlNode, gen_trace_activitydiagram_TracedBooleanVariable_TracedVariable, gen_trace_activitydiagram_TracedExecutableNode_TracedActivityNode, gen_trace_activitydiagram_TracedIntegerVariable_TracedVariable, gen_trace_activitydiagram_TracedActivityEdge_TracedNamedElement, gen_trace_activitydiagram_TracedActivity_TracedNamedElement, gen_trace_activitydiagram_TracedStringVariable_TracedVariable, gen_trace_activitydiagram_TracedActivityNode_TracedNamedElement, gen_trace_activitydiagramConfiguration_TracedControlToken_TracedToken, gen_trace_activitydiagramConfiguration_TracedForkedToken_TracedToken, gen_trace_activitydiagram_TracedOpaqueAction_TracedAction, gen_trace_activitydiagram_TracedJoinNode_TracedControlNode, gen_trace_activitydiagram_TracedDecisionNode_TracedControlNode, gen_trace_activitydiagram_TracedFinalNode_TracedControlNode, gen_trace_activitydiagram_TracedControlNode_TracedActivityNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)