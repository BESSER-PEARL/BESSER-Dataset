import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    trace::activitydiagramConfiguration::TracedOffer,
    trace::activitydiagramConfiguration::TracedInput,
    TracedToken,
    trace::activitydiagramConfiguration::TracedForkedToken,
    trace::activitydiagramConfiguration::TracedControlToken,
    trace::activitydiagramConfiguration::TracedToken,
    trace::activitydiagramConfiguration::TracedInputValue,
    activitydiagram::trace::DecisionNode,
    activitydiagram::trace::JoinNode,
    activitydiagram::trace::OpaqueAction,
    trace::activitydiagramConfiguration::TracedTrace,
    activitydiagram::trace::InitialNode,
    activitydiagram::trace::ForkNode,
    activitydiagramConfiguration::TracedForkedToken,
    activitydiagram::TracedVariable,
    trace::States::InputValue::variable::State,
    States::trace::GlobalState,
    Events::trace::BooleanBinaryExpression,
    Events::trace::BooleanUnaryExpression,
    Events::trace::IntegerComparisonExpression,
    Events::trace::IntegerExpression,
    activitydiagram::TracedBooleanVariable,
    Events::trace::IntegerCalculationExpression,
    activitydiagram::TracedStringVariable,
    Events::trace::Value,
    activitydiagram::TracedIntegerVariable,
    activitydiagram::TracedDecisionNode,
    activitydiagram::TracedMergeNode,
    activitydiagram::TracedInitialNode,
    activitydiagram::TracedForkNode,
    activitydiagram::TracedActivityFinalNode,
    activitydiagram::TracedAction,
    activitydiagram::TracedOpaqueAction,
    activitydiagramConfiguration::TracedToken,
    activitydiagram::TracedControlNode,
    activitydiagram::TracedActivityEdge,
    activitydiagram::TracedActivityNode,
    Offer::hasTokensExitEventOccurrence,
    Events::trace::EObject,
    activitydiagram::TracedActivity,
    Token::isWithdrawnExitEventOccurrence,
    Token::isWithdrawnEntryEventOccurrence,
    BooleanBinaryExpression::evaluateORExitEventOccurrence,
    Offer::hasTokensEntryEventOccurrence,
    ForkedToken::withdraw::forkedTokenExitEventOccurrence,
    ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
    Token::withdrawExitEventOccurrence,
    Token::withdrawEntryEventOccurrence,
    Token::transferExitEventOccurrence,
    Token::transferEntryEventOccurrence,
    BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
    BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
    BooleanBinaryExpression::evaluateOREntryEventOccurrence,
    BooleanBinaryExpression::evaluateANDExitEventOccurrence,
    BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
    BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
    BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
    BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
    BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
    IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
    IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
    IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
    IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
    IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
    IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
    IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
    IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
    IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
    IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
    IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
    IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
    IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
    IntegerCalculationExpression::evaluateADDExitEventOccurrence,
    StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
    IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
    IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
    IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
    BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
    BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
    BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
    BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
    StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
    StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
    StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
    InitialNode::fire::initialNodeExitEventOccurrence,
    IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
    InitialNode::fire::initialNodeEntryEventOccurrence,
    IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
    IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
    DecisionNode::fire::decisionNodeExitEventOccurrence,
    DecisionNode::fire::decisionNodeEntryEventOccurrence,
    MergeNode::hasOffers::mergeNodeExitEventOccurrence,
    MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
    ForkNode::fire::forkNodeExitEventOccurrence,
    ForkNode::fire::forkNodeEntryEventOccurrence,
    ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
    ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
    Action::isReady::actionEntryEventOccurrence,
    Action::sendOffers::actionExitEventOccurrence,
    Action::sendOffers::actionEntryEventOccurrence,
    ControlNode::fire::controlNodeExitEventOccurrence,
    InitialNode::isReady::InitialNodeExitEventOccurrence,
    InitialNode::isReady::InitialNodeEntryEventOccurrence,
    OpaqueAction::doAction::opaqueActionExitEventOccurrence,
    OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
    Action::fire::actionExitEventOccurrence,
    Action::fire::actionEntryEventOccurrence,
    ActivityNode::isReadyExitEventOccurrence,
    Action::isReady::actionExitEventOccurrence,
    ActivityNode::isReadyEntryEventOccurrence,
    ControlNode::fire::controlNodeEntryEventOccurrence,
    ControlNode::isReady::ControlNodeExitEventOccurrence,
    ControlNode::isReady::ControlNodeEntryEventOccurrence,
    ActivityEdge::hasOfferExitEventOccurrence,
    ActivityEdge::hasOfferEntryEventOccurrence,
    ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
    ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
    ActivityEdge::sendOfferExitEventOccurrence,
    ActivityEdge::sendOfferEntryEventOccurrence,
    ActivityNode::isRunningExitEventOccurrence,
    ActivityNode::isRunningEntryEventOccurrence,
    ActivityNode::run::activityNodeExitEventOccurrence,
    ActivityNode::hasOffersExitEventOccurrence,
    ActivityNode::run::activityNodeEntryEventOccurrence,
    ActivityNode::hasOffersEntryEventOccurrence,
    ActivityNode::removeTokenExitEventOccurrence,
    ActivityNode::removeTokenEntryEventOccurrence,
    ActivityNode::addTokensExitEventOccurrence,
    ActivityNode::addTokensEntryEventOccurrence,
    ActivityNode::takeOfferedTokensExitEventOccurrence,
    ActivityNode::takeOfferedTokensEntryEventOccurrence,
    ActivityNode::sendOffersExitEventOccurrence,
    ActivityNode::sendOffersEntryEventOccurrence,
    ActivityNode::terminate::activityNodeExitEventOccurrence,
    ActivityNode::terminate::activityNodeEntryEventOccurrence,
    Activity::runNodesExitEventOccurrence,
    Activity::runNodesEntryEventOccurrence,
    Activity::runExitEventOccurrence,
    Activity::runEntryEventOccurrence,
    Activity::initializeExitEventOccurrence,
    Activity::initializeEntryEventOccurrence,
    Activity::fireNodeExitEventOccurrence,
    Activity::fireNodeEntryEventOccurrence,
    Activity::getInitialNodeExitEventOccurrence,
    Activity::getInitialNodeEntryEventOccurrence,
    Activity::terminateExitEventOccurrence,
    Activity::terminateEntryEventOccurrence,
    Activity::selectNextNodeExitEventOccurrence,
    Activity::selectNextNodeEntryEventOccurrence,
    activitydiagram::trace::ActivityFinalNode,
    TracedFinalNode,
    trace::activitydiagram::TracedActivityFinalNode,
    TracedExecutableNode,
    activitydiagram::trace::Expression,
    trace::activitydiagram::TracedAction,
    TracedAction,
    trace::activitydiagram::TracedOpaqueAction,
    activitydiagram::trace::StringVariable,
    activitydiagram::trace::Activity,
    TracedNamedElement,
    trace::activitydiagram::TracedActivityNode,
    trace::activitydiagram::TracedActivity,
    trace::activitydiagram::TracedActivityEdge,
    activitydiagram::trace::IntegerVariable,
    TracedActivityNode,
    trace::activitydiagram::TracedControlNode,
    trace::activitydiagram::TracedExecutableNode,
    activitydiagram::trace::BooleanVariable,
    TracedVariable,
    trace::activitydiagram::TracedIntegerVariable,
    trace::activitydiagram::TracedStringVariable,
    trace::activitydiagram::TracedBooleanVariable,
    activitydiagram::trace::MergeNode,
    TracedControlNode,
    trace::activitydiagram::TracedDecisionNode,
    trace::activitydiagram::TracedInitialNode,
    trace::activitydiagram::TracedForkNode,
    trace::activitydiagram::TracedFinalNode,
    trace::activitydiagram::TracedJoinNode,
    trace::activitydiagram::TracedMergeNode,
    activitydiagram::trace::ControlFlow,
    TracedActivityEdge,
    trace::activitydiagram::TracedControlFlow,
    activitydiagram::TracedJoinNode,
    activitydiagram::trace::Value,
    trace::activitydiagram::TracedVariable,
    trace::activitydiagram::TracedNamedElement,
    activitydiagramConfiguration::TracedControlToken,
    activitydiagram::TracedControlFlow,
    trace::Traced::TracedObjects,
    activitydiagramConfiguration::TracedTrace,
    trace::States::Activity::trace::State,
    trace::States::ActivityNode::heldTokens::State,
    trace::States::ActivityNode::running::State,
    trace::States::Offer::offeredTokens::State,
    trace::States::Variable::currentValue::State,
    trace::States::Trace::executedNodes::State,
    trace::States::ForkedToken::baseTokenIsWithdrawn::State,
    trace::States::ForkedToken::baseToken::State,
    trace::States::ForkedToken::remainingOffersCount::State,
    activitydiagramConfiguration::TracedInput,
    trace::States::Input::inputValues::State,
    trace::States::Token::holder::State,
    trace::States::ActivityEdge::offers::State,
    activitydiagramConfiguration::TracedInputValue,
    States::trace::Value,
    trace::States::InputValue::value::State,
    activitydiagramConfiguration::TracedOffer,
    TracedObjects,
    Events,
    trace::GlobalState,
    Activity::getEnabledNodesExitEventOccurrence,
    Activity::getEnabledNodesEntryEventOccurrence,
    Activity::fireInitialNodeExitEventOccurrence,
    ActivityNode::heldTokens::State,
    Activity::fireInitialNodeEntryEventOccurrence,
    ActivityNode::running::State,
    Activity::mainExitEventOccurrence,
    Activity::mainEntryEventOccurrence,
    trace::Events::Events,
    Events::trace::GlobalState,
    trace::Events::EventOccurrence,
    trace::IntegerCalculationExpression,
    trace::BooleanUnaryExpression,
    trace::IntegerComparisonExpression,
    trace::BooleanValue,
    trace::IntegerValue,
    trace::StringValue,
    trace::BooleanBinaryExpression,
    Trace::executedNodes::State,
    Activity::trace::State,
    trace::Trace,
    Offer::offeredTokens::State,
    Variable::currentValue::State,
    ActivityEdge::offers::State,
    ForkedToken::baseTokenIsWithdrawn::State,
    ForkedToken::baseToken::State,
    ForkedToken::remainingOffersCount::State,
    Input::inputValues::State,
    Token::holder::State,
    InputValue::variable::State,
    InputValue::value::State,
    EventOccurrence,
    trace::Events::Action::isReady::actionExitEventOccurrence,
    trace::Events::Action::fire::actionExitEventOccurrence,
    trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence,
    trace::Events::Activity::fireInitialNodeEntryEventOccurrence,
    trace::Events::Activity::terminateExitEventOccurrence,
    trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence,
    trace::Events::Offer::hasTokensEntryEventOccurrence,
    trace::Events::Action::sendOffers::actionEntryEventOccurrence,
    trace::Events::Activity::fireNodeExitEventOccurrence,
    trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence,
    trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
    trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence,
    trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
    trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
    trace::Events::Activity::runNodesExitEventOccurrence,
    trace::Events::Activity::getInitialNodeEntryEventOccurrence,
    trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
    trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence,
    trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
    trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence,
    trace::Events::Activity::fireNodeEntryEventOccurrence,
    trace::Events::Activity::fireInitialNodeExitEventOccurrence,
    trace::Events::Token::withdrawExitEventOccurrence,
    trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
    trace::Events::ActivityEdge::sendOfferEntryEventOccurrence,
    trace::Events::ActivityNode::removeTokenExitEventOccurrence,
    trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
    trace::Events::Activity::mainExitEventOccurrence,
    trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
    trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
    trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
    trace::Events::Activity::runNodesEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
    trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
    trace::Events::Activity::getInitialNodeExitEventOccurrence,
    trace::Events::Activity::getEnabledNodesExitEventOccurrence,
    trace::Events::Action::isReady::actionEntryEventOccurrence,
    trace::Events::ActivityNode::addTokensEntryEventOccurrence,
    trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
    trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
    trace::Events::ActivityNode::removeTokenEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
    trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
    trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence,
    trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence,
    trace::Events::Action::fire::actionEntryEventOccurrence,
    trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
    trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence,
    trace::Events::ActivityNode::isRunningEntryEventOccurrence,
    trace::Events::ActivityNode::sendOffersEntryEventOccurrence,
    trace::Events::Token::isWithdrawnEntryEventOccurrence,
    trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
    trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence,
    trace::Events::ActivityNode::addTokensExitEventOccurrence,
    trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
    trace::Events::ActivityEdge::sendOfferExitEventOccurrence,
    trace::Events::ActivityNode::hasOffersExitEventOccurrence,
    trace::Events::InitialNode::fire::initialNodeExitEventOccurrence,
    trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
    trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
    trace::Events::Action::sendOffers::actionExitEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
    trace::Events::ControlNode::fire::controlNodeExitEventOccurrence,
    trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
    trace::Events::Token::withdrawEntryEventOccurrence,
    trace::Events::ActivityNode::isReadyEntryEventOccurrence,
    trace::Events::ActivityEdge::hasOfferExitEventOccurrence,
    trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence,
    trace::Events::Activity::runExitEventOccurrence,
    trace::Events::ActivityNode::hasOffersEntryEventOccurrence,
    trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
    trace::Events::ActivityNode::sendOffersExitEventOccurrence,
    trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
    trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
    trace::Events::ActivityNode::run::activityNodeExitEventOccurrence,
    trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
    trace::Events::Offer::hasTokensExitEventOccurrence,
    trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence,
    trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
    trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
    trace::Events::Activity::initializeExitEventOccurrence,
    trace::Events::Activity::initializeEntryEventOccurrence,
    trace::Events::Activity::selectNextNodeEntryEventOccurrence,
    trace::Events::ForkNode::fire::forkNodeExitEventOccurrence,
    trace::Events::Token::isWithdrawnExitEventOccurrence,
    trace::Events::ActivityNode::isRunningExitEventOccurrence,
    trace::Events::ActivityEdge::hasOfferEntryEventOccurrence,
    trace::Events::Activity::terminateEntryEventOccurrence,
    trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence,
    trace::Events::Token::transferEntryEventOccurrence,
    trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
    trace::Events::Activity::runEntryEventOccurrence,
    trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence,
    trace::Events::Token::transferExitEventOccurrence,
    trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence,
    trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
    trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
    trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence,
    trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence,
    trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence,
    trace::Events::ActivityNode::isReadyExitEventOccurrence,
    trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
    trace::Events::Activity::selectNextNodeExitEventOccurrence,
    trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
    trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
    trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
    trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence,
    trace::Events::Activity::getEnabledNodesEntryEventOccurrence,
    trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
    trace::Events::Activity::mainEntryEventOccurrence,
    trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
    trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
    trace::StaticObjectsPools,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_trace::activitydiagramconfiguration::tracedoffer_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedOffer)


def test_trace::activitydiagramconfiguration::tracedoffer_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedOffer.__init__)


def test_trace::activitydiagramconfiguration::tracedoffer_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedinput_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedInput)


def test_trace::activitydiagramconfiguration::tracedinput_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedInput.__init__)


def test_trace::activitydiagramconfiguration::tracedinput_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(TracedToken)


def test_tracedtoken_constructor_exists():
    assert callable(TracedToken.__init__)


def test_tracedtoken_constructor_args():
    sig = inspect.signature(TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedForkedToken)


def test_trace::activitydiagramconfiguration::tracedforkedtoken_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedForkedToken.__init__)


def test_trace::activitydiagramconfiguration::tracedforkedtoken_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedControlToken)


def test_trace::activitydiagramconfiguration::tracedcontroltoken_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedControlToken.__init__)


def test_trace::activitydiagramconfiguration::tracedcontroltoken_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedtoken_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedToken)


def test_trace::activitydiagramconfiguration::tracedtoken_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedToken.__init__)


def test_trace::activitydiagramconfiguration::tracedtoken_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedInputValue)


def test_trace::activitydiagramconfiguration::tracedinputvalue_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedInputValue.__init__)


def test_trace::activitydiagramconfiguration::tracedinputvalue_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::DecisionNode)


def test_activitydiagram::trace::decisionnode_constructor_exists():
    assert callable(activitydiagram::trace::DecisionNode.__init__)


def test_activitydiagram::trace::decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::JoinNode)


def test_activitydiagram::trace::joinnode_constructor_exists():
    assert callable(activitydiagram::trace::JoinNode.__init__)


def test_activitydiagram::trace::joinnode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::OpaqueAction)


def test_activitydiagram::trace::opaqueaction_constructor_exists():
    assert callable(activitydiagram::trace::OpaqueAction.__init__)


def test_activitydiagram::trace::opaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::trace::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagramconfiguration::tracedtrace_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagramConfiguration::TracedTrace)


def test_trace::activitydiagramconfiguration::tracedtrace_constructor_exists():
    assert callable(trace::activitydiagramConfiguration::TracedTrace.__init__)


def test_trace::activitydiagramconfiguration::tracedtrace_constructor_args():
    sig = inspect.signature(trace::activitydiagramConfiguration::TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::InitialNode)


def test_activitydiagram::trace::initialnode_constructor_exists():
    assert callable(activitydiagram::trace::InitialNode.__init__)


def test_activitydiagram::trace::initialnode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::ForkNode)


def test_activitydiagram::trace::forknode_constructor_exists():
    assert callable(activitydiagram::trace::ForkNode.__init__)


def test_activitydiagram::trace::forknode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedForkedToken)


def test_activitydiagramconfiguration::tracedforkedtoken_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedForkedToken.__init__)


def test_activitydiagramconfiguration::tracedforkedtoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedVariable)


def test_activitydiagram::tracedvariable_constructor_exists():
    assert callable(activitydiagram::TracedVariable.__init__)


def test_activitydiagram::tracedvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::inputvalue::variable::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::InputValue::variable::State)


def test_trace::states::inputvalue::variable::state_constructor_exists():
    assert callable(trace::States::InputValue::variable::State.__init__)


def test_trace::states::inputvalue::variable::state_constructor_args():
    sig = inspect.signature(trace::States::InputValue::variable::State.__init__)
    params = list(sig.parameters.keys())



def test_states::trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(States::trace::GlobalState)


def test_states::trace::globalstate_constructor_exists():
    assert callable(States::trace::GlobalState.__init__)


def test_states::trace::globalstate_constructor_args():
    sig = inspect.signature(States::trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events::trace::BooleanBinaryExpression)


def test_events::trace::booleanbinaryexpression_constructor_exists():
    assert callable(Events::trace::BooleanBinaryExpression.__init__)


def test_events::trace::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(Events::trace::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events::trace::BooleanUnaryExpression)


def test_events::trace::booleanunaryexpression_constructor_exists():
    assert callable(Events::trace::BooleanUnaryExpression.__init__)


def test_events::trace::booleanunaryexpression_constructor_args():
    sig = inspect.signature(Events::trace::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(Events::trace::IntegerComparisonExpression)


def test_events::trace::integercomparisonexpression_constructor_exists():
    assert callable(Events::trace::IntegerComparisonExpression.__init__)


def test_events::trace::integercomparisonexpression_constructor_args():
    sig = inspect.signature(Events::trace::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::integerexpression_is_not_abstract():
    assert not inspect.isabstract(Events::trace::IntegerExpression)


def test_events::trace::integerexpression_constructor_exists():
    assert callable(Events::trace::IntegerExpression.__init__)


def test_events::trace::integerexpression_constructor_args():
    sig = inspect.signature(Events::trace::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedBooleanVariable)


def test_activitydiagram::tracedbooleanvariable_constructor_exists():
    assert callable(activitydiagram::TracedBooleanVariable.__init__)


def test_activitydiagram::tracedbooleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(Events::trace::IntegerCalculationExpression)


def test_events::trace::integercalculationexpression_constructor_exists():
    assert callable(Events::trace::IntegerCalculationExpression.__init__)


def test_events::trace::integercalculationexpression_constructor_args():
    sig = inspect.signature(Events::trace::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedStringVariable)


def test_activitydiagram::tracedstringvariable_constructor_exists():
    assert callable(activitydiagram::TracedStringVariable.__init__)


def test_activitydiagram::tracedstringvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::value_is_not_abstract():
    assert not inspect.isabstract(Events::trace::Value)


def test_events::trace::value_constructor_exists():
    assert callable(Events::trace::Value.__init__)


def test_events::trace::value_constructor_args():
    sig = inspect.signature(Events::trace::Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedIntegerVariable)


def test_activitydiagram::tracedintegervariable_constructor_exists():
    assert callable(activitydiagram::TracedIntegerVariable.__init__)


def test_activitydiagram::tracedintegervariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedDecisionNode)


def test_activitydiagram::traceddecisionnode_constructor_exists():
    assert callable(activitydiagram::TracedDecisionNode.__init__)


def test_activitydiagram::traceddecisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedMergeNode)


def test_activitydiagram::tracedmergenode_constructor_exists():
    assert callable(activitydiagram::TracedMergeNode.__init__)


def test_activitydiagram::tracedmergenode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedInitialNode)


def test_activitydiagram::tracedinitialnode_constructor_exists():
    assert callable(activitydiagram::TracedInitialNode.__init__)


def test_activitydiagram::tracedinitialnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedforknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedForkNode)


def test_activitydiagram::tracedforknode_constructor_exists():
    assert callable(activitydiagram::TracedForkNode.__init__)


def test_activitydiagram::tracedforknode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedActivityFinalNode)


def test_activitydiagram::tracedactivityfinalnode_constructor_exists():
    assert callable(activitydiagram::TracedActivityFinalNode.__init__)


def test_activitydiagram::tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedAction)


def test_activitydiagram::tracedaction_constructor_exists():
    assert callable(activitydiagram::TracedAction.__init__)


def test_activitydiagram::tracedaction_constructor_args():
    sig = inspect.signature(activitydiagram::TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedOpaqueAction)


def test_activitydiagram::tracedopaqueaction_constructor_exists():
    assert callable(activitydiagram::TracedOpaqueAction.__init__)


def test_activitydiagram::tracedopaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedToken)


def test_activitydiagramconfiguration::tracedtoken_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedToken.__init__)


def test_activitydiagramconfiguration::tracedtoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedControlNode)


def test_activitydiagram::tracedcontrolnode_constructor_exists():
    assert callable(activitydiagram::TracedControlNode.__init__)


def test_activitydiagram::tracedcontrolnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedActivityEdge)


def test_activitydiagram::tracedactivityedge_constructor_exists():
    assert callable(activitydiagram::TracedActivityEdge.__init__)


def test_activitydiagram::tracedactivityedge_constructor_args():
    sig = inspect.signature(activitydiagram::TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedActivityNode)


def test_activitydiagram::tracedactivitynode_constructor_exists():
    assert callable(activitydiagram::TracedActivityNode.__init__)


def test_activitydiagram::tracedactivitynode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_offer::hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Offer::hasTokensExitEventOccurrence)


def test_offer::hastokensexiteventoccurrence_constructor_exists():
    assert callable(Offer::hasTokensExitEventOccurrence.__init__)


def test_offer::hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(Offer::hasTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::eobject_is_not_abstract():
    assert not inspect.isabstract(Events::trace::EObject)


def test_events::trace::eobject_constructor_exists():
    assert callable(Events::trace::EObject.__init__)


def test_events::trace::eobject_constructor_args():
    sig = inspect.signature(Events::trace::EObject.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedActivity)


def test_activitydiagram::tracedactivity_constructor_exists():
    assert callable(activitydiagram::TracedActivity.__init__)


def test_activitydiagram::tracedactivity_constructor_args():
    sig = inspect.signature(activitydiagram::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_token::iswithdrawnexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::isWithdrawnExitEventOccurrence)


def test_token::iswithdrawnexiteventoccurrence_constructor_exists():
    assert callable(Token::isWithdrawnExitEventOccurrence.__init__)


def test_token::iswithdrawnexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token::isWithdrawnExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::iswithdrawnentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::isWithdrawnEntryEventOccurrence)


def test_token::iswithdrawnentryeventoccurrence_constructor_exists():
    assert callable(Token::isWithdrawnEntryEventOccurrence.__init__)


def test_token::iswithdrawnentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token::isWithdrawnEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::evaluateorexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::evaluateORExitEventOccurrence)


def test_booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)


def test_booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_offer::hastokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Offer::hasTokensEntryEventOccurrence)


def test_offer::hastokensentryeventoccurrence_constructor_exists():
    assert callable(Offer::hasTokensEntryEventOccurrence.__init__)


def test_offer::hastokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(Offer::hasTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::withdraw::forkedtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::withdraw::forkedTokenExitEventOccurrence)


def test_forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_exists():
    assert callable(ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)


def test_forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::withdraw::forkedtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::withdraw::forkedTokenEntryEventOccurrence)


def test_forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_exists():
    assert callable(ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)


def test_forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::withdrawexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::withdrawExitEventOccurrence)


def test_token::withdrawexiteventoccurrence_constructor_exists():
    assert callable(Token::withdrawExitEventOccurrence.__init__)


def test_token::withdrawexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token::withdrawExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::withdrawentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::withdrawEntryEventOccurrence)


def test_token::withdrawentryeventoccurrence_constructor_exists():
    assert callable(Token::withdrawEntryEventOccurrence.__init__)


def test_token::withdrawentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token::withdrawEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::transferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::transferExitEventOccurrence)


def test_token::transferexiteventoccurrence_constructor_exists():
    assert callable(Token::transferExitEventOccurrence.__init__)


def test_token::transferexiteventoccurrence_constructor_args():
    sig = inspect.signature(Token::transferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::transferEntryEventOccurrence)


def test_token::transferentryeventoccurrence_constructor_exists():
    assert callable(Token::transferEntryEventOccurrence.__init__)


def test_token::transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token::transferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression::evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)


def test_booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)


def test_booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)


def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)


def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::evaluateorentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::evaluateOREntryEventOccurrence)


def test_booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)


def test_booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::evaluateandexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::evaluateANDExitEventOccurrence)


def test_booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)


def test_booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::evaluateandentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::evaluateANDEntryEventOccurrence)


def test_booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)


def test_booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)


def test_booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)


def test_booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)


def test_booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)


def test_booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression::evaluatenotexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::evaluateNOTExitEventOccurrence)


def test_booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)


def test_booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)


def test_integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)


def test_integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)


def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)


def test_booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)


def test_booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluategreaterexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)


def test_integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluategreaterentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)


def test_integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)


def test_integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)


def test_integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)


def test_integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluateequalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)


def test_integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluateequalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)


def test_integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)


def test_integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)


def test_integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)


def test_integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)


def test_integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)


def test_integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression::getoperandcurrentvaluesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression::getOperandCurrentValuesExitEventOccurrence)


def test_integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_exists():
    assert callable(IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)


def test_integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::evaluatesmallerentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)


def test_integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)


def test_integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)


def test_integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)


def test_integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)


def test_integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)


def test_integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::evaluatesubtractexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)


def test_integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)


def test_integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::evaluatesubtractentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)


def test_integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)


def test_integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::evaluateaddexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::evaluateADDExitEventOccurrence)


def test_integercalculationexpression::evaluateaddexiteventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)


def test_integercalculationexpression::evaluateaddexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)


def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)


def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integercalculationexpression::evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::evaluateADDEntryEventOccurrence)


def test_integercalculationexpression::evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)


def test_integercalculationexpression::evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)


def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)


def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)


def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)


def test_booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_exists():
    assert callable(BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)


def test_booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)


def test_booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_exists():
    assert callable(BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)


def test_booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)


def test_booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_exists():
    assert callable(BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)


def test_booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)


def test_booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_exists():
    assert callable(BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)


def test_booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)


def test_stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)


def test_stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)


def test_stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)


def test_stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable::setCurrentValue::stringVariableExitEventOccurrence)


def test_stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)


def test_stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode::fire::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::fire::initialNodeExitEventOccurrence)


def test_initialnode::fire::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(InitialNode::fire::initialNodeExitEventOccurrence.__init__)


def test_initialnode::fire::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::fire::initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)


def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)


def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode::fire::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::fire::initialNodeEntryEventOccurrence)


def test_initialnode::fire::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(InitialNode::fire::initialNodeEntryEventOccurrence.__init__)


def test_initialnode::fire::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::fire::initialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::setcurrentvalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)


def test_integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)


def test_integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::setcurrentvalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)


def test_integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)


def test_integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_decisionnode::fire::decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(DecisionNode::fire::decisionNodeExitEventOccurrence)


def test_decisionnode::fire::decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)


def test_decisionnode::fire::decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_decisionnode::fire::decisionnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(DecisionNode::fire::decisionNodeEntryEventOccurrence)


def test_decisionnode::fire::decisionnodeentryeventoccurrence_constructor_exists():
    assert callable(DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)


def test_decisionnode::fire::decisionnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_mergenode::hasoffers::mergenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(MergeNode::hasOffers::mergeNodeExitEventOccurrence)


def test_mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_exists():
    assert callable(MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)


def test_mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_mergenode::hasoffers::mergenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(MergeNode::hasOffers::mergeNodeEntryEventOccurrence)


def test_mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_exists():
    assert callable(MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)


def test_mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forknode::fire::forknodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkNode::fire::forkNodeExitEventOccurrence)


def test_forknode::fire::forknodeexiteventoccurrence_constructor_exists():
    assert callable(ForkNode::fire::forkNodeExitEventOccurrence.__init__)


def test_forknode::fire::forknodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ForkNode::fire::forkNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_forknode::fire::forknodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ForkNode::fire::forkNodeEntryEventOccurrence)


def test_forknode::fire::forknodeentryeventoccurrence_constructor_exists():
    assert callable(ForkNode::fire::forkNodeEntryEventOccurrence.__init__)


def test_forknode::fire::forknodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ForkNode::fire::forkNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityfinalnode::fire::activityfinalnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)


def test_activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)


def test_activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityfinalnode::fire::activityfinalnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)


def test_activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)


def test_activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::isready::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::isReady::actionEntryEventOccurrence)


def test_action::isready::actionentryeventoccurrence_constructor_exists():
    assert callable(Action::isReady::actionEntryEventOccurrence.__init__)


def test_action::isready::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action::isReady::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::sendoffers::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::sendOffers::actionExitEventOccurrence)


def test_action::sendoffers::actionexiteventoccurrence_constructor_exists():
    assert callable(Action::sendOffers::actionExitEventOccurrence.__init__)


def test_action::sendoffers::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action::sendOffers::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::sendoffers::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::sendOffers::actionEntryEventOccurrence)


def test_action::sendoffers::actionentryeventoccurrence_constructor_exists():
    assert callable(Action::sendOffers::actionEntryEventOccurrence.__init__)


def test_action::sendoffers::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action::sendOffers::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode::fire::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode::fire::controlNodeExitEventOccurrence)


def test_controlnode::fire::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(ControlNode::fire::controlNodeExitEventOccurrence.__init__)


def test_controlnode::fire::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode::fire::controlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode::isready::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::isReady::InitialNodeExitEventOccurrence)


def test_initialnode::isready::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)


def test_initialnode::isready::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode::isready::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::isReady::InitialNodeEntryEventOccurrence)


def test_initialnode::isready::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)


def test_initialnode::isready::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_opaqueaction::doaction::opaqueactionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(OpaqueAction::doAction::opaqueActionExitEventOccurrence)


def test_opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_exists():
    assert callable(OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)


def test_opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_args():
    sig = inspect.signature(OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_opaqueaction::doaction::opaqueactionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(OpaqueAction::doAction::opaqueActionEntryEventOccurrence)


def test_opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_exists():
    assert callable(OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)


def test_opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_args():
    sig = inspect.signature(OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::fire::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::fire::actionExitEventOccurrence)


def test_action::fire::actionexiteventoccurrence_constructor_exists():
    assert callable(Action::fire::actionExitEventOccurrence.__init__)


def test_action::fire::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action::fire::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::fire::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::fire::actionEntryEventOccurrence)


def test_action::fire::actionentryeventoccurrence_constructor_exists():
    assert callable(Action::fire::actionEntryEventOccurrence.__init__)


def test_action::fire::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action::fire::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isReadyExitEventOccurrence)


def test_activitynode::isreadyexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::isReadyExitEventOccurrence.__init__)


def test_activitynode::isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::isready::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::isReady::actionExitEventOccurrence)


def test_action::isready::actionexiteventoccurrence_constructor_exists():
    assert callable(Action::isReady::actionExitEventOccurrence.__init__)


def test_action::isready::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action::isReady::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isReadyEntryEventOccurrence)


def test_activitynode::isreadyentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::isReadyEntryEventOccurrence.__init__)


def test_activitynode::isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isReadyEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode::fire::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode::fire::controlNodeEntryEventOccurrence)


def test_controlnode::fire::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(ControlNode::fire::controlNodeEntryEventOccurrence.__init__)


def test_controlnode::fire::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode::fire::controlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode::isready::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode::isReady::ControlNodeExitEventOccurrence)


def test_controlnode::isready::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)


def test_controlnode::isready::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_controlnode::isready::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ControlNode::isReady::ControlNodeEntryEventOccurrence)


def test_controlnode::isready::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)


def test_controlnode::isready::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::hasofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::hasOfferExitEventOccurrence)


def test_activityedge::hasofferexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge::hasOfferExitEventOccurrence.__init__)


def test_activityedge::hasofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::hasOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::hasofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::hasOfferEntryEventOccurrence)


def test_activityedge::hasofferentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge::hasOfferEntryEventOccurrence.__init__)


def test_activityedge::hasofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::hasOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::takeofferedtokens::activityedgeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)


def test_activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)


def test_activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::takeofferedtokens::activityedgeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)


def test_activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)


def test_activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::sendofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::sendOfferExitEventOccurrence)


def test_activityedge::sendofferexiteventoccurrence_constructor_exists():
    assert callable(ActivityEdge::sendOfferExitEventOccurrence.__init__)


def test_activityedge::sendofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::sendOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::sendofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::sendOfferEntryEventOccurrence)


def test_activityedge::sendofferentryeventoccurrence_constructor_exists():
    assert callable(ActivityEdge::sendOfferEntryEventOccurrence.__init__)


def test_activityedge::sendofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityEdge::sendOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::isrunningexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isRunningExitEventOccurrence)


def test_activitynode::isrunningexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::isRunningExitEventOccurrence.__init__)


def test_activitynode::isrunningexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isRunningExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::isrunningentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isRunningEntryEventOccurrence)


def test_activitynode::isrunningentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::isRunningEntryEventOccurrence.__init__)


def test_activitynode::isrunningentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isRunningEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::run::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::run::activityNodeExitEventOccurrence)


def test_activitynode::run::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::run::activityNodeExitEventOccurrence.__init__)


def test_activitynode::run::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::run::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::hasOffersExitEventOccurrence)


def test_activitynode::hasoffersexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::hasOffersExitEventOccurrence.__init__)


def test_activitynode::hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::hasOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::run::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::run::activityNodeEntryEventOccurrence)


def test_activitynode::run::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::run::activityNodeEntryEventOccurrence.__init__)


def test_activitynode::run::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::run::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::hasoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::hasOffersEntryEventOccurrence)


def test_activitynode::hasoffersentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::hasOffersEntryEventOccurrence.__init__)


def test_activitynode::hasoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::hasOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::removeTokenExitEventOccurrence)


def test_activitynode::removetokenexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::removeTokenExitEventOccurrence.__init__)


def test_activitynode::removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::removeTokenEntryEventOccurrence)


def test_activitynode::removetokenentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::removeTokenEntryEventOccurrence.__init__)


def test_activitynode::removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::addtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::addTokensExitEventOccurrence)


def test_activitynode::addtokensexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::addTokensExitEventOccurrence.__init__)


def test_activitynode::addtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::addTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::addtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::addTokensEntryEventOccurrence)


def test_activitynode::addtokensentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::addTokensEntryEventOccurrence.__init__)


def test_activitynode::addtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::addTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::takeofferedtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::takeOfferedTokensExitEventOccurrence)


def test_activitynode::takeofferedtokensexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)


def test_activitynode::takeofferedtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::takeofferedtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::takeOfferedTokensEntryEventOccurrence)


def test_activitynode::takeofferedtokensentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)


def test_activitynode::takeofferedtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::sendoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::sendOffersExitEventOccurrence)


def test_activitynode::sendoffersexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::sendOffersExitEventOccurrence.__init__)


def test_activitynode::sendoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::sendOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::sendoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::sendOffersEntryEventOccurrence)


def test_activitynode::sendoffersentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::sendOffersEntryEventOccurrence.__init__)


def test_activitynode::sendoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::sendOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::terminate::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::terminate::activityNodeExitEventOccurrence)


def test_activitynode::terminate::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)


def test_activitynode::terminate::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::terminate::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::terminate::activityNodeEntryEventOccurrence)


def test_activitynode::terminate::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)


def test_activitynode::terminate::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::runnodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::runNodesExitEventOccurrence)


def test_activity::runnodesexiteventoccurrence_constructor_exists():
    assert callable(Activity::runNodesExitEventOccurrence.__init__)


def test_activity::runnodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::runNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::runnodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::runNodesEntryEventOccurrence)


def test_activity::runnodesentryeventoccurrence_constructor_exists():
    assert callable(Activity::runNodesEntryEventOccurrence.__init__)


def test_activity::runnodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::runNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::runExitEventOccurrence)


def test_activity::runexiteventoccurrence_constructor_exists():
    assert callable(Activity::runExitEventOccurrence.__init__)


def test_activity::runexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::runEntryEventOccurrence)


def test_activity::runentryeventoccurrence_constructor_exists():
    assert callable(Activity::runEntryEventOccurrence.__init__)


def test_activity::runentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::initializeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::initializeExitEventOccurrence)


def test_activity::initializeexiteventoccurrence_constructor_exists():
    assert callable(Activity::initializeExitEventOccurrence.__init__)


def test_activity::initializeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::initializeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::initializeEntryEventOccurrence)


def test_activity::initializeentryeventoccurrence_constructor_exists():
    assert callable(Activity::initializeEntryEventOccurrence.__init__)


def test_activity::initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::initializeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireNodeExitEventOccurrence)


def test_activity::firenodeexiteventoccurrence_constructor_exists():
    assert callable(Activity::fireNodeExitEventOccurrence.__init__)


def test_activity::firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::firenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireNodeEntryEventOccurrence)


def test_activity::firenodeentryeventoccurrence_constructor_exists():
    assert callable(Activity::fireNodeEntryEventOccurrence.__init__)


def test_activity::firenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::getinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::getInitialNodeExitEventOccurrence)


def test_activity::getinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity::getInitialNodeExitEventOccurrence.__init__)


def test_activity::getinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::getInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::getinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::getInitialNodeEntryEventOccurrence)


def test_activity::getinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity::getInitialNodeEntryEventOccurrence.__init__)


def test_activity::getinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::getInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::terminateexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::terminateExitEventOccurrence)


def test_activity::terminateexiteventoccurrence_constructor_exists():
    assert callable(Activity::terminateExitEventOccurrence.__init__)


def test_activity::terminateexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::terminateExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::terminateentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::terminateEntryEventOccurrence)


def test_activity::terminateentryeventoccurrence_constructor_exists():
    assert callable(Activity::terminateEntryEventOccurrence.__init__)


def test_activity::terminateentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::terminateEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::selectnextnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::selectNextNodeExitEventOccurrence)


def test_activity::selectnextnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity::selectNextNodeExitEventOccurrence.__init__)


def test_activity::selectnextnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::selectNextNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::selectnextnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::selectNextNodeEntryEventOccurrence)


def test_activity::selectnextnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity::selectNextNodeEntryEventOccurrence.__init__)


def test_activity::selectnextnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::selectNextNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::ActivityFinalNode)


def test_activitydiagram::trace::activityfinalnode_constructor_exists():
    assert callable(activitydiagram::trace::ActivityFinalNode.__init__)


def test_activitydiagram::trace::activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedActivityFinalNode)


def test_trace::activitydiagram::tracedactivityfinalnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedActivityFinalNode.__init__)


def test_trace::activitydiagram::tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(TracedExecutableNode)


def test_tracedexecutablenode_constructor_exists():
    assert callable(TracedExecutableNode.__init__)


def test_tracedexecutablenode_constructor_args():
    sig = inspect.signature(TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::expression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::Expression)


def test_activitydiagram::trace::expression_constructor_exists():
    assert callable(activitydiagram::trace::Expression.__init__)


def test_activitydiagram::trace::expression_constructor_args():
    sig = inspect.signature(activitydiagram::trace::Expression.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedaction_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedAction)


def test_trace::activitydiagram::tracedaction_constructor_exists():
    assert callable(trace::activitydiagram::TracedAction.__init__)


def test_trace::activitydiagram::tracedaction_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedOpaqueAction)


def test_trace::activitydiagram::tracedopaqueaction_constructor_exists():
    assert callable(trace::activitydiagram::TracedOpaqueAction.__init__)


def test_trace::activitydiagram::tracedopaqueaction_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::stringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::StringVariable)


def test_activitydiagram::trace::stringvariable_constructor_exists():
    assert callable(activitydiagram::trace::StringVariable.__init__)


def test_activitydiagram::trace::stringvariable_constructor_args():
    sig = inspect.signature(activitydiagram::trace::StringVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::Activity)


def test_activitydiagram::trace::activity_constructor_exists():
    assert callable(activitydiagram::trace::Activity.__init__)


def test_activitydiagram::trace::activity_constructor_args():
    sig = inspect.signature(activitydiagram::trace::Activity.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedActivityNode)


def test_trace::activitydiagram::tracedactivitynode_constructor_exists():
    assert callable(trace::activitydiagram::TracedActivityNode.__init__)


def test_trace::activitydiagram::tracedactivitynode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedActivity)


def test_trace::activitydiagram::tracedactivity_constructor_exists():
    assert callable(trace::activitydiagram::TracedActivity.__init__)


def test_trace::activitydiagram::tracedactivity_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedActivityEdge)


def test_trace::activitydiagram::tracedactivityedge_constructor_exists():
    assert callable(trace::activitydiagram::TracedActivityEdge.__init__)


def test_trace::activitydiagram::tracedactivityedge_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::integervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::IntegerVariable)


def test_activitydiagram::trace::integervariable_constructor_exists():
    assert callable(activitydiagram::trace::IntegerVariable.__init__)


def test_activitydiagram::trace::integervariable_constructor_args():
    sig = inspect.signature(activitydiagram::trace::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNode)


def test_tracedactivitynode_constructor_exists():
    assert callable(TracedActivityNode.__init__)


def test_tracedactivitynode_constructor_args():
    sig = inspect.signature(TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedControlNode)


def test_trace::activitydiagram::tracedcontrolnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedControlNode.__init__)


def test_trace::activitydiagram::tracedcontrolnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedExecutableNode)


def test_trace::activitydiagram::tracedexecutablenode_constructor_exists():
    assert callable(trace::activitydiagram::TracedExecutableNode.__init__)


def test_trace::activitydiagram::tracedexecutablenode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::BooleanVariable)


def test_activitydiagram::trace::booleanvariable_constructor_exists():
    assert callable(activitydiagram::trace::BooleanVariable.__init__)


def test_activitydiagram::trace::booleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::trace::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(TracedVariable)


def test_tracedvariable_constructor_exists():
    assert callable(TracedVariable.__init__)


def test_tracedvariable_constructor_args():
    sig = inspect.signature(TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedIntegerVariable)


def test_trace::activitydiagram::tracedintegervariable_constructor_exists():
    assert callable(trace::activitydiagram::TracedIntegerVariable.__init__)


def test_trace::activitydiagram::tracedintegervariable_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedStringVariable)


def test_trace::activitydiagram::tracedstringvariable_constructor_exists():
    assert callable(trace::activitydiagram::TracedStringVariable.__init__)


def test_trace::activitydiagram::tracedstringvariable_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedBooleanVariable)


def test_trace::activitydiagram::tracedbooleanvariable_constructor_exists():
    assert callable(trace::activitydiagram::TracedBooleanVariable.__init__)


def test_trace::activitydiagram::tracedbooleanvariable_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::MergeNode)


def test_activitydiagram::trace::mergenode_constructor_exists():
    assert callable(activitydiagram::trace::MergeNode.__init__)


def test_activitydiagram::trace::mergenode_constructor_args():
    sig = inspect.signature(activitydiagram::trace::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedDecisionNode)


def test_trace::activitydiagram::traceddecisionnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedDecisionNode.__init__)


def test_trace::activitydiagram::traceddecisionnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedInitialNode)


def test_trace::activitydiagram::tracedinitialnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedInitialNode.__init__)


def test_trace::activitydiagram::tracedinitialnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedforknode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedForkNode)


def test_trace::activitydiagram::tracedforknode_constructor_exists():
    assert callable(trace::activitydiagram::TracedForkNode.__init__)


def test_trace::activitydiagram::tracedforknode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedFinalNode)


def test_trace::activitydiagram::tracedfinalnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedFinalNode.__init__)


def test_trace::activitydiagram::tracedfinalnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedJoinNode)


def test_trace::activitydiagram::tracedjoinnode_constructor_exists():
    assert callable(trace::activitydiagram::TracedJoinNode.__init__)


def test_trace::activitydiagram::tracedjoinnode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedMergeNode)


def test_trace::activitydiagram::tracedmergenode_constructor_exists():
    assert callable(trace::activitydiagram::TracedMergeNode.__init__)


def test_trace::activitydiagram::tracedmergenode_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::controlflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::ControlFlow)


def test_activitydiagram::trace::controlflow_constructor_exists():
    assert callable(activitydiagram::trace::ControlFlow.__init__)


def test_activitydiagram::trace::controlflow_constructor_args():
    sig = inspect.signature(activitydiagram::trace::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(TracedActivityEdge)


def test_tracedactivityedge_constructor_exists():
    assert callable(TracedActivityEdge.__init__)


def test_tracedactivityedge_constructor_args():
    sig = inspect.signature(TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedControlFlow)


def test_trace::activitydiagram::tracedcontrolflow_constructor_exists():
    assert callable(trace::activitydiagram::TracedControlFlow.__init__)


def test_trace::activitydiagram::tracedcontrolflow_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedJoinNode)


def test_activitydiagram::tracedjoinnode_constructor_exists():
    assert callable(activitydiagram::TracedJoinNode.__init__)


def test_activitydiagram::tracedjoinnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::trace::value_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::trace::Value)


def test_activitydiagram::trace::value_constructor_exists():
    assert callable(activitydiagram::trace::Value.__init__)


def test_activitydiagram::trace::value_constructor_args():
    sig = inspect.signature(activitydiagram::trace::Value.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedVariable)


def test_trace::activitydiagram::tracedvariable_constructor_exists():
    assert callable(trace::activitydiagram::TracedVariable.__init__)


def test_trace::activitydiagram::tracedvariable_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_trace::activitydiagram::tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(trace::activitydiagram::TracedNamedElement)


def test_trace::activitydiagram::tracednamedelement_constructor_exists():
    assert callable(trace::activitydiagram::TracedNamedElement.__init__)


def test_trace::activitydiagram::tracednamedelement_constructor_args():
    sig = inspect.signature(trace::activitydiagram::TracedNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_trace::activitydiagram::tracednamedelement_has_name():
    assert hasattr(trace::activitydiagram::TracedNamedElement, "name")
    descriptor = None
    for klass in trace::activitydiagram::TracedNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagramconfiguration::tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedControlToken)


def test_activitydiagramconfiguration::tracedcontroltoken_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedControlToken.__init__)


def test_activitydiagramconfiguration::tracedcontroltoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedControlFlow)


def test_activitydiagram::tracedcontrolflow_constructor_exists():
    assert callable(activitydiagram::TracedControlFlow.__init__)


def test_activitydiagram::tracedcontrolflow_constructor_args():
    sig = inspect.signature(activitydiagram::TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_trace::traced::tracedobjects_is_not_abstract():
    assert not inspect.isabstract(trace::Traced::TracedObjects)


def test_trace::traced::tracedobjects_constructor_exists():
    assert callable(trace::Traced::TracedObjects.__init__)


def test_trace::traced::tracedobjects_constructor_args():
    sig = inspect.signature(trace::Traced::TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedtrace_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedTrace)


def test_activitydiagramconfiguration::tracedtrace_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedTrace.__init__)


def test_activitydiagramconfiguration::tracedtrace_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::activity::trace::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Activity::trace::State)


def test_trace::states::activity::trace::state_constructor_exists():
    assert callable(trace::States::Activity::trace::State.__init__)


def test_trace::states::activity::trace::state_constructor_args():
    sig = inspect.signature(trace::States::Activity::trace::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::activitynode::heldtokens::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ActivityNode::heldTokens::State)


def test_trace::states::activitynode::heldtokens::state_constructor_exists():
    assert callable(trace::States::ActivityNode::heldTokens::State.__init__)


def test_trace::states::activitynode::heldtokens::state_constructor_args():
    sig = inspect.signature(trace::States::ActivityNode::heldTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::activitynode::running::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ActivityNode::running::State)


def test_trace::states::activitynode::running::state_constructor_exists():
    assert callable(trace::States::ActivityNode::running::State.__init__)


def test_trace::states::activitynode::running::state_constructor_args():
    sig = inspect.signature(trace::States::ActivityNode::running::State.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_trace::states::activitynode::running::state_has_running():
    assert hasattr(trace::States::ActivityNode::running::State, "running")
    descriptor = None
    for klass in trace::States::ActivityNode::running::State.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_trace::states::offer::offeredtokens::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Offer::offeredTokens::State)


def test_trace::states::offer::offeredtokens::state_constructor_exists():
    assert callable(trace::States::Offer::offeredTokens::State.__init__)


def test_trace::states::offer::offeredtokens::state_constructor_args():
    sig = inspect.signature(trace::States::Offer::offeredTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::variable::currentvalue::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Variable::currentValue::State)


def test_trace::states::variable::currentvalue::state_constructor_exists():
    assert callable(trace::States::Variable::currentValue::State.__init__)


def test_trace::states::variable::currentvalue::state_constructor_args():
    sig = inspect.signature(trace::States::Variable::currentValue::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::trace::executednodes::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Trace::executedNodes::State)


def test_trace::states::trace::executednodes::state_constructor_exists():
    assert callable(trace::States::Trace::executedNodes::State.__init__)


def test_trace::states::trace::executednodes::state_constructor_args():
    sig = inspect.signature(trace::States::Trace::executedNodes::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::forkedtoken::basetokeniswithdrawn::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ForkedToken::baseTokenIsWithdrawn::State)


def test_trace::states::forkedtoken::basetokeniswithdrawn::state_constructor_exists():
    assert callable(trace::States::ForkedToken::baseTokenIsWithdrawn::State.__init__)


def test_trace::states::forkedtoken::basetokeniswithdrawn::state_constructor_args():
    sig = inspect.signature(trace::States::ForkedToken::baseTokenIsWithdrawn::State.__init__)
    params = list(sig.parameters.keys())
    assert "baseTokenIsWithdrawn" in params, "Missing parameter 'baseTokenIsWithdrawn'"

def test_trace::states::forkedtoken::basetokeniswithdrawn::state_has_baseTokenIsWithdrawn():
    assert hasattr(trace::States::ForkedToken::baseTokenIsWithdrawn::State, "baseTokenIsWithdrawn")
    descriptor = None
    for klass in trace::States::ForkedToken::baseTokenIsWithdrawn::State.__mro__:
        if "baseTokenIsWithdrawn" in klass.__dict__:
            descriptor = klass.__dict__["baseTokenIsWithdrawn"]
            break
    assert isinstance(descriptor, property)



def test_trace::states::forkedtoken::basetoken::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ForkedToken::baseToken::State)


def test_trace::states::forkedtoken::basetoken::state_constructor_exists():
    assert callable(trace::States::ForkedToken::baseToken::State.__init__)


def test_trace::states::forkedtoken::basetoken::state_constructor_args():
    sig = inspect.signature(trace::States::ForkedToken::baseToken::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::forkedtoken::remainingofferscount::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ForkedToken::remainingOffersCount::State)


def test_trace::states::forkedtoken::remainingofferscount::state_constructor_exists():
    assert callable(trace::States::ForkedToken::remainingOffersCount::State.__init__)


def test_trace::states::forkedtoken::remainingofferscount::state_constructor_args():
    sig = inspect.signature(trace::States::ForkedToken::remainingOffersCount::State.__init__)
    params = list(sig.parameters.keys())
    assert "remainingOffersCount" in params, "Missing parameter 'remainingOffersCount'"

def test_trace::states::forkedtoken::remainingofferscount::state_has_remainingOffersCount():
    assert hasattr(trace::States::ForkedToken::remainingOffersCount::State, "remainingOffersCount")
    descriptor = None
    for klass in trace::States::ForkedToken::remainingOffersCount::State.__mro__:
        if "remainingOffersCount" in klass.__dict__:
            descriptor = klass.__dict__["remainingOffersCount"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagramconfiguration::tracedinput_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedInput)


def test_activitydiagramconfiguration::tracedinput_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedInput.__init__)


def test_activitydiagramconfiguration::tracedinput_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::input::inputvalues::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Input::inputValues::State)


def test_trace::states::input::inputvalues::state_constructor_exists():
    assert callable(trace::States::Input::inputValues::State.__init__)


def test_trace::states::input::inputvalues::state_constructor_args():
    sig = inspect.signature(trace::States::Input::inputValues::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::token::holder::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::Token::holder::State)


def test_trace::states::token::holder::state_constructor_exists():
    assert callable(trace::States::Token::holder::State.__init__)


def test_trace::states::token::holder::state_constructor_args():
    sig = inspect.signature(trace::States::Token::holder::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::activityedge::offers::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::ActivityEdge::offers::State)


def test_trace::states::activityedge::offers::state_constructor_exists():
    assert callable(trace::States::ActivityEdge::offers::State.__init__)


def test_trace::states::activityedge::offers::state_constructor_args():
    sig = inspect.signature(trace::States::ActivityEdge::offers::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedInputValue)


def test_activitydiagramconfiguration::tracedinputvalue_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedInputValue.__init__)


def test_activitydiagramconfiguration::tracedinputvalue_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_states::trace::value_is_not_abstract():
    assert not inspect.isabstract(States::trace::Value)


def test_states::trace::value_constructor_exists():
    assert callable(States::trace::Value.__init__)


def test_states::trace::value_constructor_args():
    sig = inspect.signature(States::trace::Value.__init__)
    params = list(sig.parameters.keys())



def test_trace::states::inputvalue::value::state_is_not_abstract():
    assert not inspect.isabstract(trace::States::InputValue::value::State)


def test_trace::states::inputvalue::value::state_constructor_exists():
    assert callable(trace::States::InputValue::value::State.__init__)


def test_trace::states::inputvalue::value::state_constructor_args():
    sig = inspect.signature(trace::States::InputValue::value::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedoffer_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedOffer)


def test_activitydiagramconfiguration::tracedoffer_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedOffer.__init__)


def test_activitydiagramconfiguration::tracedoffer_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedOffer.__init__)
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



def test_trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(trace::GlobalState)


def test_trace::globalstate_constructor_exists():
    assert callable(trace::GlobalState.__init__)


def test_trace::globalstate_constructor_args():
    sig = inspect.signature(trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_activity::getenablednodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::getEnabledNodesExitEventOccurrence)


def test_activity::getenablednodesexiteventoccurrence_constructor_exists():
    assert callable(Activity::getEnabledNodesExitEventOccurrence.__init__)


def test_activity::getenablednodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::getEnabledNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::getenablednodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::getEnabledNodesEntryEventOccurrence)


def test_activity::getenablednodesentryeventoccurrence_constructor_exists():
    assert callable(Activity::getEnabledNodesEntryEventOccurrence.__init__)


def test_activity::getenablednodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::getEnabledNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::fireinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireInitialNodeExitEventOccurrence)


def test_activity::fireinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(Activity::fireInitialNodeExitEventOccurrence.__init__)


def test_activity::fireinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::heldtokens::state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::heldTokens::State)


def test_activitynode::heldtokens::state_constructor_exists():
    assert callable(ActivityNode::heldTokens::State.__init__)


def test_activitynode::heldtokens::state_constructor_args():
    sig = inspect.signature(ActivityNode::heldTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_activity::fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireInitialNodeEntryEventOccurrence)


def test_activity::fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity::fireInitialNodeEntryEventOccurrence.__init__)


def test_activity::fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::running::state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::running::State)


def test_activitynode::running::state_constructor_exists():
    assert callable(ActivityNode::running::State.__init__)


def test_activitynode::running::state_constructor_args():
    sig = inspect.signature(ActivityNode::running::State.__init__)
    params = list(sig.parameters.keys())



def test_activity::mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::mainExitEventOccurrence)


def test_activity::mainexiteventoccurrence_constructor_exists():
    assert callable(Activity::mainExitEventOccurrence.__init__)


def test_activity::mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::mainEntryEventOccurrence)


def test_activity::mainentryeventoccurrence_constructor_exists():
    assert callable(Activity::mainEntryEventOccurrence.__init__)


def test_activity::mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::events_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Events)


def test_trace::events::events_constructor_exists():
    assert callable(trace::Events::Events.__init__)


def test_trace::events::events_constructor_args():
    sig = inspect.signature(trace::Events::Events.__init__)
    params = list(sig.parameters.keys())



def test_events::trace::globalstate_is_not_abstract():
    assert not inspect.isabstract(Events::trace::GlobalState)


def test_events::trace::globalstate_constructor_exists():
    assert callable(Events::trace::GlobalState.__init__)


def test_events::trace::globalstate_constructor_args():
    sig = inspect.signature(Events::trace::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::EventOccurrence)


def test_trace::events::eventoccurrence_constructor_exists():
    assert callable(trace::Events::EventOccurrence.__init__)


def test_trace::events::eventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(trace::IntegerCalculationExpression)


def test_trace::integercalculationexpression_constructor_exists():
    assert callable(trace::IntegerCalculationExpression.__init__)


def test_trace::integercalculationexpression_constructor_args():
    sig = inspect.signature(trace::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(trace::BooleanUnaryExpression)


def test_trace::booleanunaryexpression_constructor_exists():
    assert callable(trace::BooleanUnaryExpression.__init__)


def test_trace::booleanunaryexpression_constructor_args():
    sig = inspect.signature(trace::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(trace::IntegerComparisonExpression)


def test_trace::integercomparisonexpression_constructor_exists():
    assert callable(trace::IntegerComparisonExpression.__init__)


def test_trace::integercomparisonexpression_constructor_args():
    sig = inspect.signature(trace::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(trace::BooleanValue)


def test_trace::booleanvalue_constructor_exists():
    assert callable(trace::BooleanValue.__init__)


def test_trace::booleanvalue_constructor_args():
    sig = inspect.signature(trace::BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::integervalue_is_not_abstract():
    assert not inspect.isabstract(trace::IntegerValue)


def test_trace::integervalue_constructor_exists():
    assert callable(trace::IntegerValue.__init__)


def test_trace::integervalue_constructor_args():
    sig = inspect.signature(trace::IntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::stringvalue_is_not_abstract():
    assert not inspect.isabstract(trace::StringValue)


def test_trace::stringvalue_constructor_exists():
    assert callable(trace::StringValue.__init__)


def test_trace::stringvalue_constructor_args():
    sig = inspect.signature(trace::StringValue.__init__)
    params = list(sig.parameters.keys())



def test_trace::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(trace::BooleanBinaryExpression)


def test_trace::booleanbinaryexpression_constructor_exists():
    assert callable(trace::BooleanBinaryExpression.__init__)


def test_trace::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(trace::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_trace::executednodes::state_is_not_abstract():
    assert not inspect.isabstract(Trace::executedNodes::State)


def test_trace::executednodes::state_constructor_exists():
    assert callable(Trace::executedNodes::State.__init__)


def test_trace::executednodes::state_constructor_args():
    sig = inspect.signature(Trace::executedNodes::State.__init__)
    params = list(sig.parameters.keys())



def test_activity::trace::state_is_not_abstract():
    assert not inspect.isabstract(Activity::trace::State)


def test_activity::trace::state_constructor_exists():
    assert callable(Activity::trace::State.__init__)


def test_activity::trace::state_constructor_args():
    sig = inspect.signature(Activity::trace::State.__init__)
    params = list(sig.parameters.keys())



def test_trace::trace_is_not_abstract():
    assert not inspect.isabstract(trace::Trace)


def test_trace::trace_constructor_exists():
    assert callable(trace::Trace.__init__)


def test_trace::trace_constructor_args():
    sig = inspect.signature(trace::Trace.__init__)
    params = list(sig.parameters.keys())



def test_offer::offeredtokens::state_is_not_abstract():
    assert not inspect.isabstract(Offer::offeredTokens::State)


def test_offer::offeredtokens::state_constructor_exists():
    assert callable(Offer::offeredTokens::State.__init__)


def test_offer::offeredtokens::state_constructor_args():
    sig = inspect.signature(Offer::offeredTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_variable::currentvalue::state_is_not_abstract():
    assert not inspect.isabstract(Variable::currentValue::State)


def test_variable::currentvalue::state_constructor_exists():
    assert callable(Variable::currentValue::State.__init__)


def test_variable::currentvalue::state_constructor_args():
    sig = inspect.signature(Variable::currentValue::State.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::offers::state_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::offers::State)


def test_activityedge::offers::state_constructor_exists():
    assert callable(ActivityEdge::offers::State.__init__)


def test_activityedge::offers::state_constructor_args():
    sig = inspect.signature(ActivityEdge::offers::State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::basetokeniswithdrawn::state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::baseTokenIsWithdrawn::State)


def test_forkedtoken::basetokeniswithdrawn::state_constructor_exists():
    assert callable(ForkedToken::baseTokenIsWithdrawn::State.__init__)


def test_forkedtoken::basetokeniswithdrawn::state_constructor_args():
    sig = inspect.signature(ForkedToken::baseTokenIsWithdrawn::State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::basetoken::state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::baseToken::State)


def test_forkedtoken::basetoken::state_constructor_exists():
    assert callable(ForkedToken::baseToken::State.__init__)


def test_forkedtoken::basetoken::state_constructor_args():
    sig = inspect.signature(ForkedToken::baseToken::State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::remainingofferscount::state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::remainingOffersCount::State)


def test_forkedtoken::remainingofferscount::state_constructor_exists():
    assert callable(ForkedToken::remainingOffersCount::State.__init__)


def test_forkedtoken::remainingofferscount::state_constructor_args():
    sig = inspect.signature(ForkedToken::remainingOffersCount::State.__init__)
    params = list(sig.parameters.keys())



def test_input::inputvalues::state_is_not_abstract():
    assert not inspect.isabstract(Input::inputValues::State)


def test_input::inputvalues::state_constructor_exists():
    assert callable(Input::inputValues::State.__init__)


def test_input::inputvalues::state_constructor_args():
    sig = inspect.signature(Input::inputValues::State.__init__)
    params = list(sig.parameters.keys())



def test_token::holder::state_is_not_abstract():
    assert not inspect.isabstract(Token::holder::State)


def test_token::holder::state_constructor_exists():
    assert callable(Token::holder::State.__init__)


def test_token::holder::state_constructor_args():
    sig = inspect.signature(Token::holder::State.__init__)
    params = list(sig.parameters.keys())



def test_inputvalue::variable::state_is_not_abstract():
    assert not inspect.isabstract(InputValue::variable::State)


def test_inputvalue::variable::state_constructor_exists():
    assert callable(InputValue::variable::State.__init__)


def test_inputvalue::variable::state_constructor_args():
    sig = inspect.signature(InputValue::variable::State.__init__)
    params = list(sig.parameters.keys())



def test_inputvalue::value::state_is_not_abstract():
    assert not inspect.isabstract(InputValue::value::State)


def test_inputvalue::value::state_constructor_exists():
    assert callable(InputValue::value::State.__init__)


def test_inputvalue::value::state_constructor_args():
    sig = inspect.signature(InputValue::value::State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::isready::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::isReady::actionExitEventOccurrence)


def test_trace::events::action::isready::actionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::isReady::actionExitEventOccurrence.__init__)


def test_trace::events::action::isready::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::isReady::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::fire::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::fire::actionExitEventOccurrence)


def test_trace::events::action::fire::actionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::fire::actionExitEventOccurrence.__init__)


def test_trace::events::action::fire::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::fire::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::takeofferedtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence)


def test_trace::events::activitynode::takeofferedtokensexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)


def test_trace::events::activitynode::takeofferedtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::fireInitialNodeEntryEventOccurrence)


def test_trace::events::activity::fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::fireInitialNodeEntryEventOccurrence.__init__)


def test_trace::events::activity::fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::terminateexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::terminateExitEventOccurrence)


def test_trace::events::activity::terminateexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::terminateExitEventOccurrence.__init__)


def test_trace::events::activity::terminateexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::terminateExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::terminate::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence)


def test_trace::events::activitynode::terminate::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)


def test_trace::events::activitynode::terminate::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::offer::hastokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Offer::hasTokensEntryEventOccurrence)


def test_trace::events::offer::hastokensentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Offer::hasTokensEntryEventOccurrence.__init__)


def test_trace::events::offer::hastokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Offer::hasTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::sendoffers::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::sendOffers::actionEntryEventOccurrence)


def test_trace::events::action::sendoffers::actionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::sendOffers::actionEntryEventOccurrence.__init__)


def test_trace::events::action::sendoffers::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::sendOffers::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::fireNodeExitEventOccurrence)


def test_trace::events::activity::firenodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::fireNodeExitEventOccurrence.__init__)


def test_trace::events::activity::firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::initialnode::fire::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence)


def test_trace::events::initialnode::fire::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence.__init__)


def test_trace::events::initialnode::fire::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)


def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::mergenode::hasoffers::mergenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence)


def test_trace::events::mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)


def test_trace::events::mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)


def test_trace::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)


def test_trace::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)


def test_trace::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::runnodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::runNodesExitEventOccurrence)


def test_trace::events::activity::runnodesexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::runNodesExitEventOccurrence.__init__)


def test_trace::events::activity::runnodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::runNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::getinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::getInitialNodeEntryEventOccurrence)


def test_trace::events::activity::getinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::getInitialNodeEntryEventOccurrence.__init__)


def test_trace::events::activity::getinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::getInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)


def test_trace::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)


def test_trace::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::terminate::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence)


def test_trace::events::activitynode::terminate::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)


def test_trace::events::activitynode::terminate::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanunaryexpression::evaluatenotexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence)


def test_trace::events::booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)


def test_trace::events::booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::decisionnode::fire::decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence)


def test_trace::events::decisionnode::fire::decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)


def test_trace::events::decisionnode::fire::decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::firenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::fireNodeEntryEventOccurrence)


def test_trace::events::activity::firenodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::fireNodeEntryEventOccurrence.__init__)


def test_trace::events::activity::firenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::fireNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::fireinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::fireInitialNodeExitEventOccurrence)


def test_trace::events::activity::fireinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::fireInitialNodeExitEventOccurrence.__init__)


def test_trace::events::activity::fireinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::fireInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::withdrawexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::withdrawExitEventOccurrence)


def test_trace::events::token::withdrawexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::withdrawExitEventOccurrence.__init__)


def test_trace::events::token::withdrawexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::withdrawExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanunaryexpression::evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)


def test_trace::events::booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)


def test_trace::events::booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::sendofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::sendOfferEntryEventOccurrence)


def test_trace::events::activityedge::sendofferentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::sendOfferEntryEventOccurrence.__init__)


def test_trace::events::activityedge::sendofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::sendOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::removeTokenExitEventOccurrence)


def test_trace::events::activitynode::removetokenexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::removeTokenExitEventOccurrence.__init__)


def test_trace::events::activitynode::removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)


def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)


def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::mainExitEventOccurrence)


def test_trace::events::activity::mainexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::mainExitEventOccurrence.__init__)


def test_trace::events::activity::mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence)


def test_trace::events::integercalculationexpression::evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)


def test_trace::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)


def test_trace::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)


def test_trace::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::runnodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::runNodesEntryEventOccurrence)


def test_trace::events::activity::runnodesentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::runNodesEntryEventOccurrence.__init__)


def test_trace::events::activity::runnodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::runNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)


def test_trace::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)


def test_trace::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::getinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::getInitialNodeExitEventOccurrence)


def test_trace::events::activity::getinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::getInitialNodeExitEventOccurrence.__init__)


def test_trace::events::activity::getinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::getInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::getenablednodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::getEnabledNodesExitEventOccurrence)


def test_trace::events::activity::getenablednodesexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::getEnabledNodesExitEventOccurrence.__init__)


def test_trace::events::activity::getenablednodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::getEnabledNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::isready::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::isReady::actionEntryEventOccurrence)


def test_trace::events::action::isready::actionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::isReady::actionEntryEventOccurrence.__init__)


def test_trace::events::action::isready::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::isReady::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::addtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::addTokensEntryEventOccurrence)


def test_trace::events::activitynode::addtokensentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::addTokensEntryEventOccurrence.__init__)


def test_trace::events::activitynode::addtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::addTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::takeofferedtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence)


def test_trace::events::activitynode::takeofferedtokensentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)


def test_trace::events::activitynode::takeofferedtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)


def test_trace::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)


def test_trace::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::removeTokenEntryEventOccurrence)


def test_trace::events::activitynode::removetokenentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::removeTokenEntryEventOccurrence.__init__)


def test_trace::events::activitynode::removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)


def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)


def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::controlnode::isready::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence)


def test_trace::events::controlnode::isready::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)


def test_trace::events::controlnode::isready::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::forknode::fire::forknodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence)


def test_trace::events::forknode::fire::forknodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence.__init__)


def test_trace::events::forknode::fire::forknodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::fire::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::fire::actionEntryEventOccurrence)


def test_trace::events::action::fire::actionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::fire::actionEntryEventOccurrence.__init__)


def test_trace::events::action::fire::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::fire::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)


def test_trace::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)


def test_trace::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::run::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence)


def test_trace::events::activitynode::run::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence.__init__)


def test_trace::events::activitynode::run::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::isrunningentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::isRunningEntryEventOccurrence)


def test_trace::events::activitynode::isrunningentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::isRunningEntryEventOccurrence.__init__)


def test_trace::events::activitynode::isrunningentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::isRunningEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::sendoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::sendOffersEntryEventOccurrence)


def test_trace::events::activitynode::sendoffersentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::sendOffersEntryEventOccurrence.__init__)


def test_trace::events::activitynode::sendoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::sendOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::iswithdrawnentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::isWithdrawnEntryEventOccurrence)


def test_trace::events::token::iswithdrawnentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::isWithdrawnEntryEventOccurrence.__init__)


def test_trace::events::token::iswithdrawnentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::isWithdrawnEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)


def test_trace::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)


def test_trace::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::evaluateandexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence)


def test_trace::events::booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::addtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::addTokensExitEventOccurrence)


def test_trace::events::activitynode::addtokensexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::addTokensExitEventOccurrence.__init__)


def test_trace::events::activitynode::addtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::addTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence)


def test_trace::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)


def test_trace::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::sendofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::sendOfferExitEventOccurrence)


def test_trace::events::activityedge::sendofferexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::sendOfferExitEventOccurrence.__init__)


def test_trace::events::activityedge::sendofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::sendOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::hasOffersExitEventOccurrence)


def test_trace::events::activitynode::hasoffersexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::hasOffersExitEventOccurrence.__init__)


def test_trace::events::activitynode::hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::hasOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::initialnode::fire::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::InitialNode::fire::initialNodeExitEventOccurrence)


def test_trace::events::initialnode::fire::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::InitialNode::fire::initialNodeExitEventOccurrence.__init__)


def test_trace::events::initialnode::fire::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::InitialNode::fire::initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)


def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::mergenode::hasoffers::mergenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence)


def test_trace::events::mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)


def test_trace::events::mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::action::sendoffers::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Action::sendOffers::actionExitEventOccurrence)


def test_trace::events::action::sendoffers::actionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Action::sendOffers::actionExitEventOccurrence.__init__)


def test_trace::events::action::sendoffers::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Action::sendOffers::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::controlnode::fire::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ControlNode::fire::controlNodeExitEventOccurrence)


def test_trace::events::controlnode::fire::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ControlNode::fire::controlNodeExitEventOccurrence.__init__)


def test_trace::events::controlnode::fire::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ControlNode::fire::controlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)


def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)


def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::withdrawentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::withdrawEntryEventOccurrence)


def test_trace::events::token::withdrawentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::withdrawEntryEventOccurrence.__init__)


def test_trace::events::token::withdrawentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::withdrawEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::isReadyEntryEventOccurrence)


def test_trace::events::activitynode::isreadyentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::isReadyEntryEventOccurrence.__init__)


def test_trace::events::activitynode::isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::isReadyEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::hasofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::hasOfferExitEventOccurrence)


def test_trace::events::activityedge::hasofferexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::hasOfferExitEventOccurrence.__init__)


def test_trace::events::activityedge::hasofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::hasOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence)


def test_trace::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)


def test_trace::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::runExitEventOccurrence)


def test_trace::events::activity::runexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::runExitEventOccurrence.__init__)


def test_trace::events::activity::runexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::hasoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::hasOffersEntryEventOccurrence)


def test_trace::events::activitynode::hasoffersentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::hasOffersEntryEventOccurrence.__init__)


def test_trace::events::activitynode::hasoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::hasOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::evaluateandentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence)


def test_trace::events::booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::sendoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::sendOffersExitEventOccurrence)


def test_trace::events::activitynode::sendoffersexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::sendOffersExitEventOccurrence.__init__)


def test_trace::events::activitynode::sendoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::sendOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence)


def test_trace::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)


def test_trace::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)


def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)


def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::run::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::run::activityNodeExitEventOccurrence)


def test_trace::events::activitynode::run::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::run::activityNodeExitEventOccurrence.__init__)


def test_trace::events::activitynode::run::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::run::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)


def test_trace::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)


def test_trace::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::offer::hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Offer::hasTokensExitEventOccurrence)


def test_trace::events::offer::hastokensexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Offer::hasTokensExitEventOccurrence.__init__)


def test_trace::events::offer::hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Offer::hasTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::evaluateorentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence)


def test_trace::events::booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)


def test_trace::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)


def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)


def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)


def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::initializeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::initializeExitEventOccurrence)


def test_trace::events::activity::initializeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::initializeExitEventOccurrence.__init__)


def test_trace::events::activity::initializeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::initializeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::initializeEntryEventOccurrence)


def test_trace::events::activity::initializeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::initializeEntryEventOccurrence.__init__)


def test_trace::events::activity::initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::initializeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::selectnextnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::selectNextNodeEntryEventOccurrence)


def test_trace::events::activity::selectnextnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::selectNextNodeEntryEventOccurrence.__init__)


def test_trace::events::activity::selectnextnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::selectNextNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::forknode::fire::forknodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ForkNode::fire::forkNodeExitEventOccurrence)


def test_trace::events::forknode::fire::forknodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ForkNode::fire::forkNodeExitEventOccurrence.__init__)


def test_trace::events::forknode::fire::forknodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ForkNode::fire::forkNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::iswithdrawnexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::isWithdrawnExitEventOccurrence)


def test_trace::events::token::iswithdrawnexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::isWithdrawnExitEventOccurrence.__init__)


def test_trace::events::token::iswithdrawnexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::isWithdrawnExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::isrunningexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::isRunningExitEventOccurrence)


def test_trace::events::activitynode::isrunningexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::isRunningExitEventOccurrence.__init__)


def test_trace::events::activitynode::isrunningexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::isRunningExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activityedge::hasofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityEdge::hasOfferEntryEventOccurrence)


def test_trace::events::activityedge::hasofferentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityEdge::hasOfferEntryEventOccurrence.__init__)


def test_trace::events::activityedge::hasofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityEdge::hasOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::terminateentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::terminateEntryEventOccurrence)


def test_trace::events::activity::terminateentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::terminateEntryEventOccurrence.__init__)


def test_trace::events::activity::terminateentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::terminateEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::evaluateaddexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence)


def test_trace::events::integercalculationexpression::evaluateaddexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::evaluateaddexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::transferEntryEventOccurrence)


def test_trace::events::token::transferentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::transferEntryEventOccurrence.__init__)


def test_trace::events::token::transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::transferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)


def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)


def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::runEntryEventOccurrence)


def test_trace::events::activity::runentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::runEntryEventOccurrence.__init__)


def test_trace::events::activity::runentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanbinaryexpression::evaluateorexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence)


def test_trace::events::booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)


def test_trace::events::booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::token::transferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Token::transferExitEventOccurrence)


def test_trace::events::token::transferexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Token::transferExitEventOccurrence.__init__)


def test_trace::events::token::transferexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Token::transferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::controlnode::fire::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence)


def test_trace::events::controlnode::fire::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence.__init__)


def test_trace::events::controlnode::fire::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence)


def test_trace::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)


def test_trace::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)


def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)


def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::decisionnode::fire::decisionnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence)


def test_trace::events::decisionnode::fire::decisionnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)


def test_trace::events::decisionnode::fire::decisionnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::initialnode::isready::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence)


def test_trace::events::initialnode::isready::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)


def test_trace::events::initialnode::isready::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::initialnode::isready::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence)


def test_trace::events::initialnode::isready::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)


def test_trace::events::initialnode::isready::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activitynode::isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ActivityNode::isReadyExitEventOccurrence)


def test_trace::events::activitynode::isreadyexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ActivityNode::isReadyExitEventOccurrence.__init__)


def test_trace::events::activitynode::isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ActivityNode::isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence)


def test_trace::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)


def test_trace::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::selectnextnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::selectNextNodeExitEventOccurrence)


def test_trace::events::activity::selectnextnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::selectNextNodeExitEventOccurrence.__init__)


def test_trace::events::activity::selectnextnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::selectNextNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)


def test_trace::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_trace::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)


def test_trace::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)


def test_trace::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)


def test_trace::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)


def test_trace::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)


def test_trace::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::controlnode::isready::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence)


def test_trace::events::controlnode::isready::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)


def test_trace::events::controlnode::isready::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::getenablednodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::getEnabledNodesEntryEventOccurrence)


def test_trace::events::activity::getenablednodesentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::getEnabledNodesEntryEventOccurrence.__init__)


def test_trace::events::activity::getenablednodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::getEnabledNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence)


def test_trace::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)


def test_trace::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::activity::mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::Activity::mainEntryEventOccurrence)


def test_trace::events::activity::mainentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::Activity::mainEntryEventOccurrence.__init__)


def test_trace::events::activity::mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::Activity::mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)


def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)


def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)


def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_exists():
    assert callable(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)


def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_trace::staticobjectspools_is_not_abstract():
    assert not inspect.isabstract(trace::StaticObjectsPools)


def test_trace::staticobjectspools_constructor_exists():
    assert callable(trace::StaticObjectsPools.__init__)


def test_trace::staticobjectspools_constructor_args():
    sig = inspect.signature(trace::StaticObjectsPools.__init__)
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
trace::activitydiagramConfiguration::TracedOffer_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedOffer,
)
trace::activitydiagramConfiguration::TracedInput_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedInput,
)
TracedToken_strategy = st.builds(
    TracedToken,
)
trace::activitydiagramConfiguration::TracedForkedToken_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedForkedToken,
)
trace::activitydiagramConfiguration::TracedControlToken_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedControlToken,
)
trace::activitydiagramConfiguration::TracedToken_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedToken,
)
trace::activitydiagramConfiguration::TracedInputValue_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedInputValue,
)
activitydiagram::trace::DecisionNode_strategy = st.builds(
    activitydiagram::trace::DecisionNode,
)
activitydiagram::trace::JoinNode_strategy = st.builds(
    activitydiagram::trace::JoinNode,
)
activitydiagram::trace::OpaqueAction_strategy = st.builds(
    activitydiagram::trace::OpaqueAction,
)
trace::activitydiagramConfiguration::TracedTrace_strategy = st.builds(
    trace::activitydiagramConfiguration::TracedTrace,
)
activitydiagram::trace::InitialNode_strategy = st.builds(
    activitydiagram::trace::InitialNode,
)
activitydiagram::trace::ForkNode_strategy = st.builds(
    activitydiagram::trace::ForkNode,
)
activitydiagramConfiguration::TracedForkedToken_strategy = st.builds(
    activitydiagramConfiguration::TracedForkedToken,
)
activitydiagram::TracedVariable_strategy = st.builds(
    activitydiagram::TracedVariable,
)
trace::States::InputValue::variable::State_strategy = st.builds(
    trace::States::InputValue::variable::State,
)
States::trace::GlobalState_strategy = st.builds(
    States::trace::GlobalState,
)
Events::trace::BooleanBinaryExpression_strategy = st.builds(
    Events::trace::BooleanBinaryExpression,
)
Events::trace::BooleanUnaryExpression_strategy = st.builds(
    Events::trace::BooleanUnaryExpression,
)
Events::trace::IntegerComparisonExpression_strategy = st.builds(
    Events::trace::IntegerComparisonExpression,
)
Events::trace::IntegerExpression_strategy = st.builds(
    Events::trace::IntegerExpression,
)
activitydiagram::TracedBooleanVariable_strategy = st.builds(
    activitydiagram::TracedBooleanVariable,
)
Events::trace::IntegerCalculationExpression_strategy = st.builds(
    Events::trace::IntegerCalculationExpression,
)
activitydiagram::TracedStringVariable_strategy = st.builds(
    activitydiagram::TracedStringVariable,
)
Events::trace::Value_strategy = st.builds(
    Events::trace::Value,
)
activitydiagram::TracedIntegerVariable_strategy = st.builds(
    activitydiagram::TracedIntegerVariable,
)
activitydiagram::TracedDecisionNode_strategy = st.builds(
    activitydiagram::TracedDecisionNode,
)
activitydiagram::TracedMergeNode_strategy = st.builds(
    activitydiagram::TracedMergeNode,
)
activitydiagram::TracedInitialNode_strategy = st.builds(
    activitydiagram::TracedInitialNode,
)
activitydiagram::TracedForkNode_strategy = st.builds(
    activitydiagram::TracedForkNode,
)
activitydiagram::TracedActivityFinalNode_strategy = st.builds(
    activitydiagram::TracedActivityFinalNode,
)
activitydiagram::TracedAction_strategy = st.builds(
    activitydiagram::TracedAction,
)
activitydiagram::TracedOpaqueAction_strategy = st.builds(
    activitydiagram::TracedOpaqueAction,
)
activitydiagramConfiguration::TracedToken_strategy = st.builds(
    activitydiagramConfiguration::TracedToken,
)
activitydiagram::TracedControlNode_strategy = st.builds(
    activitydiagram::TracedControlNode,
)
activitydiagram::TracedActivityEdge_strategy = st.builds(
    activitydiagram::TracedActivityEdge,
)
activitydiagram::TracedActivityNode_strategy = st.builds(
    activitydiagram::TracedActivityNode,
)
Offer::hasTokensExitEventOccurrence_strategy = st.builds(
    Offer::hasTokensExitEventOccurrence,
)
Events::trace::EObject_strategy = st.builds(
    Events::trace::EObject,
)
activitydiagram::TracedActivity_strategy = st.builds(
    activitydiagram::TracedActivity,
)
Token::isWithdrawnExitEventOccurrence_strategy = st.builds(
    Token::isWithdrawnExitEventOccurrence,
)
Token::isWithdrawnEntryEventOccurrence_strategy = st.builds(
    Token::isWithdrawnEntryEventOccurrence,
)
BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::evaluateORExitEventOccurrence,
)
Offer::hasTokensEntryEventOccurrence_strategy = st.builds(
    Offer::hasTokensEntryEventOccurrence,
)
ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy = st.builds(
    ForkedToken::withdraw::forkedTokenExitEventOccurrence,
)
ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy = st.builds(
    ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
)
Token::withdrawExitEventOccurrence_strategy = st.builds(
    Token::withdrawExitEventOccurrence,
)
Token::withdrawEntryEventOccurrence_strategy = st.builds(
    Token::withdrawEntryEventOccurrence,
)
Token::transferExitEventOccurrence_strategy = st.builds(
    Token::transferExitEventOccurrence,
)
Token::transferEntryEventOccurrence_strategy = st.builds(
    Token::transferEntryEventOccurrence,
)
BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
)
BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
)
BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::evaluateOREntryEventOccurrence,
)
BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::evaluateANDExitEventOccurrence,
)
BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
)
BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
)
BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(
    BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
)
BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
)
BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
)
IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
)
IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
)
IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
)
IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(
    IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
)
IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
)
IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
)
IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
)
IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
)
IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateADDExitEventOccurrence,
)
StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
)
IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
)
IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
)
IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
)
BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy = st.builds(
    BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
)
BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy = st.builds(
    BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
)
BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy = st.builds(
    BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
)
BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy = st.builds(
    BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
)
StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
)
StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
)
StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
)
InitialNode::fire::initialNodeExitEventOccurrence_strategy = st.builds(
    InitialNode::fire::initialNodeExitEventOccurrence,
)
IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
)
InitialNode::fire::initialNodeEntryEventOccurrence_strategy = st.builds(
    InitialNode::fire::initialNodeEntryEventOccurrence,
)
IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
)
IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
)
DecisionNode::fire::decisionNodeExitEventOccurrence_strategy = st.builds(
    DecisionNode::fire::decisionNodeExitEventOccurrence,
)
DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy = st.builds(
    DecisionNode::fire::decisionNodeEntryEventOccurrence,
)
MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy = st.builds(
    MergeNode::hasOffers::mergeNodeExitEventOccurrence,
)
MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy = st.builds(
    MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
)
ForkNode::fire::forkNodeExitEventOccurrence_strategy = st.builds(
    ForkNode::fire::forkNodeExitEventOccurrence,
)
ForkNode::fire::forkNodeEntryEventOccurrence_strategy = st.builds(
    ForkNode::fire::forkNodeEntryEventOccurrence,
)
ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy = st.builds(
    ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
)
ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
)
Action::isReady::actionEntryEventOccurrence_strategy = st.builds(
    Action::isReady::actionEntryEventOccurrence,
)
Action::sendOffers::actionExitEventOccurrence_strategy = st.builds(
    Action::sendOffers::actionExitEventOccurrence,
)
Action::sendOffers::actionEntryEventOccurrence_strategy = st.builds(
    Action::sendOffers::actionEntryEventOccurrence,
)
ControlNode::fire::controlNodeExitEventOccurrence_strategy = st.builds(
    ControlNode::fire::controlNodeExitEventOccurrence,
)
InitialNode::isReady::InitialNodeExitEventOccurrence_strategy = st.builds(
    InitialNode::isReady::InitialNodeExitEventOccurrence,
)
InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy = st.builds(
    InitialNode::isReady::InitialNodeEntryEventOccurrence,
)
OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy = st.builds(
    OpaqueAction::doAction::opaqueActionExitEventOccurrence,
)
OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy = st.builds(
    OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
)
Action::fire::actionExitEventOccurrence_strategy = st.builds(
    Action::fire::actionExitEventOccurrence,
)
Action::fire::actionEntryEventOccurrence_strategy = st.builds(
    Action::fire::actionEntryEventOccurrence,
)
ActivityNode::isReadyExitEventOccurrence_strategy = st.builds(
    ActivityNode::isReadyExitEventOccurrence,
)
Action::isReady::actionExitEventOccurrence_strategy = st.builds(
    Action::isReady::actionExitEventOccurrence,
)
ActivityNode::isReadyEntryEventOccurrence_strategy = st.builds(
    ActivityNode::isReadyEntryEventOccurrence,
)
ControlNode::fire::controlNodeEntryEventOccurrence_strategy = st.builds(
    ControlNode::fire::controlNodeEntryEventOccurrence,
)
ControlNode::isReady::ControlNodeExitEventOccurrence_strategy = st.builds(
    ControlNode::isReady::ControlNodeExitEventOccurrence,
)
ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy = st.builds(
    ControlNode::isReady::ControlNodeEntryEventOccurrence,
)
ActivityEdge::hasOfferExitEventOccurrence_strategy = st.builds(
    ActivityEdge::hasOfferExitEventOccurrence,
)
ActivityEdge::hasOfferEntryEventOccurrence_strategy = st.builds(
    ActivityEdge::hasOfferEntryEventOccurrence,
)
ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy = st.builds(
    ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
)
ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy = st.builds(
    ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
)
ActivityEdge::sendOfferExitEventOccurrence_strategy = st.builds(
    ActivityEdge::sendOfferExitEventOccurrence,
)
ActivityEdge::sendOfferEntryEventOccurrence_strategy = st.builds(
    ActivityEdge::sendOfferEntryEventOccurrence,
)
ActivityNode::isRunningExitEventOccurrence_strategy = st.builds(
    ActivityNode::isRunningExitEventOccurrence,
)
ActivityNode::isRunningEntryEventOccurrence_strategy = st.builds(
    ActivityNode::isRunningEntryEventOccurrence,
)
ActivityNode::run::activityNodeExitEventOccurrence_strategy = st.builds(
    ActivityNode::run::activityNodeExitEventOccurrence,
)
ActivityNode::hasOffersExitEventOccurrence_strategy = st.builds(
    ActivityNode::hasOffersExitEventOccurrence,
)
ActivityNode::run::activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode::run::activityNodeEntryEventOccurrence,
)
ActivityNode::hasOffersEntryEventOccurrence_strategy = st.builds(
    ActivityNode::hasOffersEntryEventOccurrence,
)
ActivityNode::removeTokenExitEventOccurrence_strategy = st.builds(
    ActivityNode::removeTokenExitEventOccurrence,
)
ActivityNode::removeTokenEntryEventOccurrence_strategy = st.builds(
    ActivityNode::removeTokenEntryEventOccurrence,
)
ActivityNode::addTokensExitEventOccurrence_strategy = st.builds(
    ActivityNode::addTokensExitEventOccurrence,
)
ActivityNode::addTokensEntryEventOccurrence_strategy = st.builds(
    ActivityNode::addTokensEntryEventOccurrence,
)
ActivityNode::takeOfferedTokensExitEventOccurrence_strategy = st.builds(
    ActivityNode::takeOfferedTokensExitEventOccurrence,
)
ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy = st.builds(
    ActivityNode::takeOfferedTokensEntryEventOccurrence,
)
ActivityNode::sendOffersExitEventOccurrence_strategy = st.builds(
    ActivityNode::sendOffersExitEventOccurrence,
)
ActivityNode::sendOffersEntryEventOccurrence_strategy = st.builds(
    ActivityNode::sendOffersEntryEventOccurrence,
)
ActivityNode::terminate::activityNodeExitEventOccurrence_strategy = st.builds(
    ActivityNode::terminate::activityNodeExitEventOccurrence,
)
ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode::terminate::activityNodeEntryEventOccurrence,
)
Activity::runNodesExitEventOccurrence_strategy = st.builds(
    Activity::runNodesExitEventOccurrence,
)
Activity::runNodesEntryEventOccurrence_strategy = st.builds(
    Activity::runNodesEntryEventOccurrence,
)
Activity::runExitEventOccurrence_strategy = st.builds(
    Activity::runExitEventOccurrence,
)
Activity::runEntryEventOccurrence_strategy = st.builds(
    Activity::runEntryEventOccurrence,
)
Activity::initializeExitEventOccurrence_strategy = st.builds(
    Activity::initializeExitEventOccurrence,
)
Activity::initializeEntryEventOccurrence_strategy = st.builds(
    Activity::initializeEntryEventOccurrence,
)
Activity::fireNodeExitEventOccurrence_strategy = st.builds(
    Activity::fireNodeExitEventOccurrence,
)
Activity::fireNodeEntryEventOccurrence_strategy = st.builds(
    Activity::fireNodeEntryEventOccurrence,
)
Activity::getInitialNodeExitEventOccurrence_strategy = st.builds(
    Activity::getInitialNodeExitEventOccurrence,
)
Activity::getInitialNodeEntryEventOccurrence_strategy = st.builds(
    Activity::getInitialNodeEntryEventOccurrence,
)
Activity::terminateExitEventOccurrence_strategy = st.builds(
    Activity::terminateExitEventOccurrence,
)
Activity::terminateEntryEventOccurrence_strategy = st.builds(
    Activity::terminateEntryEventOccurrence,
)
Activity::selectNextNodeExitEventOccurrence_strategy = st.builds(
    Activity::selectNextNodeExitEventOccurrence,
)
Activity::selectNextNodeEntryEventOccurrence_strategy = st.builds(
    Activity::selectNextNodeEntryEventOccurrence,
)
activitydiagram::trace::ActivityFinalNode_strategy = st.builds(
    activitydiagram::trace::ActivityFinalNode,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
trace::activitydiagram::TracedActivityFinalNode_strategy = st.builds(
    trace::activitydiagram::TracedActivityFinalNode,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
activitydiagram::trace::Expression_strategy = st.builds(
    activitydiagram::trace::Expression,
)
trace::activitydiagram::TracedAction_strategy = st.builds(
    trace::activitydiagram::TracedAction,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
trace::activitydiagram::TracedOpaqueAction_strategy = st.builds(
    trace::activitydiagram::TracedOpaqueAction,
)
activitydiagram::trace::StringVariable_strategy = st.builds(
    activitydiagram::trace::StringVariable,
)
activitydiagram::trace::Activity_strategy = st.builds(
    activitydiagram::trace::Activity,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
trace::activitydiagram::TracedActivityNode_strategy = st.builds(
    trace::activitydiagram::TracedActivityNode,
)
trace::activitydiagram::TracedActivity_strategy = st.builds(
    trace::activitydiagram::TracedActivity,
)
trace::activitydiagram::TracedActivityEdge_strategy = st.builds(
    trace::activitydiagram::TracedActivityEdge,
)
activitydiagram::trace::IntegerVariable_strategy = st.builds(
    activitydiagram::trace::IntegerVariable,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
trace::activitydiagram::TracedControlNode_strategy = st.builds(
    trace::activitydiagram::TracedControlNode,
)
trace::activitydiagram::TracedExecutableNode_strategy = st.builds(
    trace::activitydiagram::TracedExecutableNode,
)
activitydiagram::trace::BooleanVariable_strategy = st.builds(
    activitydiagram::trace::BooleanVariable,
)
TracedVariable_strategy = st.builds(
    TracedVariable,
)
trace::activitydiagram::TracedIntegerVariable_strategy = st.builds(
    trace::activitydiagram::TracedIntegerVariable,
)
trace::activitydiagram::TracedStringVariable_strategy = st.builds(
    trace::activitydiagram::TracedStringVariable,
)
trace::activitydiagram::TracedBooleanVariable_strategy = st.builds(
    trace::activitydiagram::TracedBooleanVariable,
)
activitydiagram::trace::MergeNode_strategy = st.builds(
    activitydiagram::trace::MergeNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
trace::activitydiagram::TracedDecisionNode_strategy = st.builds(
    trace::activitydiagram::TracedDecisionNode,
)
trace::activitydiagram::TracedInitialNode_strategy = st.builds(
    trace::activitydiagram::TracedInitialNode,
)
trace::activitydiagram::TracedForkNode_strategy = st.builds(
    trace::activitydiagram::TracedForkNode,
)
trace::activitydiagram::TracedFinalNode_strategy = st.builds(
    trace::activitydiagram::TracedFinalNode,
)
trace::activitydiagram::TracedJoinNode_strategy = st.builds(
    trace::activitydiagram::TracedJoinNode,
)
trace::activitydiagram::TracedMergeNode_strategy = st.builds(
    trace::activitydiagram::TracedMergeNode,
)
activitydiagram::trace::ControlFlow_strategy = st.builds(
    activitydiagram::trace::ControlFlow,
)
TracedActivityEdge_strategy = st.builds(
    TracedActivityEdge,
)
trace::activitydiagram::TracedControlFlow_strategy = st.builds(
    trace::activitydiagram::TracedControlFlow,
)
activitydiagram::TracedJoinNode_strategy = st.builds(
    activitydiagram::TracedJoinNode,
)
activitydiagram::trace::Value_strategy = st.builds(
    activitydiagram::trace::Value,
)
trace::activitydiagram::TracedVariable_strategy = st.builds(
    trace::activitydiagram::TracedVariable,
)
trace::activitydiagram::TracedNamedElement_strategy = st.builds(
    trace::activitydiagram::TracedNamedElement,
    name=
        safe_text
)
activitydiagramConfiguration::TracedControlToken_strategy = st.builds(
    activitydiagramConfiguration::TracedControlToken,
)
activitydiagram::TracedControlFlow_strategy = st.builds(
    activitydiagram::TracedControlFlow,
)
trace::Traced::TracedObjects_strategy = st.builds(
    trace::Traced::TracedObjects,
)
activitydiagramConfiguration::TracedTrace_strategy = st.builds(
    activitydiagramConfiguration::TracedTrace,
)
trace::States::Activity::trace::State_strategy = st.builds(
    trace::States::Activity::trace::State,
)
trace::States::ActivityNode::heldTokens::State_strategy = st.builds(
    trace::States::ActivityNode::heldTokens::State,
)
trace::States::ActivityNode::running::State_strategy = st.builds(
    trace::States::ActivityNode::running::State,
    running=
        st.booleans()
)
trace::States::Offer::offeredTokens::State_strategy = st.builds(
    trace::States::Offer::offeredTokens::State,
)
trace::States::Variable::currentValue::State_strategy = st.builds(
    trace::States::Variable::currentValue::State,
)
trace::States::Trace::executedNodes::State_strategy = st.builds(
    trace::States::Trace::executedNodes::State,
)
trace::States::ForkedToken::baseTokenIsWithdrawn::State_strategy = st.builds(
    trace::States::ForkedToken::baseTokenIsWithdrawn::State,
    baseTokenIsWithdrawn=
        st.booleans()
)
trace::States::ForkedToken::baseToken::State_strategy = st.builds(
    trace::States::ForkedToken::baseToken::State,
)
trace::States::ForkedToken::remainingOffersCount::State_strategy = st.builds(
    trace::States::ForkedToken::remainingOffersCount::State,
    remainingOffersCount=
        st.integers()
)
activitydiagramConfiguration::TracedInput_strategy = st.builds(
    activitydiagramConfiguration::TracedInput,
)
trace::States::Input::inputValues::State_strategy = st.builds(
    trace::States::Input::inputValues::State,
)
trace::States::Token::holder::State_strategy = st.builds(
    trace::States::Token::holder::State,
)
trace::States::ActivityEdge::offers::State_strategy = st.builds(
    trace::States::ActivityEdge::offers::State,
)
activitydiagramConfiguration::TracedInputValue_strategy = st.builds(
    activitydiagramConfiguration::TracedInputValue,
)
States::trace::Value_strategy = st.builds(
    States::trace::Value,
)
trace::States::InputValue::value::State_strategy = st.builds(
    trace::States::InputValue::value::State,
)
activitydiagramConfiguration::TracedOffer_strategy = st.builds(
    activitydiagramConfiguration::TracedOffer,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)
Events_strategy = st.builds(
    Events,
)
trace::GlobalState_strategy = st.builds(
    trace::GlobalState,
)
Activity::getEnabledNodesExitEventOccurrence_strategy = st.builds(
    Activity::getEnabledNodesExitEventOccurrence,
)
Activity::getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    Activity::getEnabledNodesEntryEventOccurrence,
)
Activity::fireInitialNodeExitEventOccurrence_strategy = st.builds(
    Activity::fireInitialNodeExitEventOccurrence,
)
ActivityNode::heldTokens::State_strategy = st.builds(
    ActivityNode::heldTokens::State,
)
Activity::fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    Activity::fireInitialNodeEntryEventOccurrence,
)
ActivityNode::running::State_strategy = st.builds(
    ActivityNode::running::State,
)
Activity::mainExitEventOccurrence_strategy = st.builds(
    Activity::mainExitEventOccurrence,
)
Activity::mainEntryEventOccurrence_strategy = st.builds(
    Activity::mainEntryEventOccurrence,
)
trace::Events::Events_strategy = st.builds(
    trace::Events::Events,
)
Events::trace::GlobalState_strategy = st.builds(
    Events::trace::GlobalState,
)
trace::Events::EventOccurrence_strategy = st.builds(
    trace::Events::EventOccurrence,
)
trace::IntegerCalculationExpression_strategy = st.builds(
    trace::IntegerCalculationExpression,
)
trace::BooleanUnaryExpression_strategy = st.builds(
    trace::BooleanUnaryExpression,
)
trace::IntegerComparisonExpression_strategy = st.builds(
    trace::IntegerComparisonExpression,
)
trace::BooleanValue_strategy = st.builds(
    trace::BooleanValue,
)
trace::IntegerValue_strategy = st.builds(
    trace::IntegerValue,
)
trace::StringValue_strategy = st.builds(
    trace::StringValue,
)
trace::BooleanBinaryExpression_strategy = st.builds(
    trace::BooleanBinaryExpression,
)
Trace::executedNodes::State_strategy = st.builds(
    Trace::executedNodes::State,
)
Activity::trace::State_strategy = st.builds(
    Activity::trace::State,
)
trace::Trace_strategy = st.builds(
    trace::Trace,
)
Offer::offeredTokens::State_strategy = st.builds(
    Offer::offeredTokens::State,
)
Variable::currentValue::State_strategy = st.builds(
    Variable::currentValue::State,
)
ActivityEdge::offers::State_strategy = st.builds(
    ActivityEdge::offers::State,
)
ForkedToken::baseTokenIsWithdrawn::State_strategy = st.builds(
    ForkedToken::baseTokenIsWithdrawn::State,
)
ForkedToken::baseToken::State_strategy = st.builds(
    ForkedToken::baseToken::State,
)
ForkedToken::remainingOffersCount::State_strategy = st.builds(
    ForkedToken::remainingOffersCount::State,
)
Input::inputValues::State_strategy = st.builds(
    Input::inputValues::State,
)
Token::holder::State_strategy = st.builds(
    Token::holder::State,
)
InputValue::variable::State_strategy = st.builds(
    InputValue::variable::State,
)
InputValue::value::State_strategy = st.builds(
    InputValue::value::State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
trace::Events::Action::isReady::actionExitEventOccurrence_strategy = st.builds(
    trace::Events::Action::isReady::actionExitEventOccurrence,
)
trace::Events::Action::fire::actionExitEventOccurrence_strategy = st.builds(
    trace::Events::Action::fire::actionExitEventOccurrence,
)
trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence,
)
trace::Events::Activity::fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::fireInitialNodeEntryEventOccurrence,
)
trace::Events::Activity::terminateExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::terminateExitEventOccurrence,
)
trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence,
)
trace::Events::Offer::hasTokensEntryEventOccurrence_strategy = st.builds(
    trace::Events::Offer::hasTokensEntryEventOccurrence,
)
trace::Events::Action::sendOffers::actionEntryEventOccurrence_strategy = st.builds(
    trace::Events::Action::sendOffers::actionEntryEventOccurrence,
)
trace::Events::Activity::fireNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::fireNodeExitEventOccurrence,
)
trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence,
)
trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
)
trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence,
)
trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
)
trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
)
trace::Events::Activity::runNodesExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::runNodesExitEventOccurrence,
)
trace::Events::Activity::getInitialNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::getInitialNodeEntryEventOccurrence,
)
trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
)
trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence,
)
trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
)
trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence,
)
trace::Events::Activity::fireNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::fireNodeEntryEventOccurrence,
)
trace::Events::Activity::fireInitialNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::fireInitialNodeExitEventOccurrence,
)
trace::Events::Token::withdrawExitEventOccurrence_strategy = st.builds(
    trace::Events::Token::withdrawExitEventOccurrence,
)
trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
)
trace::Events::ActivityEdge::sendOfferEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::sendOfferEntryEventOccurrence,
)
trace::Events::ActivityNode::removeTokenExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::removeTokenExitEventOccurrence,
)
trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
)
trace::Events::Activity::mainExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::mainExitEventOccurrence,
)
trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
)
trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
)
trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
)
trace::Events::Activity::runNodesEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::runNodesEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
)
trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
)
trace::Events::Activity::getInitialNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::getInitialNodeExitEventOccurrence,
)
trace::Events::Activity::getEnabledNodesExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::getEnabledNodesExitEventOccurrence,
)
trace::Events::Action::isReady::actionEntryEventOccurrence_strategy = st.builds(
    trace::Events::Action::isReady::actionEntryEventOccurrence,
)
trace::Events::ActivityNode::addTokensEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::addTokensEntryEventOccurrence,
)
trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
)
trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
)
trace::Events::ActivityNode::removeTokenEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::removeTokenEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
)
trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
)
trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence,
)
trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence,
)
trace::Events::Action::fire::actionEntryEventOccurrence_strategy = st.builds(
    trace::Events::Action::fire::actionEntryEventOccurrence,
)
trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
)
trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence,
)
trace::Events::ActivityNode::isRunningEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::isRunningEntryEventOccurrence,
)
trace::Events::ActivityNode::sendOffersEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::sendOffersEntryEventOccurrence,
)
trace::Events::Token::isWithdrawnEntryEventOccurrence_strategy = st.builds(
    trace::Events::Token::isWithdrawnEntryEventOccurrence,
)
trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
)
trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence,
)
trace::Events::ActivityNode::addTokensExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::addTokensExitEventOccurrence,
)
trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy = st.builds(
    trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
)
trace::Events::ActivityEdge::sendOfferExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::sendOfferExitEventOccurrence,
)
trace::Events::ActivityNode::hasOffersExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::hasOffersExitEventOccurrence,
)
trace::Events::InitialNode::fire::initialNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::InitialNode::fire::initialNodeExitEventOccurrence,
)
trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
)
trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
)
trace::Events::Action::sendOffers::actionExitEventOccurrence_strategy = st.builds(
    trace::Events::Action::sendOffers::actionExitEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
)
trace::Events::ControlNode::fire::controlNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ControlNode::fire::controlNodeExitEventOccurrence,
)
trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
)
trace::Events::Token::withdrawEntryEventOccurrence_strategy = st.builds(
    trace::Events::Token::withdrawEntryEventOccurrence,
)
trace::Events::ActivityNode::isReadyEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::isReadyEntryEventOccurrence,
)
trace::Events::ActivityEdge::hasOfferExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::hasOfferExitEventOccurrence,
)
trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy = st.builds(
    trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence,
)
trace::Events::Activity::runExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::runExitEventOccurrence,
)
trace::Events::ActivityNode::hasOffersEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::hasOffersEntryEventOccurrence,
)
trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
)
trace::Events::ActivityNode::sendOffersExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::sendOffersExitEventOccurrence,
)
trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy = st.builds(
    trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
)
trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
)
trace::Events::ActivityNode::run::activityNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::run::activityNodeExitEventOccurrence,
)
trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
)
trace::Events::Offer::hasTokensExitEventOccurrence_strategy = st.builds(
    trace::Events::Offer::hasTokensExitEventOccurrence,
)
trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence,
)
trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
)
trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
)
trace::Events::Activity::initializeExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::initializeExitEventOccurrence,
)
trace::Events::Activity::initializeEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::initializeEntryEventOccurrence,
)
trace::Events::Activity::selectNextNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::selectNextNodeEntryEventOccurrence,
)
trace::Events::ForkNode::fire::forkNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ForkNode::fire::forkNodeExitEventOccurrence,
)
trace::Events::Token::isWithdrawnExitEventOccurrence_strategy = st.builds(
    trace::Events::Token::isWithdrawnExitEventOccurrence,
)
trace::Events::ActivityNode::isRunningExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::isRunningExitEventOccurrence,
)
trace::Events::ActivityEdge::hasOfferEntryEventOccurrence_strategy = st.builds(
    trace::Events::ActivityEdge::hasOfferEntryEventOccurrence,
)
trace::Events::Activity::terminateEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::terminateEntryEventOccurrence,
)
trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence,
)
trace::Events::Token::transferEntryEventOccurrence_strategy = st.builds(
    trace::Events::Token::transferEntryEventOccurrence,
)
trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
)
trace::Events::Activity::runEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::runEntryEventOccurrence,
)
trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence,
)
trace::Events::Token::transferExitEventOccurrence_strategy = st.builds(
    trace::Events::Token::transferExitEventOccurrence,
)
trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence,
)
trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy = st.builds(
    trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
)
trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
)
trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence,
)
trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy = st.builds(
    trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence,
)
trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence,
)
trace::Events::ActivityNode::isReadyExitEventOccurrence_strategy = st.builds(
    trace::Events::ActivityNode::isReadyExitEventOccurrence,
)
trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy = st.builds(
    trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
)
trace::Events::Activity::selectNextNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::Activity::selectNextNodeExitEventOccurrence,
)
trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
)
trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
)
trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
)
trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence_strategy = st.builds(
    trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence,
)
trace::Events::Activity::getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::getEnabledNodesEntryEventOccurrence,
)
trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(
    trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
)
trace::Events::Activity::mainEntryEventOccurrence_strategy = st.builds(
    trace::Events::Activity::mainEntryEventOccurrence,
)
trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
)
trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(
    trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
)
trace::StaticObjectsPools_strategy = st.builds(
    trace::StaticObjectsPools,
)

@given(instance=trace::activitydiagramConfiguration::TracedOffer_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedoffer_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedOffer)

@given(instance=trace::activitydiagramConfiguration::TracedInput_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedinput_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedInput)

@given(instance=TracedToken_strategy)
@settings(max_examples=50)
def test_tracedtoken_instantiation(instance):
    assert isinstance(instance, TracedToken)

@given(instance=trace::activitydiagramConfiguration::TracedForkedToken_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedForkedToken)

@given(instance=trace::activitydiagramConfiguration::TracedControlToken_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedControlToken)

@given(instance=trace::activitydiagramConfiguration::TracedToken_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedtoken_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedToken)

@given(instance=trace::activitydiagramConfiguration::TracedInputValue_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedinputvalue_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedInputValue)

@given(instance=activitydiagram::trace::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::DecisionNode)

@given(instance=activitydiagram::trace::JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::JoinNode)

@given(instance=activitydiagram::trace::OpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::opaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::OpaqueAction)

@given(instance=trace::activitydiagramConfiguration::TracedTrace_strategy)
@settings(max_examples=50)
def test_trace::activitydiagramconfiguration::tracedtrace_instantiation(instance):
    assert isinstance(instance, trace::activitydiagramConfiguration::TracedTrace)

@given(instance=activitydiagram::trace::InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::InitialNode)

@given(instance=activitydiagram::trace::ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::ForkNode)

@given(instance=activitydiagramConfiguration::TracedForkedToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedForkedToken)

@given(instance=activitydiagram::TracedVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedVariable)

@given(instance=trace::States::InputValue::variable::State_strategy)
@settings(max_examples=50)
def test_trace::states::inputvalue::variable::state_instantiation(instance):
    assert isinstance(instance, trace::States::InputValue::variable::State)

@given(instance=States::trace::GlobalState_strategy)
@settings(max_examples=50)
def test_states::trace::globalstate_instantiation(instance):
    assert isinstance(instance, States::trace::GlobalState)

@given(instance=Events::trace::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_events::trace::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, Events::trace::BooleanBinaryExpression)

@given(instance=Events::trace::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_events::trace::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, Events::trace::BooleanUnaryExpression)

@given(instance=Events::trace::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_events::trace::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, Events::trace::IntegerComparisonExpression)

@given(instance=Events::trace::IntegerExpression_strategy)
@settings(max_examples=50)
def test_events::trace::integerexpression_instantiation(instance):
    assert isinstance(instance, Events::trace::IntegerExpression)

@given(instance=activitydiagram::TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedBooleanVariable)

@given(instance=Events::trace::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_events::trace::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, Events::trace::IntegerCalculationExpression)

@given(instance=activitydiagram::TracedStringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedstringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedStringVariable)

@given(instance=Events::trace::Value_strategy)
@settings(max_examples=50)
def test_events::trace::value_instantiation(instance):
    assert isinstance(instance, Events::trace::Value)

@given(instance=activitydiagram::TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedintegervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedIntegerVariable)

@given(instance=activitydiagram::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedDecisionNode)

@given(instance=activitydiagram::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedmergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedMergeNode)

@given(instance=activitydiagram::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedInitialNode)

@given(instance=activitydiagram::TracedForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedforknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedForkNode)

@given(instance=activitydiagram::TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedActivityFinalNode)

@given(instance=activitydiagram::TracedAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedAction)

@given(instance=activitydiagram::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedOpaqueAction)

@given(instance=activitydiagramConfiguration::TracedToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedToken)

@given(instance=activitydiagram::TracedControlNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedControlNode)

@given(instance=activitydiagram::TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedactivityedge_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedActivityEdge)

@given(instance=activitydiagram::TracedActivityNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedactivitynode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedActivityNode)

@given(instance=Offer::hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_offer::hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Offer::hasTokensExitEventOccurrence)

@given(instance=Events::trace::EObject_strategy)
@settings(max_examples=50)
def test_events::trace::eobject_instantiation(instance):
    assert isinstance(instance, Events::trace::EObject)

@given(instance=activitydiagram::TracedActivity_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedactivity_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedActivity)

@given(instance=Token::isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::iswithdrawnexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::isWithdrawnExitEventOccurrence)

@given(instance=Token::isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::iswithdrawnentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::isWithdrawnEntryEventOccurrence)

@given(instance=BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::evaluateorexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::evaluateORExitEventOccurrence)

@given(instance=Offer::hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_offer::hastokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Offer::hasTokensEntryEventOccurrence)

@given(instance=ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_forkedtoken::withdraw::forkedtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken::withdraw::forkedTokenExitEventOccurrence)

@given(instance=ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_forkedtoken::withdraw::forkedtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkedToken::withdraw::forkedTokenEntryEventOccurrence)

@given(instance=Token::withdrawExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::withdrawexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::withdrawExitEventOccurrence)

@given(instance=Token::withdrawEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::withdrawentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::withdrawEntryEventOccurrence)

@given(instance=Token::transferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::transferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::transferExitEventOccurrence)

@given(instance=Token::transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::transferEntryEventOccurrence)

@given(instance=BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)

@given(instance=BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)

@given(instance=BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::evaluateorentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::evaluateOREntryEventOccurrence)

@given(instance=BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::evaluateandexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::evaluateANDExitEventOccurrence)

@given(instance=BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::evaluateandentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::evaluateANDEntryEventOccurrence)

@given(instance=BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)

@given(instance=BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)

@given(instance=BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::evaluatenotexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::evaluateNOTExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)

@given(instance=BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluateequalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluateequalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)

@given(instance=IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)

@given(instance=IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)

@given(instance=IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integerexpression::getoperandcurrentvaluesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression::getOperandCurrentValuesExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmallerentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)

@given(instance=IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)

@given(instance=IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluatesubtractexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateADDExitEventOccurrence)

@given(instance=StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateADDEntryEventOccurrence)

@given(instance=IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)

@given(instance=IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)

@given(instance=BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)

@given(instance=BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)

@given(instance=BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)

@given(instance=BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)

@given(instance=StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)

@given(instance=StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)

@given(instance=StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable::setCurrentValue::stringVariableExitEventOccurrence)

@given(instance=InitialNode::fire::initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::fire::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::fire::initialNodeExitEventOccurrence)

@given(instance=IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)

@given(instance=InitialNode::fire::initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::fire::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::fire::initialNodeEntryEventOccurrence)

@given(instance=IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::setcurrentvalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)

@given(instance=IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::setcurrentvalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)

@given(instance=DecisionNode::fire::decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_decisionnode::fire::decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode::fire::decisionNodeExitEventOccurrence)

@given(instance=DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_decisionnode::fire::decisionnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode::fire::decisionNodeEntryEventOccurrence)

@given(instance=MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_mergenode::hasoffers::mergenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode::hasOffers::mergeNodeExitEventOccurrence)

@given(instance=MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_mergenode::hasoffers::mergenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, MergeNode::hasOffers::mergeNodeEntryEventOccurrence)

@given(instance=ForkNode::fire::forkNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_forknode::fire::forknodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode::fire::forkNodeExitEventOccurrence)

@given(instance=ForkNode::fire::forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_forknode::fire::forknodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ForkNode::fire::forkNodeEntryEventOccurrence)

@given(instance=ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityfinalnode::fire::activityfinalnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)

@given(instance=ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityfinalnode::fire::activityfinalnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)

@given(instance=Action::isReady::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::isready::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::isReady::actionEntryEventOccurrence)

@given(instance=Action::sendOffers::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::sendoffers::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::sendOffers::actionExitEventOccurrence)

@given(instance=Action::sendOffers::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::sendoffers::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::sendOffers::actionEntryEventOccurrence)

@given(instance=ControlNode::fire::controlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode::fire::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode::fire::controlNodeExitEventOccurrence)

@given(instance=InitialNode::isReady::InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::isready::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::isReady::InitialNodeExitEventOccurrence)

@given(instance=InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::isready::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::isReady::InitialNodeEntryEventOccurrence)

@given(instance=OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_opaqueaction::doaction::opaqueactionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction::doAction::opaqueActionExitEventOccurrence)

@given(instance=OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_opaqueaction::doaction::opaqueactionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, OpaqueAction::doAction::opaqueActionEntryEventOccurrence)

@given(instance=Action::fire::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::fire::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::fire::actionExitEventOccurrence)

@given(instance=Action::fire::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::fire::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::fire::actionEntryEventOccurrence)

@given(instance=ActivityNode::isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isReadyExitEventOccurrence)

@given(instance=Action::isReady::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::isready::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::isReady::actionExitEventOccurrence)

@given(instance=ActivityNode::isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isReadyEntryEventOccurrence)

@given(instance=ControlNode::fire::controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode::fire::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode::fire::controlNodeEntryEventOccurrence)

@given(instance=ControlNode::isReady::ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode::isready::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode::isReady::ControlNodeExitEventOccurrence)

@given(instance=ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_controlnode::isready::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ControlNode::isReady::ControlNodeEntryEventOccurrence)

@given(instance=ActivityEdge::hasOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::hasofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::hasOfferExitEventOccurrence)

@given(instance=ActivityEdge::hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::hasofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::hasOfferEntryEventOccurrence)

@given(instance=ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::takeofferedtokens::activityedgeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)

@given(instance=ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::takeofferedtokens::activityedgeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)

@given(instance=ActivityEdge::sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::sendOfferExitEventOccurrence)

@given(instance=ActivityEdge::sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::sendOfferEntryEventOccurrence)

@given(instance=ActivityNode::isRunningExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isrunningexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isRunningExitEventOccurrence)

@given(instance=ActivityNode::isRunningEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isrunningentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isRunningEntryEventOccurrence)

@given(instance=ActivityNode::run::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::run::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::run::activityNodeExitEventOccurrence)

@given(instance=ActivityNode::hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::hasOffersExitEventOccurrence)

@given(instance=ActivityNode::run::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::run::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::run::activityNodeEntryEventOccurrence)

@given(instance=ActivityNode::hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::hasoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::hasOffersEntryEventOccurrence)

@given(instance=ActivityNode::removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::removeTokenExitEventOccurrence)

@given(instance=ActivityNode::removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::removeTokenEntryEventOccurrence)

@given(instance=ActivityNode::addTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::addtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::addTokensExitEventOccurrence)

@given(instance=ActivityNode::addTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::addtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::addTokensEntryEventOccurrence)

@given(instance=ActivityNode::takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::takeofferedtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::takeOfferedTokensExitEventOccurrence)

@given(instance=ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::takeofferedtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::takeOfferedTokensEntryEventOccurrence)

@given(instance=ActivityNode::sendOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::sendoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::sendOffersExitEventOccurrence)

@given(instance=ActivityNode::sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::sendoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::sendOffersEntryEventOccurrence)

@given(instance=ActivityNode::terminate::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::terminate::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::terminate::activityNodeExitEventOccurrence)

@given(instance=ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::terminate::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::terminate::activityNodeEntryEventOccurrence)

@given(instance=Activity::runNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::runnodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::runNodesExitEventOccurrence)

@given(instance=Activity::runNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::runnodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::runNodesEntryEventOccurrence)

@given(instance=Activity::runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::runExitEventOccurrence)

@given(instance=Activity::runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::runEntryEventOccurrence)

@given(instance=Activity::initializeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::initializeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::initializeExitEventOccurrence)

@given(instance=Activity::initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::initializeEntryEventOccurrence)

@given(instance=Activity::fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireNodeExitEventOccurrence)

@given(instance=Activity::fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::firenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireNodeEntryEventOccurrence)

@given(instance=Activity::getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::getinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::getInitialNodeExitEventOccurrence)

@given(instance=Activity::getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::getinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::getInitialNodeEntryEventOccurrence)

@given(instance=Activity::terminateExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::terminateexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::terminateExitEventOccurrence)

@given(instance=Activity::terminateEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::terminateentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::terminateEntryEventOccurrence)

@given(instance=Activity::selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::selectnextnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::selectNextNodeExitEventOccurrence)

@given(instance=Activity::selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::selectnextnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::selectNextNodeEntryEventOccurrence)

@given(instance=activitydiagram::trace::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::ActivityFinalNode)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=trace::activitydiagram::TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedActivityFinalNode)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=activitydiagram::trace::Expression_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::expression_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::Expression)

@given(instance=trace::activitydiagram::TracedAction_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedaction_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedAction)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=trace::activitydiagram::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedOpaqueAction)

@given(instance=activitydiagram::trace::StringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::stringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::StringVariable)

@given(instance=activitydiagram::trace::Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::activity_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::Activity)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=trace::activitydiagram::TracedActivityNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedactivitynode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedActivityNode)

@given(instance=trace::activitydiagram::TracedActivity_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedactivity_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedActivity)

@given(instance=trace::activitydiagram::TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedactivityedge_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedActivityEdge)

@given(instance=activitydiagram::trace::IntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::integervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::IntegerVariable)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=trace::activitydiagram::TracedControlNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedControlNode)

@given(instance=trace::activitydiagram::TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedExecutableNode)

@given(instance=activitydiagram::trace::BooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::booleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::BooleanVariable)

@given(instance=TracedVariable_strategy)
@settings(max_examples=50)
def test_tracedvariable_instantiation(instance):
    assert isinstance(instance, TracedVariable)

@given(instance=trace::activitydiagram::TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedintegervariable_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedIntegerVariable)

@given(instance=trace::activitydiagram::TracedStringVariable_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedstringvariable_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedStringVariable)

@given(instance=trace::activitydiagram::TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedBooleanVariable)

@given(instance=activitydiagram::trace::MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::MergeNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=trace::activitydiagram::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedDecisionNode)

@given(instance=trace::activitydiagram::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedInitialNode)

@given(instance=trace::activitydiagram::TracedForkNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedforknode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedForkNode)

@given(instance=trace::activitydiagram::TracedFinalNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedfinalnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedFinalNode)

@given(instance=trace::activitydiagram::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedJoinNode)

@given(instance=trace::activitydiagram::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedmergenode_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedMergeNode)

@given(instance=activitydiagram::trace::ControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::controlflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::ControlFlow)

@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)

@given(instance=trace::activitydiagram::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedControlFlow)

@given(instance=activitydiagram::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedJoinNode)

@given(instance=activitydiagram::trace::Value_strategy)
@settings(max_examples=50)
def test_activitydiagram::trace::value_instantiation(instance):
    assert isinstance(instance, activitydiagram::trace::Value)

@given(instance=trace::activitydiagram::TracedVariable_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracedvariable_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedVariable)

@given(instance=trace::activitydiagram::TracedNamedElement_strategy)
@settings(max_examples=50)
def test_trace::activitydiagram::tracednamedelement_instantiation(instance):
    assert isinstance(instance, trace::activitydiagram::TracedNamedElement)

@given(instance=trace::activitydiagram::TracedNamedElement_strategy)
def test_trace::activitydiagram::tracednamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=trace::activitydiagram::TracedNamedElement_strategy)
def test_trace::activitydiagram::tracednamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activitydiagramConfiguration::TracedControlToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedControlToken)

@given(instance=activitydiagram::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedControlFlow)

@given(instance=trace::Traced::TracedObjects_strategy)
@settings(max_examples=50)
def test_trace::traced::tracedobjects_instantiation(instance):
    assert isinstance(instance, trace::Traced::TracedObjects)

@given(instance=activitydiagramConfiguration::TracedTrace_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedtrace_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedTrace)

@given(instance=trace::States::Activity::trace::State_strategy)
@settings(max_examples=50)
def test_trace::states::activity::trace::state_instantiation(instance):
    assert isinstance(instance, trace::States::Activity::trace::State)

@given(instance=trace::States::ActivityNode::heldTokens::State_strategy)
@settings(max_examples=50)
def test_trace::states::activitynode::heldtokens::state_instantiation(instance):
    assert isinstance(instance, trace::States::ActivityNode::heldTokens::State)

@given(instance=trace::States::ActivityNode::running::State_strategy)
@settings(max_examples=50)
def test_trace::states::activitynode::running::state_instantiation(instance):
    assert isinstance(instance, trace::States::ActivityNode::running::State)

@given(instance=trace::States::ActivityNode::running::State_strategy)
def test_trace::states::activitynode::running::state_running_type(instance):
    assert isinstance(instance.running, bool)


@given(instance=trace::States::ActivityNode::running::State_strategy)
def test_trace::states::activitynode::running::state_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=trace::States::Offer::offeredTokens::State_strategy)
@settings(max_examples=50)
def test_trace::states::offer::offeredtokens::state_instantiation(instance):
    assert isinstance(instance, trace::States::Offer::offeredTokens::State)

@given(instance=trace::States::Variable::currentValue::State_strategy)
@settings(max_examples=50)
def test_trace::states::variable::currentvalue::state_instantiation(instance):
    assert isinstance(instance, trace::States::Variable::currentValue::State)

@given(instance=trace::States::Trace::executedNodes::State_strategy)
@settings(max_examples=50)
def test_trace::states::trace::executednodes::state_instantiation(instance):
    assert isinstance(instance, trace::States::Trace::executedNodes::State)

@given(instance=trace::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
@settings(max_examples=50)
def test_trace::states::forkedtoken::basetokeniswithdrawn::state_instantiation(instance):
    assert isinstance(instance, trace::States::ForkedToken::baseTokenIsWithdrawn::State)

@given(instance=trace::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
def test_trace::states::forkedtoken::basetokeniswithdrawn::state_baseTokenIsWithdrawn_type(instance):
    assert isinstance(instance.baseTokenIsWithdrawn, bool)


@given(instance=trace::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
def test_trace::states::forkedtoken::basetokeniswithdrawn::state_baseTokenIsWithdrawn_setter(instance):
    original = instance.baseTokenIsWithdrawn
    instance.baseTokenIsWithdrawn = original
    assert instance.baseTokenIsWithdrawn == original

@given(instance=trace::States::ForkedToken::baseToken::State_strategy)
@settings(max_examples=50)
def test_trace::states::forkedtoken::basetoken::state_instantiation(instance):
    assert isinstance(instance, trace::States::ForkedToken::baseToken::State)

@given(instance=trace::States::ForkedToken::remainingOffersCount::State_strategy)
@settings(max_examples=50)
def test_trace::states::forkedtoken::remainingofferscount::state_instantiation(instance):
    assert isinstance(instance, trace::States::ForkedToken::remainingOffersCount::State)

@given(instance=trace::States::ForkedToken::remainingOffersCount::State_strategy)
def test_trace::states::forkedtoken::remainingofferscount::state_remainingOffersCount_type(instance):
    assert isinstance(instance.remainingOffersCount, int)


@given(instance=trace::States::ForkedToken::remainingOffersCount::State_strategy)
def test_trace::states::forkedtoken::remainingofferscount::state_remainingOffersCount_setter(instance):
    original = instance.remainingOffersCount
    instance.remainingOffersCount = original
    assert instance.remainingOffersCount == original

@given(instance=activitydiagramConfiguration::TracedInput_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedinput_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedInput)

@given(instance=trace::States::Input::inputValues::State_strategy)
@settings(max_examples=50)
def test_trace::states::input::inputvalues::state_instantiation(instance):
    assert isinstance(instance, trace::States::Input::inputValues::State)

@given(instance=trace::States::Token::holder::State_strategy)
@settings(max_examples=50)
def test_trace::states::token::holder::state_instantiation(instance):
    assert isinstance(instance, trace::States::Token::holder::State)

@given(instance=trace::States::ActivityEdge::offers::State_strategy)
@settings(max_examples=50)
def test_trace::states::activityedge::offers::state_instantiation(instance):
    assert isinstance(instance, trace::States::ActivityEdge::offers::State)

@given(instance=activitydiagramConfiguration::TracedInputValue_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedinputvalue_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedInputValue)

@given(instance=States::trace::Value_strategy)
@settings(max_examples=50)
def test_states::trace::value_instantiation(instance):
    assert isinstance(instance, States::trace::Value)

@given(instance=trace::States::InputValue::value::State_strategy)
@settings(max_examples=50)
def test_trace::states::inputvalue::value::state_instantiation(instance):
    assert isinstance(instance, trace::States::InputValue::value::State)

@given(instance=activitydiagramConfiguration::TracedOffer_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedoffer_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedOffer)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=trace::GlobalState_strategy)
@settings(max_examples=50)
def test_trace::globalstate_instantiation(instance):
    assert isinstance(instance, trace::GlobalState)

@given(instance=Activity::getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::getenablednodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::getEnabledNodesExitEventOccurrence)

@given(instance=Activity::getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::getenablednodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::getEnabledNodesEntryEventOccurrence)

@given(instance=Activity::fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::fireinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireInitialNodeExitEventOccurrence)

@given(instance=ActivityNode::heldTokens::State_strategy)
@settings(max_examples=50)
def test_activitynode::heldtokens::state_instantiation(instance):
    assert isinstance(instance, ActivityNode::heldTokens::State)

@given(instance=Activity::fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireInitialNodeEntryEventOccurrence)

@given(instance=ActivityNode::running::State_strategy)
@settings(max_examples=50)
def test_activitynode::running::state_instantiation(instance):
    assert isinstance(instance, ActivityNode::running::State)

@given(instance=Activity::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::mainExitEventOccurrence)

@given(instance=Activity::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::mainEntryEventOccurrence)

@given(instance=trace::Events::Events_strategy)
@settings(max_examples=50)
def test_trace::events::events_instantiation(instance):
    assert isinstance(instance, trace::Events::Events)

@given(instance=Events::trace::GlobalState_strategy)
@settings(max_examples=50)
def test_events::trace::globalstate_instantiation(instance):
    assert isinstance(instance, Events::trace::GlobalState)

@given(instance=trace::Events::EventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::eventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::EventOccurrence)

@given(instance=trace::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_trace::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, trace::IntegerCalculationExpression)

@given(instance=trace::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_trace::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, trace::BooleanUnaryExpression)

@given(instance=trace::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_trace::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, trace::IntegerComparisonExpression)

@given(instance=trace::BooleanValue_strategy)
@settings(max_examples=50)
def test_trace::booleanvalue_instantiation(instance):
    assert isinstance(instance, trace::BooleanValue)

@given(instance=trace::IntegerValue_strategy)
@settings(max_examples=50)
def test_trace::integervalue_instantiation(instance):
    assert isinstance(instance, trace::IntegerValue)

@given(instance=trace::StringValue_strategy)
@settings(max_examples=50)
def test_trace::stringvalue_instantiation(instance):
    assert isinstance(instance, trace::StringValue)

@given(instance=trace::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_trace::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, trace::BooleanBinaryExpression)

@given(instance=Trace::executedNodes::State_strategy)
@settings(max_examples=50)
def test_trace::executednodes::state_instantiation(instance):
    assert isinstance(instance, Trace::executedNodes::State)

@given(instance=Activity::trace::State_strategy)
@settings(max_examples=50)
def test_activity::trace::state_instantiation(instance):
    assert isinstance(instance, Activity::trace::State)

@given(instance=trace::Trace_strategy)
@settings(max_examples=50)
def test_trace::trace_instantiation(instance):
    assert isinstance(instance, trace::Trace)

@given(instance=Offer::offeredTokens::State_strategy)
@settings(max_examples=50)
def test_offer::offeredtokens::state_instantiation(instance):
    assert isinstance(instance, Offer::offeredTokens::State)

@given(instance=Variable::currentValue::State_strategy)
@settings(max_examples=50)
def test_variable::currentvalue::state_instantiation(instance):
    assert isinstance(instance, Variable::currentValue::State)

@given(instance=ActivityEdge::offers::State_strategy)
@settings(max_examples=50)
def test_activityedge::offers::state_instantiation(instance):
    assert isinstance(instance, ActivityEdge::offers::State)

@given(instance=ForkedToken::baseTokenIsWithdrawn::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::basetokeniswithdrawn::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::baseTokenIsWithdrawn::State)

@given(instance=ForkedToken::baseToken::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::basetoken::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::baseToken::State)

@given(instance=ForkedToken::remainingOffersCount::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::remainingofferscount::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::remainingOffersCount::State)

@given(instance=Input::inputValues::State_strategy)
@settings(max_examples=50)
def test_input::inputvalues::state_instantiation(instance):
    assert isinstance(instance, Input::inputValues::State)

@given(instance=Token::holder::State_strategy)
@settings(max_examples=50)
def test_token::holder::state_instantiation(instance):
    assert isinstance(instance, Token::holder::State)

@given(instance=InputValue::variable::State_strategy)
@settings(max_examples=50)
def test_inputvalue::variable::state_instantiation(instance):
    assert isinstance(instance, InputValue::variable::State)

@given(instance=InputValue::value::State_strategy)
@settings(max_examples=50)
def test_inputvalue::value::state_instantiation(instance):
    assert isinstance(instance, InputValue::value::State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=trace::Events::Action::isReady::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::isready::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::isReady::actionExitEventOccurrence)

@given(instance=trace::Events::Action::fire::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::fire::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::fire::actionExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::takeofferedtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::takeOfferedTokensExitEventOccurrence)

@given(instance=trace::Events::Activity::fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::fireInitialNodeEntryEventOccurrence)

@given(instance=trace::Events::Activity::terminateExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::terminateexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::terminateExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::terminate::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::terminate::activityNodeExitEventOccurrence)

@given(instance=trace::Events::Offer::hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::offer::hastokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Offer::hasTokensEntryEventOccurrence)

@given(instance=trace::Events::Action::sendOffers::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::sendoffers::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::sendOffers::actionEntryEventOccurrence)

@given(instance=trace::Events::Activity::fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::fireNodeExitEventOccurrence)

@given(instance=trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::initialnode::fire::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::InitialNode::fire::initialNodeEntryEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)

@given(instance=trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::mergenode::hasoffers::mergenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence)

@given(instance=trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)

@given(instance=trace::Events::Activity::runNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::runnodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::runNodesExitEventOccurrence)

@given(instance=trace::Events::Activity::getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::getinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::getInitialNodeEntryEventOccurrence)

@given(instance=trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::terminate::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence)

@given(instance=trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanunaryexpression::evaluatenotexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence)

@given(instance=trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::decisionnode::fire::decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::DecisionNode::fire::decisionNodeExitEventOccurrence)

@given(instance=trace::Events::Activity::fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::firenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::fireNodeEntryEventOccurrence)

@given(instance=trace::Events::Activity::fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::fireinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::fireInitialNodeExitEventOccurrence)

@given(instance=trace::Events::Token::withdrawExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::withdrawexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::withdrawExitEventOccurrence)

@given(instance=trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanunaryexpression::evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)

@given(instance=trace::Events::ActivityEdge::sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::sendOfferEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::removeTokenExitEventOccurrence)

@given(instance=trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)

@given(instance=trace::Events::Activity::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::mainExitEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)

@given(instance=trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)

@given(instance=trace::Events::Activity::runNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::runnodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::runNodesEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)

@given(instance=trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)

@given(instance=trace::Events::Activity::getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::getinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::getInitialNodeExitEventOccurrence)

@given(instance=trace::Events::Activity::getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::getenablednodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::getEnabledNodesExitEventOccurrence)

@given(instance=trace::Events::Action::isReady::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::isready::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::isReady::actionEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::addTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::addtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::addTokensEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::takeofferedtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)

@given(instance=trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::removeTokenEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)

@given(instance=trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)

@given(instance=trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::controlnode::isready::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence)

@given(instance=trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::forknode::fire::forknodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ForkNode::fire::forkNodeEntryEventOccurrence)

@given(instance=trace::Events::Action::fire::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::fire::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::fire::actionEntryEventOccurrence)

@given(instance=trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::run::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::run::activityNodeEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::isRunningEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::isrunningentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::isRunningEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::sendoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::sendOffersEntryEventOccurrence)

@given(instance=trace::Events::Token::isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::iswithdrawnentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::isWithdrawnEntryEventOccurrence)

@given(instance=trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::evaluateandexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::addTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::addtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::addTokensExitEventOccurrence)

@given(instance=trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)

@given(instance=trace::Events::ActivityEdge::sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::sendOfferExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::hasOffersExitEventOccurrence)

@given(instance=trace::Events::InitialNode::fire::initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::initialnode::fire::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::InitialNode::fire::initialNodeExitEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)

@given(instance=trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::mergenode::hasoffers::mergenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence)

@given(instance=trace::Events::Action::sendOffers::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::action::sendoffers::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Action::sendOffers::actionExitEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)

@given(instance=trace::Events::ControlNode::fire::controlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::controlnode::fire::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ControlNode::fire::controlNodeExitEventOccurrence)

@given(instance=trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)

@given(instance=trace::Events::Token::withdrawEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::withdrawentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::withdrawEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::isReadyEntryEventOccurrence)

@given(instance=trace::Events::ActivityEdge::hasOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::hasofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::hasOfferExitEventOccurrence)

@given(instance=trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence)

@given(instance=trace::Events::Activity::runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::runExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::hasoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::hasOffersEntryEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::evaluateandentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::sendOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::sendoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::sendOffersExitEventOccurrence)

@given(instance=trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)

@given(instance=trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)

@given(instance=trace::Events::ActivityNode::run::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::run::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::run::activityNodeExitEventOccurrence)

@given(instance=trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)

@given(instance=trace::Events::Offer::hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::offer::hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Offer::hasTokensExitEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::evaluateorentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)

@given(instance=trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)

@given(instance=trace::Events::Activity::initializeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::initializeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::initializeExitEventOccurrence)

@given(instance=trace::Events::Activity::initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::initializeEntryEventOccurrence)

@given(instance=trace::Events::Activity::selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::selectnextnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::selectNextNodeEntryEventOccurrence)

@given(instance=trace::Events::ForkNode::fire::forkNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::forknode::fire::forknodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ForkNode::fire::forkNodeExitEventOccurrence)

@given(instance=trace::Events::Token::isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::iswithdrawnexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::isWithdrawnExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::isRunningExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::isrunningexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::isRunningExitEventOccurrence)

@given(instance=trace::Events::ActivityEdge::hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activityedge::hasofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityEdge::hasOfferEntryEventOccurrence)

@given(instance=trace::Events::Activity::terminateEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::terminateentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::terminateEntryEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence)

@given(instance=trace::Events::Token::transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::transferEntryEventOccurrence)

@given(instance=trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)

@given(instance=trace::Events::Activity::runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::runEntryEventOccurrence)

@given(instance=trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanbinaryexpression::evaluateorexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence)

@given(instance=trace::Events::Token::transferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::token::transferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Token::transferExitEventOccurrence)

@given(instance=trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::controlnode::fire::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ControlNode::fire::controlNodeEntryEventOccurrence)

@given(instance=trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence)

@given(instance=trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)

@given(instance=trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::decisionnode::fire::decisionnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence)

@given(instance=trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::initialnode::isready::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence)

@given(instance=trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::initialnode::isready::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::InitialNode::isReady::InitialNodeExitEventOccurrence)

@given(instance=trace::Events::ActivityNode::isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activitynode::isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ActivityNode::isReadyExitEventOccurrence)

@given(instance=trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence)

@given(instance=trace::Events::Activity::selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::selectnextnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::selectNextNodeExitEventOccurrence)

@given(instance=trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)

@given(instance=trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)

@given(instance=trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)

@given(instance=trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::controlnode::isready::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::ControlNode::isReady::ControlNodeExitEventOccurrence)

@given(instance=trace::Events::Activity::getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::getenablednodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::getEnabledNodesEntryEventOccurrence)

@given(instance=trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence)

@given(instance=trace::Events::Activity::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::activity::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::Activity::mainEntryEventOccurrence)

@given(instance=trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)

@given(instance=trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_trace::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, trace::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)

@given(instance=trace::StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_trace::staticobjectspools_instantiation(instance):
    assert isinstance(instance, trace::StaticObjectsPools)
