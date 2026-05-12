import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    restbehavior_Attribute,
    WritableReference,
    restbehavior_InternalLinkReference,
    restbehavior_AttributeReference,
    restbehavior_ExternalLink,
    restbehavior_ExternalLinkReference,
    State,
    restbehavior_DeletedState,
    restbehavior_MediaTypeElement,
    restbehavior_MediaTypeLink,
    MTReference,
    restbehavior_MtElementReference,
    restbehavior_MTLinkReference,
    Reference,
    restbehavior_MTReference,
    restbehavior_InternalLink,
    OpType,
    restbehavior_OpType,
    restbehavior_BinOpType,
    Operation,
    restbehavior_BinaryOperation,
    restbehavior_DataType,
    Value,
    restbehavior_Reference,
    restbehavior_Operation,
    restbehavior_Constant,
    restbehavior_Representation,
    restbehavior_Metadata,
    restbehavior_StatusCode,
    restbehavior_WritableReference,
    restbehavior_MediaType,
    restbehavior_Creator,
    Action,
    restbehavior_ReturnAction,
    restbehavior_UpdateAction,
    restbehavior_ListAddAction,
    restbehavior_CreateAction,
    restbehavior_ConditionalAction,
    restbehavior_ActionSequence,
    restbehavior_ListRemoveAction,
    restbehavior_MessageAction,
    Trigger,
    restbehavior_InternalMessage,
    restbehavior_Value,
    restbehavior_Condition,
    restbehavior_Trigger,
    restbehavior_Method,
    restbehavior_Transition,
    restbehavior_State,
    restbehavior_Action,
    restbehavior_BehaviorSpecification,
    restbehavior_Parameter,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_restbehavior_attribute_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Attribute)


def test_restbehavior_attribute_constructor_exists():
    assert callable(restbehavior_Attribute.__init__)


def test_restbehavior_attribute_constructor_args():
    sig = inspect.signature(restbehavior_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_writablereference_is_not_abstract():
    assert not inspect.isabstract(WritableReference)


def test_writablereference_constructor_exists():
    assert callable(WritableReference.__init__)


def test_writablereference_constructor_args():
    sig = inspect.signature(WritableReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_internallinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_InternalLinkReference)


def test_restbehavior_internallinkreference_constructor_exists():
    assert callable(restbehavior_InternalLinkReference.__init__)


def test_restbehavior_internallinkreference_constructor_args():
    sig = inspect.signature(restbehavior_InternalLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_attributereference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_AttributeReference)


def test_restbehavior_attributereference_constructor_exists():
    assert callable(restbehavior_AttributeReference.__init__)


def test_restbehavior_attributereference_constructor_args():
    sig = inspect.signature(restbehavior_AttributeReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_externallink_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ExternalLink)


def test_restbehavior_externallink_constructor_exists():
    assert callable(restbehavior_ExternalLink.__init__)


def test_restbehavior_externallink_constructor_args():
    sig = inspect.signature(restbehavior_ExternalLink.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_externallinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ExternalLinkReference)


def test_restbehavior_externallinkreference_constructor_exists():
    assert callable(restbehavior_ExternalLinkReference.__init__)


def test_restbehavior_externallinkreference_constructor_args():
    sig = inspect.signature(restbehavior_ExternalLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_deletedstate_is_not_abstract():
    assert not inspect.isabstract(restbehavior_DeletedState)


def test_restbehavior_deletedstate_constructor_exists():
    assert callable(restbehavior_DeletedState.__init__)


def test_restbehavior_deletedstate_constructor_args():
    sig = inspect.signature(restbehavior_DeletedState.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mediatypeelement_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MediaTypeElement)


def test_restbehavior_mediatypeelement_constructor_exists():
    assert callable(restbehavior_MediaTypeElement.__init__)


def test_restbehavior_mediatypeelement_constructor_args():
    sig = inspect.signature(restbehavior_MediaTypeElement.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mediatypelink_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MediaTypeLink)


def test_restbehavior_mediatypelink_constructor_exists():
    assert callable(restbehavior_MediaTypeLink.__init__)


def test_restbehavior_mediatypelink_constructor_args():
    sig = inspect.signature(restbehavior_MediaTypeLink.__init__)
    params = list(sig.parameters.keys())



def test_mtreference_is_not_abstract():
    assert not inspect.isabstract(MTReference)


def test_mtreference_constructor_exists():
    assert callable(MTReference.__init__)


def test_mtreference_constructor_args():
    sig = inspect.signature(MTReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mtelementreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MtElementReference)


def test_restbehavior_mtelementreference_constructor_exists():
    assert callable(restbehavior_MtElementReference.__init__)


def test_restbehavior_mtelementreference_constructor_args():
    sig = inspect.signature(restbehavior_MtElementReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mtlinkreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MTLinkReference)


def test_restbehavior_mtlinkreference_constructor_exists():
    assert callable(restbehavior_MTLinkReference.__init__)


def test_restbehavior_mtlinkreference_constructor_args():
    sig = inspect.signature(restbehavior_MTLinkReference.__init__)
    params = list(sig.parameters.keys())



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mtreference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MTReference)


def test_restbehavior_mtreference_constructor_exists():
    assert callable(restbehavior_MTReference.__init__)


def test_restbehavior_mtreference_constructor_args():
    sig = inspect.signature(restbehavior_MTReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_internallink_is_not_abstract():
    assert not inspect.isabstract(restbehavior_InternalLink)


def test_restbehavior_internallink_constructor_exists():
    assert callable(restbehavior_InternalLink.__init__)


def test_restbehavior_internallink_constructor_args():
    sig = inspect.signature(restbehavior_InternalLink.__init__)
    params = list(sig.parameters.keys())



def test_optype_is_not_abstract():
    assert not inspect.isabstract(OpType)


def test_optype_constructor_exists():
    assert callable(OpType.__init__)


def test_optype_constructor_args():
    sig = inspect.signature(OpType.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_optype_is_not_abstract():
    assert not inspect.isabstract(restbehavior_OpType)


def test_restbehavior_optype_constructor_exists():
    assert callable(restbehavior_OpType.__init__)


def test_restbehavior_optype_constructor_args():
    sig = inspect.signature(restbehavior_OpType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior_optype_has_name():
    assert hasattr(restbehavior_OpType, "name")
    descriptor = None
    for klass in restbehavior_OpType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior_binoptype_is_not_abstract():
    assert not inspect.isabstract(restbehavior_BinOpType)


def test_restbehavior_binoptype_constructor_exists():
    assert callable(restbehavior_BinOpType.__init__)


def test_restbehavior_binoptype_constructor_args():
    sig = inspect.signature(restbehavior_BinOpType.__init__)
    params = list(sig.parameters.keys())



def test_operation_is_not_abstract():
    assert not inspect.isabstract(Operation)


def test_operation_constructor_exists():
    assert callable(Operation.__init__)


def test_operation_constructor_args():
    sig = inspect.signature(Operation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_binaryoperation_is_not_abstract():
    assert not inspect.isabstract(restbehavior_BinaryOperation)


def test_restbehavior_binaryoperation_constructor_exists():
    assert callable(restbehavior_BinaryOperation.__init__)


def test_restbehavior_binaryoperation_constructor_args():
    sig = inspect.signature(restbehavior_BinaryOperation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_datatype_is_not_abstract():
    assert not inspect.isabstract(restbehavior_DataType)


def test_restbehavior_datatype_constructor_exists():
    assert callable(restbehavior_DataType.__init__)


def test_restbehavior_datatype_constructor_args():
    sig = inspect.signature(restbehavior_DataType.__init__)
    params = list(sig.parameters.keys())



def test_value_is_not_abstract():
    assert not inspect.isabstract(Value)


def test_value_constructor_exists():
    assert callable(Value.__init__)


def test_value_constructor_args():
    sig = inspect.signature(Value.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_reference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Reference)


def test_restbehavior_reference_constructor_exists():
    assert callable(restbehavior_Reference.__init__)


def test_restbehavior_reference_constructor_args():
    sig = inspect.signature(restbehavior_Reference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_operation_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Operation)


def test_restbehavior_operation_constructor_exists():
    assert callable(restbehavior_Operation.__init__)


def test_restbehavior_operation_constructor_args():
    sig = inspect.signature(restbehavior_Operation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_constant_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Constant)


def test_restbehavior_constant_constructor_exists():
    assert callable(restbehavior_Constant.__init__)


def test_restbehavior_constant_constructor_args():
    sig = inspect.signature(restbehavior_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "stringRepresentation" in params, "Missing parameter 'stringRepresentation'"

def test_restbehavior_constant_has_stringRepresentation():
    assert hasattr(restbehavior_Constant, "stringRepresentation")
    descriptor = None
    for klass in restbehavior_Constant.__mro__:
        if "stringRepresentation" in klass.__dict__:
            descriptor = klass.__dict__["stringRepresentation"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior_representation_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Representation)


def test_restbehavior_representation_constructor_exists():
    assert callable(restbehavior_Representation.__init__)


def test_restbehavior_representation_constructor_args():
    sig = inspect.signature(restbehavior_Representation.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_metadata_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Metadata)


def test_restbehavior_metadata_constructor_exists():
    assert callable(restbehavior_Metadata.__init__)


def test_restbehavior_metadata_constructor_args():
    sig = inspect.signature(restbehavior_Metadata.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_statuscode_is_not_abstract():
    assert not inspect.isabstract(restbehavior_StatusCode)


def test_restbehavior_statuscode_constructor_exists():
    assert callable(restbehavior_StatusCode.__init__)


def test_restbehavior_statuscode_constructor_args():
    sig = inspect.signature(restbehavior_StatusCode.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"

def test_restbehavior_statuscode_has_number():
    assert hasattr(restbehavior_StatusCode, "number")
    descriptor = None
    for klass in restbehavior_StatusCode.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior_writablereference_is_not_abstract():
    assert not inspect.isabstract(restbehavior_WritableReference)


def test_restbehavior_writablereference_constructor_exists():
    assert callable(restbehavior_WritableReference.__init__)


def test_restbehavior_writablereference_constructor_args():
    sig = inspect.signature(restbehavior_WritableReference.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_mediatype_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MediaType)


def test_restbehavior_mediatype_constructor_exists():
    assert callable(restbehavior_MediaType.__init__)


def test_restbehavior_mediatype_constructor_args():
    sig = inspect.signature(restbehavior_MediaType.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_creator_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Creator)


def test_restbehavior_creator_constructor_exists():
    assert callable(restbehavior_Creator.__init__)


def test_restbehavior_creator_constructor_args():
    sig = inspect.signature(restbehavior_Creator.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_returnaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ReturnAction)


def test_restbehavior_returnaction_constructor_exists():
    assert callable(restbehavior_ReturnAction.__init__)


def test_restbehavior_returnaction_constructor_args():
    sig = inspect.signature(restbehavior_ReturnAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_updateaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_UpdateAction)


def test_restbehavior_updateaction_constructor_exists():
    assert callable(restbehavior_UpdateAction.__init__)


def test_restbehavior_updateaction_constructor_args():
    sig = inspect.signature(restbehavior_UpdateAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_listaddaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ListAddAction)


def test_restbehavior_listaddaction_constructor_exists():
    assert callable(restbehavior_ListAddAction.__init__)


def test_restbehavior_listaddaction_constructor_args():
    sig = inspect.signature(restbehavior_ListAddAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_createaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_CreateAction)


def test_restbehavior_createaction_constructor_exists():
    assert callable(restbehavior_CreateAction.__init__)


def test_restbehavior_createaction_constructor_args():
    sig = inspect.signature(restbehavior_CreateAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_conditionalaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ConditionalAction)


def test_restbehavior_conditionalaction_constructor_exists():
    assert callable(restbehavior_ConditionalAction.__init__)


def test_restbehavior_conditionalaction_constructor_args():
    sig = inspect.signature(restbehavior_ConditionalAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_actionsequence_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ActionSequence)


def test_restbehavior_actionsequence_constructor_exists():
    assert callable(restbehavior_ActionSequence.__init__)


def test_restbehavior_actionsequence_constructor_args():
    sig = inspect.signature(restbehavior_ActionSequence.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_listremoveaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_ListRemoveAction)


def test_restbehavior_listremoveaction_constructor_exists():
    assert callable(restbehavior_ListRemoveAction.__init__)


def test_restbehavior_listremoveaction_constructor_args():
    sig = inspect.signature(restbehavior_ListRemoveAction.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_messageaction_is_not_abstract():
    assert not inspect.isabstract(restbehavior_MessageAction)


def test_restbehavior_messageaction_constructor_exists():
    assert callable(restbehavior_MessageAction.__init__)


def test_restbehavior_messageaction_constructor_args():
    sig = inspect.signature(restbehavior_MessageAction.__init__)
    params = list(sig.parameters.keys())



def test_trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger)


def test_trigger_constructor_exists():
    assert callable(Trigger.__init__)


def test_trigger_constructor_args():
    sig = inspect.signature(Trigger.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_internalmessage_is_not_abstract():
    assert not inspect.isabstract(restbehavior_InternalMessage)


def test_restbehavior_internalmessage_constructor_exists():
    assert callable(restbehavior_InternalMessage.__init__)


def test_restbehavior_internalmessage_constructor_args():
    sig = inspect.signature(restbehavior_InternalMessage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior_internalmessage_has_name():
    assert hasattr(restbehavior_InternalMessage, "name")
    descriptor = None
    for klass in restbehavior_InternalMessage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior_value_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Value)


def test_restbehavior_value_constructor_exists():
    assert callable(restbehavior_Value.__init__)


def test_restbehavior_value_constructor_args():
    sig = inspect.signature(restbehavior_Value.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_condition_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Condition)


def test_restbehavior_condition_constructor_exists():
    assert callable(restbehavior_Condition.__init__)


def test_restbehavior_condition_constructor_args():
    sig = inspect.signature(restbehavior_Condition.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_trigger_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Trigger)


def test_restbehavior_trigger_constructor_exists():
    assert callable(restbehavior_Trigger.__init__)


def test_restbehavior_trigger_constructor_args():
    sig = inspect.signature(restbehavior_Trigger.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_method_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Method)


def test_restbehavior_method_constructor_exists():
    assert callable(restbehavior_Method.__init__)


def test_restbehavior_method_constructor_args():
    sig = inspect.signature(restbehavior_Method.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_transition_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Transition)


def test_restbehavior_transition_constructor_exists():
    assert callable(restbehavior_Transition.__init__)


def test_restbehavior_transition_constructor_args():
    sig = inspect.signature(restbehavior_Transition.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_state_is_not_abstract():
    assert not inspect.isabstract(restbehavior_State)


def test_restbehavior_state_constructor_exists():
    assert callable(restbehavior_State.__init__)


def test_restbehavior_state_constructor_args():
    sig = inspect.signature(restbehavior_State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_restbehavior_state_has_name():
    assert hasattr(restbehavior_State, "name")
    descriptor = None
    for klass in restbehavior_State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_restbehavior_action_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Action)


def test_restbehavior_action_constructor_exists():
    assert callable(restbehavior_Action.__init__)


def test_restbehavior_action_constructor_args():
    sig = inspect.signature(restbehavior_Action.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_behaviorspecification_is_not_abstract():
    assert not inspect.isabstract(restbehavior_BehaviorSpecification)


def test_restbehavior_behaviorspecification_constructor_exists():
    assert callable(restbehavior_BehaviorSpecification.__init__)


def test_restbehavior_behaviorspecification_constructor_args():
    sig = inspect.signature(restbehavior_BehaviorSpecification.__init__)
    params = list(sig.parameters.keys())



def test_restbehavior_parameter_is_not_abstract():
    assert not inspect.isabstract(restbehavior_Parameter)


def test_restbehavior_parameter_constructor_exists():
    assert callable(restbehavior_Parameter.__init__)


def test_restbehavior_parameter_constructor_args():
    sig = inspect.signature(restbehavior_Parameter.__init__)
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
restbehavior_Attribute_strategy = st.builds(
    restbehavior_Attribute,
)
WritableReference_strategy = st.builds(
    WritableReference,
)
restbehavior_InternalLinkReference_strategy = st.builds(
    restbehavior_InternalLinkReference,
)
restbehavior_AttributeReference_strategy = st.builds(
    restbehavior_AttributeReference,
)
restbehavior_ExternalLink_strategy = st.builds(
    restbehavior_ExternalLink,
)
restbehavior_ExternalLinkReference_strategy = st.builds(
    restbehavior_ExternalLinkReference,
)
State_strategy = st.builds(
    State,
)
restbehavior_DeletedState_strategy = st.builds(
    restbehavior_DeletedState,
)
restbehavior_MediaTypeElement_strategy = st.builds(
    restbehavior_MediaTypeElement,
)
restbehavior_MediaTypeLink_strategy = st.builds(
    restbehavior_MediaTypeLink,
)
MTReference_strategy = st.builds(
    MTReference,
)
restbehavior_MtElementReference_strategy = st.builds(
    restbehavior_MtElementReference,
)
restbehavior_MTLinkReference_strategy = st.builds(
    restbehavior_MTLinkReference,
)
Reference_strategy = st.builds(
    Reference,
)
restbehavior_MTReference_strategy = st.builds(
    restbehavior_MTReference,
)
restbehavior_InternalLink_strategy = st.builds(
    restbehavior_InternalLink,
)
OpType_strategy = st.builds(
    OpType,
)
restbehavior_OpType_strategy = st.builds(
    restbehavior_OpType,
    name=
        safe_text
)
restbehavior_BinOpType_strategy = st.builds(
    restbehavior_BinOpType,
)
Operation_strategy = st.builds(
    Operation,
)
restbehavior_BinaryOperation_strategy = st.builds(
    restbehavior_BinaryOperation,
)
restbehavior_DataType_strategy = st.builds(
    restbehavior_DataType,
)
Value_strategy = st.builds(
    Value,
)
restbehavior_Reference_strategy = st.builds(
    restbehavior_Reference,
)
restbehavior_Operation_strategy = st.builds(
    restbehavior_Operation,
)
restbehavior_Constant_strategy = st.builds(
    restbehavior_Constant,
    stringRepresentation=
        safe_text
)
restbehavior_Representation_strategy = st.builds(
    restbehavior_Representation,
)
restbehavior_Metadata_strategy = st.builds(
    restbehavior_Metadata,
)
restbehavior_StatusCode_strategy = st.builds(
    restbehavior_StatusCode,
    number=
        st.integers()
)
restbehavior_WritableReference_strategy = st.builds(
    restbehavior_WritableReference,
)
restbehavior_MediaType_strategy = st.builds(
    restbehavior_MediaType,
)
restbehavior_Creator_strategy = st.builds(
    restbehavior_Creator,
)
Action_strategy = st.builds(
    Action,
)
restbehavior_ReturnAction_strategy = st.builds(
    restbehavior_ReturnAction,
)
restbehavior_UpdateAction_strategy = st.builds(
    restbehavior_UpdateAction,
)
restbehavior_ListAddAction_strategy = st.builds(
    restbehavior_ListAddAction,
)
restbehavior_CreateAction_strategy = st.builds(
    restbehavior_CreateAction,
)
restbehavior_ConditionalAction_strategy = st.builds(
    restbehavior_ConditionalAction,
)
restbehavior_ActionSequence_strategy = st.builds(
    restbehavior_ActionSequence,
)
restbehavior_ListRemoveAction_strategy = st.builds(
    restbehavior_ListRemoveAction,
)
restbehavior_MessageAction_strategy = st.builds(
    restbehavior_MessageAction,
)
Trigger_strategy = st.builds(
    Trigger,
)
restbehavior_InternalMessage_strategy = st.builds(
    restbehavior_InternalMessage,
    name=
        safe_text
)
restbehavior_Value_strategy = st.builds(
    restbehavior_Value,
)
restbehavior_Condition_strategy = st.builds(
    restbehavior_Condition,
)
restbehavior_Trigger_strategy = st.builds(
    restbehavior_Trigger,
)
restbehavior_Method_strategy = st.builds(
    restbehavior_Method,
)
restbehavior_Transition_strategy = st.builds(
    restbehavior_Transition,
)
restbehavior_State_strategy = st.builds(
    restbehavior_State,
    name=
        safe_text
)
restbehavior_Action_strategy = st.builds(
    restbehavior_Action,
)
restbehavior_BehaviorSpecification_strategy = st.builds(
    restbehavior_BehaviorSpecification,
)
restbehavior_Parameter_strategy = st.builds(
    restbehavior_Parameter,
)

@given(instance=restbehavior_Attribute_strategy)
@settings(max_examples=50)
def test_restbehavior_attribute_instantiation(instance):
    assert isinstance(instance, restbehavior_Attribute)

@given(instance=WritableReference_strategy)
@settings(max_examples=50)
def test_writablereference_instantiation(instance):
    assert isinstance(instance, WritableReference)

@given(instance=restbehavior_InternalLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior_internallinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior_InternalLinkReference)

@given(instance=restbehavior_AttributeReference_strategy)
@settings(max_examples=50)
def test_restbehavior_attributereference_instantiation(instance):
    assert isinstance(instance, restbehavior_AttributeReference)

@given(instance=restbehavior_ExternalLink_strategy)
@settings(max_examples=50)
def test_restbehavior_externallink_instantiation(instance):
    assert isinstance(instance, restbehavior_ExternalLink)

@given(instance=restbehavior_ExternalLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior_externallinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior_ExternalLinkReference)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=restbehavior_DeletedState_strategy)
@settings(max_examples=50)
def test_restbehavior_deletedstate_instantiation(instance):
    assert isinstance(instance, restbehavior_DeletedState)

@given(instance=restbehavior_MediaTypeElement_strategy)
@settings(max_examples=50)
def test_restbehavior_mediatypeelement_instantiation(instance):
    assert isinstance(instance, restbehavior_MediaTypeElement)

@given(instance=restbehavior_MediaTypeLink_strategy)
@settings(max_examples=50)
def test_restbehavior_mediatypelink_instantiation(instance):
    assert isinstance(instance, restbehavior_MediaTypeLink)

@given(instance=MTReference_strategy)
@settings(max_examples=50)
def test_mtreference_instantiation(instance):
    assert isinstance(instance, MTReference)

@given(instance=restbehavior_MtElementReference_strategy)
@settings(max_examples=50)
def test_restbehavior_mtelementreference_instantiation(instance):
    assert isinstance(instance, restbehavior_MtElementReference)

@given(instance=restbehavior_MTLinkReference_strategy)
@settings(max_examples=50)
def test_restbehavior_mtlinkreference_instantiation(instance):
    assert isinstance(instance, restbehavior_MTLinkReference)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=restbehavior_MTReference_strategy)
@settings(max_examples=50)
def test_restbehavior_mtreference_instantiation(instance):
    assert isinstance(instance, restbehavior_MTReference)

@given(instance=restbehavior_InternalLink_strategy)
@settings(max_examples=50)
def test_restbehavior_internallink_instantiation(instance):
    assert isinstance(instance, restbehavior_InternalLink)

@given(instance=OpType_strategy)
@settings(max_examples=50)
def test_optype_instantiation(instance):
    assert isinstance(instance, OpType)

@given(instance=restbehavior_OpType_strategy)
@settings(max_examples=50)
def test_restbehavior_optype_instantiation(instance):
    assert isinstance(instance, restbehavior_OpType)



@given(instance=restbehavior_OpType_strategy)
def test_restbehavior_optype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=restbehavior_BinOpType_strategy)
@settings(max_examples=50)
def test_restbehavior_binoptype_instantiation(instance):
    assert isinstance(instance, restbehavior_BinOpType)

@given(instance=Operation_strategy)
@settings(max_examples=50)
def test_operation_instantiation(instance):
    assert isinstance(instance, Operation)

@given(instance=restbehavior_BinaryOperation_strategy)
@settings(max_examples=50)
def test_restbehavior_binaryoperation_instantiation(instance):
    assert isinstance(instance, restbehavior_BinaryOperation)

@given(instance=restbehavior_DataType_strategy)
@settings(max_examples=50)
def test_restbehavior_datatype_instantiation(instance):
    assert isinstance(instance, restbehavior_DataType)

@given(instance=Value_strategy)
@settings(max_examples=50)
def test_value_instantiation(instance):
    assert isinstance(instance, Value)

@given(instance=restbehavior_Reference_strategy)
@settings(max_examples=50)
def test_restbehavior_reference_instantiation(instance):
    assert isinstance(instance, restbehavior_Reference)

@given(instance=restbehavior_Operation_strategy)
@settings(max_examples=50)
def test_restbehavior_operation_instantiation(instance):
    assert isinstance(instance, restbehavior_Operation)

@given(instance=restbehavior_Constant_strategy)
@settings(max_examples=50)
def test_restbehavior_constant_instantiation(instance):
    assert isinstance(instance, restbehavior_Constant)



@given(instance=restbehavior_Constant_strategy)
def test_restbehavior_constant_stringRepresentation_setter(instance):
    original = instance.stringRepresentation
    instance.stringRepresentation = original
    assert instance.stringRepresentation == original

@given(instance=restbehavior_Representation_strategy)
@settings(max_examples=50)
def test_restbehavior_representation_instantiation(instance):
    assert isinstance(instance, restbehavior_Representation)

@given(instance=restbehavior_Metadata_strategy)
@settings(max_examples=50)
def test_restbehavior_metadata_instantiation(instance):
    assert isinstance(instance, restbehavior_Metadata)

@given(instance=restbehavior_StatusCode_strategy)
@settings(max_examples=50)
def test_restbehavior_statuscode_instantiation(instance):
    assert isinstance(instance, restbehavior_StatusCode)



@given(instance=restbehavior_StatusCode_strategy)
def test_restbehavior_statuscode_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=restbehavior_WritableReference_strategy)
@settings(max_examples=50)
def test_restbehavior_writablereference_instantiation(instance):
    assert isinstance(instance, restbehavior_WritableReference)

@given(instance=restbehavior_MediaType_strategy)
@settings(max_examples=50)
def test_restbehavior_mediatype_instantiation(instance):
    assert isinstance(instance, restbehavior_MediaType)

@given(instance=restbehavior_Creator_strategy)
@settings(max_examples=50)
def test_restbehavior_creator_instantiation(instance):
    assert isinstance(instance, restbehavior_Creator)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=restbehavior_ReturnAction_strategy)
@settings(max_examples=50)
def test_restbehavior_returnaction_instantiation(instance):
    assert isinstance(instance, restbehavior_ReturnAction)

@given(instance=restbehavior_UpdateAction_strategy)
@settings(max_examples=50)
def test_restbehavior_updateaction_instantiation(instance):
    assert isinstance(instance, restbehavior_UpdateAction)

@given(instance=restbehavior_ListAddAction_strategy)
@settings(max_examples=50)
def test_restbehavior_listaddaction_instantiation(instance):
    assert isinstance(instance, restbehavior_ListAddAction)

@given(instance=restbehavior_CreateAction_strategy)
@settings(max_examples=50)
def test_restbehavior_createaction_instantiation(instance):
    assert isinstance(instance, restbehavior_CreateAction)

@given(instance=restbehavior_ConditionalAction_strategy)
@settings(max_examples=50)
def test_restbehavior_conditionalaction_instantiation(instance):
    assert isinstance(instance, restbehavior_ConditionalAction)

@given(instance=restbehavior_ActionSequence_strategy)
@settings(max_examples=50)
def test_restbehavior_actionsequence_instantiation(instance):
    assert isinstance(instance, restbehavior_ActionSequence)

@given(instance=restbehavior_ListRemoveAction_strategy)
@settings(max_examples=50)
def test_restbehavior_listremoveaction_instantiation(instance):
    assert isinstance(instance, restbehavior_ListRemoveAction)

@given(instance=restbehavior_MessageAction_strategy)
@settings(max_examples=50)
def test_restbehavior_messageaction_instantiation(instance):
    assert isinstance(instance, restbehavior_MessageAction)

@given(instance=Trigger_strategy)
@settings(max_examples=50)
def test_trigger_instantiation(instance):
    assert isinstance(instance, Trigger)

@given(instance=restbehavior_InternalMessage_strategy)
@settings(max_examples=50)
def test_restbehavior_internalmessage_instantiation(instance):
    assert isinstance(instance, restbehavior_InternalMessage)



@given(instance=restbehavior_InternalMessage_strategy)
def test_restbehavior_internalmessage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=restbehavior_Value_strategy)
@settings(max_examples=50)
def test_restbehavior_value_instantiation(instance):
    assert isinstance(instance, restbehavior_Value)

@given(instance=restbehavior_Condition_strategy)
@settings(max_examples=50)
def test_restbehavior_condition_instantiation(instance):
    assert isinstance(instance, restbehavior_Condition)

@given(instance=restbehavior_Trigger_strategy)
@settings(max_examples=50)
def test_restbehavior_trigger_instantiation(instance):
    assert isinstance(instance, restbehavior_Trigger)

@given(instance=restbehavior_Method_strategy)
@settings(max_examples=50)
def test_restbehavior_method_instantiation(instance):
    assert isinstance(instance, restbehavior_Method)

@given(instance=restbehavior_Transition_strategy)
@settings(max_examples=50)
def test_restbehavior_transition_instantiation(instance):
    assert isinstance(instance, restbehavior_Transition)

@given(instance=restbehavior_State_strategy)
@settings(max_examples=50)
def test_restbehavior_state_instantiation(instance):
    assert isinstance(instance, restbehavior_State)



@given(instance=restbehavior_State_strategy)
def test_restbehavior_state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=restbehavior_Action_strategy)
@settings(max_examples=50)
def test_restbehavior_action_instantiation(instance):
    assert isinstance(instance, restbehavior_Action)

@given(instance=restbehavior_BehaviorSpecification_strategy)
@settings(max_examples=50)
def test_restbehavior_behaviorspecification_instantiation(instance):
    assert isinstance(instance, restbehavior_BehaviorSpecification)

@given(instance=restbehavior_Parameter_strategy)
@settings(max_examples=50)
def test_restbehavior_parameter_instantiation(instance):
    assert isinstance(instance, restbehavior_Parameter)
