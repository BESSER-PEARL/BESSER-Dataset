import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    assembly::Strategy,
    behavioral::assembly::Strategy,
    Strategy,
    behavioral::assembly::NeutralStrategy,
    behavioral::assembly::InhibitingStrategy,
    behavioral::assembly::EnablingStrategy,
    behavioral::assembly::RequiredStrategy,
    Operator,
    behavioral::assembly::OrOperator,
    behavioral::assembly::AndOperator,
    design::AbstractStatusVariable,
    Connector,
    behavioral::assembly::Precondition,
    behavioral::assembly::Synchroniser,
    behavioral::assembly::Transition,
    design::StatusValue,
    Signature,
    design::AbstractAction,
    ConnectableElement,
    behavioral::assembly::Operator,
    assembly::ConnectableElement,
    SchemaElement,
    behavioral::assembly::ConnectableElement,
    behavioral::assembly::Connector,
    assembly::SchemaElement,
    design::BusinessObjectNode,
    behavioral::design::BusinessObject,
    design::AbstractStatusValue,
    behavioral::assembly::StatusValueProxy,
    AbstractAction,
    behavioral::design::Action,
    AbstractStatusValue,
    behavioral::design::StatusValue,
    AbstractStatusVariable,
    behavioral::design::StatusVariable,
    design::Action,
    behavioral::assembly::ActionProxy,
    design::StatusVariable,
    behavioral::assembly::StatusVariableProxy,
    SAMDerivator,
    behavioral::status::and::action::old::SAMSchemaDerivator,
    SAMAction,
    behavioral::status::and::action::old::SAMSchemaAction,
    SAMStatusSchema,
    behavioral::status::and::action::old::SAMOperator,
    behavioral::status::and::action::old::SAMSchemaValue,
    behavioral::status::and::action::old::SAMSchemaVariable,
    SAMSchemaValue,
    behavioral::status::and::action::old::SAMAction,
    SAMOperator,
    behavioral::status::and::action::old::SAMStatusSchema,
    SAMStatusVariable,
    behavioral::status::and::action::old::SAMStatusValue,
    SAMSchemaDerivator,
    behavioral::status::and::action::old::SAMDerivator,
    SAMSchemaVariable,
    SAMStatusValue,
    behavioral::status::and::action::old::SAMStatusVariable,
    SAMSchemaAction,
    behavioral::transactions::Dummy,
    behavioral::events::EventFilter,
    MethodSignature,
    Subscription,
    behavioral::events::EventProducer,
    SapClass,
    EventFilter,
    EventProducer,
    DimensionDefinition,
    NamedElement,
    behavioral::design::AbstractStatusVariable,
    behavioral::design::AbstractAction,
    behavioral::design::AbstractStatusValue,
    behavioral::design::BusinessObjectNode,
    behavioral::assembly::StatusSchema,
    behavioral::assembly::SchemaElement,
    behavioral::events::Subscription,
    behavioral::rules::Dummy,
    expressions::Conditional,
    NamedValueDeclaration,
    expressions::WithArgument,
    actions::Statement,
    behavioral::actions::ConditionalStatement,
    behavioral::actions::StatementWithArgument,
    Association,
    GroupBy,
    FromClause,
    Selection,
    Foreach,
    Assignment,
    collectionexpressions::Iterate,
    NamedValueWithOptionalInitExpression,
    behavioral::actions::Variable,
    behavioral::actions::Constant,
    behavioral::actions::QueryInvocation,
    behavioral::actions::Sort,
    LinkManipulationStatement,
    behavioral::actions::RemoveLink,
    behavioral::actions::AddLink,
    Iterator,
    Expression,
    SingleBlockStatement,
    behavioral::actions::Foreach,
    actions::SingleBlockStatement,
    Block,
    actions::StatementWithNestedBlocks,
    actions::ConditionalStatement,
    behavioral::actions::WhileLoop,
    behavioral::actions::IfElse,
    StatementWithNestedBlocks,
    behavioral::actions::SingleBlockStatement,
    NamedValue,
    behavioral::actions::NamedValueWithOptionalInitExpression,
    behavioral::actions::Iterator,
    Statement,
    behavioral::actions::NamedValueDeclaration,
    behavioral::actions::LinkManipulationStatement,
    behavioral::actions::ExpressionStatement,
    behavioral::actions::StatementWithNestedBlocks,
    classes::InScope,
    classes::FunctionSignatureImplementation,
    behavioral::actions::Block,
    behavioral::businesstasks::TaskAgent,
    InScope,
    behavioral::actions::Statement,
    Variable,
    StatementWithArgument,
    behavioral::actions::Return,
    behavioral::actions::Assignment,
    behavioral::bpdm::Dummy,
    PreconditionKindEnum,
    SAMOperatorKindEnum,
    SAMDerivatorKindEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_assembly::strategy_is_not_abstract():
    assert not inspect.isabstract(assembly::Strategy)


def test_assembly::strategy_constructor_exists():
    assert callable(assembly::Strategy.__init__)


def test_assembly::strategy_constructor_args():
    sig = inspect.signature(assembly::Strategy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::strategy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Strategy)


def test_behavioral::assembly::strategy_constructor_exists():
    assert callable(behavioral::assembly::Strategy.__init__)


def test_behavioral::assembly::strategy_constructor_args():
    sig = inspect.signature(behavioral::assembly::Strategy.__init__)
    params = list(sig.parameters.keys())



def test_strategy_is_not_abstract():
    assert not inspect.isabstract(Strategy)


def test_strategy_constructor_exists():
    assert callable(Strategy.__init__)


def test_strategy_constructor_args():
    sig = inspect.signature(Strategy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::neutralstrategy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::NeutralStrategy)


def test_behavioral::assembly::neutralstrategy_constructor_exists():
    assert callable(behavioral::assembly::NeutralStrategy.__init__)


def test_behavioral::assembly::neutralstrategy_constructor_args():
    sig = inspect.signature(behavioral::assembly::NeutralStrategy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::inhibitingstrategy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::InhibitingStrategy)


def test_behavioral::assembly::inhibitingstrategy_constructor_exists():
    assert callable(behavioral::assembly::InhibitingStrategy.__init__)


def test_behavioral::assembly::inhibitingstrategy_constructor_args():
    sig = inspect.signature(behavioral::assembly::InhibitingStrategy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::enablingstrategy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::EnablingStrategy)


def test_behavioral::assembly::enablingstrategy_constructor_exists():
    assert callable(behavioral::assembly::EnablingStrategy.__init__)


def test_behavioral::assembly::enablingstrategy_constructor_args():
    sig = inspect.signature(behavioral::assembly::EnablingStrategy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::requiredstrategy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::RequiredStrategy)


def test_behavioral::assembly::requiredstrategy_constructor_exists():
    assert callable(behavioral::assembly::RequiredStrategy.__init__)


def test_behavioral::assembly::requiredstrategy_constructor_args():
    sig = inspect.signature(behavioral::assembly::RequiredStrategy.__init__)
    params = list(sig.parameters.keys())



def test_operator_is_not_abstract():
    assert not inspect.isabstract(Operator)


def test_operator_constructor_exists():
    assert callable(Operator.__init__)


def test_operator_constructor_args():
    sig = inspect.signature(Operator.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::oroperator_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::OrOperator)


def test_behavioral::assembly::oroperator_constructor_exists():
    assert callable(behavioral::assembly::OrOperator.__init__)


def test_behavioral::assembly::oroperator_constructor_args():
    sig = inspect.signature(behavioral::assembly::OrOperator.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::andoperator_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::AndOperator)


def test_behavioral::assembly::andoperator_constructor_exists():
    assert callable(behavioral::assembly::AndOperator.__init__)


def test_behavioral::assembly::andoperator_constructor_args():
    sig = inspect.signature(behavioral::assembly::AndOperator.__init__)
    params = list(sig.parameters.keys())



def test_design::abstractstatusvariable_is_not_abstract():
    assert not inspect.isabstract(design::AbstractStatusVariable)


def test_design::abstractstatusvariable_constructor_exists():
    assert callable(design::AbstractStatusVariable.__init__)


def test_design::abstractstatusvariable_constructor_args():
    sig = inspect.signature(design::AbstractStatusVariable.__init__)
    params = list(sig.parameters.keys())



def test_connector_is_not_abstract():
    assert not inspect.isabstract(Connector)


def test_connector_constructor_exists():
    assert callable(Connector.__init__)


def test_connector_constructor_args():
    sig = inspect.signature(Connector.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::precondition_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Precondition)


def test_behavioral::assembly::precondition_constructor_exists():
    assert callable(behavioral::assembly::Precondition.__init__)


def test_behavioral::assembly::precondition_constructor_args():
    sig = inspect.signature(behavioral::assembly::Precondition.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::synchroniser_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Synchroniser)


def test_behavioral::assembly::synchroniser_constructor_exists():
    assert callable(behavioral::assembly::Synchroniser.__init__)


def test_behavioral::assembly::synchroniser_constructor_args():
    sig = inspect.signature(behavioral::assembly::Synchroniser.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::transition_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Transition)


def test_behavioral::assembly::transition_constructor_exists():
    assert callable(behavioral::assembly::Transition.__init__)


def test_behavioral::assembly::transition_constructor_args():
    sig = inspect.signature(behavioral::assembly::Transition.__init__)
    params = list(sig.parameters.keys())



def test_design::statusvalue_is_not_abstract():
    assert not inspect.isabstract(design::StatusValue)


def test_design::statusvalue_constructor_exists():
    assert callable(design::StatusValue.__init__)


def test_design::statusvalue_constructor_args():
    sig = inspect.signature(design::StatusValue.__init__)
    params = list(sig.parameters.keys())



def test_signature_is_not_abstract():
    assert not inspect.isabstract(Signature)


def test_signature_constructor_exists():
    assert callable(Signature.__init__)


def test_signature_constructor_args():
    sig = inspect.signature(Signature.__init__)
    params = list(sig.parameters.keys())



def test_design::abstractaction_is_not_abstract():
    assert not inspect.isabstract(design::AbstractAction)


def test_design::abstractaction_constructor_exists():
    assert callable(design::AbstractAction.__init__)


def test_design::abstractaction_constructor_args():
    sig = inspect.signature(design::AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_connectableelement_is_not_abstract():
    assert not inspect.isabstract(ConnectableElement)


def test_connectableelement_constructor_exists():
    assert callable(ConnectableElement.__init__)


def test_connectableelement_constructor_args():
    sig = inspect.signature(ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::operator_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Operator)


def test_behavioral::assembly::operator_constructor_exists():
    assert callable(behavioral::assembly::Operator.__init__)


def test_behavioral::assembly::operator_constructor_args():
    sig = inspect.signature(behavioral::assembly::Operator.__init__)
    params = list(sig.parameters.keys())



def test_assembly::connectableelement_is_not_abstract():
    assert not inspect.isabstract(assembly::ConnectableElement)


def test_assembly::connectableelement_constructor_exists():
    assert callable(assembly::ConnectableElement.__init__)


def test_assembly::connectableelement_constructor_args():
    sig = inspect.signature(assembly::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_schemaelement_is_not_abstract():
    assert not inspect.isabstract(SchemaElement)


def test_schemaelement_constructor_exists():
    assert callable(SchemaElement.__init__)


def test_schemaelement_constructor_args():
    sig = inspect.signature(SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::connectableelement_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::ConnectableElement)


def test_behavioral::assembly::connectableelement_constructor_exists():
    assert callable(behavioral::assembly::ConnectableElement.__init__)


def test_behavioral::assembly::connectableelement_constructor_args():
    sig = inspect.signature(behavioral::assembly::ConnectableElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::connector_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::Connector)


def test_behavioral::assembly::connector_constructor_exists():
    assert callable(behavioral::assembly::Connector.__init__)


def test_behavioral::assembly::connector_constructor_args():
    sig = inspect.signature(behavioral::assembly::Connector.__init__)
    params = list(sig.parameters.keys())



def test_assembly::schemaelement_is_not_abstract():
    assert not inspect.isabstract(assembly::SchemaElement)


def test_assembly::schemaelement_constructor_exists():
    assert callable(assembly::SchemaElement.__init__)


def test_assembly::schemaelement_constructor_args():
    sig = inspect.signature(assembly::SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_design::businessobjectnode_is_not_abstract():
    assert not inspect.isabstract(design::BusinessObjectNode)


def test_design::businessobjectnode_constructor_exists():
    assert callable(design::BusinessObjectNode.__init__)


def test_design::businessobjectnode_constructor_args():
    sig = inspect.signature(design::BusinessObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::design::businessobject_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::BusinessObject)


def test_behavioral::design::businessobject_constructor_exists():
    assert callable(behavioral::design::BusinessObject.__init__)


def test_behavioral::design::businessobject_constructor_args():
    sig = inspect.signature(behavioral::design::BusinessObject.__init__)
    params = list(sig.parameters.keys())



def test_design::abstractstatusvalue_is_not_abstract():
    assert not inspect.isabstract(design::AbstractStatusValue)


def test_design::abstractstatusvalue_constructor_exists():
    assert callable(design::AbstractStatusValue.__init__)


def test_design::abstractstatusvalue_constructor_args():
    sig = inspect.signature(design::AbstractStatusValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::statusvalueproxy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::StatusValueProxy)


def test_behavioral::assembly::statusvalueproxy_constructor_exists():
    assert callable(behavioral::assembly::StatusValueProxy.__init__)


def test_behavioral::assembly::statusvalueproxy_constructor_args():
    sig = inspect.signature(behavioral::assembly::StatusValueProxy.__init__)
    params = list(sig.parameters.keys())



def test_abstractaction_is_not_abstract():
    assert not inspect.isabstract(AbstractAction)


def test_abstractaction_constructor_exists():
    assert callable(AbstractAction.__init__)


def test_abstractaction_constructor_args():
    sig = inspect.signature(AbstractAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::design::action_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::Action)


def test_behavioral::design::action_constructor_exists():
    assert callable(behavioral::design::Action.__init__)


def test_behavioral::design::action_constructor_args():
    sig = inspect.signature(behavioral::design::Action.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatusvalue_is_not_abstract():
    assert not inspect.isabstract(AbstractStatusValue)


def test_abstractstatusvalue_constructor_exists():
    assert callable(AbstractStatusValue.__init__)


def test_abstractstatusvalue_constructor_args():
    sig = inspect.signature(AbstractStatusValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::design::statusvalue_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::StatusValue)


def test_behavioral::design::statusvalue_constructor_exists():
    assert callable(behavioral::design::StatusValue.__init__)


def test_behavioral::design::statusvalue_constructor_args():
    sig = inspect.signature(behavioral::design::StatusValue.__init__)
    params = list(sig.parameters.keys())



def test_abstractstatusvariable_is_not_abstract():
    assert not inspect.isabstract(AbstractStatusVariable)


def test_abstractstatusvariable_constructor_exists():
    assert callable(AbstractStatusVariable.__init__)


def test_abstractstatusvariable_constructor_args():
    sig = inspect.signature(AbstractStatusVariable.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::design::statusvariable_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::StatusVariable)


def test_behavioral::design::statusvariable_constructor_exists():
    assert callable(behavioral::design::StatusVariable.__init__)


def test_behavioral::design::statusvariable_constructor_args():
    sig = inspect.signature(behavioral::design::StatusVariable.__init__)
    params = list(sig.parameters.keys())



def test_design::action_is_not_abstract():
    assert not inspect.isabstract(design::Action)


def test_design::action_constructor_exists():
    assert callable(design::Action.__init__)


def test_design::action_constructor_args():
    sig = inspect.signature(design::Action.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::actionproxy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::ActionProxy)


def test_behavioral::assembly::actionproxy_constructor_exists():
    assert callable(behavioral::assembly::ActionProxy.__init__)


def test_behavioral::assembly::actionproxy_constructor_args():
    sig = inspect.signature(behavioral::assembly::ActionProxy.__init__)
    params = list(sig.parameters.keys())



def test_design::statusvariable_is_not_abstract():
    assert not inspect.isabstract(design::StatusVariable)


def test_design::statusvariable_constructor_exists():
    assert callable(design::StatusVariable.__init__)


def test_design::statusvariable_constructor_args():
    sig = inspect.signature(design::StatusVariable.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::statusvariableproxy_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::StatusVariableProxy)


def test_behavioral::assembly::statusvariableproxy_constructor_exists():
    assert callable(behavioral::assembly::StatusVariableProxy.__init__)


def test_behavioral::assembly::statusvariableproxy_constructor_args():
    sig = inspect.signature(behavioral::assembly::StatusVariableProxy.__init__)
    params = list(sig.parameters.keys())



def test_samderivator_is_not_abstract():
    assert not inspect.isabstract(SAMDerivator)


def test_samderivator_constructor_exists():
    assert callable(SAMDerivator.__init__)


def test_samderivator_constructor_args():
    sig = inspect.signature(SAMDerivator.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samschemaderivator_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMSchemaDerivator)


def test_behavioral::status::and::action::old::samschemaderivator_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMSchemaDerivator.__init__)


def test_behavioral::status::and::action::old::samschemaderivator_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMSchemaDerivator.__init__)
    params = list(sig.parameters.keys())



def test_samaction_is_not_abstract():
    assert not inspect.isabstract(SAMAction)


def test_samaction_constructor_exists():
    assert callable(SAMAction.__init__)


def test_samaction_constructor_args():
    sig = inspect.signature(SAMAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samschemaaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMSchemaAction)


def test_behavioral::status::and::action::old::samschemaaction_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMSchemaAction.__init__)


def test_behavioral::status::and::action::old::samschemaaction_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMSchemaAction.__init__)
    params = list(sig.parameters.keys())



def test_samstatusschema_is_not_abstract():
    assert not inspect.isabstract(SAMStatusSchema)


def test_samstatusschema_constructor_exists():
    assert callable(SAMStatusSchema.__init__)


def test_samstatusschema_constructor_args():
    sig = inspect.signature(SAMStatusSchema.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samoperator_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMOperator)


def test_behavioral::status::and::action::old::samoperator_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMOperator.__init__)


def test_behavioral::status::and::action::old::samoperator_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMOperator.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_behavioral::status::and::action::old::samoperator_has_kind():
    assert hasattr(behavioral::status::and::action::old::SAMOperator, "kind")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMOperator.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::status::and::action::old::samschemavalue_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMSchemaValue)


def test_behavioral::status::and::action::old::samschemavalue_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMSchemaValue.__init__)


def test_behavioral::status::and::action::old::samschemavalue_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMSchemaValue.__init__)
    params = list(sig.parameters.keys())
    assert "isInhibiting" in params, "Missing parameter 'isInhibiting'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"

def test_behavioral::status::and::action::old::samschemavalue_has_isInhibiting():
    assert hasattr(behavioral::status::and::action::old::SAMSchemaValue, "isInhibiting")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMSchemaValue.__mro__:
        if "isInhibiting" in klass.__dict__:
            descriptor = klass.__dict__["isInhibiting"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::status::and::action::old::samschemavalue_has_isInitial():
    assert hasattr(behavioral::status::and::action::old::SAMSchemaValue, "isInitial")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMSchemaValue.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::status::and::action::old::samschemavariable_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMSchemaVariable)


def test_behavioral::status::and::action::old::samschemavariable_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMSchemaVariable.__init__)


def test_behavioral::status::and::action::old::samschemavariable_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMSchemaVariable.__init__)
    params = list(sig.parameters.keys())
    assert "hasStateGuard" in params, "Missing parameter 'hasStateGuard'"

def test_behavioral::status::and::action::old::samschemavariable_has_hasStateGuard():
    assert hasattr(behavioral::status::and::action::old::SAMSchemaVariable, "hasStateGuard")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMSchemaVariable.__mro__:
        if "hasStateGuard" in klass.__dict__:
            descriptor = klass.__dict__["hasStateGuard"]
            break
    assert isinstance(descriptor, property)



def test_samschemavalue_is_not_abstract():
    assert not inspect.isabstract(SAMSchemaValue)


def test_samschemavalue_constructor_exists():
    assert callable(SAMSchemaValue.__init__)


def test_samschemavalue_constructor_args():
    sig = inspect.signature(SAMSchemaValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMAction)


def test_behavioral::status::and::action::old::samaction_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMAction.__init__)


def test_behavioral::status::and::action::old::samaction_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMAction.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAgentAction" in params, "Missing parameter 'isAgentAction'"

def test_behavioral::status::and::action::old::samaction_has_name():
    assert hasattr(behavioral::status::and::action::old::SAMAction, "name")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMAction.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::status::and::action::old::samaction_has_isAgentAction():
    assert hasattr(behavioral::status::and::action::old::SAMAction, "isAgentAction")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMAction.__mro__:
        if "isAgentAction" in klass.__dict__:
            descriptor = klass.__dict__["isAgentAction"]
            break
    assert isinstance(descriptor, property)



def test_samoperator_is_not_abstract():
    assert not inspect.isabstract(SAMOperator)


def test_samoperator_constructor_exists():
    assert callable(SAMOperator.__init__)


def test_samoperator_constructor_args():
    sig = inspect.signature(SAMOperator.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samstatusschema_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMStatusSchema)


def test_behavioral::status::and::action::old::samstatusschema_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMStatusSchema.__init__)


def test_behavioral::status::and::action::old::samstatusschema_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMStatusSchema.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behavioral::status::and::action::old::samstatusschema_has_name():
    assert hasattr(behavioral::status::and::action::old::SAMStatusSchema, "name")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMStatusSchema.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_samstatusvariable_is_not_abstract():
    assert not inspect.isabstract(SAMStatusVariable)


def test_samstatusvariable_constructor_exists():
    assert callable(SAMStatusVariable.__init__)


def test_samstatusvariable_constructor_args():
    sig = inspect.signature(SAMStatusVariable.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samstatusvalue_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMStatusValue)


def test_behavioral::status::and::action::old::samstatusvalue_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMStatusValue.__init__)


def test_behavioral::status::and::action::old::samstatusvalue_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMStatusValue.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behavioral::status::and::action::old::samstatusvalue_has_name():
    assert hasattr(behavioral::status::and::action::old::SAMStatusValue, "name")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMStatusValue.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_samschemaderivator_is_not_abstract():
    assert not inspect.isabstract(SAMSchemaDerivator)


def test_samschemaderivator_constructor_exists():
    assert callable(SAMSchemaDerivator.__init__)


def test_samschemaderivator_constructor_args():
    sig = inspect.signature(SAMSchemaDerivator.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samderivator_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMDerivator)


def test_behavioral::status::and::action::old::samderivator_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMDerivator.__init__)


def test_behavioral::status::and::action::old::samderivator_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMDerivator.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_behavioral::status::and::action::old::samderivator_has_kind():
    assert hasattr(behavioral::status::and::action::old::SAMDerivator, "kind")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMDerivator.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_samschemavariable_is_not_abstract():
    assert not inspect.isabstract(SAMSchemaVariable)


def test_samschemavariable_constructor_exists():
    assert callable(SAMSchemaVariable.__init__)


def test_samschemavariable_constructor_args():
    sig = inspect.signature(SAMSchemaVariable.__init__)
    params = list(sig.parameters.keys())



def test_samstatusvalue_is_not_abstract():
    assert not inspect.isabstract(SAMStatusValue)


def test_samstatusvalue_constructor_exists():
    assert callable(SAMStatusValue.__init__)


def test_samstatusvalue_constructor_args():
    sig = inspect.signature(SAMStatusValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::status::and::action::old::samstatusvariable_is_not_abstract():
    assert not inspect.isabstract(behavioral::status::and::action::old::SAMStatusVariable)


def test_behavioral::status::and::action::old::samstatusvariable_constructor_exists():
    assert callable(behavioral::status::and::action::old::SAMStatusVariable.__init__)


def test_behavioral::status::and::action::old::samstatusvariable_constructor_args():
    sig = inspect.signature(behavioral::status::and::action::old::SAMStatusVariable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isAgentVariable" in params, "Missing parameter 'isAgentVariable'"

def test_behavioral::status::and::action::old::samstatusvariable_has_name():
    assert hasattr(behavioral::status::and::action::old::SAMStatusVariable, "name")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMStatusVariable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::status::and::action::old::samstatusvariable_has_isAgentVariable():
    assert hasattr(behavioral::status::and::action::old::SAMStatusVariable, "isAgentVariable")
    descriptor = None
    for klass in behavioral::status::and::action::old::SAMStatusVariable.__mro__:
        if "isAgentVariable" in klass.__dict__:
            descriptor = klass.__dict__["isAgentVariable"]
            break
    assert isinstance(descriptor, property)



def test_samschemaaction_is_not_abstract():
    assert not inspect.isabstract(SAMSchemaAction)


def test_samschemaaction_constructor_exists():
    assert callable(SAMSchemaAction.__init__)


def test_samschemaaction_constructor_args():
    sig = inspect.signature(SAMSchemaAction.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::transactions::dummy_is_not_abstract():
    assert not inspect.isabstract(behavioral::transactions::Dummy)


def test_behavioral::transactions::dummy_constructor_exists():
    assert callable(behavioral::transactions::Dummy.__init__)


def test_behavioral::transactions::dummy_constructor_args():
    sig = inspect.signature(behavioral::transactions::Dummy.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::events::eventfilter_is_not_abstract():
    assert not inspect.isabstract(behavioral::events::EventFilter)


def test_behavioral::events::eventfilter_constructor_exists():
    assert callable(behavioral::events::EventFilter.__init__)


def test_behavioral::events::eventfilter_constructor_args():
    sig = inspect.signature(behavioral::events::EventFilter.__init__)
    params = list(sig.parameters.keys())



def test_methodsignature_is_not_abstract():
    assert not inspect.isabstract(MethodSignature)


def test_methodsignature_constructor_exists():
    assert callable(MethodSignature.__init__)


def test_methodsignature_constructor_args():
    sig = inspect.signature(MethodSignature.__init__)
    params = list(sig.parameters.keys())



def test_subscription_is_not_abstract():
    assert not inspect.isabstract(Subscription)


def test_subscription_constructor_exists():
    assert callable(Subscription.__init__)


def test_subscription_constructor_args():
    sig = inspect.signature(Subscription.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::events::eventproducer_is_not_abstract():
    assert not inspect.isabstract(behavioral::events::EventProducer)


def test_behavioral::events::eventproducer_constructor_exists():
    assert callable(behavioral::events::EventProducer.__init__)


def test_behavioral::events::eventproducer_constructor_args():
    sig = inspect.signature(behavioral::events::EventProducer.__init__)
    params = list(sig.parameters.keys())



def test_sapclass_is_not_abstract():
    assert not inspect.isabstract(SapClass)


def test_sapclass_constructor_exists():
    assert callable(SapClass.__init__)


def test_sapclass_constructor_args():
    sig = inspect.signature(SapClass.__init__)
    params = list(sig.parameters.keys())



def test_eventfilter_is_not_abstract():
    assert not inspect.isabstract(EventFilter)


def test_eventfilter_constructor_exists():
    assert callable(EventFilter.__init__)


def test_eventfilter_constructor_args():
    sig = inspect.signature(EventFilter.__init__)
    params = list(sig.parameters.keys())



def test_eventproducer_is_not_abstract():
    assert not inspect.isabstract(EventProducer)


def test_eventproducer_constructor_exists():
    assert callable(EventProducer.__init__)


def test_eventproducer_constructor_args():
    sig = inspect.signature(EventProducer.__init__)
    params = list(sig.parameters.keys())



def test_dimensiondefinition_is_not_abstract():
    assert not inspect.isabstract(DimensionDefinition)


def test_dimensiondefinition_constructor_exists():
    assert callable(DimensionDefinition.__init__)


def test_dimensiondefinition_constructor_args():
    sig = inspect.signature(DimensionDefinition.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::design::abstractstatusvariable_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::AbstractStatusVariable)


def test_behavioral::design::abstractstatusvariable_constructor_exists():
    assert callable(behavioral::design::AbstractStatusVariable.__init__)


def test_behavioral::design::abstractstatusvariable_constructor_args():
    sig = inspect.signature(behavioral::design::AbstractStatusVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isStateGuarded" in params, "Missing parameter 'isStateGuarded'"
    assert "isAgent" in params, "Missing parameter 'isAgent'"

def test_behavioral::design::abstractstatusvariable_has_isStateGuarded():
    assert hasattr(behavioral::design::AbstractStatusVariable, "isStateGuarded")
    descriptor = None
    for klass in behavioral::design::AbstractStatusVariable.__mro__:
        if "isStateGuarded" in klass.__dict__:
            descriptor = klass.__dict__["isStateGuarded"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::design::abstractstatusvariable_has_isAgent():
    assert hasattr(behavioral::design::AbstractStatusVariable, "isAgent")
    descriptor = None
    for klass in behavioral::design::AbstractStatusVariable.__mro__:
        if "isAgent" in klass.__dict__:
            descriptor = klass.__dict__["isAgent"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::design::abstractaction_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::AbstractAction)


def test_behavioral::design::abstractaction_constructor_exists():
    assert callable(behavioral::design::AbstractAction.__init__)


def test_behavioral::design::abstractaction_constructor_args():
    sig = inspect.signature(behavioral::design::AbstractAction.__init__)
    params = list(sig.parameters.keys())
    assert "isPreconditionFixed" in params, "Missing parameter 'isPreconditionFixed'"
    assert "isAgent" in params, "Missing parameter 'isAgent'"

def test_behavioral::design::abstractaction_has_isPreconditionFixed():
    assert hasattr(behavioral::design::AbstractAction, "isPreconditionFixed")
    descriptor = None
    for klass in behavioral::design::AbstractAction.__mro__:
        if "isPreconditionFixed" in klass.__dict__:
            descriptor = klass.__dict__["isPreconditionFixed"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::design::abstractaction_has_isAgent():
    assert hasattr(behavioral::design::AbstractAction, "isAgent")
    descriptor = None
    for klass in behavioral::design::AbstractAction.__mro__:
        if "isAgent" in klass.__dict__:
            descriptor = klass.__dict__["isAgent"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::design::abstractstatusvalue_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::AbstractStatusValue)


def test_behavioral::design::abstractstatusvalue_constructor_exists():
    assert callable(behavioral::design::AbstractStatusValue.__init__)


def test_behavioral::design::abstractstatusvalue_constructor_args():
    sig = inspect.signature(behavioral::design::AbstractStatusValue.__init__)
    params = list(sig.parameters.keys())
    assert "isStateGuarded" in params, "Missing parameter 'isStateGuarded'"
    assert "isInitial" in params, "Missing parameter 'isInitial'"
    assert "isInhibiting" in params, "Missing parameter 'isInhibiting'"

def test_behavioral::design::abstractstatusvalue_has_isStateGuarded():
    assert hasattr(behavioral::design::AbstractStatusValue, "isStateGuarded")
    descriptor = None
    for klass in behavioral::design::AbstractStatusValue.__mro__:
        if "isStateGuarded" in klass.__dict__:
            descriptor = klass.__dict__["isStateGuarded"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::design::abstractstatusvalue_has_isInitial():
    assert hasattr(behavioral::design::AbstractStatusValue, "isInitial")
    descriptor = None
    for klass in behavioral::design::AbstractStatusValue.__mro__:
        if "isInitial" in klass.__dict__:
            descriptor = klass.__dict__["isInitial"]
            break
    assert isinstance(descriptor, property)

def test_behavioral::design::abstractstatusvalue_has_isInhibiting():
    assert hasattr(behavioral::design::AbstractStatusValue, "isInhibiting")
    descriptor = None
    for klass in behavioral::design::AbstractStatusValue.__mro__:
        if "isInhibiting" in klass.__dict__:
            descriptor = klass.__dict__["isInhibiting"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::design::businessobjectnode_is_not_abstract():
    assert not inspect.isabstract(behavioral::design::BusinessObjectNode)


def test_behavioral::design::businessobjectnode_constructor_exists():
    assert callable(behavioral::design::BusinessObjectNode.__init__)


def test_behavioral::design::businessobjectnode_constructor_args():
    sig = inspect.signature(behavioral::design::BusinessObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::statusschema_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::StatusSchema)


def test_behavioral::assembly::statusschema_constructor_exists():
    assert callable(behavioral::assembly::StatusSchema.__init__)


def test_behavioral::assembly::statusschema_constructor_args():
    sig = inspect.signature(behavioral::assembly::StatusSchema.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::assembly::schemaelement_is_not_abstract():
    assert not inspect.isabstract(behavioral::assembly::SchemaElement)


def test_behavioral::assembly::schemaelement_constructor_exists():
    assert callable(behavioral::assembly::SchemaElement.__init__)


def test_behavioral::assembly::schemaelement_constructor_args():
    sig = inspect.signature(behavioral::assembly::SchemaElement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::events::subscription_is_not_abstract():
    assert not inspect.isabstract(behavioral::events::Subscription)


def test_behavioral::events::subscription_constructor_exists():
    assert callable(behavioral::events::Subscription.__init__)


def test_behavioral::events::subscription_constructor_args():
    sig = inspect.signature(behavioral::events::Subscription.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::rules::dummy_is_not_abstract():
    assert not inspect.isabstract(behavioral::rules::Dummy)


def test_behavioral::rules::dummy_constructor_exists():
    assert callable(behavioral::rules::Dummy.__init__)


def test_behavioral::rules::dummy_constructor_args():
    sig = inspect.signature(behavioral::rules::Dummy.__init__)
    params = list(sig.parameters.keys())



def test_expressions::conditional_is_not_abstract():
    assert not inspect.isabstract(expressions::Conditional)


def test_expressions::conditional_constructor_exists():
    assert callable(expressions::Conditional.__init__)


def test_expressions::conditional_constructor_args():
    sig = inspect.signature(expressions::Conditional.__init__)
    params = list(sig.parameters.keys())



def test_namedvaluedeclaration_is_not_abstract():
    assert not inspect.isabstract(NamedValueDeclaration)


def test_namedvaluedeclaration_constructor_exists():
    assert callable(NamedValueDeclaration.__init__)


def test_namedvaluedeclaration_constructor_args():
    sig = inspect.signature(NamedValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_expressions::withargument_is_not_abstract():
    assert not inspect.isabstract(expressions::WithArgument)


def test_expressions::withargument_constructor_exists():
    assert callable(expressions::WithArgument.__init__)


def test_expressions::withargument_constructor_args():
    sig = inspect.signature(expressions::WithArgument.__init__)
    params = list(sig.parameters.keys())



def test_actions::statement_is_not_abstract():
    assert not inspect.isabstract(actions::Statement)


def test_actions::statement_constructor_exists():
    assert callable(actions::Statement.__init__)


def test_actions::statement_constructor_args():
    sig = inspect.signature(actions::Statement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::ConditionalStatement)


def test_behavioral::actions::conditionalstatement_constructor_exists():
    assert callable(behavioral::actions::ConditionalStatement.__init__)


def test_behavioral::actions::conditionalstatement_constructor_args():
    sig = inspect.signature(behavioral::actions::ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::statementwithargument_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::StatementWithArgument)


def test_behavioral::actions::statementwithargument_constructor_exists():
    assert callable(behavioral::actions::StatementWithArgument.__init__)


def test_behavioral::actions::statementwithargument_constructor_args():
    sig = inspect.signature(behavioral::actions::StatementWithArgument.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_groupby_is_not_abstract():
    assert not inspect.isabstract(GroupBy)


def test_groupby_constructor_exists():
    assert callable(GroupBy.__init__)


def test_groupby_constructor_args():
    sig = inspect.signature(GroupBy.__init__)
    params = list(sig.parameters.keys())



def test_fromclause_is_not_abstract():
    assert not inspect.isabstract(FromClause)


def test_fromclause_constructor_exists():
    assert callable(FromClause.__init__)


def test_fromclause_constructor_args():
    sig = inspect.signature(FromClause.__init__)
    params = list(sig.parameters.keys())



def test_selection_is_not_abstract():
    assert not inspect.isabstract(Selection)


def test_selection_constructor_exists():
    assert callable(Selection.__init__)


def test_selection_constructor_args():
    sig = inspect.signature(Selection.__init__)
    params = list(sig.parameters.keys())



def test_foreach_is_not_abstract():
    assert not inspect.isabstract(Foreach)


def test_foreach_constructor_exists():
    assert callable(Foreach.__init__)


def test_foreach_constructor_args():
    sig = inspect.signature(Foreach.__init__)
    params = list(sig.parameters.keys())



def test_assignment_is_not_abstract():
    assert not inspect.isabstract(Assignment)


def test_assignment_constructor_exists():
    assert callable(Assignment.__init__)


def test_assignment_constructor_args():
    sig = inspect.signature(Assignment.__init__)
    params = list(sig.parameters.keys())



def test_collectionexpressions::iterate_is_not_abstract():
    assert not inspect.isabstract(collectionexpressions::Iterate)


def test_collectionexpressions::iterate_constructor_exists():
    assert callable(collectionexpressions::Iterate.__init__)


def test_collectionexpressions::iterate_constructor_args():
    sig = inspect.signature(collectionexpressions::Iterate.__init__)
    params = list(sig.parameters.keys())



def test_namedvaluewithoptionalinitexpression_is_not_abstract():
    assert not inspect.isabstract(NamedValueWithOptionalInitExpression)


def test_namedvaluewithoptionalinitexpression_constructor_exists():
    assert callable(NamedValueWithOptionalInitExpression.__init__)


def test_namedvaluewithoptionalinitexpression_constructor_args():
    sig = inspect.signature(NamedValueWithOptionalInitExpression.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::variable_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Variable)


def test_behavioral::actions::variable_constructor_exists():
    assert callable(behavioral::actions::Variable.__init__)


def test_behavioral::actions::variable_constructor_args():
    sig = inspect.signature(behavioral::actions::Variable.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::constant_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Constant)


def test_behavioral::actions::constant_constructor_exists():
    assert callable(behavioral::actions::Constant.__init__)


def test_behavioral::actions::constant_constructor_args():
    sig = inspect.signature(behavioral::actions::Constant.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::queryinvocation_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::QueryInvocation)


def test_behavioral::actions::queryinvocation_constructor_exists():
    assert callable(behavioral::actions::QueryInvocation.__init__)


def test_behavioral::actions::queryinvocation_constructor_args():
    sig = inspect.signature(behavioral::actions::QueryInvocation.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::sort_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Sort)


def test_behavioral::actions::sort_constructor_exists():
    assert callable(behavioral::actions::Sort.__init__)


def test_behavioral::actions::sort_constructor_args():
    sig = inspect.signature(behavioral::actions::Sort.__init__)
    params = list(sig.parameters.keys())



def test_linkmanipulationstatement_is_not_abstract():
    assert not inspect.isabstract(LinkManipulationStatement)


def test_linkmanipulationstatement_constructor_exists():
    assert callable(LinkManipulationStatement.__init__)


def test_linkmanipulationstatement_constructor_args():
    sig = inspect.signature(LinkManipulationStatement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::removelink_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::RemoveLink)


def test_behavioral::actions::removelink_constructor_exists():
    assert callable(behavioral::actions::RemoveLink.__init__)


def test_behavioral::actions::removelink_constructor_args():
    sig = inspect.signature(behavioral::actions::RemoveLink.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::addlink_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::AddLink)


def test_behavioral::actions::addlink_constructor_exists():
    assert callable(behavioral::actions::AddLink.__init__)


def test_behavioral::actions::addlink_constructor_args():
    sig = inspect.signature(behavioral::actions::AddLink.__init__)
    params = list(sig.parameters.keys())



def test_iterator_is_not_abstract():
    assert not inspect.isabstract(Iterator)


def test_iterator_constructor_exists():
    assert callable(Iterator.__init__)


def test_iterator_constructor_args():
    sig = inspect.signature(Iterator.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_singleblockstatement_is_not_abstract():
    assert not inspect.isabstract(SingleBlockStatement)


def test_singleblockstatement_constructor_exists():
    assert callable(SingleBlockStatement.__init__)


def test_singleblockstatement_constructor_args():
    sig = inspect.signature(SingleBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::foreach_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Foreach)


def test_behavioral::actions::foreach_constructor_exists():
    assert callable(behavioral::actions::Foreach.__init__)


def test_behavioral::actions::foreach_constructor_args():
    sig = inspect.signature(behavioral::actions::Foreach.__init__)
    params = list(sig.parameters.keys())
    assert "parallel" in params, "Missing parameter 'parallel'"

def test_behavioral::actions::foreach_has_parallel():
    assert hasattr(behavioral::actions::Foreach, "parallel")
    descriptor = None
    for klass in behavioral::actions::Foreach.__mro__:
        if "parallel" in klass.__dict__:
            descriptor = klass.__dict__["parallel"]
            break
    assert isinstance(descriptor, property)



def test_actions::singleblockstatement_is_not_abstract():
    assert not inspect.isabstract(actions::SingleBlockStatement)


def test_actions::singleblockstatement_constructor_exists():
    assert callable(actions::SingleBlockStatement.__init__)


def test_actions::singleblockstatement_constructor_args():
    sig = inspect.signature(actions::SingleBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_actions::statementwithnestedblocks_is_not_abstract():
    assert not inspect.isabstract(actions::StatementWithNestedBlocks)


def test_actions::statementwithnestedblocks_constructor_exists():
    assert callable(actions::StatementWithNestedBlocks.__init__)


def test_actions::statementwithnestedblocks_constructor_args():
    sig = inspect.signature(actions::StatementWithNestedBlocks.__init__)
    params = list(sig.parameters.keys())



def test_actions::conditionalstatement_is_not_abstract():
    assert not inspect.isabstract(actions::ConditionalStatement)


def test_actions::conditionalstatement_constructor_exists():
    assert callable(actions::ConditionalStatement.__init__)


def test_actions::conditionalstatement_constructor_args():
    sig = inspect.signature(actions::ConditionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::whileloop_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::WhileLoop)


def test_behavioral::actions::whileloop_constructor_exists():
    assert callable(behavioral::actions::WhileLoop.__init__)


def test_behavioral::actions::whileloop_constructor_args():
    sig = inspect.signature(behavioral::actions::WhileLoop.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::ifelse_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::IfElse)


def test_behavioral::actions::ifelse_constructor_exists():
    assert callable(behavioral::actions::IfElse.__init__)


def test_behavioral::actions::ifelse_constructor_args():
    sig = inspect.signature(behavioral::actions::IfElse.__init__)
    params = list(sig.parameters.keys())



def test_statementwithnestedblocks_is_not_abstract():
    assert not inspect.isabstract(StatementWithNestedBlocks)


def test_statementwithnestedblocks_constructor_exists():
    assert callable(StatementWithNestedBlocks.__init__)


def test_statementwithnestedblocks_constructor_args():
    sig = inspect.signature(StatementWithNestedBlocks.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::singleblockstatement_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::SingleBlockStatement)


def test_behavioral::actions::singleblockstatement_constructor_exists():
    assert callable(behavioral::actions::SingleBlockStatement.__init__)


def test_behavioral::actions::singleblockstatement_constructor_args():
    sig = inspect.signature(behavioral::actions::SingleBlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_namedvalue_is_not_abstract():
    assert not inspect.isabstract(NamedValue)


def test_namedvalue_constructor_exists():
    assert callable(NamedValue.__init__)


def test_namedvalue_constructor_args():
    sig = inspect.signature(NamedValue.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::namedvaluewithoptionalinitexpression_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::NamedValueWithOptionalInitExpression)


def test_behavioral::actions::namedvaluewithoptionalinitexpression_constructor_exists():
    assert callable(behavioral::actions::NamedValueWithOptionalInitExpression.__init__)


def test_behavioral::actions::namedvaluewithoptionalinitexpression_constructor_args():
    sig = inspect.signature(behavioral::actions::NamedValueWithOptionalInitExpression.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::iterator_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Iterator)


def test_behavioral::actions::iterator_constructor_exists():
    assert callable(behavioral::actions::Iterator.__init__)


def test_behavioral::actions::iterator_constructor_args():
    sig = inspect.signature(behavioral::actions::Iterator.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::namedvaluedeclaration_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::NamedValueDeclaration)


def test_behavioral::actions::namedvaluedeclaration_constructor_exists():
    assert callable(behavioral::actions::NamedValueDeclaration.__init__)


def test_behavioral::actions::namedvaluedeclaration_constructor_args():
    sig = inspect.signature(behavioral::actions::NamedValueDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::linkmanipulationstatement_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::LinkManipulationStatement)


def test_behavioral::actions::linkmanipulationstatement_constructor_exists():
    assert callable(behavioral::actions::LinkManipulationStatement.__init__)


def test_behavioral::actions::linkmanipulationstatement_constructor_args():
    sig = inspect.signature(behavioral::actions::LinkManipulationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "at" in params, "Missing parameter 'at'"

def test_behavioral::actions::linkmanipulationstatement_has_at():
    assert hasattr(behavioral::actions::LinkManipulationStatement, "at")
    descriptor = None
    for klass in behavioral::actions::LinkManipulationStatement.__mro__:
        if "at" in klass.__dict__:
            descriptor = klass.__dict__["at"]
            break
    assert isinstance(descriptor, property)



def test_behavioral::actions::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::ExpressionStatement)


def test_behavioral::actions::expressionstatement_constructor_exists():
    assert callable(behavioral::actions::ExpressionStatement.__init__)


def test_behavioral::actions::expressionstatement_constructor_args():
    sig = inspect.signature(behavioral::actions::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::statementwithnestedblocks_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::StatementWithNestedBlocks)


def test_behavioral::actions::statementwithnestedblocks_constructor_exists():
    assert callable(behavioral::actions::StatementWithNestedBlocks.__init__)


def test_behavioral::actions::statementwithnestedblocks_constructor_args():
    sig = inspect.signature(behavioral::actions::StatementWithNestedBlocks.__init__)
    params = list(sig.parameters.keys())



def test_classes::inscope_is_not_abstract():
    assert not inspect.isabstract(classes::InScope)


def test_classes::inscope_constructor_exists():
    assert callable(classes::InScope.__init__)


def test_classes::inscope_constructor_args():
    sig = inspect.signature(classes::InScope.__init__)
    params = list(sig.parameters.keys())



def test_classes::functionsignatureimplementation_is_not_abstract():
    assert not inspect.isabstract(classes::FunctionSignatureImplementation)


def test_classes::functionsignatureimplementation_constructor_exists():
    assert callable(classes::FunctionSignatureImplementation.__init__)


def test_classes::functionsignatureimplementation_constructor_args():
    sig = inspect.signature(classes::FunctionSignatureImplementation.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::block_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Block)


def test_behavioral::actions::block_constructor_exists():
    assert callable(behavioral::actions::Block.__init__)


def test_behavioral::actions::block_constructor_args():
    sig = inspect.signature(behavioral::actions::Block.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::businesstasks::taskagent_is_not_abstract():
    assert not inspect.isabstract(behavioral::businesstasks::TaskAgent)


def test_behavioral::businesstasks::taskagent_constructor_exists():
    assert callable(behavioral::businesstasks::TaskAgent.__init__)


def test_behavioral::businesstasks::taskagent_constructor_args():
    sig = inspect.signature(behavioral::businesstasks::TaskAgent.__init__)
    params = list(sig.parameters.keys())



def test_inscope_is_not_abstract():
    assert not inspect.isabstract(InScope)


def test_inscope_constructor_exists():
    assert callable(InScope.__init__)


def test_inscope_constructor_args():
    sig = inspect.signature(InScope.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::statement_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Statement)


def test_behavioral::actions::statement_constructor_exists():
    assert callable(behavioral::actions::Statement.__init__)


def test_behavioral::actions::statement_constructor_args():
    sig = inspect.signature(behavioral::actions::Statement.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_statementwithargument_is_not_abstract():
    assert not inspect.isabstract(StatementWithArgument)


def test_statementwithargument_constructor_exists():
    assert callable(StatementWithArgument.__init__)


def test_statementwithargument_constructor_args():
    sig = inspect.signature(StatementWithArgument.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::return_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Return)


def test_behavioral::actions::return_constructor_exists():
    assert callable(behavioral::actions::Return.__init__)


def test_behavioral::actions::return_constructor_args():
    sig = inspect.signature(behavioral::actions::Return.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::actions::assignment_is_not_abstract():
    assert not inspect.isabstract(behavioral::actions::Assignment)


def test_behavioral::actions::assignment_constructor_exists():
    assert callable(behavioral::actions::Assignment.__init__)


def test_behavioral::actions::assignment_constructor_args():
    sig = inspect.signature(behavioral::actions::Assignment.__init__)
    params = list(sig.parameters.keys())



def test_behavioral::bpdm::dummy_is_not_abstract():
    assert not inspect.isabstract(behavioral::bpdm::Dummy)


def test_behavioral::bpdm::dummy_constructor_exists():
    assert callable(behavioral::bpdm::Dummy.__init__)


def test_behavioral::bpdm::dummy_constructor_args():
    sig = inspect.signature(behavioral::bpdm::Dummy.__init__)
    params = list(sig.parameters.keys())

def test_preconditionkindenum_exists():
    # Check that the Enumeration exists
    assert PreconditionKindEnum is not None

def test_preconditionkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PreconditionKindEnum]
    expected_literals = [
        "NEUTEAL",
        "INHIBIT",
        "ENABLE",
        "REQUIRED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PreconditionKindEnum"

def test_samoperatorkindenum_exists():
    # Check that the Enumeration exists
    assert SAMOperatorKindEnum is not None

def test_samoperatorkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SAMOperatorKindEnum]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SAMOperatorKindEnum"

def test_samderivatorkindenum_exists():
    # Check that the Enumeration exists
    assert SAMDerivatorKindEnum is not None

def test_samderivatorkindenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SAMDerivatorKindEnum]
    expected_literals = [
        "POPULATION",
        "OVERALL",
        "AGGREGATION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SAMDerivatorKindEnum"


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
assembly::Strategy_strategy = st.builds(
    assembly::Strategy,
)
behavioral::assembly::Strategy_strategy = st.builds(
    behavioral::assembly::Strategy,
)
Strategy_strategy = st.builds(
    Strategy,
)
behavioral::assembly::NeutralStrategy_strategy = st.builds(
    behavioral::assembly::NeutralStrategy,
)
behavioral::assembly::InhibitingStrategy_strategy = st.builds(
    behavioral::assembly::InhibitingStrategy,
)
behavioral::assembly::EnablingStrategy_strategy = st.builds(
    behavioral::assembly::EnablingStrategy,
)
behavioral::assembly::RequiredStrategy_strategy = st.builds(
    behavioral::assembly::RequiredStrategy,
)
Operator_strategy = st.builds(
    Operator,
)
behavioral::assembly::OrOperator_strategy = st.builds(
    behavioral::assembly::OrOperator,
)
behavioral::assembly::AndOperator_strategy = st.builds(
    behavioral::assembly::AndOperator,
)
design::AbstractStatusVariable_strategy = st.builds(
    design::AbstractStatusVariable,
)
Connector_strategy = st.builds(
    Connector,
)
behavioral::assembly::Precondition_strategy = st.builds(
    behavioral::assembly::Precondition,
)
behavioral::assembly::Synchroniser_strategy = st.builds(
    behavioral::assembly::Synchroniser,
)
behavioral::assembly::Transition_strategy = st.builds(
    behavioral::assembly::Transition,
)
design::StatusValue_strategy = st.builds(
    design::StatusValue,
)
Signature_strategy = st.builds(
    Signature,
)
design::AbstractAction_strategy = st.builds(
    design::AbstractAction,
)
ConnectableElement_strategy = st.builds(
    ConnectableElement,
)
behavioral::assembly::Operator_strategy = st.builds(
    behavioral::assembly::Operator,
)
assembly::ConnectableElement_strategy = st.builds(
    assembly::ConnectableElement,
)
SchemaElement_strategy = st.builds(
    SchemaElement,
)
behavioral::assembly::ConnectableElement_strategy = st.builds(
    behavioral::assembly::ConnectableElement,
)
behavioral::assembly::Connector_strategy = st.builds(
    behavioral::assembly::Connector,
)
assembly::SchemaElement_strategy = st.builds(
    assembly::SchemaElement,
)
design::BusinessObjectNode_strategy = st.builds(
    design::BusinessObjectNode,
)
behavioral::design::BusinessObject_strategy = st.builds(
    behavioral::design::BusinessObject,
)
design::AbstractStatusValue_strategy = st.builds(
    design::AbstractStatusValue,
)
behavioral::assembly::StatusValueProxy_strategy = st.builds(
    behavioral::assembly::StatusValueProxy,
)
AbstractAction_strategy = st.builds(
    AbstractAction,
)
behavioral::design::Action_strategy = st.builds(
    behavioral::design::Action,
)
AbstractStatusValue_strategy = st.builds(
    AbstractStatusValue,
)
behavioral::design::StatusValue_strategy = st.builds(
    behavioral::design::StatusValue,
)
AbstractStatusVariable_strategy = st.builds(
    AbstractStatusVariable,
)
behavioral::design::StatusVariable_strategy = st.builds(
    behavioral::design::StatusVariable,
)
design::Action_strategy = st.builds(
    design::Action,
)
behavioral::assembly::ActionProxy_strategy = st.builds(
    behavioral::assembly::ActionProxy,
)
design::StatusVariable_strategy = st.builds(
    design::StatusVariable,
)
behavioral::assembly::StatusVariableProxy_strategy = st.builds(
    behavioral::assembly::StatusVariableProxy,
)
SAMDerivator_strategy = st.builds(
    SAMDerivator,
)
behavioral::status::and::action::old::SAMSchemaDerivator_strategy = st.builds(
    behavioral::status::and::action::old::SAMSchemaDerivator,
)
SAMAction_strategy = st.builds(
    SAMAction,
)
behavioral::status::and::action::old::SAMSchemaAction_strategy = st.builds(
    behavioral::status::and::action::old::SAMSchemaAction,
)
SAMStatusSchema_strategy = st.builds(
    SAMStatusSchema,
)
behavioral::status::and::action::old::SAMOperator_strategy = st.builds(
    behavioral::status::and::action::old::SAMOperator,
    kind=
        safe_text
)
behavioral::status::and::action::old::SAMSchemaValue_strategy = st.builds(
    behavioral::status::and::action::old::SAMSchemaValue,
    isInhibiting=
        st.booleans(),
    isInitial=
        st.booleans()
)
behavioral::status::and::action::old::SAMSchemaVariable_strategy = st.builds(
    behavioral::status::and::action::old::SAMSchemaVariable,
    hasStateGuard=
        st.booleans()
)
SAMSchemaValue_strategy = st.builds(
    SAMSchemaValue,
)
behavioral::status::and::action::old::SAMAction_strategy = st.builds(
    behavioral::status::and::action::old::SAMAction,
    name=
        safe_text,
    isAgentAction=
        st.booleans()
)
SAMOperator_strategy = st.builds(
    SAMOperator,
)
behavioral::status::and::action::old::SAMStatusSchema_strategy = st.builds(
    behavioral::status::and::action::old::SAMStatusSchema,
    name=
        safe_text
)
SAMStatusVariable_strategy = st.builds(
    SAMStatusVariable,
)
behavioral::status::and::action::old::SAMStatusValue_strategy = st.builds(
    behavioral::status::and::action::old::SAMStatusValue,
    name=
        safe_text
)
SAMSchemaDerivator_strategy = st.builds(
    SAMSchemaDerivator,
)
behavioral::status::and::action::old::SAMDerivator_strategy = st.builds(
    behavioral::status::and::action::old::SAMDerivator,
    kind=
        safe_text
)
SAMSchemaVariable_strategy = st.builds(
    SAMSchemaVariable,
)
SAMStatusValue_strategy = st.builds(
    SAMStatusValue,
)
behavioral::status::and::action::old::SAMStatusVariable_strategy = st.builds(
    behavioral::status::and::action::old::SAMStatusVariable,
    name=
        safe_text,
    isAgentVariable=
        st.booleans()
)
SAMSchemaAction_strategy = st.builds(
    SAMSchemaAction,
)
behavioral::transactions::Dummy_strategy = st.builds(
    behavioral::transactions::Dummy,
)
behavioral::events::EventFilter_strategy = st.builds(
    behavioral::events::EventFilter,
)
MethodSignature_strategy = st.builds(
    MethodSignature,
)
Subscription_strategy = st.builds(
    Subscription,
)
behavioral::events::EventProducer_strategy = st.builds(
    behavioral::events::EventProducer,
)
SapClass_strategy = st.builds(
    SapClass,
)
EventFilter_strategy = st.builds(
    EventFilter,
)
EventProducer_strategy = st.builds(
    EventProducer,
)
DimensionDefinition_strategy = st.builds(
    DimensionDefinition,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
behavioral::design::AbstractStatusVariable_strategy = st.builds(
    behavioral::design::AbstractStatusVariable,
    isStateGuarded=
        st.booleans(),
    isAgent=
        st.booleans()
)
behavioral::design::AbstractAction_strategy = st.builds(
    behavioral::design::AbstractAction,
    isPreconditionFixed=
        st.booleans(),
    isAgent=
        st.booleans()
)
behavioral::design::AbstractStatusValue_strategy = st.builds(
    behavioral::design::AbstractStatusValue,
    isStateGuarded=
        st.booleans(),
    isInitial=
        st.booleans(),
    isInhibiting=
        st.booleans()
)
behavioral::design::BusinessObjectNode_strategy = st.builds(
    behavioral::design::BusinessObjectNode,
)
behavioral::assembly::StatusSchema_strategy = st.builds(
    behavioral::assembly::StatusSchema,
)
behavioral::assembly::SchemaElement_strategy = st.builds(
    behavioral::assembly::SchemaElement,
)
behavioral::events::Subscription_strategy = st.builds(
    behavioral::events::Subscription,
)
behavioral::rules::Dummy_strategy = st.builds(
    behavioral::rules::Dummy,
)
expressions::Conditional_strategy = st.builds(
    expressions::Conditional,
)
NamedValueDeclaration_strategy = st.builds(
    NamedValueDeclaration,
)
expressions::WithArgument_strategy = st.builds(
    expressions::WithArgument,
)
actions::Statement_strategy = st.builds(
    actions::Statement,
)
behavioral::actions::ConditionalStatement_strategy = st.builds(
    behavioral::actions::ConditionalStatement,
)
behavioral::actions::StatementWithArgument_strategy = st.builds(
    behavioral::actions::StatementWithArgument,
)
Association_strategy = st.builds(
    Association,
)
GroupBy_strategy = st.builds(
    GroupBy,
)
FromClause_strategy = st.builds(
    FromClause,
)
Selection_strategy = st.builds(
    Selection,
)
Foreach_strategy = st.builds(
    Foreach,
)
Assignment_strategy = st.builds(
    Assignment,
)
collectionexpressions::Iterate_strategy = st.builds(
    collectionexpressions::Iterate,
)
NamedValueWithOptionalInitExpression_strategy = st.builds(
    NamedValueWithOptionalInitExpression,
)
behavioral::actions::Variable_strategy = st.builds(
    behavioral::actions::Variable,
)
behavioral::actions::Constant_strategy = st.builds(
    behavioral::actions::Constant,
)
behavioral::actions::QueryInvocation_strategy = st.builds(
    behavioral::actions::QueryInvocation,
)
behavioral::actions::Sort_strategy = st.builds(
    behavioral::actions::Sort,
)
LinkManipulationStatement_strategy = st.builds(
    LinkManipulationStatement,
)
behavioral::actions::RemoveLink_strategy = st.builds(
    behavioral::actions::RemoveLink,
)
behavioral::actions::AddLink_strategy = st.builds(
    behavioral::actions::AddLink,
)
Iterator_strategy = st.builds(
    Iterator,
)
Expression_strategy = st.builds(
    Expression,
)
SingleBlockStatement_strategy = st.builds(
    SingleBlockStatement,
)
behavioral::actions::Foreach_strategy = st.builds(
    behavioral::actions::Foreach,
    parallel=
        st.booleans()
)
actions::SingleBlockStatement_strategy = st.builds(
    actions::SingleBlockStatement,
)
Block_strategy = st.builds(
    Block,
)
actions::StatementWithNestedBlocks_strategy = st.builds(
    actions::StatementWithNestedBlocks,
)
actions::ConditionalStatement_strategy = st.builds(
    actions::ConditionalStatement,
)
behavioral::actions::WhileLoop_strategy = st.builds(
    behavioral::actions::WhileLoop,
)
behavioral::actions::IfElse_strategy = st.builds(
    behavioral::actions::IfElse,
)
StatementWithNestedBlocks_strategy = st.builds(
    StatementWithNestedBlocks,
)
behavioral::actions::SingleBlockStatement_strategy = st.builds(
    behavioral::actions::SingleBlockStatement,
)
NamedValue_strategy = st.builds(
    NamedValue,
)
behavioral::actions::NamedValueWithOptionalInitExpression_strategy = st.builds(
    behavioral::actions::NamedValueWithOptionalInitExpression,
)
behavioral::actions::Iterator_strategy = st.builds(
    behavioral::actions::Iterator,
)
Statement_strategy = st.builds(
    Statement,
)
behavioral::actions::NamedValueDeclaration_strategy = st.builds(
    behavioral::actions::NamedValueDeclaration,
)
behavioral::actions::LinkManipulationStatement_strategy = st.builds(
    behavioral::actions::LinkManipulationStatement,
    at=
        st.integers()
)
behavioral::actions::ExpressionStatement_strategy = st.builds(
    behavioral::actions::ExpressionStatement,
)
behavioral::actions::StatementWithNestedBlocks_strategy = st.builds(
    behavioral::actions::StatementWithNestedBlocks,
)
classes::InScope_strategy = st.builds(
    classes::InScope,
)
classes::FunctionSignatureImplementation_strategy = st.builds(
    classes::FunctionSignatureImplementation,
)
behavioral::actions::Block_strategy = st.builds(
    behavioral::actions::Block,
)
behavioral::businesstasks::TaskAgent_strategy = st.builds(
    behavioral::businesstasks::TaskAgent,
)
InScope_strategy = st.builds(
    InScope,
)
behavioral::actions::Statement_strategy = st.builds(
    behavioral::actions::Statement,
)
Variable_strategy = st.builds(
    Variable,
)
StatementWithArgument_strategy = st.builds(
    StatementWithArgument,
)
behavioral::actions::Return_strategy = st.builds(
    behavioral::actions::Return,
)
behavioral::actions::Assignment_strategy = st.builds(
    behavioral::actions::Assignment,
)
behavioral::bpdm::Dummy_strategy = st.builds(
    behavioral::bpdm::Dummy,
)

@given(instance=assembly::Strategy_strategy)
@settings(max_examples=50)
def test_assembly::strategy_instantiation(instance):
    assert isinstance(instance, assembly::Strategy)

@given(instance=behavioral::assembly::Strategy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::strategy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Strategy)

@given(instance=Strategy_strategy)
@settings(max_examples=50)
def test_strategy_instantiation(instance):
    assert isinstance(instance, Strategy)

@given(instance=behavioral::assembly::NeutralStrategy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::neutralstrategy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::NeutralStrategy)

@given(instance=behavioral::assembly::InhibitingStrategy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::inhibitingstrategy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::InhibitingStrategy)

@given(instance=behavioral::assembly::EnablingStrategy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::enablingstrategy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::EnablingStrategy)

@given(instance=behavioral::assembly::RequiredStrategy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::requiredstrategy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::RequiredStrategy)

@given(instance=Operator_strategy)
@settings(max_examples=50)
def test_operator_instantiation(instance):
    assert isinstance(instance, Operator)

@given(instance=behavioral::assembly::OrOperator_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::oroperator_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::OrOperator)

@given(instance=behavioral::assembly::AndOperator_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::andoperator_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::AndOperator)

@given(instance=design::AbstractStatusVariable_strategy)
@settings(max_examples=50)
def test_design::abstractstatusvariable_instantiation(instance):
    assert isinstance(instance, design::AbstractStatusVariable)

@given(instance=Connector_strategy)
@settings(max_examples=50)
def test_connector_instantiation(instance):
    assert isinstance(instance, Connector)

@given(instance=behavioral::assembly::Precondition_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::precondition_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Precondition)

@given(instance=behavioral::assembly::Synchroniser_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::synchroniser_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Synchroniser)

@given(instance=behavioral::assembly::Transition_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::transition_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Transition)

@given(instance=design::StatusValue_strategy)
@settings(max_examples=50)
def test_design::statusvalue_instantiation(instance):
    assert isinstance(instance, design::StatusValue)

@given(instance=Signature_strategy)
@settings(max_examples=50)
def test_signature_instantiation(instance):
    assert isinstance(instance, Signature)

@given(instance=design::AbstractAction_strategy)
@settings(max_examples=50)
def test_design::abstractaction_instantiation(instance):
    assert isinstance(instance, design::AbstractAction)

@given(instance=ConnectableElement_strategy)
@settings(max_examples=50)
def test_connectableelement_instantiation(instance):
    assert isinstance(instance, ConnectableElement)

@given(instance=behavioral::assembly::Operator_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::operator_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Operator)

@given(instance=assembly::ConnectableElement_strategy)
@settings(max_examples=50)
def test_assembly::connectableelement_instantiation(instance):
    assert isinstance(instance, assembly::ConnectableElement)

@given(instance=SchemaElement_strategy)
@settings(max_examples=50)
def test_schemaelement_instantiation(instance):
    assert isinstance(instance, SchemaElement)

@given(instance=behavioral::assembly::ConnectableElement_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::connectableelement_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::ConnectableElement)

@given(instance=behavioral::assembly::Connector_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::connector_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::Connector)

@given(instance=assembly::SchemaElement_strategy)
@settings(max_examples=50)
def test_assembly::schemaelement_instantiation(instance):
    assert isinstance(instance, assembly::SchemaElement)

@given(instance=design::BusinessObjectNode_strategy)
@settings(max_examples=50)
def test_design::businessobjectnode_instantiation(instance):
    assert isinstance(instance, design::BusinessObjectNode)

@given(instance=behavioral::design::BusinessObject_strategy)
@settings(max_examples=50)
def test_behavioral::design::businessobject_instantiation(instance):
    assert isinstance(instance, behavioral::design::BusinessObject)

@given(instance=design::AbstractStatusValue_strategy)
@settings(max_examples=50)
def test_design::abstractstatusvalue_instantiation(instance):
    assert isinstance(instance, design::AbstractStatusValue)

@given(instance=behavioral::assembly::StatusValueProxy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::statusvalueproxy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::StatusValueProxy)

@given(instance=AbstractAction_strategy)
@settings(max_examples=50)
def test_abstractaction_instantiation(instance):
    assert isinstance(instance, AbstractAction)

@given(instance=behavioral::design::Action_strategy)
@settings(max_examples=50)
def test_behavioral::design::action_instantiation(instance):
    assert isinstance(instance, behavioral::design::Action)

@given(instance=AbstractStatusValue_strategy)
@settings(max_examples=50)
def test_abstractstatusvalue_instantiation(instance):
    assert isinstance(instance, AbstractStatusValue)

@given(instance=behavioral::design::StatusValue_strategy)
@settings(max_examples=50)
def test_behavioral::design::statusvalue_instantiation(instance):
    assert isinstance(instance, behavioral::design::StatusValue)

@given(instance=AbstractStatusVariable_strategy)
@settings(max_examples=50)
def test_abstractstatusvariable_instantiation(instance):
    assert isinstance(instance, AbstractStatusVariable)

@given(instance=behavioral::design::StatusVariable_strategy)
@settings(max_examples=50)
def test_behavioral::design::statusvariable_instantiation(instance):
    assert isinstance(instance, behavioral::design::StatusVariable)

@given(instance=design::Action_strategy)
@settings(max_examples=50)
def test_design::action_instantiation(instance):
    assert isinstance(instance, design::Action)

@given(instance=behavioral::assembly::ActionProxy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::actionproxy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::ActionProxy)

@given(instance=design::StatusVariable_strategy)
@settings(max_examples=50)
def test_design::statusvariable_instantiation(instance):
    assert isinstance(instance, design::StatusVariable)

@given(instance=behavioral::assembly::StatusVariableProxy_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::statusvariableproxy_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::StatusVariableProxy)

@given(instance=SAMDerivator_strategy)
@settings(max_examples=50)
def test_samderivator_instantiation(instance):
    assert isinstance(instance, SAMDerivator)

@given(instance=behavioral::status::and::action::old::SAMSchemaDerivator_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samschemaderivator_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMSchemaDerivator)

@given(instance=SAMAction_strategy)
@settings(max_examples=50)
def test_samaction_instantiation(instance):
    assert isinstance(instance, SAMAction)

@given(instance=behavioral::status::and::action::old::SAMSchemaAction_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samschemaaction_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMSchemaAction)

@given(instance=SAMStatusSchema_strategy)
@settings(max_examples=50)
def test_samstatusschema_instantiation(instance):
    assert isinstance(instance, SAMStatusSchema)

@given(instance=behavioral::status::and::action::old::SAMOperator_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samoperator_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMOperator)

@given(instance=behavioral::status::and::action::old::SAMOperator_strategy)
def test_behavioral::status::and::action::old::samoperator_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=behavioral::status::and::action::old::SAMOperator_strategy)
def test_behavioral::status::and::action::old::samoperator_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=behavioral::status::and::action::old::SAMSchemaValue_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samschemavalue_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMSchemaValue)

@given(instance=behavioral::status::and::action::old::SAMSchemaValue_strategy)
def test_behavioral::status::and::action::old::samschemavalue_isInhibiting_type(instance):
    assert isinstance(instance.isInhibiting, bool)


@given(instance=behavioral::status::and::action::old::SAMSchemaValue_strategy)
def test_behavioral::status::and::action::old::samschemavalue_isInhibiting_setter(instance):
    original = instance.isInhibiting
    instance.isInhibiting = original
    assert instance.isInhibiting == original

@given(instance=behavioral::status::and::action::old::SAMSchemaValue_strategy)
def test_behavioral::status::and::action::old::samschemavalue_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=behavioral::status::and::action::old::SAMSchemaValue_strategy)
def test_behavioral::status::and::action::old::samschemavalue_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=behavioral::status::and::action::old::SAMSchemaVariable_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samschemavariable_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMSchemaVariable)

@given(instance=behavioral::status::and::action::old::SAMSchemaVariable_strategy)
def test_behavioral::status::and::action::old::samschemavariable_hasStateGuard_type(instance):
    assert isinstance(instance.hasStateGuard, bool)


@given(instance=behavioral::status::and::action::old::SAMSchemaVariable_strategy)
def test_behavioral::status::and::action::old::samschemavariable_hasStateGuard_setter(instance):
    original = instance.hasStateGuard
    instance.hasStateGuard = original
    assert instance.hasStateGuard == original

@given(instance=SAMSchemaValue_strategy)
@settings(max_examples=50)
def test_samschemavalue_instantiation(instance):
    assert isinstance(instance, SAMSchemaValue)

@given(instance=behavioral::status::and::action::old::SAMAction_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samaction_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMAction)

@given(instance=behavioral::status::and::action::old::SAMAction_strategy)
def test_behavioral::status::and::action::old::samaction_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behavioral::status::and::action::old::SAMAction_strategy)
def test_behavioral::status::and::action::old::samaction_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=behavioral::status::and::action::old::SAMAction_strategy)
def test_behavioral::status::and::action::old::samaction_isAgentAction_type(instance):
    assert isinstance(instance.isAgentAction, bool)


@given(instance=behavioral::status::and::action::old::SAMAction_strategy)
def test_behavioral::status::and::action::old::samaction_isAgentAction_setter(instance):
    original = instance.isAgentAction
    instance.isAgentAction = original
    assert instance.isAgentAction == original

@given(instance=SAMOperator_strategy)
@settings(max_examples=50)
def test_samoperator_instantiation(instance):
    assert isinstance(instance, SAMOperator)

@given(instance=behavioral::status::and::action::old::SAMStatusSchema_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samstatusschema_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMStatusSchema)

@given(instance=behavioral::status::and::action::old::SAMStatusSchema_strategy)
def test_behavioral::status::and::action::old::samstatusschema_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behavioral::status::and::action::old::SAMStatusSchema_strategy)
def test_behavioral::status::and::action::old::samstatusschema_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SAMStatusVariable_strategy)
@settings(max_examples=50)
def test_samstatusvariable_instantiation(instance):
    assert isinstance(instance, SAMStatusVariable)

@given(instance=behavioral::status::and::action::old::SAMStatusValue_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samstatusvalue_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMStatusValue)

@given(instance=behavioral::status::and::action::old::SAMStatusValue_strategy)
def test_behavioral::status::and::action::old::samstatusvalue_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behavioral::status::and::action::old::SAMStatusValue_strategy)
def test_behavioral::status::and::action::old::samstatusvalue_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=SAMSchemaDerivator_strategy)
@settings(max_examples=50)
def test_samschemaderivator_instantiation(instance):
    assert isinstance(instance, SAMSchemaDerivator)

@given(instance=behavioral::status::and::action::old::SAMDerivator_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samderivator_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMDerivator)

@given(instance=behavioral::status::and::action::old::SAMDerivator_strategy)
def test_behavioral::status::and::action::old::samderivator_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=behavioral::status::and::action::old::SAMDerivator_strategy)
def test_behavioral::status::and::action::old::samderivator_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=SAMSchemaVariable_strategy)
@settings(max_examples=50)
def test_samschemavariable_instantiation(instance):
    assert isinstance(instance, SAMSchemaVariable)

@given(instance=SAMStatusValue_strategy)
@settings(max_examples=50)
def test_samstatusvalue_instantiation(instance):
    assert isinstance(instance, SAMStatusValue)

@given(instance=behavioral::status::and::action::old::SAMStatusVariable_strategy)
@settings(max_examples=50)
def test_behavioral::status::and::action::old::samstatusvariable_instantiation(instance):
    assert isinstance(instance, behavioral::status::and::action::old::SAMStatusVariable)

@given(instance=behavioral::status::and::action::old::SAMStatusVariable_strategy)
def test_behavioral::status::and::action::old::samstatusvariable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behavioral::status::and::action::old::SAMStatusVariable_strategy)
def test_behavioral::status::and::action::old::samstatusvariable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=behavioral::status::and::action::old::SAMStatusVariable_strategy)
def test_behavioral::status::and::action::old::samstatusvariable_isAgentVariable_type(instance):
    assert isinstance(instance.isAgentVariable, bool)


@given(instance=behavioral::status::and::action::old::SAMStatusVariable_strategy)
def test_behavioral::status::and::action::old::samstatusvariable_isAgentVariable_setter(instance):
    original = instance.isAgentVariable
    instance.isAgentVariable = original
    assert instance.isAgentVariable == original

@given(instance=SAMSchemaAction_strategy)
@settings(max_examples=50)
def test_samschemaaction_instantiation(instance):
    assert isinstance(instance, SAMSchemaAction)

@given(instance=behavioral::transactions::Dummy_strategy)
@settings(max_examples=50)
def test_behavioral::transactions::dummy_instantiation(instance):
    assert isinstance(instance, behavioral::transactions::Dummy)

@given(instance=behavioral::events::EventFilter_strategy)
@settings(max_examples=50)
def test_behavioral::events::eventfilter_instantiation(instance):
    assert isinstance(instance, behavioral::events::EventFilter)

@given(instance=MethodSignature_strategy)
@settings(max_examples=50)
def test_methodsignature_instantiation(instance):
    assert isinstance(instance, MethodSignature)

@given(instance=Subscription_strategy)
@settings(max_examples=50)
def test_subscription_instantiation(instance):
    assert isinstance(instance, Subscription)

@given(instance=behavioral::events::EventProducer_strategy)
@settings(max_examples=50)
def test_behavioral::events::eventproducer_instantiation(instance):
    assert isinstance(instance, behavioral::events::EventProducer)

@given(instance=SapClass_strategy)
@settings(max_examples=50)
def test_sapclass_instantiation(instance):
    assert isinstance(instance, SapClass)

@given(instance=EventFilter_strategy)
@settings(max_examples=50)
def test_eventfilter_instantiation(instance):
    assert isinstance(instance, EventFilter)

@given(instance=EventProducer_strategy)
@settings(max_examples=50)
def test_eventproducer_instantiation(instance):
    assert isinstance(instance, EventProducer)

@given(instance=DimensionDefinition_strategy)
@settings(max_examples=50)
def test_dimensiondefinition_instantiation(instance):
    assert isinstance(instance, DimensionDefinition)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=behavioral::design::AbstractStatusVariable_strategy)
@settings(max_examples=50)
def test_behavioral::design::abstractstatusvariable_instantiation(instance):
    assert isinstance(instance, behavioral::design::AbstractStatusVariable)

@given(instance=behavioral::design::AbstractStatusVariable_strategy)
def test_behavioral::design::abstractstatusvariable_isStateGuarded_type(instance):
    assert isinstance(instance.isStateGuarded, bool)


@given(instance=behavioral::design::AbstractStatusVariable_strategy)
def test_behavioral::design::abstractstatusvariable_isStateGuarded_setter(instance):
    original = instance.isStateGuarded
    instance.isStateGuarded = original
    assert instance.isStateGuarded == original

@given(instance=behavioral::design::AbstractStatusVariable_strategy)
def test_behavioral::design::abstractstatusvariable_isAgent_type(instance):
    assert isinstance(instance.isAgent, bool)


@given(instance=behavioral::design::AbstractStatusVariable_strategy)
def test_behavioral::design::abstractstatusvariable_isAgent_setter(instance):
    original = instance.isAgent
    instance.isAgent = original
    assert instance.isAgent == original

@given(instance=behavioral::design::AbstractAction_strategy)
@settings(max_examples=50)
def test_behavioral::design::abstractaction_instantiation(instance):
    assert isinstance(instance, behavioral::design::AbstractAction)

@given(instance=behavioral::design::AbstractAction_strategy)
def test_behavioral::design::abstractaction_isPreconditionFixed_type(instance):
    assert isinstance(instance.isPreconditionFixed, bool)


@given(instance=behavioral::design::AbstractAction_strategy)
def test_behavioral::design::abstractaction_isPreconditionFixed_setter(instance):
    original = instance.isPreconditionFixed
    instance.isPreconditionFixed = original
    assert instance.isPreconditionFixed == original

@given(instance=behavioral::design::AbstractAction_strategy)
def test_behavioral::design::abstractaction_isAgent_type(instance):
    assert isinstance(instance.isAgent, bool)


@given(instance=behavioral::design::AbstractAction_strategy)
def test_behavioral::design::abstractaction_isAgent_setter(instance):
    original = instance.isAgent
    instance.isAgent = original
    assert instance.isAgent == original

@given(instance=behavioral::design::AbstractStatusValue_strategy)
@settings(max_examples=50)
def test_behavioral::design::abstractstatusvalue_instantiation(instance):
    assert isinstance(instance, behavioral::design::AbstractStatusValue)

@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isStateGuarded_type(instance):
    assert isinstance(instance.isStateGuarded, bool)


@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isStateGuarded_setter(instance):
    original = instance.isStateGuarded
    instance.isStateGuarded = original
    assert instance.isStateGuarded == original

@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isInitial_type(instance):
    assert isinstance(instance.isInitial, bool)


@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isInitial_setter(instance):
    original = instance.isInitial
    instance.isInitial = original
    assert instance.isInitial == original

@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isInhibiting_type(instance):
    assert isinstance(instance.isInhibiting, bool)


@given(instance=behavioral::design::AbstractStatusValue_strategy)
def test_behavioral::design::abstractstatusvalue_isInhibiting_setter(instance):
    original = instance.isInhibiting
    instance.isInhibiting = original
    assert instance.isInhibiting == original

@given(instance=behavioral::design::BusinessObjectNode_strategy)
@settings(max_examples=50)
def test_behavioral::design::businessobjectnode_instantiation(instance):
    assert isinstance(instance, behavioral::design::BusinessObjectNode)

@given(instance=behavioral::assembly::StatusSchema_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::statusschema_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::StatusSchema)

@given(instance=behavioral::assembly::SchemaElement_strategy)
@settings(max_examples=50)
def test_behavioral::assembly::schemaelement_instantiation(instance):
    assert isinstance(instance, behavioral::assembly::SchemaElement)

@given(instance=behavioral::events::Subscription_strategy)
@settings(max_examples=50)
def test_behavioral::events::subscription_instantiation(instance):
    assert isinstance(instance, behavioral::events::Subscription)

@given(instance=behavioral::rules::Dummy_strategy)
@settings(max_examples=50)
def test_behavioral::rules::dummy_instantiation(instance):
    assert isinstance(instance, behavioral::rules::Dummy)

@given(instance=expressions::Conditional_strategy)
@settings(max_examples=50)
def test_expressions::conditional_instantiation(instance):
    assert isinstance(instance, expressions::Conditional)

@given(instance=NamedValueDeclaration_strategy)
@settings(max_examples=50)
def test_namedvaluedeclaration_instantiation(instance):
    assert isinstance(instance, NamedValueDeclaration)

@given(instance=expressions::WithArgument_strategy)
@settings(max_examples=50)
def test_expressions::withargument_instantiation(instance):
    assert isinstance(instance, expressions::WithArgument)

@given(instance=actions::Statement_strategy)
@settings(max_examples=50)
def test_actions::statement_instantiation(instance):
    assert isinstance(instance, actions::Statement)

@given(instance=behavioral::actions::ConditionalStatement_strategy)
@settings(max_examples=50)
def test_behavioral::actions::conditionalstatement_instantiation(instance):
    assert isinstance(instance, behavioral::actions::ConditionalStatement)

@given(instance=behavioral::actions::StatementWithArgument_strategy)
@settings(max_examples=50)
def test_behavioral::actions::statementwithargument_instantiation(instance):
    assert isinstance(instance, behavioral::actions::StatementWithArgument)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=GroupBy_strategy)
@settings(max_examples=50)
def test_groupby_instantiation(instance):
    assert isinstance(instance, GroupBy)

@given(instance=FromClause_strategy)
@settings(max_examples=50)
def test_fromclause_instantiation(instance):
    assert isinstance(instance, FromClause)

@given(instance=Selection_strategy)
@settings(max_examples=50)
def test_selection_instantiation(instance):
    assert isinstance(instance, Selection)

@given(instance=Foreach_strategy)
@settings(max_examples=50)
def test_foreach_instantiation(instance):
    assert isinstance(instance, Foreach)

@given(instance=Assignment_strategy)
@settings(max_examples=50)
def test_assignment_instantiation(instance):
    assert isinstance(instance, Assignment)

@given(instance=collectionexpressions::Iterate_strategy)
@settings(max_examples=50)
def test_collectionexpressions::iterate_instantiation(instance):
    assert isinstance(instance, collectionexpressions::Iterate)

@given(instance=NamedValueWithOptionalInitExpression_strategy)
@settings(max_examples=50)
def test_namedvaluewithoptionalinitexpression_instantiation(instance):
    assert isinstance(instance, NamedValueWithOptionalInitExpression)

@given(instance=behavioral::actions::Variable_strategy)
@settings(max_examples=50)
def test_behavioral::actions::variable_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Variable)

@given(instance=behavioral::actions::Constant_strategy)
@settings(max_examples=50)
def test_behavioral::actions::constant_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Constant)

@given(instance=behavioral::actions::QueryInvocation_strategy)
@settings(max_examples=50)
def test_behavioral::actions::queryinvocation_instantiation(instance):
    assert isinstance(instance, behavioral::actions::QueryInvocation)

@given(instance=behavioral::actions::Sort_strategy)
@settings(max_examples=50)
def test_behavioral::actions::sort_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Sort)

@given(instance=LinkManipulationStatement_strategy)
@settings(max_examples=50)
def test_linkmanipulationstatement_instantiation(instance):
    assert isinstance(instance, LinkManipulationStatement)

@given(instance=behavioral::actions::RemoveLink_strategy)
@settings(max_examples=50)
def test_behavioral::actions::removelink_instantiation(instance):
    assert isinstance(instance, behavioral::actions::RemoveLink)

@given(instance=behavioral::actions::AddLink_strategy)
@settings(max_examples=50)
def test_behavioral::actions::addlink_instantiation(instance):
    assert isinstance(instance, behavioral::actions::AddLink)

@given(instance=Iterator_strategy)
@settings(max_examples=50)
def test_iterator_instantiation(instance):
    assert isinstance(instance, Iterator)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=SingleBlockStatement_strategy)
@settings(max_examples=50)
def test_singleblockstatement_instantiation(instance):
    assert isinstance(instance, SingleBlockStatement)

@given(instance=behavioral::actions::Foreach_strategy)
@settings(max_examples=50)
def test_behavioral::actions::foreach_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Foreach)

@given(instance=behavioral::actions::Foreach_strategy)
def test_behavioral::actions::foreach_parallel_type(instance):
    assert isinstance(instance.parallel, bool)


@given(instance=behavioral::actions::Foreach_strategy)
def test_behavioral::actions::foreach_parallel_setter(instance):
    original = instance.parallel
    instance.parallel = original
    assert instance.parallel == original

@given(instance=actions::SingleBlockStatement_strategy)
@settings(max_examples=50)
def test_actions::singleblockstatement_instantiation(instance):
    assert isinstance(instance, actions::SingleBlockStatement)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=actions::StatementWithNestedBlocks_strategy)
@settings(max_examples=50)
def test_actions::statementwithnestedblocks_instantiation(instance):
    assert isinstance(instance, actions::StatementWithNestedBlocks)

@given(instance=actions::ConditionalStatement_strategy)
@settings(max_examples=50)
def test_actions::conditionalstatement_instantiation(instance):
    assert isinstance(instance, actions::ConditionalStatement)

@given(instance=behavioral::actions::WhileLoop_strategy)
@settings(max_examples=50)
def test_behavioral::actions::whileloop_instantiation(instance):
    assert isinstance(instance, behavioral::actions::WhileLoop)

@given(instance=behavioral::actions::IfElse_strategy)
@settings(max_examples=50)
def test_behavioral::actions::ifelse_instantiation(instance):
    assert isinstance(instance, behavioral::actions::IfElse)

@given(instance=StatementWithNestedBlocks_strategy)
@settings(max_examples=50)
def test_statementwithnestedblocks_instantiation(instance):
    assert isinstance(instance, StatementWithNestedBlocks)

@given(instance=behavioral::actions::SingleBlockStatement_strategy)
@settings(max_examples=50)
def test_behavioral::actions::singleblockstatement_instantiation(instance):
    assert isinstance(instance, behavioral::actions::SingleBlockStatement)

@given(instance=NamedValue_strategy)
@settings(max_examples=50)
def test_namedvalue_instantiation(instance):
    assert isinstance(instance, NamedValue)

@given(instance=behavioral::actions::NamedValueWithOptionalInitExpression_strategy)
@settings(max_examples=50)
def test_behavioral::actions::namedvaluewithoptionalinitexpression_instantiation(instance):
    assert isinstance(instance, behavioral::actions::NamedValueWithOptionalInitExpression)

@given(instance=behavioral::actions::Iterator_strategy)
@settings(max_examples=50)
def test_behavioral::actions::iterator_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Iterator)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=behavioral::actions::NamedValueDeclaration_strategy)
@settings(max_examples=50)
def test_behavioral::actions::namedvaluedeclaration_instantiation(instance):
    assert isinstance(instance, behavioral::actions::NamedValueDeclaration)

@given(instance=behavioral::actions::LinkManipulationStatement_strategy)
@settings(max_examples=50)
def test_behavioral::actions::linkmanipulationstatement_instantiation(instance):
    assert isinstance(instance, behavioral::actions::LinkManipulationStatement)

@given(instance=behavioral::actions::LinkManipulationStatement_strategy)
def test_behavioral::actions::linkmanipulationstatement_at_type(instance):
    assert isinstance(instance.at, int)


@given(instance=behavioral::actions::LinkManipulationStatement_strategy)
def test_behavioral::actions::linkmanipulationstatement_at_setter(instance):
    original = instance.at
    instance.at = original
    assert instance.at == original

@given(instance=behavioral::actions::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_behavioral::actions::expressionstatement_instantiation(instance):
    assert isinstance(instance, behavioral::actions::ExpressionStatement)

@given(instance=behavioral::actions::StatementWithNestedBlocks_strategy)
@settings(max_examples=50)
def test_behavioral::actions::statementwithnestedblocks_instantiation(instance):
    assert isinstance(instance, behavioral::actions::StatementWithNestedBlocks)

@given(instance=classes::InScope_strategy)
@settings(max_examples=50)
def test_classes::inscope_instantiation(instance):
    assert isinstance(instance, classes::InScope)

@given(instance=classes::FunctionSignatureImplementation_strategy)
@settings(max_examples=50)
def test_classes::functionsignatureimplementation_instantiation(instance):
    assert isinstance(instance, classes::FunctionSignatureImplementation)

@given(instance=behavioral::actions::Block_strategy)
@settings(max_examples=50)
def test_behavioral::actions::block_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Block)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=behavioral::actions::Block_strategy)
@settings(max_examples=30)
def test_behavioral::actions::block_localissideeffectfree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.localIsSideEffectFree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.localIsSideEffectFree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'localIsSideEffectFree' in behavioral::actions::Block is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'localIsSideEffectFree' in behavioral::actions::Block did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'localIsSideEffectFree' in behavioral::actions::Block is not implemented or raised an error")

@given(instance=behavioral::businesstasks::TaskAgent_strategy)
@settings(max_examples=50)
def test_behavioral::businesstasks::taskagent_instantiation(instance):
    assert isinstance(instance, behavioral::businesstasks::TaskAgent)

@given(instance=InScope_strategy)
@settings(max_examples=50)
def test_inscope_instantiation(instance):
    assert isinstance(instance, InScope)

@given(instance=behavioral::actions::Statement_strategy)
@settings(max_examples=50)
def test_behavioral::actions::statement_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Statement)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=behavioral::actions::Statement_strategy)
@settings(max_examples=30)
def test_behavioral::actions::statement_issideeffectfreeforblock_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSideEffectFreeForBlock(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSideEffectFreeForBlock).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSideEffectFreeForBlock' in behavioral::actions::Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSideEffectFreeForBlock' in behavioral::actions::Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSideEffectFreeForBlock' in behavioral::actions::Statement is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=behavioral::actions::Statement_strategy)
@settings(max_examples=30)
def test_behavioral::actions::statement_issideeffectfree_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.isSideEffectFree()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.isSideEffectFree).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'isSideEffectFree' in behavioral::actions::Statement is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'isSideEffectFree' in behavioral::actions::Statement did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'isSideEffectFree' in behavioral::actions::Statement is not implemented or raised an error")

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=StatementWithArgument_strategy)
@settings(max_examples=50)
def test_statementwithargument_instantiation(instance):
    assert isinstance(instance, StatementWithArgument)

@given(instance=behavioral::actions::Return_strategy)
@settings(max_examples=50)
def test_behavioral::actions::return_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Return)

@given(instance=behavioral::actions::Assignment_strategy)
@settings(max_examples=50)
def test_behavioral::actions::assignment_instantiation(instance):
    assert isinstance(instance, behavioral::actions::Assignment)

@given(instance=behavioral::bpdm::Dummy_strategy)
@settings(max_examples=50)
def test_behavioral::bpdm::dummy_instantiation(instance):
    assert isinstance(instance, behavioral::bpdm::Dummy)
