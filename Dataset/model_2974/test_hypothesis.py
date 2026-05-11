import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    OpType,
    restbehavior::OpType,
    restbehavior::BinOpType,
    Operation,
    restbehavior::BinaryOperation,
    restbehavior::ExternalLink,
    State,
    restbehavior::DeletedState,
    restbehavior::MediaTypeElement,
    restbehavior::MediaTypeLink,
    MTReference,
    restbehavior::MtElementReference,
    restbehavior::MTLinkReference,
    Reference,
    restbehavior::MTReference,
    restbehavior::InternalLink,
    restbehavior::Attribute,
    WritableReference,
    restbehavior::AttributeReference,
    restbehavior::InternalLinkReference,
    restbehavior::ExternalLinkReference,
    Action,
    restbehavior::CreateAction,
    restbehavior::ListAddAction,
    restbehavior::ListRemoveAction,
    restbehavior::ActionSequence,
    restbehavior::ConditionalAction,
    restbehavior::MessageAction,
    Trigger,
    restbehavior::InternalMessage,
    restbehavior::DataType,
    Value,
    restbehavior::Operation,
    restbehavior::Reference,
    restbehavior::Constant,
    restbehavior::Representation,
    restbehavior::Metadata,
    restbehavior::StatusCode,
    restbehavior::ReturnAction,
    restbehavior::WritableReference,
    restbehavior::UpdateAction,
    restbehavior::Action,
    restbehavior::BehaviorSpecification,
    restbehavior::Parameter,
    restbehavior::MediaType,
    restbehavior::Creator,
    restbehavior::Value,
    restbehavior::Condition,
    restbehavior::Trigger,
    restbehavior::Method,
    restbehavior::Transition,
    restbehavior::State,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_optype_is_not_abstract():
    assert not inspect.isabstract(OpType)


def test_optype_constructor_exists():
    assert callable(OpType.__init__)


def test_optype_constructor_args():
    sig = inspect.signature(OpType.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::optype_is_not_abstract():
    assert not inspect.isabstract(restbehavior::OpType)


def test_restbehavior::optype_constructor_exists():
    assert callable(restbehavior::OpType.__init__)


def test_restbehavior::optype_constructor_args():
    sig = inspect.signature(restbehavior::OpType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior::optype_has_name():
    assert hasattr(restbehavior::OpType, "name")
    descriptor = None
    for klass in restbehavior::OpType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior::binoptype_is_not_abstract():
    assert not inspect.isabstract(restbehavior::BinOpType)


def test_restbehavior::binoptype_constructor_exists():
    assert callable(restbehavior::BinOpType.__init__)


def test_restbehavior::binoptype_constructor_args():
    sig = inspect.signature(restbehavior::BinOpType.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::binaryoperation_is_not_abstract():
    assert not inspect.isabstract(restbehavior::BinaryOperation)


def test_restbehavior::binaryoperation_constructor_exists():
    assert callable(restbehavior::BinaryOperation.__init__)


def test_restbehavior::binaryoperation_constructor_args():
    sig = inspect.signature(restbehavior::BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::externallink_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ExternalLink)


def test_restbehavior::externallink_constructor_exists():
    assert callable(restbehavior::ExternalLink.__init__)


def test_restbehavior::externallink_constructor_args():
    sig = inspect.signature(restbehavior::ExternalLink.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::deletedstate_is_not_abstract():
    assert not inspect.isabstract(restbehavior::DeletedState)


def test_restbehavior::deletedstate_constructor_exists():
    assert callable(restbehavior::DeletedState.__init__)


def test_restbehavior::deletedstate_constructor_args():
    sig = inspect.signature(restbehavior::DeletedState.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mediatypeelement_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MediaTypeElement)


def test_restbehavior::mediatypeelement_constructor_exists():
    assert callable(restbehavior::MediaTypeElement.__init__)


def test_restbehavior::mediatypeelement_constructor_args():
    sig = inspect.signature(restbehavior::MediaTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mediatypelink_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MediaTypeLink)


def test_restbehavior::mediatypelink_constructor_exists():
    assert callable(restbehavior::MediaTypeLink.__init__)


def test_restbehavior::mediatypelink_constructor_args():
    sig = inspect.signature(restbehavior::MediaTypeLink.__init__)
    params = list(sig.parameters.keys())



def test_mtreference_is_not_abstract():
    assert not inspect.isabstract(MTReference)


def test_mtreference_constructor_exists():
    assert callable(MTReference.__init__)


def test_mtreference_constructor_args():
    sig = inspect.signature(MTReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mtelementreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MtElementReference)


def test_restbehavior::mtelementreference_constructor_exists():
    assert callable(restbehavior::MtElementReference.__init__)


def test_restbehavior::mtelementreference_constructor_args():
    sig = inspect.signature(restbehavior::MtElementReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mtlinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MTLinkReference)


def test_restbehavior::mtlinkreference_constructor_exists():
    assert callable(restbehavior::MTLinkReference.__init__)


def test_restbehavior::mtlinkreference_constructor_args():
    sig = inspect.signature(restbehavior::MTLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mtreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MTReference)


def test_restbehavior::mtreference_constructor_exists():
    assert callable(restbehavior::MTReference.__init__)


def test_restbehavior::mtreference_constructor_args():
    sig = inspect.signature(restbehavior::MTReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::internallink_is_not_abstract():
    assert not inspect.isabstract(restbehavior::InternalLink)


def test_restbehavior::internallink_constructor_exists():
    assert callable(restbehavior::InternalLink.__init__)


def test_restbehavior::internallink_constructor_args():
    sig = inspect.signature(restbehavior::InternalLink.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::attribute_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Attribute)


def test_restbehavior::attribute_constructor_exists():
    assert callable(restbehavior::Attribute.__init__)


def test_restbehavior::attribute_constructor_args():
    sig = inspect.signature(restbehavior::Attribute.__init__)
    params = list(sig.parameters.keys())



def test_writablereference_is_not_abstract():
    assert not inspect.isabstract(WritableReference)


def test_writablereference_constructor_exists():
    assert callable(WritableReference.__init__)


def test_writablereference_constructor_args():
    sig = inspect.signature(WritableReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::attributereference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::AttributeReference)


def test_restbehavior::attributereference_constructor_exists():
    assert callable(restbehavior::AttributeReference.__init__)


def test_restbehavior::attributereference_constructor_args():
    sig = inspect.signature(restbehavior::AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::internallinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::InternalLinkReference)


def test_restbehavior::internallinkreference_constructor_exists():
    assert callable(restbehavior::InternalLinkReference.__init__)


def test_restbehavior::internallinkreference_constructor_args():
    sig = inspect.signature(restbehavior::InternalLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::externallinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ExternalLinkReference)


def test_restbehavior::externallinkreference_constructor_exists():
    assert callable(restbehavior::ExternalLinkReference.__init__)


def test_restbehavior::externallinkreference_constructor_args():
    sig = inspect.signature(restbehavior::ExternalLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::createaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::CreateAction)


def test_restbehavior::createaction_constructor_exists():
    assert callable(restbehavior::CreateAction.__init__)


def test_restbehavior::createaction_constructor_args():
    sig = inspect.signature(restbehavior::CreateAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::listaddaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ListAddAction)


def test_restbehavior::listaddaction_constructor_exists():
    assert callable(restbehavior::ListAddAction.__init__)


def test_restbehavior::listaddaction_constructor_args():
    sig = inspect.signature(restbehavior::ListAddAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::listremoveaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ListRemoveAction)


def test_restbehavior::listremoveaction_constructor_exists():
    assert callable(restbehavior::ListRemoveAction.__init__)


def test_restbehavior::listremoveaction_constructor_args():
    sig = inspect.signature(restbehavior::ListRemoveAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::actionsequence_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ActionSequence)


def test_restbehavior::actionsequence_constructor_exists():
    assert callable(restbehavior::ActionSequence.__init__)


def test_restbehavior::actionsequence_constructor_args():
    sig = inspect.signature(restbehavior::ActionSequence.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::conditionalaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ConditionalAction)


def test_restbehavior::conditionalaction_constructor_exists():
    assert callable(restbehavior::ConditionalAction.__init__)


def test_restbehavior::conditionalaction_constructor_args():
    sig = inspect.signature(restbehavior::ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::messageaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MessageAction)


def test_restbehavior::messageaction_constructor_exists():
    assert callable(restbehavior::MessageAction.__init__)


def test_restbehavior::messageaction_constructor_args():
    sig = inspect.signature(restbehavior::MessageAction.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::internalmessage_is_not_abstract():
    assert not inspect.isabstract(restbehavior::InternalMessage)


def test_restbehavior::internalmessage_constructor_exists():
    assert callable(restbehavior::InternalMessage.__init__)


def test_restbehavior::internalmessage_constructor_args():
    sig = inspect.signature(restbehavior::InternalMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior::internalmessage_has_name():
    assert hasattr(restbehavior::InternalMessage, "name")
    descriptor = None
    for klass in restbehavior::InternalMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior::datatype_is_not_abstract():
    assert not inspect.isabstract(restbehavior::DataType)


def test_restbehavior::datatype_constructor_exists():
    assert callable(restbehavior::DataType.__init__)


def test_restbehavior::datatype_constructor_args():
    sig = inspect.signature(restbehavior::DataType.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::operation_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Operation)


def test_restbehavior::operation_constructor_exists():
    assert callable(restbehavior::Operation.__init__)


def test_restbehavior::operation_constructor_args():
    sig = inspect.signature(restbehavior::Operation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::reference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Reference)


def test_restbehavior::reference_constructor_exists():
    assert callable(restbehavior::Reference.__init__)


def test_restbehavior::reference_constructor_args():
    sig = inspect.signature(restbehavior::Reference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::constant_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Constant)


def test_restbehavior::constant_constructor_exists():
    assert callable(restbehavior::Constant.__init__)


def test_restbehavior::constant_constructor_args():
    sig = inspect.signature(restbehavior::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "stringRepresentation" in params, "Missing parameter 'stringRepresentation'"

def test_restbehavior::constant_has_stringRepresentation():
    assert hasattr(restbehavior::Constant, "stringRepresentation")
    descriptor = None
    for klass in restbehavior::Constant.__mro__:
        if "stringRepresentation" in klass.__dict__:
            descriptor = klass.__dict__["stringRepresentation"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior::representation_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Representation)


def test_restbehavior::representation_constructor_exists():
    assert callable(restbehavior::Representation.__init__)


def test_restbehavior::representation_constructor_args():
    sig = inspect.signature(restbehavior::Representation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::metadata_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Metadata)


def test_restbehavior::metadata_constructor_exists():
    assert callable(restbehavior::Metadata.__init__)


def test_restbehavior::metadata_constructor_args():
    sig = inspect.signature(restbehavior::Metadata.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::statuscode_is_not_abstract():
    assert not inspect.isabstract(restbehavior::StatusCode)


def test_restbehavior::statuscode_constructor_exists():
    assert callable(restbehavior::StatusCode.__init__)


def test_restbehavior::statuscode_constructor_args():
    sig = inspect.signature(restbehavior::StatusCode.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_restbehavior::statuscode_has_number():
    assert hasattr(restbehavior::StatusCode, "number")
    descriptor = None
    for klass in restbehavior::StatusCode.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior::returnaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::ReturnAction)


def test_restbehavior::returnaction_constructor_exists():
    assert callable(restbehavior::ReturnAction.__init__)


def test_restbehavior::returnaction_constructor_args():
    sig = inspect.signature(restbehavior::ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::writablereference_is_not_abstract():
    assert not inspect.isabstract(restbehavior::WritableReference)


def test_restbehavior::writablereference_constructor_exists():
    assert callable(restbehavior::WritableReference.__init__)


def test_restbehavior::writablereference_constructor_args():
    sig = inspect.signature(restbehavior::WritableReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::updateaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior::UpdateAction)


def test_restbehavior::updateaction_constructor_exists():
    assert callable(restbehavior::UpdateAction.__init__)


def test_restbehavior::updateaction_constructor_args():
    sig = inspect.signature(restbehavior::UpdateAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::action_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Action)


def test_restbehavior::action_constructor_exists():
    assert callable(restbehavior::Action.__init__)


def test_restbehavior::action_constructor_args():
    sig = inspect.signature(restbehavior::Action.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::behaviorspecification_is_not_abstract():
    assert not inspect.isabstract(restbehavior::BehaviorSpecification)


def test_restbehavior::behaviorspecification_constructor_exists():
    assert callable(restbehavior::BehaviorSpecification.__init__)


def test_restbehavior::behaviorspecification_constructor_args():
    sig = inspect.signature(restbehavior::BehaviorSpecification.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::parameter_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Parameter)


def test_restbehavior::parameter_constructor_exists():
    assert callable(restbehavior::Parameter.__init__)


def test_restbehavior::parameter_constructor_args():
    sig = inspect.signature(restbehavior::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::mediatype_is_not_abstract():
    assert not inspect.isabstract(restbehavior::MediaType)


def test_restbehavior::mediatype_constructor_exists():
    assert callable(restbehavior::MediaType.__init__)


def test_restbehavior::mediatype_constructor_args():
    sig = inspect.signature(restbehavior::MediaType.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::creator_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Creator)


def test_restbehavior::creator_constructor_exists():
    assert callable(restbehavior::Creator.__init__)


def test_restbehavior::creator_constructor_args():
    sig = inspect.signature(restbehavior::Creator.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::value_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Value)


def test_restbehavior::value_constructor_exists():
    assert callable(restbehavior::Value.__init__)


def test_restbehavior::value_constructor_args():
    sig = inspect.signature(restbehavior::Value.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::condition_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Condition)


def test_restbehavior::condition_constructor_exists():
    assert callable(restbehavior::Condition.__init__)


def test_restbehavior::condition_constructor_args():
    sig = inspect.signature(restbehavior::Condition.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::trigger_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Trigger)


def test_restbehavior::trigger_constructor_exists():
    assert callable(restbehavior::Trigger.__init__)


def test_restbehavior::trigger_constructor_args():
    sig = inspect.signature(restbehavior::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::method_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Method)


def test_restbehavior::method_constructor_exists():
    assert callable(restbehavior::Method.__init__)


def test_restbehavior::method_constructor_args():
    sig = inspect.signature(restbehavior::Method.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::transition_is_not_abstract():
    assert not inspect.isabstract(restbehavior::Transition)


def test_restbehavior::transition_constructor_exists():
    assert callable(restbehavior::Transition.__init__)


def test_restbehavior::transition_constructor_args():
    sig = inspect.signature(restbehavior::Transition.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior::state_is_not_abstract():
    assert not inspect.isabstract(restbehavior::State)


def test_restbehavior::state_constructor_exists():
    assert callable(restbehavior::State.__init__)


def test_restbehavior::state_constructor_args():
    sig = inspect.signature(restbehavior::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior::state_has_name():
    assert hasattr(restbehavior::State, "name")
    descriptor = None
    for klass in restbehavior::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
OpType_strategy = st.builds(
    OpType,
)
restbehavior::OpType_strategy = st.builds(
    restbehavior::OpType,
    name=
        safe_text
)
restbehavior::BinOpType_strategy = st.builds(
    restbehavior::BinOpType,
)
Operation_strategy = st.builds(
    Operation,
)
restbehavior::BinaryOperation_strategy = st.builds(
    restbehavior::BinaryOperation,
)
restbehavior::ExternalLink_strategy = st.builds(
    restbehavior::ExternalLink,
)
State_strategy = st.builds(
    State,
)
restbehavior::DeletedState_strategy = st.builds(
    restbehavior::DeletedState,
)
restbehavior::MediaTypeElement_strategy = st.builds(
    restbehavior::MediaTypeElement,
)
restbehavior::MediaTypeLink_strategy = st.builds(
    restbehavior::MediaTypeLink,
)
MTReference_strategy = st.builds(
    MTReference,
)
restbehavior::MtElementReference_strategy = st.builds(
    restbehavior::MtElementReference,
)
restbehavior::MTLinkReference_strategy = st.builds(
    restbehavior::MTLinkReference,
)
Reference_strategy = st.builds(
    Reference,
)
restbehavior::MTReference_strategy = st.builds(
    restbehavior::MTReference,
)
restbehavior::InternalLink_strategy = st.builds(
    restbehavior::InternalLink,
)
restbehavior::Attribute_strategy = st.builds(
    restbehavior::Attribute,
)
WritableReference_strategy = st.builds(
    WritableReference,
)
restbehavior::AttributeReference_strategy = st.builds(
    restbehavior::AttributeReference,
)
restbehavior::InternalLinkReference_strategy = st.builds(
    restbehavior::InternalLinkReference,
)
restbehavior::ExternalLinkReference_strategy = st.builds(
    restbehavior::ExternalLinkReference,
)
Action_strategy = st.builds(
    Action,
)
restbehavior::CreateAction_strategy = st.builds(
    restbehavior::CreateAction,
)
restbehavior::ListAddAction_strategy = st.builds(
    restbehavior::ListAddAction,
)
restbehavior::ListRemoveAction_strategy = st.builds(
    restbehavior::ListRemoveAction,
)
restbehavior::ActionSequence_strategy = st.builds(
    restbehavior::ActionSequence,
)
restbehavior::ConditionalAction_strategy = st.builds(
    restbehavior::ConditionalAction,
)
restbehavior::MessageAction_strategy = st.builds(
    restbehavior::MessageAction,
)
Trigger_strategy = st.builds(
    Trigger,
)
restbehavior::InternalMessage_strategy = st.builds(
    restbehavior::InternalMessage,
    name=
        safe_text
)
restbehavior::DataType_strategy = st.builds(
    restbehavior::DataType,
)
Value_strategy = st.builds(
    Value,
)
restbehavior::Operation_strategy = st.builds(
    restbehavior::Operation,
)
restbehavior::Reference_strategy = st.builds(
    restbehavior::Reference,
)
restbehavior::Constant_strategy = st.builds(
    restbehavior::Constant,
    stringRepresentation=
        safe_text
)
restbehavior::Representation_strategy = st.builds(
    restbehavior::Representation,
)
restbehavior::Metadata_strategy = st.builds(
    restbehavior::Metadata,
)
restbehavior::StatusCode_strategy = st.builds(
    restbehavior::StatusCode,
    number=
        st.integers()
)
restbehavior::ReturnAction_strategy = st.builds(
    restbehavior::ReturnAction,
)
restbehavior::WritableReference_strategy = st.builds(
    restbehavior::WritableReference,
)
restbehavior::UpdateAction_strategy = st.builds(
    restbehavior::UpdateAction,
)
restbehavior::Action_strategy = st.builds(
    restbehavior::Action,
)
restbehavior::BehaviorSpecification_strategy = st.builds(
    restbehavior::BehaviorSpecification,
)
restbehavior::Parameter_strategy = st.builds(
    restbehavior::Parameter,
)
restbehavior::MediaType_strategy = st.builds(
    restbehavior::MediaType,
)
restbehavior::Creator_strategy = st.builds(
    restbehavior::Creator,
)
restbehavior::Value_strategy = st.builds(
    restbehavior::Value,
)
restbehavior::Condition_strategy = st.builds(
    restbehavior::Condition,
)
restbehavior::Trigger_strategy = st.builds(
    restbehavior::Trigger,
)
restbehavior::Method_strategy = st.builds(
    restbehavior::Method,
)
restbehavior::Transition_strategy = st.builds(
    restbehavior::Transition,
)
restbehavior::State_strategy = st.builds(
    restbehavior::State,
    name=
        safe_text
)

@given(instance=OpType_strategy)
@settings(max_examples=50)
def test_optype_instantiation(instance):
    assert isinstance(instance, OpType)

@given(instance=restbehavior::OpType_strategy)
@settings(max_examples=50)
def test_restbehavior::optype_instantiation(instance):
    assert isinstance(instance, restbehavior::OpType)

@given(instance=restbehavior::OpType_strategy)
def test_restbehavior::optype_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=restbehavior::OpType_strategy)
def test_restbehavior::optype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=restbehavior::BinOpType_strategy)
@settings(max_examples=50)
def test_restbehavior::binoptype_instantiation(instance):
    assert isinstance(instance, restbehavior::BinOpType)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=restbehavior::BinaryOperation_strategy)
@settings(max_examples=50)
def test_restbehavior::binaryoperation_instantiation(instance):
    assert isinstance(instance, restbehavior::BinaryOperation)

@given(instance=restbehavior::ExternalLink_strategy)
@settings(max_examples=50)
def test_restbehavior::externallink_instantiation(instance):
    assert isinstance(instance, restbehavior::ExternalLink)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=restbehavior::DeletedState_strategy)
@settings(max_examples=50)
def test_restbehavior::deletedstate_instantiation(instance):
    assert isinstance(instance, restbehavior::DeletedState)

@given(instance=restbehavior::MediaTypeElement_strategy)
@settings(max_examples=50)
def test_restbehavior::mediatypeelement_instantiation(instance):
    assert isinstance(instance, restbehavior::MediaTypeElement)

@given(instance=restbehavior::MediaTypeLink_strategy)
@settings(max_examples=50)
def test_restbehavior::mediatypelink_instantiation(instance):
    assert isinstance(instance, restbehavior::MediaTypeLink)

@given(instance=MTReference_strategy)
@settings(max_examples=50)
def test_mtreference_instantiation(instance):
    assert isinstance(instance, MTReference)

@given(instance=restbehavior::MtElementReference_strategy)
@settings(max_examples=50)
def test_restbehavior::mtelementreference_instantiation(instance):
    assert isinstance(instance, restbehavior::MtElementReference)

@given(instance=restbehavior::MTLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior::mtlinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior::MTLinkReference)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=restbehavior::MTReference_strategy)
@settings(max_examples=50)
def test_restbehavior::mtreference_instantiation(instance):
    assert isinstance(instance, restbehavior::MTReference)

@given(instance=restbehavior::InternalLink_strategy)
@settings(max_examples=50)
def test_restbehavior::internallink_instantiation(instance):
    assert isinstance(instance, restbehavior::InternalLink)

@given(instance=restbehavior::Attribute_strategy)
@settings(max_examples=50)
def test_restbehavior::attribute_instantiation(instance):
    assert isinstance(instance, restbehavior::Attribute)

@given(instance=WritableReference_strategy)
@settings(max_examples=50)
def test_writablereference_instantiation(instance):
    assert isinstance(instance, WritableReference)

@given(instance=restbehavior::AttributeReference_strategy)
@settings(max_examples=50)
def test_restbehavior::attributereference_instantiation(instance):
    assert isinstance(instance, restbehavior::AttributeReference)

@given(instance=restbehavior::InternalLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior::internallinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior::InternalLinkReference)

@given(instance=restbehavior::ExternalLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior::externallinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior::ExternalLinkReference)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=restbehavior::CreateAction_strategy)
@settings(max_examples=50)
def test_restbehavior::createaction_instantiation(instance):
    assert isinstance(instance, restbehavior::CreateAction)

@given(instance=restbehavior::ListAddAction_strategy)
@settings(max_examples=50)
def test_restbehavior::listaddaction_instantiation(instance):
    assert isinstance(instance, restbehavior::ListAddAction)

@given(instance=restbehavior::ListRemoveAction_strategy)
@settings(max_examples=50)
def test_restbehavior::listremoveaction_instantiation(instance):
    assert isinstance(instance, restbehavior::ListRemoveAction)

@given(instance=restbehavior::ActionSequence_strategy)
@settings(max_examples=50)
def test_restbehavior::actionsequence_instantiation(instance):
    assert isinstance(instance, restbehavior::ActionSequence)

@given(instance=restbehavior::ConditionalAction_strategy)
@settings(max_examples=50)
def test_restbehavior::conditionalaction_instantiation(instance):
    assert isinstance(instance, restbehavior::ConditionalAction)

@given(instance=restbehavior::MessageAction_strategy)
@settings(max_examples=50)
def test_restbehavior::messageaction_instantiation(instance):
    assert isinstance(instance, restbehavior::MessageAction)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=restbehavior::InternalMessage_strategy)
@settings(max_examples=50)
def test_restbehavior::internalmessage_instantiation(instance):
    assert isinstance(instance, restbehavior::InternalMessage)

@given(instance=restbehavior::InternalMessage_strategy)
def test_restbehavior::internalmessage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=restbehavior::InternalMessage_strategy)
def test_restbehavior::internalmessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=restbehavior::DataType_strategy)
@settings(max_examples=50)
def test_restbehavior::datatype_instantiation(instance):
    assert isinstance(instance, restbehavior::DataType)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=restbehavior::Operation_strategy)
@settings(max_examples=50)
def test_restbehavior::operation_instantiation(instance):
    assert isinstance(instance, restbehavior::Operation)

@given(instance=restbehavior::Reference_strategy)
@settings(max_examples=50)
def test_restbehavior::reference_instantiation(instance):
    assert isinstance(instance, restbehavior::Reference)

@given(instance=restbehavior::Constant_strategy)
@settings(max_examples=50)
def test_restbehavior::constant_instantiation(instance):
    assert isinstance(instance, restbehavior::Constant)

@given(instance=restbehavior::Constant_strategy)
def test_restbehavior::constant_stringRepresentation_type(instance):
    assert isinstance(instance.stringRepresentation, str)


@given(instance=restbehavior::Constant_strategy)
def test_restbehavior::constant_stringRepresentation_setter(instance):
    original = instance.stringRepresentation
    instance.stringRepresentation = original
    assert instance.stringRepresentation == original

@given(instance=restbehavior::Representation_strategy)
@settings(max_examples=50)
def test_restbehavior::representation_instantiation(instance):
    assert isinstance(instance, restbehavior::Representation)

@given(instance=restbehavior::Metadata_strategy)
@settings(max_examples=50)
def test_restbehavior::metadata_instantiation(instance):
    assert isinstance(instance, restbehavior::Metadata)

@given(instance=restbehavior::StatusCode_strategy)
@settings(max_examples=50)
def test_restbehavior::statuscode_instantiation(instance):
    assert isinstance(instance, restbehavior::StatusCode)

@given(instance=restbehavior::StatusCode_strategy)
def test_restbehavior::statuscode_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=restbehavior::StatusCode_strategy)
def test_restbehavior::statuscode_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=restbehavior::ReturnAction_strategy)
@settings(max_examples=50)
def test_restbehavior::returnaction_instantiation(instance):
    assert isinstance(instance, restbehavior::ReturnAction)

@given(instance=restbehavior::WritableReference_strategy)
@settings(max_examples=50)
def test_restbehavior::writablereference_instantiation(instance):
    assert isinstance(instance, restbehavior::WritableReference)

@given(instance=restbehavior::UpdateAction_strategy)
@settings(max_examples=50)
def test_restbehavior::updateaction_instantiation(instance):
    assert isinstance(instance, restbehavior::UpdateAction)

@given(instance=restbehavior::Action_strategy)
@settings(max_examples=50)
def test_restbehavior::action_instantiation(instance):
    assert isinstance(instance, restbehavior::Action)

@given(instance=restbehavior::BehaviorSpecification_strategy)
@settings(max_examples=50)
def test_restbehavior::behaviorspecification_instantiation(instance):
    assert isinstance(instance, restbehavior::BehaviorSpecification)

@given(instance=restbehavior::Parameter_strategy)
@settings(max_examples=50)
def test_restbehavior::parameter_instantiation(instance):
    assert isinstance(instance, restbehavior::Parameter)

@given(instance=restbehavior::MediaType_strategy)
@settings(max_examples=50)
def test_restbehavior::mediatype_instantiation(instance):
    assert isinstance(instance, restbehavior::MediaType)

@given(instance=restbehavior::Creator_strategy)
@settings(max_examples=50)
def test_restbehavior::creator_instantiation(instance):
    assert isinstance(instance, restbehavior::Creator)

@given(instance=restbehavior::Value_strategy)
@settings(max_examples=50)
def test_restbehavior::value_instantiation(instance):
    assert isinstance(instance, restbehavior::Value)

@given(instance=restbehavior::Condition_strategy)
@settings(max_examples=50)
def test_restbehavior::condition_instantiation(instance):
    assert isinstance(instance, restbehavior::Condition)

@given(instance=restbehavior::Trigger_strategy)
@settings(max_examples=50)
def test_restbehavior::trigger_instantiation(instance):
    assert isinstance(instance, restbehavior::Trigger)

@given(instance=restbehavior::Method_strategy)
@settings(max_examples=50)
def test_restbehavior::method_instantiation(instance):
    assert isinstance(instance, restbehavior::Method)

@given(instance=restbehavior::Transition_strategy)
@settings(max_examples=50)
def test_restbehavior::transition_instantiation(instance):
    assert isinstance(instance, restbehavior::Transition)

@given(instance=restbehavior::State_strategy)
@settings(max_examples=50)
def test_restbehavior::state_instantiation(instance):
    assert isinstance(instance, restbehavior::State)

@given(instance=restbehavior::State_strategy)
def test_restbehavior::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=restbehavior::State_strategy)
def test_restbehavior::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
