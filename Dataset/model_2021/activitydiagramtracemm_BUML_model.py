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
traceSystem_Trace = Class(name="traceSystem::Trace")
traceSystem_GlobalState = Class(name="traceSystem::GlobalState")
Events = Class(name="Events")
Offer_offeredTokens_State = Class(name="Offer::offeredTokens::State")
Activity_trace_State = Class(name="Activity::trace::State")
Variable_currentValue_State = Class(name="Variable::currentValue::State")
InputValue_value_State = Class(name="InputValue::value::State")
InputValue_variable_State = Class(name="InputValue::variable::State")
ActivityEdge_offers_State = Class(name="ActivityEdge::offers::State")
Trace_executedNodes_State = Class(name="Trace::executedNodes::State")
Input_inputValues_State = Class(name="Input::inputValues::State")
ActivityNode_heldTokens_State = Class(name="ActivityNode::heldTokens::State")
ActivityNode_running_State = Class(name="ActivityNode::running::State")
TracedObjects = Class(name="TracedObjects")
traceSystem_StaticObjectsPools = Class(name="traceSystem::StaticObjectsPools")
EventOccurrence = Class(name="EventOccurrence")
ForkedToken_baseToken_State = Class(name="ForkedToken::baseToken::State")
ForkedToken_remainingOffersCount_State = Class(name="ForkedToken::remainingOffersCount::State")
ForkedToken_baseTokenIsWithdrawn_State = Class(name="ForkedToken::baseTokenIsWithdrawn::State")
Token_holder_State = Class(name="Token::holder::State")
Activity_mainEntryEventOccurrence = Class(name="Activity::mainEntryEventOccurrence")
Activity_mainExitEventOccurrence = Class(name="Activity::mainExitEventOccurrence")
Activity_initializeEntryEventOccurrence = Class(name="Activity::initializeEntryEventOccurrence")
Activity_initializeExitEventOccurrence = Class(name="Activity::initializeExitEventOccurrence")
Activity_runEntryEventOccurrence = Class(name="Activity::runEntryEventOccurrence")
Activity_runExitEventOccurrence = Class(name="Activity::runExitEventOccurrence")
Activity_runNodesEntryEventOccurrence = Class(name="Activity::runNodesEntryEventOccurrence")
Activity_runNodesExitEventOccurrence = Class(name="Activity::runNodesExitEventOccurrence")
Activity_fireInitialNodeEntryEventOccurrence = Class(name="Activity::fireInitialNodeEntryEventOccurrence")
Activity_fireInitialNodeExitEventOccurrence = Class(name="Activity::fireInitialNodeExitEventOccurrence")
Activity_getEnabledNodesEntryEventOccurrence = Class(name="Activity::getEnabledNodesEntryEventOccurrence")
traceSystem_BooleanValue = Class(name="traceSystem::BooleanValue")
traceSystem_IntegerComparisonExpression = Class(name="traceSystem::IntegerComparisonExpression")
traceSystem_StringValue = Class(name="traceSystem::StringValue")
traceSystem_BooleanBinaryExpression = Class(name="traceSystem::BooleanBinaryExpression")
traceSystem_BooleanUnaryExpression = Class(name="traceSystem::BooleanUnaryExpression")
traceSystem_IntegerValue = Class(name="traceSystem::IntegerValue")
traceSystem_IntegerCalculationExpression = Class(name="traceSystem::IntegerCalculationExpression")
traceSystem_Events_EventOccurrence = Class(name="traceSystem::Events::EventOccurrence", is_abstract=True)
Events_traceSystem_GlobalState = Class(name="Events::traceSystem::GlobalState")
traceSystem_Events_Events = Class(name="traceSystem::Events::Events")
ActivityNode_run_activityNodeEntryEventOccurrence = Class(name="ActivityNode::run::activityNodeEntryEventOccurrence")
ActivityNode_run_activityNodeExitEventOccurrence = Class(name="ActivityNode::run::activityNodeExitEventOccurrence")
ActivityNode_isRunningEntryEventOccurrence = Class(name="ActivityNode::isRunningEntryEventOccurrence")
ActivityNode_isRunningExitEventOccurrence = Class(name="ActivityNode::isRunningExitEventOccurrence")
ActivityNode_terminate_activityNodeEntryEventOccurrence = Class(name="ActivityNode::terminate::activityNodeEntryEventOccurrence")
ActivityNode_terminate_activityNodeExitEventOccurrence = Class(name="ActivityNode::terminate::activityNodeExitEventOccurrence")
Activity_getEnabledNodesExitEventOccurrence = Class(name="Activity::getEnabledNodesExitEventOccurrence")
Activity_selectNextNodeEntryEventOccurrence = Class(name="Activity::selectNextNodeEntryEventOccurrence")
Activity_selectNextNodeExitEventOccurrence = Class(name="Activity::selectNextNodeExitEventOccurrence")
Activity_terminateEntryEventOccurrence = Class(name="Activity::terminateEntryEventOccurrence")
Activity_terminateExitEventOccurrence = Class(name="Activity::terminateExitEventOccurrence")
Activity_getInitialNodeEntryEventOccurrence = Class(name="Activity::getInitialNodeEntryEventOccurrence")
Activity_getInitialNodeExitEventOccurrence = Class(name="Activity::getInitialNodeExitEventOccurrence")
Activity_fireNodeEntryEventOccurrence = Class(name="Activity::fireNodeEntryEventOccurrence")
Activity_fireNodeExitEventOccurrence = Class(name="Activity::fireNodeExitEventOccurrence")
ActivityNode_removeTokenExitEventOccurrence = Class(name="ActivityNode::removeTokenExitEventOccurrence")
ActivityNode_hasOffersEntryEventOccurrence = Class(name="ActivityNode::hasOffersEntryEventOccurrence")
ActivityNode_hasOffersExitEventOccurrence = Class(name="ActivityNode::hasOffersExitEventOccurrence")
ActivityNode_isReadyEntryEventOccurrence = Class(name="ActivityNode::isReadyEntryEventOccurrence")
ActivityNode_isReadyExitEventOccurrence = Class(name="ActivityNode::isReadyExitEventOccurrence")
ActivityEdge_sendOfferEntryEventOccurrence = Class(name="ActivityEdge::sendOfferEntryEventOccurrence")
ActivityEdge_sendOfferExitEventOccurrence = Class(name="ActivityEdge::sendOfferExitEventOccurrence")
ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence = Class(name="ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence")
ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence = Class(name="ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence")
ActivityNode_sendOffersEntryEventOccurrence = Class(name="ActivityNode::sendOffersEntryEventOccurrence")
ActivityNode_sendOffersExitEventOccurrence = Class(name="ActivityNode::sendOffersExitEventOccurrence")
ActivityNode_takeOfferedTokensEntryEventOccurrence = Class(name="ActivityNode::takeOfferedTokensEntryEventOccurrence")
ActivityNode_takeOfferedTokensExitEventOccurrence = Class(name="ActivityNode::takeOfferedTokensExitEventOccurrence")
ActivityNode_addTokensEntryEventOccurrence = Class(name="ActivityNode::addTokensEntryEventOccurrence")
ActivityNode_addTokensExitEventOccurrence = Class(name="ActivityNode::addTokensExitEventOccurrence")
ActivityNode_removeTokenEntryEventOccurrence = Class(name="ActivityNode::removeTokenEntryEventOccurrence")
Action_sendOffers_actionExitEventOccurrence = Class(name="Action::sendOffers::actionExitEventOccurrence")
Action_isReady_actionEntryEventOccurrence = Class(name="Action::isReady::actionEntryEventOccurrence")
Action_isReady_actionExitEventOccurrence = Class(name="Action::isReady::actionExitEventOccurrence")
Action_fire_actionEntryEventOccurrence = Class(name="Action::fire::actionEntryEventOccurrence")
Action_fire_actionExitEventOccurrence = Class(name="Action::fire::actionExitEventOccurrence")
OpaqueAction_doAction_opaqueActionEntryEventOccurrence = Class(name="OpaqueAction::doAction::opaqueActionEntryEventOccurrence")
OpaqueAction_doAction_opaqueActionExitEventOccurrence = Class(name="OpaqueAction::doAction::opaqueActionExitEventOccurrence")
InitialNode_isReady_InitialNodeEntryEventOccurrence = Class(name="InitialNode::isReady::InitialNodeEntryEventOccurrence")
ActivityEdge_hasOfferEntryEventOccurrence = Class(name="ActivityEdge::hasOfferEntryEventOccurrence")
ActivityEdge_hasOfferExitEventOccurrence = Class(name="ActivityEdge::hasOfferExitEventOccurrence")
ControlNode_isReady_ControlNodeEntryEventOccurrence = Class(name="ControlNode::isReady::ControlNodeEntryEventOccurrence")
ControlNode_isReady_ControlNodeExitEventOccurrence = Class(name="ControlNode::isReady::ControlNodeExitEventOccurrence")
ControlNode_fire_controlNodeEntryEventOccurrence = Class(name="ControlNode::fire::controlNodeEntryEventOccurrence")
ControlNode_fire_controlNodeExitEventOccurrence = Class(name="ControlNode::fire::controlNodeExitEventOccurrence")
Action_sendOffers_actionEntryEventOccurrence = Class(name="Action::sendOffers::actionEntryEventOccurrence")
InitialNode_fire_initialNodeExitEventOccurrence = Class(name="InitialNode::fire::initialNodeExitEventOccurrence")
ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence = Class(name="ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence")
ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence = Class(name="ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence")
ForkNode_fire_forkNodeEntryEventOccurrence = Class(name="ForkNode::fire::forkNodeEntryEventOccurrence")
ForkNode_fire_forkNodeExitEventOccurrence = Class(name="ForkNode::fire::forkNodeExitEventOccurrence")
MergeNode_hasOffers_mergeNodeEntryEventOccurrence = Class(name="MergeNode::hasOffers::mergeNodeEntryEventOccurrence")
InitialNode_isReady_InitialNodeExitEventOccurrence = Class(name="InitialNode::isReady::InitialNodeExitEventOccurrence")
StringVariable_setCurrentValue_stringVariableEntryEventOccurrence = Class(name="StringVariable::setCurrentValue::stringVariableEntryEventOccurrence")
InitialNode_fire_initialNodeEntryEventOccurrence = Class(name="InitialNode::fire::initialNodeEntryEventOccurrence")
StringVariable_setCurrentValue_stringVariableExitEventOccurrence = Class(name="StringVariable::setCurrentValue::stringVariableExitEventOccurrence")
StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence = Class(name="StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence")
StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence = Class(name="StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence")
BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence = Class(name="BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence")
BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence = Class(name="BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence")
MergeNode_hasOffers_mergeNodeExitEventOccurrence = Class(name="MergeNode::hasOffers::mergeNodeExitEventOccurrence")
BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence = Class(name="BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence")
DecisionNode_fire_decisionNodeEntryEventOccurrence = Class(name="DecisionNode::fire::decisionNodeEntryEventOccurrence")
DecisionNode_fire_decisionNodeExitEventOccurrence = Class(name="DecisionNode::fire::decisionNodeExitEventOccurrence")
IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence = Class(name="IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence")
IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence = Class(name="IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence")
IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence = Class(name="IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence")
IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence = Class(name="IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence")
IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence = Class(name="IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence")
IntegerCalculationExpression_evaluateADDEntryEventOccurrence = Class(name="IntegerCalculationExpression::evaluateADDEntryEventOccurrence")
IntegerCalculationExpression_evaluateADDExitEventOccurrence = Class(name="IntegerCalculationExpression::evaluateADDExitEventOccurrence")
IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence = Class(name="IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence")
IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence = Class(name="IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence")
IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence = Class(name="IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence")
IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence = Class(name="IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence")
BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence = Class(name="BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence")
IntegerExpression_getOperandCurrentValuesEntryEventOccurrence = Class(name="IntegerExpression::getOperandCurrentValuesEntryEventOccurrence")
IntegerExpression_getOperandCurrentValuesExitEventOccurrence = Class(name="IntegerExpression::getOperandCurrentValuesExitEventOccurrence")
IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence = Class(name="IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence")
IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence")
IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence")
IntegerComparisonExpression_evaluateGREATERExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateGREATERExitEventOccurrence")
BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence = Class(name="BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence")
IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence")
IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence")
IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence")
IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence = Class(name="IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence")
IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence = Class(name="IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence")
BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence = Class(name="BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence")
BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence = Class(name="BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence")
BooleanBinaryExpression_evaluateANDEntryEventOccurrence = Class(name="BooleanBinaryExpression::evaluateANDEntryEventOccurrence")
BooleanBinaryExpression_evaluateANDExitEventOccurrence = Class(name="BooleanBinaryExpression::evaluateANDExitEventOccurrence")
BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence = Class(name="BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence")
BooleanUnaryExpression_evaluateNOTEntryEventOccurrence = Class(name="BooleanUnaryExpression::evaluateNOTEntryEventOccurrence")
BooleanUnaryExpression_evaluateNOTExitEventOccurrence = Class(name="BooleanUnaryExpression::evaluateNOTExitEventOccurrence")
Token_transferExitEventOccurrence = Class(name="Token::transferExitEventOccurrence")
Token_withdrawEntryEventOccurrence = Class(name="Token::withdrawEntryEventOccurrence")
Token_withdrawExitEventOccurrence = Class(name="Token::withdrawExitEventOccurrence")
ForkedToken_withdraw_forkedTokenEntryEventOccurrence = Class(name="ForkedToken::withdraw::forkedTokenEntryEventOccurrence")
BooleanBinaryExpression_evaluateOREntryEventOccurrence = Class(name="BooleanBinaryExpression::evaluateOREntryEventOccurrence")
ForkedToken_withdraw_forkedTokenExitEventOccurrence = Class(name="ForkedToken::withdraw::forkedTokenExitEventOccurrence")
BooleanBinaryExpression_evaluateORExitEventOccurrence = Class(name="BooleanBinaryExpression::evaluateORExitEventOccurrence")
Offer_hasTokensEntryEventOccurrence = Class(name="Offer::hasTokensEntryEventOccurrence")
Token_isWithdrawnEntryEventOccurrence = Class(name="Token::isWithdrawnEntryEventOccurrence")
Token_isWithdrawnExitEventOccurrence = Class(name="Token::isWithdrawnExitEventOccurrence")
Token_transferEntryEventOccurrence = Class(name="Token::transferEntryEventOccurrence")
Offer_hasTokensExitEventOccurrence = Class(name="Offer::hasTokensExitEventOccurrence")
traceSystem_Events_Activity_mainEntryEventOccurrence = Class(name="traceSystem::Events::Activity::mainEntryEventOccurrence")
activitydiagram_TracedActivity = Class(name="activitydiagram::TracedActivity")
Events_traceSystem_EObject = Class(name="Events::traceSystem::EObject")
traceSystem_Events_Activity_mainExitEventOccurrence = Class(name="traceSystem::Events::Activity::mainExitEventOccurrence")
traceSystem_Events_Activity_initializeEntryEventOccurrence = Class(name="traceSystem::Events::Activity::initializeEntryEventOccurrence")
traceSystem_Events_Activity_initializeExitEventOccurrence = Class(name="traceSystem::Events::Activity::initializeExitEventOccurrence")
traceSystem_Events_Activity_runNodesExitEventOccurrence = Class(name="traceSystem::Events::Activity::runNodesExitEventOccurrence")
traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence = Class(name="traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence")
traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence = Class(name="traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence")
traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence = Class(name="traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence")
traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence = Class(name="traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence")
traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence = Class(name="traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence")
traceSystem_Events_Activity_selectNextNodeExitEventOccurrence = Class(name="traceSystem::Events::Activity::selectNextNodeExitEventOccurrence")
traceSystem_Events_Activity_runEntryEventOccurrence = Class(name="traceSystem::Events::Activity::runEntryEventOccurrence")
traceSystem_Events_Activity_runExitEventOccurrence = Class(name="traceSystem::Events::Activity::runExitEventOccurrence")
traceSystem_Events_Activity_runNodesEntryEventOccurrence = Class(name="traceSystem::Events::Activity::runNodesEntryEventOccurrence")
traceSystem_Events_Activity_fireNodeEntryEventOccurrence = Class(name="traceSystem::Events::Activity::fireNodeEntryEventOccurrence")
traceSystem_Events_Activity_fireNodeExitEventOccurrence = Class(name="traceSystem::Events::Activity::fireNodeExitEventOccurrence")
traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence")
activitydiagram_TracedActivityNode = Class(name="activitydiagram::TracedActivityNode")
traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence")
traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence")
traceSystem_Events_ActivityNode_isRunningExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::isRunningExitEventOccurrence")
traceSystem_Events_Activity_terminateEntryEventOccurrence = Class(name="traceSystem::Events::Activity::terminateEntryEventOccurrence")
traceSystem_Events_Activity_terminateExitEventOccurrence = Class(name="traceSystem::Events::Activity::terminateExitEventOccurrence")
traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence = Class(name="traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence")
traceSystem_Events_Activity_getInitialNodeExitEventOccurrence = Class(name="traceSystem::Events::Activity::getInitialNodeExitEventOccurrence")
traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence")
traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence")
traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence")
traceSystem_Events_ActivityNode_addTokensExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::addTokensExitEventOccurrence")
traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence")
traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence")
traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence")
traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence")
traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence")
traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence")
traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence")
traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence")
activitydiagram_TracedActivityEdge = Class(name="activitydiagram::TracedActivityEdge")
traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence")
traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence")
traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence")
traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence")
traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence = Class(name="traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence")
traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence = Class(name="traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence")
activitydiagram_TracedControlNode = Class(name="activitydiagram::TracedControlNode")
traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence")
traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence = Class(name="traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence")
traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence = Class(name="traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence")
traceSystem_Events_ActivityNode_isReadyExitEventOccurrence = Class(name="traceSystem::Events::ActivityNode::isReadyExitEventOccurrence")
traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence = Class(name="traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence")
activitydiagramConfiguration_TracedToken = Class(name="activitydiagramConfiguration::TracedToken")
traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence = Class(name="traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence")
traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence = Class(name="traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence")
activitydiagram_TracedAction = Class(name="activitydiagram::TracedAction")
traceSystem_Events_Action_sendOffers_actionExitEventOccurrence = Class(name="traceSystem::Events::Action::sendOffers::actionExitEventOccurrence")
traceSystem_Events_Action_isReady_actionEntryEventOccurrence = Class(name="traceSystem::Events::Action::isReady::actionEntryEventOccurrence")
traceSystem_Events_Action_isReady_actionExitEventOccurrence = Class(name="traceSystem::Events::Action::isReady::actionExitEventOccurrence")
activitydiagram_TracedOpaqueAction = Class(name="activitydiagram::TracedOpaqueAction")
traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence = Class(name="traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence")
traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence = Class(name="traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence")
activitydiagram_TracedInitialNode = Class(name="activitydiagram::TracedInitialNode")
traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence = Class(name="traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence")
traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence = Class(name="traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence")
traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence = Class(name="traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence")
traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence = Class(name="traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence")
activitydiagram_TracedActivityFinalNode = Class(name="activitydiagram::TracedActivityFinalNode")
traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence = Class(name="traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence")
traceSystem_Events_Action_fire_actionEntryEventOccurrence = Class(name="traceSystem::Events::Action::fire::actionEntryEventOccurrence")
traceSystem_Events_Action_fire_actionExitEventOccurrence = Class(name="traceSystem::Events::Action::fire::actionExitEventOccurrence")
traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence = Class(name="traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence")
traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence = Class(name="traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence")
activitydiagram_TracedMergeNode = Class(name="activitydiagram::TracedMergeNode")
traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence = Class(name="traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence")
traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence = Class(name="traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence")
activitydiagram_TracedDecisionNode = Class(name="activitydiagram::TracedDecisionNode")
traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence = Class(name="traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence")
traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence = Class(name="traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence")
activitydiagram_TracedIntegerVariable = Class(name="activitydiagram::TracedIntegerVariable")
traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence = Class(name="traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence")
activitydiagram_TracedForkNode = Class(name="activitydiagram::TracedForkNode")
traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence = Class(name="traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence")
traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence = Class(name="traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence")
activitydiagram_TracedStringVariable = Class(name="activitydiagram::TracedStringVariable")
traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence = Class(name="traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence")
traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence = Class(name="traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence")
traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence = Class(name="traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence")
traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence = Class(name="traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence")
activitydiagram_TracedBooleanVariable = Class(name="activitydiagram::TracedBooleanVariable")
traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence = Class(name="traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence")
Events_traceSystem_Value = Class(name="Events::traceSystem::Value")
traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence = Class(name="traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence")
traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence = Class(name="traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence")
traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence = Class(name="traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence")
traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence = Class(name="traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence")
Events_traceSystem_IntegerExpression = Class(name="Events::traceSystem::IntegerExpression")
traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence = Class(name="traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence")
traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence")
Events_traceSystem_IntegerCalculationExpression = Class(name="Events::traceSystem::IntegerCalculationExpression")
traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence")
traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence")
traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence")
traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence")
traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence = Class(name="traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence")
traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence = Class(name="traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence")
Events_traceSystem_IntegerComparisonExpression = Class(name="Events::traceSystem::IntegerComparisonExpression")
traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence")
traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence = Class(name="traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence")
traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence = Class(name="traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence")
traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence = Class(name="traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence")
Events_traceSystem_BooleanUnaryExpression = Class(name="Events::traceSystem::BooleanUnaryExpression")
traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence")
Events_traceSystem_BooleanBinaryExpression = Class(name="Events::traceSystem::BooleanBinaryExpression")
traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence")
traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence")
traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence")
traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence")
traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence = Class(name="traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence")
traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence = Class(name="traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence")
traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence = Class(name="traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence")
traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence = Class(name="traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence")
traceSystem_Events_Token_isWithdrawnEntryEventOccurrence = Class(name="traceSystem::Events::Token::isWithdrawnEntryEventOccurrence")
traceSystem_Events_Token_isWithdrawnExitEventOccurrence = Class(name="traceSystem::Events::Token::isWithdrawnExitEventOccurrence")
traceSystem_Events_Token_transferEntryEventOccurrence = Class(name="traceSystem::Events::Token::transferEntryEventOccurrence")
traceSystem_Events_Token_transferExitEventOccurrence = Class(name="traceSystem::Events::Token::transferExitEventOccurrence")
traceSystem_Events_Token_withdrawEntryEventOccurrence = Class(name="traceSystem::Events::Token::withdrawEntryEventOccurrence")
traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence = Class(name="traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence")
traceSystem_Events_Offer_hasTokensEntryEventOccurrence = Class(name="traceSystem::Events::Offer::hasTokensEntryEventOccurrence")
activitydiagramConfiguration_TracedOffer = Class(name="activitydiagramConfiguration::TracedOffer")
traceSystem_Events_Offer_hasTokensExitEventOccurrence = Class(name="traceSystem::Events::Offer::hasTokensExitEventOccurrence")
traceSystem_States_ForkedToken_baseToken_State = Class(name="traceSystem::States::ForkedToken::baseToken::State")
States_traceSystem_GlobalState = Class(name="States::traceSystem::GlobalState")
traceSystem_States_ForkedToken_remainingOffersCount_State = Class(name="traceSystem::States::ForkedToken::remainingOffersCount::State")
traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State = Class(name="traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State")
traceSystem_Events_Token_withdrawExitEventOccurrence = Class(name="traceSystem::Events::Token::withdrawExitEventOccurrence")
traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence = Class(name="traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence")
activitydiagramConfiguration_TracedForkedToken = Class(name="activitydiagramConfiguration::TracedForkedToken")
traceSystem_States_Offer_offeredTokens_State = Class(name="traceSystem::States::Offer::offeredTokens::State")
traceSystem_States_Activity_trace_State = Class(name="traceSystem::States::Activity::trace::State")
activitydiagramConfiguration_TracedTrace = Class(name="activitydiagramConfiguration::TracedTrace")
traceSystem_States_Variable_currentValue_State = Class(name="traceSystem::States::Variable::currentValue::State")
States_traceSystem_Value = Class(name="States::traceSystem::Value")
activitydiagram_TracedVariable = Class(name="activitydiagram::TracedVariable")
traceSystem_States_InputValue_value_State = Class(name="traceSystem::States::InputValue::value::State")
activitydiagramConfiguration_TracedInputValue = Class(name="activitydiagramConfiguration::TracedInputValue")
traceSystem_States_Token_holder_State = Class(name="traceSystem::States::Token::holder::State")
traceSystem_States_ActivityEdge_offers_State = Class(name="traceSystem::States::ActivityEdge::offers::State")
traceSystem_States_Trace_executedNodes_State = Class(name="traceSystem::States::Trace::executedNodes::State")
traceSystem_States_Input_inputValues_State = Class(name="traceSystem::States::Input::inputValues::State")
activitydiagramConfiguration_TracedInput = Class(name="activitydiagramConfiguration::TracedInput")
traceSystem_States_ActivityNode_heldTokens_State = Class(name="traceSystem::States::ActivityNode::heldTokens::State")
traceSystem_States_InputValue_variable_State = Class(name="traceSystem::States::InputValue::variable::State")
traceSystem_Traced_TracedObjects = Class(name="traceSystem::Traced::TracedObjects")
activitydiagram_TracedControlFlow = Class(name="activitydiagram::TracedControlFlow")
activitydiagramConfiguration_TracedControlToken = Class(name="activitydiagramConfiguration::TracedControlToken")
traceSystem_States_ActivityNode_running_State = Class(name="traceSystem::States::ActivityNode::running::State")
traceSystem_activitydiagramConfiguration_TracedInputValue = Class(name="traceSystem::activitydiagramConfiguration::TracedInputValue")
traceSystem_activitydiagramConfiguration_TracedTrace = Class(name="traceSystem::activitydiagramConfiguration::TracedTrace")
activitydiagram_TracedJoinNode = Class(name="activitydiagram::TracedJoinNode")
traceSystem_activitydiagramConfiguration_TracedForkedToken = Class(name="traceSystem::activitydiagramConfiguration::TracedForkedToken")
TracedToken = Class(name="TracedToken")
traceSystem_activitydiagramConfiguration_TracedToken = Class(name="traceSystem::activitydiagramConfiguration::TracedToken", is_abstract=True)
traceSystem_activitydiagramConfiguration_TracedControlToken = Class(name="traceSystem::activitydiagramConfiguration::TracedControlToken")
traceSystem_activitydiagramConfiguration_TracedOffer = Class(name="traceSystem::activitydiagramConfiguration::TracedOffer")
activitydiagram_traceSystem_Expression = Class(name="activitydiagram::traceSystem::Expression")
activitydiagram_traceSystem_OpaqueAction = Class(name="activitydiagram::traceSystem::OpaqueAction")
traceSystem_activitydiagram_TracedExecutableNode = Class(name="traceSystem::activitydiagram::TracedExecutableNode", is_abstract=True)
TracedActivityNode = Class(name="TracedActivityNode")
traceSystem_activitydiagram_TracedActivity = Class(name="traceSystem::activitydiagram::TracedActivity")
TracedNamedElement = Class(name="TracedNamedElement")
traceSystem_activitydiagramConfiguration_TracedInput = Class(name="traceSystem::activitydiagramConfiguration::TracedInput")
traceSystem_activitydiagram_TracedBooleanVariable = Class(name="traceSystem::activitydiagram::TracedBooleanVariable")
TracedVariable = Class(name="TracedVariable")
activitydiagram_traceSystem_BooleanVariable = Class(name="activitydiagram::traceSystem::BooleanVariable")
traceSystem_activitydiagram_TracedForkNode = Class(name="traceSystem::activitydiagram::TracedForkNode")
TracedControlNode = Class(name="TracedControlNode")
activitydiagram_traceSystem_ForkNode = Class(name="activitydiagram::traceSystem::ForkNode")
traceSystem_activitydiagram_TracedControlFlow = Class(name="traceSystem::activitydiagram::TracedControlFlow")
TracedActivityEdge = Class(name="TracedActivityEdge")
activitydiagram_traceSystem_ControlFlow = Class(name="activitydiagram::traceSystem::ControlFlow")
traceSystem_activitydiagram_TracedActivityFinalNode = Class(name="traceSystem::activitydiagram::TracedActivityFinalNode")
TracedFinalNode = Class(name="TracedFinalNode")
activitydiagram_traceSystem_ActivityFinalNode = Class(name="activitydiagram::traceSystem::ActivityFinalNode")
traceSystem_activitydiagram_TracedAction = Class(name="traceSystem::activitydiagram::TracedAction", is_abstract=True)
TracedExecutableNode = Class(name="TracedExecutableNode")
traceSystem_activitydiagram_TracedFinalNode = Class(name="traceSystem::activitydiagram::TracedFinalNode", is_abstract=True)
traceSystem_activitydiagram_TracedStringVariable = Class(name="traceSystem::activitydiagram::TracedStringVariable")
activitydiagram_traceSystem_StringVariable = Class(name="activitydiagram::traceSystem::StringVariable")
traceSystem_activitydiagram_TracedOpaqueAction = Class(name="traceSystem::activitydiagram::TracedOpaqueAction")
TracedAction = Class(name="TracedAction")
traceSystem_activitydiagram_TracedActivityEdge = Class(name="traceSystem::activitydiagram::TracedActivityEdge", is_abstract=True)
traceSystem_activitydiagram_TracedJoinNode = Class(name="traceSystem::activitydiagram::TracedJoinNode")
activitydiagram_traceSystem_JoinNode = Class(name="activitydiagram::traceSystem::JoinNode")
activitydiagram_traceSystem_Activity = Class(name="activitydiagram::traceSystem::Activity")
traceSystem_activitydiagram_TracedVariable = Class(name="traceSystem::activitydiagram::TracedVariable", is_abstract=True)
activitydiagram_traceSystem_Value = Class(name="activitydiagram::traceSystem::Value")
traceSystem_activitydiagram_TracedMergeNode = Class(name="traceSystem::activitydiagram::TracedMergeNode")
activitydiagram_traceSystem_MergeNode = Class(name="activitydiagram::traceSystem::MergeNode")
traceSystem_activitydiagram_TracedDecisionNode = Class(name="traceSystem::activitydiagram::TracedDecisionNode")
activitydiagram_traceSystem_DecisionNode = Class(name="activitydiagram::traceSystem::DecisionNode")
traceSystem_activitydiagram_TracedIntegerVariable = Class(name="traceSystem::activitydiagram::TracedIntegerVariable")
activitydiagram_traceSystem_IntegerVariable = Class(name="activitydiagram::traceSystem::IntegerVariable")
traceSystem_activitydiagram_TracedControlNode = Class(name="traceSystem::activitydiagram::TracedControlNode", is_abstract=True)
traceSystem_activitydiagram_TracedActivityNode = Class(name="traceSystem::activitydiagram::TracedActivityNode", is_abstract=True)
traceSystem_activitydiagram_TracedNamedElement = Class(name="traceSystem::activitydiagram::TracedNamedElement", is_abstract=True)
traceSystem_activitydiagram_TracedInitialNode = Class(name="traceSystem::activitydiagram::TracedInitialNode")
activitydiagram_traceSystem_InitialNode = Class(name="activitydiagram::traceSystem::InitialNode")

# traceSystem_Trace class attributes and methods

# traceSystem_GlobalState class attributes and methods

# Events class attributes and methods

# Offer_offeredTokens_State class attributes and methods

# Activity_trace_State class attributes and methods

# Variable_currentValue_State class attributes and methods

# InputValue_value_State class attributes and methods

# InputValue_variable_State class attributes and methods

# ActivityEdge_offers_State class attributes and methods

# Trace_executedNodes_State class attributes and methods

# Input_inputValues_State class attributes and methods

# ActivityNode_heldTokens_State class attributes and methods

# ActivityNode_running_State class attributes and methods

# TracedObjects class attributes and methods

# traceSystem_StaticObjectsPools class attributes and methods

# EventOccurrence class attributes and methods

# ForkedToken_baseToken_State class attributes and methods

# ForkedToken_remainingOffersCount_State class attributes and methods

# ForkedToken_baseTokenIsWithdrawn_State class attributes and methods

# Token_holder_State class attributes and methods

# Activity_mainEntryEventOccurrence class attributes and methods

# Activity_mainExitEventOccurrence class attributes and methods

# Activity_initializeEntryEventOccurrence class attributes and methods

# Activity_initializeExitEventOccurrence class attributes and methods

# Activity_runEntryEventOccurrence class attributes and methods

# Activity_runExitEventOccurrence class attributes and methods

# Activity_runNodesEntryEventOccurrence class attributes and methods

# Activity_runNodesExitEventOccurrence class attributes and methods

# Activity_fireInitialNodeEntryEventOccurrence class attributes and methods

# Activity_fireInitialNodeExitEventOccurrence class attributes and methods

# Activity_getEnabledNodesEntryEventOccurrence class attributes and methods

# traceSystem_BooleanValue class attributes and methods

# traceSystem_IntegerComparisonExpression class attributes and methods

# traceSystem_StringValue class attributes and methods

# traceSystem_BooleanBinaryExpression class attributes and methods

# traceSystem_BooleanUnaryExpression class attributes and methods

# traceSystem_IntegerValue class attributes and methods

# traceSystem_IntegerCalculationExpression class attributes and methods

# traceSystem_Events_EventOccurrence class attributes and methods

# Events_traceSystem_GlobalState class attributes and methods

# traceSystem_Events_Events class attributes and methods

# ActivityNode_run_activityNodeEntryEventOccurrence class attributes and methods

# ActivityNode_run_activityNodeExitEventOccurrence class attributes and methods

# ActivityNode_isRunningEntryEventOccurrence class attributes and methods

# ActivityNode_isRunningExitEventOccurrence class attributes and methods

# ActivityNode_terminate_activityNodeEntryEventOccurrence class attributes and methods

# ActivityNode_terminate_activityNodeExitEventOccurrence class attributes and methods

# Activity_getEnabledNodesExitEventOccurrence class attributes and methods

# Activity_selectNextNodeEntryEventOccurrence class attributes and methods

# Activity_selectNextNodeExitEventOccurrence class attributes and methods

# Activity_terminateEntryEventOccurrence class attributes and methods

# Activity_terminateExitEventOccurrence class attributes and methods

# Activity_getInitialNodeEntryEventOccurrence class attributes and methods

# Activity_getInitialNodeExitEventOccurrence class attributes and methods

# Activity_fireNodeEntryEventOccurrence class attributes and methods

# Activity_fireNodeExitEventOccurrence class attributes and methods

# ActivityNode_removeTokenExitEventOccurrence class attributes and methods

# ActivityNode_hasOffersEntryEventOccurrence class attributes and methods

# ActivityNode_hasOffersExitEventOccurrence class attributes and methods

# ActivityNode_isReadyEntryEventOccurrence class attributes and methods

# ActivityNode_isReadyExitEventOccurrence class attributes and methods

# ActivityEdge_sendOfferEntryEventOccurrence class attributes and methods

# ActivityEdge_sendOfferExitEventOccurrence class attributes and methods

# ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence class attributes and methods

# ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence class attributes and methods

# ActivityNode_sendOffersEntryEventOccurrence class attributes and methods

# ActivityNode_sendOffersExitEventOccurrence class attributes and methods

# ActivityNode_takeOfferedTokensEntryEventOccurrence class attributes and methods

# ActivityNode_takeOfferedTokensExitEventOccurrence class attributes and methods

# ActivityNode_addTokensEntryEventOccurrence class attributes and methods

# ActivityNode_addTokensExitEventOccurrence class attributes and methods

# ActivityNode_removeTokenEntryEventOccurrence class attributes and methods

# Action_sendOffers_actionExitEventOccurrence class attributes and methods

# Action_isReady_actionEntryEventOccurrence class attributes and methods

# Action_isReady_actionExitEventOccurrence class attributes and methods

# Action_fire_actionEntryEventOccurrence class attributes and methods

# Action_fire_actionExitEventOccurrence class attributes and methods

# OpaqueAction_doAction_opaqueActionEntryEventOccurrence class attributes and methods

# OpaqueAction_doAction_opaqueActionExitEventOccurrence class attributes and methods

# InitialNode_isReady_InitialNodeEntryEventOccurrence class attributes and methods

# ActivityEdge_hasOfferEntryEventOccurrence class attributes and methods

# ActivityEdge_hasOfferExitEventOccurrence class attributes and methods

# ControlNode_isReady_ControlNodeEntryEventOccurrence class attributes and methods

# ControlNode_isReady_ControlNodeExitEventOccurrence class attributes and methods

# ControlNode_fire_controlNodeEntryEventOccurrence class attributes and methods

# ControlNode_fire_controlNodeExitEventOccurrence class attributes and methods

# Action_sendOffers_actionEntryEventOccurrence class attributes and methods

# InitialNode_fire_initialNodeExitEventOccurrence class attributes and methods

# ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence class attributes and methods

# ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence class attributes and methods

# ForkNode_fire_forkNodeEntryEventOccurrence class attributes and methods

# ForkNode_fire_forkNodeExitEventOccurrence class attributes and methods

# MergeNode_hasOffers_mergeNodeEntryEventOccurrence class attributes and methods

# InitialNode_isReady_InitialNodeExitEventOccurrence class attributes and methods

# StringVariable_setCurrentValue_stringVariableEntryEventOccurrence class attributes and methods

# InitialNode_fire_initialNodeEntryEventOccurrence class attributes and methods

# StringVariable_setCurrentValue_stringVariableExitEventOccurrence class attributes and methods

# StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence class attributes and methods

# StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence class attributes and methods

# BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence class attributes and methods

# BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence class attributes and methods

# MergeNode_hasOffers_mergeNodeExitEventOccurrence class attributes and methods

# BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence class attributes and methods

# DecisionNode_fire_decisionNodeEntryEventOccurrence class attributes and methods

# DecisionNode_fire_decisionNodeExitEventOccurrence class attributes and methods

# IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence class attributes and methods

# IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence class attributes and methods

# IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence class attributes and methods

# IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateADDEntryEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateADDExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence class attributes and methods

# IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence class attributes and methods

# BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence class attributes and methods

# IntegerExpression_getOperandCurrentValuesEntryEventOccurrence class attributes and methods

# IntegerExpression_getOperandCurrentValuesExitEventOccurrence class attributes and methods

# IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateGREATERExitEventOccurrence class attributes and methods

# BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence class attributes and methods

# IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateANDEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateANDExitEventOccurrence class attributes and methods

# BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence class attributes and methods

# BooleanUnaryExpression_evaluateNOTEntryEventOccurrence class attributes and methods

# BooleanUnaryExpression_evaluateNOTExitEventOccurrence class attributes and methods

# Token_transferExitEventOccurrence class attributes and methods

# Token_withdrawEntryEventOccurrence class attributes and methods

# Token_withdrawExitEventOccurrence class attributes and methods

# ForkedToken_withdraw_forkedTokenEntryEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateOREntryEventOccurrence class attributes and methods

# ForkedToken_withdraw_forkedTokenExitEventOccurrence class attributes and methods

# BooleanBinaryExpression_evaluateORExitEventOccurrence class attributes and methods

# Offer_hasTokensEntryEventOccurrence class attributes and methods

# Token_isWithdrawnEntryEventOccurrence class attributes and methods

# Token_isWithdrawnExitEventOccurrence class attributes and methods

# Token_transferEntryEventOccurrence class attributes and methods

# Offer_hasTokensExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_mainEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivity class attributes and methods

# Events_traceSystem_EObject class attributes and methods

# traceSystem_Events_Activity_mainExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_initializeEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_initializeExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_runNodesExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_selectNextNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_runEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_runExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_runNodesEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_fireNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_fireNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityNode class attributes and methods

# traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_isRunningExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_terminateEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_terminateExitEventOccurrence class attributes and methods

# traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_Activity_getInitialNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_addTokensExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityEdge class attributes and methods

# traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence class attributes and methods

# traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedControlNode class attributes and methods

# traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence class attributes and methods

# traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence class attributes and methods

# traceSystem_Events_ActivityNode_isReadyExitEventOccurrence class attributes and methods

# traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedToken class attributes and methods

# traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence class attributes and methods

# activitydiagram_TracedAction class attributes and methods

# traceSystem_Events_Action_sendOffers_actionExitEventOccurrence class attributes and methods

# traceSystem_Events_Action_isReady_actionEntryEventOccurrence class attributes and methods

# traceSystem_Events_Action_isReady_actionExitEventOccurrence class attributes and methods

# activitydiagram_TracedOpaqueAction class attributes and methods

# traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence class attributes and methods

# traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedInitialNode class attributes and methods

# traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence class attributes and methods

# traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedActivityFinalNode class attributes and methods

# traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_Action_fire_actionEntryEventOccurrence class attributes and methods

# traceSystem_Events_Action_fire_actionExitEventOccurrence class attributes and methods

# traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence class attributes and methods

# traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedMergeNode class attributes and methods

# traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedDecisionNode class attributes and methods

# traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedIntegerVariable class attributes and methods

# traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence class attributes and methods

# activitydiagram_TracedForkNode class attributes and methods

# traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence class attributes and methods

# traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedStringVariable class attributes and methods

# traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence class attributes and methods

# traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence class attributes and methods

# traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence class attributes and methods

# activitydiagram_TracedBooleanVariable class attributes and methods

# traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence class attributes and methods

# Events_traceSystem_Value class attributes and methods

# traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence class attributes and methods

# Events_traceSystem_IntegerExpression class attributes and methods

# traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence class attributes and methods

# Events_traceSystem_IntegerCalculationExpression class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence class attributes and methods

# traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence class attributes and methods

# traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence class attributes and methods

# Events_traceSystem_IntegerComparisonExpression class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence class attributes and methods

# traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence class attributes and methods

# Events_traceSystem_BooleanUnaryExpression class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence class attributes and methods

# Events_traceSystem_BooleanBinaryExpression class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence class attributes and methods

# traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence class attributes and methods

# traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence class attributes and methods

# traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence class attributes and methods

# traceSystem_Events_Token_isWithdrawnEntryEventOccurrence class attributes and methods

# traceSystem_Events_Token_isWithdrawnExitEventOccurrence class attributes and methods

# traceSystem_Events_Token_transferEntryEventOccurrence class attributes and methods

# traceSystem_Events_Token_transferExitEventOccurrence class attributes and methods

# traceSystem_Events_Token_withdrawEntryEventOccurrence class attributes and methods

# traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence class attributes and methods

# traceSystem_Events_Offer_hasTokensEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedOffer class attributes and methods

# traceSystem_Events_Offer_hasTokensExitEventOccurrence class attributes and methods

# traceSystem_States_ForkedToken_baseToken_State class attributes and methods

# States_traceSystem_GlobalState class attributes and methods

# traceSystem_States_ForkedToken_remainingOffersCount_State class attributes and methods
traceSystem_States_ForkedToken_remainingOffersCount_State_remainingOffersCount: Property = Property(name="remainingOffersCount", type=IntegerType)
traceSystem_States_ForkedToken_remainingOffersCount_State.attributes={traceSystem_States_ForkedToken_remainingOffersCount_State_remainingOffersCount}

# traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State class attributes and methods
traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State_baseTokenIsWithdrawn: Property = Property(name="baseTokenIsWithdrawn", type=BooleanType)
traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State.attributes={traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State_baseTokenIsWithdrawn}

# traceSystem_Events_Token_withdrawExitEventOccurrence class attributes and methods

# traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence class attributes and methods

# activitydiagramConfiguration_TracedForkedToken class attributes and methods

# traceSystem_States_Offer_offeredTokens_State class attributes and methods

# traceSystem_States_Activity_trace_State class attributes and methods

# activitydiagramConfiguration_TracedTrace class attributes and methods

# traceSystem_States_Variable_currentValue_State class attributes and methods

# States_traceSystem_Value class attributes and methods

# activitydiagram_TracedVariable class attributes and methods

# traceSystem_States_InputValue_value_State class attributes and methods

# activitydiagramConfiguration_TracedInputValue class attributes and methods

# traceSystem_States_Token_holder_State class attributes and methods

# traceSystem_States_ActivityEdge_offers_State class attributes and methods

# traceSystem_States_Trace_executedNodes_State class attributes and methods

# traceSystem_States_Input_inputValues_State class attributes and methods

# activitydiagramConfiguration_TracedInput class attributes and methods

# traceSystem_States_ActivityNode_heldTokens_State class attributes and methods

# traceSystem_States_InputValue_variable_State class attributes and methods

# traceSystem_Traced_TracedObjects class attributes and methods

# activitydiagram_TracedControlFlow class attributes and methods

# activitydiagramConfiguration_TracedControlToken class attributes and methods

# traceSystem_States_ActivityNode_running_State class attributes and methods
traceSystem_States_ActivityNode_running_State_running: Property = Property(name="running", type=BooleanType)
traceSystem_States_ActivityNode_running_State.attributes={traceSystem_States_ActivityNode_running_State_running}

# traceSystem_activitydiagramConfiguration_TracedInputValue class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedTrace class attributes and methods

# activitydiagram_TracedJoinNode class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedForkedToken class attributes and methods

# TracedToken class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedToken class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedControlToken class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedOffer class attributes and methods

# activitydiagram_traceSystem_Expression class attributes and methods

# activitydiagram_traceSystem_OpaqueAction class attributes and methods

# traceSystem_activitydiagram_TracedExecutableNode class attributes and methods

# TracedActivityNode class attributes and methods

# traceSystem_activitydiagram_TracedActivity class attributes and methods

# TracedNamedElement class attributes and methods

# traceSystem_activitydiagramConfiguration_TracedInput class attributes and methods

# traceSystem_activitydiagram_TracedBooleanVariable class attributes and methods

# TracedVariable class attributes and methods

# activitydiagram_traceSystem_BooleanVariable class attributes and methods

# traceSystem_activitydiagram_TracedForkNode class attributes and methods

# TracedControlNode class attributes and methods

# activitydiagram_traceSystem_ForkNode class attributes and methods

# traceSystem_activitydiagram_TracedControlFlow class attributes and methods

# TracedActivityEdge class attributes and methods

# activitydiagram_traceSystem_ControlFlow class attributes and methods

# traceSystem_activitydiagram_TracedActivityFinalNode class attributes and methods

# TracedFinalNode class attributes and methods

# activitydiagram_traceSystem_ActivityFinalNode class attributes and methods

# traceSystem_activitydiagram_TracedAction class attributes and methods

# TracedExecutableNode class attributes and methods

# traceSystem_activitydiagram_TracedFinalNode class attributes and methods

# traceSystem_activitydiagram_TracedStringVariable class attributes and methods

# activitydiagram_traceSystem_StringVariable class attributes and methods

# traceSystem_activitydiagram_TracedOpaqueAction class attributes and methods

# TracedAction class attributes and methods

# traceSystem_activitydiagram_TracedActivityEdge class attributes and methods

# traceSystem_activitydiagram_TracedJoinNode class attributes and methods

# activitydiagram_traceSystem_JoinNode class attributes and methods

# activitydiagram_traceSystem_Activity class attributes and methods

# traceSystem_activitydiagram_TracedVariable class attributes and methods

# activitydiagram_traceSystem_Value class attributes and methods

# traceSystem_activitydiagram_TracedMergeNode class attributes and methods

# activitydiagram_traceSystem_MergeNode class attributes and methods

# traceSystem_activitydiagram_TracedDecisionNode class attributes and methods

# activitydiagram_traceSystem_DecisionNode class attributes and methods

# traceSystem_activitydiagram_TracedIntegerVariable class attributes and methods

# activitydiagram_traceSystem_IntegerVariable class attributes and methods

# traceSystem_activitydiagram_TracedControlNode class attributes and methods

# traceSystem_activitydiagram_TracedActivityNode class attributes and methods

# traceSystem_activitydiagram_TracedNamedElement class attributes and methods
traceSystem_activitydiagram_TracedNamedElement_name: Property = Property(name="name", type=StringType)
traceSystem_activitydiagram_TracedNamedElement.attributes={traceSystem_activitydiagram_TracedNamedElement_name}

# traceSystem_activitydiagram_TracedInitialNode class attributes and methods

# activitydiagram_traceSystem_InitialNode class attributes and methods

# Relationships
globalTrace0: BinaryAssociation = BinaryAssociation(
    name="globalTrace0",
    ends={
        Property(name="traceSystem_GlobalState", type=traceSystem_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Trace", type=traceSystem_GlobalState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
token_holder_States14: BinaryAssociation = BinaryAssociation(
    name="token_holder_States14",
    ends={
        Property(name="States15", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_State", type=Token_holder_State, multiplicity=Multiplicity(0, 9999))
    }
)
offer_offeredTokens_States16: BinaryAssociation = BinaryAssociation(
    name="offer_offeredTokens_States16",
    ends={
        Property(name="States17", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_State", type=Offer_offeredTokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
activity_trace_States18: BinaryAssociation = BinaryAssociation(
    name="activity_trace_States18",
    ends={
        Property(name="States19", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity_trace_State", type=Activity_trace_State, multiplicity=Multiplicity(0, 9999))
    }
)
variable_currentValue_States20: BinaryAssociation = BinaryAssociation(
    name="variable_currentValue_States20",
    ends={
        Property(name="States21", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable_currentValue_State", type=Variable_currentValue_State, multiplicity=Multiplicity(0, 9999))
    }
)
inputValue_value_States22: BinaryAssociation = BinaryAssociation(
    name="inputValue_value_States22",
    ends={
        Property(name="States23", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_value_State", type=InputValue_value_State, multiplicity=Multiplicity(0, 9999))
    }
)
inputValue_variable_States24: BinaryAssociation = BinaryAssociation(
    name="inputValue_variable_States24",
    ends={
        Property(name="States25", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_variable_State", type=InputValue_variable_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityEdge_offers_States26: BinaryAssociation = BinaryAssociation(
    name="activityEdge_offers_States26",
    ends={
        Property(name="States27", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge_offers_State", type=ActivityEdge_offers_State, multiplicity=Multiplicity(0, 9999))
    }
)
trace_executedNodes_States28: BinaryAssociation = BinaryAssociation(
    name="trace_executedNodes_States28",
    ends={
        Property(name="States29", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_executedNodes_State", type=Trace_executedNodes_State, multiplicity=Multiplicity(0, 9999))
    }
)
input_inputValues_States30: BinaryAssociation = BinaryAssociation(
    name="input_inputValues_States30",
    ends={
        Property(name="States31", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="Input_inputValues_State", type=Input_inputValues_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityNode_heldTokens_States32: BinaryAssociation = BinaryAssociation(
    name="activityNode_heldTokens_States32",
    ends={
        Property(name="States33", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_heldTokens_State", type=ActivityNode_heldTokens_State, multiplicity=Multiplicity(0, 9999))
    }
)
activityNode_running_States34: BinaryAssociation = BinaryAssociation(
    name="activityNode_running_States34",
    ends={
        Property(name="States35", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_running_State", type=ActivityNode_running_State, multiplicity=Multiplicity(0, 9999))
    }
)
events1: BinaryAssociation = BinaryAssociation(
    name="events1",
    ends={
        Property(name="Events", type=traceSystem_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Trace2", type=Events, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tracedObjects3: BinaryAssociation = BinaryAssociation(
    name="tracedObjects3",
    ends={
        Property(name="TracedObjects", type=traceSystem_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Trace4", type=TracedObjects, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
staticObjectsPools5: BinaryAssociation = BinaryAssociation(
    name="staticObjectsPools5",
    ends={
        Property(name="traceSystem_StaticObjectsPools", type=traceSystem_Trace, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Trace6", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
eventsTriggeredDuringState7: BinaryAssociation = BinaryAssociation(
    name="eventsTriggeredDuringState7",
    ends={
        Property(name="Events8", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="EventOccurrence", type=EventOccurrence, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseToken_States9: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseToken_States9",
    ends={
        Property(name="States", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_State", type=ForkedToken_baseToken_State, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_remainingOffersCount_States10: BinaryAssociation = BinaryAssociation(
    name="forkedToken_remainingOffersCount_States10",
    ends={
        Property(name="States11", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_State", type=ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(0, 9999))
    }
)
forkedToken_baseTokenIsWithdrawn_States12: BinaryAssociation = BinaryAssociation(
    name="forkedToken_baseTokenIsWithdrawn_States12",
    ends={
        Property(name="States13", type=traceSystem_GlobalState, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_State", type=ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(0, 9999))
    }
)
Activity_mainEntryEventOccurrence_Trace51: BinaryAssociation = BinaryAssociation(
    name="Activity_mainEntryEventOccurrence_Trace51",
    ends={
        Property(name="Activity_mainEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events", type=Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_mainExitEventOccurrence_Trace52: BinaryAssociation = BinaryAssociation(
    name="Activity_mainExitEventOccurrence_Trace52",
    ends={
        Property(name="Activity_mainExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events53", type=Activity_mainExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_initializeEntryEventOccurrence_Trace54: BinaryAssociation = BinaryAssociation(
    name="Activity_initializeEntryEventOccurrence_Trace54",
    ends={
        Property(name="Activity_initializeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events55", type=Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_initializeExitEventOccurrence_Trace56: BinaryAssociation = BinaryAssociation(
    name="Activity_initializeExitEventOccurrence_Trace56",
    ends={
        Property(name="Activity_initializeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events57", type=Activity_initializeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runEntryEventOccurrence_Trace58: BinaryAssociation = BinaryAssociation(
    name="Activity_runEntryEventOccurrence_Trace58",
    ends={
        Property(name="Activity_runEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events59", type=Activity_runEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runExitEventOccurrence_Trace60: BinaryAssociation = BinaryAssociation(
    name="Activity_runExitEventOccurrence_Trace60",
    ends={
        Property(name="Activity_runExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events61", type=Activity_runExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runNodesEntryEventOccurrence_Trace62: BinaryAssociation = BinaryAssociation(
    name="Activity_runNodesEntryEventOccurrence_Trace62",
    ends={
        Property(name="Activity_runNodesEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events63", type=Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_runNodesExitEventOccurrence_Trace64: BinaryAssociation = BinaryAssociation(
    name="Activity_runNodesExitEventOccurrence_Trace64",
    ends={
        Property(name="Activity_runNodesExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events65", type=Activity_runNodesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireInitialNodeEntryEventOccurrence_Trace66: BinaryAssociation = BinaryAssociation(
    name="Activity_fireInitialNodeEntryEventOccurrence_Trace66",
    ends={
        Property(name="Activity_fireInitialNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events67", type=Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireInitialNodeExitEventOccurrence_Trace68: BinaryAssociation = BinaryAssociation(
    name="Activity_fireInitialNodeExitEventOccurrence_Trace68",
    ends={
        Property(name="Activity_fireInitialNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events69", type=Activity_fireInitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_BooleanValues36: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanValues36",
    ends={
        Property(name="traceSystem_BooleanValue", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools37", type=traceSystem_BooleanValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerComparisonExpressions38: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerComparisonExpressions38",
    ends={
        Property(name="traceSystem_IntegerComparisonExpression", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools39", type=traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_StringValues40: BinaryAssociation = BinaryAssociation(
    name="pool_StringValues40",
    ends={
        Property(name="traceSystem_StringValue", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools41", type=traceSystem_StringValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_BooleanBinaryExpressions42: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanBinaryExpressions42",
    ends={
        Property(name="traceSystem_BooleanBinaryExpression", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools43", type=traceSystem_BooleanBinaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_BooleanUnaryExpressions44: BinaryAssociation = BinaryAssociation(
    name="pool_BooleanUnaryExpressions44",
    ends={
        Property(name="traceSystem_BooleanUnaryExpression", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools45", type=traceSystem_BooleanUnaryExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerValues46: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerValues46",
    ends={
        Property(name="traceSystem_IntegerValue", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools47", type=traceSystem_IntegerValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pool_IntegerCalculationExpressions48: BinaryAssociation = BinaryAssociation(
    name="pool_IntegerCalculationExpressions48",
    ends={
        Property(name="traceSystem_IntegerCalculationExpression", type=traceSystem_StaticObjectsPools, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_StaticObjectsPools49", type=traceSystem_IntegerCalculationExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateDuringWhichTriggered50: BinaryAssociation = BinaryAssociation(
    name="stateDuringWhichTriggered50",
    ends={
        Property(name="GlobalState", type=traceSystem_Events_EventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="eventsTriggeredDuringState", type=Events_traceSystem_GlobalState, multiplicity=Multiplicity(1, 1))
    }
)
Activity_fireNodeExitEventOccurrence_Trace88: BinaryAssociation = BinaryAssociation(
    name="Activity_fireNodeExitEventOccurrence_Trace88",
    ends={
        Property(name="Activity_fireNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events89", type=Activity_fireNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_run_activityNodeEntryEventOccurrence_Trace90: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_run_activityNodeEntryEventOccurrence_Trace90",
    ends={
        Property(name="ActivityNode_run_activityNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events91", type=ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_run_activityNodeExitEventOccurrence_Trace92: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_run_activityNodeExitEventOccurrence_Trace92",
    ends={
        Property(name="ActivityNode_run_activityNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events93", type=ActivityNode_run_activityNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isRunningEntryEventOccurrence_Trace94: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isRunningEntryEventOccurrence_Trace94",
    ends={
        Property(name="ActivityNode_isRunningEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events95", type=ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isRunningExitEventOccurrence_Trace96: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isRunningExitEventOccurrence_Trace96",
    ends={
        Property(name="ActivityNode_isRunningExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events97", type=ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98",
    ends={
        Property(name="ActivityNode_terminate_activityNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events99", type=ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getEnabledNodesEntryEventOccurrence_Trace70: BinaryAssociation = BinaryAssociation(
    name="Activity_getEnabledNodesEntryEventOccurrence_Trace70",
    ends={
        Property(name="Activity_getEnabledNodesEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events71", type=Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100",
    ends={
        Property(name="ActivityNode_terminate_activityNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events101", type=ActivityNode_terminate_activityNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getEnabledNodesExitEventOccurrence_Trace72: BinaryAssociation = BinaryAssociation(
    name="Activity_getEnabledNodesExitEventOccurrence_Trace72",
    ends={
        Property(name="Activity_getEnabledNodesExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events73", type=Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_selectNextNodeEntryEventOccurrence_Trace74: BinaryAssociation = BinaryAssociation(
    name="Activity_selectNextNodeEntryEventOccurrence_Trace74",
    ends={
        Property(name="Activity_selectNextNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events75", type=Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_selectNextNodeExitEventOccurrence_Trace76: BinaryAssociation = BinaryAssociation(
    name="Activity_selectNextNodeExitEventOccurrence_Trace76",
    ends={
        Property(name="Activity_selectNextNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events77", type=Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_terminateEntryEventOccurrence_Trace78: BinaryAssociation = BinaryAssociation(
    name="Activity_terminateEntryEventOccurrence_Trace78",
    ends={
        Property(name="Activity_terminateEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events79", type=Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_terminateExitEventOccurrence_Trace80: BinaryAssociation = BinaryAssociation(
    name="Activity_terminateExitEventOccurrence_Trace80",
    ends={
        Property(name="Activity_terminateExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events81", type=Activity_terminateExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getInitialNodeEntryEventOccurrence_Trace82: BinaryAssociation = BinaryAssociation(
    name="Activity_getInitialNodeEntryEventOccurrence_Trace82",
    ends={
        Property(name="Activity_getInitialNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events83", type=Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_getInitialNodeExitEventOccurrence_Trace84: BinaryAssociation = BinaryAssociation(
    name="Activity_getInitialNodeExitEventOccurrence_Trace84",
    ends={
        Property(name="Activity_getInitialNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events85", type=Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Activity_fireNodeEntryEventOccurrence_Trace86: BinaryAssociation = BinaryAssociation(
    name="Activity_fireNodeEntryEventOccurrence_Trace86",
    ends={
        Property(name="Activity_fireNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events87", type=Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_removeTokenExitEventOccurrence_Trace116: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_removeTokenExitEventOccurrence_Trace116",
    ends={
        Property(name="ActivityNode_removeTokenExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events117", type=ActivityNode_removeTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_hasOffersEntryEventOccurrence_Trace118: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_hasOffersEntryEventOccurrence_Trace118",
    ends={
        Property(name="ActivityNode_hasOffersEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events119", type=ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_hasOffersExitEventOccurrence_Trace120: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_hasOffersExitEventOccurrence_Trace120",
    ends={
        Property(name="ActivityNode_hasOffersExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events121", type=ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isReadyEntryEventOccurrence_Trace122: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isReadyEntryEventOccurrence_Trace122",
    ends={
        Property(name="ActivityNode_isReadyEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events123", type=ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_isReadyExitEventOccurrence_Trace124: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_isReadyExitEventOccurrence_Trace124",
    ends={
        Property(name="ActivityNode_isReadyExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events125", type=ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_sendOfferEntryEventOccurrence_Trace126: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_sendOfferEntryEventOccurrence_Trace126",
    ends={
        Property(name="ActivityEdge_sendOfferEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events127", type=ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_sendOfferExitEventOccurrence_Trace128: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_sendOfferExitEventOccurrence_Trace128",
    ends={
        Property(name="ActivityEdge_sendOfferExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events129", type=ActivityEdge_sendOfferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events131", type=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events133", type=ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_sendOffersEntryEventOccurrence_Trace102: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_sendOffersEntryEventOccurrence_Trace102",
    ends={
        Property(name="ActivityNode_sendOffersEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events103", type=ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_sendOffersExitEventOccurrence_Trace104: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_sendOffersExitEventOccurrence_Trace104",
    ends={
        Property(name="ActivityNode_sendOffersExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events105", type=ActivityNode_sendOffersExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106",
    ends={
        Property(name="ActivityNode_takeOfferedTokensEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events107", type=ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108",
    ends={
        Property(name="ActivityNode_takeOfferedTokensExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events109", type=ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_addTokensEntryEventOccurrence_Trace110: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_addTokensEntryEventOccurrence_Trace110",
    ends={
        Property(name="ActivityNode_addTokensEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events111", type=ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_addTokensExitEventOccurrence_Trace112: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_addTokensExitEventOccurrence_Trace112",
    ends={
        Property(name="ActivityNode_addTokensExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events113", type=ActivityNode_addTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityNode_removeTokenEntryEventOccurrence_Trace114: BinaryAssociation = BinaryAssociation(
    name="ActivityNode_removeTokenEntryEventOccurrence_Trace114",
    ends={
        Property(name="ActivityNode_removeTokenEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events115", type=ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_sendOffers_actionExitEventOccurrence_Trace148: BinaryAssociation = BinaryAssociation(
    name="Action_sendOffers_actionExitEventOccurrence_Trace148",
    ends={
        Property(name="Action_sendOffers_actionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events149", type=Action_sendOffers_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_isReady_actionEntryEventOccurrence_Trace150: BinaryAssociation = BinaryAssociation(
    name="Action_isReady_actionEntryEventOccurrence_Trace150",
    ends={
        Property(name="Action_isReady_actionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events151", type=Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_isReady_actionExitEventOccurrence_Trace152: BinaryAssociation = BinaryAssociation(
    name="Action_isReady_actionExitEventOccurrence_Trace152",
    ends={
        Property(name="Action_isReady_actionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events153", type=Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_fire_actionEntryEventOccurrence_Trace154: BinaryAssociation = BinaryAssociation(
    name="Action_fire_actionEntryEventOccurrence_Trace154",
    ends={
        Property(name="Action_fire_actionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events155", type=Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_fire_actionExitEventOccurrence_Trace156: BinaryAssociation = BinaryAssociation(
    name="Action_fire_actionExitEventOccurrence_Trace156",
    ends={
        Property(name="Action_fire_actionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events157", type=Action_fire_actionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158: BinaryAssociation = BinaryAssociation(
    name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events159", type=OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160: BinaryAssociation = BinaryAssociation(
    name="OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events161", type=OpaqueAction_doAction_opaqueActionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162: BinaryAssociation = BinaryAssociation(
    name="InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162",
    ends={
        Property(name="InitialNode_isReady_InitialNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events163", type=InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_hasOfferEntryEventOccurrence_Trace134: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_hasOfferEntryEventOccurrence_Trace134",
    ends={
        Property(name="ActivityEdge_hasOfferEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events135", type=ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityEdge_hasOfferExitEventOccurrence_Trace136: BinaryAssociation = BinaryAssociation(
    name="ActivityEdge_hasOfferExitEventOccurrence_Trace136",
    ends={
        Property(name="ActivityEdge_hasOfferExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events137", type=ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138: BinaryAssociation = BinaryAssociation(
    name="ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138",
    ends={
        Property(name="ControlNode_isReady_ControlNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events139", type=ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140: BinaryAssociation = BinaryAssociation(
    name="ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140",
    ends={
        Property(name="ControlNode_isReady_ControlNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events141", type=ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_fire_controlNodeEntryEventOccurrence_Trace142: BinaryAssociation = BinaryAssociation(
    name="ControlNode_fire_controlNodeEntryEventOccurrence_Trace142",
    ends={
        Property(name="ControlNode_fire_controlNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events143", type=ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ControlNode_fire_controlNodeExitEventOccurrence_Trace144: BinaryAssociation = BinaryAssociation(
    name="ControlNode_fire_controlNodeExitEventOccurrence_Trace144",
    ends={
        Property(name="ControlNode_fire_controlNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events145", type=ControlNode_fire_controlNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Action_sendOffers_actionEntryEventOccurrence_Trace146: BinaryAssociation = BinaryAssociation(
    name="Action_sendOffers_actionEntryEventOccurrence_Trace146",
    ends={
        Property(name="Action_sendOffers_actionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events147", type=Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_fire_initialNodeExitEventOccurrence_Trace168: BinaryAssociation = BinaryAssociation(
    name="InitialNode_fire_initialNodeExitEventOccurrence_Trace168",
    ends={
        Property(name="InitialNode_fire_initialNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events169", type=InitialNode_fire_initialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170: BinaryAssociation = BinaryAssociation(
    name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events171", type=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172: BinaryAssociation = BinaryAssociation(
    name="ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events173", type=ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkNode_fire_forkNodeEntryEventOccurrence_Trace174: BinaryAssociation = BinaryAssociation(
    name="ForkNode_fire_forkNodeEntryEventOccurrence_Trace174",
    ends={
        Property(name="ForkNode_fire_forkNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events175", type=ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkNode_fire_forkNodeExitEventOccurrence_Trace176: BinaryAssociation = BinaryAssociation(
    name="ForkNode_fire_forkNodeExitEventOccurrence_Trace176",
    ends={
        Property(name="ForkNode_fire_forkNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events177", type=ForkNode_fire_forkNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178: BinaryAssociation = BinaryAssociation(
    name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events179", type=MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164: BinaryAssociation = BinaryAssociation(
    name="InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164",
    ends={
        Property(name="InitialNode_isReady_InitialNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events165", type=InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194: BinaryAssociation = BinaryAssociation(
    name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events195", type=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
InitialNode_fire_initialNodeEntryEventOccurrence_Trace166: BinaryAssociation = BinaryAssociation(
    name="InitialNode_fire_initialNodeEntryEventOccurrence_Trace166",
    ends={
        Property(name="InitialNode_fire_initialNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events167", type=InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196: BinaryAssociation = BinaryAssociation(
    name="StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events197", type=StringVariable_setCurrentValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198: BinaryAssociation = BinaryAssociation(
    name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events199", type=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200: BinaryAssociation = BinaryAssociation(
    name="StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events201", type=StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events203", type=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events205", type=BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180: BinaryAssociation = BinaryAssociation(
    name="MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events181", type=MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events207", type=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182: BinaryAssociation = BinaryAssociation(
    name="DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182",
    ends={
        Property(name="DecisionNode_fire_decisionNodeEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events183", type=DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184: BinaryAssociation = BinaryAssociation(
    name="DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184",
    ends={
        Property(name="DecisionNode_fire_decisionNodeExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events185", type=DecisionNode_fire_decisionNodeExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events187", type=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events189", type=IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events191", type=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192: BinaryAssociation = BinaryAssociation(
    name="IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events193", type=IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events217", type=IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events219", type=IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events221", type=IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events223", type=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events225", type=IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events227", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events229", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208: BinaryAssociation = BinaryAssociation(
    name="BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events209", type=BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210: BinaryAssociation = BinaryAssociation(
    name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events211", type=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212: BinaryAssociation = BinaryAssociation(
    name="IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events213", type=IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214: BinaryAssociation = BinaryAssociation(
    name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events215", type=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events241", type=IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events243", type=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events245", type=IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events247", type=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATERExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events249", type=IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events251", type=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events231", type=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events233", type=IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events235", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events237", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238: BinaryAssociation = BinaryAssociation(
    name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events239", type=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events259", type=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events261", type=BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events263", type=BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events265", type=BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events253", type=BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events255", type=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256: BinaryAssociation = BinaryAssociation(
    name="BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events257", type=BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_transferExitEventOccurrence_Trace276: BinaryAssociation = BinaryAssociation(
    name="Token_transferExitEventOccurrence_Trace276",
    ends={
        Property(name="Token_transferExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events277", type=Token_transferExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_withdrawEntryEventOccurrence_Trace278: BinaryAssociation = BinaryAssociation(
    name="Token_withdrawEntryEventOccurrence_Trace278",
    ends={
        Property(name="Token_withdrawEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events279", type=Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_withdrawExitEventOccurrence_Trace280: BinaryAssociation = BinaryAssociation(
    name="Token_withdrawExitEventOccurrence_Trace280",
    ends={
        Property(name="Token_withdrawExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events281", type=Token_withdrawExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282: BinaryAssociation = BinaryAssociation(
    name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events283", type=ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266",
    ends={
        Property(name="BooleanBinaryExpression_evaluateOREntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events267", type=BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284: BinaryAssociation = BinaryAssociation(
    name="ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events285", type=ForkedToken_withdraw_forkedTokenExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268: BinaryAssociation = BinaryAssociation(
    name="BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268",
    ends={
        Property(name="BooleanBinaryExpression_evaluateORExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events269", type=BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_isWithdrawnEntryEventOccurrence_Trace270: BinaryAssociation = BinaryAssociation(
    name="Token_isWithdrawnEntryEventOccurrence_Trace270",
    ends={
        Property(name="Token_isWithdrawnEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events271", type=Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_isWithdrawnExitEventOccurrence_Trace272: BinaryAssociation = BinaryAssociation(
    name="Token_isWithdrawnExitEventOccurrence_Trace272",
    ends={
        Property(name="Token_isWithdrawnExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events273", type=Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Token_transferEntryEventOccurrence_Trace274: BinaryAssociation = BinaryAssociation(
    name="Token_transferEntryEventOccurrence_Trace274",
    ends={
        Property(name="Token_transferEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events275", type=Token_transferEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
Offer_hasTokensExitEventOccurrence_Trace288: BinaryAssociation = BinaryAssociation(
    name="Offer_hasTokensExitEventOccurrence_Trace288",
    ends={
        Property(name="Offer_hasTokensExitEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events289", type=Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thisParam290: BinaryAssociation = BinaryAssociation(
    name="thisParam290",
    ends={
        Property(name="activitydiagram_TracedActivity", type=traceSystem_Events_Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_mainEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inputValuesParam291: BinaryAssociation = BinaryAssociation(
    name="inputValuesParam291",
    ends={
        Property(name="Events_traceSystem_EObject", type=traceSystem_Events_Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_mainEntryEventOccurrence292", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent293: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent293",
    ends={
        Property(name="Activity_mainEntryEventOccurrence294", type=traceSystem_Events_Activity_mainExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_mainExitEventOccurrence", type=Activity_mainEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam295: BinaryAssociation = BinaryAssociation(
    name="thisParam295",
    ends={
        Property(name="activitydiagram_TracedActivity296", type=traceSystem_Events_Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_initializeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
inputValuesParam297: BinaryAssociation = BinaryAssociation(
    name="inputValuesParam297",
    ends={
        Property(name="Events_traceSystem_EObject299", type=traceSystem_Events_Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_initializeEntryEventOccurrence298", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent300: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent300",
    ends={
        Property(name="Activity_initializeEntryEventOccurrence301", type=traceSystem_Events_Activity_initializeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_initializeExitEventOccurrence", type=Activity_initializeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
Offer_hasTokensEntryEventOccurrence_Trace286: BinaryAssociation = BinaryAssociation(
    name="Offer_hasTokensEntryEventOccurrence_Trace286",
    ends={
        Property(name="Offer_hasTokensEntryEventOccurrence", type=traceSystem_Events_Events, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Events287", type=Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
correspondingEntryEvent308: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent308",
    ends={
        Property(name="Activity_runNodesEntryEventOccurrence309", type=traceSystem_Events_Activity_runNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_runNodesExitEventOccurrence", type=Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam310: BinaryAssociation = BinaryAssociation(
    name="thisParam310",
    ends={
        Property(name="activitydiagram_TracedActivity311", type=traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent312: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent312",
    ends={
        Property(name="Activity_fireInitialNodeEntryEventOccurrence313", type=traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence", type=Activity_fireInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam314: BinaryAssociation = BinaryAssociation(
    name="thisParam314",
    ends={
        Property(name="activitydiagram_TracedActivity315", type=traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent316: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent316",
    ends={
        Property(name="Activity_getEnabledNodesEntryEventOccurrence317", type=traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence", type=Activity_getEnabledNodesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
enabledNodesReturn318: BinaryAssociation = BinaryAssociation(
    name="enabledNodesReturn318",
    ends={
        Property(name="Events_traceSystem_EObject320", type=traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence319", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam321: BinaryAssociation = BinaryAssociation(
    name="thisParam321",
    ends={
        Property(name="activitydiagram_TracedActivity322", type=traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
activityNodesParam323: BinaryAssociation = BinaryAssociation(
    name="activityNodesParam323",
    ends={
        Property(name="Events_traceSystem_EObject325", type=traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence324", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent326: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent326",
    ends={
        Property(name="Activity_selectNextNodeEntryEventOccurrence327", type=traceSystem_Events_Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_selectNextNodeExitEventOccurrence", type=Activity_selectNextNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam302: BinaryAssociation = BinaryAssociation(
    name="thisParam302",
    ends={
        Property(name="activitydiagram_TracedActivity303", type=traceSystem_Events_Activity_runEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_runEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent304: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent304",
    ends={
        Property(name="Activity_runEntryEventOccurrence305", type=traceSystem_Events_Activity_runExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_runExitEventOccurrence", type=Activity_runEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam306: BinaryAssociation = BinaryAssociation(
    name="thisParam306",
    ends={
        Property(name="activitydiagram_TracedActivity307", type=traceSystem_Events_Activity_runNodesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_runNodesEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
initialNodeReturn339: BinaryAssociation = BinaryAssociation(
    name="initialNodeReturn339",
    ends={
        Property(name="Events_traceSystem_EObject341", type=traceSystem_Events_Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getInitialNodeExitEventOccurrence340", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam342: BinaryAssociation = BinaryAssociation(
    name="thisParam342",
    ends={
        Property(name="activitydiagram_TracedActivity343", type=traceSystem_Events_Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_fireNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
nodeParam344: BinaryAssociation = BinaryAssociation(
    name="nodeParam344",
    ends={
        Property(name="Events_traceSystem_EObject346", type=traceSystem_Events_Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_fireNodeEntryEventOccurrence345", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent347: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent347",
    ends={
        Property(name="Activity_fireNodeEntryEventOccurrence348", type=traceSystem_Events_Activity_fireNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_fireNodeExitEventOccurrence", type=Activity_fireNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam349: BinaryAssociation = BinaryAssociation(
    name="thisParam349",
    ends={
        Property(name="activitydiagram_TracedActivityNode", type=traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent350: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent350",
    ends={
        Property(name="ActivityNode_run_activityNodeEntryEventOccurrence351", type=traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence", type=ActivityNode_run_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam352: BinaryAssociation = BinaryAssociation(
    name="thisParam352",
    ends={
        Property(name="activitydiagram_TracedActivityNode353", type=traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent354: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent354",
    ends={
        Property(name="ActivityNode_isRunningEntryEventOccurrence355", type=traceSystem_Events_ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isRunningExitEventOccurrence", type=ActivityNode_isRunningEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isRunningReturn356: BinaryAssociation = BinaryAssociation(
    name="isRunningReturn356",
    ends={
        Property(name="Events_traceSystem_EObject358", type=traceSystem_Events_ActivityNode_isRunningExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isRunningExitEventOccurrence357", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
selectedNodeReturn328: BinaryAssociation = BinaryAssociation(
    name="selectedNodeReturn328",
    ends={
        Property(name="Events_traceSystem_EObject330", type=traceSystem_Events_Activity_selectNextNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_selectNextNodeExitEventOccurrence329", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam331: BinaryAssociation = BinaryAssociation(
    name="thisParam331",
    ends={
        Property(name="activitydiagram_TracedActivity332", type=traceSystem_Events_Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_terminateEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent333: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent333",
    ends={
        Property(name="Activity_terminateEntryEventOccurrence334", type=traceSystem_Events_Activity_terminateExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_terminateExitEventOccurrence", type=Activity_terminateEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam335: BinaryAssociation = BinaryAssociation(
    name="thisParam335",
    ends={
        Property(name="activitydiagram_TracedActivity336", type=traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent337: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent337",
    ends={
        Property(name="Activity_getInitialNodeEntryEventOccurrence338", type=traceSystem_Events_Activity_getInitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Activity_getInitialNodeExitEventOccurrence", type=Activity_getInitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam370: BinaryAssociation = BinaryAssociation(
    name="thisParam370",
    ends={
        Property(name="activitydiagram_TracedActivityNode371", type=traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent372: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent372",
    ends={
        Property(name="ActivityNode_takeOfferedTokensEntryEventOccurrence373", type=traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence", type=ActivityNode_takeOfferedTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensReturn374: BinaryAssociation = BinaryAssociation(
    name="tokensReturn374",
    ends={
        Property(name="Events_traceSystem_EObject376", type=traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence375", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam377: BinaryAssociation = BinaryAssociation(
    name="thisParam377",
    ends={
        Property(name="activitydiagram_TracedActivityNode378", type=traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam379: BinaryAssociation = BinaryAssociation(
    name="tokensParam379",
    ends={
        Property(name="Events_traceSystem_EObject381", type=traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence380", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent382: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent382",
    ends={
        Property(name="ActivityNode_addTokensEntryEventOccurrence383", type=traceSystem_Events_ActivityNode_addTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_addTokensExitEventOccurrence", type=ActivityNode_addTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam384: BinaryAssociation = BinaryAssociation(
    name="thisParam384",
    ends={
        Property(name="activitydiagram_TracedActivityNode385", type=traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
tokenParam386: BinaryAssociation = BinaryAssociation(
    name="tokenParam386",
    ends={
        Property(name="Events_traceSystem_EObject388", type=traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence387", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent389: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent389",
    ends={
        Property(name="ActivityNode_removeTokenEntryEventOccurrence390", type=traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence", type=ActivityNode_removeTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam359: BinaryAssociation = BinaryAssociation(
    name="thisParam359",
    ends={
        Property(name="activitydiagram_TracedActivityNode360", type=traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent361: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent361",
    ends={
        Property(name="ActivityNode_terminate_activityNodeEntryEventOccurrence362", type=traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence", type=ActivityNode_terminate_activityNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam363: BinaryAssociation = BinaryAssociation(
    name="thisParam363",
    ends={
        Property(name="activitydiagram_TracedActivityNode364", type=traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam365: BinaryAssociation = BinaryAssociation(
    name="tokensParam365",
    ends={
        Property(name="Events_traceSystem_EObject367", type=traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence366", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 9999))
    }
)
correspondingEntryEvent368: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent368",
    ends={
        Property(name="ActivityNode_sendOffersEntryEventOccurrence369", type=traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence", type=ActivityNode_sendOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam405: BinaryAssociation = BinaryAssociation(
    name="thisParam405",
    ends={
        Property(name="activitydiagram_TracedActivityEdge", type=traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam406: BinaryAssociation = BinaryAssociation(
    name="tokensParam406",
    ends={
        Property(name="Events_traceSystem_EObject408", type=traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence407", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent409: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent409",
    ends={
        Property(name="ActivityEdge_sendOfferEntryEventOccurrence410", type=traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence", type=ActivityEdge_sendOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam411: BinaryAssociation = BinaryAssociation(
    name="thisParam411",
    ends={
        Property(name="activitydiagram_TracedActivityEdge412", type=traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent413: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent413",
    ends={
        Property(name="ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence414", type=traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence", type=ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensReturn415: BinaryAssociation = BinaryAssociation(
    name="tokensReturn415",
    ends={
        Property(name="Events_traceSystem_EObject417", type=traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence416", type=Events_traceSystem_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
thisParam418: BinaryAssociation = BinaryAssociation(
    name="thisParam418",
    ends={
        Property(name="activitydiagram_TracedActivityEdge419", type=traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent420: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent420",
    ends={
        Property(name="ActivityEdge_hasOfferEntryEventOccurrence421", type=traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence", type=ActivityEdge_hasOfferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
hasOfferReturn422: BinaryAssociation = BinaryAssociation(
    name="hasOfferReturn422",
    ends={
        Property(name="Events_traceSystem_EObject424", type=traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence423", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam391: BinaryAssociation = BinaryAssociation(
    name="thisParam391",
    ends={
        Property(name="activitydiagram_TracedActivityNode392", type=traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
thisParam425: BinaryAssociation = BinaryAssociation(
    name="thisParam425",
    ends={
        Property(name="activitydiagram_TracedControlNode", type=traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence", type=activitydiagram_TracedControlNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent393: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent393",
    ends={
        Property(name="ActivityNode_hasOffersEntryEventOccurrence394", type=traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence", type=ActivityNode_hasOffersEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn395: BinaryAssociation = BinaryAssociation(
    name="returnReturn395",
    ends={
        Property(name="Events_traceSystem_EObject397", type=traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence396", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam398: BinaryAssociation = BinaryAssociation(
    name="thisParam398",
    ends={
        Property(name="activitydiagram_TracedActivityNode399", type=traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent400: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent400",
    ends={
        Property(name="ActivityNode_isReadyEntryEventOccurrence401", type=traceSystem_Events_ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isReadyExitEventOccurrence", type=ActivityNode_isReadyEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn402: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn402",
    ends={
        Property(name="Events_traceSystem_EObject404", type=traceSystem_Events_ActivityNode_isReadyExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityNode_isReadyExitEventOccurrence403", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam431: BinaryAssociation = BinaryAssociation(
    name="thisParam431",
    ends={
        Property(name="activitydiagram_TracedControlNode432", type=traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence", type=activitydiagram_TracedControlNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam433: BinaryAssociation = BinaryAssociation(
    name="tokensParam433",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken", type=traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence434", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent435: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent435",
    ends={
        Property(name="ControlNode_fire_controlNodeEntryEventOccurrence436", type=traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence", type=ControlNode_fire_controlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam437: BinaryAssociation = BinaryAssociation(
    name="thisParam437",
    ends={
        Property(name="activitydiagram_TracedAction", type=traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent438: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent438",
    ends={
        Property(name="Action_sendOffers_actionEntryEventOccurrence439", type=traceSystem_Events_Action_sendOffers_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_sendOffers_actionExitEventOccurrence", type=Action_sendOffers_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam440: BinaryAssociation = BinaryAssociation(
    name="thisParam440",
    ends={
        Property(name="activitydiagram_TracedAction441", type=traceSystem_Events_Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_isReady_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent442: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent442",
    ends={
        Property(name="Action_isReady_actionEntryEventOccurrence443", type=traceSystem_Events_Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_isReady_actionExitEventOccurrence", type=Action_isReady_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn444: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn444",
    ends={
        Property(name="Events_traceSystem_EObject446", type=traceSystem_Events_Action_isReady_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_isReady_actionExitEventOccurrence445", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent426: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent426",
    ends={
        Property(name="ControlNode_isReady_ControlNodeEntryEventOccurrence427", type=traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence", type=ControlNode_isReady_ControlNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam454: BinaryAssociation = BinaryAssociation(
    name="thisParam454",
    ends={
        Property(name="activitydiagram_TracedOpaqueAction", type=traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence", type=activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn428: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn428",
    ends={
        Property(name="Events_traceSystem_EObject430", type=traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence429", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent455: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent455",
    ends={
        Property(name="OpaqueAction_doAction_opaqueActionEntryEventOccurrence456", type=traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence", type=OpaqueAction_doAction_opaqueActionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam457: BinaryAssociation = BinaryAssociation(
    name="thisParam457",
    ends={
        Property(name="activitydiagram_TracedInitialNode", type=traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent458: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent458",
    ends={
        Property(name="InitialNode_isReady_InitialNodeEntryEventOccurrence459", type=traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence", type=InitialNode_isReady_InitialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isReadyReturn460: BinaryAssociation = BinaryAssociation(
    name="isReadyReturn460",
    ends={
        Property(name="Events_traceSystem_EObject462", type=traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence461", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam463: BinaryAssociation = BinaryAssociation(
    name="thisParam463",
    ends={
        Property(name="activitydiagram_TracedInitialNode464", type=traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam465: BinaryAssociation = BinaryAssociation(
    name="tokensParam465",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken467", type=traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence466", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent468: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent468",
    ends={
        Property(name="InitialNode_fire_initialNodeEntryEventOccurrence469", type=traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence", type=InitialNode_fire_initialNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam470: BinaryAssociation = BinaryAssociation(
    name="thisParam470",
    ends={
        Property(name="activitydiagram_TracedActivityFinalNode", type=traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence", type=activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam471: BinaryAssociation = BinaryAssociation(
    name="tokensParam471",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken473", type=traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence472", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent474: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent474",
    ends={
        Property(name="ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence475", type=traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence", type=ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam447: BinaryAssociation = BinaryAssociation(
    name="thisParam447",
    ends={
        Property(name="activitydiagram_TracedAction448", type=traceSystem_Events_Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_fire_actionEntryEventOccurrence", type=activitydiagram_TracedAction, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam449: BinaryAssociation = BinaryAssociation(
    name="tokensParam449",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken451", type=traceSystem_Events_Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_fire_actionEntryEventOccurrence450", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent452: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent452",
    ends={
        Property(name="Action_fire_actionEntryEventOccurrence453", type=traceSystem_Events_Action_fire_actionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Action_fire_actionExitEventOccurrence", type=Action_fire_actionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam482: BinaryAssociation = BinaryAssociation(
    name="thisParam482",
    ends={
        Property(name="activitydiagram_TracedMergeNode", type=traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence", type=activitydiagram_TracedMergeNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent483: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent483",
    ends={
        Property(name="MergeNode_hasOffers_mergeNodeEntryEventOccurrence484", type=traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence", type=MergeNode_hasOffers_mergeNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
returnReturn485: BinaryAssociation = BinaryAssociation(
    name="returnReturn485",
    ends={
        Property(name="Events_traceSystem_EObject487", type=traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence486", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam488: BinaryAssociation = BinaryAssociation(
    name="thisParam488",
    ends={
        Property(name="activitydiagram_TracedDecisionNode", type=traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence", type=activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam489: BinaryAssociation = BinaryAssociation(
    name="tokensParam489",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken491", type=traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence490", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
correspondingEntryEvent492: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent492",
    ends={
        Property(name="DecisionNode_fire_decisionNodeEntryEventOccurrence493", type=traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence", type=DecisionNode_fire_decisionNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam476: BinaryAssociation = BinaryAssociation(
    name="thisParam476",
    ends={
        Property(name="activitydiagram_TracedForkNode", type=traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence", type=activitydiagram_TracedForkNode, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent501: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent501",
    ends={
        Property(name="IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence502", type=traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence", type=IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
tokensParam477: BinaryAssociation = BinaryAssociation(
    name="tokensParam477",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken479", type=traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence478", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
valueReturn503: BinaryAssociation = BinaryAssociation(
    name="valueReturn503",
    ends={
        Property(name="Events_traceSystem_EObject505", type=traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence504", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent480: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent480",
    ends={
        Property(name="ForkNode_fire_forkNodeEntryEventOccurrence481", type=traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence", type=ForkNode_fire_forkNodeEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam506: BinaryAssociation = BinaryAssociation(
    name="thisParam506",
    ends={
        Property(name="activitydiagram_TracedStringVariable", type=traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 1))
    }
)
valueParam507: BinaryAssociation = BinaryAssociation(
    name="valueParam507",
    ends={
        Property(name="Events_traceSystem_Value509", type=traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence508", type=Events_traceSystem_Value, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent510: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent510",
    ends={
        Property(name="StringVariable_setCurrentValue_stringVariableEntryEventOccurrence511", type=traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence", type=StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam512: BinaryAssociation = BinaryAssociation(
    name="thisParam512",
    ends={
        Property(name="activitydiagram_TracedStringVariable513", type=traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent514: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent514",
    ends={
        Property(name="StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence515", type=traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence", type=StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
valueReturn516: BinaryAssociation = BinaryAssociation(
    name="valueReturn516",
    ends={
        Property(name="Events_traceSystem_EObject518", type=traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence517", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam519: BinaryAssociation = BinaryAssociation(
    name="thisParam519",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable", type=traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
valueParam520: BinaryAssociation = BinaryAssociation(
    name="valueParam520",
    ends={
        Property(name="Events_traceSystem_Value522", type=traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence521", type=Events_traceSystem_Value, multiplicity=Multiplicity(1, 1))
    }
)
thisParam494: BinaryAssociation = BinaryAssociation(
    name="thisParam494",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable", type=traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
valueParam495: BinaryAssociation = BinaryAssociation(
    name="valueParam495",
    ends={
        Property(name="Events_traceSystem_Value", type=traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence496", type=Events_traceSystem_Value, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent523: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent523",
    ends={
        Property(name="BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence524", type=traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence", type=BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent497: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent497",
    ends={
        Property(name="IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence498", type=traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence", type=IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam499: BinaryAssociation = BinaryAssociation(
    name="thisParam499",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable500", type=traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
thisParam532: BinaryAssociation = BinaryAssociation(
    name="thisParam532",
    ends={
        Property(name="Events_traceSystem_IntegerExpression", type=traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence", type=Events_traceSystem_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent533: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent533",
    ends={
        Property(name="IntegerExpression_getOperandCurrentValuesEntryEventOccurrence534", type=traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence", type=IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
operand1ValueReturn535: BinaryAssociation = BinaryAssociation(
    name="operand1ValueReturn535",
    ends={
        Property(name="Events_traceSystem_EObject537", type=traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence536", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
operand2ValueReturn538: BinaryAssociation = BinaryAssociation(
    name="operand2ValueReturn538",
    ends={
        Property(name="Events_traceSystem_EObject540", type=traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence539", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam541: BinaryAssociation = BinaryAssociation(
    name="thisParam541",
    ends={
        Property(name="Events_traceSystem_IntegerCalculationExpression", type=traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence", type=Events_traceSystem_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent542: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent542",
    ends={
        Property(name="IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence543", type=traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence", type=IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam544: BinaryAssociation = BinaryAssociation(
    name="thisParam544",
    ends={
        Property(name="Events_traceSystem_IntegerCalculationExpression545", type=traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence", type=Events_traceSystem_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent546: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent546",
    ends={
        Property(name="IntegerCalculationExpression_evaluateADDEntryEventOccurrence547", type=traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence", type=IntegerCalculationExpression_evaluateADDEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn548: BinaryAssociation = BinaryAssociation(
    name="resultReturn548",
    ends={
        Property(name="Events_traceSystem_EObject550", type=traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence549", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam525: BinaryAssociation = BinaryAssociation(
    name="thisParam525",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable526", type=traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent527: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent527",
    ends={
        Property(name="BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence528", type=traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence", type=BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
valueReturn529: BinaryAssociation = BinaryAssociation(
    name="valueReturn529",
    ends={
        Property(name="Events_traceSystem_EObject531", type=traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence530", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam558: BinaryAssociation = BinaryAssociation(
    name="thisParam558",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression", type=traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent559: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent559",
    ends={
        Property(name="IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence560", type=traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence", type=IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam561: BinaryAssociation = BinaryAssociation(
    name="thisParam561",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression562", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent563: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent563",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence564", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence", type=IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn565: BinaryAssociation = BinaryAssociation(
    name="resultReturn565",
    ends={
        Property(name="Events_traceSystem_EObject567", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence566", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam568: BinaryAssociation = BinaryAssociation(
    name="thisParam568",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression569", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent570: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent570",
    ends={
        Property(name="IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence571", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn572: BinaryAssociation = BinaryAssociation(
    name="resultReturn572",
    ends={
        Property(name="Events_traceSystem_EObject574", type=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence573", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam575: BinaryAssociation = BinaryAssociation(
    name="thisParam575",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression576", type=traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
thisParam551: BinaryAssociation = BinaryAssociation(
    name="thisParam551",
    ends={
        Property(name="Events_traceSystem_IntegerCalculationExpression552", type=traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence", type=Events_traceSystem_IntegerCalculationExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent553: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent553",
    ends={
        Property(name="IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence554", type=traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence", type=IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn555: BinaryAssociation = BinaryAssociation(
    name="resultReturn555",
    ends={
        Property(name="Events_traceSystem_EObject557", type=traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence556", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam582: BinaryAssociation = BinaryAssociation(
    name="thisParam582",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression583", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent584: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent584",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence585", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn586: BinaryAssociation = BinaryAssociation(
    name="resultReturn586",
    ends={
        Property(name="Events_traceSystem_EObject588", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence587", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam589: BinaryAssociation = BinaryAssociation(
    name="thisParam589",
    ends={
        Property(name="Events_traceSystem_IntegerComparisonExpression590", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence", type=Events_traceSystem_IntegerComparisonExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent591: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent591",
    ends={
        Property(name="IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence592", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence", type=IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn593: BinaryAssociation = BinaryAssociation(
    name="resultReturn593",
    ends={
        Property(name="Events_traceSystem_EObject595", type=traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence594", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam596: BinaryAssociation = BinaryAssociation(
    name="thisParam596",
    ends={
        Property(name="Events_traceSystem_BooleanUnaryExpression", type=traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence", type=Events_traceSystem_BooleanUnaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent577: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent577",
    ends={
        Property(name="IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence578", type=traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence", type=IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn603: BinaryAssociation = BinaryAssociation(
    name="resultReturn603",
    ends={
        Property(name="Events_traceSystem_EObject605", type=traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence604", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
resultReturn579: BinaryAssociation = BinaryAssociation(
    name="resultReturn579",
    ends={
        Property(name="Events_traceSystem_EObject581", type=traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence580", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam606: BinaryAssociation = BinaryAssociation(
    name="thisParam606",
    ends={
        Property(name="Events_traceSystem_BooleanBinaryExpression", type=traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence", type=Events_traceSystem_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent607: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent607",
    ends={
        Property(name="BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence608", type=traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence", type=BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam609: BinaryAssociation = BinaryAssociation(
    name="thisParam609",
    ends={
        Property(name="Events_traceSystem_BooleanBinaryExpression610", type=traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence", type=Events_traceSystem_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent611: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent611",
    ends={
        Property(name="BooleanBinaryExpression_evaluateANDEntryEventOccurrence612", type=traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence", type=BooleanBinaryExpression_evaluateANDEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
resultReturn613: BinaryAssociation = BinaryAssociation(
    name="resultReturn613",
    ends={
        Property(name="Events_traceSystem_EObject615", type=traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence614", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam616: BinaryAssociation = BinaryAssociation(
    name="thisParam616",
    ends={
        Property(name="Events_traceSystem_BooleanBinaryExpression617", type=traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence", type=Events_traceSystem_BooleanBinaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent618: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent618",
    ends={
        Property(name="BooleanBinaryExpression_evaluateOREntryEventOccurrence619", type=traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence", type=BooleanBinaryExpression_evaluateOREntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent597: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent597",
    ends={
        Property(name="BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence598", type=traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence", type=BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam599: BinaryAssociation = BinaryAssociation(
    name="thisParam599",
    ends={
        Property(name="Events_traceSystem_BooleanUnaryExpression600", type=traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence", type=Events_traceSystem_BooleanUnaryExpression, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent601: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent601",
    ends={
        Property(name="BooleanUnaryExpression_evaluateNOTEntryEventOccurrence602", type=traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence", type=BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam623: BinaryAssociation = BinaryAssociation(
    name="thisParam623",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken624", type=traceSystem_Events_Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_isWithdrawnEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent625: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent625",
    ends={
        Property(name="Token_isWithdrawnEntryEventOccurrence626", type=traceSystem_Events_Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_isWithdrawnExitEventOccurrence", type=Token_isWithdrawnEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
isWithdrawnReturn627: BinaryAssociation = BinaryAssociation(
    name="isWithdrawnReturn627",
    ends={
        Property(name="Events_traceSystem_EObject629", type=traceSystem_Events_Token_isWithdrawnExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_isWithdrawnExitEventOccurrence628", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
thisParam630: BinaryAssociation = BinaryAssociation(
    name="thisParam630",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken631", type=traceSystem_Events_Token_transferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_transferEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
holderParam632: BinaryAssociation = BinaryAssociation(
    name="holderParam632",
    ends={
        Property(name="Events_traceSystem_EObject634", type=traceSystem_Events_Token_transferEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_transferEntryEventOccurrence633", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent635: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent635",
    ends={
        Property(name="Token_transferEntryEventOccurrence636", type=traceSystem_Events_Token_transferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_transferExitEventOccurrence", type=Token_transferEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
transferredTokenReturn637: BinaryAssociation = BinaryAssociation(
    name="transferredTokenReturn637",
    ends={
        Property(name="Events_traceSystem_EObject639", type=traceSystem_Events_Token_transferExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_transferExitEventOccurrence638", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
resultReturn620: BinaryAssociation = BinaryAssociation(
    name="resultReturn620",
    ends={
        Property(name="Events_traceSystem_EObject622", type=traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence621", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
correspondingEntryEvent645: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent645",
    ends={
        Property(name="ForkedToken_withdraw_forkedTokenEntryEventOccurrence646", type=traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence", type=ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam647: BinaryAssociation = BinaryAssociation(
    name="thisParam647",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer", type=traceSystem_Events_Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Offer_hasTokensEntryEventOccurrence", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent648: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent648",
    ends={
        Property(name="Offer_hasTokensEntryEventOccurrence649", type=traceSystem_Events_Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Offer_hasTokensExitEventOccurrence", type=Offer_hasTokensEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
hasTokensReturn650: BinaryAssociation = BinaryAssociation(
    name="hasTokensReturn650",
    ends={
        Property(name="Events_traceSystem_EObject652", type=traceSystem_Events_Offer_hasTokensExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Offer_hasTokensExitEventOccurrence651", type=Events_traceSystem_EObject, multiplicity=Multiplicity(1, 1))
    }
)
baseToken653: BinaryAssociation = BinaryAssociation(
    name="baseToken653",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken654", type=traceSystem_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_ForkedToken_baseToken_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
parent655: BinaryAssociation = BinaryAssociation(
    name="parent655",
    ends={
        Property(name="Traced", type=traceSystem_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates656: BinaryAssociation = BinaryAssociation(
    name="globalStates656",
    ends={
        Property(name="GlobalState657", type=traceSystem_States_ForkedToken_baseToken_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseToken_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent658: BinaryAssociation = BinaryAssociation(
    name="parent658",
    ends={
        Property(name="Traced660", type=traceSystem_States_ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration659", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates661: BinaryAssociation = BinaryAssociation(
    name="globalStates661",
    ends={
        Property(name="GlobalState662", type=traceSystem_States_ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_remainingOffersCount_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
thisParam640: BinaryAssociation = BinaryAssociation(
    name="thisParam640",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken641", type=traceSystem_Events_Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_withdrawEntryEventOccurrence", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 1))
    }
)
correspondingEntryEvent642: BinaryAssociation = BinaryAssociation(
    name="correspondingEntryEvent642",
    ends={
        Property(name="Token_withdrawEntryEventOccurrence643", type=traceSystem_Events_Token_withdrawExitEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_Token_withdrawExitEventOccurrence", type=Token_withdrawEntryEventOccurrence, multiplicity=Multiplicity(0, 1))
    }
)
thisParam644: BinaryAssociation = BinaryAssociation(
    name="thisParam644",
    ends={
        Property(name="activitydiagramConfiguration_TracedForkedToken", type=traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(0, 1))
    }
)
globalStates673: BinaryAssociation = BinaryAssociation(
    name="globalStates673",
    ends={
        Property(name="GlobalState674", type=traceSystem_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="token_holder_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
offeredTokens675: BinaryAssociation = BinaryAssociation(
    name="offeredTokens675",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken676", type=traceSystem_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Offer_offeredTokens_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent677: BinaryAssociation = BinaryAssociation(
    name="parent677",
    ends={
        Property(name="Traced679", type=traceSystem_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration678", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(1, 1))
    }
)
globalStates680: BinaryAssociation = BinaryAssociation(
    name="globalStates680",
    ends={
        Property(name="GlobalState681", type=traceSystem_States_Offer_offeredTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="offer_offeredTokens_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
trace682: BinaryAssociation = BinaryAssociation(
    name="trace682",
    ends={
        Property(name="activitydiagramConfiguration_TracedTrace", type=traceSystem_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Activity_trace_State", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1))
    }
)
parent683: BinaryAssociation = BinaryAssociation(
    name="parent683",
    ends={
        Property(name="Traced684", type=traceSystem_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1))
    }
)
globalStates685: BinaryAssociation = BinaryAssociation(
    name="globalStates685",
    ends={
        Property(name="GlobalState686", type=traceSystem_States_Activity_trace_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activity_trace_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
currentValue687: BinaryAssociation = BinaryAssociation(
    name="currentValue687",
    ends={
        Property(name="States_traceSystem_Value", type=traceSystem_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Variable_currentValue_State", type=States_traceSystem_Value, multiplicity=Multiplicity(1, 1))
    }
)
parent688: BinaryAssociation = BinaryAssociation(
    name="parent688",
    ends={
        Property(name="Traced690", type=traceSystem_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram689", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
globalStates691: BinaryAssociation = BinaryAssociation(
    name="globalStates691",
    ends={
        Property(name="GlobalState692", type=traceSystem_States_Variable_currentValue_State, multiplicity=Multiplicity(1, 1)),
        Property(name="variable_currentValue_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
value693: BinaryAssociation = BinaryAssociation(
    name="value693",
    ends={
        Property(name="States_traceSystem_Value694", type=traceSystem_States_InputValue_value_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_InputValue_value_State", type=States_traceSystem_Value, multiplicity=Multiplicity(1, 1))
    }
)
parent695: BinaryAssociation = BinaryAssociation(
    name="parent695",
    ends={
        Property(name="Traced697", type=traceSystem_States_InputValue_value_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration696", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1))
    }
)
globalStates698: BinaryAssociation = BinaryAssociation(
    name="globalStates698",
    ends={
        Property(name="GlobalState699", type=traceSystem_States_InputValue_value_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inputValue_value_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent663: BinaryAssociation = BinaryAssociation(
    name="parent663",
    ends={
        Property(name="Traced665", type=traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration664", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates666: BinaryAssociation = BinaryAssociation(
    name="globalStates666",
    ends={
        Property(name="GlobalState667", type=traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(1, 1)),
        Property(name="forkedToken_baseTokenIsWithdrawn_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
holder668: BinaryAssociation = BinaryAssociation(
    name="holder668",
    ends={
        Property(name="activitydiagram_TracedActivityNode669", type=traceSystem_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Token_holder_State", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
parent670: BinaryAssociation = BinaryAssociation(
    name="parent670",
    ends={
        Property(name="Traced672", type=traceSystem_States_Token_holder_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration671", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1))
    }
)
globalStates704: BinaryAssociation = BinaryAssociation(
    name="globalStates704",
    ends={
        Property(name="GlobalState705", type=traceSystem_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="inputValue_variable_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
offers706: BinaryAssociation = BinaryAssociation(
    name="offers706",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer707", type=traceSystem_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_ActivityEdge_offers_State", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 9999))
    }
)
parent708: BinaryAssociation = BinaryAssociation(
    name="parent708",
    ends={
        Property(name="Traced710", type=traceSystem_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram709", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1))
    }
)
globalStates711: BinaryAssociation = BinaryAssociation(
    name="globalStates711",
    ends={
        Property(name="GlobalState712", type=traceSystem_States_ActivityEdge_offers_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityEdge_offers_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
executedNodes713: BinaryAssociation = BinaryAssociation(
    name="executedNodes713",
    ends={
        Property(name="activitydiagram_TracedActivityNode714", type=traceSystem_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Trace_executedNodes_State", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
parent715: BinaryAssociation = BinaryAssociation(
    name="parent715",
    ends={
        Property(name="Traced717", type=traceSystem_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration716", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1))
    }
)
globalStates718: BinaryAssociation = BinaryAssociation(
    name="globalStates718",
    ends={
        Property(name="GlobalState719", type=traceSystem_States_Trace_executedNodes_State, multiplicity=Multiplicity(1, 1)),
        Property(name="trace_executedNodes_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
inputValues720: BinaryAssociation = BinaryAssociation(
    name="inputValues720",
    ends={
        Property(name="activitydiagramConfiguration_TracedInputValue", type=traceSystem_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_Input_inputValues_State", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(0, 9999))
    }
)
parent721: BinaryAssociation = BinaryAssociation(
    name="parent721",
    ends={
        Property(name="Traced723", type=traceSystem_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration722", type=activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(1, 1))
    }
)
globalStates724: BinaryAssociation = BinaryAssociation(
    name="globalStates724",
    ends={
        Property(name="GlobalState725", type=traceSystem_States_Input_inputValues_State, multiplicity=Multiplicity(1, 1)),
        Property(name="input_inputValues_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
variable700: BinaryAssociation = BinaryAssociation(
    name="variable700",
    ends={
        Property(name="activitydiagram_TracedVariable", type=traceSystem_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_InputValue_variable_State", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1))
    }
)
globalStates736: BinaryAssociation = BinaryAssociation(
    name="globalStates736",
    ends={
        Property(name="GlobalState737", type=traceSystem_States_ActivityNode_running_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNode_running_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent701: BinaryAssociation = BinaryAssociation(
    name="parent701",
    ends={
        Property(name="Traced703", type=traceSystem_States_InputValue_variable_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagramConfiguration702", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1))
    }
)
activitydiagramConfiguration_tracedForkedTokens738: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedForkedTokens738",
    ends={
        Property(name="activitydiagramConfiguration_TracedForkedToken739", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects", type=activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedBooleanVariables740: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedBooleanVariables740",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable742", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects741", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedForkNodes743: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedForkNodes743",
    ends={
        Property(name="activitydiagram_TracedForkNode745", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects744", type=activitydiagram_TracedForkNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedControlFlows746: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedControlFlows746",
    ends={
        Property(name="activitydiagram_TracedControlFlow", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects747", type=activitydiagram_TracedControlFlow, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedActivityFinalNodes748: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedActivityFinalNodes748",
    ends={
        Property(name="activitydiagram_TracedActivityFinalNode750", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects749", type=activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedStringVariables751: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedStringVariables751",
    ends={
        Property(name="activitydiagram_TracedStringVariable753", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects752", type=activitydiagram_TracedStringVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedOpaqueActions754: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedOpaqueActions754",
    ends={
        Property(name="activitydiagram_TracedOpaqueAction756", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects755", type=activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedControlTokens757: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedControlTokens757",
    ends={
        Property(name="activitydiagramConfiguration_TracedControlToken", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects758", type=activitydiagramConfiguration_TracedControlToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedOffers759: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedOffers759",
    ends={
        Property(name="activitydiagramConfiguration_TracedOffer761", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects760", type=activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
heldTokens726: BinaryAssociation = BinaryAssociation(
    name="heldTokens726",
    ends={
        Property(name="activitydiagramConfiguration_TracedToken727", type=traceSystem_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_States_ActivityNode_heldTokens_State", type=activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(0, 9999))
    }
)
parent728: BinaryAssociation = BinaryAssociation(
    name="parent728",
    ends={
        Property(name="Traced730", type=traceSystem_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram729", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
globalStates731: BinaryAssociation = BinaryAssociation(
    name="globalStates731",
    ends={
        Property(name="GlobalState732", type=traceSystem_States_ActivityNode_heldTokens_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activityNode_heldTokens_States", type=States_traceSystem_GlobalState, multiplicity=Multiplicity(1, 9999))
    }
)
parent733: BinaryAssociation = BinaryAssociation(
    name="parent733",
    ends={
        Property(name="Traced735", type=traceSystem_States_ActivityNode_running_State, multiplicity=Multiplicity(1, 1)),
        Property(name="activitydiagram734", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
activitydiagram_tracedDecisionNodes771: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedDecisionNodes771",
    ends={
        Property(name="activitydiagram_TracedDecisionNode773", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects772", type=activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
valueTrace802: BinaryAssociation = BinaryAssociation(
    name="valueTrace802",
    ends={
        Property(name="States804", type=traceSystem_activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_value_State803", type=InputValue_value_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
variableTrace805: BinaryAssociation = BinaryAssociation(
    name="variableTrace805",
    ends={
        Property(name="States807", type=traceSystem_activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(1, 1)),
        Property(name="InputValue_variable_State806", type=InputValue_variable_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedIntegerVariables774: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedIntegerVariables774",
    ends={
        Property(name="activitydiagram_TracedIntegerVariable776", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects775", type=activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedJoinNodes777: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedJoinNodes777",
    ends={
        Property(name="activitydiagram_TracedJoinNode", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects778", type=activitydiagram_TracedJoinNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedTraces779: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedTraces779",
    ends={
        Property(name="activitydiagramConfiguration_TracedTrace781", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects780", type=activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedInputs782: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedInputs782",
    ends={
        Property(name="activitydiagramConfiguration_TracedInput", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects783", type=activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedInitialNodes784: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedInitialNodes784",
    ends={
        Property(name="activitydiagram_TracedInitialNode786", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects785", type=activitydiagram_TracedInitialNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenTrace787: BinaryAssociation = BinaryAssociation(
    name="baseTokenTrace787",
    ends={
        Property(name="States789", type=traceSystem_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseToken_State788", type=ForkedToken_baseToken_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
remainingOffersCountTrace790: BinaryAssociation = BinaryAssociation(
    name="remainingOffersCountTrace790",
    ends={
        Property(name="States792", type=traceSystem_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_remainingOffersCount_State791", type=ForkedToken_remainingOffersCount_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedActivitys762: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedActivitys762",
    ends={
        Property(name="activitydiagram_TracedActivity764", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects763", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
baseTokenIsWithdrawnTrace793: BinaryAssociation = BinaryAssociation(
    name="baseTokenIsWithdrawnTrace793",
    ends={
        Property(name="States795", type=traceSystem_activitydiagramConfiguration_TracedForkedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="ForkedToken_baseTokenIsWithdrawn_State794", type=ForkedToken_baseTokenIsWithdrawn_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagramConfiguration_tracedInputValues765: BinaryAssociation = BinaryAssociation(
    name="activitydiagramConfiguration_tracedInputValues765",
    ends={
        Property(name="activitydiagramConfiguration_TracedInputValue767", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects766", type=activitydiagramConfiguration_TracedInputValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
holderTrace796: BinaryAssociation = BinaryAssociation(
    name="holderTrace796",
    ends={
        Property(name="States798", type=traceSystem_activitydiagramConfiguration_TracedToken, multiplicity=Multiplicity(1, 1)),
        Property(name="Token_holder_State797", type=Token_holder_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
activitydiagram_tracedMergeNodes768: BinaryAssociation = BinaryAssociation(
    name="activitydiagram_tracedMergeNodes768",
    ends={
        Property(name="activitydiagram_TracedMergeNode770", type=traceSystem_Traced_TracedObjects, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_Traced_TracedObjects769", type=activitydiagram_TracedMergeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
offeredTokensTrace799: BinaryAssociation = BinaryAssociation(
    name="offeredTokensTrace799",
    ends={
        Property(name="States801", type=traceSystem_activitydiagramConfiguration_TracedOffer, multiplicity=Multiplicity(1, 1)),
        Property(name="Offer_offeredTokens_State800", type=Offer_offeredTokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions822: BinaryAssociation = BinaryAssociation(
    name="expressions822",
    ends={
        Property(name="activitydiagram_traceSystem_Expression", type=traceSystem_activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedOpaqueAction", type=activitydiagram_traceSystem_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject823: BinaryAssociation = BinaryAssociation(
    name="originalObject823",
    ends={
        Property(name="activitydiagram_traceSystem_OpaqueAction", type=traceSystem_activitydiagram_TracedOpaqueAction, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedOpaqueAction824", type=activitydiagram_traceSystem_OpaqueAction, multiplicity=Multiplicity(0, 1))
    }
)
nodes825: BinaryAssociation = BinaryAssociation(
    name="nodes825",
    ends={
        Property(name="activitydiagram_TracedActivityNode826", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivity", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(0, 9999))
    }
)
executedNodesTrace808: BinaryAssociation = BinaryAssociation(
    name="executedNodesTrace808",
    ends={
        Property(name="States810", type=traceSystem_activitydiagramConfiguration_TracedTrace, multiplicity=Multiplicity(1, 1)),
        Property(name="Trace_executedNodes_State809", type=Trace_executedNodes_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges827: BinaryAssociation = BinaryAssociation(
    name="edges827",
    ends={
        Property(name="activitydiagram_TracedActivityEdge829", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivity828", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
inputValuesTrace811: BinaryAssociation = BinaryAssociation(
    name="inputValuesTrace811",
    ends={
        Property(name="States813", type=traceSystem_activitydiagramConfiguration_TracedInput, multiplicity=Multiplicity(1, 1)),
        Property(name="Input_inputValues_State812", type=Input_inputValues_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject814: BinaryAssociation = BinaryAssociation(
    name="originalObject814",
    ends={
        Property(name="activitydiagram_traceSystem_BooleanVariable", type=traceSystem_activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedBooleanVariable", type=activitydiagram_traceSystem_BooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
originalObject815: BinaryAssociation = BinaryAssociation(
    name="originalObject815",
    ends={
        Property(name="activitydiagram_traceSystem_ForkNode", type=traceSystem_activitydiagram_TracedForkNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedForkNode", type=activitydiagram_traceSystem_ForkNode, multiplicity=Multiplicity(0, 1))
    }
)
guard816: BinaryAssociation = BinaryAssociation(
    name="guard816",
    ends={
        Property(name="activitydiagram_TracedBooleanVariable817", type=traceSystem_activitydiagram_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedControlFlow", type=activitydiagram_TracedBooleanVariable, multiplicity=Multiplicity(0, 1))
    }
)
originalObject818: BinaryAssociation = BinaryAssociation(
    name="originalObject818",
    ends={
        Property(name="activitydiagram_traceSystem_ControlFlow", type=traceSystem_activitydiagram_TracedControlFlow, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedControlFlow819", type=activitydiagram_traceSystem_ControlFlow, multiplicity=Multiplicity(0, 1))
    }
)
originalObject820: BinaryAssociation = BinaryAssociation(
    name="originalObject820",
    ends={
        Property(name="activitydiagram_traceSystem_ActivityFinalNode", type=traceSystem_activitydiagram_TracedActivityFinalNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityFinalNode", type=activitydiagram_traceSystem_ActivityFinalNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject821: BinaryAssociation = BinaryAssociation(
    name="originalObject821",
    ends={
        Property(name="activitydiagram_traceSystem_StringVariable", type=traceSystem_activitydiagram_TracedStringVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedStringVariable", type=activitydiagram_traceSystem_StringVariable, multiplicity=Multiplicity(0, 1))
    }
)
source848: BinaryAssociation = BinaryAssociation(
    name="source848",
    ends={
        Property(name="activitydiagram_TracedActivityNode849", type=traceSystem_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityEdge", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
target850: BinaryAssociation = BinaryAssociation(
    name="target850",
    ends={
        Property(name="activitydiagram_TracedActivityNode852", type=traceSystem_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityEdge851", type=activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1))
    }
)
offersTrace853: BinaryAssociation = BinaryAssociation(
    name="offersTrace853",
    ends={
        Property(name="States855", type=traceSystem_activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityEdge_offers_State854", type=ActivityEdge_offers_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
locals830: BinaryAssociation = BinaryAssociation(
    name="locals830",
    ends={
        Property(name="activitydiagram_TracedVariable832", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivity831", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
inputs833: BinaryAssociation = BinaryAssociation(
    name="inputs833",
    ends={
        Property(name="activitydiagram_TracedVariable835", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivity834", type=activitydiagram_TracedVariable, multiplicity=Multiplicity(0, 9999))
    }
)
originalObject836: BinaryAssociation = BinaryAssociation(
    name="originalObject836",
    ends={
        Property(name="activitydiagram_traceSystem_Activity", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivity837", type=activitydiagram_traceSystem_Activity, multiplicity=Multiplicity(0, 1))
    }
)
traceTrace838: BinaryAssociation = BinaryAssociation(
    name="traceTrace838",
    ends={
        Property(name="States840", type=traceSystem_activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1)),
        Property(name="Activity_trace_State839", type=Activity_trace_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue841: BinaryAssociation = BinaryAssociation(
    name="initialValue841",
    ends={
        Property(name="activitydiagram_traceSystem_Value", type=traceSystem_activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedVariable", type=activitydiagram_traceSystem_Value, multiplicity=Multiplicity(0, 1))
    }
)
currentValueTrace842: BinaryAssociation = BinaryAssociation(
    name="currentValueTrace842",
    ends={
        Property(name="States844", type=traceSystem_activitydiagram_TracedVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="Variable_currentValue_State843", type=Variable_currentValue_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject845: BinaryAssociation = BinaryAssociation(
    name="originalObject845",
    ends={
        Property(name="activitydiagram_traceSystem_MergeNode", type=traceSystem_activitydiagram_TracedMergeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedMergeNode", type=activitydiagram_traceSystem_MergeNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject846: BinaryAssociation = BinaryAssociation(
    name="originalObject846",
    ends={
        Property(name="activitydiagram_traceSystem_DecisionNode", type=traceSystem_activitydiagram_TracedDecisionNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedDecisionNode", type=activitydiagram_traceSystem_DecisionNode, multiplicity=Multiplicity(0, 1))
    }
)
originalObject847: BinaryAssociation = BinaryAssociation(
    name="originalObject847",
    ends={
        Property(name="activitydiagram_traceSystem_IntegerVariable", type=traceSystem_activitydiagram_TracedIntegerVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedIntegerVariable", type=activitydiagram_traceSystem_IntegerVariable, multiplicity=Multiplicity(0, 1))
    }
)
originalObject856: BinaryAssociation = BinaryAssociation(
    name="originalObject856",
    ends={
        Property(name="activitydiagram_traceSystem_JoinNode", type=traceSystem_activitydiagram_TracedJoinNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedJoinNode", type=activitydiagram_traceSystem_JoinNode, multiplicity=Multiplicity(0, 1))
    }
)
outgoing857: BinaryAssociation = BinaryAssociation(
    name="outgoing857",
    ends={
        Property(name="activitydiagram_TracedActivityEdge858", type=traceSystem_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityNode", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
incoming859: BinaryAssociation = BinaryAssociation(
    name="incoming859",
    ends={
        Property(name="activitydiagram_TracedActivityEdge861", type=traceSystem_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityNode860", type=activitydiagram_TracedActivityEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activity862: BinaryAssociation = BinaryAssociation(
    name="activity862",
    ends={
        Property(name="activitydiagram_TracedActivity864", type=traceSystem_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedActivityNode863", type=activitydiagram_TracedActivity, multiplicity=Multiplicity(1, 1))
    }
)
heldTokensTrace865: BinaryAssociation = BinaryAssociation(
    name="heldTokensTrace865",
    ends={
        Property(name="States867", type=traceSystem_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_heldTokens_State866", type=ActivityNode_heldTokens_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
runningTrace868: BinaryAssociation = BinaryAssociation(
    name="runningTrace868",
    ends={
        Property(name="States870", type=traceSystem_activitydiagram_TracedActivityNode, multiplicity=Multiplicity(1, 1)),
        Property(name="ActivityNode_running_State869", type=ActivityNode_running_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
originalObject871: BinaryAssociation = BinaryAssociation(
    name="originalObject871",
    ends={
        Property(name="activitydiagram_traceSystem_InitialNode", type=traceSystem_activitydiagram_TracedInitialNode, multiplicity=Multiplicity(1, 1)),
        Property(name="traceSystem_activitydiagram_TracedInitialNode", type=activitydiagram_traceSystem_InitialNode, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_traceSystem_Events_Activity_mainEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_mainEntryEventOccurrence)
gen_traceSystem_Events_Activity_mainExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_mainExitEventOccurrence)
gen_traceSystem_Events_Activity_initializeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_initializeEntryEventOccurrence)
gen_traceSystem_Events_Activity_initializeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_initializeExitEventOccurrence)
gen_traceSystem_Events_Activity_runNodesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_runNodesExitEventOccurrence)
gen_traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence)
gen_traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence)
gen_traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence)
gen_traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence)
gen_traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence)
gen_traceSystem_Events_Activity_selectNextNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_selectNextNodeExitEventOccurrence)
gen_traceSystem_Events_Activity_runEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_runEntryEventOccurrence)
gen_traceSystem_Events_Activity_runExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_runExitEventOccurrence)
gen_traceSystem_Events_Activity_runNodesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_runNodesEntryEventOccurrence)
gen_traceSystem_Events_Activity_fireNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_fireNodeEntryEventOccurrence)
gen_traceSystem_Events_Activity_fireNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_fireNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_isRunningExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_isRunningExitEventOccurrence)
gen_traceSystem_Events_Activity_terminateEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_terminateEntryEventOccurrence)
gen_traceSystem_Events_Activity_terminateExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_terminateExitEventOccurrence)
gen_traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence)
gen_traceSystem_Events_Activity_getInitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Activity_getInitialNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_addTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_addTokensExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence)
gen_traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence)
gen_traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence)
gen_traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence)
gen_traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence)
gen_traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence)
gen_traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence)
gen_traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence)
gen_traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence)
gen_traceSystem_Events_ActivityNode_isReadyExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityNode_isReadyExitEventOccurrence)
gen_traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence)
gen_traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence)
gen_traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence)
gen_traceSystem_Events_Action_sendOffers_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_sendOffers_actionExitEventOccurrence)
gen_traceSystem_Events_Action_isReady_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_isReady_actionEntryEventOccurrence)
gen_traceSystem_Events_Action_isReady_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_isReady_actionExitEventOccurrence)
gen_traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence)
gen_traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence)
gen_traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence)
gen_traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence)
gen_traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence)
gen_traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence)
gen_traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence)
gen_traceSystem_Events_Action_fire_actionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_fire_actionEntryEventOccurrence)
gen_traceSystem_Events_Action_fire_actionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Action_fire_actionExitEventOccurrence)
gen_traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence)
gen_traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence)
gen_traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence)
gen_traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence)
gen_traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence)
gen_traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence)
gen_traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence)
gen_traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence)
gen_traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence)
gen_traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence)
gen_traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence)
gen_traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence)
gen_traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence)
gen_traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence)
gen_traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence)
gen_traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence)
gen_traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence)
gen_traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence)
gen_traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence)
gen_traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence)
gen_traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence)
gen_traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence)
gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence)
gen_traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence)
gen_traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence)
gen_traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence)
gen_traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence)
gen_traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence)
gen_traceSystem_Events_Token_isWithdrawnEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_isWithdrawnEntryEventOccurrence)
gen_traceSystem_Events_Token_isWithdrawnExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_isWithdrawnExitEventOccurrence)
gen_traceSystem_Events_Token_transferEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_transferEntryEventOccurrence)
gen_traceSystem_Events_Token_transferExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_transferExitEventOccurrence)
gen_traceSystem_Events_Token_withdrawEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_withdrawEntryEventOccurrence)
gen_traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence)
gen_traceSystem_Events_Offer_hasTokensEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Offer_hasTokensEntryEventOccurrence)
gen_traceSystem_Events_Offer_hasTokensExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Offer_hasTokensExitEventOccurrence)
gen_traceSystem_Events_Token_withdrawExitEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_Token_withdrawExitEventOccurrence)
gen_traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_EventOccurrence = Generalization(general=EventOccurrence, specific=traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence)
gen_traceSystem_activitydiagramConfiguration_TracedForkedToken_TracedToken = Generalization(general=TracedToken, specific=traceSystem_activitydiagramConfiguration_TracedForkedToken)
gen_traceSystem_activitydiagramConfiguration_TracedControlToken_TracedToken = Generalization(general=TracedToken, specific=traceSystem_activitydiagramConfiguration_TracedControlToken)
gen_traceSystem_activitydiagram_TracedExecutableNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=traceSystem_activitydiagram_TracedExecutableNode)
gen_traceSystem_activitydiagram_TracedActivity_TracedNamedElement = Generalization(general=TracedNamedElement, specific=traceSystem_activitydiagram_TracedActivity)
gen_traceSystem_activitydiagram_TracedBooleanVariable_TracedVariable = Generalization(general=TracedVariable, specific=traceSystem_activitydiagram_TracedBooleanVariable)
gen_traceSystem_activitydiagram_TracedForkNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedForkNode)
gen_traceSystem_activitydiagram_TracedControlFlow_TracedActivityEdge = Generalization(general=TracedActivityEdge, specific=traceSystem_activitydiagram_TracedControlFlow)
gen_traceSystem_activitydiagram_TracedActivityFinalNode_TracedFinalNode = Generalization(general=TracedFinalNode, specific=traceSystem_activitydiagram_TracedActivityFinalNode)
gen_traceSystem_activitydiagram_TracedAction_TracedExecutableNode = Generalization(general=TracedExecutableNode, specific=traceSystem_activitydiagram_TracedAction)
gen_traceSystem_activitydiagram_TracedFinalNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedFinalNode)
gen_traceSystem_activitydiagram_TracedStringVariable_TracedVariable = Generalization(general=TracedVariable, specific=traceSystem_activitydiagram_TracedStringVariable)
gen_traceSystem_activitydiagram_TracedOpaqueAction_TracedAction = Generalization(general=TracedAction, specific=traceSystem_activitydiagram_TracedOpaqueAction)
gen_traceSystem_activitydiagram_TracedActivityEdge_TracedNamedElement = Generalization(general=TracedNamedElement, specific=traceSystem_activitydiagram_TracedActivityEdge)
gen_traceSystem_activitydiagram_TracedJoinNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedJoinNode)
gen_traceSystem_activitydiagram_TracedVariable_TracedNamedElement = Generalization(general=TracedNamedElement, specific=traceSystem_activitydiagram_TracedVariable)
gen_traceSystem_activitydiagram_TracedMergeNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedMergeNode)
gen_traceSystem_activitydiagram_TracedDecisionNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedDecisionNode)
gen_traceSystem_activitydiagram_TracedIntegerVariable_TracedVariable = Generalization(general=TracedVariable, specific=traceSystem_activitydiagram_TracedIntegerVariable)
gen_traceSystem_activitydiagram_TracedControlNode_TracedActivityNode = Generalization(general=TracedActivityNode, specific=traceSystem_activitydiagram_TracedControlNode)
gen_traceSystem_activitydiagram_TracedActivityNode_TracedNamedElement = Generalization(general=TracedNamedElement, specific=traceSystem_activitydiagram_TracedActivityNode)
gen_traceSystem_activitydiagram_TracedInitialNode_TracedControlNode = Generalization(general=TracedControlNode, specific=traceSystem_activitydiagram_TracedInitialNode)

# Domain Model
domain_model = DomainModel(
    name="traceSystem",
    types={traceSystem_Trace, traceSystem_GlobalState, Events, Offer_offeredTokens_State, Activity_trace_State, Variable_currentValue_State, InputValue_value_State, InputValue_variable_State, ActivityEdge_offers_State, Trace_executedNodes_State, Input_inputValues_State, ActivityNode_heldTokens_State, ActivityNode_running_State, TracedObjects, traceSystem_StaticObjectsPools, EventOccurrence, ForkedToken_baseToken_State, ForkedToken_remainingOffersCount_State, ForkedToken_baseTokenIsWithdrawn_State, Token_holder_State, Activity_mainEntryEventOccurrence, Activity_mainExitEventOccurrence, Activity_initializeEntryEventOccurrence, Activity_initializeExitEventOccurrence, Activity_runEntryEventOccurrence, Activity_runExitEventOccurrence, Activity_runNodesEntryEventOccurrence, Activity_runNodesExitEventOccurrence, Activity_fireInitialNodeEntryEventOccurrence, Activity_fireInitialNodeExitEventOccurrence, Activity_getEnabledNodesEntryEventOccurrence, traceSystem_BooleanValue, traceSystem_IntegerComparisonExpression, traceSystem_StringValue, traceSystem_BooleanBinaryExpression, traceSystem_BooleanUnaryExpression, traceSystem_IntegerValue, traceSystem_IntegerCalculationExpression, traceSystem_Events_EventOccurrence, Events_traceSystem_GlobalState, traceSystem_Events_Events, ActivityNode_run_activityNodeEntryEventOccurrence, ActivityNode_run_activityNodeExitEventOccurrence, ActivityNode_isRunningEntryEventOccurrence, ActivityNode_isRunningExitEventOccurrence, ActivityNode_terminate_activityNodeEntryEventOccurrence, ActivityNode_terminate_activityNodeExitEventOccurrence, Activity_getEnabledNodesExitEventOccurrence, Activity_selectNextNodeEntryEventOccurrence, Activity_selectNextNodeExitEventOccurrence, Activity_terminateEntryEventOccurrence, Activity_terminateExitEventOccurrence, Activity_getInitialNodeEntryEventOccurrence, Activity_getInitialNodeExitEventOccurrence, Activity_fireNodeEntryEventOccurrence, Activity_fireNodeExitEventOccurrence, ActivityNode_removeTokenExitEventOccurrence, ActivityNode_hasOffersEntryEventOccurrence, ActivityNode_hasOffersExitEventOccurrence, ActivityNode_isReadyEntryEventOccurrence, ActivityNode_isReadyExitEventOccurrence, ActivityEdge_sendOfferEntryEventOccurrence, ActivityEdge_sendOfferExitEventOccurrence, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, ActivityNode_sendOffersEntryEventOccurrence, ActivityNode_sendOffersExitEventOccurrence, ActivityNode_takeOfferedTokensEntryEventOccurrence, ActivityNode_takeOfferedTokensExitEventOccurrence, ActivityNode_addTokensEntryEventOccurrence, ActivityNode_addTokensExitEventOccurrence, ActivityNode_removeTokenEntryEventOccurrence, Action_sendOffers_actionExitEventOccurrence, Action_isReady_actionEntryEventOccurrence, Action_isReady_actionExitEventOccurrence, Action_fire_actionEntryEventOccurrence, Action_fire_actionExitEventOccurrence, OpaqueAction_doAction_opaqueActionEntryEventOccurrence, OpaqueAction_doAction_opaqueActionExitEventOccurrence, InitialNode_isReady_InitialNodeEntryEventOccurrence, ActivityEdge_hasOfferEntryEventOccurrence, ActivityEdge_hasOfferExitEventOccurrence, ControlNode_isReady_ControlNodeEntryEventOccurrence, ControlNode_isReady_ControlNodeExitEventOccurrence, ControlNode_fire_controlNodeEntryEventOccurrence, ControlNode_fire_controlNodeExitEventOccurrence, Action_sendOffers_actionEntryEventOccurrence, InitialNode_fire_initialNodeExitEventOccurrence, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, ForkNode_fire_forkNodeEntryEventOccurrence, ForkNode_fire_forkNodeExitEventOccurrence, MergeNode_hasOffers_mergeNodeEntryEventOccurrence, InitialNode_isReady_InitialNodeExitEventOccurrence, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, InitialNode_fire_initialNodeEntryEventOccurrence, StringVariable_setCurrentValue_stringVariableExitEventOccurrence, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, MergeNode_hasOffers_mergeNodeExitEventOccurrence, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, DecisionNode_fire_decisionNodeEntryEventOccurrence, DecisionNode_fire_decisionNodeExitEventOccurrence, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, IntegerCalculationExpression_evaluateADDEntryEventOccurrence, IntegerCalculationExpression_evaluateADDExitEventOccurrence, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, IntegerExpression_getOperandCurrentValuesExitEventOccurrence, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, BooleanBinaryExpression_evaluateANDEntryEventOccurrence, BooleanBinaryExpression_evaluateANDExitEventOccurrence, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, BooleanUnaryExpression_evaluateNOTExitEventOccurrence, Token_transferExitEventOccurrence, Token_withdrawEntryEventOccurrence, Token_withdrawExitEventOccurrence, ForkedToken_withdraw_forkedTokenEntryEventOccurrence, BooleanBinaryExpression_evaluateOREntryEventOccurrence, ForkedToken_withdraw_forkedTokenExitEventOccurrence, BooleanBinaryExpression_evaluateORExitEventOccurrence, Offer_hasTokensEntryEventOccurrence, Token_isWithdrawnEntryEventOccurrence, Token_isWithdrawnExitEventOccurrence, Token_transferEntryEventOccurrence, Offer_hasTokensExitEventOccurrence, traceSystem_Events_Activity_mainEntryEventOccurrence, activitydiagram_TracedActivity, Events_traceSystem_EObject, traceSystem_Events_Activity_mainExitEventOccurrence, traceSystem_Events_Activity_initializeEntryEventOccurrence, traceSystem_Events_Activity_initializeExitEventOccurrence, traceSystem_Events_Activity_runNodesExitEventOccurrence, traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence, traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence, traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence, traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence, traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence, traceSystem_Events_Activity_selectNextNodeExitEventOccurrence, traceSystem_Events_Activity_runEntryEventOccurrence, traceSystem_Events_Activity_runExitEventOccurrence, traceSystem_Events_Activity_runNodesEntryEventOccurrence, traceSystem_Events_Activity_fireNodeEntryEventOccurrence, traceSystem_Events_Activity_fireNodeExitEventOccurrence, traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence, activitydiagram_TracedActivityNode, traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence, traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence, traceSystem_Events_ActivityNode_isRunningExitEventOccurrence, traceSystem_Events_Activity_terminateEntryEventOccurrence, traceSystem_Events_Activity_terminateExitEventOccurrence, traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence, traceSystem_Events_Activity_getInitialNodeExitEventOccurrence, traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence, traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence, traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence, traceSystem_Events_ActivityNode_addTokensExitEventOccurrence, traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence, traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence, traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence, traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence, traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence, traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence, traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence, traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence, activitydiagram_TracedActivityEdge, traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence, traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence, traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence, traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence, traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence, traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence, activitydiagram_TracedControlNode, traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence, traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence, traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence, traceSystem_Events_ActivityNode_isReadyExitEventOccurrence, traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence, activitydiagramConfiguration_TracedToken, traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence, traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence, activitydiagram_TracedAction, traceSystem_Events_Action_sendOffers_actionExitEventOccurrence, traceSystem_Events_Action_isReady_actionEntryEventOccurrence, traceSystem_Events_Action_isReady_actionExitEventOccurrence, activitydiagram_TracedOpaqueAction, traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence, traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence, activitydiagram_TracedInitialNode, traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence, traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence, traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence, traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence, activitydiagram_TracedActivityFinalNode, traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence, traceSystem_Events_Action_fire_actionEntryEventOccurrence, traceSystem_Events_Action_fire_actionExitEventOccurrence, traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence, traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence, activitydiagram_TracedMergeNode, traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence, traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence, activitydiagram_TracedDecisionNode, traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence, traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence, activitydiagram_TracedIntegerVariable, traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence, activitydiagram_TracedForkNode, traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence, traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence, activitydiagram_TracedStringVariable, traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence, traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence, traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence, traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence, activitydiagram_TracedBooleanVariable, traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence, Events_traceSystem_Value, traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence, traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence, traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence, traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence, Events_traceSystem_IntegerExpression, traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence, traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence, Events_traceSystem_IntegerCalculationExpression, traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence, traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence, traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence, traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence, traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence, traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence, Events_traceSystem_IntegerComparisonExpression, traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence, traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence, traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence, traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence, traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence, Events_traceSystem_BooleanUnaryExpression, traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence, Events_traceSystem_BooleanBinaryExpression, traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence, traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence, traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence, traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence, traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence, traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence, traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence, traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence, traceSystem_Events_Token_isWithdrawnEntryEventOccurrence, traceSystem_Events_Token_isWithdrawnExitEventOccurrence, traceSystem_Events_Token_transferEntryEventOccurrence, traceSystem_Events_Token_transferExitEventOccurrence, traceSystem_Events_Token_withdrawEntryEventOccurrence, traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence, traceSystem_Events_Offer_hasTokensEntryEventOccurrence, activitydiagramConfiguration_TracedOffer, traceSystem_Events_Offer_hasTokensExitEventOccurrence, traceSystem_States_ForkedToken_baseToken_State, States_traceSystem_GlobalState, traceSystem_States_ForkedToken_remainingOffersCount_State, traceSystem_States_ForkedToken_baseTokenIsWithdrawn_State, traceSystem_Events_Token_withdrawExitEventOccurrence, traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence, activitydiagramConfiguration_TracedForkedToken, traceSystem_States_Offer_offeredTokens_State, traceSystem_States_Activity_trace_State, activitydiagramConfiguration_TracedTrace, traceSystem_States_Variable_currentValue_State, States_traceSystem_Value, activitydiagram_TracedVariable, traceSystem_States_InputValue_value_State, activitydiagramConfiguration_TracedInputValue, traceSystem_States_Token_holder_State, traceSystem_States_ActivityEdge_offers_State, traceSystem_States_Trace_executedNodes_State, traceSystem_States_Input_inputValues_State, activitydiagramConfiguration_TracedInput, traceSystem_States_ActivityNode_heldTokens_State, traceSystem_States_InputValue_variable_State, traceSystem_Traced_TracedObjects, activitydiagram_TracedControlFlow, activitydiagramConfiguration_TracedControlToken, traceSystem_States_ActivityNode_running_State, traceSystem_activitydiagramConfiguration_TracedInputValue, traceSystem_activitydiagramConfiguration_TracedTrace, activitydiagram_TracedJoinNode, traceSystem_activitydiagramConfiguration_TracedForkedToken, TracedToken, traceSystem_activitydiagramConfiguration_TracedToken, traceSystem_activitydiagramConfiguration_TracedControlToken, traceSystem_activitydiagramConfiguration_TracedOffer, activitydiagram_traceSystem_Expression, activitydiagram_traceSystem_OpaqueAction, traceSystem_activitydiagram_TracedExecutableNode, TracedActivityNode, traceSystem_activitydiagram_TracedActivity, TracedNamedElement, traceSystem_activitydiagramConfiguration_TracedInput, traceSystem_activitydiagram_TracedBooleanVariable, TracedVariable, activitydiagram_traceSystem_BooleanVariable, traceSystem_activitydiagram_TracedForkNode, TracedControlNode, activitydiagram_traceSystem_ForkNode, traceSystem_activitydiagram_TracedControlFlow, TracedActivityEdge, activitydiagram_traceSystem_ControlFlow, traceSystem_activitydiagram_TracedActivityFinalNode, TracedFinalNode, activitydiagram_traceSystem_ActivityFinalNode, traceSystem_activitydiagram_TracedAction, TracedExecutableNode, traceSystem_activitydiagram_TracedFinalNode, traceSystem_activitydiagram_TracedStringVariable, activitydiagram_traceSystem_StringVariable, traceSystem_activitydiagram_TracedOpaqueAction, TracedAction, traceSystem_activitydiagram_TracedActivityEdge, traceSystem_activitydiagram_TracedJoinNode, activitydiagram_traceSystem_JoinNode, activitydiagram_traceSystem_Activity, traceSystem_activitydiagram_TracedVariable, activitydiagram_traceSystem_Value, traceSystem_activitydiagram_TracedMergeNode, activitydiagram_traceSystem_MergeNode, traceSystem_activitydiagram_TracedDecisionNode, activitydiagram_traceSystem_DecisionNode, traceSystem_activitydiagram_TracedIntegerVariable, activitydiagram_traceSystem_IntegerVariable, traceSystem_activitydiagram_TracedControlNode, traceSystem_activitydiagram_TracedActivityNode, traceSystem_activitydiagram_TracedNamedElement, traceSystem_activitydiagram_TracedInitialNode, activitydiagram_traceSystem_InitialNode},
    associations={globalTrace0, token_holder_States14, offer_offeredTokens_States16, activity_trace_States18, variable_currentValue_States20, inputValue_value_States22, inputValue_variable_States24, activityEdge_offers_States26, trace_executedNodes_States28, input_inputValues_States30, activityNode_heldTokens_States32, activityNode_running_States34, events1, tracedObjects3, staticObjectsPools5, eventsTriggeredDuringState7, forkedToken_baseToken_States9, forkedToken_remainingOffersCount_States10, forkedToken_baseTokenIsWithdrawn_States12, Activity_mainEntryEventOccurrence_Trace51, Activity_mainExitEventOccurrence_Trace52, Activity_initializeEntryEventOccurrence_Trace54, Activity_initializeExitEventOccurrence_Trace56, Activity_runEntryEventOccurrence_Trace58, Activity_runExitEventOccurrence_Trace60, Activity_runNodesEntryEventOccurrence_Trace62, Activity_runNodesExitEventOccurrence_Trace64, Activity_fireInitialNodeEntryEventOccurrence_Trace66, Activity_fireInitialNodeExitEventOccurrence_Trace68, pool_BooleanValues36, pool_IntegerComparisonExpressions38, pool_StringValues40, pool_BooleanBinaryExpressions42, pool_BooleanUnaryExpressions44, pool_IntegerValues46, pool_IntegerCalculationExpressions48, stateDuringWhichTriggered50, Activity_fireNodeExitEventOccurrence_Trace88, ActivityNode_run_activityNodeEntryEventOccurrence_Trace90, ActivityNode_run_activityNodeExitEventOccurrence_Trace92, ActivityNode_isRunningEntryEventOccurrence_Trace94, ActivityNode_isRunningExitEventOccurrence_Trace96, ActivityNode_terminate_activityNodeEntryEventOccurrence_Trace98, Activity_getEnabledNodesEntryEventOccurrence_Trace70, ActivityNode_terminate_activityNodeExitEventOccurrence_Trace100, Activity_getEnabledNodesExitEventOccurrence_Trace72, Activity_selectNextNodeEntryEventOccurrence_Trace74, Activity_selectNextNodeExitEventOccurrence_Trace76, Activity_terminateEntryEventOccurrence_Trace78, Activity_terminateExitEventOccurrence_Trace80, Activity_getInitialNodeEntryEventOccurrence_Trace82, Activity_getInitialNodeExitEventOccurrence_Trace84, Activity_fireNodeEntryEventOccurrence_Trace86, ActivityNode_removeTokenExitEventOccurrence_Trace116, ActivityNode_hasOffersEntryEventOccurrence_Trace118, ActivityNode_hasOffersExitEventOccurrence_Trace120, ActivityNode_isReadyEntryEventOccurrence_Trace122, ActivityNode_isReadyExitEventOccurrence_Trace124, ActivityEdge_sendOfferEntryEventOccurrence_Trace126, ActivityEdge_sendOfferExitEventOccurrence_Trace128, ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_Trace130, ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_Trace132, ActivityNode_sendOffersEntryEventOccurrence_Trace102, ActivityNode_sendOffersExitEventOccurrence_Trace104, ActivityNode_takeOfferedTokensEntryEventOccurrence_Trace106, ActivityNode_takeOfferedTokensExitEventOccurrence_Trace108, ActivityNode_addTokensEntryEventOccurrence_Trace110, ActivityNode_addTokensExitEventOccurrence_Trace112, ActivityNode_removeTokenEntryEventOccurrence_Trace114, Action_sendOffers_actionExitEventOccurrence_Trace148, Action_isReady_actionEntryEventOccurrence_Trace150, Action_isReady_actionExitEventOccurrence_Trace152, Action_fire_actionEntryEventOccurrence_Trace154, Action_fire_actionExitEventOccurrence_Trace156, OpaqueAction_doAction_opaqueActionEntryEventOccurrence_Trace158, OpaqueAction_doAction_opaqueActionExitEventOccurrence_Trace160, InitialNode_isReady_InitialNodeEntryEventOccurrence_Trace162, ActivityEdge_hasOfferEntryEventOccurrence_Trace134, ActivityEdge_hasOfferExitEventOccurrence_Trace136, ControlNode_isReady_ControlNodeEntryEventOccurrence_Trace138, ControlNode_isReady_ControlNodeExitEventOccurrence_Trace140, ControlNode_fire_controlNodeEntryEventOccurrence_Trace142, ControlNode_fire_controlNodeExitEventOccurrence_Trace144, Action_sendOffers_actionEntryEventOccurrence_Trace146, InitialNode_fire_initialNodeExitEventOccurrence_Trace168, ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_Trace170, ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_Trace172, ForkNode_fire_forkNodeEntryEventOccurrence_Trace174, ForkNode_fire_forkNodeExitEventOccurrence_Trace176, MergeNode_hasOffers_mergeNodeEntryEventOccurrence_Trace178, InitialNode_isReady_InitialNodeExitEventOccurrence_Trace164, StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_Trace194, InitialNode_fire_initialNodeEntryEventOccurrence_Trace166, StringVariable_setCurrentValue_stringVariableExitEventOccurrence_Trace196, StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_Trace198, StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_Trace200, BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_Trace202, BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_Trace204, MergeNode_hasOffers_mergeNodeExitEventOccurrence_Trace180, BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_Trace206, DecisionNode_fire_decisionNodeEntryEventOccurrence_Trace182, DecisionNode_fire_decisionNodeExitEventOccurrence_Trace184, IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_Trace186, IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_Trace188, IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_Trace190, IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_Trace192, IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_Trace216, IntegerCalculationExpression_evaluateADDEntryEventOccurrence_Trace218, IntegerCalculationExpression_evaluateADDExitEventOccurrence_Trace220, IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_Trace222, IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_Trace224, IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_Trace226, IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_Trace228, BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_Trace208, IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_Trace210, IntegerExpression_getOperandCurrentValuesExitEventOccurrence_Trace212, IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_Trace214, IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_Trace240, IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_Trace242, IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_Trace244, IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_Trace246, IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_Trace248, BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_Trace250, IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_Trace230, IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_Trace232, IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_Trace234, IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_Trace236, IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_Trace238, BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_Trace258, BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_Trace260, BooleanBinaryExpression_evaluateANDEntryEventOccurrence_Trace262, BooleanBinaryExpression_evaluateANDExitEventOccurrence_Trace264, BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_Trace252, BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_Trace254, BooleanUnaryExpression_evaluateNOTExitEventOccurrence_Trace256, Token_transferExitEventOccurrence_Trace276, Token_withdrawEntryEventOccurrence_Trace278, Token_withdrawExitEventOccurrence_Trace280, ForkedToken_withdraw_forkedTokenEntryEventOccurrence_Trace282, BooleanBinaryExpression_evaluateOREntryEventOccurrence_Trace266, ForkedToken_withdraw_forkedTokenExitEventOccurrence_Trace284, BooleanBinaryExpression_evaluateORExitEventOccurrence_Trace268, Token_isWithdrawnEntryEventOccurrence_Trace270, Token_isWithdrawnExitEventOccurrence_Trace272, Token_transferEntryEventOccurrence_Trace274, Offer_hasTokensExitEventOccurrence_Trace288, thisParam290, inputValuesParam291, correspondingEntryEvent293, thisParam295, inputValuesParam297, correspondingEntryEvent300, Offer_hasTokensEntryEventOccurrence_Trace286, correspondingEntryEvent308, thisParam310, correspondingEntryEvent312, thisParam314, correspondingEntryEvent316, enabledNodesReturn318, thisParam321, activityNodesParam323, correspondingEntryEvent326, thisParam302, correspondingEntryEvent304, thisParam306, initialNodeReturn339, thisParam342, nodeParam344, correspondingEntryEvent347, thisParam349, correspondingEntryEvent350, thisParam352, correspondingEntryEvent354, isRunningReturn356, selectedNodeReturn328, thisParam331, correspondingEntryEvent333, thisParam335, correspondingEntryEvent337, thisParam370, correspondingEntryEvent372, tokensReturn374, thisParam377, tokensParam379, correspondingEntryEvent382, thisParam384, tokenParam386, correspondingEntryEvent389, thisParam359, correspondingEntryEvent361, thisParam363, tokensParam365, correspondingEntryEvent368, thisParam405, tokensParam406, correspondingEntryEvent409, thisParam411, correspondingEntryEvent413, tokensReturn415, thisParam418, correspondingEntryEvent420, hasOfferReturn422, thisParam391, thisParam425, correspondingEntryEvent393, returnReturn395, thisParam398, correspondingEntryEvent400, isReadyReturn402, thisParam431, tokensParam433, correspondingEntryEvent435, thisParam437, correspondingEntryEvent438, thisParam440, correspondingEntryEvent442, isReadyReturn444, correspondingEntryEvent426, thisParam454, isReadyReturn428, correspondingEntryEvent455, thisParam457, correspondingEntryEvent458, isReadyReturn460, thisParam463, tokensParam465, correspondingEntryEvent468, thisParam470, tokensParam471, correspondingEntryEvent474, thisParam447, tokensParam449, correspondingEntryEvent452, thisParam482, correspondingEntryEvent483, returnReturn485, thisParam488, tokensParam489, correspondingEntryEvent492, thisParam476, correspondingEntryEvent501, tokensParam477, valueReturn503, correspondingEntryEvent480, thisParam506, valueParam507, correspondingEntryEvent510, thisParam512, correspondingEntryEvent514, valueReturn516, thisParam519, valueParam520, thisParam494, valueParam495, correspondingEntryEvent523, correspondingEntryEvent497, thisParam499, thisParam532, correspondingEntryEvent533, operand1ValueReturn535, operand2ValueReturn538, thisParam541, correspondingEntryEvent542, thisParam544, correspondingEntryEvent546, resultReturn548, thisParam525, correspondingEntryEvent527, valueReturn529, thisParam558, correspondingEntryEvent559, thisParam561, correspondingEntryEvent563, resultReturn565, thisParam568, correspondingEntryEvent570, resultReturn572, thisParam575, thisParam551, correspondingEntryEvent553, resultReturn555, thisParam582, correspondingEntryEvent584, resultReturn586, thisParam589, correspondingEntryEvent591, resultReturn593, thisParam596, correspondingEntryEvent577, resultReturn603, resultReturn579, thisParam606, correspondingEntryEvent607, thisParam609, correspondingEntryEvent611, resultReturn613, thisParam616, correspondingEntryEvent618, correspondingEntryEvent597, thisParam599, correspondingEntryEvent601, thisParam623, correspondingEntryEvent625, isWithdrawnReturn627, thisParam630, holderParam632, correspondingEntryEvent635, transferredTokenReturn637, resultReturn620, correspondingEntryEvent645, thisParam647, correspondingEntryEvent648, hasTokensReturn650, baseToken653, parent655, globalStates656, parent658, globalStates661, thisParam640, correspondingEntryEvent642, thisParam644, globalStates673, offeredTokens675, parent677, globalStates680, trace682, parent683, globalStates685, currentValue687, parent688, globalStates691, value693, parent695, globalStates698, parent663, globalStates666, holder668, parent670, globalStates704, offers706, parent708, globalStates711, executedNodes713, parent715, globalStates718, inputValues720, parent721, globalStates724, variable700, globalStates736, parent701, activitydiagramConfiguration_tracedForkedTokens738, activitydiagram_tracedBooleanVariables740, activitydiagram_tracedForkNodes743, activitydiagram_tracedControlFlows746, activitydiagram_tracedActivityFinalNodes748, activitydiagram_tracedStringVariables751, activitydiagram_tracedOpaqueActions754, activitydiagramConfiguration_tracedControlTokens757, activitydiagramConfiguration_tracedOffers759, heldTokens726, parent728, globalStates731, parent733, activitydiagram_tracedDecisionNodes771, valueTrace802, variableTrace805, activitydiagram_tracedIntegerVariables774, activitydiagram_tracedJoinNodes777, activitydiagramConfiguration_tracedTraces779, activitydiagramConfiguration_tracedInputs782, activitydiagram_tracedInitialNodes784, baseTokenTrace787, remainingOffersCountTrace790, activitydiagram_tracedActivitys762, baseTokenIsWithdrawnTrace793, activitydiagramConfiguration_tracedInputValues765, holderTrace796, activitydiagram_tracedMergeNodes768, offeredTokensTrace799, expressions822, originalObject823, nodes825, executedNodesTrace808, edges827, inputValuesTrace811, originalObject814, originalObject815, guard816, originalObject818, originalObject820, originalObject821, source848, target850, offersTrace853, locals830, inputs833, originalObject836, traceTrace838, initialValue841, currentValueTrace842, originalObject845, originalObject846, originalObject847, originalObject856, outgoing857, incoming859, activity862, heldTokensTrace865, runningTrace868, originalObject871},
    generalizations={gen_traceSystem_Events_Activity_mainEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_mainExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_initializeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_initializeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_runNodesExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_fireInitialNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_fireInitialNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_getEnabledNodesEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_getEnabledNodesExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_selectNextNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_selectNextNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_runEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_runExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_runNodesEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_fireNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_fireNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_run_activityNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_run_activityNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_isRunningEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_isRunningExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_terminateEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_terminateExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_getInitialNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Activity_getInitialNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_takeOfferedTokensEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_takeOfferedTokensExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_addTokensEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_addTokensExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_removeTokenEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_removeTokenExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_hasOffersEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_terminate_activityNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_terminate_activityNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_sendOffersEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_sendOffersExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_sendOfferEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_sendOfferExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_takeOfferedTokens_activityEdgeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_hasOfferEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityEdge_hasOfferExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ControlNode_isReady_ControlNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_hasOffersExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ControlNode_isReady_ControlNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_isReadyEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityNode_isReadyExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ControlNode_fire_controlNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ControlNode_fire_controlNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_sendOffers_actionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_sendOffers_actionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_isReady_actionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_isReady_actionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_OpaqueAction_doAction_opaqueActionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_InitialNode_isReady_InitialNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_InitialNode_isReady_InitialNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_InitialNode_fire_initialNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_InitialNode_fire_initialNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ActivityFinalNode_fire_activityFinalNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_fire_actionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Action_fire_actionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_OpaqueAction_doAction_opaqueActionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_MergeNode_hasOffers_mergeNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_MergeNode_hasOffers_mergeNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_DecisionNode_fire_decisionNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_DecisionNode_fire_decisionNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ForkNode_fire_forkNodeEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ForkNode_fire_forkNodeExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_StringVariable_setCurrentValue_stringVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_StringVariable_setCurrentValue_stringVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_StringVariable_getCurrentValueValue_stringVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanVariable_setCurrentValue_boolenVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerVariable_setCurrentValue_integerVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerVariable_getCurrentValueValue_integerVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerExpression_getOperandCurrentValuesEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerExpression_getOperandCurrentValuesExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_execute_integerCalculationExpressionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_evaluateADDEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_evaluateADDExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanVariable_getCurrentValueValue_booleanVariableExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLEREntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLERExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateSMALLER_EQUALSExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateEQUALSExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerCalculationExpression_evaluateSUBTRACTExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_execute_IntegerComparisionExpressionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATER_EQUALSExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATEREntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_IntegerComparisonExpression_evaluateGREATERExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_execute_booleanBinaryExpressionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_evaluateANDEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_evaluateANDExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_evaluateOREntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanBinaryExpression_evaluateORExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanUnaryExpression_execute_booleanUnaryExpressionExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanUnaryExpression_evaluateNOTEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_BooleanUnaryExpression_evaluateNOTExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_isWithdrawnEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_isWithdrawnExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_transferEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_transferExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_withdrawEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_ForkedToken_withdraw_forkedTokenExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Offer_hasTokensEntryEventOccurrence_EventOccurrence, gen_traceSystem_Events_Offer_hasTokensExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_Token_withdrawExitEventOccurrence_EventOccurrence, gen_traceSystem_Events_ForkedToken_withdraw_forkedTokenEntryEventOccurrence_EventOccurrence, gen_traceSystem_activitydiagramConfiguration_TracedForkedToken_TracedToken, gen_traceSystem_activitydiagramConfiguration_TracedControlToken_TracedToken, gen_traceSystem_activitydiagram_TracedExecutableNode_TracedActivityNode, gen_traceSystem_activitydiagram_TracedActivity_TracedNamedElement, gen_traceSystem_activitydiagram_TracedBooleanVariable_TracedVariable, gen_traceSystem_activitydiagram_TracedForkNode_TracedControlNode, gen_traceSystem_activitydiagram_TracedControlFlow_TracedActivityEdge, gen_traceSystem_activitydiagram_TracedActivityFinalNode_TracedFinalNode, gen_traceSystem_activitydiagram_TracedAction_TracedExecutableNode, gen_traceSystem_activitydiagram_TracedFinalNode_TracedControlNode, gen_traceSystem_activitydiagram_TracedStringVariable_TracedVariable, gen_traceSystem_activitydiagram_TracedOpaqueAction_TracedAction, gen_traceSystem_activitydiagram_TracedActivityEdge_TracedNamedElement, gen_traceSystem_activitydiagram_TracedJoinNode_TracedControlNode, gen_traceSystem_activitydiagram_TracedVariable_TracedNamedElement, gen_traceSystem_activitydiagram_TracedMergeNode_TracedControlNode, gen_traceSystem_activitydiagram_TracedDecisionNode_TracedControlNode, gen_traceSystem_activitydiagram_TracedIntegerVariable_TracedVariable, gen_traceSystem_activitydiagram_TracedControlNode_TracedActivityNode, gen_traceSystem_activitydiagram_TracedActivityNode_TracedNamedElement, gen_traceSystem_activitydiagram_TracedInitialNode_TracedControlNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)