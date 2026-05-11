import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
    IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
    IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
    BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
    BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
    IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
    IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
    IntegerCalculationExpression::evaluateADDExitEventOccurrence,
    IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
    IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
    IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
    IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
    IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
    IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
    IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
    IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
    StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
    StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
    StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
    StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
    IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
    IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
    IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
    IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
    IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
    DecisionNode::fire::decisionNodeExitEventOccurrence,
    BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
    BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
    BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
    BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
    ForkNode::fire::forkNodeEntryEventOccurrence,
    ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
    ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
    InitialNode::fire::initialNodeExitEventOccurrence,
    InitialNode::fire::initialNodeEntryEventOccurrence,
    InitialNode::isReady::InitialNodeExitEventOccurrence,
    InitialNode::isReady::InitialNodeEntryEventOccurrence,
    OpaqueAction::doAction::opaqueActionExitEventOccurrence,
    OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
    DecisionNode::fire::decisionNodeEntryEventOccurrence,
    MergeNode::hasOffers::mergeNodeExitEventOccurrence,
    MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
    ForkNode::fire::forkNodeExitEventOccurrence,
    Action::sendOffers::actionExitEventOccurrence,
    Action::sendOffers::actionEntryEventOccurrence,
    ControlNode::fire::controlNodeExitEventOccurrence,
    ControlNode::fire::controlNodeEntryEventOccurrence,
    ControlNode::isReady::ControlNodeExitEventOccurrence,
    ControlNode::isReady::ControlNodeEntryEventOccurrence,
    ActivityEdge::hasOfferExitEventOccurrence,
    ActivityEdge::hasOfferEntryEventOccurrence,
    ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
    ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
    activitydiagram::traceSystem::JoinNode,
    activitydiagram::traceSystem::InitialNode,
    traceSystem::activitydiagram::TracedNamedElement,
    activitydiagram::traceSystem::IntegerVariable,
    activitydiagram::traceSystem::DecisionNode,
    activitydiagram::traceSystem::MergeNode,
    activitydiagram::traceSystem::Value,
    activitydiagram::traceSystem::Activity,
    activitydiagram::traceSystem::ControlFlow,
    TracedActivityEdge,
    traceSystem::activitydiagram::TracedControlFlow,
    activitydiagram::traceSystem::ForkNode,
    TracedControlNode,
    traceSystem::activitydiagram::TracedDecisionNode,
    traceSystem::activitydiagram::TracedJoinNode,
    traceSystem::activitydiagram::TracedMergeNode,
    traceSystem::activitydiagram::TracedInitialNode,
    traceSystem::activitydiagram::TracedForkNode,
    activitydiagram::traceSystem::BooleanVariable,
    TracedNamedElement,
    traceSystem::activitydiagram::TracedVariable,
    traceSystem::activitydiagram::TracedActivityNode,
    traceSystem::activitydiagram::TracedActivityEdge,
    traceSystem::activitydiagram::TracedActivity,
    TracedActivityNode,
    traceSystem::activitydiagram::TracedControlNode,
    traceSystem::activitydiagram::TracedExecutableNode,
    activitydiagram::traceSystem::OpaqueAction,
    activitydiagram::traceSystem::Expression,
    TracedAction,
    traceSystem::activitydiagram::TracedOpaqueAction,
    activitydiagram::traceSystem::StringVariable,
    traceSystem::activitydiagram::TracedFinalNode,
    TracedExecutableNode,
    traceSystem::activitydiagram::TracedAction,
    activitydiagram::traceSystem::ActivityFinalNode,
    TracedFinalNode,
    traceSystem::activitydiagram::TracedActivityFinalNode,
    TracedVariable,
    traceSystem::activitydiagram::TracedIntegerVariable,
    traceSystem::activitydiagram::TracedStringVariable,
    traceSystem::activitydiagram::TracedBooleanVariable,
    traceSystem::activitydiagramConfiguration::TracedInput,
    traceSystem::activitydiagramConfiguration::TracedTrace,
    traceSystem::activitydiagramConfiguration::TracedInputValue,
    traceSystem::activitydiagramConfiguration::TracedOffer,
    traceSystem::activitydiagramConfiguration::TracedToken,
    TracedToken,
    traceSystem::activitydiagramConfiguration::TracedControlToken,
    traceSystem::activitydiagramConfiguration::TracedForkedToken,
    traceSystem::Traced::TracedObjects,
    activitydiagram::TracedJoinNode,
    activitydiagramConfiguration::TracedControlToken,
    activitydiagram::TracedControlFlow,
    traceSystem::States::ActivityEdge::offers::State,
    traceSystem::States::ActivityNode::running::State,
    traceSystem::States::ActivityNode::heldTokens::State,
    activitydiagramConfiguration::TracedInput,
    traceSystem::States::Input::inputValues::State,
    traceSystem::States::Trace::executedNodes::State,
    traceSystem::States::Offer::offeredTokens::State,
    traceSystem::States::InputValue::variable::State,
    activitydiagramConfiguration::TracedInputValue,
    traceSystem::States::InputValue::value::State,
    activitydiagram::TracedVariable,
    States::traceSystem::Value,
    traceSystem::States::Variable::currentValue::State,
    activitydiagramConfiguration::TracedTrace,
    traceSystem::States::Activity::trace::State,
    activitydiagramConfiguration::TracedForkedToken,
    traceSystem::States::Token::holder::State,
    traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State,
    traceSystem::States::ForkedToken::remainingOffersCount::State,
    States::traceSystem::GlobalState,
    traceSystem::States::ForkedToken::baseToken::State,
    activitydiagramConfiguration::TracedOffer,
    Events::traceSystem::BooleanBinaryExpression,
    Events::traceSystem::BooleanUnaryExpression,
    Events::traceSystem::IntegerComparisonExpression,
    Events::traceSystem::IntegerCalculationExpression,
    Events::traceSystem::IntegerExpression,
    activitydiagram::TracedDecisionNode,
    activitydiagram::TracedBooleanVariable,
    activitydiagram::TracedStringVariable,
    Events::traceSystem::Value,
    activitydiagram::TracedIntegerVariable,
    activitydiagram::TracedInitialNode,
    activitydiagram::TracedMergeNode,
    activitydiagram::TracedOpaqueAction,
    activitydiagram::TracedForkNode,
    activitydiagram::TracedActivityFinalNode,
    activitydiagram::TracedAction,
    activitydiagramConfiguration::TracedToken,
    activitydiagram::TracedControlNode,
    activitydiagram::TracedActivityEdge,
    activitydiagram::TracedActivityNode,
    Offer::hasTokensEntryEventOccurrence,
    ForkedToken::withdraw::forkedTokenExitEventOccurrence,
    ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
    Token::withdrawExitEventOccurrence,
    Token::withdrawEntryEventOccurrence,
    Token::transferExitEventOccurrence,
    Events::traceSystem::EObject,
    activitydiagram::TracedActivity,
    Offer::hasTokensExitEventOccurrence,
    BooleanBinaryExpression::evaluateOREntryEventOccurrence,
    BooleanBinaryExpression::evaluateANDExitEventOccurrence,
    BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
    BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
    BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
    BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
    BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
    Token::transferEntryEventOccurrence,
    Token::isWithdrawnExitEventOccurrence,
    Token::isWithdrawnEntryEventOccurrence,
    BooleanBinaryExpression::evaluateORExitEventOccurrence,
    IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
    IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
    Action::fire::actionExitEventOccurrence,
    Action::fire::actionEntryEventOccurrence,
    Action::isReady::actionExitEventOccurrence,
    Action::isReady::actionEntryEventOccurrence,
    ActivityNode::hasOffersExitEventOccurrence,
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
    ActivityEdge::sendOfferExitEventOccurrence,
    ActivityEdge::sendOfferEntryEventOccurrence,
    ActivityNode::isReadyExitEventOccurrence,
    ActivityNode::isReadyEntryEventOccurrence,
    Activity::fireNodeEntryEventOccurrence,
    Activity::getInitialNodeExitEventOccurrence,
    Activity::getInitialNodeEntryEventOccurrence,
    Activity::terminateExitEventOccurrence,
    Activity::terminateEntryEventOccurrence,
    Activity::selectNextNodeExitEventOccurrence,
    Activity::selectNextNodeEntryEventOccurrence,
    Activity::getEnabledNodesExitEventOccurrence,
    Activity::getEnabledNodesEntryEventOccurrence,
    Activity::fireInitialNodeExitEventOccurrence,
    Activity::fireInitialNodeEntryEventOccurrence,
    ActivityNode::terminate::activityNodeEntryEventOccurrence,
    ActivityNode::isRunningExitEventOccurrence,
    ActivityNode::isRunningEntryEventOccurrence,
    ActivityNode::run::activityNodeExitEventOccurrence,
    ActivityNode::run::activityNodeEntryEventOccurrence,
    Activity::fireNodeExitEventOccurrence,
    Activity::initializeEntryEventOccurrence,
    Activity::mainExitEventOccurrence,
    Activity::mainEntryEventOccurrence,
    traceSystem::Events::Events,
    Events::traceSystem::GlobalState,
    traceSystem::Events::EventOccurrence,
    traceSystem::IntegerCalculationExpression,
    traceSystem::IntegerValue,
    traceSystem::BooleanUnaryExpression,
    traceSystem::BooleanBinaryExpression,
    traceSystem::StringValue,
    traceSystem::IntegerComparisonExpression,
    traceSystem::BooleanValue,
    ActivityNode::running::State,
    ActivityNode::heldTokens::State,
    Activity::runNodesExitEventOccurrence,
    Activity::runNodesEntryEventOccurrence,
    Activity::runExitEventOccurrence,
    Activity::runEntryEventOccurrence,
    Activity::initializeExitEventOccurrence,
    InputValue::value::State,
    Variable::currentValue::State,
    Activity::trace::State,
    Offer::offeredTokens::State,
    Token::holder::State,
    ForkedToken::baseTokenIsWithdrawn::State,
    ForkedToken::remainingOffersCount::State,
    Input::inputValues::State,
    Trace::executedNodes::State,
    ActivityEdge::offers::State,
    InputValue::variable::State,
    Events,
    traceSystem::GlobalState,
    traceSystem::Trace,
    ForkedToken::baseToken::State,
    EventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
    traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
    traceSystem::Events::Action::fire::actionEntryEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence,
    traceSystem::Events::Action::sendOffers::actionExitEventOccurrence,
    traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
    traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
    traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
    traceSystem::Events::Activity::mainEntryEventOccurrence,
    traceSystem::Events::Activity::fireNodeExitEventOccurrence,
    traceSystem::Events::Activity::fireNodeEntryEventOccurrence,
    traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence,
    traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence,
    traceSystem::Events::Token::isWithdrawnEntryEventOccurrence,
    traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
    traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
    traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
    traceSystem::Events::Activity::initializeExitEventOccurrence,
    traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence,
    traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
    traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence,
    traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence,
    traceSystem::Events::Activity::runExitEventOccurrence,
    traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
    traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence,
    traceSystem::Events::Action::isReady::actionExitEventOccurrence,
    traceSystem::Events::Token::withdrawEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
    traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence,
    traceSystem::Events::ActivityNode::isRunningExitEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
    traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence,
    traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence,
    traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence,
    traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence,
    traceSystem::Events::Action::fire::actionExitEventOccurrence,
    traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence,
    traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence,
    traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence,
    traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
    traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence,
    traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
    traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence,
    traceSystem::Events::Activity::runEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
    traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence,
    traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence,
    traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence,
    traceSystem::Events::Activity::terminateEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
    traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
    traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
    traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence,
    traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence,
    traceSystem::Events::Activity::terminateExitEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
    traceSystem::Events::Activity::runNodesEntryEventOccurrence,
    traceSystem::Events::Token::transferEntryEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence,
    traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
    traceSystem::Events::Activity::mainExitEventOccurrence,
    traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence,
    traceSystem::Events::Activity::getInitialNodeExitEventOccurrence,
    traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
    traceSystem::Events::Activity::runNodesExitEventOccurrence,
    traceSystem::Events::Token::withdrawExitEventOccurrence,
    traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
    traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence,
    traceSystem::Events::Token::transferExitEventOccurrence,
    traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
    traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence,
    traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
    traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence,
    traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
    traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence,
    traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
    traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence,
    traceSystem::Events::Action::isReady::actionEntryEventOccurrence,
    traceSystem::Events::Offer::hasTokensEntryEventOccurrence,
    traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence,
    traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence,
    traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
    traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence,
    traceSystem::Events::ActivityNode::isReadyExitEventOccurrence,
    traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence,
    traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence,
    traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence,
    traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence,
    traceSystem::Events::Activity::selectNextNodeExitEventOccurrence,
    traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence,
    traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
    traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence,
    traceSystem::Events::ActivityNode::addTokensExitEventOccurrence,
    traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence,
    traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
    traceSystem::Events::Offer::hasTokensExitEventOccurrence,
    traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
    traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence,
    traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
    traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
    traceSystem::Events::Token::isWithdrawnExitEventOccurrence,
    traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence,
    traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
    traceSystem::Events::Activity::initializeEntryEventOccurrence,
    traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
    traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
    traceSystem::StaticObjectsPools,
    TracedObjects,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)


def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)


def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)
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



def test_integercalculationexpression::evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerCalculationExpression::evaluateADDEntryEventOccurrence)


def test_integercalculationexpression::evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)


def test_integercalculationexpression::evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)
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



def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)


def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)


def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)
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



def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)


def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)


def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)


def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)


def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)


def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)


def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)
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



def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)


def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_decisionnode::fire::decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(DecisionNode::fire::decisionNodeExitEventOccurrence)


def test_decisionnode::fire::decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)


def test_decisionnode::fire::decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)
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



def test_initialnode::fire::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::fire::initialNodeExitEventOccurrence)


def test_initialnode::fire::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(InitialNode::fire::initialNodeExitEventOccurrence.__init__)


def test_initialnode::fire::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::fire::initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_initialnode::fire::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(InitialNode::fire::initialNodeEntryEventOccurrence)


def test_initialnode::fire::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(InitialNode::fire::initialNodeEntryEventOccurrence.__init__)


def test_initialnode::fire::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(InitialNode::fire::initialNodeEntryEventOccurrence.__init__)
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



def test_activitydiagram::tracesystem::joinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::JoinNode)


def test_activitydiagram::tracesystem::joinnode_constructor_exists():
    assert callable(activitydiagram::traceSystem::JoinNode.__init__)


def test_activitydiagram::tracesystem::joinnode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::JoinNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::initialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::InitialNode)


def test_activitydiagram::tracesystem::initialnode_constructor_exists():
    assert callable(activitydiagram::traceSystem::InitialNode.__init__)


def test_activitydiagram::tracesystem::initialnode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::InitialNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedNamedElement)


def test_tracesystem::activitydiagram::tracednamedelement_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedNamedElement.__init__)


def test_tracesystem::activitydiagram::tracednamedelement_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedNamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_tracesystem::activitydiagram::tracednamedelement_has_name():
    assert hasattr(traceSystem::activitydiagram::TracedNamedElement, "name")
    descriptor = None
    for klass in traceSystem::activitydiagram::TracedNamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_activitydiagram::tracesystem::integervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::IntegerVariable)


def test_activitydiagram::tracesystem::integervariable_constructor_exists():
    assert callable(activitydiagram::traceSystem::IntegerVariable.__init__)


def test_activitydiagram::tracesystem::integervariable_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::IntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::decisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::DecisionNode)


def test_activitydiagram::tracesystem::decisionnode_constructor_exists():
    assert callable(activitydiagram::traceSystem::DecisionNode.__init__)


def test_activitydiagram::tracesystem::decisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::DecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::mergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::MergeNode)


def test_activitydiagram::tracesystem::mergenode_constructor_exists():
    assert callable(activitydiagram::traceSystem::MergeNode.__init__)


def test_activitydiagram::tracesystem::mergenode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::MergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::value_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::Value)


def test_activitydiagram::tracesystem::value_constructor_exists():
    assert callable(activitydiagram::traceSystem::Value.__init__)


def test_activitydiagram::tracesystem::value_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::activity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::Activity)


def test_activitydiagram::tracesystem::activity_constructor_exists():
    assert callable(activitydiagram::traceSystem::Activity.__init__)


def test_activitydiagram::tracesystem::activity_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::Activity.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::controlflow_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::ControlFlow)


def test_activitydiagram::tracesystem::controlflow_constructor_exists():
    assert callable(activitydiagram::traceSystem::ControlFlow.__init__)


def test_activitydiagram::tracesystem::controlflow_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::ControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(TracedActivityEdge)


def test_tracedactivityedge_constructor_exists():
    assert callable(TracedActivityEdge.__init__)


def test_tracedactivityedge_constructor_args():
    sig = inspect.signature(TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedcontrolflow_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedControlFlow)


def test_tracesystem::activitydiagram::tracedcontrolflow_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedControlFlow.__init__)


def test_tracesystem::activitydiagram::tracedcontrolflow_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedControlFlow.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::forknode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::ForkNode)


def test_activitydiagram::tracesystem::forknode_constructor_exists():
    assert callable(activitydiagram::traceSystem::ForkNode.__init__)


def test_activitydiagram::tracesystem::forknode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::ForkNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(TracedControlNode)


def test_tracedcontrolnode_constructor_exists():
    assert callable(TracedControlNode.__init__)


def test_tracedcontrolnode_constructor_args():
    sig = inspect.signature(TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedDecisionNode)


def test_tracesystem::activitydiagram::traceddecisionnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedDecisionNode.__init__)


def test_tracesystem::activitydiagram::traceddecisionnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedJoinNode)


def test_tracesystem::activitydiagram::tracedjoinnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedJoinNode.__init__)


def test_tracesystem::activitydiagram::tracedjoinnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedMergeNode)


def test_tracesystem::activitydiagram::tracedmergenode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedMergeNode.__init__)


def test_tracesystem::activitydiagram::tracedmergenode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedInitialNode)


def test_tracesystem::activitydiagram::tracedinitialnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedInitialNode.__init__)


def test_tracesystem::activitydiagram::tracedinitialnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedforknode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedForkNode)


def test_tracesystem::activitydiagram::tracedforknode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedForkNode.__init__)


def test_tracesystem::activitydiagram::tracedforknode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedForkNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::booleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::BooleanVariable)


def test_activitydiagram::tracesystem::booleanvariable_constructor_exists():
    assert callable(activitydiagram::traceSystem::BooleanVariable.__init__)


def test_activitydiagram::tracesystem::booleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::BooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracednamedelement_is_not_abstract():
    assert not inspect.isabstract(TracedNamedElement)


def test_tracednamedelement_constructor_exists():
    assert callable(TracedNamedElement.__init__)


def test_tracednamedelement_constructor_args():
    sig = inspect.signature(TracedNamedElement.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedVariable)


def test_tracesystem::activitydiagram::tracedvariable_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedVariable.__init__)


def test_tracesystem::activitydiagram::tracedvariable_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedActivityNode)


def test_tracesystem::activitydiagram::tracedactivitynode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedActivityNode.__init__)


def test_tracesystem::activitydiagram::tracedactivitynode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedactivityedge_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedActivityEdge)


def test_tracesystem::activitydiagram::tracedactivityedge_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedActivityEdge.__init__)


def test_tracesystem::activitydiagram::tracedactivityedge_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedActivityEdge.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedActivity)


def test_tracesystem::activitydiagram::tracedactivity_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedActivity.__init__)


def test_tracesystem::activitydiagram::tracedactivity_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_tracedactivitynode_is_not_abstract():
    assert not inspect.isabstract(TracedActivityNode)


def test_tracedactivitynode_constructor_exists():
    assert callable(TracedActivityNode.__init__)


def test_tracedactivitynode_constructor_args():
    sig = inspect.signature(TracedActivityNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedcontrolnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedControlNode)


def test_tracesystem::activitydiagram::tracedcontrolnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedControlNode.__init__)


def test_tracesystem::activitydiagram::tracedcontrolnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedControlNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedExecutableNode)


def test_tracesystem::activitydiagram::tracedexecutablenode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedExecutableNode.__init__)


def test_tracesystem::activitydiagram::tracedexecutablenode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::opaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::OpaqueAction)


def test_activitydiagram::tracesystem::opaqueaction_constructor_exists():
    assert callable(activitydiagram::traceSystem::OpaqueAction.__init__)


def test_activitydiagram::tracesystem::opaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::OpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::expression_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::Expression)


def test_activitydiagram::tracesystem::expression_constructor_exists():
    assert callable(activitydiagram::traceSystem::Expression.__init__)


def test_activitydiagram::tracesystem::expression_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::Expression.__init__)
    params = list(sig.parameters.keys())



def test_tracedaction_is_not_abstract():
    assert not inspect.isabstract(TracedAction)


def test_tracedaction_constructor_exists():
    assert callable(TracedAction.__init__)


def test_tracedaction_constructor_args():
    sig = inspect.signature(TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedOpaqueAction)


def test_tracesystem::activitydiagram::tracedopaqueaction_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedOpaqueAction.__init__)


def test_tracesystem::activitydiagram::tracedopaqueaction_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedOpaqueAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::stringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::StringVariable)


def test_activitydiagram::tracesystem::stringvariable_constructor_exists():
    assert callable(activitydiagram::traceSystem::StringVariable.__init__)


def test_activitydiagram::tracesystem::stringvariable_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::StringVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedFinalNode)


def test_tracesystem::activitydiagram::tracedfinalnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedFinalNode.__init__)


def test_tracesystem::activitydiagram::tracedfinalnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedexecutablenode_is_not_abstract():
    assert not inspect.isabstract(TracedExecutableNode)


def test_tracedexecutablenode_constructor_exists():
    assert callable(TracedExecutableNode.__init__)


def test_tracedexecutablenode_constructor_args():
    sig = inspect.signature(TracedExecutableNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedaction_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedAction)


def test_tracesystem::activitydiagram::tracedaction_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedAction.__init__)


def test_tracesystem::activitydiagram::tracedaction_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedAction.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracesystem::activityfinalnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::traceSystem::ActivityFinalNode)


def test_activitydiagram::tracesystem::activityfinalnode_constructor_exists():
    assert callable(activitydiagram::traceSystem::ActivityFinalNode.__init__)


def test_activitydiagram::tracesystem::activityfinalnode_constructor_args():
    sig = inspect.signature(activitydiagram::traceSystem::ActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedfinalnode_is_not_abstract():
    assert not inspect.isabstract(TracedFinalNode)


def test_tracedfinalnode_constructor_exists():
    assert callable(TracedFinalNode.__init__)


def test_tracedfinalnode_constructor_args():
    sig = inspect.signature(TracedFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedactivityfinalnode_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedActivityFinalNode)


def test_tracesystem::activitydiagram::tracedactivityfinalnode_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedActivityFinalNode.__init__)


def test_tracesystem::activitydiagram::tracedactivityfinalnode_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedActivityFinalNode.__init__)
    params = list(sig.parameters.keys())



def test_tracedvariable_is_not_abstract():
    assert not inspect.isabstract(TracedVariable)


def test_tracedvariable_constructor_exists():
    assert callable(TracedVariable.__init__)


def test_tracedvariable_constructor_args():
    sig = inspect.signature(TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedIntegerVariable)


def test_tracesystem::activitydiagram::tracedintegervariable_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedIntegerVariable.__init__)


def test_tracesystem::activitydiagram::tracedintegervariable_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedStringVariable)


def test_tracesystem::activitydiagram::tracedstringvariable_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedStringVariable.__init__)


def test_tracesystem::activitydiagram::tracedstringvariable_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagram::tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagram::TracedBooleanVariable)


def test_tracesystem::activitydiagram::tracedbooleanvariable_constructor_exists():
    assert callable(traceSystem::activitydiagram::TracedBooleanVariable.__init__)


def test_tracesystem::activitydiagram::tracedbooleanvariable_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagram::TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedinput_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedInput)


def test_tracesystem::activitydiagramconfiguration::tracedinput_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedInput.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedinput_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedtrace_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedTrace)


def test_tracesystem::activitydiagramconfiguration::tracedtrace_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedTrace.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedtrace_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedInputValue)


def test_tracesystem::activitydiagramconfiguration::tracedinputvalue_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedInputValue.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedinputvalue_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedoffer_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedOffer)


def test_tracesystem::activitydiagramconfiguration::tracedoffer_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedOffer.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedoffer_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedtoken_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedToken)


def test_tracesystem::activitydiagramconfiguration::tracedtoken_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedToken.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedtoken_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_tracedtoken_is_not_abstract():
    assert not inspect.isabstract(TracedToken)


def test_tracedtoken_constructor_exists():
    assert callable(TracedToken.__init__)


def test_tracedtoken_constructor_args():
    sig = inspect.signature(TracedToken.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedcontroltoken_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedControlToken)


def test_tracesystem::activitydiagramconfiguration::tracedcontroltoken_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedControlToken.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedcontroltoken_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedControlToken.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::activitydiagramconfiguration::tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(traceSystem::activitydiagramConfiguration::TracedForkedToken)


def test_tracesystem::activitydiagramconfiguration::tracedforkedtoken_constructor_exists():
    assert callable(traceSystem::activitydiagramConfiguration::TracedForkedToken.__init__)


def test_tracesystem::activitydiagramconfiguration::tracedforkedtoken_constructor_args():
    sig = inspect.signature(traceSystem::activitydiagramConfiguration::TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::traced::tracedobjects_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Traced::TracedObjects)


def test_tracesystem::traced::tracedobjects_constructor_exists():
    assert callable(traceSystem::Traced::TracedObjects.__init__)


def test_tracesystem::traced::tracedobjects_constructor_args():
    sig = inspect.signature(traceSystem::Traced::TracedObjects.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedjoinnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedJoinNode)


def test_activitydiagram::tracedjoinnode_constructor_exists():
    assert callable(activitydiagram::TracedJoinNode.__init__)


def test_activitydiagram::tracedjoinnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedJoinNode.__init__)
    params = list(sig.parameters.keys())



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



def test_tracesystem::states::activityedge::offers::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ActivityEdge::offers::State)


def test_tracesystem::states::activityedge::offers::state_constructor_exists():
    assert callable(traceSystem::States::ActivityEdge::offers::State.__init__)


def test_tracesystem::states::activityedge::offers::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ActivityEdge::offers::State.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::activitynode::running::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ActivityNode::running::State)


def test_tracesystem::states::activitynode::running::state_constructor_exists():
    assert callable(traceSystem::States::ActivityNode::running::State.__init__)


def test_tracesystem::states::activitynode::running::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ActivityNode::running::State.__init__)
    params = list(sig.parameters.keys())
    assert "running" in params, "Missing parameter 'running'"

def test_tracesystem::states::activitynode::running::state_has_running():
    assert hasattr(traceSystem::States::ActivityNode::running::State, "running")
    descriptor = None
    for klass in traceSystem::States::ActivityNode::running::State.__mro__:
        if "running" in klass.__dict__:
            descriptor = klass.__dict__["running"]
            break
    assert isinstance(descriptor, property)



def test_tracesystem::states::activitynode::heldtokens::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ActivityNode::heldTokens::State)


def test_tracesystem::states::activitynode::heldtokens::state_constructor_exists():
    assert callable(traceSystem::States::ActivityNode::heldTokens::State.__init__)


def test_tracesystem::states::activitynode::heldtokens::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ActivityNode::heldTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedinput_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedInput)


def test_activitydiagramconfiguration::tracedinput_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedInput.__init__)


def test_activitydiagramconfiguration::tracedinput_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedInput.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::input::inputvalues::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Input::inputValues::State)


def test_tracesystem::states::input::inputvalues::state_constructor_exists():
    assert callable(traceSystem::States::Input::inputValues::State.__init__)


def test_tracesystem::states::input::inputvalues::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Input::inputValues::State.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::trace::executednodes::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Trace::executedNodes::State)


def test_tracesystem::states::trace::executednodes::state_constructor_exists():
    assert callable(traceSystem::States::Trace::executedNodes::State.__init__)


def test_tracesystem::states::trace::executednodes::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Trace::executedNodes::State.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::offer::offeredtokens::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Offer::offeredTokens::State)


def test_tracesystem::states::offer::offeredtokens::state_constructor_exists():
    assert callable(traceSystem::States::Offer::offeredTokens::State.__init__)


def test_tracesystem::states::offer::offeredtokens::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Offer::offeredTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::inputvalue::variable::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::InputValue::variable::State)


def test_tracesystem::states::inputvalue::variable::state_constructor_exists():
    assert callable(traceSystem::States::InputValue::variable::State.__init__)


def test_tracesystem::states::inputvalue::variable::state_constructor_args():
    sig = inspect.signature(traceSystem::States::InputValue::variable::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedinputvalue_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedInputValue)


def test_activitydiagramconfiguration::tracedinputvalue_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedInputValue.__init__)


def test_activitydiagramconfiguration::tracedinputvalue_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedInputValue.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::inputvalue::value::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::InputValue::value::State)


def test_tracesystem::states::inputvalue::value::state_constructor_exists():
    assert callable(traceSystem::States::InputValue::value::State.__init__)


def test_tracesystem::states::inputvalue::value::state_constructor_args():
    sig = inspect.signature(traceSystem::States::InputValue::value::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedVariable)


def test_activitydiagram::tracedvariable_constructor_exists():
    assert callable(activitydiagram::TracedVariable.__init__)


def test_activitydiagram::tracedvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedVariable.__init__)
    params = list(sig.parameters.keys())



def test_states::tracesystem::value_is_not_abstract():
    assert not inspect.isabstract(States::traceSystem::Value)


def test_states::tracesystem::value_constructor_exists():
    assert callable(States::traceSystem::Value.__init__)


def test_states::tracesystem::value_constructor_args():
    sig = inspect.signature(States::traceSystem::Value.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::variable::currentvalue::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Variable::currentValue::State)


def test_tracesystem::states::variable::currentvalue::state_constructor_exists():
    assert callable(traceSystem::States::Variable::currentValue::State.__init__)


def test_tracesystem::states::variable::currentvalue::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Variable::currentValue::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedtrace_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedTrace)


def test_activitydiagramconfiguration::tracedtrace_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedTrace.__init__)


def test_activitydiagramconfiguration::tracedtrace_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedTrace.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::activity::trace::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Activity::trace::State)


def test_tracesystem::states::activity::trace::state_constructor_exists():
    assert callable(traceSystem::States::Activity::trace::State.__init__)


def test_tracesystem::states::activity::trace::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Activity::trace::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedforkedtoken_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedForkedToken)


def test_activitydiagramconfiguration::tracedforkedtoken_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedForkedToken.__init__)


def test_activitydiagramconfiguration::tracedforkedtoken_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedForkedToken.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::token::holder::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::Token::holder::State)


def test_tracesystem::states::token::holder::state_constructor_exists():
    assert callable(traceSystem::States::Token::holder::State.__init__)


def test_tracesystem::states::token::holder::state_constructor_args():
    sig = inspect.signature(traceSystem::States::Token::holder::State.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State)


def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_constructor_exists():
    assert callable(traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State.__init__)


def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State.__init__)
    params = list(sig.parameters.keys())
    assert "baseTokenIsWithdrawn" in params, "Missing parameter 'baseTokenIsWithdrawn'"

def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_has_baseTokenIsWithdrawn():
    assert hasattr(traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State, "baseTokenIsWithdrawn")
    descriptor = None
    for klass in traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State.__mro__:
        if "baseTokenIsWithdrawn" in klass.__dict__:
            descriptor = klass.__dict__["baseTokenIsWithdrawn"]
            break
    assert isinstance(descriptor, property)



def test_tracesystem::states::forkedtoken::remainingofferscount::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ForkedToken::remainingOffersCount::State)


def test_tracesystem::states::forkedtoken::remainingofferscount::state_constructor_exists():
    assert callable(traceSystem::States::ForkedToken::remainingOffersCount::State.__init__)


def test_tracesystem::states::forkedtoken::remainingofferscount::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ForkedToken::remainingOffersCount::State.__init__)
    params = list(sig.parameters.keys())
    assert "remainingOffersCount" in params, "Missing parameter 'remainingOffersCount'"

def test_tracesystem::states::forkedtoken::remainingofferscount::state_has_remainingOffersCount():
    assert hasattr(traceSystem::States::ForkedToken::remainingOffersCount::State, "remainingOffersCount")
    descriptor = None
    for klass in traceSystem::States::ForkedToken::remainingOffersCount::State.__mro__:
        if "remainingOffersCount" in klass.__dict__:
            descriptor = klass.__dict__["remainingOffersCount"]
            break
    assert isinstance(descriptor, property)



def test_states::tracesystem::globalstate_is_not_abstract():
    assert not inspect.isabstract(States::traceSystem::GlobalState)


def test_states::tracesystem::globalstate_constructor_exists():
    assert callable(States::traceSystem::GlobalState.__init__)


def test_states::tracesystem::globalstate_constructor_args():
    sig = inspect.signature(States::traceSystem::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::states::forkedtoken::basetoken::state_is_not_abstract():
    assert not inspect.isabstract(traceSystem::States::ForkedToken::baseToken::State)


def test_tracesystem::states::forkedtoken::basetoken::state_constructor_exists():
    assert callable(traceSystem::States::ForkedToken::baseToken::State.__init__)


def test_tracesystem::states::forkedtoken::basetoken::state_constructor_args():
    sig = inspect.signature(traceSystem::States::ForkedToken::baseToken::State.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagramconfiguration::tracedoffer_is_not_abstract():
    assert not inspect.isabstract(activitydiagramConfiguration::TracedOffer)


def test_activitydiagramconfiguration::tracedoffer_constructor_exists():
    assert callable(activitydiagramConfiguration::TracedOffer.__init__)


def test_activitydiagramconfiguration::tracedoffer_constructor_args():
    sig = inspect.signature(activitydiagramConfiguration::TracedOffer.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::BooleanBinaryExpression)


def test_events::tracesystem::booleanbinaryexpression_constructor_exists():
    assert callable(Events::traceSystem::BooleanBinaryExpression.__init__)


def test_events::tracesystem::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(Events::traceSystem::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::BooleanUnaryExpression)


def test_events::tracesystem::booleanunaryexpression_constructor_exists():
    assert callable(Events::traceSystem::BooleanUnaryExpression.__init__)


def test_events::tracesystem::booleanunaryexpression_constructor_args():
    sig = inspect.signature(Events::traceSystem::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::IntegerComparisonExpression)


def test_events::tracesystem::integercomparisonexpression_constructor_exists():
    assert callable(Events::traceSystem::IntegerComparisonExpression.__init__)


def test_events::tracesystem::integercomparisonexpression_constructor_args():
    sig = inspect.signature(Events::traceSystem::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::IntegerCalculationExpression)


def test_events::tracesystem::integercalculationexpression_constructor_exists():
    assert callable(Events::traceSystem::IntegerCalculationExpression.__init__)


def test_events::tracesystem::integercalculationexpression_constructor_args():
    sig = inspect.signature(Events::traceSystem::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::integerexpression_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::IntegerExpression)


def test_events::tracesystem::integerexpression_constructor_exists():
    assert callable(Events::traceSystem::IntegerExpression.__init__)


def test_events::tracesystem::integerexpression_constructor_args():
    sig = inspect.signature(Events::traceSystem::IntegerExpression.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::traceddecisionnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedDecisionNode)


def test_activitydiagram::traceddecisionnode_constructor_exists():
    assert callable(activitydiagram::TracedDecisionNode.__init__)


def test_activitydiagram::traceddecisionnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedDecisionNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedbooleanvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedBooleanVariable)


def test_activitydiagram::tracedbooleanvariable_constructor_exists():
    assert callable(activitydiagram::TracedBooleanVariable.__init__)


def test_activitydiagram::tracedbooleanvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedBooleanVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedstringvariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedStringVariable)


def test_activitydiagram::tracedstringvariable_constructor_exists():
    assert callable(activitydiagram::TracedStringVariable.__init__)


def test_activitydiagram::tracedstringvariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedStringVariable.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::value_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::Value)


def test_events::tracesystem::value_constructor_exists():
    assert callable(Events::traceSystem::Value.__init__)


def test_events::tracesystem::value_constructor_args():
    sig = inspect.signature(Events::traceSystem::Value.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedintegervariable_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedIntegerVariable)


def test_activitydiagram::tracedintegervariable_constructor_exists():
    assert callable(activitydiagram::TracedIntegerVariable.__init__)


def test_activitydiagram::tracedintegervariable_constructor_args():
    sig = inspect.signature(activitydiagram::TracedIntegerVariable.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedinitialnode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedInitialNode)


def test_activitydiagram::tracedinitialnode_constructor_exists():
    assert callable(activitydiagram::TracedInitialNode.__init__)


def test_activitydiagram::tracedinitialnode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedInitialNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedmergenode_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedMergeNode)


def test_activitydiagram::tracedmergenode_constructor_exists():
    assert callable(activitydiagram::TracedMergeNode.__init__)


def test_activitydiagram::tracedmergenode_constructor_args():
    sig = inspect.signature(activitydiagram::TracedMergeNode.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedopaqueaction_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedOpaqueAction)


def test_activitydiagram::tracedopaqueaction_constructor_exists():
    assert callable(activitydiagram::TracedOpaqueAction.__init__)


def test_activitydiagram::tracedopaqueaction_constructor_args():
    sig = inspect.signature(activitydiagram::TracedOpaqueAction.__init__)
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



def test_events::tracesystem::eobject_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::EObject)


def test_events::tracesystem::eobject_constructor_exists():
    assert callable(Events::traceSystem::EObject.__init__)


def test_events::tracesystem::eobject_constructor_args():
    sig = inspect.signature(Events::traceSystem::EObject.__init__)
    params = list(sig.parameters.keys())



def test_activitydiagram::tracedactivity_is_not_abstract():
    assert not inspect.isabstract(activitydiagram::TracedActivity)


def test_activitydiagram::tracedactivity_constructor_exists():
    assert callable(activitydiagram::TracedActivity.__init__)


def test_activitydiagram::tracedactivity_constructor_args():
    sig = inspect.signature(activitydiagram::TracedActivity.__init__)
    params = list(sig.parameters.keys())



def test_offer::hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Offer::hasTokensExitEventOccurrence)


def test_offer::hastokensexiteventoccurrence_constructor_exists():
    assert callable(Offer::hasTokensExitEventOccurrence.__init__)


def test_offer::hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(Offer::hasTokensExitEventOccurrence.__init__)
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



def test_booleanunaryexpression::evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)


def test_booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)


def test_booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_token::transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Token::transferEntryEventOccurrence)


def test_token::transferentryeventoccurrence_constructor_exists():
    assert callable(Token::transferEntryEventOccurrence.__init__)


def test_token::transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(Token::transferEntryEventOccurrence.__init__)
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



def test_action::isready::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::isReady::actionExitEventOccurrence)


def test_action::isready::actionexiteventoccurrence_constructor_exists():
    assert callable(Action::isReady::actionExitEventOccurrence.__init__)


def test_action::isready::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(Action::isReady::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_action::isready::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Action::isReady::actionEntryEventOccurrence)


def test_action::isready::actionentryeventoccurrence_constructor_exists():
    assert callable(Action::isReady::actionEntryEventOccurrence.__init__)


def test_action::isready::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(Action::isReady::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::hasOffersExitEventOccurrence)


def test_activitynode::hasoffersexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::hasOffersExitEventOccurrence.__init__)


def test_activitynode::hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::hasOffersExitEventOccurrence.__init__)
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



def test_activitynode::isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isReadyExitEventOccurrence)


def test_activitynode::isreadyexiteventoccurrence_constructor_exists():
    assert callable(ActivityNode::isReadyExitEventOccurrence.__init__)


def test_activitynode::isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::isReadyEntryEventOccurrence)


def test_activitynode::isreadyentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::isReadyEntryEventOccurrence.__init__)


def test_activitynode::isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::isReadyEntryEventOccurrence.__init__)
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



def test_activity::fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireInitialNodeEntryEventOccurrence)


def test_activity::fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(Activity::fireInitialNodeEntryEventOccurrence.__init__)


def test_activity::fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::terminate::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::terminate::activityNodeEntryEventOccurrence)


def test_activitynode::terminate::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)


def test_activitynode::terminate::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)
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



def test_activitynode::run::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::run::activityNodeEntryEventOccurrence)


def test_activitynode::run::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(ActivityNode::run::activityNodeEntryEventOccurrence.__init__)


def test_activitynode::run::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(ActivityNode::run::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::fireNodeExitEventOccurrence)


def test_activity::firenodeexiteventoccurrence_constructor_exists():
    assert callable(Activity::fireNodeExitEventOccurrence.__init__)


def test_activity::firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(Activity::fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_activity::initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(Activity::initializeEntryEventOccurrence)


def test_activity::initializeentryeventoccurrence_constructor_exists():
    assert callable(Activity::initializeEntryEventOccurrence.__init__)


def test_activity::initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(Activity::initializeEntryEventOccurrence.__init__)
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



def test_tracesystem::events::events_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Events)


def test_tracesystem::events::events_constructor_exists():
    assert callable(traceSystem::Events::Events.__init__)


def test_tracesystem::events::events_constructor_args():
    sig = inspect.signature(traceSystem::Events::Events.__init__)
    params = list(sig.parameters.keys())



def test_events::tracesystem::globalstate_is_not_abstract():
    assert not inspect.isabstract(Events::traceSystem::GlobalState)


def test_events::tracesystem::globalstate_constructor_exists():
    assert callable(Events::traceSystem::GlobalState.__init__)


def test_events::tracesystem::globalstate_constructor_args():
    sig = inspect.signature(Events::traceSystem::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::EventOccurrence)


def test_tracesystem::events::eventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::EventOccurrence.__init__)


def test_tracesystem::events::eventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::integercalculationexpression_is_not_abstract():
    assert not inspect.isabstract(traceSystem::IntegerCalculationExpression)


def test_tracesystem::integercalculationexpression_constructor_exists():
    assert callable(traceSystem::IntegerCalculationExpression.__init__)


def test_tracesystem::integercalculationexpression_constructor_args():
    sig = inspect.signature(traceSystem::IntegerCalculationExpression.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::integervalue_is_not_abstract():
    assert not inspect.isabstract(traceSystem::IntegerValue)


def test_tracesystem::integervalue_constructor_exists():
    assert callable(traceSystem::IntegerValue.__init__)


def test_tracesystem::integervalue_constructor_args():
    sig = inspect.signature(traceSystem::IntegerValue.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::booleanunaryexpression_is_not_abstract():
    assert not inspect.isabstract(traceSystem::BooleanUnaryExpression)


def test_tracesystem::booleanunaryexpression_constructor_exists():
    assert callable(traceSystem::BooleanUnaryExpression.__init__)


def test_tracesystem::booleanunaryexpression_constructor_args():
    sig = inspect.signature(traceSystem::BooleanUnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::booleanbinaryexpression_is_not_abstract():
    assert not inspect.isabstract(traceSystem::BooleanBinaryExpression)


def test_tracesystem::booleanbinaryexpression_constructor_exists():
    assert callable(traceSystem::BooleanBinaryExpression.__init__)


def test_tracesystem::booleanbinaryexpression_constructor_args():
    sig = inspect.signature(traceSystem::BooleanBinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::stringvalue_is_not_abstract():
    assert not inspect.isabstract(traceSystem::StringValue)


def test_tracesystem::stringvalue_constructor_exists():
    assert callable(traceSystem::StringValue.__init__)


def test_tracesystem::stringvalue_constructor_args():
    sig = inspect.signature(traceSystem::StringValue.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::integercomparisonexpression_is_not_abstract():
    assert not inspect.isabstract(traceSystem::IntegerComparisonExpression)


def test_tracesystem::integercomparisonexpression_constructor_exists():
    assert callable(traceSystem::IntegerComparisonExpression.__init__)


def test_tracesystem::integercomparisonexpression_constructor_args():
    sig = inspect.signature(traceSystem::IntegerComparisonExpression.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(traceSystem::BooleanValue)


def test_tracesystem::booleanvalue_constructor_exists():
    assert callable(traceSystem::BooleanValue.__init__)


def test_tracesystem::booleanvalue_constructor_args():
    sig = inspect.signature(traceSystem::BooleanValue.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::running::state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::running::State)


def test_activitynode::running::state_constructor_exists():
    assert callable(ActivityNode::running::State.__init__)


def test_activitynode::running::state_constructor_args():
    sig = inspect.signature(ActivityNode::running::State.__init__)
    params = list(sig.parameters.keys())



def test_activitynode::heldtokens::state_is_not_abstract():
    assert not inspect.isabstract(ActivityNode::heldTokens::State)


def test_activitynode::heldtokens::state_constructor_exists():
    assert callable(ActivityNode::heldTokens::State.__init__)


def test_activitynode::heldtokens::state_constructor_args():
    sig = inspect.signature(ActivityNode::heldTokens::State.__init__)
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



def test_inputvalue::value::state_is_not_abstract():
    assert not inspect.isabstract(InputValue::value::State)


def test_inputvalue::value::state_constructor_exists():
    assert callable(InputValue::value::State.__init__)


def test_inputvalue::value::state_constructor_args():
    sig = inspect.signature(InputValue::value::State.__init__)
    params = list(sig.parameters.keys())



def test_variable::currentvalue::state_is_not_abstract():
    assert not inspect.isabstract(Variable::currentValue::State)


def test_variable::currentvalue::state_constructor_exists():
    assert callable(Variable::currentValue::State.__init__)


def test_variable::currentvalue::state_constructor_args():
    sig = inspect.signature(Variable::currentValue::State.__init__)
    params = list(sig.parameters.keys())



def test_activity::trace::state_is_not_abstract():
    assert not inspect.isabstract(Activity::trace::State)


def test_activity::trace::state_constructor_exists():
    assert callable(Activity::trace::State.__init__)


def test_activity::trace::state_constructor_args():
    sig = inspect.signature(Activity::trace::State.__init__)
    params = list(sig.parameters.keys())



def test_offer::offeredtokens::state_is_not_abstract():
    assert not inspect.isabstract(Offer::offeredTokens::State)


def test_offer::offeredtokens::state_constructor_exists():
    assert callable(Offer::offeredTokens::State.__init__)


def test_offer::offeredtokens::state_constructor_args():
    sig = inspect.signature(Offer::offeredTokens::State.__init__)
    params = list(sig.parameters.keys())



def test_token::holder::state_is_not_abstract():
    assert not inspect.isabstract(Token::holder::State)


def test_token::holder::state_constructor_exists():
    assert callable(Token::holder::State.__init__)


def test_token::holder::state_constructor_args():
    sig = inspect.signature(Token::holder::State.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::basetokeniswithdrawn::state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::baseTokenIsWithdrawn::State)


def test_forkedtoken::basetokeniswithdrawn::state_constructor_exists():
    assert callable(ForkedToken::baseTokenIsWithdrawn::State.__init__)


def test_forkedtoken::basetokeniswithdrawn::state_constructor_args():
    sig = inspect.signature(ForkedToken::baseTokenIsWithdrawn::State.__init__)
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



def test_trace::executednodes::state_is_not_abstract():
    assert not inspect.isabstract(Trace::executedNodes::State)


def test_trace::executednodes::state_constructor_exists():
    assert callable(Trace::executedNodes::State.__init__)


def test_trace::executednodes::state_constructor_args():
    sig = inspect.signature(Trace::executedNodes::State.__init__)
    params = list(sig.parameters.keys())



def test_activityedge::offers::state_is_not_abstract():
    assert not inspect.isabstract(ActivityEdge::offers::State)


def test_activityedge::offers::state_constructor_exists():
    assert callable(ActivityEdge::offers::State.__init__)


def test_activityedge::offers::state_constructor_args():
    sig = inspect.signature(ActivityEdge::offers::State.__init__)
    params = list(sig.parameters.keys())



def test_inputvalue::variable::state_is_not_abstract():
    assert not inspect.isabstract(InputValue::variable::State)


def test_inputvalue::variable::state_constructor_exists():
    assert callable(InputValue::variable::State.__init__)


def test_inputvalue::variable::state_constructor_args():
    sig = inspect.signature(InputValue::variable::State.__init__)
    params = list(sig.parameters.keys())



def test_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_events_constructor_exists():
    assert callable(Events.__init__)


def test_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::globalstate_is_not_abstract():
    assert not inspect.isabstract(traceSystem::GlobalState)


def test_tracesystem::globalstate_constructor_exists():
    assert callable(traceSystem::GlobalState.__init__)


def test_tracesystem::globalstate_constructor_args():
    sig = inspect.signature(traceSystem::GlobalState.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::trace_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Trace)


def test_tracesystem::trace_constructor_exists():
    assert callable(traceSystem::Trace.__init__)


def test_tracesystem::trace_constructor_args():
    sig = inspect.signature(traceSystem::Trace.__init__)
    params = list(sig.parameters.keys())



def test_forkedtoken::basetoken::state_is_not_abstract():
    assert not inspect.isabstract(ForkedToken::baseToken::State)


def test_forkedtoken::basetoken::state_constructor_exists():
    assert callable(ForkedToken::baseToken::State.__init__)


def test_forkedtoken::basetoken::state_constructor_args():
    sig = inspect.signature(ForkedToken::baseToken::State.__init__)
    params = list(sig.parameters.keys())



def test_eventoccurrence_is_not_abstract():
    assert not inspect.isabstract(EventOccurrence)


def test_eventoccurrence_constructor_exists():
    assert callable(EventOccurrence.__init__)


def test_eventoccurrence_constructor_args():
    sig = inspect.signature(EventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)


def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)


def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::fire::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::fire::actionEntryEventOccurrence)


def test_tracesystem::events::action::fire::actionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::fire::actionEntryEventOccurrence.__init__)


def test_tracesystem::events::action::fire::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::fire::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::evaluateandexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::evaluateandexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::sendoffers::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::sendOffers::actionExitEventOccurrence)


def test_tracesystem::events::action::sendoffers::actionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::sendOffers::actionExitEventOccurrence.__init__)


def test_tracesystem::events::action::sendoffers::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::sendOffers::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence)


def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)


def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)


def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)


def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)


def test_tracesystem::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence)


def test_tracesystem::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)


def test_tracesystem::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)


def test_tracesystem::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::mainentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::mainEntryEventOccurrence)


def test_tracesystem::events::activity::mainentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::mainEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::mainentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::mainEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::firenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::fireNodeExitEventOccurrence)


def test_tracesystem::events::activity::firenodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::fireNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activity::firenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::fireNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::firenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::fireNodeEntryEventOccurrence)


def test_tracesystem::events::activity::firenodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::fireNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::firenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::fireNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::initialnode::isready::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence)


def test_tracesystem::events::initialnode::isready::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::initialnode::isready::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::initialnode::fire::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence)


def test_tracesystem::events::initialnode::fire::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence.__init__)


def test_tracesystem::events::initialnode::fire::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::iswithdrawnentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::isWithdrawnEntryEventOccurrence)


def test_tracesystem::events::token::iswithdrawnentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::isWithdrawnEntryEventOccurrence.__init__)


def test_tracesystem::events::token::iswithdrawnentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::isWithdrawnEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence)


def test_tracesystem::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)


def test_tracesystem::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)


def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)


def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)


def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::initializeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::initializeExitEventOccurrence)


def test_tracesystem::events::activity::initializeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::initializeExitEventOccurrence.__init__)


def test_tracesystem::events::activity::initializeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::initializeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::forknode::fire::forknodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence)


def test_tracesystem::events::forknode::fire::forknodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence.__init__)


def test_tracesystem::events::forknode::fire::forknodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)


def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)


def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::fireinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence)


def test_tracesystem::events::activity::fireinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activity::fireinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence)


def test_tracesystem::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)


def test_tracesystem::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::runexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::runExitEventOccurrence)


def test_tracesystem::events::activity::runexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::runExitEventOccurrence.__init__)


def test_tracesystem::events::activity::runexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::runExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanunaryexpression::evaluatenotexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence)


def test_tracesystem::events::booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)


def test_tracesystem::events::booleanunaryexpression::evaluatenotexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::hasoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence)


def test_tracesystem::events::activitynode::hasoffersentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::hasoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::isready::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::isReady::actionExitEventOccurrence)


def test_tracesystem::events::action::isready::actionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::isReady::actionExitEventOccurrence.__init__)


def test_tracesystem::events::action::isready::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::isReady::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::withdrawentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::withdrawEntryEventOccurrence)


def test_tracesystem::events::token::withdrawentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::withdrawEntryEventOccurrence.__init__)


def test_tracesystem::events::token::withdrawentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::withdrawEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::initialnode::isready::initialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence)


def test_tracesystem::events::initialnode::isready::initialnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)


def test_tracesystem::events::initialnode::isready::initialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::isrunningexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::isRunningExitEventOccurrence)


def test_tracesystem::events::activitynode::isrunningexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::isRunningExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::isrunningexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::isRunningExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::sendoffers::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence)


def test_tracesystem::events::action::sendoffers::actionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence.__init__)


def test_tracesystem::events::action::sendoffers::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::fireinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence)


def test_tracesystem::events::activity::fireinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::fireinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::forknode::fire::forknodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence)


def test_tracesystem::events::forknode::fire::forknodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::forknode::fire::forknodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::terminate::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence)


def test_tracesystem::events::activitynode::terminate::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::terminate::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::fire::actionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::fire::actionExitEventOccurrence)


def test_tracesystem::events::action::fire::actionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::fire::actionExitEventOccurrence.__init__)


def test_tracesystem::events::action::fire::actionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::fire::actionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::controlnode::isready::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence)


def test_tracesystem::events::controlnode::isready::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)


def test_tracesystem::events::controlnode::isready::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::isreadyentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence)


def test_tracesystem::events::activitynode::isreadyentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::isreadyentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::takeofferedtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence)


def test_tracesystem::events::activitynode::takeofferedtokensexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::takeofferedtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::removetokenexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence)


def test_tracesystem::events::activitynode::removetokenexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::removetokenexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)


def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence)


def test_tracesystem::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)


def test_tracesystem::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)


def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::takeofferedtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence)


def test_tracesystem::events::activitynode::takeofferedtokensentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::takeofferedtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::evaluateorentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::evaluateorentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::runentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::runEntryEventOccurrence)


def test_tracesystem::events::activity::runentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::runEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::runentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::runEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::isrunningentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence)


def test_tracesystem::events::activitynode::isrunningentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::isrunningentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::initialnode::fire::initialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence)


def test_tracesystem::events::initialnode::fire::initialnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::initialnode::fire::initialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::getenablednodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence)


def test_tracesystem::events::activity::getenablednodesentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::getenablednodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::terminateentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::terminateEntryEventOccurrence)


def test_tracesystem::events::activity::terminateentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::terminateEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::terminateentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::terminateEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)


def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::mergenode::hasoffers::mergenodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence)


def test_tracesystem::events::mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)


def test_tracesystem::events::mergenode::hasoffers::mergenodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::controlnode::isready::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence)


def test_tracesystem::events::controlnode::isready::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::controlnode::isready::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::controlnode::fire::controlnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence)


def test_tracesystem::events::controlnode::fire::controlnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::controlnode::fire::controlnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::terminateexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::terminateExitEventOccurrence)


def test_tracesystem::events::activity::terminateexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::terminateExitEventOccurrence.__init__)


def test_tracesystem::events::activity::terminateexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::terminateExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::runnodesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::runNodesEntryEventOccurrence)


def test_tracesystem::events::activity::runnodesentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::runNodesEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::runnodesentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::runNodesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::transferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::transferEntryEventOccurrence)


def test_tracesystem::events::token::transferentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::transferEntryEventOccurrence.__init__)


def test_tracesystem::events::token::transferentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::transferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::evaluateorexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::evaluateorexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence)


def test_tracesystem::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)


def test_tracesystem::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::mainexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::mainExitEventOccurrence)


def test_tracesystem::events::activity::mainexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::mainExitEventOccurrence.__init__)


def test_tracesystem::events::activity::mainexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::mainExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::decisionnode::fire::decisionnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence)


def test_tracesystem::events::decisionnode::fire::decisionnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)


def test_tracesystem::events::decisionnode::fire::decisionnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::getinitialnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::getInitialNodeExitEventOccurrence)


def test_tracesystem::events::activity::getinitialnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::getInitialNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activity::getinitialnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::getInitialNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)


def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)


def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::runnodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::runNodesExitEventOccurrence)


def test_tracesystem::events::activity::runnodesexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::runNodesExitEventOccurrence.__init__)


def test_tracesystem::events::activity::runnodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::runNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::withdrawexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::withdrawExitEventOccurrence)


def test_tracesystem::events::token::withdrawexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::withdrawExitEventOccurrence.__init__)


def test_tracesystem::events::token::withdrawexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::withdrawExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)


def test_tracesystem::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::selectnextnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence)


def test_tracesystem::events::activity::selectnextnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::selectnextnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::transferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::transferExitEventOccurrence)


def test_tracesystem::events::token::transferexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::transferExitEventOccurrence.__init__)


def test_tracesystem::events::token::transferexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::transferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)


def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::evaluateandentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::evaluateandentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)


def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)


def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::evaluateaddexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence)


def test_tracesystem::events::integercalculationexpression::evaluateaddexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::evaluateaddexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercalculationexpression::evaluateaddentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence)


def test_tracesystem::events::integercalculationexpression::evaluateaddentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)


def test_tracesystem::events::integercalculationexpression::evaluateaddentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::hasofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence)


def test_tracesystem::events::activityedge::hasofferexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence.__init__)


def test_tracesystem::events::activityedge::hasofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)


def test_tracesystem::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)


def test_tracesystem::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::decisionnode::fire::decisionnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence)


def test_tracesystem::events::decisionnode::fire::decisionnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::decisionnode::fire::decisionnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)


def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::hasoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence)


def test_tracesystem::events::activitynode::hasoffersexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::hasoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::action::isready::actionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Action::isReady::actionEntryEventOccurrence)


def test_tracesystem::events::action::isready::actionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Action::isReady::actionEntryEventOccurrence.__init__)


def test_tracesystem::events::action::isready::actionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Action::isReady::actionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::offer::hastokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Offer::hasTokensEntryEventOccurrence)


def test_tracesystem::events::offer::hastokensentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Offer::hasTokensEntryEventOccurrence.__init__)


def test_tracesystem::events::offer::hastokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Offer::hasTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::getinitialnodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence)


def test_tracesystem::events::activity::getinitialnodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::getinitialnodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::controlnode::fire::controlnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence)


def test_tracesystem::events::controlnode::fire::controlnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence.__init__)


def test_tracesystem::events::controlnode::fire::controlnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::run::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence)


def test_tracesystem::events::activitynode::run::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::run::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::removetokenentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence)


def test_tracesystem::events::activitynode::removetokenentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::removetokenentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::isreadyexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::isReadyExitEventOccurrence)


def test_tracesystem::events::activitynode::isreadyexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::isReadyExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::isreadyexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::isReadyExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::getenablednodesexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence)


def test_tracesystem::events::activity::getenablednodesexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence.__init__)


def test_tracesystem::events::activity::getenablednodesexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::sendoffersexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence)


def test_tracesystem::events::activitynode::sendoffersexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::sendoffersexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::sendofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence)


def test_tracesystem::events::activityedge::sendofferentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence.__init__)


def test_tracesystem::events::activityedge::sendofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::sendofferexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence)


def test_tracesystem::events::activityedge::sendofferexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence.__init__)


def test_tracesystem::events::activityedge::sendofferexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::selectnextnodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::selectNextNodeExitEventOccurrence)


def test_tracesystem::events::activity::selectnextnodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::selectNextNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activity::selectnextnodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::selectNextNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::addtokensentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence)


def test_tracesystem::events::activitynode::addtokensentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::addtokensentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)


def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)


def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::terminate::activitynodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence)


def test_tracesystem::events::activitynode::terminate::activitynodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::terminate::activitynodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::addtokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::addTokensExitEventOccurrence)


def test_tracesystem::events::activitynode::addtokensexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::addTokensExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::addtokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::addTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::run::activitynodeexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence)


def test_tracesystem::events::activitynode::run::activitynodeexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence.__init__)


def test_tracesystem::events::activitynode::run::activitynodeexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::mergenode::hasoffers::mergenodeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence)


def test_tracesystem::events::mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)


def test_tracesystem::events::mergenode::hasoffers::mergenodeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::offer::hastokensexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Offer::hasTokensExitEventOccurrence)


def test_tracesystem::events::offer::hastokensexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Offer::hasTokensExitEventOccurrence.__init__)


def test_tracesystem::events::offer::hastokensexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Offer::hasTokensExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanunaryexpression::evaluatenotentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)


def test_tracesystem::events::booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanunaryexpression::evaluatenotentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::hasofferentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence)


def test_tracesystem::events::activityedge::hasofferentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence.__init__)


def test_tracesystem::events::activityedge::hasofferentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)


def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)


def test_tracesystem::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)


def test_tracesystem::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::token::iswithdrawnexiteventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Token::isWithdrawnExitEventOccurrence)


def test_tracesystem::events::token::iswithdrawnexiteventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Token::isWithdrawnExitEventOccurrence.__init__)


def test_tracesystem::events::token::iswithdrawnexiteventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Token::isWithdrawnExitEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activitynode::sendoffersentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence)


def test_tracesystem::events::activitynode::sendoffersentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence.__init__)


def test_tracesystem::events::activitynode::sendoffersentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)


def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)


def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)


def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activity::initializeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::Activity::initializeEntryEventOccurrence)


def test_tracesystem::events::activity::initializeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::Activity::initializeEntryEventOccurrence.__init__)


def test_tracesystem::events::activity::initializeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::Activity::initializeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)


def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)


def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_is_not_abstract():
    assert not inspect.isabstract(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)


def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_exists():
    assert callable(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)


def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_constructor_args():
    sig = inspect.signature(traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence.__init__)
    params = list(sig.parameters.keys())



def test_tracesystem::staticobjectspools_is_not_abstract():
    assert not inspect.isabstract(traceSystem::StaticObjectsPools)


def test_tracesystem::staticobjectspools_constructor_exists():
    assert callable(traceSystem::StaticObjectsPools.__init__)


def test_tracesystem::staticobjectspools_constructor_args():
    sig = inspect.signature(traceSystem::StaticObjectsPools.__init__)
    params = list(sig.parameters.keys())



def test_tracedobjects_is_not_abstract():
    assert not inspect.isabstract(TracedObjects)


def test_tracedobjects_constructor_exists():
    assert callable(TracedObjects.__init__)


def test_tracedobjects_constructor_args():
    sig = inspect.signature(TracedObjects.__init__)
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
IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
)
IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
)
IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
)
BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
)
BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
)
IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
)
IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateADDExitEventOccurrence,
)
IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy = st.builds(
    IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
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
IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
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
StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
)
StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
)
StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy = st.builds(
    StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
)
StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
)
IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
)
IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
)
IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy = st.builds(
    IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
)
IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
)
IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
)
DecisionNode::fire::decisionNodeExitEventOccurrence_strategy = st.builds(
    DecisionNode::fire::decisionNodeExitEventOccurrence,
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
ForkNode::fire::forkNodeEntryEventOccurrence_strategy = st.builds(
    ForkNode::fire::forkNodeEntryEventOccurrence,
)
ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy = st.builds(
    ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
)
ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
)
InitialNode::fire::initialNodeExitEventOccurrence_strategy = st.builds(
    InitialNode::fire::initialNodeExitEventOccurrence,
)
InitialNode::fire::initialNodeEntryEventOccurrence_strategy = st.builds(
    InitialNode::fire::initialNodeEntryEventOccurrence,
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
Action::sendOffers::actionExitEventOccurrence_strategy = st.builds(
    Action::sendOffers::actionExitEventOccurrence,
)
Action::sendOffers::actionEntryEventOccurrence_strategy = st.builds(
    Action::sendOffers::actionEntryEventOccurrence,
)
ControlNode::fire::controlNodeExitEventOccurrence_strategy = st.builds(
    ControlNode::fire::controlNodeExitEventOccurrence,
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
activitydiagram::traceSystem::JoinNode_strategy = st.builds(
    activitydiagram::traceSystem::JoinNode,
)
activitydiagram::traceSystem::InitialNode_strategy = st.builds(
    activitydiagram::traceSystem::InitialNode,
)
traceSystem::activitydiagram::TracedNamedElement_strategy = st.builds(
    traceSystem::activitydiagram::TracedNamedElement,
    name=
        safe_text
)
activitydiagram::traceSystem::IntegerVariable_strategy = st.builds(
    activitydiagram::traceSystem::IntegerVariable,
)
activitydiagram::traceSystem::DecisionNode_strategy = st.builds(
    activitydiagram::traceSystem::DecisionNode,
)
activitydiagram::traceSystem::MergeNode_strategy = st.builds(
    activitydiagram::traceSystem::MergeNode,
)
activitydiagram::traceSystem::Value_strategy = st.builds(
    activitydiagram::traceSystem::Value,
)
activitydiagram::traceSystem::Activity_strategy = st.builds(
    activitydiagram::traceSystem::Activity,
)
activitydiagram::traceSystem::ControlFlow_strategy = st.builds(
    activitydiagram::traceSystem::ControlFlow,
)
TracedActivityEdge_strategy = st.builds(
    TracedActivityEdge,
)
traceSystem::activitydiagram::TracedControlFlow_strategy = st.builds(
    traceSystem::activitydiagram::TracedControlFlow,
)
activitydiagram::traceSystem::ForkNode_strategy = st.builds(
    activitydiagram::traceSystem::ForkNode,
)
TracedControlNode_strategy = st.builds(
    TracedControlNode,
)
traceSystem::activitydiagram::TracedDecisionNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedDecisionNode,
)
traceSystem::activitydiagram::TracedJoinNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedJoinNode,
)
traceSystem::activitydiagram::TracedMergeNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedMergeNode,
)
traceSystem::activitydiagram::TracedInitialNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedInitialNode,
)
traceSystem::activitydiagram::TracedForkNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedForkNode,
)
activitydiagram::traceSystem::BooleanVariable_strategy = st.builds(
    activitydiagram::traceSystem::BooleanVariable,
)
TracedNamedElement_strategy = st.builds(
    TracedNamedElement,
)
traceSystem::activitydiagram::TracedVariable_strategy = st.builds(
    traceSystem::activitydiagram::TracedVariable,
)
traceSystem::activitydiagram::TracedActivityNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedActivityNode,
)
traceSystem::activitydiagram::TracedActivityEdge_strategy = st.builds(
    traceSystem::activitydiagram::TracedActivityEdge,
)
traceSystem::activitydiagram::TracedActivity_strategy = st.builds(
    traceSystem::activitydiagram::TracedActivity,
)
TracedActivityNode_strategy = st.builds(
    TracedActivityNode,
)
traceSystem::activitydiagram::TracedControlNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedControlNode,
)
traceSystem::activitydiagram::TracedExecutableNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedExecutableNode,
)
activitydiagram::traceSystem::OpaqueAction_strategy = st.builds(
    activitydiagram::traceSystem::OpaqueAction,
)
activitydiagram::traceSystem::Expression_strategy = st.builds(
    activitydiagram::traceSystem::Expression,
)
TracedAction_strategy = st.builds(
    TracedAction,
)
traceSystem::activitydiagram::TracedOpaqueAction_strategy = st.builds(
    traceSystem::activitydiagram::TracedOpaqueAction,
)
activitydiagram::traceSystem::StringVariable_strategy = st.builds(
    activitydiagram::traceSystem::StringVariable,
)
traceSystem::activitydiagram::TracedFinalNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedFinalNode,
)
TracedExecutableNode_strategy = st.builds(
    TracedExecutableNode,
)
traceSystem::activitydiagram::TracedAction_strategy = st.builds(
    traceSystem::activitydiagram::TracedAction,
)
activitydiagram::traceSystem::ActivityFinalNode_strategy = st.builds(
    activitydiagram::traceSystem::ActivityFinalNode,
)
TracedFinalNode_strategy = st.builds(
    TracedFinalNode,
)
traceSystem::activitydiagram::TracedActivityFinalNode_strategy = st.builds(
    traceSystem::activitydiagram::TracedActivityFinalNode,
)
TracedVariable_strategy = st.builds(
    TracedVariable,
)
traceSystem::activitydiagram::TracedIntegerVariable_strategy = st.builds(
    traceSystem::activitydiagram::TracedIntegerVariable,
)
traceSystem::activitydiagram::TracedStringVariable_strategy = st.builds(
    traceSystem::activitydiagram::TracedStringVariable,
)
traceSystem::activitydiagram::TracedBooleanVariable_strategy = st.builds(
    traceSystem::activitydiagram::TracedBooleanVariable,
)
traceSystem::activitydiagramConfiguration::TracedInput_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedInput,
)
traceSystem::activitydiagramConfiguration::TracedTrace_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedTrace,
)
traceSystem::activitydiagramConfiguration::TracedInputValue_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedInputValue,
)
traceSystem::activitydiagramConfiguration::TracedOffer_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedOffer,
)
traceSystem::activitydiagramConfiguration::TracedToken_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedToken,
)
TracedToken_strategy = st.builds(
    TracedToken,
)
traceSystem::activitydiagramConfiguration::TracedControlToken_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedControlToken,
)
traceSystem::activitydiagramConfiguration::TracedForkedToken_strategy = st.builds(
    traceSystem::activitydiagramConfiguration::TracedForkedToken,
)
traceSystem::Traced::TracedObjects_strategy = st.builds(
    traceSystem::Traced::TracedObjects,
)
activitydiagram::TracedJoinNode_strategy = st.builds(
    activitydiagram::TracedJoinNode,
)
activitydiagramConfiguration::TracedControlToken_strategy = st.builds(
    activitydiagramConfiguration::TracedControlToken,
)
activitydiagram::TracedControlFlow_strategy = st.builds(
    activitydiagram::TracedControlFlow,
)
traceSystem::States::ActivityEdge::offers::State_strategy = st.builds(
    traceSystem::States::ActivityEdge::offers::State,
)
traceSystem::States::ActivityNode::running::State_strategy = st.builds(
    traceSystem::States::ActivityNode::running::State,
    running=
        st.booleans()
)
traceSystem::States::ActivityNode::heldTokens::State_strategy = st.builds(
    traceSystem::States::ActivityNode::heldTokens::State,
)
activitydiagramConfiguration::TracedInput_strategy = st.builds(
    activitydiagramConfiguration::TracedInput,
)
traceSystem::States::Input::inputValues::State_strategy = st.builds(
    traceSystem::States::Input::inputValues::State,
)
traceSystem::States::Trace::executedNodes::State_strategy = st.builds(
    traceSystem::States::Trace::executedNodes::State,
)
traceSystem::States::Offer::offeredTokens::State_strategy = st.builds(
    traceSystem::States::Offer::offeredTokens::State,
)
traceSystem::States::InputValue::variable::State_strategy = st.builds(
    traceSystem::States::InputValue::variable::State,
)
activitydiagramConfiguration::TracedInputValue_strategy = st.builds(
    activitydiagramConfiguration::TracedInputValue,
)
traceSystem::States::InputValue::value::State_strategy = st.builds(
    traceSystem::States::InputValue::value::State,
)
activitydiagram::TracedVariable_strategy = st.builds(
    activitydiagram::TracedVariable,
)
States::traceSystem::Value_strategy = st.builds(
    States::traceSystem::Value,
)
traceSystem::States::Variable::currentValue::State_strategy = st.builds(
    traceSystem::States::Variable::currentValue::State,
)
activitydiagramConfiguration::TracedTrace_strategy = st.builds(
    activitydiagramConfiguration::TracedTrace,
)
traceSystem::States::Activity::trace::State_strategy = st.builds(
    traceSystem::States::Activity::trace::State,
)
activitydiagramConfiguration::TracedForkedToken_strategy = st.builds(
    activitydiagramConfiguration::TracedForkedToken,
)
traceSystem::States::Token::holder::State_strategy = st.builds(
    traceSystem::States::Token::holder::State,
)
traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State_strategy = st.builds(
    traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State,
    baseTokenIsWithdrawn=
        st.booleans()
)
traceSystem::States::ForkedToken::remainingOffersCount::State_strategy = st.builds(
    traceSystem::States::ForkedToken::remainingOffersCount::State,
    remainingOffersCount=
        st.integers()
)
States::traceSystem::GlobalState_strategy = st.builds(
    States::traceSystem::GlobalState,
)
traceSystem::States::ForkedToken::baseToken::State_strategy = st.builds(
    traceSystem::States::ForkedToken::baseToken::State,
)
activitydiagramConfiguration::TracedOffer_strategy = st.builds(
    activitydiagramConfiguration::TracedOffer,
)
Events::traceSystem::BooleanBinaryExpression_strategy = st.builds(
    Events::traceSystem::BooleanBinaryExpression,
)
Events::traceSystem::BooleanUnaryExpression_strategy = st.builds(
    Events::traceSystem::BooleanUnaryExpression,
)
Events::traceSystem::IntegerComparisonExpression_strategy = st.builds(
    Events::traceSystem::IntegerComparisonExpression,
)
Events::traceSystem::IntegerCalculationExpression_strategy = st.builds(
    Events::traceSystem::IntegerCalculationExpression,
)
Events::traceSystem::IntegerExpression_strategy = st.builds(
    Events::traceSystem::IntegerExpression,
)
activitydiagram::TracedDecisionNode_strategy = st.builds(
    activitydiagram::TracedDecisionNode,
)
activitydiagram::TracedBooleanVariable_strategy = st.builds(
    activitydiagram::TracedBooleanVariable,
)
activitydiagram::TracedStringVariable_strategy = st.builds(
    activitydiagram::TracedStringVariable,
)
Events::traceSystem::Value_strategy = st.builds(
    Events::traceSystem::Value,
)
activitydiagram::TracedIntegerVariable_strategy = st.builds(
    activitydiagram::TracedIntegerVariable,
)
activitydiagram::TracedInitialNode_strategy = st.builds(
    activitydiagram::TracedInitialNode,
)
activitydiagram::TracedMergeNode_strategy = st.builds(
    activitydiagram::TracedMergeNode,
)
activitydiagram::TracedOpaqueAction_strategy = st.builds(
    activitydiagram::TracedOpaqueAction,
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
Events::traceSystem::EObject_strategy = st.builds(
    Events::traceSystem::EObject,
)
activitydiagram::TracedActivity_strategy = st.builds(
    activitydiagram::TracedActivity,
)
Offer::hasTokensExitEventOccurrence_strategy = st.builds(
    Offer::hasTokensExitEventOccurrence,
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
BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy = st.builds(
    BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
)
Token::transferEntryEventOccurrence_strategy = st.builds(
    Token::transferEntryEventOccurrence,
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
IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
)
IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy = st.builds(
    IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
)
Action::fire::actionExitEventOccurrence_strategy = st.builds(
    Action::fire::actionExitEventOccurrence,
)
Action::fire::actionEntryEventOccurrence_strategy = st.builds(
    Action::fire::actionEntryEventOccurrence,
)
Action::isReady::actionExitEventOccurrence_strategy = st.builds(
    Action::isReady::actionExitEventOccurrence,
)
Action::isReady::actionEntryEventOccurrence_strategy = st.builds(
    Action::isReady::actionEntryEventOccurrence,
)
ActivityNode::hasOffersExitEventOccurrence_strategy = st.builds(
    ActivityNode::hasOffersExitEventOccurrence,
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
ActivityEdge::sendOfferExitEventOccurrence_strategy = st.builds(
    ActivityEdge::sendOfferExitEventOccurrence,
)
ActivityEdge::sendOfferEntryEventOccurrence_strategy = st.builds(
    ActivityEdge::sendOfferEntryEventOccurrence,
)
ActivityNode::isReadyExitEventOccurrence_strategy = st.builds(
    ActivityNode::isReadyExitEventOccurrence,
)
ActivityNode::isReadyEntryEventOccurrence_strategy = st.builds(
    ActivityNode::isReadyEntryEventOccurrence,
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
Activity::getEnabledNodesExitEventOccurrence_strategy = st.builds(
    Activity::getEnabledNodesExitEventOccurrence,
)
Activity::getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    Activity::getEnabledNodesEntryEventOccurrence,
)
Activity::fireInitialNodeExitEventOccurrence_strategy = st.builds(
    Activity::fireInitialNodeExitEventOccurrence,
)
Activity::fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    Activity::fireInitialNodeEntryEventOccurrence,
)
ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode::terminate::activityNodeEntryEventOccurrence,
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
ActivityNode::run::activityNodeEntryEventOccurrence_strategy = st.builds(
    ActivityNode::run::activityNodeEntryEventOccurrence,
)
Activity::fireNodeExitEventOccurrence_strategy = st.builds(
    Activity::fireNodeExitEventOccurrence,
)
Activity::initializeEntryEventOccurrence_strategy = st.builds(
    Activity::initializeEntryEventOccurrence,
)
Activity::mainExitEventOccurrence_strategy = st.builds(
    Activity::mainExitEventOccurrence,
)
Activity::mainEntryEventOccurrence_strategy = st.builds(
    Activity::mainEntryEventOccurrence,
)
traceSystem::Events::Events_strategy = st.builds(
    traceSystem::Events::Events,
)
Events::traceSystem::GlobalState_strategy = st.builds(
    Events::traceSystem::GlobalState,
)
traceSystem::Events::EventOccurrence_strategy = st.builds(
    traceSystem::Events::EventOccurrence,
)
traceSystem::IntegerCalculationExpression_strategy = st.builds(
    traceSystem::IntegerCalculationExpression,
)
traceSystem::IntegerValue_strategy = st.builds(
    traceSystem::IntegerValue,
)
traceSystem::BooleanUnaryExpression_strategy = st.builds(
    traceSystem::BooleanUnaryExpression,
)
traceSystem::BooleanBinaryExpression_strategy = st.builds(
    traceSystem::BooleanBinaryExpression,
)
traceSystem::StringValue_strategy = st.builds(
    traceSystem::StringValue,
)
traceSystem::IntegerComparisonExpression_strategy = st.builds(
    traceSystem::IntegerComparisonExpression,
)
traceSystem::BooleanValue_strategy = st.builds(
    traceSystem::BooleanValue,
)
ActivityNode::running::State_strategy = st.builds(
    ActivityNode::running::State,
)
ActivityNode::heldTokens::State_strategy = st.builds(
    ActivityNode::heldTokens::State,
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
InputValue::value::State_strategy = st.builds(
    InputValue::value::State,
)
Variable::currentValue::State_strategy = st.builds(
    Variable::currentValue::State,
)
Activity::trace::State_strategy = st.builds(
    Activity::trace::State,
)
Offer::offeredTokens::State_strategy = st.builds(
    Offer::offeredTokens::State,
)
Token::holder::State_strategy = st.builds(
    Token::holder::State,
)
ForkedToken::baseTokenIsWithdrawn::State_strategy = st.builds(
    ForkedToken::baseTokenIsWithdrawn::State,
)
ForkedToken::remainingOffersCount::State_strategy = st.builds(
    ForkedToken::remainingOffersCount::State,
)
Input::inputValues::State_strategy = st.builds(
    Input::inputValues::State,
)
Trace::executedNodes::State_strategy = st.builds(
    Trace::executedNodes::State,
)
ActivityEdge::offers::State_strategy = st.builds(
    ActivityEdge::offers::State,
)
InputValue::variable::State_strategy = st.builds(
    InputValue::variable::State,
)
Events_strategy = st.builds(
    Events,
)
traceSystem::GlobalState_strategy = st.builds(
    traceSystem::GlobalState,
)
traceSystem::Trace_strategy = st.builds(
    traceSystem::Trace,
)
ForkedToken::baseToken::State_strategy = st.builds(
    ForkedToken::baseToken::State,
)
EventOccurrence_strategy = st.builds(
    EventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence,
)
traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence,
)
traceSystem::Events::Action::fire::actionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::fire::actionEntryEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence,
)
traceSystem::Events::Action::sendOffers::actionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::sendOffers::actionExitEventOccurrence,
)
traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence,
)
traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence,
)
traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence,
)
traceSystem::Events::Activity::mainEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::mainEntryEventOccurrence,
)
traceSystem::Events::Activity::fireNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::fireNodeExitEventOccurrence,
)
traceSystem::Events::Activity::fireNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::fireNodeEntryEventOccurrence,
)
traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence,
)
traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence,
)
traceSystem::Events::Token::isWithdrawnEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::isWithdrawnEntryEventOccurrence,
)
traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence,
)
traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence,
)
traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence,
)
traceSystem::Events::Activity::initializeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::initializeExitEventOccurrence,
)
traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence,
)
traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence,
)
traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence,
)
traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence,
)
traceSystem::Events::Activity::runExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::runExitEventOccurrence,
)
traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence,
)
traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence,
)
traceSystem::Events::Action::isReady::actionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::isReady::actionExitEventOccurrence,
)
traceSystem::Events::Token::withdrawEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::withdrawEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence,
)
traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence,
)
traceSystem::Events::ActivityNode::isRunningExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::isRunningExitEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence,
)
traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence,
)
traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence,
)
traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence,
)
traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence,
)
traceSystem::Events::Action::fire::actionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::fire::actionExitEventOccurrence,
)
traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence,
)
traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence,
)
traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence,
)
traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence,
)
traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence,
)
traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence,
)
traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence,
)
traceSystem::Events::Activity::runEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::runEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence,
)
traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence,
)
traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence,
)
traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence,
)
traceSystem::Events::Activity::terminateEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::terminateEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence,
)
traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence,
)
traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence,
)
traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence,
)
traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence,
)
traceSystem::Events::Activity::terminateExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::terminateExitEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence,
)
traceSystem::Events::Activity::runNodesEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::runNodesEntryEventOccurrence,
)
traceSystem::Events::Token::transferEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::transferEntryEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence,
)
traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence,
)
traceSystem::Events::Activity::mainExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::mainExitEventOccurrence,
)
traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence,
)
traceSystem::Events::Activity::getInitialNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::getInitialNodeExitEventOccurrence,
)
traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence,
)
traceSystem::Events::Activity::runNodesExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::runNodesExitEventOccurrence,
)
traceSystem::Events::Token::withdrawExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::withdrawExitEventOccurrence,
)
traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence,
)
traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence,
)
traceSystem::Events::Token::transferExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::transferExitEventOccurrence,
)
traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence,
)
traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence,
)
traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence,
)
traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence,
)
traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence,
)
traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence,
)
traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence,
)
traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence,
)
traceSystem::Events::Action::isReady::actionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Action::isReady::actionEntryEventOccurrence,
)
traceSystem::Events::Offer::hasTokensEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Offer::hasTokensEntryEventOccurrence,
)
traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence,
)
traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence,
)
traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence,
)
traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence,
)
traceSystem::Events::ActivityNode::isReadyExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::isReadyExitEventOccurrence,
)
traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence,
)
traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence,
)
traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence,
)
traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence,
)
traceSystem::Events::Activity::selectNextNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::selectNextNodeExitEventOccurrence,
)
traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence,
)
traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence,
)
traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence,
)
traceSystem::Events::ActivityNode::addTokensExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::addTokensExitEventOccurrence,
)
traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence,
)
traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence,
)
traceSystem::Events::Offer::hasTokensExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Offer::hasTokensExitEventOccurrence,
)
traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence,
)
traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence,
)
traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence,
)
traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence,
)
traceSystem::Events::Token::isWithdrawnExitEventOccurrence_strategy = st.builds(
    traceSystem::Events::Token::isWithdrawnExitEventOccurrence,
)
traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence,
)
traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence,
)
traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence,
)
traceSystem::Events::Activity::initializeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::Activity::initializeEntryEventOccurrence,
)
traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence,
)
traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy = st.builds(
    traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence,
)
traceSystem::StaticObjectsPools_strategy = st.builds(
    traceSystem::StaticObjectsPools,
)
TracedObjects_strategy = st.builds(
    TracedObjects,
)

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

@given(instance=IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)

@given(instance=BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)

@given(instance=BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateADDExitEventOccurrence)

@given(instance=IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercalculationexpression::evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerCalculationExpression::evaluateADDEntryEventOccurrence)

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

@given(instance=IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)

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

@given(instance=StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)

@given(instance=IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)

@given(instance=IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)

@given(instance=IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::setcurrentvalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)

@given(instance=IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integervariable::setcurrentvalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)

@given(instance=IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integerexpression::getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)

@given(instance=DecisionNode::fire::decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_decisionnode::fire::decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, DecisionNode::fire::decisionNodeExitEventOccurrence)

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

@given(instance=InitialNode::fire::initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::fire::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::fire::initialNodeExitEventOccurrence)

@given(instance=InitialNode::fire::initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_initialnode::fire::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, InitialNode::fire::initialNodeEntryEventOccurrence)

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

@given(instance=activitydiagram::traceSystem::JoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::joinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::JoinNode)

@given(instance=activitydiagram::traceSystem::InitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::initialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::InitialNode)

@given(instance=traceSystem::activitydiagram::TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracednamedelement_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedNamedElement)

@given(instance=traceSystem::activitydiagram::TracedNamedElement_strategy)
def test_tracesystem::activitydiagram::tracednamedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=traceSystem::activitydiagram::TracedNamedElement_strategy)
def test_tracesystem::activitydiagram::tracednamedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=activitydiagram::traceSystem::IntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::integervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::IntegerVariable)

@given(instance=activitydiagram::traceSystem::DecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::decisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::DecisionNode)

@given(instance=activitydiagram::traceSystem::MergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::mergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::MergeNode)

@given(instance=activitydiagram::traceSystem::Value_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::value_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::Value)

@given(instance=activitydiagram::traceSystem::Activity_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::activity_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::Activity)

@given(instance=activitydiagram::traceSystem::ControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::controlflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::ControlFlow)

@given(instance=TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracedactivityedge_instantiation(instance):
    assert isinstance(instance, TracedActivityEdge)

@given(instance=traceSystem::activitydiagram::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedControlFlow)

@given(instance=activitydiagram::traceSystem::ForkNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::forknode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::ForkNode)

@given(instance=TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, TracedControlNode)

@given(instance=traceSystem::activitydiagram::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedDecisionNode)

@given(instance=traceSystem::activitydiagram::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedJoinNode)

@given(instance=traceSystem::activitydiagram::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedmergenode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedMergeNode)

@given(instance=traceSystem::activitydiagram::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedInitialNode)

@given(instance=traceSystem::activitydiagram::TracedForkNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedforknode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedForkNode)

@given(instance=activitydiagram::traceSystem::BooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::booleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::BooleanVariable)

@given(instance=TracedNamedElement_strategy)
@settings(max_examples=50)
def test_tracednamedelement_instantiation(instance):
    assert isinstance(instance, TracedNamedElement)

@given(instance=traceSystem::activitydiagram::TracedVariable_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedvariable_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedVariable)

@given(instance=traceSystem::activitydiagram::TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedactivitynode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedActivityNode)

@given(instance=traceSystem::activitydiagram::TracedActivityEdge_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedactivityedge_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedActivityEdge)

@given(instance=traceSystem::activitydiagram::TracedActivity_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedactivity_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedActivity)

@given(instance=TracedActivityNode_strategy)
@settings(max_examples=50)
def test_tracedactivitynode_instantiation(instance):
    assert isinstance(instance, TracedActivityNode)

@given(instance=traceSystem::activitydiagram::TracedControlNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedcontrolnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedControlNode)

@given(instance=traceSystem::activitydiagram::TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedExecutableNode)

@given(instance=activitydiagram::traceSystem::OpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::opaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::OpaqueAction)

@given(instance=activitydiagram::traceSystem::Expression_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::expression_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::Expression)

@given(instance=TracedAction_strategy)
@settings(max_examples=50)
def test_tracedaction_instantiation(instance):
    assert isinstance(instance, TracedAction)

@given(instance=traceSystem::activitydiagram::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedOpaqueAction)

@given(instance=activitydiagram::traceSystem::StringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::stringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::StringVariable)

@given(instance=traceSystem::activitydiagram::TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedfinalnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedFinalNode)

@given(instance=TracedExecutableNode_strategy)
@settings(max_examples=50)
def test_tracedexecutablenode_instantiation(instance):
    assert isinstance(instance, TracedExecutableNode)

@given(instance=traceSystem::activitydiagram::TracedAction_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedaction_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedAction)

@given(instance=activitydiagram::traceSystem::ActivityFinalNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracesystem::activityfinalnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::traceSystem::ActivityFinalNode)

@given(instance=TracedFinalNode_strategy)
@settings(max_examples=50)
def test_tracedfinalnode_instantiation(instance):
    assert isinstance(instance, TracedFinalNode)

@given(instance=traceSystem::activitydiagram::TracedActivityFinalNode_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedactivityfinalnode_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedActivityFinalNode)

@given(instance=TracedVariable_strategy)
@settings(max_examples=50)
def test_tracedvariable_instantiation(instance):
    assert isinstance(instance, TracedVariable)

@given(instance=traceSystem::activitydiagram::TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedintegervariable_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedIntegerVariable)

@given(instance=traceSystem::activitydiagram::TracedStringVariable_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedstringvariable_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedStringVariable)

@given(instance=traceSystem::activitydiagram::TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagram::tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagram::TracedBooleanVariable)

@given(instance=traceSystem::activitydiagramConfiguration::TracedInput_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedinput_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedInput)

@given(instance=traceSystem::activitydiagramConfiguration::TracedTrace_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedtrace_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedTrace)

@given(instance=traceSystem::activitydiagramConfiguration::TracedInputValue_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedinputvalue_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedInputValue)

@given(instance=traceSystem::activitydiagramConfiguration::TracedOffer_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedoffer_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedOffer)

@given(instance=traceSystem::activitydiagramConfiguration::TracedToken_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedtoken_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedToken)

@given(instance=TracedToken_strategy)
@settings(max_examples=50)
def test_tracedtoken_instantiation(instance):
    assert isinstance(instance, TracedToken)

@given(instance=traceSystem::activitydiagramConfiguration::TracedControlToken_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedControlToken)

@given(instance=traceSystem::activitydiagramConfiguration::TracedForkedToken_strategy)
@settings(max_examples=50)
def test_tracesystem::activitydiagramconfiguration::tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, traceSystem::activitydiagramConfiguration::TracedForkedToken)

@given(instance=traceSystem::Traced::TracedObjects_strategy)
@settings(max_examples=50)
def test_tracesystem::traced::tracedobjects_instantiation(instance):
    assert isinstance(instance, traceSystem::Traced::TracedObjects)

@given(instance=activitydiagram::TracedJoinNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedjoinnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedJoinNode)

@given(instance=activitydiagramConfiguration::TracedControlToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedcontroltoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedControlToken)

@given(instance=activitydiagram::TracedControlFlow_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedcontrolflow_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedControlFlow)

@given(instance=traceSystem::States::ActivityEdge::offers::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::activityedge::offers::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ActivityEdge::offers::State)

@given(instance=traceSystem::States::ActivityNode::running::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::activitynode::running::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ActivityNode::running::State)

@given(instance=traceSystem::States::ActivityNode::running::State_strategy)
def test_tracesystem::states::activitynode::running::state_running_type(instance):
    assert isinstance(instance.running, bool)


@given(instance=traceSystem::States::ActivityNode::running::State_strategy)
def test_tracesystem::states::activitynode::running::state_running_setter(instance):
    original = instance.running
    instance.running = original
    assert instance.running == original

@given(instance=traceSystem::States::ActivityNode::heldTokens::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::activitynode::heldtokens::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ActivityNode::heldTokens::State)

@given(instance=activitydiagramConfiguration::TracedInput_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedinput_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedInput)

@given(instance=traceSystem::States::Input::inputValues::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::input::inputvalues::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Input::inputValues::State)

@given(instance=traceSystem::States::Trace::executedNodes::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::trace::executednodes::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Trace::executedNodes::State)

@given(instance=traceSystem::States::Offer::offeredTokens::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::offer::offeredtokens::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Offer::offeredTokens::State)

@given(instance=traceSystem::States::InputValue::variable::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::inputvalue::variable::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::InputValue::variable::State)

@given(instance=activitydiagramConfiguration::TracedInputValue_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedinputvalue_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedInputValue)

@given(instance=traceSystem::States::InputValue::value::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::inputvalue::value::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::InputValue::value::State)

@given(instance=activitydiagram::TracedVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedVariable)

@given(instance=States::traceSystem::Value_strategy)
@settings(max_examples=50)
def test_states::tracesystem::value_instantiation(instance):
    assert isinstance(instance, States::traceSystem::Value)

@given(instance=traceSystem::States::Variable::currentValue::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::variable::currentvalue::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Variable::currentValue::State)

@given(instance=activitydiagramConfiguration::TracedTrace_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedtrace_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedTrace)

@given(instance=traceSystem::States::Activity::trace::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::activity::trace::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Activity::trace::State)

@given(instance=activitydiagramConfiguration::TracedForkedToken_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedforkedtoken_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedForkedToken)

@given(instance=traceSystem::States::Token::holder::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::token::holder::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::Token::holder::State)

@given(instance=traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State)

@given(instance=traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_baseTokenIsWithdrawn_type(instance):
    assert isinstance(instance.baseTokenIsWithdrawn, bool)


@given(instance=traceSystem::States::ForkedToken::baseTokenIsWithdrawn::State_strategy)
def test_tracesystem::states::forkedtoken::basetokeniswithdrawn::state_baseTokenIsWithdrawn_setter(instance):
    original = instance.baseTokenIsWithdrawn
    instance.baseTokenIsWithdrawn = original
    assert instance.baseTokenIsWithdrawn == original

@given(instance=traceSystem::States::ForkedToken::remainingOffersCount::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::forkedtoken::remainingofferscount::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ForkedToken::remainingOffersCount::State)

@given(instance=traceSystem::States::ForkedToken::remainingOffersCount::State_strategy)
def test_tracesystem::states::forkedtoken::remainingofferscount::state_remainingOffersCount_type(instance):
    assert isinstance(instance.remainingOffersCount, int)


@given(instance=traceSystem::States::ForkedToken::remainingOffersCount::State_strategy)
def test_tracesystem::states::forkedtoken::remainingofferscount::state_remainingOffersCount_setter(instance):
    original = instance.remainingOffersCount
    instance.remainingOffersCount = original
    assert instance.remainingOffersCount == original

@given(instance=States::traceSystem::GlobalState_strategy)
@settings(max_examples=50)
def test_states::tracesystem::globalstate_instantiation(instance):
    assert isinstance(instance, States::traceSystem::GlobalState)

@given(instance=traceSystem::States::ForkedToken::baseToken::State_strategy)
@settings(max_examples=50)
def test_tracesystem::states::forkedtoken::basetoken::state_instantiation(instance):
    assert isinstance(instance, traceSystem::States::ForkedToken::baseToken::State)

@given(instance=activitydiagramConfiguration::TracedOffer_strategy)
@settings(max_examples=50)
def test_activitydiagramconfiguration::tracedoffer_instantiation(instance):
    assert isinstance(instance, activitydiagramConfiguration::TracedOffer)

@given(instance=Events::traceSystem::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_events::tracesystem::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::BooleanBinaryExpression)

@given(instance=Events::traceSystem::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_events::tracesystem::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::BooleanUnaryExpression)

@given(instance=Events::traceSystem::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_events::tracesystem::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::IntegerComparisonExpression)

@given(instance=Events::traceSystem::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_events::tracesystem::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::IntegerCalculationExpression)

@given(instance=Events::traceSystem::IntegerExpression_strategy)
@settings(max_examples=50)
def test_events::tracesystem::integerexpression_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::IntegerExpression)

@given(instance=activitydiagram::TracedDecisionNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::traceddecisionnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedDecisionNode)

@given(instance=activitydiagram::TracedBooleanVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedbooleanvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedBooleanVariable)

@given(instance=activitydiagram::TracedStringVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedstringvariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedStringVariable)

@given(instance=Events::traceSystem::Value_strategy)
@settings(max_examples=50)
def test_events::tracesystem::value_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::Value)

@given(instance=activitydiagram::TracedIntegerVariable_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedintegervariable_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedIntegerVariable)

@given(instance=activitydiagram::TracedInitialNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedinitialnode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedInitialNode)

@given(instance=activitydiagram::TracedMergeNode_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedmergenode_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedMergeNode)

@given(instance=activitydiagram::TracedOpaqueAction_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedopaqueaction_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedOpaqueAction)

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

@given(instance=Events::traceSystem::EObject_strategy)
@settings(max_examples=50)
def test_events::tracesystem::eobject_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::EObject)

@given(instance=activitydiagram::TracedActivity_strategy)
@settings(max_examples=50)
def test_activitydiagram::tracedactivity_instantiation(instance):
    assert isinstance(instance, activitydiagram::TracedActivity)

@given(instance=Offer::hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_offer::hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Offer::hasTokensExitEventOccurrence)

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

@given(instance=BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_booleanunaryexpression::evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)

@given(instance=Token::transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_token::transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Token::transferEntryEventOccurrence)

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

@given(instance=IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)

@given(instance=IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)

@given(instance=Action::fire::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::fire::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::fire::actionExitEventOccurrence)

@given(instance=Action::fire::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::fire::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::fire::actionEntryEventOccurrence)

@given(instance=Action::isReady::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::isready::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::isReady::actionExitEventOccurrence)

@given(instance=Action::isReady::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_action::isready::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Action::isReady::actionEntryEventOccurrence)

@given(instance=ActivityNode::hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::hasOffersExitEventOccurrence)

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

@given(instance=ActivityEdge::sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::sendOfferExitEventOccurrence)

@given(instance=ActivityEdge::sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activityedge::sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityEdge::sendOfferEntryEventOccurrence)

@given(instance=ActivityNode::isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isReadyExitEventOccurrence)

@given(instance=ActivityNode::isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::isReadyEntryEventOccurrence)

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

@given(instance=Activity::fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireInitialNodeEntryEventOccurrence)

@given(instance=ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::terminate::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::terminate::activityNodeEntryEventOccurrence)

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

@given(instance=ActivityNode::run::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activitynode::run::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, ActivityNode::run::activityNodeEntryEventOccurrence)

@given(instance=Activity::fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::fireNodeExitEventOccurrence)

@given(instance=Activity::initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::initializeEntryEventOccurrence)

@given(instance=Activity::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::mainExitEventOccurrence)

@given(instance=Activity::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_activity::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, Activity::mainEntryEventOccurrence)

@given(instance=traceSystem::Events::Events_strategy)
@settings(max_examples=50)
def test_tracesystem::events::events_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Events)

@given(instance=Events::traceSystem::GlobalState_strategy)
@settings(max_examples=50)
def test_events::tracesystem::globalstate_instantiation(instance):
    assert isinstance(instance, Events::traceSystem::GlobalState)

@given(instance=traceSystem::Events::EventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::eventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::EventOccurrence)

@given(instance=traceSystem::IntegerCalculationExpression_strategy)
@settings(max_examples=50)
def test_tracesystem::integercalculationexpression_instantiation(instance):
    assert isinstance(instance, traceSystem::IntegerCalculationExpression)

@given(instance=traceSystem::IntegerValue_strategy)
@settings(max_examples=50)
def test_tracesystem::integervalue_instantiation(instance):
    assert isinstance(instance, traceSystem::IntegerValue)

@given(instance=traceSystem::BooleanUnaryExpression_strategy)
@settings(max_examples=50)
def test_tracesystem::booleanunaryexpression_instantiation(instance):
    assert isinstance(instance, traceSystem::BooleanUnaryExpression)

@given(instance=traceSystem::BooleanBinaryExpression_strategy)
@settings(max_examples=50)
def test_tracesystem::booleanbinaryexpression_instantiation(instance):
    assert isinstance(instance, traceSystem::BooleanBinaryExpression)

@given(instance=traceSystem::StringValue_strategy)
@settings(max_examples=50)
def test_tracesystem::stringvalue_instantiation(instance):
    assert isinstance(instance, traceSystem::StringValue)

@given(instance=traceSystem::IntegerComparisonExpression_strategy)
@settings(max_examples=50)
def test_tracesystem::integercomparisonexpression_instantiation(instance):
    assert isinstance(instance, traceSystem::IntegerComparisonExpression)

@given(instance=traceSystem::BooleanValue_strategy)
@settings(max_examples=50)
def test_tracesystem::booleanvalue_instantiation(instance):
    assert isinstance(instance, traceSystem::BooleanValue)

@given(instance=ActivityNode::running::State_strategy)
@settings(max_examples=50)
def test_activitynode::running::state_instantiation(instance):
    assert isinstance(instance, ActivityNode::running::State)

@given(instance=ActivityNode::heldTokens::State_strategy)
@settings(max_examples=50)
def test_activitynode::heldtokens::state_instantiation(instance):
    assert isinstance(instance, ActivityNode::heldTokens::State)

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

@given(instance=InputValue::value::State_strategy)
@settings(max_examples=50)
def test_inputvalue::value::state_instantiation(instance):
    assert isinstance(instance, InputValue::value::State)

@given(instance=Variable::currentValue::State_strategy)
@settings(max_examples=50)
def test_variable::currentvalue::state_instantiation(instance):
    assert isinstance(instance, Variable::currentValue::State)

@given(instance=Activity::trace::State_strategy)
@settings(max_examples=50)
def test_activity::trace::state_instantiation(instance):
    assert isinstance(instance, Activity::trace::State)

@given(instance=Offer::offeredTokens::State_strategy)
@settings(max_examples=50)
def test_offer::offeredtokens::state_instantiation(instance):
    assert isinstance(instance, Offer::offeredTokens::State)

@given(instance=Token::holder::State_strategy)
@settings(max_examples=50)
def test_token::holder::state_instantiation(instance):
    assert isinstance(instance, Token::holder::State)

@given(instance=ForkedToken::baseTokenIsWithdrawn::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::basetokeniswithdrawn::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::baseTokenIsWithdrawn::State)

@given(instance=ForkedToken::remainingOffersCount::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::remainingofferscount::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::remainingOffersCount::State)

@given(instance=Input::inputValues::State_strategy)
@settings(max_examples=50)
def test_input::inputvalues::state_instantiation(instance):
    assert isinstance(instance, Input::inputValues::State)

@given(instance=Trace::executedNodes::State_strategy)
@settings(max_examples=50)
def test_trace::executednodes::state_instantiation(instance):
    assert isinstance(instance, Trace::executedNodes::State)

@given(instance=ActivityEdge::offers::State_strategy)
@settings(max_examples=50)
def test_activityedge::offers::state_instantiation(instance):
    assert isinstance(instance, ActivityEdge::offers::State)

@given(instance=InputValue::variable::State_strategy)
@settings(max_examples=50)
def test_inputvalue::variable::state_instantiation(instance):
    assert isinstance(instance, InputValue::variable::State)

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=traceSystem::GlobalState_strategy)
@settings(max_examples=50)
def test_tracesystem::globalstate_instantiation(instance):
    assert isinstance(instance, traceSystem::GlobalState)

@given(instance=traceSystem::Trace_strategy)
@settings(max_examples=50)
def test_tracesystem::trace_instantiation(instance):
    assert isinstance(instance, traceSystem::Trace)

@given(instance=ForkedToken::baseToken::State_strategy)
@settings(max_examples=50)
def test_forkedtoken::basetoken::state_instantiation(instance):
    assert isinstance(instance, ForkedToken::baseToken::State)

@given(instance=EventOccurrence_strategy)
@settings(max_examples=50)
def test_eventoccurrence_instantiation(instance):
    assert isinstance(instance, EventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluateequalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableExitEventOccurrence)

@given(instance=traceSystem::Events::Action::fire::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::fire::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::fire::actionEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::evaluateandexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::evaluateANDExitEventOccurrence)

@given(instance=traceSystem::Events::Action::sendOffers::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::sendoffers::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::sendOffers::actionExitEventOccurrence)

@given(instance=traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::StringVariable::setCurrentValue::stringVariableExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::evaluatesubtractentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTEntryEventOccurrence)

@given(instance=traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::forkedtoken::withdraw::forkedtokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ForkedToken::withdraw::forkedTokenEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::evaluatesubtractexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::evaluateSUBTRACTExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::mainEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::mainentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::mainEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::fireNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::firenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::fireNodeExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::fireNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::firenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::fireNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::initialnode::isready::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::InitialNode::isReady::InitialNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::initialnode::fire::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::InitialNode::fire::initialNodeExitEventOccurrence)

@given(instance=traceSystem::Events::Token::isWithdrawnEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::iswithdrawnentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::isWithdrawnEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integerexpression::getoperandcurrentvaluesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerExpression::getOperandCurrentValuesExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanunaryexpression::execute::booleanunaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanUnaryExpression::execute::booleanUnaryExpressionEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::initializeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::initializeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::initializeExitEventOccurrence)

@given(instance=traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::forknode::fire::forknodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ForkNode::fire::forkNodeExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::fireinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::fireInitialNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::forkedtoken::withdraw::forkedtokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ForkedToken::withdraw::forkedTokenExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::runExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::runexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::runExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanunaryexpression::evaluatenotexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanUnaryExpression::evaluateNOTExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::hasoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::hasOffersEntryEventOccurrence)

@given(instance=traceSystem::Events::Action::isReady::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::isready::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::isReady::actionExitEventOccurrence)

@given(instance=traceSystem::Events::Token::withdrawEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::withdrawentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::withdrawEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluatesmallerexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateSMALLERExitEventOccurrence)

@given(instance=traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::initialnode::isready::initialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::InitialNode::isReady::InitialNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::isRunningExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::isrunningexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::isRunningExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSExitEventOccurrence)

@given(instance=traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::sendoffers::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::sendOffers::actionEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::fireinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::fireInitialNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::forknode::fire::forknodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ForkNode::fire::forkNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::terminate::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::terminate::activityNodeExitEventOccurrence)

@given(instance=traceSystem::Events::Action::fire::actionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::fire::actionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::fire::actionExitEventOccurrence)

@given(instance=traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::controlnode::isready::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ControlNode::isReady::ControlNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::isreadyentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::isReadyEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::takeofferedtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::takeOfferedTokensExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::removetokenexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::removeTokenExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionExitEventOccurrence)

@given(instance=traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::opaqueaction::doaction::opaqueactionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::OpaqueAction::doAction::opaqueActionExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::takeofferedtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::takeOfferedTokensEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::evaluateorentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::evaluateOREntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::runEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::runentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::runEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::execute::integercomparisionexpressionexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::execute::IntegerComparisionExpressionExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::isrunningentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::isRunningEntryEventOccurrence)

@given(instance=traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::initialnode::fire::initialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::InitialNode::fire::initialNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::getenablednodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::getEnabledNodesEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::terminateEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::terminateentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::terminateEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluategreaterentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateGREATEREntryEventOccurrence)

@given(instance=traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::stringvariable::setcurrentvalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::StringVariable::setCurrentValue::stringVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::mergenode::hasoffers::mergenodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::MergeNode::hasOffers::mergeNodeExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSEntryEventOccurrence)

@given(instance=traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::controlnode::isready::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ControlNode::isReady::ControlNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::controlnode::fire::controlnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ControlNode::fire::controlNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::terminateExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::terminateexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::terminateExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluategreaterexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateGREATERExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::runNodesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::runnodesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::runNodesEntryEventOccurrence)

@given(instance=traceSystem::Events::Token::transferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::transferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::transferEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::evaluateorexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::evaluateORExitEventOccurrence)

@given(instance=traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::opaqueaction::doaction::opaqueactionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::OpaqueAction::doAction::opaqueActionEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::mainExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::mainexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::mainExitEventOccurrence)

@given(instance=traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::decisionnode::fire::decisionnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::DecisionNode::fire::decisionNodeExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::getInitialNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::getinitialnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::getInitialNodeExitEventOccurrence)

@given(instance=traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::execute::integercalculationexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::execute::integerCalculationExpressionEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::runNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::runnodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::runNodesExitEventOccurrence)

@given(instance=traceSystem::Events::Token::withdrawExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::withdrawexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::withdrawExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integervariable::setcurrentvalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::selectnextnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::selectNextNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::Token::transferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::transferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::transferExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanvariable::setcurrentvalue::boolenvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanVariable::setCurrentValue::boolenVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::evaluateandentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::evaluateANDEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::evaluateaddexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::evaluateADDExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercalculationexpression::evaluateaddentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerCalculationExpression::evaluateADDEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::hasofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::hasOfferExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integerexpression::getoperandcurrentvaluesentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerExpression::getOperandCurrentValuesEntryEventOccurrence)

@given(instance=traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::decisionnode::fire::decisionnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::DecisionNode::fire::decisionNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityfinalnode::fire::activityfinalnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityFinalNode::fire::activityFinalNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::hasoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::hasOffersExitEventOccurrence)

@given(instance=traceSystem::Events::Action::isReady::actionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::action::isready::actionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Action::isReady::actionEntryEventOccurrence)

@given(instance=traceSystem::Events::Offer::hasTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::offer::hastokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Offer::hasTokensEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::getinitialnodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::getInitialNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::controlnode::fire::controlnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ControlNode::fire::controlNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::run::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::run::activityNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluatesmaller::equalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateSMALLER::EQUALSExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::removetokenentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::removeTokenEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::isReadyExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::isreadyexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::isReadyExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::getenablednodesexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::getEnabledNodesExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::sendoffersexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::sendOffersExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::sendofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::sendOfferEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::sendofferexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::sendOfferExitEventOccurrence)

@given(instance=traceSystem::Events::Activity::selectNextNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::selectnextnodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::selectNextNodeExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::addtokensentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::addTokensEntryEventOccurrence)

@given(instance=traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::stringvariable::getcurrentvaluevalue::stringvariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::StringVariable::getCurrentValueValue::stringVariableExitEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluateequalsexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateEQUALSExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::terminate::activitynodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::terminate::activityNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::addTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::addtokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::addTokensExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::run::activitynodeexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::run::activityNodeExitEventOccurrence)

@given(instance=traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::mergenode::hasoffers::mergenodeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::MergeNode::hasOffers::mergeNodeEntryEventOccurrence)

@given(instance=traceSystem::Events::Offer::hasTokensExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::offer::hastokensexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Offer::hasTokensExitEventOccurrence)

@given(instance=traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanunaryexpression::evaluatenotentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanUnaryExpression::evaluateNOTEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluatesmallerentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateSMALLEREntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::hasofferentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::hasOfferEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integervariable::getcurrentvaluevalue::integervariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerVariable::getCurrentValueValue::integerVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integervariable::setcurrentvalue::integervariableexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerVariable::setCurrentValue::integerVariableExitEventOccurrence)

@given(instance=traceSystem::Events::Token::isWithdrawnExitEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::token::iswithdrawnexiteventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Token::isWithdrawnExitEventOccurrence)

@given(instance=traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activitynode::sendoffersentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityNode::sendOffersEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanvariable::getcurrentvaluevalue::booleanvariableentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanVariable::getCurrentValueValue::booleanVariableEntryEventOccurrence)

@given(instance=traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::integercomparisonexpression::evaluategreater::equalsentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::IntegerComparisonExpression::evaluateGREATER::EQUALSEntryEventOccurrence)

@given(instance=traceSystem::Events::Activity::initializeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activity::initializeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::Activity::initializeEntryEventOccurrence)

@given(instance=traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::booleanbinaryexpression::execute::booleanbinaryexpressionentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::BooleanBinaryExpression::execute::booleanBinaryExpressionEntryEventOccurrence)

@given(instance=traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence_strategy)
@settings(max_examples=50)
def test_tracesystem::events::activityedge::takeofferedtokens::activityedgeentryeventoccurrence_instantiation(instance):
    assert isinstance(instance, traceSystem::Events::ActivityEdge::takeOfferedTokens::activityEdgeEntryEventOccurrence)

@given(instance=traceSystem::StaticObjectsPools_strategy)
@settings(max_examples=50)
def test_tracesystem::staticobjectspools_instantiation(instance):
    assert isinstance(instance, traceSystem::StaticObjectsPools)

@given(instance=TracedObjects_strategy)
@settings(max_examples=50)
def test_tracedobjects_instantiation(instance):
    assert isinstance(instance, TracedObjects)
