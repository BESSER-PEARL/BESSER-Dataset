import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    bpmn2_FormalExpression,
    bpmn2_InteractionNode,
    bpmn2_ParticipantMultiplicity,
    InteractionNode,
    Collaboration,
    FlowElement,
    bpmn2_SequenceFlow,
    bpmn2_FlowNode,
    FlowElementsContainer,
    bpmn2_Choreography,
    ResourceRole,
    bpmn2_Performer,
    bpmn2_ResourceAssignmentExpression,
    bpmn2_ResourceParameterBinding,
    ItemAwareElement,
    bpmn2_Property,
    bpmn2_DataOutput,
    bpmn2_Import,
    bpmn2_DataInput,
    bpmn2_InputOutputBinding,
    CallableElement,
    bpmn2_Process,
    bpmn2_GlobalTask,
    bpmn2_ExtensionAttributeDefinition,
    bpmn2_ExtensionAttributeValue,
    bpmn2_ExtensionDefinition,
    bpmn2_BaseElement,
    BaseElement,
    bpmn2_FlowElement,
    bpmn2_MessageFlowAssociation,
    bpmn2_OutputSet,
    bpmn2_InputSet,
    bpmn2_CorrelationSubscription,
    bpmn2_LaneSet,
    bpmn2_ConversationLink,
    bpmn2_FlowElementsContainer,
    bpmn2_Monitoring,
    bpmn2_InputOutputSpecification,
    bpmn2_CorrelationPropertyRetrievalExpression,
    bpmn2_Lane,
    bpmn2_CorrelationKey,
    bpmn2_Artifact,
    bpmn2_ResourceRole,
    bpmn2_ConversationNode,
    bpmn2_ParticipantAssociation,
    bpmn2_ItemAwareElement,
    bpmn2_MessageFlow,
    bpmn2_ResourceParameter,
    bpmn2_CategoryValue,
    bpmn2_Expression,
    bpmn2_CorrelationPropertyBinding,
    bpmn2_Participant,
    bpmn2_Auditing,
    bpmn2_DataState,
    bpmn2_ConversationAssociation,
    bpmn2_Documentation,
    bpmn2_RootElement,
    bpmn2_EObject,
    bpmn2_Operation,
    RootElement,
    bpmn2_CallableElement,
    bpmn2_EndPoint,
    bpmn2_Resource,
    bpmn2_Collaboration,
    bpmn2_CorrelationProperty,
    bpmn2_ItemDefinition,
    bpmn2_Error,
    bpmn2_Message,
    bpmn2_Interface,
    bpmn2_BPMNDiagram,
    bpmn2_Definitions,
    SubProcess,
    bpmn2_Transaction,
    bpmn2_AdHocSubProcess,
    bpmn2_ComplexBehaviorDefinition,
    LoopCharacteristics,
    bpmn2_StandardLoopCharacteristics,
    bpmn2_MultiInstanceLoopCharacteristics,
    bpmn2_Category,
    Artifact,
    bpmn2_Association,
    bpmn2_Group,
    bpmn2_TextAnnotation,
    Choreography,
    bpmn2_GlobalChoreographyTask,
    ChoreographyActivity,
    bpmn2_SubChoreography,
    bpmn2_ChoreographyTask,
    bpmn2_CallChoreography,
    bpmn2_PartnerRole,
    bpmn2_PartnerEntity,
    bpmn2_GlobalConversation,
    ConversationNode,
    bpmn2_Conversation,
    bpmn2_SubConversation,
    bpmn2_CallConversation,
    bpmn2_DataObjectReference,
    bpmn2_DataStoreReference,
    bpmn2_DataStore,
    bpmn2_DataObject,
    bpmn2_Signal,
    bpmn2_Escalation,
    EventDefinition,
    bpmn2_SignalEventDefinition,
    bpmn2_CompensateEventDefinition,
    bpmn2_ConditionalEventDefinition,
    bpmn2_MessageEventDefinition,
    bpmn2_ErrorEventDefinition,
    bpmn2_TimerEventDefinition,
    bpmn2_EscalationEventDefinition,
    bpmn2_TerminateEventDefinition,
    bpmn2_LinkEventDefinition,
    bpmn2_CancelEventDefinition,
    ThrowEvent,
    bpmn2_ImplicitThrowEvent,
    bpmn2_EndEvent,
    bpmn2_IntermediateThrowEvent,
    bpmn2_Extension,
    bpmn2_Relationship,
    bpmn2_Assignment,
    Gateway,
    bpmn2_ParallelGateway,
    bpmn2_ExclusiveGateway,
    bpmn2_ComplexGateway,
    bpmn2_InclusiveGateway,
    bpmn2_EventBasedGateway,
    HumanPerformer,
    bpmn2_PotentialOwner,
    Performer,
    bpmn2_HumanPerformer,
    bpmn2_Rendering,
    bpmn2_DataAssociation,
    DataAssociation,
    bpmn2_EventDefinition,
    Event,
    bpmn2_ThrowEvent,
    bpmn2_CatchEvent,
    CatchEvent,
    bpmn2_StartEvent,
    bpmn2_IntermediateCatchEvent,
    bpmn2_DataOutputAssociation,
    bpmn2_DataInputAssociation,
    bpmn2_BoundaryEvent,
    bpmn2_LoopCharacteristics,
    FlowNode,
    bpmn2_ChoreographyActivity,
    bpmn2_Event,
    bpmn2_Gateway,
    bpmn2_Activity,
    Activity,
    bpmn2_CallActivity,
    bpmn2_SubProcess,
    bpmn2_Task,
    Task,
    bpmn2_SendTask,
    bpmn2_ScriptTask,
    bpmn2_BusinessRuleTask,
    bpmn2_ReceiveTask,
    bpmn2_ServiceTask,
    bpmn2_UserTask,
    bpmn2_ManualTask,
    GlobalTask,
    bpmn2_GlobalScriptTask,
    bpmn2_GlobalUserTask,
    bpmn2_GlobalBusinessRuleTask,
    bpmn2_GlobalManualTask,
    MultiInstanceBehavior,
    RelationshipDirection,
    ItemKind,
    ProcessType,
    ChoreographyLoopType,
    AdHocOrdering,
    EventBasedGatewayType,
    GatewayDirection,
    AssociationDirection,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_formalexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2_FormalExpression)


def test_bpmn2_formalexpression_constructor_exists():
    assert callable(bpmn2_FormalExpression.__init__)


def test_bpmn2_formalexpression_constructor_args():
    sig = inspect.signature(bpmn2_FormalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"

def test_bpmn2_formalexpression_has_language():
    assert hasattr(bpmn2_FormalExpression, "language")
    descriptor = None
    for klass in bpmn2_FormalExpression.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_interactionnode_is_not_abstract():
    assert not inspect.isabstract(bpmn2_InteractionNode)


def test_bpmn2_interactionnode_constructor_exists():
    assert callable(bpmn2_InteractionNode.__init__)


def test_bpmn2_interactionnode_constructor_args():
    sig = inspect.signature(bpmn2_InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_participantmultiplicity_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ParticipantMultiplicity)


def test_bpmn2_participantmultiplicity_constructor_exists():
    assert callable(bpmn2_ParticipantMultiplicity.__init__)


def test_bpmn2_participantmultiplicity_constructor_args():
    sig = inspect.signature(bpmn2_ParticipantMultiplicity.__init__)
    params = list(sig.parameters.keys())
    assert "minimum" in params, "Missing parameter 'minimum'"
    assert "maximum" in params, "Missing parameter 'maximum'"
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_participantmultiplicity_has_minimum():
    assert hasattr(bpmn2_ParticipantMultiplicity, "minimum")
    descriptor = None
    for klass in bpmn2_ParticipantMultiplicity.__mro__:
        if "minimum" in klass.__dict__:
            descriptor = klass.__dict__["minimum"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_participantmultiplicity_has_maximum():
    assert hasattr(bpmn2_ParticipantMultiplicity, "maximum")
    descriptor = None
    for klass in bpmn2_ParticipantMultiplicity.__mro__:
        if "maximum" in klass.__dict__:
            descriptor = klass.__dict__["maximum"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_participantmultiplicity_has_id():
    assert hasattr(bpmn2_ParticipantMultiplicity, "id")
    descriptor = None
    for klass in bpmn2_ParticipantMultiplicity.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_interactionnode_is_not_abstract():
    assert not inspect.isabstract(InteractionNode)


def test_interactionnode_constructor_exists():
    assert callable(InteractionNode.__init__)


def test_interactionnode_constructor_args():
    sig = inspect.signature(InteractionNode.__init__)
    params = list(sig.parameters.keys())



def test_collaboration_is_not_abstract():
    assert not inspect.isabstract(Collaboration)


def test_collaboration_constructor_exists():
    assert callable(Collaboration.__init__)


def test_collaboration_constructor_args():
    sig = inspect.signature(Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_flowelement_is_not_abstract():
    assert not inspect.isabstract(FlowElement)


def test_flowelement_constructor_exists():
    assert callable(FlowElement.__init__)


def test_flowelement_constructor_args():
    sig = inspect.signature(FlowElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_sequenceflow_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SequenceFlow)


def test_bpmn2_sequenceflow_constructor_exists():
    assert callable(bpmn2_SequenceFlow.__init__)


def test_bpmn2_sequenceflow_constructor_args():
    sig = inspect.signature(bpmn2_SequenceFlow.__init__)
    params = list(sig.parameters.keys())
    assert "isImmediate" in params, "Missing parameter 'isImmediate'"

def test_bpmn2_sequenceflow_has_isImmediate():
    assert hasattr(bpmn2_SequenceFlow, "isImmediate")
    descriptor = None
    for klass in bpmn2_SequenceFlow.__mro__:
        if "isImmediate" in klass.__dict__:
            descriptor = klass.__dict__["isImmediate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_flownode_is_not_abstract():
    assert not inspect.isabstract(bpmn2_FlowNode)


def test_bpmn2_flownode_constructor_exists():
    assert callable(bpmn2_FlowNode.__init__)


def test_bpmn2_flownode_constructor_args():
    sig = inspect.signature(bpmn2_FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(FlowElementsContainer)


def test_flowelementscontainer_constructor_exists():
    assert callable(FlowElementsContainer.__init__)


def test_flowelementscontainer_constructor_args():
    sig = inspect.signature(FlowElementsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_choreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Choreography)


def test_bpmn2_choreography_constructor_exists():
    assert callable(bpmn2_Choreography.__init__)


def test_bpmn2_choreography_constructor_args():
    sig = inspect.signature(bpmn2_Choreography.__init__)
    params = list(sig.parameters.keys())



def test_resourcerole_is_not_abstract():
    assert not inspect.isabstract(ResourceRole)


def test_resourcerole_constructor_exists():
    assert callable(ResourceRole.__init__)


def test_resourcerole_constructor_args():
    sig = inspect.signature(ResourceRole.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_performer_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Performer)


def test_bpmn2_performer_constructor_exists():
    assert callable(bpmn2_Performer.__init__)


def test_bpmn2_performer_constructor_args():
    sig = inspect.signature(bpmn2_Performer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_resourceassignmentexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ResourceAssignmentExpression)


def test_bpmn2_resourceassignmentexpression_constructor_exists():
    assert callable(bpmn2_ResourceAssignmentExpression.__init__)


def test_bpmn2_resourceassignmentexpression_constructor_args():
    sig = inspect.signature(bpmn2_ResourceAssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_resourceassignmentexpression_has_id():
    assert hasattr(bpmn2_ResourceAssignmentExpression, "id")
    descriptor = None
    for klass in bpmn2_ResourceAssignmentExpression.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_resourceparameterbinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ResourceParameterBinding)


def test_bpmn2_resourceparameterbinding_constructor_exists():
    assert callable(bpmn2_ResourceParameterBinding.__init__)


def test_bpmn2_resourceparameterbinding_constructor_args():
    sig = inspect.signature(bpmn2_ResourceParameterBinding.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_resourceparameterbinding_has_id():
    assert hasattr(bpmn2_ResourceParameterBinding, "id")
    descriptor = None
    for klass in bpmn2_ResourceParameterBinding.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(ItemAwareElement)


def test_itemawareelement_constructor_exists():
    assert callable(ItemAwareElement.__init__)


def test_itemawareelement_constructor_args():
    sig = inspect.signature(ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_property_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Property)


def test_bpmn2_property_constructor_exists():
    assert callable(bpmn2_Property.__init__)


def test_bpmn2_property_constructor_args():
    sig = inspect.signature(bpmn2_Property.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_property_has_name():
    assert hasattr(bpmn2_Property, "name")
    descriptor = None
    for klass in bpmn2_Property.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_dataoutput_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataOutput)


def test_bpmn2_dataoutput_constructor_exists():
    assert callable(bpmn2_DataOutput.__init__)


def test_bpmn2_dataoutput_constructor_args():
    sig = inspect.signature(bpmn2_DataOutput.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_dataoutput_has_isCollection():
    assert hasattr(bpmn2_DataOutput, "isCollection")
    descriptor = None
    for klass in bpmn2_DataOutput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_dataoutput_has_name():
    assert hasattr(bpmn2_DataOutput, "name")
    descriptor = None
    for klass in bpmn2_DataOutput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_import_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Import)


def test_bpmn2_import_constructor_exists():
    assert callable(bpmn2_Import.__init__)


def test_bpmn2_import_constructor_args():
    sig = inspect.signature(bpmn2_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importType" in params, "Missing parameter 'importType'"
    assert "namespace" in params, "Missing parameter 'namespace'"
    assert "id" in params, "Missing parameter 'id'"
    assert "location" in params, "Missing parameter 'location'"

def test_bpmn2_import_has_importType():
    assert hasattr(bpmn2_Import, "importType")
    descriptor = None
    for klass in bpmn2_Import.__mro__:
        if "importType" in klass.__dict__:
            descriptor = klass.__dict__["importType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_import_has_namespace():
    assert hasattr(bpmn2_Import, "namespace")
    descriptor = None
    for klass in bpmn2_Import.__mro__:
        if "namespace" in klass.__dict__:
            descriptor = klass.__dict__["namespace"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_import_has_id():
    assert hasattr(bpmn2_Import, "id")
    descriptor = None
    for klass in bpmn2_Import.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_import_has_location():
    assert hasattr(bpmn2_Import, "location")
    descriptor = None
    for klass in bpmn2_Import.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_datainput_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataInput)


def test_bpmn2_datainput_constructor_exists():
    assert callable(bpmn2_DataInput.__init__)


def test_bpmn2_datainput_constructor_args():
    sig = inspect.signature(bpmn2_DataInput.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2_datainput_has_name():
    assert hasattr(bpmn2_DataInput, "name")
    descriptor = None
    for klass in bpmn2_DataInput.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_datainput_has_isCollection():
    assert hasattr(bpmn2_DataInput, "isCollection")
    descriptor = None
    for klass in bpmn2_DataInput.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_inputoutputbinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2_InputOutputBinding)


def test_bpmn2_inputoutputbinding_constructor_exists():
    assert callable(bpmn2_InputOutputBinding.__init__)


def test_bpmn2_inputoutputbinding_constructor_args():
    sig = inspect.signature(bpmn2_InputOutputBinding.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_inputoutputbinding_has_id():
    assert hasattr(bpmn2_InputOutputBinding, "id")
    descriptor = None
    for klass in bpmn2_InputOutputBinding.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_callableelement_is_not_abstract():
    assert not inspect.isabstract(CallableElement)


def test_callableelement_constructor_exists():
    assert callable(CallableElement.__init__)


def test_callableelement_constructor_args():
    sig = inspect.signature(CallableElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_process_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Process)


def test_bpmn2_process_constructor_exists():
    assert callable(bpmn2_Process.__init__)


def test_bpmn2_process_constructor_args():
    sig = inspect.signature(bpmn2_Process.__init__)
    params = list(sig.parameters.keys())
    assert "processType" in params, "Missing parameter 'processType'"
    assert "isExecutable" in params, "Missing parameter 'isExecutable'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_bpmn2_process_has_processType():
    assert hasattr(bpmn2_Process, "processType")
    descriptor = None
    for klass in bpmn2_Process.__mro__:
        if "processType" in klass.__dict__:
            descriptor = klass.__dict__["processType"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_process_has_isExecutable():
    assert hasattr(bpmn2_Process, "isExecutable")
    descriptor = None
    for klass in bpmn2_Process.__mro__:
        if "isExecutable" in klass.__dict__:
            descriptor = klass.__dict__["isExecutable"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_process_has_isClosed():
    assert hasattr(bpmn2_Process, "isClosed")
    descriptor = None
    for klass in bpmn2_Process.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_globaltask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalTask)


def test_bpmn2_globaltask_constructor_exists():
    assert callable(bpmn2_GlobalTask.__init__)


def test_bpmn2_globaltask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_extensionattributedefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ExtensionAttributeDefinition)


def test_bpmn2_extensionattributedefinition_constructor_exists():
    assert callable(bpmn2_ExtensionAttributeDefinition.__init__)


def test_bpmn2_extensionattributedefinition_constructor_args():
    sig = inspect.signature(bpmn2_ExtensionAttributeDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "isReference" in params, "Missing parameter 'isReference'"

def test_bpmn2_extensionattributedefinition_has_type():
    assert hasattr(bpmn2_ExtensionAttributeDefinition, "type")
    descriptor = None
    for klass in bpmn2_ExtensionAttributeDefinition.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_extensionattributedefinition_has_name():
    assert hasattr(bpmn2_ExtensionAttributeDefinition, "name")
    descriptor = None
    for klass in bpmn2_ExtensionAttributeDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_extensionattributedefinition_has_id():
    assert hasattr(bpmn2_ExtensionAttributeDefinition, "id")
    descriptor = None
    for klass in bpmn2_ExtensionAttributeDefinition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_extensionattributedefinition_has_isReference():
    assert hasattr(bpmn2_ExtensionAttributeDefinition, "isReference")
    descriptor = None
    for klass in bpmn2_ExtensionAttributeDefinition.__mro__:
        if "isReference" in klass.__dict__:
            descriptor = klass.__dict__["isReference"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_extensionattributevalue_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ExtensionAttributeValue)


def test_bpmn2_extensionattributevalue_constructor_exists():
    assert callable(bpmn2_ExtensionAttributeValue.__init__)


def test_bpmn2_extensionattributevalue_constructor_args():
    sig = inspect.signature(bpmn2_ExtensionAttributeValue.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_extensionattributevalue_has_id():
    assert hasattr(bpmn2_ExtensionAttributeValue, "id")
    descriptor = None
    for klass in bpmn2_ExtensionAttributeValue.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_extensiondefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ExtensionDefinition)


def test_bpmn2_extensiondefinition_constructor_exists():
    assert callable(bpmn2_ExtensionDefinition.__init__)


def test_bpmn2_extensiondefinition_constructor_args():
    sig = inspect.signature(bpmn2_ExtensionDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_extensiondefinition_has_id():
    assert hasattr(bpmn2_ExtensionDefinition, "id")
    descriptor = None
    for klass in bpmn2_ExtensionDefinition.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_extensiondefinition_has_name():
    assert hasattr(bpmn2_ExtensionDefinition, "name")
    descriptor = None
    for klass in bpmn2_ExtensionDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_baseelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2_BaseElement)


def test_bpmn2_baseelement_constructor_exists():
    assert callable(bpmn2_BaseElement.__init__)


def test_bpmn2_baseelement_constructor_args():
    sig = inspect.signature(bpmn2_BaseElement.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_baseelement_has_description():
    assert hasattr(bpmn2_BaseElement, "description")
    descriptor = None
    for klass in bpmn2_BaseElement.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_baseelement_has_id():
    assert hasattr(bpmn2_BaseElement, "id")
    descriptor = None
    for klass in bpmn2_BaseElement.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_baseelement_is_not_abstract():
    assert not inspect.isabstract(BaseElement)


def test_baseelement_constructor_exists():
    assert callable(BaseElement.__init__)


def test_baseelement_constructor_args():
    sig = inspect.signature(BaseElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_flowelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2_FlowElement)


def test_bpmn2_flowelement_constructor_exists():
    assert callable(bpmn2_FlowElement.__init__)


def test_bpmn2_flowelement_constructor_args():
    sig = inspect.signature(bpmn2_FlowElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_flowelement_has_name():
    assert hasattr(bpmn2_FlowElement, "name")
    descriptor = None
    for klass in bpmn2_FlowElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_messageflowassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_MessageFlowAssociation)


def test_bpmn2_messageflowassociation_constructor_exists():
    assert callable(bpmn2_MessageFlowAssociation.__init__)


def test_bpmn2_messageflowassociation_constructor_args():
    sig = inspect.signature(bpmn2_MessageFlowAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_outputset_is_not_abstract():
    assert not inspect.isabstract(bpmn2_OutputSet)


def test_bpmn2_outputset_constructor_exists():
    assert callable(bpmn2_OutputSet.__init__)


def test_bpmn2_outputset_constructor_args():
    sig = inspect.signature(bpmn2_OutputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_outputset_has_name():
    assert hasattr(bpmn2_OutputSet, "name")
    descriptor = None
    for klass in bpmn2_OutputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_inputset_is_not_abstract():
    assert not inspect.isabstract(bpmn2_InputSet)


def test_bpmn2_inputset_constructor_exists():
    assert callable(bpmn2_InputSet.__init__)


def test_bpmn2_inputset_constructor_args():
    sig = inspect.signature(bpmn2_InputSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_inputset_has_name():
    assert hasattr(bpmn2_InputSet, "name")
    descriptor = None
    for klass in bpmn2_InputSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_correlationsubscription_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CorrelationSubscription)


def test_bpmn2_correlationsubscription_constructor_exists():
    assert callable(bpmn2_CorrelationSubscription.__init__)


def test_bpmn2_correlationsubscription_constructor_args():
    sig = inspect.signature(bpmn2_CorrelationSubscription.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_laneset_is_not_abstract():
    assert not inspect.isabstract(bpmn2_LaneSet)


def test_bpmn2_laneset_constructor_exists():
    assert callable(bpmn2_LaneSet.__init__)


def test_bpmn2_laneset_constructor_args():
    sig = inspect.signature(bpmn2_LaneSet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_laneset_has_name():
    assert hasattr(bpmn2_LaneSet, "name")
    descriptor = None
    for klass in bpmn2_LaneSet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_conversationlink_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ConversationLink)


def test_bpmn2_conversationlink_constructor_exists():
    assert callable(bpmn2_ConversationLink.__init__)


def test_bpmn2_conversationlink_constructor_args():
    sig = inspect.signature(bpmn2_ConversationLink.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_conversationlink_has_name():
    assert hasattr(bpmn2_ConversationLink, "name")
    descriptor = None
    for klass in bpmn2_ConversationLink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_flowelementscontainer_is_not_abstract():
    assert not inspect.isabstract(bpmn2_FlowElementsContainer)


def test_bpmn2_flowelementscontainer_constructor_exists():
    assert callable(bpmn2_FlowElementsContainer.__init__)


def test_bpmn2_flowelementscontainer_constructor_args():
    sig = inspect.signature(bpmn2_FlowElementsContainer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_monitoring_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Monitoring)


def test_bpmn2_monitoring_constructor_exists():
    assert callable(bpmn2_Monitoring.__init__)


def test_bpmn2_monitoring_constructor_args():
    sig = inspect.signature(bpmn2_Monitoring.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_inputoutputspecification_is_not_abstract():
    assert not inspect.isabstract(bpmn2_InputOutputSpecification)


def test_bpmn2_inputoutputspecification_constructor_exists():
    assert callable(bpmn2_InputOutputSpecification.__init__)


def test_bpmn2_inputoutputspecification_constructor_args():
    sig = inspect.signature(bpmn2_InputOutputSpecification.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_correlationpropertyretrievalexpression_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CorrelationPropertyRetrievalExpression)


def test_bpmn2_correlationpropertyretrievalexpression_constructor_exists():
    assert callable(bpmn2_CorrelationPropertyRetrievalExpression.__init__)


def test_bpmn2_correlationpropertyretrievalexpression_constructor_args():
    sig = inspect.signature(bpmn2_CorrelationPropertyRetrievalExpression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_lane_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Lane)


def test_bpmn2_lane_constructor_exists():
    assert callable(bpmn2_Lane.__init__)


def test_bpmn2_lane_constructor_args():
    sig = inspect.signature(bpmn2_Lane.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_lane_has_name():
    assert hasattr(bpmn2_Lane, "name")
    descriptor = None
    for klass in bpmn2_Lane.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_correlationkey_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CorrelationKey)


def test_bpmn2_correlationkey_constructor_exists():
    assert callable(bpmn2_CorrelationKey.__init__)


def test_bpmn2_correlationkey_constructor_args():
    sig = inspect.signature(bpmn2_CorrelationKey.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_correlationkey_has_name():
    assert hasattr(bpmn2_CorrelationKey, "name")
    descriptor = None
    for klass in bpmn2_CorrelationKey.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_artifact_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Artifact)


def test_bpmn2_artifact_constructor_exists():
    assert callable(bpmn2_Artifact.__init__)


def test_bpmn2_artifact_constructor_args():
    sig = inspect.signature(bpmn2_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_resourcerole_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ResourceRole)


def test_bpmn2_resourcerole_constructor_exists():
    assert callable(bpmn2_ResourceRole.__init__)


def test_bpmn2_resourcerole_constructor_args():
    sig = inspect.signature(bpmn2_ResourceRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_resourcerole_has_name():
    assert hasattr(bpmn2_ResourceRole, "name")
    descriptor = None
    for klass in bpmn2_ResourceRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_conversationnode_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ConversationNode)


def test_bpmn2_conversationnode_constructor_exists():
    assert callable(bpmn2_ConversationNode.__init__)


def test_bpmn2_conversationnode_constructor_args():
    sig = inspect.signature(bpmn2_ConversationNode.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_conversationnode_has_name():
    assert hasattr(bpmn2_ConversationNode, "name")
    descriptor = None
    for klass in bpmn2_ConversationNode.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_participantassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ParticipantAssociation)


def test_bpmn2_participantassociation_constructor_exists():
    assert callable(bpmn2_ParticipantAssociation.__init__)


def test_bpmn2_participantassociation_constructor_args():
    sig = inspect.signature(bpmn2_ParticipantAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_itemawareelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ItemAwareElement)


def test_bpmn2_itemawareelement_constructor_exists():
    assert callable(bpmn2_ItemAwareElement.__init__)


def test_bpmn2_itemawareelement_constructor_args():
    sig = inspect.signature(bpmn2_ItemAwareElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_messageflow_is_not_abstract():
    assert not inspect.isabstract(bpmn2_MessageFlow)


def test_bpmn2_messageflow_constructor_exists():
    assert callable(bpmn2_MessageFlow.__init__)


def test_bpmn2_messageflow_constructor_args():
    sig = inspect.signature(bpmn2_MessageFlow.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_messageflow_has_name():
    assert hasattr(bpmn2_MessageFlow, "name")
    descriptor = None
    for klass in bpmn2_MessageFlow.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_resourceparameter_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ResourceParameter)


def test_bpmn2_resourceparameter_constructor_exists():
    assert callable(bpmn2_ResourceParameter.__init__)


def test_bpmn2_resourceparameter_constructor_args():
    sig = inspect.signature(bpmn2_ResourceParameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isRequired" in params, "Missing parameter 'isRequired'"

def test_bpmn2_resourceparameter_has_name():
    assert hasattr(bpmn2_ResourceParameter, "name")
    descriptor = None
    for klass in bpmn2_ResourceParameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_resourceparameter_has_isRequired():
    assert hasattr(bpmn2_ResourceParameter, "isRequired")
    descriptor = None
    for klass in bpmn2_ResourceParameter.__mro__:
        if "isRequired" in klass.__dict__:
            descriptor = klass.__dict__["isRequired"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_categoryvalue_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CategoryValue)


def test_bpmn2_categoryvalue_constructor_exists():
    assert callable(bpmn2_CategoryValue.__init__)


def test_bpmn2_categoryvalue_constructor_args():
    sig = inspect.signature(bpmn2_CategoryValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_bpmn2_categoryvalue_has_value():
    assert hasattr(bpmn2_CategoryValue, "value")
    descriptor = None
    for klass in bpmn2_CategoryValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_expression_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Expression)


def test_bpmn2_expression_constructor_exists():
    assert callable(bpmn2_Expression.__init__)


def test_bpmn2_expression_constructor_args():
    sig = inspect.signature(bpmn2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_correlationpropertybinding_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CorrelationPropertyBinding)


def test_bpmn2_correlationpropertybinding_constructor_exists():
    assert callable(bpmn2_CorrelationPropertyBinding.__init__)


def test_bpmn2_correlationpropertybinding_constructor_args():
    sig = inspect.signature(bpmn2_CorrelationPropertyBinding.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_participant_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Participant)


def test_bpmn2_participant_constructor_exists():
    assert callable(bpmn2_Participant.__init__)


def test_bpmn2_participant_constructor_args():
    sig = inspect.signature(bpmn2_Participant.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_participant_has_name():
    assert hasattr(bpmn2_Participant, "name")
    descriptor = None
    for klass in bpmn2_Participant.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_auditing_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Auditing)


def test_bpmn2_auditing_constructor_exists():
    assert callable(bpmn2_Auditing.__init__)


def test_bpmn2_auditing_constructor_args():
    sig = inspect.signature(bpmn2_Auditing.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_datastate_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataState)


def test_bpmn2_datastate_constructor_exists():
    assert callable(bpmn2_DataState.__init__)


def test_bpmn2_datastate_constructor_args():
    sig = inspect.signature(bpmn2_DataState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_datastate_has_name():
    assert hasattr(bpmn2_DataState, "name")
    descriptor = None
    for klass in bpmn2_DataState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_conversationassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ConversationAssociation)


def test_bpmn2_conversationassociation_constructor_exists():
    assert callable(bpmn2_ConversationAssociation.__init__)


def test_bpmn2_conversationassociation_constructor_args():
    sig = inspect.signature(bpmn2_ConversationAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_documentation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Documentation)


def test_bpmn2_documentation_constructor_exists():
    assert callable(bpmn2_Documentation.__init__)


def test_bpmn2_documentation_constructor_args():
    sig = inspect.signature(bpmn2_Documentation.__init__)
    params = list(sig.parameters.keys())
    assert "textFormat" in params, "Missing parameter 'textFormat'"
    assert "text" in params, "Missing parameter 'text'"

def test_bpmn2_documentation_has_textFormat():
    assert hasattr(bpmn2_Documentation, "textFormat")
    descriptor = None
    for klass in bpmn2_Documentation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_documentation_has_text():
    assert hasattr(bpmn2_Documentation, "text")
    descriptor = None
    for klass in bpmn2_Documentation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_rootelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2_RootElement)


def test_bpmn2_rootelement_constructor_exists():
    assert callable(bpmn2_RootElement.__init__)


def test_bpmn2_rootelement_constructor_args():
    sig = inspect.signature(bpmn2_RootElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_eobject_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EObject)


def test_bpmn2_eobject_constructor_exists():
    assert callable(bpmn2_EObject.__init__)


def test_bpmn2_eobject_constructor_args():
    sig = inspect.signature(bpmn2_EObject.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_operation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Operation)


def test_bpmn2_operation_constructor_exists():
    assert callable(bpmn2_Operation.__init__)


def test_bpmn2_operation_constructor_args():
    sig = inspect.signature(bpmn2_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_operation_has_name():
    assert hasattr(bpmn2_Operation, "name")
    descriptor = None
    for klass in bpmn2_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rootelement_is_not_abstract():
    assert not inspect.isabstract(RootElement)


def test_rootelement_constructor_exists():
    assert callable(RootElement.__init__)


def test_rootelement_constructor_args():
    sig = inspect.signature(RootElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_callableelement_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CallableElement)


def test_bpmn2_callableelement_constructor_exists():
    assert callable(bpmn2_CallableElement.__init__)


def test_bpmn2_callableelement_constructor_args():
    sig = inspect.signature(bpmn2_CallableElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_callableelement_has_name():
    assert hasattr(bpmn2_CallableElement, "name")
    descriptor = None
    for klass in bpmn2_CallableElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_endpoint_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EndPoint)


def test_bpmn2_endpoint_constructor_exists():
    assert callable(bpmn2_EndPoint.__init__)


def test_bpmn2_endpoint_constructor_args():
    sig = inspect.signature(bpmn2_EndPoint.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_resource_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Resource)


def test_bpmn2_resource_constructor_exists():
    assert callable(bpmn2_Resource.__init__)


def test_bpmn2_resource_constructor_args():
    sig = inspect.signature(bpmn2_Resource.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_resource_has_name():
    assert hasattr(bpmn2_Resource, "name")
    descriptor = None
    for klass in bpmn2_Resource.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_collaboration_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Collaboration)


def test_bpmn2_collaboration_constructor_exists():
    assert callable(bpmn2_Collaboration.__init__)


def test_bpmn2_collaboration_constructor_args():
    sig = inspect.signature(bpmn2_Collaboration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_bpmn2_collaboration_has_name():
    assert hasattr(bpmn2_Collaboration, "name")
    descriptor = None
    for klass in bpmn2_Collaboration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_collaboration_has_isClosed():
    assert hasattr(bpmn2_Collaboration, "isClosed")
    descriptor = None
    for klass in bpmn2_Collaboration.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_correlationproperty_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CorrelationProperty)


def test_bpmn2_correlationproperty_constructor_exists():
    assert callable(bpmn2_CorrelationProperty.__init__)


def test_bpmn2_correlationproperty_constructor_args():
    sig = inspect.signature(bpmn2_CorrelationProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_correlationproperty_has_name():
    assert hasattr(bpmn2_CorrelationProperty, "name")
    descriptor = None
    for klass in bpmn2_CorrelationProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_itemdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ItemDefinition)


def test_bpmn2_itemdefinition_constructor_exists():
    assert callable(bpmn2_ItemDefinition.__init__)


def test_bpmn2_itemdefinition_constructor_args():
    sig = inspect.signature(bpmn2_ItemDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"
    assert "itemKind" in params, "Missing parameter 'itemKind'"

def test_bpmn2_itemdefinition_has_isCollection():
    assert hasattr(bpmn2_ItemDefinition, "isCollection")
    descriptor = None
    for klass in bpmn2_ItemDefinition.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_itemdefinition_has_itemKind():
    assert hasattr(bpmn2_ItemDefinition, "itemKind")
    descriptor = None
    for klass in bpmn2_ItemDefinition.__mro__:
        if "itemKind" in klass.__dict__:
            descriptor = klass.__dict__["itemKind"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_error_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Error)


def test_bpmn2_error_constructor_exists():
    assert callable(bpmn2_Error.__init__)


def test_bpmn2_error_constructor_args():
    sig = inspect.signature(bpmn2_Error.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "errorCode" in params, "Missing parameter 'errorCode'"

def test_bpmn2_error_has_name():
    assert hasattr(bpmn2_Error, "name")
    descriptor = None
    for klass in bpmn2_Error.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_error_has_errorCode():
    assert hasattr(bpmn2_Error, "errorCode")
    descriptor = None
    for klass in bpmn2_Error.__mro__:
        if "errorCode" in klass.__dict__:
            descriptor = klass.__dict__["errorCode"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_message_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Message)


def test_bpmn2_message_constructor_exists():
    assert callable(bpmn2_Message.__init__)


def test_bpmn2_message_constructor_args():
    sig = inspect.signature(bpmn2_Message.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_message_has_name():
    assert hasattr(bpmn2_Message, "name")
    descriptor = None
    for klass in bpmn2_Message.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_interface_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Interface)


def test_bpmn2_interface_constructor_exists():
    assert callable(bpmn2_Interface.__init__)


def test_bpmn2_interface_constructor_args():
    sig = inspect.signature(bpmn2_Interface.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_interface_has_name():
    assert hasattr(bpmn2_Interface, "name")
    descriptor = None
    for klass in bpmn2_Interface.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_bpmndiagram_is_not_abstract():
    assert not inspect.isabstract(bpmn2_BPMNDiagram)


def test_bpmn2_bpmndiagram_constructor_exists():
    assert callable(bpmn2_BPMNDiagram.__init__)


def test_bpmn2_bpmndiagram_constructor_args():
    sig = inspect.signature(bpmn2_BPMNDiagram.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_definitions_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Definitions)


def test_bpmn2_definitions_constructor_exists():
    assert callable(bpmn2_Definitions.__init__)


def test_bpmn2_definitions_constructor_args():
    sig = inspect.signature(bpmn2_Definitions.__init__)
    params = list(sig.parameters.keys())
    assert "exporter" in params, "Missing parameter 'exporter'"
    assert "name" in params, "Missing parameter 'name'"
    assert "exporterVersion" in params, "Missing parameter 'exporterVersion'"
    assert "typeLanguage" in params, "Missing parameter 'typeLanguage'"
    assert "expressionLanguage" in params, "Missing parameter 'expressionLanguage'"
    assert "targetNamespace" in params, "Missing parameter 'targetNamespace'"

def test_bpmn2_definitions_has_exporter():
    assert hasattr(bpmn2_Definitions, "exporter")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "exporter" in klass.__dict__:
            descriptor = klass.__dict__["exporter"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_definitions_has_name():
    assert hasattr(bpmn2_Definitions, "name")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_definitions_has_exporterVersion():
    assert hasattr(bpmn2_Definitions, "exporterVersion")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "exporterVersion" in klass.__dict__:
            descriptor = klass.__dict__["exporterVersion"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_definitions_has_typeLanguage():
    assert hasattr(bpmn2_Definitions, "typeLanguage")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "typeLanguage" in klass.__dict__:
            descriptor = klass.__dict__["typeLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_definitions_has_expressionLanguage():
    assert hasattr(bpmn2_Definitions, "expressionLanguage")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "expressionLanguage" in klass.__dict__:
            descriptor = klass.__dict__["expressionLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_definitions_has_targetNamespace():
    assert hasattr(bpmn2_Definitions, "targetNamespace")
    descriptor = None
    for klass in bpmn2_Definitions.__mro__:
        if "targetNamespace" in klass.__dict__:
            descriptor = klass.__dict__["targetNamespace"]
            break
    assert isinstance(descriptor, property)



def test_subprocess_is_not_abstract():
    assert not inspect.isabstract(SubProcess)


def test_subprocess_constructor_exists():
    assert callable(SubProcess.__init__)


def test_subprocess_constructor_args():
    sig = inspect.signature(SubProcess.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_transaction_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Transaction)


def test_bpmn2_transaction_constructor_exists():
    assert callable(bpmn2_Transaction.__init__)


def test_bpmn2_transaction_constructor_args():
    sig = inspect.signature(bpmn2_Transaction.__init__)
    params = list(sig.parameters.keys())
    assert "protocol" in params, "Missing parameter 'protocol'"
    assert "method" in params, "Missing parameter 'method'"

def test_bpmn2_transaction_has_protocol():
    assert hasattr(bpmn2_Transaction, "protocol")
    descriptor = None
    for klass in bpmn2_Transaction.__mro__:
        if "protocol" in klass.__dict__:
            descriptor = klass.__dict__["protocol"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_transaction_has_method():
    assert hasattr(bpmn2_Transaction, "method")
    descriptor = None
    for klass in bpmn2_Transaction.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_adhocsubprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn2_AdHocSubProcess)


def test_bpmn2_adhocsubprocess_constructor_exists():
    assert callable(bpmn2_AdHocSubProcess.__init__)


def test_bpmn2_adhocsubprocess_constructor_args():
    sig = inspect.signature(bpmn2_AdHocSubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "ordering" in params, "Missing parameter 'ordering'"
    assert "cancelRemainingInstances" in params, "Missing parameter 'cancelRemainingInstances'"

def test_bpmn2_adhocsubprocess_has_ordering():
    assert hasattr(bpmn2_AdHocSubProcess, "ordering")
    descriptor = None
    for klass in bpmn2_AdHocSubProcess.__mro__:
        if "ordering" in klass.__dict__:
            descriptor = klass.__dict__["ordering"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_adhocsubprocess_has_cancelRemainingInstances():
    assert hasattr(bpmn2_AdHocSubProcess, "cancelRemainingInstances")
    descriptor = None
    for klass in bpmn2_AdHocSubProcess.__mro__:
        if "cancelRemainingInstances" in klass.__dict__:
            descriptor = klass.__dict__["cancelRemainingInstances"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_complexbehaviordefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ComplexBehaviorDefinition)


def test_bpmn2_complexbehaviordefinition_constructor_exists():
    assert callable(bpmn2_ComplexBehaviorDefinition.__init__)


def test_bpmn2_complexbehaviordefinition_constructor_args():
    sig = inspect.signature(bpmn2_ComplexBehaviorDefinition.__init__)
    params = list(sig.parameters.keys())



def test_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(LoopCharacteristics)


def test_loopcharacteristics_constructor_exists():
    assert callable(LoopCharacteristics.__init__)


def test_loopcharacteristics_constructor_args():
    sig = inspect.signature(LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_standardloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2_StandardLoopCharacteristics)


def test_bpmn2_standardloopcharacteristics_constructor_exists():
    assert callable(bpmn2_StandardLoopCharacteristics.__init__)


def test_bpmn2_standardloopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2_StandardLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "testBefore" in params, "Missing parameter 'testBefore'"

def test_bpmn2_standardloopcharacteristics_has_testBefore():
    assert hasattr(bpmn2_StandardLoopCharacteristics, "testBefore")
    descriptor = None
    for klass in bpmn2_StandardLoopCharacteristics.__mro__:
        if "testBefore" in klass.__dict__:
            descriptor = klass.__dict__["testBefore"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_multiinstanceloopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2_MultiInstanceLoopCharacteristics)


def test_bpmn2_multiinstanceloopcharacteristics_constructor_exists():
    assert callable(bpmn2_MultiInstanceLoopCharacteristics.__init__)


def test_bpmn2_multiinstanceloopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2_MultiInstanceLoopCharacteristics.__init__)
    params = list(sig.parameters.keys())
    assert "isSequential" in params, "Missing parameter 'isSequential'"
    assert "behavior" in params, "Missing parameter 'behavior'"

def test_bpmn2_multiinstanceloopcharacteristics_has_isSequential():
    assert hasattr(bpmn2_MultiInstanceLoopCharacteristics, "isSequential")
    descriptor = None
    for klass in bpmn2_MultiInstanceLoopCharacteristics.__mro__:
        if "isSequential" in klass.__dict__:
            descriptor = klass.__dict__["isSequential"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_multiinstanceloopcharacteristics_has_behavior():
    assert hasattr(bpmn2_MultiInstanceLoopCharacteristics, "behavior")
    descriptor = None
    for klass in bpmn2_MultiInstanceLoopCharacteristics.__mro__:
        if "behavior" in klass.__dict__:
            descriptor = klass.__dict__["behavior"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_category_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Category)


def test_bpmn2_category_constructor_exists():
    assert callable(bpmn2_Category.__init__)


def test_bpmn2_category_constructor_args():
    sig = inspect.signature(bpmn2_Category.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_category_has_name():
    assert hasattr(bpmn2_Category, "name")
    descriptor = None
    for klass in bpmn2_Category.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_association_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Association)


def test_bpmn2_association_constructor_exists():
    assert callable(bpmn2_Association.__init__)


def test_bpmn2_association_constructor_args():
    sig = inspect.signature(bpmn2_Association.__init__)
    params = list(sig.parameters.keys())
    assert "associationDirection" in params, "Missing parameter 'associationDirection'"

def test_bpmn2_association_has_associationDirection():
    assert hasattr(bpmn2_Association, "associationDirection")
    descriptor = None
    for klass in bpmn2_Association.__mro__:
        if "associationDirection" in klass.__dict__:
            descriptor = klass.__dict__["associationDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_group_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Group)


def test_bpmn2_group_constructor_exists():
    assert callable(bpmn2_Group.__init__)


def test_bpmn2_group_constructor_args():
    sig = inspect.signature(bpmn2_Group.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_textannotation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_TextAnnotation)


def test_bpmn2_textannotation_constructor_exists():
    assert callable(bpmn2_TextAnnotation.__init__)


def test_bpmn2_textannotation_constructor_args():
    sig = inspect.signature(bpmn2_TextAnnotation.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "textFormat" in params, "Missing parameter 'textFormat'"

def test_bpmn2_textannotation_has_text():
    assert hasattr(bpmn2_TextAnnotation, "text")
    descriptor = None
    for klass in bpmn2_TextAnnotation.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_textannotation_has_textFormat():
    assert hasattr(bpmn2_TextAnnotation, "textFormat")
    descriptor = None
    for klass in bpmn2_TextAnnotation.__mro__:
        if "textFormat" in klass.__dict__:
            descriptor = klass.__dict__["textFormat"]
            break
    assert isinstance(descriptor, property)



def test_choreography_is_not_abstract():
    assert not inspect.isabstract(Choreography)


def test_choreography_constructor_exists():
    assert callable(Choreography.__init__)


def test_choreography_constructor_args():
    sig = inspect.signature(Choreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_globalchoreographytask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalChoreographyTask)


def test_bpmn2_globalchoreographytask_constructor_exists():
    assert callable(bpmn2_GlobalChoreographyTask.__init__)


def test_bpmn2_globalchoreographytask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(ChoreographyActivity)


def test_choreographyactivity_constructor_exists():
    assert callable(ChoreographyActivity.__init__)


def test_choreographyactivity_constructor_args():
    sig = inspect.signature(ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_subchoreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SubChoreography)


def test_bpmn2_subchoreography_constructor_exists():
    assert callable(bpmn2_SubChoreography.__init__)


def test_bpmn2_subchoreography_constructor_args():
    sig = inspect.signature(bpmn2_SubChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_choreographytask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ChoreographyTask)


def test_bpmn2_choreographytask_constructor_exists():
    assert callable(bpmn2_ChoreographyTask.__init__)


def test_bpmn2_choreographytask_constructor_args():
    sig = inspect.signature(bpmn2_ChoreographyTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_callchoreography_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CallChoreography)


def test_bpmn2_callchoreography_constructor_exists():
    assert callable(bpmn2_CallChoreography.__init__)


def test_bpmn2_callchoreography_constructor_args():
    sig = inspect.signature(bpmn2_CallChoreography.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_partnerrole_is_not_abstract():
    assert not inspect.isabstract(bpmn2_PartnerRole)


def test_bpmn2_partnerrole_constructor_exists():
    assert callable(bpmn2_PartnerRole.__init__)


def test_bpmn2_partnerrole_constructor_args():
    sig = inspect.signature(bpmn2_PartnerRole.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_partnerrole_has_name():
    assert hasattr(bpmn2_PartnerRole, "name")
    descriptor = None
    for klass in bpmn2_PartnerRole.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_partnerentity_is_not_abstract():
    assert not inspect.isabstract(bpmn2_PartnerEntity)


def test_bpmn2_partnerentity_constructor_exists():
    assert callable(bpmn2_PartnerEntity.__init__)


def test_bpmn2_partnerentity_constructor_args():
    sig = inspect.signature(bpmn2_PartnerEntity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_partnerentity_has_name():
    assert hasattr(bpmn2_PartnerEntity, "name")
    descriptor = None
    for klass in bpmn2_PartnerEntity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_globalconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalConversation)


def test_bpmn2_globalconversation_constructor_exists():
    assert callable(bpmn2_GlobalConversation.__init__)


def test_bpmn2_globalconversation_constructor_args():
    sig = inspect.signature(bpmn2_GlobalConversation.__init__)
    params = list(sig.parameters.keys())



def test_conversationnode_is_not_abstract():
    assert not inspect.isabstract(ConversationNode)


def test_conversationnode_constructor_exists():
    assert callable(ConversationNode.__init__)


def test_conversationnode_constructor_args():
    sig = inspect.signature(ConversationNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_conversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Conversation)


def test_bpmn2_conversation_constructor_exists():
    assert callable(bpmn2_Conversation.__init__)


def test_bpmn2_conversation_constructor_args():
    sig = inspect.signature(bpmn2_Conversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_subconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SubConversation)


def test_bpmn2_subconversation_constructor_exists():
    assert callable(bpmn2_SubConversation.__init__)


def test_bpmn2_subconversation_constructor_args():
    sig = inspect.signature(bpmn2_SubConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_callconversation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CallConversation)


def test_bpmn2_callconversation_constructor_exists():
    assert callable(bpmn2_CallConversation.__init__)


def test_bpmn2_callconversation_constructor_args():
    sig = inspect.signature(bpmn2_CallConversation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_dataobjectreference_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataObjectReference)


def test_bpmn2_dataobjectreference_constructor_exists():
    assert callable(bpmn2_DataObjectReference.__init__)


def test_bpmn2_dataobjectreference_constructor_args():
    sig = inspect.signature(bpmn2_DataObjectReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_datastorereference_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataStoreReference)


def test_bpmn2_datastorereference_constructor_exists():
    assert callable(bpmn2_DataStoreReference.__init__)


def test_bpmn2_datastorereference_constructor_args():
    sig = inspect.signature(bpmn2_DataStoreReference.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_datastore_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataStore)


def test_bpmn2_datastore_constructor_exists():
    assert callable(bpmn2_DataStore.__init__)


def test_bpmn2_datastore_constructor_args():
    sig = inspect.signature(bpmn2_DataStore.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "isUnlimited" in params, "Missing parameter 'isUnlimited'"
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_datastore_has_capacity():
    assert hasattr(bpmn2_DataStore, "capacity")
    descriptor = None
    for klass in bpmn2_DataStore.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_datastore_has_isUnlimited():
    assert hasattr(bpmn2_DataStore, "isUnlimited")
    descriptor = None
    for klass in bpmn2_DataStore.__mro__:
        if "isUnlimited" in klass.__dict__:
            descriptor = klass.__dict__["isUnlimited"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_datastore_has_name():
    assert hasattr(bpmn2_DataStore, "name")
    descriptor = None
    for klass in bpmn2_DataStore.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_dataobject_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataObject)


def test_bpmn2_dataobject_constructor_exists():
    assert callable(bpmn2_DataObject.__init__)


def test_bpmn2_dataobject_constructor_args():
    sig = inspect.signature(bpmn2_DataObject.__init__)
    params = list(sig.parameters.keys())
    assert "isCollection" in params, "Missing parameter 'isCollection'"

def test_bpmn2_dataobject_has_isCollection():
    assert hasattr(bpmn2_DataObject, "isCollection")
    descriptor = None
    for klass in bpmn2_DataObject.__mro__:
        if "isCollection" in klass.__dict__:
            descriptor = klass.__dict__["isCollection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_signal_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Signal)


def test_bpmn2_signal_constructor_exists():
    assert callable(bpmn2_Signal.__init__)


def test_bpmn2_signal_constructor_args():
    sig = inspect.signature(bpmn2_Signal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_signal_has_name():
    assert hasattr(bpmn2_Signal, "name")
    descriptor = None
    for klass in bpmn2_Signal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_escalation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Escalation)


def test_bpmn2_escalation_constructor_exists():
    assert callable(bpmn2_Escalation.__init__)


def test_bpmn2_escalation_constructor_args():
    sig = inspect.signature(bpmn2_Escalation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "escalationCode" in params, "Missing parameter 'escalationCode'"
    assert "id" in params, "Missing parameter 'id'"

def test_bpmn2_escalation_has_name():
    assert hasattr(bpmn2_Escalation, "name")
    descriptor = None
    for klass in bpmn2_Escalation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_escalation_has_escalationCode():
    assert hasattr(bpmn2_Escalation, "escalationCode")
    descriptor = None
    for klass in bpmn2_Escalation.__mro__:
        if "escalationCode" in klass.__dict__:
            descriptor = klass.__dict__["escalationCode"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_escalation_has_id():
    assert hasattr(bpmn2_Escalation, "id")
    descriptor = None
    for klass in bpmn2_Escalation.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(EventDefinition)


def test_eventdefinition_constructor_exists():
    assert callable(EventDefinition.__init__)


def test_eventdefinition_constructor_args():
    sig = inspect.signature(EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_signaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SignalEventDefinition)


def test_bpmn2_signaleventdefinition_constructor_exists():
    assert callable(bpmn2_SignalEventDefinition.__init__)


def test_bpmn2_signaleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_SignalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_compensateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CompensateEventDefinition)


def test_bpmn2_compensateeventdefinition_constructor_exists():
    assert callable(bpmn2_CompensateEventDefinition.__init__)


def test_bpmn2_compensateeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_CompensateEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "waitForCompletion" in params, "Missing parameter 'waitForCompletion'"

def test_bpmn2_compensateeventdefinition_has_waitForCompletion():
    assert hasattr(bpmn2_CompensateEventDefinition, "waitForCompletion")
    descriptor = None
    for klass in bpmn2_CompensateEventDefinition.__mro__:
        if "waitForCompletion" in klass.__dict__:
            descriptor = klass.__dict__["waitForCompletion"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_conditionaleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ConditionalEventDefinition)


def test_bpmn2_conditionaleventdefinition_constructor_exists():
    assert callable(bpmn2_ConditionalEventDefinition.__init__)


def test_bpmn2_conditionaleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_ConditionalEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_messageeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_MessageEventDefinition)


def test_bpmn2_messageeventdefinition_constructor_exists():
    assert callable(bpmn2_MessageEventDefinition.__init__)


def test_bpmn2_messageeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_MessageEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_erroreventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ErrorEventDefinition)


def test_bpmn2_erroreventdefinition_constructor_exists():
    assert callable(bpmn2_ErrorEventDefinition.__init__)


def test_bpmn2_erroreventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_ErrorEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_timereventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_TimerEventDefinition)


def test_bpmn2_timereventdefinition_constructor_exists():
    assert callable(bpmn2_TimerEventDefinition.__init__)


def test_bpmn2_timereventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_TimerEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_escalationeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EscalationEventDefinition)


def test_bpmn2_escalationeventdefinition_constructor_exists():
    assert callable(bpmn2_EscalationEventDefinition.__init__)


def test_bpmn2_escalationeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_EscalationEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_terminateeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_TerminateEventDefinition)


def test_bpmn2_terminateeventdefinition_constructor_exists():
    assert callable(bpmn2_TerminateEventDefinition.__init__)


def test_bpmn2_terminateeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_TerminateEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_linkeventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_LinkEventDefinition)


def test_bpmn2_linkeventdefinition_constructor_exists():
    assert callable(bpmn2_LinkEventDefinition.__init__)


def test_bpmn2_linkeventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_LinkEventDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bpmn2_linkeventdefinition_has_name():
    assert hasattr(bpmn2_LinkEventDefinition, "name")
    descriptor = None
    for klass in bpmn2_LinkEventDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_canceleventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CancelEventDefinition)


def test_bpmn2_canceleventdefinition_constructor_exists():
    assert callable(bpmn2_CancelEventDefinition.__init__)


def test_bpmn2_canceleventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_CancelEventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_throwevent_is_not_abstract():
    assert not inspect.isabstract(ThrowEvent)


def test_throwevent_constructor_exists():
    assert callable(ThrowEvent.__init__)


def test_throwevent_constructor_args():
    sig = inspect.signature(ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_implicitthrowevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ImplicitThrowEvent)


def test_bpmn2_implicitthrowevent_constructor_exists():
    assert callable(bpmn2_ImplicitThrowEvent.__init__)


def test_bpmn2_implicitthrowevent_constructor_args():
    sig = inspect.signature(bpmn2_ImplicitThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_endevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EndEvent)


def test_bpmn2_endevent_constructor_exists():
    assert callable(bpmn2_EndEvent.__init__)


def test_bpmn2_endevent_constructor_args():
    sig = inspect.signature(bpmn2_EndEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_intermediatethrowevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_IntermediateThrowEvent)


def test_bpmn2_intermediatethrowevent_constructor_exists():
    assert callable(bpmn2_IntermediateThrowEvent.__init__)


def test_bpmn2_intermediatethrowevent_constructor_args():
    sig = inspect.signature(bpmn2_IntermediateThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_extension_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Extension)


def test_bpmn2_extension_constructor_exists():
    assert callable(bpmn2_Extension.__init__)


def test_bpmn2_extension_constructor_args():
    sig = inspect.signature(bpmn2_Extension.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "mustUnderstand" in params, "Missing parameter 'mustUnderstand'"

def test_bpmn2_extension_has_id():
    assert hasattr(bpmn2_Extension, "id")
    descriptor = None
    for klass in bpmn2_Extension.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_extension_has_mustUnderstand():
    assert hasattr(bpmn2_Extension, "mustUnderstand")
    descriptor = None
    for klass in bpmn2_Extension.__mro__:
        if "mustUnderstand" in klass.__dict__:
            descriptor = klass.__dict__["mustUnderstand"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_relationship_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Relationship)


def test_bpmn2_relationship_constructor_exists():
    assert callable(bpmn2_Relationship.__init__)


def test_bpmn2_relationship_constructor_args():
    sig = inspect.signature(bpmn2_Relationship.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "direction" in params, "Missing parameter 'direction'"

def test_bpmn2_relationship_has_type():
    assert hasattr(bpmn2_Relationship, "type")
    descriptor = None
    for klass in bpmn2_Relationship.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_relationship_has_direction():
    assert hasattr(bpmn2_Relationship, "direction")
    descriptor = None
    for klass in bpmn2_Relationship.__mro__:
        if "direction" in klass.__dict__:
            descriptor = klass.__dict__["direction"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_assignment_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Assignment)


def test_bpmn2_assignment_constructor_exists():
    assert callable(bpmn2_Assignment.__init__)


def test_bpmn2_assignment_constructor_args():
    sig = inspect.signature(bpmn2_Assignment.__init__)
    params = list(sig.parameters.keys())



def test_gateway_is_not_abstract():
    assert not inspect.isabstract(Gateway)


def test_gateway_constructor_exists():
    assert callable(Gateway.__init__)


def test_gateway_constructor_args():
    sig = inspect.signature(Gateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_parallelgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ParallelGateway)


def test_bpmn2_parallelgateway_constructor_exists():
    assert callable(bpmn2_ParallelGateway.__init__)


def test_bpmn2_parallelgateway_constructor_args():
    sig = inspect.signature(bpmn2_ParallelGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_exclusivegateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ExclusiveGateway)


def test_bpmn2_exclusivegateway_constructor_exists():
    assert callable(bpmn2_ExclusiveGateway.__init__)


def test_bpmn2_exclusivegateway_constructor_args():
    sig = inspect.signature(bpmn2_ExclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_complexgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ComplexGateway)


def test_bpmn2_complexgateway_constructor_exists():
    assert callable(bpmn2_ComplexGateway.__init__)


def test_bpmn2_complexgateway_constructor_args():
    sig = inspect.signature(bpmn2_ComplexGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_inclusivegateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_InclusiveGateway)


def test_bpmn2_inclusivegateway_constructor_exists():
    assert callable(bpmn2_InclusiveGateway.__init__)


def test_bpmn2_inclusivegateway_constructor_args():
    sig = inspect.signature(bpmn2_InclusiveGateway.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_eventbasedgateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EventBasedGateway)


def test_bpmn2_eventbasedgateway_constructor_exists():
    assert callable(bpmn2_EventBasedGateway.__init__)


def test_bpmn2_eventbasedgateway_constructor_args():
    sig = inspect.signature(bpmn2_EventBasedGateway.__init__)
    params = list(sig.parameters.keys())
    assert "instantiate" in params, "Missing parameter 'instantiate'"
    assert "eventGatewayType" in params, "Missing parameter 'eventGatewayType'"

def test_bpmn2_eventbasedgateway_has_instantiate():
    assert hasattr(bpmn2_EventBasedGateway, "instantiate")
    descriptor = None
    for klass in bpmn2_EventBasedGateway.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_eventbasedgateway_has_eventGatewayType():
    assert hasattr(bpmn2_EventBasedGateway, "eventGatewayType")
    descriptor = None
    for klass in bpmn2_EventBasedGateway.__mro__:
        if "eventGatewayType" in klass.__dict__:
            descriptor = klass.__dict__["eventGatewayType"]
            break
    assert isinstance(descriptor, property)



def test_humanperformer_is_not_abstract():
    assert not inspect.isabstract(HumanPerformer)


def test_humanperformer_constructor_exists():
    assert callable(HumanPerformer.__init__)


def test_humanperformer_constructor_args():
    sig = inspect.signature(HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_potentialowner_is_not_abstract():
    assert not inspect.isabstract(bpmn2_PotentialOwner)


def test_bpmn2_potentialowner_constructor_exists():
    assert callable(bpmn2_PotentialOwner.__init__)


def test_bpmn2_potentialowner_constructor_args():
    sig = inspect.signature(bpmn2_PotentialOwner.__init__)
    params = list(sig.parameters.keys())



def test_performer_is_not_abstract():
    assert not inspect.isabstract(Performer)


def test_performer_constructor_exists():
    assert callable(Performer.__init__)


def test_performer_constructor_args():
    sig = inspect.signature(Performer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_humanperformer_is_not_abstract():
    assert not inspect.isabstract(bpmn2_HumanPerformer)


def test_bpmn2_humanperformer_constructor_exists():
    assert callable(bpmn2_HumanPerformer.__init__)


def test_bpmn2_humanperformer_constructor_args():
    sig = inspect.signature(bpmn2_HumanPerformer.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_rendering_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Rendering)


def test_bpmn2_rendering_constructor_exists():
    assert callable(bpmn2_Rendering.__init__)


def test_bpmn2_rendering_constructor_args():
    sig = inspect.signature(bpmn2_Rendering.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_dataassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataAssociation)


def test_bpmn2_dataassociation_constructor_exists():
    assert callable(bpmn2_DataAssociation.__init__)


def test_bpmn2_dataassociation_constructor_args():
    sig = inspect.signature(bpmn2_DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_dataassociation_is_not_abstract():
    assert not inspect.isabstract(DataAssociation)


def test_dataassociation_constructor_exists():
    assert callable(DataAssociation.__init__)


def test_dataassociation_constructor_args():
    sig = inspect.signature(DataAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_eventdefinition_is_not_abstract():
    assert not inspect.isabstract(bpmn2_EventDefinition)


def test_bpmn2_eventdefinition_constructor_exists():
    assert callable(bpmn2_EventDefinition.__init__)


def test_bpmn2_eventdefinition_constructor_args():
    sig = inspect.signature(bpmn2_EventDefinition.__init__)
    params = list(sig.parameters.keys())



def test_event_is_not_abstract():
    assert not inspect.isabstract(Event)


def test_event_constructor_exists():
    assert callable(Event.__init__)


def test_event_constructor_args():
    sig = inspect.signature(Event.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_throwevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ThrowEvent)


def test_bpmn2_throwevent_constructor_exists():
    assert callable(bpmn2_ThrowEvent.__init__)


def test_bpmn2_throwevent_constructor_args():
    sig = inspect.signature(bpmn2_ThrowEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_catchevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CatchEvent)


def test_bpmn2_catchevent_constructor_exists():
    assert callable(bpmn2_CatchEvent.__init__)


def test_bpmn2_catchevent_constructor_args():
    sig = inspect.signature(bpmn2_CatchEvent.__init__)
    params = list(sig.parameters.keys())
    assert "parallelMultiple" in params, "Missing parameter 'parallelMultiple'"

def test_bpmn2_catchevent_has_parallelMultiple():
    assert hasattr(bpmn2_CatchEvent, "parallelMultiple")
    descriptor = None
    for klass in bpmn2_CatchEvent.__mro__:
        if "parallelMultiple" in klass.__dict__:
            descriptor = klass.__dict__["parallelMultiple"]
            break
    assert isinstance(descriptor, property)



def test_catchevent_is_not_abstract():
    assert not inspect.isabstract(CatchEvent)


def test_catchevent_constructor_exists():
    assert callable(CatchEvent.__init__)


def test_catchevent_constructor_args():
    sig = inspect.signature(CatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_startevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_StartEvent)


def test_bpmn2_startevent_constructor_exists():
    assert callable(bpmn2_StartEvent.__init__)


def test_bpmn2_startevent_constructor_args():
    sig = inspect.signature(bpmn2_StartEvent.__init__)
    params = list(sig.parameters.keys())
    assert "isInterrupting" in params, "Missing parameter 'isInterrupting'"

def test_bpmn2_startevent_has_isInterrupting():
    assert hasattr(bpmn2_StartEvent, "isInterrupting")
    descriptor = None
    for klass in bpmn2_StartEvent.__mro__:
        if "isInterrupting" in klass.__dict__:
            descriptor = klass.__dict__["isInterrupting"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_intermediatecatchevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_IntermediateCatchEvent)


def test_bpmn2_intermediatecatchevent_constructor_exists():
    assert callable(bpmn2_IntermediateCatchEvent.__init__)


def test_bpmn2_intermediatecatchevent_constructor_args():
    sig = inspect.signature(bpmn2_IntermediateCatchEvent.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_dataoutputassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataOutputAssociation)


def test_bpmn2_dataoutputassociation_constructor_exists():
    assert callable(bpmn2_DataOutputAssociation.__init__)


def test_bpmn2_dataoutputassociation_constructor_args():
    sig = inspect.signature(bpmn2_DataOutputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_datainputassociation_is_not_abstract():
    assert not inspect.isabstract(bpmn2_DataInputAssociation)


def test_bpmn2_datainputassociation_constructor_exists():
    assert callable(bpmn2_DataInputAssociation.__init__)


def test_bpmn2_datainputassociation_constructor_args():
    sig = inspect.signature(bpmn2_DataInputAssociation.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_boundaryevent_is_not_abstract():
    assert not inspect.isabstract(bpmn2_BoundaryEvent)


def test_bpmn2_boundaryevent_constructor_exists():
    assert callable(bpmn2_BoundaryEvent.__init__)


def test_bpmn2_boundaryevent_constructor_args():
    sig = inspect.signature(bpmn2_BoundaryEvent.__init__)
    params = list(sig.parameters.keys())
    assert "cancelActivity" in params, "Missing parameter 'cancelActivity'"

def test_bpmn2_boundaryevent_has_cancelActivity():
    assert hasattr(bpmn2_BoundaryEvent, "cancelActivity")
    descriptor = None
    for klass in bpmn2_BoundaryEvent.__mro__:
        if "cancelActivity" in klass.__dict__:
            descriptor = klass.__dict__["cancelActivity"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_loopcharacteristics_is_not_abstract():
    assert not inspect.isabstract(bpmn2_LoopCharacteristics)


def test_bpmn2_loopcharacteristics_constructor_exists():
    assert callable(bpmn2_LoopCharacteristics.__init__)


def test_bpmn2_loopcharacteristics_constructor_args():
    sig = inspect.signature(bpmn2_LoopCharacteristics.__init__)
    params = list(sig.parameters.keys())



def test_flownode_is_not_abstract():
    assert not inspect.isabstract(FlowNode)


def test_flownode_constructor_exists():
    assert callable(FlowNode.__init__)


def test_flownode_constructor_args():
    sig = inspect.signature(FlowNode.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_choreographyactivity_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ChoreographyActivity)


def test_bpmn2_choreographyactivity_constructor_exists():
    assert callable(bpmn2_ChoreographyActivity.__init__)


def test_bpmn2_choreographyactivity_constructor_args():
    sig = inspect.signature(bpmn2_ChoreographyActivity.__init__)
    params = list(sig.parameters.keys())
    assert "loopType" in params, "Missing parameter 'loopType'"

def test_bpmn2_choreographyactivity_has_loopType():
    assert hasattr(bpmn2_ChoreographyActivity, "loopType")
    descriptor = None
    for klass in bpmn2_ChoreographyActivity.__mro__:
        if "loopType" in klass.__dict__:
            descriptor = klass.__dict__["loopType"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_event_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Event)


def test_bpmn2_event_constructor_exists():
    assert callable(bpmn2_Event.__init__)


def test_bpmn2_event_constructor_args():
    sig = inspect.signature(bpmn2_Event.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_gateway_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Gateway)


def test_bpmn2_gateway_constructor_exists():
    assert callable(bpmn2_Gateway.__init__)


def test_bpmn2_gateway_constructor_args():
    sig = inspect.signature(bpmn2_Gateway.__init__)
    params = list(sig.parameters.keys())
    assert "gatewayDirection" in params, "Missing parameter 'gatewayDirection'"

def test_bpmn2_gateway_has_gatewayDirection():
    assert hasattr(bpmn2_Gateway, "gatewayDirection")
    descriptor = None
    for klass in bpmn2_Gateway.__mro__:
        if "gatewayDirection" in klass.__dict__:
            descriptor = klass.__dict__["gatewayDirection"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_activity_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Activity)


def test_bpmn2_activity_constructor_exists():
    assert callable(bpmn2_Activity.__init__)


def test_bpmn2_activity_constructor_args():
    sig = inspect.signature(bpmn2_Activity.__init__)
    params = list(sig.parameters.keys())
    assert "isForCompensation" in params, "Missing parameter 'isForCompensation'"
    assert "startQuantity" in params, "Missing parameter 'startQuantity'"
    assert "completionQuantity" in params, "Missing parameter 'completionQuantity'"

def test_bpmn2_activity_has_isForCompensation():
    assert hasattr(bpmn2_Activity, "isForCompensation")
    descriptor = None
    for klass in bpmn2_Activity.__mro__:
        if "isForCompensation" in klass.__dict__:
            descriptor = klass.__dict__["isForCompensation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_activity_has_startQuantity():
    assert hasattr(bpmn2_Activity, "startQuantity")
    descriptor = None
    for klass in bpmn2_Activity.__mro__:
        if "startQuantity" in klass.__dict__:
            descriptor = klass.__dict__["startQuantity"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_activity_has_completionQuantity():
    assert hasattr(bpmn2_Activity, "completionQuantity")
    descriptor = None
    for klass in bpmn2_Activity.__mro__:
        if "completionQuantity" in klass.__dict__:
            descriptor = klass.__dict__["completionQuantity"]
            break
    assert isinstance(descriptor, property)



def test_activity_is_not_abstract():
    assert not inspect.isabstract(Activity)


def test_activity_constructor_exists():
    assert callable(Activity.__init__)


def test_activity_constructor_args():
    sig = inspect.signature(Activity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_callactivity_is_not_abstract():
    assert not inspect.isabstract(bpmn2_CallActivity)


def test_bpmn2_callactivity_constructor_exists():
    assert callable(bpmn2_CallActivity.__init__)


def test_bpmn2_callactivity_constructor_args():
    sig = inspect.signature(bpmn2_CallActivity.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_subprocess_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SubProcess)


def test_bpmn2_subprocess_constructor_exists():
    assert callable(bpmn2_SubProcess.__init__)


def test_bpmn2_subprocess_constructor_args():
    sig = inspect.signature(bpmn2_SubProcess.__init__)
    params = list(sig.parameters.keys())
    assert "triggeredByEvent" in params, "Missing parameter 'triggeredByEvent'"

def test_bpmn2_subprocess_has_triggeredByEvent():
    assert hasattr(bpmn2_SubProcess, "triggeredByEvent")
    descriptor = None
    for klass in bpmn2_SubProcess.__mro__:
        if "triggeredByEvent" in klass.__dict__:
            descriptor = klass.__dict__["triggeredByEvent"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_task_is_not_abstract():
    assert not inspect.isabstract(bpmn2_Task)


def test_bpmn2_task_constructor_exists():
    assert callable(bpmn2_Task.__init__)


def test_bpmn2_task_constructor_args():
    sig = inspect.signature(bpmn2_Task.__init__)
    params = list(sig.parameters.keys())



def test_task_is_not_abstract():
    assert not inspect.isabstract(Task)


def test_task_constructor_exists():
    assert callable(Task.__init__)


def test_task_constructor_args():
    sig = inspect.signature(Task.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_sendtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_SendTask)


def test_bpmn2_sendtask_constructor_exists():
    assert callable(bpmn2_SendTask.__init__)


def test_bpmn2_sendtask_constructor_args():
    sig = inspect.signature(bpmn2_SendTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_sendtask_has_implementation():
    assert hasattr(bpmn2_SendTask, "implementation")
    descriptor = None
    for klass in bpmn2_SendTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_scripttask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ScriptTask)


def test_bpmn2_scripttask_constructor_exists():
    assert callable(bpmn2_ScriptTask.__init__)


def test_bpmn2_scripttask_constructor_args():
    sig = inspect.signature(bpmn2_ScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "script" in params, "Missing parameter 'script'"
    assert "scriptFormat" in params, "Missing parameter 'scriptFormat'"

def test_bpmn2_scripttask_has_script():
    assert hasattr(bpmn2_ScriptTask, "script")
    descriptor = None
    for klass in bpmn2_ScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_scripttask_has_scriptFormat():
    assert hasattr(bpmn2_ScriptTask, "scriptFormat")
    descriptor = None
    for klass in bpmn2_ScriptTask.__mro__:
        if "scriptFormat" in klass.__dict__:
            descriptor = klass.__dict__["scriptFormat"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_businessruletask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_BusinessRuleTask)


def test_bpmn2_businessruletask_constructor_exists():
    assert callable(bpmn2_BusinessRuleTask.__init__)


def test_bpmn2_businessruletask_constructor_args():
    sig = inspect.signature(bpmn2_BusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_businessruletask_has_implementation():
    assert hasattr(bpmn2_BusinessRuleTask, "implementation")
    descriptor = None
    for klass in bpmn2_BusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_receivetask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ReceiveTask)


def test_bpmn2_receivetask_constructor_exists():
    assert callable(bpmn2_ReceiveTask.__init__)


def test_bpmn2_receivetask_constructor_args():
    sig = inspect.signature(bpmn2_ReceiveTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"
    assert "instantiate" in params, "Missing parameter 'instantiate'"

def test_bpmn2_receivetask_has_implementation():
    assert hasattr(bpmn2_ReceiveTask, "implementation")
    descriptor = None
    for klass in bpmn2_ReceiveTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_receivetask_has_instantiate():
    assert hasattr(bpmn2_ReceiveTask, "instantiate")
    descriptor = None
    for klass in bpmn2_ReceiveTask.__mro__:
        if "instantiate" in klass.__dict__:
            descriptor = klass.__dict__["instantiate"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_servicetask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ServiceTask)


def test_bpmn2_servicetask_constructor_exists():
    assert callable(bpmn2_ServiceTask.__init__)


def test_bpmn2_servicetask_constructor_args():
    sig = inspect.signature(bpmn2_ServiceTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_servicetask_has_implementation():
    assert hasattr(bpmn2_ServiceTask, "implementation")
    descriptor = None
    for klass in bpmn2_ServiceTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_usertask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_UserTask)


def test_bpmn2_usertask_constructor_exists():
    assert callable(bpmn2_UserTask.__init__)


def test_bpmn2_usertask_constructor_args():
    sig = inspect.signature(bpmn2_UserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_usertask_has_implementation():
    assert hasattr(bpmn2_UserTask, "implementation")
    descriptor = None
    for klass in bpmn2_UserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_manualtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_ManualTask)


def test_bpmn2_manualtask_constructor_exists():
    assert callable(bpmn2_ManualTask.__init__)


def test_bpmn2_manualtask_constructor_args():
    sig = inspect.signature(bpmn2_ManualTask.__init__)
    params = list(sig.parameters.keys())



def test_globaltask_is_not_abstract():
    assert not inspect.isabstract(GlobalTask)


def test_globaltask_constructor_exists():
    assert callable(GlobalTask.__init__)


def test_globaltask_constructor_args():
    sig = inspect.signature(GlobalTask.__init__)
    params = list(sig.parameters.keys())



def test_bpmn2_globalscripttask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalScriptTask)


def test_bpmn2_globalscripttask_constructor_exists():
    assert callable(bpmn2_GlobalScriptTask.__init__)


def test_bpmn2_globalscripttask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalScriptTask.__init__)
    params = list(sig.parameters.keys())
    assert "scriptLanguage" in params, "Missing parameter 'scriptLanguage'"
    assert "script" in params, "Missing parameter 'script'"

def test_bpmn2_globalscripttask_has_scriptLanguage():
    assert hasattr(bpmn2_GlobalScriptTask, "scriptLanguage")
    descriptor = None
    for klass in bpmn2_GlobalScriptTask.__mro__:
        if "scriptLanguage" in klass.__dict__:
            descriptor = klass.__dict__["scriptLanguage"]
            break
    assert isinstance(descriptor, property)

def test_bpmn2_globalscripttask_has_script():
    assert hasattr(bpmn2_GlobalScriptTask, "script")
    descriptor = None
    for klass in bpmn2_GlobalScriptTask.__mro__:
        if "script" in klass.__dict__:
            descriptor = klass.__dict__["script"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_globalusertask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalUserTask)


def test_bpmn2_globalusertask_constructor_exists():
    assert callable(bpmn2_GlobalUserTask.__init__)


def test_bpmn2_globalusertask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalUserTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_globalusertask_has_implementation():
    assert hasattr(bpmn2_GlobalUserTask, "implementation")
    descriptor = None
    for klass in bpmn2_GlobalUserTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_globalbusinessruletask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalBusinessRuleTask)


def test_bpmn2_globalbusinessruletask_constructor_exists():
    assert callable(bpmn2_GlobalBusinessRuleTask.__init__)


def test_bpmn2_globalbusinessruletask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalBusinessRuleTask.__init__)
    params = list(sig.parameters.keys())
    assert "implementation" in params, "Missing parameter 'implementation'"

def test_bpmn2_globalbusinessruletask_has_implementation():
    assert hasattr(bpmn2_GlobalBusinessRuleTask, "implementation")
    descriptor = None
    for klass in bpmn2_GlobalBusinessRuleTask.__mro__:
        if "implementation" in klass.__dict__:
            descriptor = klass.__dict__["implementation"]
            break
    assert isinstance(descriptor, property)



def test_bpmn2_globalmanualtask_is_not_abstract():
    assert not inspect.isabstract(bpmn2_GlobalManualTask)


def test_bpmn2_globalmanualtask_constructor_exists():
    assert callable(bpmn2_GlobalManualTask.__init__)


def test_bpmn2_globalmanualtask_constructor_args():
    sig = inspect.signature(bpmn2_GlobalManualTask.__init__)
    params = list(sig.parameters.keys())

def test_multiinstancebehavior_exists():
    # Check that the Enumeration exists
    assert MultiInstanceBehavior is not None

def test_multiinstancebehavior_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MultiInstanceBehavior]
    expected_literals = [
        "Complex",
        "One",
        "None_",
        "All",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MultiInstanceBehavior"

def test_relationshipdirection_exists():
    # Check that the Enumeration exists
    assert RelationshipDirection is not None

def test_relationshipdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in RelationshipDirection]
    expected_literals = [
        "Both",
        "None_",
        "Backward",
        "Forward",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in RelationshipDirection"

def test_itemkind_exists():
    # Check that the Enumeration exists
    assert ItemKind is not None

def test_itemkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ItemKind]
    expected_literals = [
        "Information",
        "Physical",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ItemKind"

def test_processtype_exists():
    # Check that the Enumeration exists
    assert ProcessType is not None

def test_processtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ProcessType]
    expected_literals = [
        "Public",
        "Private",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ProcessType"

def test_choreographylooptype_exists():
    # Check that the Enumeration exists
    assert ChoreographyLoopType is not None

def test_choreographylooptype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ChoreographyLoopType]
    expected_literals = [
        "MultiInstanceSequential",
        "None_",
        "MultiInstanceParallel",
        "Standard",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ChoreographyLoopType"

def test_adhocordering_exists():
    # Check that the Enumeration exists
    assert AdHocOrdering is not None

def test_adhocordering_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AdHocOrdering]
    expected_literals = [
        "Sequential",
        "Parallel",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AdHocOrdering"

def test_eventbasedgatewaytype_exists():
    # Check that the Enumeration exists
    assert EventBasedGatewayType is not None

def test_eventbasedgatewaytype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EventBasedGatewayType]
    expected_literals = [
        "Parallel",
        "Exclusive",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EventBasedGatewayType"

def test_gatewaydirection_exists():
    # Check that the Enumeration exists
    assert GatewayDirection is not None

def test_gatewaydirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GatewayDirection]
    expected_literals = [
        "Diverging",
        "Converging",
        "Mixed",
        "Unspecified",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GatewayDirection"

def test_associationdirection_exists():
    # Check that the Enumeration exists
    assert AssociationDirection is not None

def test_associationdirection_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssociationDirection]
    expected_literals = [
        "One",
        "Both",
        "None_",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssociationDirection"


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
Expression_strategy = st.builds(
    Expression,
)
bpmn2_FormalExpression_strategy = st.builds(
    bpmn2_FormalExpression,
    language=
        safe_text
)
bpmn2_InteractionNode_strategy = st.builds(
    bpmn2_InteractionNode,
)
bpmn2_ParticipantMultiplicity_strategy = st.builds(
    bpmn2_ParticipantMultiplicity,
    minimum=
        st.integers(),
    maximum=
        st.integers(),
    id=
        safe_text
)
InteractionNode_strategy = st.builds(
    InteractionNode,
)
Collaboration_strategy = st.builds(
    Collaboration,
)
FlowElement_strategy = st.builds(
    FlowElement,
)
bpmn2_SequenceFlow_strategy = st.builds(
    bpmn2_SequenceFlow,
    isImmediate=
        st.booleans()
)
bpmn2_FlowNode_strategy = st.builds(
    bpmn2_FlowNode,
)
FlowElementsContainer_strategy = st.builds(
    FlowElementsContainer,
)
bpmn2_Choreography_strategy = st.builds(
    bpmn2_Choreography,
)
ResourceRole_strategy = st.builds(
    ResourceRole,
)
bpmn2_Performer_strategy = st.builds(
    bpmn2_Performer,
)
bpmn2_ResourceAssignmentExpression_strategy = st.builds(
    bpmn2_ResourceAssignmentExpression,
    id=
        safe_text
)
bpmn2_ResourceParameterBinding_strategy = st.builds(
    bpmn2_ResourceParameterBinding,
    id=
        safe_text
)
ItemAwareElement_strategy = st.builds(
    ItemAwareElement,
)
bpmn2_Property_strategy = st.builds(
    bpmn2_Property,
    name=
        safe_text
)
bpmn2_DataOutput_strategy = st.builds(
    bpmn2_DataOutput,
    isCollection=
        st.booleans(),
    name=
        safe_text
)
bpmn2_Import_strategy = st.builds(
    bpmn2_Import,
    importType=
        safe_text,
    namespace=
        safe_text,
    id=
        safe_text,
    location=
        safe_text
)
bpmn2_DataInput_strategy = st.builds(
    bpmn2_DataInput,
    name=
        safe_text,
    isCollection=
        st.booleans()
)
bpmn2_InputOutputBinding_strategy = st.builds(
    bpmn2_InputOutputBinding,
    id=
        safe_text
)
CallableElement_strategy = st.builds(
    CallableElement,
)
bpmn2_Process_strategy = st.builds(
    bpmn2_Process,
    processType=
        safe_text,
    isExecutable=
        st.booleans(),
    isClosed=
        st.booleans()
)
bpmn2_GlobalTask_strategy = st.builds(
    bpmn2_GlobalTask,
)
bpmn2_ExtensionAttributeDefinition_strategy = st.builds(
    bpmn2_ExtensionAttributeDefinition,
    type=
        safe_text,
    name=
        safe_text,
    id=
        safe_text,
    isReference=
        st.booleans()
)
bpmn2_ExtensionAttributeValue_strategy = st.builds(
    bpmn2_ExtensionAttributeValue,
    id=
        safe_text
)
bpmn2_ExtensionDefinition_strategy = st.builds(
    bpmn2_ExtensionDefinition,
    id=
        safe_text,
    name=
        safe_text
)
bpmn2_BaseElement_strategy = st.builds(
    bpmn2_BaseElement,
    description=
        safe_text,
    id=
        safe_text
)
BaseElement_strategy = st.builds(
    BaseElement,
)
bpmn2_FlowElement_strategy = st.builds(
    bpmn2_FlowElement,
    name=
        safe_text
)
bpmn2_MessageFlowAssociation_strategy = st.builds(
    bpmn2_MessageFlowAssociation,
)
bpmn2_OutputSet_strategy = st.builds(
    bpmn2_OutputSet,
    name=
        safe_text
)
bpmn2_InputSet_strategy = st.builds(
    bpmn2_InputSet,
    name=
        safe_text
)
bpmn2_CorrelationSubscription_strategy = st.builds(
    bpmn2_CorrelationSubscription,
)
bpmn2_LaneSet_strategy = st.builds(
    bpmn2_LaneSet,
    name=
        safe_text
)
bpmn2_ConversationLink_strategy = st.builds(
    bpmn2_ConversationLink,
    name=
        safe_text
)
bpmn2_FlowElementsContainer_strategy = st.builds(
    bpmn2_FlowElementsContainer,
)
bpmn2_Monitoring_strategy = st.builds(
    bpmn2_Monitoring,
)
bpmn2_InputOutputSpecification_strategy = st.builds(
    bpmn2_InputOutputSpecification,
)
bpmn2_CorrelationPropertyRetrievalExpression_strategy = st.builds(
    bpmn2_CorrelationPropertyRetrievalExpression,
)
bpmn2_Lane_strategy = st.builds(
    bpmn2_Lane,
    name=
        safe_text
)
bpmn2_CorrelationKey_strategy = st.builds(
    bpmn2_CorrelationKey,
    name=
        safe_text
)
bpmn2_Artifact_strategy = st.builds(
    bpmn2_Artifact,
)
bpmn2_ResourceRole_strategy = st.builds(
    bpmn2_ResourceRole,
    name=
        safe_text
)
bpmn2_ConversationNode_strategy = st.builds(
    bpmn2_ConversationNode,
    name=
        safe_text
)
bpmn2_ParticipantAssociation_strategy = st.builds(
    bpmn2_ParticipantAssociation,
)
bpmn2_ItemAwareElement_strategy = st.builds(
    bpmn2_ItemAwareElement,
)
bpmn2_MessageFlow_strategy = st.builds(
    bpmn2_MessageFlow,
    name=
        safe_text
)
bpmn2_ResourceParameter_strategy = st.builds(
    bpmn2_ResourceParameter,
    name=
        safe_text,
    isRequired=
        st.booleans()
)
bpmn2_CategoryValue_strategy = st.builds(
    bpmn2_CategoryValue,
    value=
        safe_text
)
bpmn2_Expression_strategy = st.builds(
    bpmn2_Expression,
)
bpmn2_CorrelationPropertyBinding_strategy = st.builds(
    bpmn2_CorrelationPropertyBinding,
)
bpmn2_Participant_strategy = st.builds(
    bpmn2_Participant,
    name=
        safe_text
)
bpmn2_Auditing_strategy = st.builds(
    bpmn2_Auditing,
)
bpmn2_DataState_strategy = st.builds(
    bpmn2_DataState,
    name=
        safe_text
)
bpmn2_ConversationAssociation_strategy = st.builds(
    bpmn2_ConversationAssociation,
)
bpmn2_Documentation_strategy = st.builds(
    bpmn2_Documentation,
    textFormat=
        safe_text,
    text=
        safe_text
)
bpmn2_RootElement_strategy = st.builds(
    bpmn2_RootElement,
)
bpmn2_EObject_strategy = st.builds(
    bpmn2_EObject,
)
bpmn2_Operation_strategy = st.builds(
    bpmn2_Operation,
    name=
        safe_text
)
RootElement_strategy = st.builds(
    RootElement,
)
bpmn2_CallableElement_strategy = st.builds(
    bpmn2_CallableElement,
    name=
        safe_text
)
bpmn2_EndPoint_strategy = st.builds(
    bpmn2_EndPoint,
)
bpmn2_Resource_strategy = st.builds(
    bpmn2_Resource,
    name=
        safe_text
)
bpmn2_Collaboration_strategy = st.builds(
    bpmn2_Collaboration,
    name=
        safe_text,
    isClosed=
        st.booleans()
)
bpmn2_CorrelationProperty_strategy = st.builds(
    bpmn2_CorrelationProperty,
    name=
        safe_text
)
bpmn2_ItemDefinition_strategy = st.builds(
    bpmn2_ItemDefinition,
    isCollection=
        st.booleans(),
    itemKind=
        safe_text
)
bpmn2_Error_strategy = st.builds(
    bpmn2_Error,
    name=
        safe_text,
    errorCode=
        safe_text
)
bpmn2_Message_strategy = st.builds(
    bpmn2_Message,
    name=
        safe_text
)
bpmn2_Interface_strategy = st.builds(
    bpmn2_Interface,
    name=
        safe_text
)
bpmn2_BPMNDiagram_strategy = st.builds(
    bpmn2_BPMNDiagram,
)
bpmn2_Definitions_strategy = st.builds(
    bpmn2_Definitions,
    exporter=
        safe_text,
    name=
        safe_text,
    exporterVersion=
        safe_text,
    typeLanguage=
        safe_text,
    expressionLanguage=
        safe_text,
    targetNamespace=
        safe_text
)
SubProcess_strategy = st.builds(
    SubProcess,
)
bpmn2_Transaction_strategy = st.builds(
    bpmn2_Transaction,
    protocol=
        safe_text,
    method=
        safe_text
)
bpmn2_AdHocSubProcess_strategy = st.builds(
    bpmn2_AdHocSubProcess,
    ordering=
        safe_text,
    cancelRemainingInstances=
        st.booleans()
)
bpmn2_ComplexBehaviorDefinition_strategy = st.builds(
    bpmn2_ComplexBehaviorDefinition,
)
LoopCharacteristics_strategy = st.builds(
    LoopCharacteristics,
)
bpmn2_StandardLoopCharacteristics_strategy = st.builds(
    bpmn2_StandardLoopCharacteristics,
    testBefore=
        st.booleans()
)
bpmn2_MultiInstanceLoopCharacteristics_strategy = st.builds(
    bpmn2_MultiInstanceLoopCharacteristics,
    isSequential=
        st.booleans(),
    behavior=
        safe_text
)
bpmn2_Category_strategy = st.builds(
    bpmn2_Category,
    name=
        safe_text
)
Artifact_strategy = st.builds(
    Artifact,
)
bpmn2_Association_strategy = st.builds(
    bpmn2_Association,
    associationDirection=
        safe_text
)
bpmn2_Group_strategy = st.builds(
    bpmn2_Group,
)
bpmn2_TextAnnotation_strategy = st.builds(
    bpmn2_TextAnnotation,
    text=
        safe_text,
    textFormat=
        safe_text
)
Choreography_strategy = st.builds(
    Choreography,
)
bpmn2_GlobalChoreographyTask_strategy = st.builds(
    bpmn2_GlobalChoreographyTask,
)
ChoreographyActivity_strategy = st.builds(
    ChoreographyActivity,
)
bpmn2_SubChoreography_strategy = st.builds(
    bpmn2_SubChoreography,
)
bpmn2_ChoreographyTask_strategy = st.builds(
    bpmn2_ChoreographyTask,
)
bpmn2_CallChoreography_strategy = st.builds(
    bpmn2_CallChoreography,
)
bpmn2_PartnerRole_strategy = st.builds(
    bpmn2_PartnerRole,
    name=
        safe_text
)
bpmn2_PartnerEntity_strategy = st.builds(
    bpmn2_PartnerEntity,
    name=
        safe_text
)
bpmn2_GlobalConversation_strategy = st.builds(
    bpmn2_GlobalConversation,
)
ConversationNode_strategy = st.builds(
    ConversationNode,
)
bpmn2_Conversation_strategy = st.builds(
    bpmn2_Conversation,
)
bpmn2_SubConversation_strategy = st.builds(
    bpmn2_SubConversation,
)
bpmn2_CallConversation_strategy = st.builds(
    bpmn2_CallConversation,
)
bpmn2_DataObjectReference_strategy = st.builds(
    bpmn2_DataObjectReference,
)
bpmn2_DataStoreReference_strategy = st.builds(
    bpmn2_DataStoreReference,
)
bpmn2_DataStore_strategy = st.builds(
    bpmn2_DataStore,
    capacity=
        st.integers(),
    isUnlimited=
        st.booleans(),
    name=
        safe_text
)
bpmn2_DataObject_strategy = st.builds(
    bpmn2_DataObject,
    isCollection=
        st.booleans()
)
bpmn2_Signal_strategy = st.builds(
    bpmn2_Signal,
    name=
        safe_text
)
bpmn2_Escalation_strategy = st.builds(
    bpmn2_Escalation,
    name=
        safe_text,
    escalationCode=
        safe_text,
    id=
        safe_text
)
EventDefinition_strategy = st.builds(
    EventDefinition,
)
bpmn2_SignalEventDefinition_strategy = st.builds(
    bpmn2_SignalEventDefinition,
)
bpmn2_CompensateEventDefinition_strategy = st.builds(
    bpmn2_CompensateEventDefinition,
    waitForCompletion=
        st.booleans()
)
bpmn2_ConditionalEventDefinition_strategy = st.builds(
    bpmn2_ConditionalEventDefinition,
)
bpmn2_MessageEventDefinition_strategy = st.builds(
    bpmn2_MessageEventDefinition,
)
bpmn2_ErrorEventDefinition_strategy = st.builds(
    bpmn2_ErrorEventDefinition,
)
bpmn2_TimerEventDefinition_strategy = st.builds(
    bpmn2_TimerEventDefinition,
)
bpmn2_EscalationEventDefinition_strategy = st.builds(
    bpmn2_EscalationEventDefinition,
)
bpmn2_TerminateEventDefinition_strategy = st.builds(
    bpmn2_TerminateEventDefinition,
)
bpmn2_LinkEventDefinition_strategy = st.builds(
    bpmn2_LinkEventDefinition,
    name=
        safe_text
)
bpmn2_CancelEventDefinition_strategy = st.builds(
    bpmn2_CancelEventDefinition,
)
ThrowEvent_strategy = st.builds(
    ThrowEvent,
)
bpmn2_ImplicitThrowEvent_strategy = st.builds(
    bpmn2_ImplicitThrowEvent,
)
bpmn2_EndEvent_strategy = st.builds(
    bpmn2_EndEvent,
)
bpmn2_IntermediateThrowEvent_strategy = st.builds(
    bpmn2_IntermediateThrowEvent,
)
bpmn2_Extension_strategy = st.builds(
    bpmn2_Extension,
    id=
        safe_text,
    mustUnderstand=
        st.booleans()
)
bpmn2_Relationship_strategy = st.builds(
    bpmn2_Relationship,
    type=
        safe_text,
    direction=
        safe_text
)
bpmn2_Assignment_strategy = st.builds(
    bpmn2_Assignment,
)
Gateway_strategy = st.builds(
    Gateway,
)
bpmn2_ParallelGateway_strategy = st.builds(
    bpmn2_ParallelGateway,
)
bpmn2_ExclusiveGateway_strategy = st.builds(
    bpmn2_ExclusiveGateway,
)
bpmn2_ComplexGateway_strategy = st.builds(
    bpmn2_ComplexGateway,
)
bpmn2_InclusiveGateway_strategy = st.builds(
    bpmn2_InclusiveGateway,
)
bpmn2_EventBasedGateway_strategy = st.builds(
    bpmn2_EventBasedGateway,
    instantiate=
        st.booleans(),
    eventGatewayType=
        safe_text
)
HumanPerformer_strategy = st.builds(
    HumanPerformer,
)
bpmn2_PotentialOwner_strategy = st.builds(
    bpmn2_PotentialOwner,
)
Performer_strategy = st.builds(
    Performer,
)
bpmn2_HumanPerformer_strategy = st.builds(
    bpmn2_HumanPerformer,
)
bpmn2_Rendering_strategy = st.builds(
    bpmn2_Rendering,
)
bpmn2_DataAssociation_strategy = st.builds(
    bpmn2_DataAssociation,
)
DataAssociation_strategy = st.builds(
    DataAssociation,
)
bpmn2_EventDefinition_strategy = st.builds(
    bpmn2_EventDefinition,
)
Event_strategy = st.builds(
    Event,
)
bpmn2_ThrowEvent_strategy = st.builds(
    bpmn2_ThrowEvent,
)
bpmn2_CatchEvent_strategy = st.builds(
    bpmn2_CatchEvent,
    parallelMultiple=
        st.booleans()
)
CatchEvent_strategy = st.builds(
    CatchEvent,
)
bpmn2_StartEvent_strategy = st.builds(
    bpmn2_StartEvent,
    isInterrupting=
        st.booleans()
)
bpmn2_IntermediateCatchEvent_strategy = st.builds(
    bpmn2_IntermediateCatchEvent,
)
bpmn2_DataOutputAssociation_strategy = st.builds(
    bpmn2_DataOutputAssociation,
)
bpmn2_DataInputAssociation_strategy = st.builds(
    bpmn2_DataInputAssociation,
)
bpmn2_BoundaryEvent_strategy = st.builds(
    bpmn2_BoundaryEvent,
    cancelActivity=
        st.booleans()
)
bpmn2_LoopCharacteristics_strategy = st.builds(
    bpmn2_LoopCharacteristics,
)
FlowNode_strategy = st.builds(
    FlowNode,
)
bpmn2_ChoreographyActivity_strategy = st.builds(
    bpmn2_ChoreographyActivity,
    loopType=
        safe_text
)
bpmn2_Event_strategy = st.builds(
    bpmn2_Event,
)
bpmn2_Gateway_strategy = st.builds(
    bpmn2_Gateway,
    gatewayDirection=
        safe_text
)
bpmn2_Activity_strategy = st.builds(
    bpmn2_Activity,
    isForCompensation=
        st.booleans(),
    startQuantity=
        st.integers(),
    completionQuantity=
        st.integers()
)
Activity_strategy = st.builds(
    Activity,
)
bpmn2_CallActivity_strategy = st.builds(
    bpmn2_CallActivity,
)
bpmn2_SubProcess_strategy = st.builds(
    bpmn2_SubProcess,
    triggeredByEvent=
        st.booleans()
)
bpmn2_Task_strategy = st.builds(
    bpmn2_Task,
)
Task_strategy = st.builds(
    Task,
)
bpmn2_SendTask_strategy = st.builds(
    bpmn2_SendTask,
    implementation=
        safe_text
)
bpmn2_ScriptTask_strategy = st.builds(
    bpmn2_ScriptTask,
    script=
        safe_text,
    scriptFormat=
        safe_text
)
bpmn2_BusinessRuleTask_strategy = st.builds(
    bpmn2_BusinessRuleTask,
    implementation=
        safe_text
)
bpmn2_ReceiveTask_strategy = st.builds(
    bpmn2_ReceiveTask,
    implementation=
        safe_text,
    instantiate=
        st.booleans()
)
bpmn2_ServiceTask_strategy = st.builds(
    bpmn2_ServiceTask,
    implementation=
        safe_text
)
bpmn2_UserTask_strategy = st.builds(
    bpmn2_UserTask,
    implementation=
        safe_text
)
bpmn2_ManualTask_strategy = st.builds(
    bpmn2_ManualTask,
)
GlobalTask_strategy = st.builds(
    GlobalTask,
)
bpmn2_GlobalScriptTask_strategy = st.builds(
    bpmn2_GlobalScriptTask,
    scriptLanguage=
        safe_text,
    script=
        safe_text
)
bpmn2_GlobalUserTask_strategy = st.builds(
    bpmn2_GlobalUserTask,
    implementation=
        safe_text
)
bpmn2_GlobalBusinessRuleTask_strategy = st.builds(
    bpmn2_GlobalBusinessRuleTask,
    implementation=
        safe_text
)
bpmn2_GlobalManualTask_strategy = st.builds(
    bpmn2_GlobalManualTask,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=bpmn2_FormalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2_formalexpression_instantiation(instance):
    assert isinstance(instance, bpmn2_FormalExpression)



@given(instance=bpmn2_FormalExpression_strategy)
def test_bpmn2_formalexpression_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=bpmn2_InteractionNode_strategy)
@settings(max_examples=50)
def test_bpmn2_interactionnode_instantiation(instance):
    assert isinstance(instance, bpmn2_InteractionNode)

@given(instance=bpmn2_ParticipantMultiplicity_strategy)
@settings(max_examples=50)
def test_bpmn2_participantmultiplicity_instantiation(instance):
    assert isinstance(instance, bpmn2_ParticipantMultiplicity)



@given(instance=bpmn2_ParticipantMultiplicity_strategy)
def test_bpmn2_participantmultiplicity_minimum_setter(instance):
    original = instance.minimum
    instance.minimum = original
    assert instance.minimum == original



@given(instance=bpmn2_ParticipantMultiplicity_strategy)
def test_bpmn2_participantmultiplicity_maximum_setter(instance):
    original = instance.maximum
    instance.maximum = original
    assert instance.maximum == original



@given(instance=bpmn2_ParticipantMultiplicity_strategy)
def test_bpmn2_participantmultiplicity_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=InteractionNode_strategy)
@settings(max_examples=50)
def test_interactionnode_instantiation(instance):
    assert isinstance(instance, InteractionNode)

@given(instance=Collaboration_strategy)
@settings(max_examples=50)
def test_collaboration_instantiation(instance):
    assert isinstance(instance, Collaboration)

@given(instance=FlowElement_strategy)
@settings(max_examples=50)
def test_flowelement_instantiation(instance):
    assert isinstance(instance, FlowElement)

@given(instance=bpmn2_SequenceFlow_strategy)
@settings(max_examples=50)
def test_bpmn2_sequenceflow_instantiation(instance):
    assert isinstance(instance, bpmn2_SequenceFlow)



@given(instance=bpmn2_SequenceFlow_strategy)
def test_bpmn2_sequenceflow_isImmediate_setter(instance):
    original = instance.isImmediate
    instance.isImmediate = original
    assert instance.isImmediate == original

@given(instance=bpmn2_FlowNode_strategy)
@settings(max_examples=50)
def test_bpmn2_flownode_instantiation(instance):
    assert isinstance(instance, bpmn2_FlowNode)

@given(instance=FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_flowelementscontainer_instantiation(instance):
    assert isinstance(instance, FlowElementsContainer)

@given(instance=bpmn2_Choreography_strategy)
@settings(max_examples=50)
def test_bpmn2_choreography_instantiation(instance):
    assert isinstance(instance, bpmn2_Choreography)

@given(instance=ResourceRole_strategy)
@settings(max_examples=50)
def test_resourcerole_instantiation(instance):
    assert isinstance(instance, ResourceRole)

@given(instance=bpmn2_Performer_strategy)
@settings(max_examples=50)
def test_bpmn2_performer_instantiation(instance):
    assert isinstance(instance, bpmn2_Performer)

@given(instance=bpmn2_ResourceAssignmentExpression_strategy)
@settings(max_examples=50)
def test_bpmn2_resourceassignmentexpression_instantiation(instance):
    assert isinstance(instance, bpmn2_ResourceAssignmentExpression)



@given(instance=bpmn2_ResourceAssignmentExpression_strategy)
def test_bpmn2_resourceassignmentexpression_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=bpmn2_ResourceParameterBinding_strategy)
@settings(max_examples=50)
def test_bpmn2_resourceparameterbinding_instantiation(instance):
    assert isinstance(instance, bpmn2_ResourceParameterBinding)



@given(instance=bpmn2_ResourceParameterBinding_strategy)
def test_bpmn2_resourceparameterbinding_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=ItemAwareElement_strategy)
@settings(max_examples=50)
def test_itemawareelement_instantiation(instance):
    assert isinstance(instance, ItemAwareElement)

@given(instance=bpmn2_Property_strategy)
@settings(max_examples=50)
def test_bpmn2_property_instantiation(instance):
    assert isinstance(instance, bpmn2_Property)



@given(instance=bpmn2_Property_strategy)
def test_bpmn2_property_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_DataOutput_strategy)
@settings(max_examples=50)
def test_bpmn2_dataoutput_instantiation(instance):
    assert isinstance(instance, bpmn2_DataOutput)



@given(instance=bpmn2_DataOutput_strategy)
def test_bpmn2_dataoutput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original



@given(instance=bpmn2_DataOutput_strategy)
def test_bpmn2_dataoutput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Import_strategy)
@settings(max_examples=50)
def test_bpmn2_import_instantiation(instance):
    assert isinstance(instance, bpmn2_Import)



@given(instance=bpmn2_Import_strategy)
def test_bpmn2_import_importType_setter(instance):
    original = instance.importType
    instance.importType = original
    assert instance.importType == original



@given(instance=bpmn2_Import_strategy)
def test_bpmn2_import_namespace_setter(instance):
    original = instance.namespace
    instance.namespace = original
    assert instance.namespace == original



@given(instance=bpmn2_Import_strategy)
def test_bpmn2_import_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bpmn2_Import_strategy)
def test_bpmn2_import_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=bpmn2_DataInput_strategy)
@settings(max_examples=50)
def test_bpmn2_datainput_instantiation(instance):
    assert isinstance(instance, bpmn2_DataInput)



@given(instance=bpmn2_DataInput_strategy)
def test_bpmn2_datainput_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_DataInput_strategy)
def test_bpmn2_datainput_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2_InputOutputBinding_strategy)
@settings(max_examples=50)
def test_bpmn2_inputoutputbinding_instantiation(instance):
    assert isinstance(instance, bpmn2_InputOutputBinding)



@given(instance=bpmn2_InputOutputBinding_strategy)
def test_bpmn2_inputoutputbinding_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=CallableElement_strategy)
@settings(max_examples=50)
def test_callableelement_instantiation(instance):
    assert isinstance(instance, CallableElement)

@given(instance=bpmn2_Process_strategy)
@settings(max_examples=50)
def test_bpmn2_process_instantiation(instance):
    assert isinstance(instance, bpmn2_Process)



@given(instance=bpmn2_Process_strategy)
def test_bpmn2_process_processType_setter(instance):
    original = instance.processType
    instance.processType = original
    assert instance.processType == original



@given(instance=bpmn2_Process_strategy)
def test_bpmn2_process_isExecutable_setter(instance):
    original = instance.isExecutable
    instance.isExecutable = original
    assert instance.isExecutable == original



@given(instance=bpmn2_Process_strategy)
def test_bpmn2_process_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=bpmn2_GlobalTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globaltask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalTask)

@given(instance=bpmn2_ExtensionAttributeDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_extensionattributedefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ExtensionAttributeDefinition)



@given(instance=bpmn2_ExtensionAttributeDefinition_strategy)
def test_bpmn2_extensionattributedefinition_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=bpmn2_ExtensionAttributeDefinition_strategy)
def test_bpmn2_extensionattributedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_ExtensionAttributeDefinition_strategy)
def test_bpmn2_extensionattributedefinition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bpmn2_ExtensionAttributeDefinition_strategy)
def test_bpmn2_extensionattributedefinition_isReference_setter(instance):
    original = instance.isReference
    instance.isReference = original
    assert instance.isReference == original

@given(instance=bpmn2_ExtensionAttributeValue_strategy)
@settings(max_examples=50)
def test_bpmn2_extensionattributevalue_instantiation(instance):
    assert isinstance(instance, bpmn2_ExtensionAttributeValue)



@given(instance=bpmn2_ExtensionAttributeValue_strategy)
def test_bpmn2_extensionattributevalue_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=bpmn2_ExtensionDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_extensiondefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ExtensionDefinition)



@given(instance=bpmn2_ExtensionDefinition_strategy)
def test_bpmn2_extensiondefinition_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bpmn2_ExtensionDefinition_strategy)
def test_bpmn2_extensiondefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_BaseElement_strategy)
@settings(max_examples=50)
def test_bpmn2_baseelement_instantiation(instance):
    assert isinstance(instance, bpmn2_BaseElement)



@given(instance=bpmn2_BaseElement_strategy)
def test_bpmn2_baseelement_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=bpmn2_BaseElement_strategy)
def test_bpmn2_baseelement_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=BaseElement_strategy)
@settings(max_examples=50)
def test_baseelement_instantiation(instance):
    assert isinstance(instance, BaseElement)

@given(instance=bpmn2_FlowElement_strategy)
@settings(max_examples=50)
def test_bpmn2_flowelement_instantiation(instance):
    assert isinstance(instance, bpmn2_FlowElement)



@given(instance=bpmn2_FlowElement_strategy)
def test_bpmn2_flowelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_MessageFlowAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_messageflowassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_MessageFlowAssociation)

@given(instance=bpmn2_OutputSet_strategy)
@settings(max_examples=50)
def test_bpmn2_outputset_instantiation(instance):
    assert isinstance(instance, bpmn2_OutputSet)



@given(instance=bpmn2_OutputSet_strategy)
def test_bpmn2_outputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_InputSet_strategy)
@settings(max_examples=50)
def test_bpmn2_inputset_instantiation(instance):
    assert isinstance(instance, bpmn2_InputSet)



@given(instance=bpmn2_InputSet_strategy)
def test_bpmn2_inputset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_CorrelationSubscription_strategy)
@settings(max_examples=50)
def test_bpmn2_correlationsubscription_instantiation(instance):
    assert isinstance(instance, bpmn2_CorrelationSubscription)

@given(instance=bpmn2_LaneSet_strategy)
@settings(max_examples=50)
def test_bpmn2_laneset_instantiation(instance):
    assert isinstance(instance, bpmn2_LaneSet)



@given(instance=bpmn2_LaneSet_strategy)
def test_bpmn2_laneset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ConversationLink_strategy)
@settings(max_examples=50)
def test_bpmn2_conversationlink_instantiation(instance):
    assert isinstance(instance, bpmn2_ConversationLink)



@given(instance=bpmn2_ConversationLink_strategy)
def test_bpmn2_conversationlink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_FlowElementsContainer_strategy)
@settings(max_examples=50)
def test_bpmn2_flowelementscontainer_instantiation(instance):
    assert isinstance(instance, bpmn2_FlowElementsContainer)

@given(instance=bpmn2_Monitoring_strategy)
@settings(max_examples=50)
def test_bpmn2_monitoring_instantiation(instance):
    assert isinstance(instance, bpmn2_Monitoring)

@given(instance=bpmn2_InputOutputSpecification_strategy)
@settings(max_examples=50)
def test_bpmn2_inputoutputspecification_instantiation(instance):
    assert isinstance(instance, bpmn2_InputOutputSpecification)

@given(instance=bpmn2_CorrelationPropertyRetrievalExpression_strategy)
@settings(max_examples=50)
def test_bpmn2_correlationpropertyretrievalexpression_instantiation(instance):
    assert isinstance(instance, bpmn2_CorrelationPropertyRetrievalExpression)

@given(instance=bpmn2_Lane_strategy)
@settings(max_examples=50)
def test_bpmn2_lane_instantiation(instance):
    assert isinstance(instance, bpmn2_Lane)



@given(instance=bpmn2_Lane_strategy)
def test_bpmn2_lane_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_CorrelationKey_strategy)
@settings(max_examples=50)
def test_bpmn2_correlationkey_instantiation(instance):
    assert isinstance(instance, bpmn2_CorrelationKey)



@given(instance=bpmn2_CorrelationKey_strategy)
def test_bpmn2_correlationkey_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Artifact_strategy)
@settings(max_examples=50)
def test_bpmn2_artifact_instantiation(instance):
    assert isinstance(instance, bpmn2_Artifact)

@given(instance=bpmn2_ResourceRole_strategy)
@settings(max_examples=50)
def test_bpmn2_resourcerole_instantiation(instance):
    assert isinstance(instance, bpmn2_ResourceRole)



@given(instance=bpmn2_ResourceRole_strategy)
def test_bpmn2_resourcerole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ConversationNode_strategy)
@settings(max_examples=50)
def test_bpmn2_conversationnode_instantiation(instance):
    assert isinstance(instance, bpmn2_ConversationNode)



@given(instance=bpmn2_ConversationNode_strategy)
def test_bpmn2_conversationnode_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ParticipantAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_participantassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_ParticipantAssociation)

@given(instance=bpmn2_ItemAwareElement_strategy)
@settings(max_examples=50)
def test_bpmn2_itemawareelement_instantiation(instance):
    assert isinstance(instance, bpmn2_ItemAwareElement)

@given(instance=bpmn2_MessageFlow_strategy)
@settings(max_examples=50)
def test_bpmn2_messageflow_instantiation(instance):
    assert isinstance(instance, bpmn2_MessageFlow)



@given(instance=bpmn2_MessageFlow_strategy)
def test_bpmn2_messageflow_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ResourceParameter_strategy)
@settings(max_examples=50)
def test_bpmn2_resourceparameter_instantiation(instance):
    assert isinstance(instance, bpmn2_ResourceParameter)



@given(instance=bpmn2_ResourceParameter_strategy)
def test_bpmn2_resourceparameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_ResourceParameter_strategy)
def test_bpmn2_resourceparameter_isRequired_setter(instance):
    original = instance.isRequired
    instance.isRequired = original
    assert instance.isRequired == original

@given(instance=bpmn2_CategoryValue_strategy)
@settings(max_examples=50)
def test_bpmn2_categoryvalue_instantiation(instance):
    assert isinstance(instance, bpmn2_CategoryValue)



@given(instance=bpmn2_CategoryValue_strategy)
def test_bpmn2_categoryvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=bpmn2_Expression_strategy)
@settings(max_examples=50)
def test_bpmn2_expression_instantiation(instance):
    assert isinstance(instance, bpmn2_Expression)

@given(instance=bpmn2_CorrelationPropertyBinding_strategy)
@settings(max_examples=50)
def test_bpmn2_correlationpropertybinding_instantiation(instance):
    assert isinstance(instance, bpmn2_CorrelationPropertyBinding)

@given(instance=bpmn2_Participant_strategy)
@settings(max_examples=50)
def test_bpmn2_participant_instantiation(instance):
    assert isinstance(instance, bpmn2_Participant)



@given(instance=bpmn2_Participant_strategy)
def test_bpmn2_participant_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Auditing_strategy)
@settings(max_examples=50)
def test_bpmn2_auditing_instantiation(instance):
    assert isinstance(instance, bpmn2_Auditing)

@given(instance=bpmn2_DataState_strategy)
@settings(max_examples=50)
def test_bpmn2_datastate_instantiation(instance):
    assert isinstance(instance, bpmn2_DataState)



@given(instance=bpmn2_DataState_strategy)
def test_bpmn2_datastate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ConversationAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_conversationassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_ConversationAssociation)

@given(instance=bpmn2_Documentation_strategy)
@settings(max_examples=50)
def test_bpmn2_documentation_instantiation(instance):
    assert isinstance(instance, bpmn2_Documentation)



@given(instance=bpmn2_Documentation_strategy)
def test_bpmn2_documentation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original



@given(instance=bpmn2_Documentation_strategy)
def test_bpmn2_documentation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=bpmn2_RootElement_strategy)
@settings(max_examples=50)
def test_bpmn2_rootelement_instantiation(instance):
    assert isinstance(instance, bpmn2_RootElement)

@given(instance=bpmn2_EObject_strategy)
@settings(max_examples=50)
def test_bpmn2_eobject_instantiation(instance):
    assert isinstance(instance, bpmn2_EObject)

@given(instance=bpmn2_Operation_strategy)
@settings(max_examples=50)
def test_bpmn2_operation_instantiation(instance):
    assert isinstance(instance, bpmn2_Operation)



@given(instance=bpmn2_Operation_strategy)
def test_bpmn2_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RootElement_strategy)
@settings(max_examples=50)
def test_rootelement_instantiation(instance):
    assert isinstance(instance, RootElement)

@given(instance=bpmn2_CallableElement_strategy)
@settings(max_examples=50)
def test_bpmn2_callableelement_instantiation(instance):
    assert isinstance(instance, bpmn2_CallableElement)



@given(instance=bpmn2_CallableElement_strategy)
def test_bpmn2_callableelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_EndPoint_strategy)
@settings(max_examples=50)
def test_bpmn2_endpoint_instantiation(instance):
    assert isinstance(instance, bpmn2_EndPoint)

@given(instance=bpmn2_Resource_strategy)
@settings(max_examples=50)
def test_bpmn2_resource_instantiation(instance):
    assert isinstance(instance, bpmn2_Resource)



@given(instance=bpmn2_Resource_strategy)
def test_bpmn2_resource_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Collaboration_strategy)
@settings(max_examples=50)
def test_bpmn2_collaboration_instantiation(instance):
    assert isinstance(instance, bpmn2_Collaboration)



@given(instance=bpmn2_Collaboration_strategy)
def test_bpmn2_collaboration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_Collaboration_strategy)
def test_bpmn2_collaboration_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=bpmn2_CorrelationProperty_strategy)
@settings(max_examples=50)
def test_bpmn2_correlationproperty_instantiation(instance):
    assert isinstance(instance, bpmn2_CorrelationProperty)



@given(instance=bpmn2_CorrelationProperty_strategy)
def test_bpmn2_correlationproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_ItemDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_itemdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ItemDefinition)



@given(instance=bpmn2_ItemDefinition_strategy)
def test_bpmn2_itemdefinition_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original



@given(instance=bpmn2_ItemDefinition_strategy)
def test_bpmn2_itemdefinition_itemKind_setter(instance):
    original = instance.itemKind
    instance.itemKind = original
    assert instance.itemKind == original

@given(instance=bpmn2_Error_strategy)
@settings(max_examples=50)
def test_bpmn2_error_instantiation(instance):
    assert isinstance(instance, bpmn2_Error)



@given(instance=bpmn2_Error_strategy)
def test_bpmn2_error_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_Error_strategy)
def test_bpmn2_error_errorCode_setter(instance):
    original = instance.errorCode
    instance.errorCode = original
    assert instance.errorCode == original

@given(instance=bpmn2_Message_strategy)
@settings(max_examples=50)
def test_bpmn2_message_instantiation(instance):
    assert isinstance(instance, bpmn2_Message)



@given(instance=bpmn2_Message_strategy)
def test_bpmn2_message_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Interface_strategy)
@settings(max_examples=50)
def test_bpmn2_interface_instantiation(instance):
    assert isinstance(instance, bpmn2_Interface)



@given(instance=bpmn2_Interface_strategy)
def test_bpmn2_interface_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_BPMNDiagram_strategy)
@settings(max_examples=50)
def test_bpmn2_bpmndiagram_instantiation(instance):
    assert isinstance(instance, bpmn2_BPMNDiagram)

@given(instance=bpmn2_Definitions_strategy)
@settings(max_examples=50)
def test_bpmn2_definitions_instantiation(instance):
    assert isinstance(instance, bpmn2_Definitions)



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_exporter_setter(instance):
    original = instance.exporter
    instance.exporter = original
    assert instance.exporter == original



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_exporterVersion_setter(instance):
    original = instance.exporterVersion
    instance.exporterVersion = original
    assert instance.exporterVersion == original



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_typeLanguage_setter(instance):
    original = instance.typeLanguage
    instance.typeLanguage = original
    assert instance.typeLanguage == original



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_expressionLanguage_setter(instance):
    original = instance.expressionLanguage
    instance.expressionLanguage = original
    assert instance.expressionLanguage == original



@given(instance=bpmn2_Definitions_strategy)
def test_bpmn2_definitions_targetNamespace_setter(instance):
    original = instance.targetNamespace
    instance.targetNamespace = original
    assert instance.targetNamespace == original

@given(instance=SubProcess_strategy)
@settings(max_examples=50)
def test_subprocess_instantiation(instance):
    assert isinstance(instance, SubProcess)

@given(instance=bpmn2_Transaction_strategy)
@settings(max_examples=50)
def test_bpmn2_transaction_instantiation(instance):
    assert isinstance(instance, bpmn2_Transaction)



@given(instance=bpmn2_Transaction_strategy)
def test_bpmn2_transaction_protocol_setter(instance):
    original = instance.protocol
    instance.protocol = original
    assert instance.protocol == original



@given(instance=bpmn2_Transaction_strategy)
def test_bpmn2_transaction_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=bpmn2_AdHocSubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2_adhocsubprocess_instantiation(instance):
    assert isinstance(instance, bpmn2_AdHocSubProcess)



@given(instance=bpmn2_AdHocSubProcess_strategy)
def test_bpmn2_adhocsubprocess_ordering_setter(instance):
    original = instance.ordering
    instance.ordering = original
    assert instance.ordering == original



@given(instance=bpmn2_AdHocSubProcess_strategy)
def test_bpmn2_adhocsubprocess_cancelRemainingInstances_setter(instance):
    original = instance.cancelRemainingInstances
    instance.cancelRemainingInstances = original
    assert instance.cancelRemainingInstances == original

@given(instance=bpmn2_ComplexBehaviorDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_complexbehaviordefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ComplexBehaviorDefinition)

@given(instance=LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, LoopCharacteristics)

@given(instance=bpmn2_StandardLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2_standardloopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2_StandardLoopCharacteristics)



@given(instance=bpmn2_StandardLoopCharacteristics_strategy)
def test_bpmn2_standardloopcharacteristics_testBefore_setter(instance):
    original = instance.testBefore
    instance.testBefore = original
    assert instance.testBefore == original

@given(instance=bpmn2_MultiInstanceLoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2_multiinstanceloopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2_MultiInstanceLoopCharacteristics)



@given(instance=bpmn2_MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2_multiinstanceloopcharacteristics_isSequential_setter(instance):
    original = instance.isSequential
    instance.isSequential = original
    assert instance.isSequential == original



@given(instance=bpmn2_MultiInstanceLoopCharacteristics_strategy)
def test_bpmn2_multiinstanceloopcharacteristics_behavior_setter(instance):
    original = instance.behavior
    instance.behavior = original
    assert instance.behavior == original

@given(instance=bpmn2_Category_strategy)
@settings(max_examples=50)
def test_bpmn2_category_instantiation(instance):
    assert isinstance(instance, bpmn2_Category)



@given(instance=bpmn2_Category_strategy)
def test_bpmn2_category_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=bpmn2_Association_strategy)
@settings(max_examples=50)
def test_bpmn2_association_instantiation(instance):
    assert isinstance(instance, bpmn2_Association)



@given(instance=bpmn2_Association_strategy)
def test_bpmn2_association_associationDirection_setter(instance):
    original = instance.associationDirection
    instance.associationDirection = original
    assert instance.associationDirection == original

@given(instance=bpmn2_Group_strategy)
@settings(max_examples=50)
def test_bpmn2_group_instantiation(instance):
    assert isinstance(instance, bpmn2_Group)

@given(instance=bpmn2_TextAnnotation_strategy)
@settings(max_examples=50)
def test_bpmn2_textannotation_instantiation(instance):
    assert isinstance(instance, bpmn2_TextAnnotation)



@given(instance=bpmn2_TextAnnotation_strategy)
def test_bpmn2_textannotation_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original



@given(instance=bpmn2_TextAnnotation_strategy)
def test_bpmn2_textannotation_textFormat_setter(instance):
    original = instance.textFormat
    instance.textFormat = original
    assert instance.textFormat == original

@given(instance=Choreography_strategy)
@settings(max_examples=50)
def test_choreography_instantiation(instance):
    assert isinstance(instance, Choreography)

@given(instance=bpmn2_GlobalChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globalchoreographytask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalChoreographyTask)

@given(instance=ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_choreographyactivity_instantiation(instance):
    assert isinstance(instance, ChoreographyActivity)

@given(instance=bpmn2_SubChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2_subchoreography_instantiation(instance):
    assert isinstance(instance, bpmn2_SubChoreography)

@given(instance=bpmn2_ChoreographyTask_strategy)
@settings(max_examples=50)
def test_bpmn2_choreographytask_instantiation(instance):
    assert isinstance(instance, bpmn2_ChoreographyTask)

@given(instance=bpmn2_CallChoreography_strategy)
@settings(max_examples=50)
def test_bpmn2_callchoreography_instantiation(instance):
    assert isinstance(instance, bpmn2_CallChoreography)

@given(instance=bpmn2_PartnerRole_strategy)
@settings(max_examples=50)
def test_bpmn2_partnerrole_instantiation(instance):
    assert isinstance(instance, bpmn2_PartnerRole)



@given(instance=bpmn2_PartnerRole_strategy)
def test_bpmn2_partnerrole_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_PartnerEntity_strategy)
@settings(max_examples=50)
def test_bpmn2_partnerentity_instantiation(instance):
    assert isinstance(instance, bpmn2_PartnerEntity)



@given(instance=bpmn2_PartnerEntity_strategy)
def test_bpmn2_partnerentity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_GlobalConversation_strategy)
@settings(max_examples=50)
def test_bpmn2_globalconversation_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalConversation)

@given(instance=ConversationNode_strategy)
@settings(max_examples=50)
def test_conversationnode_instantiation(instance):
    assert isinstance(instance, ConversationNode)

@given(instance=bpmn2_Conversation_strategy)
@settings(max_examples=50)
def test_bpmn2_conversation_instantiation(instance):
    assert isinstance(instance, bpmn2_Conversation)

@given(instance=bpmn2_SubConversation_strategy)
@settings(max_examples=50)
def test_bpmn2_subconversation_instantiation(instance):
    assert isinstance(instance, bpmn2_SubConversation)

@given(instance=bpmn2_CallConversation_strategy)
@settings(max_examples=50)
def test_bpmn2_callconversation_instantiation(instance):
    assert isinstance(instance, bpmn2_CallConversation)

@given(instance=bpmn2_DataObjectReference_strategy)
@settings(max_examples=50)
def test_bpmn2_dataobjectreference_instantiation(instance):
    assert isinstance(instance, bpmn2_DataObjectReference)

@given(instance=bpmn2_DataStoreReference_strategy)
@settings(max_examples=50)
def test_bpmn2_datastorereference_instantiation(instance):
    assert isinstance(instance, bpmn2_DataStoreReference)

@given(instance=bpmn2_DataStore_strategy)
@settings(max_examples=50)
def test_bpmn2_datastore_instantiation(instance):
    assert isinstance(instance, bpmn2_DataStore)



@given(instance=bpmn2_DataStore_strategy)
def test_bpmn2_datastore_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original



@given(instance=bpmn2_DataStore_strategy)
def test_bpmn2_datastore_isUnlimited_setter(instance):
    original = instance.isUnlimited
    instance.isUnlimited = original
    assert instance.isUnlimited == original



@given(instance=bpmn2_DataStore_strategy)
def test_bpmn2_datastore_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_DataObject_strategy)
@settings(max_examples=50)
def test_bpmn2_dataobject_instantiation(instance):
    assert isinstance(instance, bpmn2_DataObject)



@given(instance=bpmn2_DataObject_strategy)
def test_bpmn2_dataobject_isCollection_setter(instance):
    original = instance.isCollection
    instance.isCollection = original
    assert instance.isCollection == original

@given(instance=bpmn2_Signal_strategy)
@settings(max_examples=50)
def test_bpmn2_signal_instantiation(instance):
    assert isinstance(instance, bpmn2_Signal)



@given(instance=bpmn2_Signal_strategy)
def test_bpmn2_signal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_Escalation_strategy)
@settings(max_examples=50)
def test_bpmn2_escalation_instantiation(instance):
    assert isinstance(instance, bpmn2_Escalation)



@given(instance=bpmn2_Escalation_strategy)
def test_bpmn2_escalation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=bpmn2_Escalation_strategy)
def test_bpmn2_escalation_escalationCode_setter(instance):
    original = instance.escalationCode
    instance.escalationCode = original
    assert instance.escalationCode == original



@given(instance=bpmn2_Escalation_strategy)
def test_bpmn2_escalation_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=EventDefinition_strategy)
@settings(max_examples=50)
def test_eventdefinition_instantiation(instance):
    assert isinstance(instance, EventDefinition)

@given(instance=bpmn2_SignalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_signaleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_SignalEventDefinition)

@given(instance=bpmn2_CompensateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_compensateeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_CompensateEventDefinition)



@given(instance=bpmn2_CompensateEventDefinition_strategy)
def test_bpmn2_compensateeventdefinition_waitForCompletion_setter(instance):
    original = instance.waitForCompletion
    instance.waitForCompletion = original
    assert instance.waitForCompletion == original

@given(instance=bpmn2_ConditionalEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_conditionaleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ConditionalEventDefinition)

@given(instance=bpmn2_MessageEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_messageeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_MessageEventDefinition)

@given(instance=bpmn2_ErrorEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_erroreventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_ErrorEventDefinition)

@given(instance=bpmn2_TimerEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_timereventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_TimerEventDefinition)

@given(instance=bpmn2_EscalationEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_escalationeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_EscalationEventDefinition)

@given(instance=bpmn2_TerminateEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_terminateeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_TerminateEventDefinition)

@given(instance=bpmn2_LinkEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_linkeventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_LinkEventDefinition)



@given(instance=bpmn2_LinkEventDefinition_strategy)
def test_bpmn2_linkeventdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=bpmn2_CancelEventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_canceleventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_CancelEventDefinition)

@given(instance=ThrowEvent_strategy)
@settings(max_examples=50)
def test_throwevent_instantiation(instance):
    assert isinstance(instance, ThrowEvent)

@given(instance=bpmn2_ImplicitThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_implicitthrowevent_instantiation(instance):
    assert isinstance(instance, bpmn2_ImplicitThrowEvent)

@given(instance=bpmn2_EndEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_endevent_instantiation(instance):
    assert isinstance(instance, bpmn2_EndEvent)

@given(instance=bpmn2_IntermediateThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_intermediatethrowevent_instantiation(instance):
    assert isinstance(instance, bpmn2_IntermediateThrowEvent)

@given(instance=bpmn2_Extension_strategy)
@settings(max_examples=50)
def test_bpmn2_extension_instantiation(instance):
    assert isinstance(instance, bpmn2_Extension)



@given(instance=bpmn2_Extension_strategy)
def test_bpmn2_extension_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=bpmn2_Extension_strategy)
def test_bpmn2_extension_mustUnderstand_setter(instance):
    original = instance.mustUnderstand
    instance.mustUnderstand = original
    assert instance.mustUnderstand == original

@given(instance=bpmn2_Relationship_strategy)
@settings(max_examples=50)
def test_bpmn2_relationship_instantiation(instance):
    assert isinstance(instance, bpmn2_Relationship)



@given(instance=bpmn2_Relationship_strategy)
def test_bpmn2_relationship_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=bpmn2_Relationship_strategy)
def test_bpmn2_relationship_direction_setter(instance):
    original = instance.direction
    instance.direction = original
    assert instance.direction == original

@given(instance=bpmn2_Assignment_strategy)
@settings(max_examples=50)
def test_bpmn2_assignment_instantiation(instance):
    assert isinstance(instance, bpmn2_Assignment)

@given(instance=Gateway_strategy)
@settings(max_examples=50)
def test_gateway_instantiation(instance):
    assert isinstance(instance, Gateway)

@given(instance=bpmn2_ParallelGateway_strategy)
@settings(max_examples=50)
def test_bpmn2_parallelgateway_instantiation(instance):
    assert isinstance(instance, bpmn2_ParallelGateway)

@given(instance=bpmn2_ExclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2_exclusivegateway_instantiation(instance):
    assert isinstance(instance, bpmn2_ExclusiveGateway)

@given(instance=bpmn2_ComplexGateway_strategy)
@settings(max_examples=50)
def test_bpmn2_complexgateway_instantiation(instance):
    assert isinstance(instance, bpmn2_ComplexGateway)

@given(instance=bpmn2_InclusiveGateway_strategy)
@settings(max_examples=50)
def test_bpmn2_inclusivegateway_instantiation(instance):
    assert isinstance(instance, bpmn2_InclusiveGateway)

@given(instance=bpmn2_EventBasedGateway_strategy)
@settings(max_examples=50)
def test_bpmn2_eventbasedgateway_instantiation(instance):
    assert isinstance(instance, bpmn2_EventBasedGateway)



@given(instance=bpmn2_EventBasedGateway_strategy)
def test_bpmn2_eventbasedgateway_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original



@given(instance=bpmn2_EventBasedGateway_strategy)
def test_bpmn2_eventbasedgateway_eventGatewayType_setter(instance):
    original = instance.eventGatewayType
    instance.eventGatewayType = original
    assert instance.eventGatewayType == original

@given(instance=HumanPerformer_strategy)
@settings(max_examples=50)
def test_humanperformer_instantiation(instance):
    assert isinstance(instance, HumanPerformer)

@given(instance=bpmn2_PotentialOwner_strategy)
@settings(max_examples=50)
def test_bpmn2_potentialowner_instantiation(instance):
    assert isinstance(instance, bpmn2_PotentialOwner)

@given(instance=Performer_strategy)
@settings(max_examples=50)
def test_performer_instantiation(instance):
    assert isinstance(instance, Performer)

@given(instance=bpmn2_HumanPerformer_strategy)
@settings(max_examples=50)
def test_bpmn2_humanperformer_instantiation(instance):
    assert isinstance(instance, bpmn2_HumanPerformer)

@given(instance=bpmn2_Rendering_strategy)
@settings(max_examples=50)
def test_bpmn2_rendering_instantiation(instance):
    assert isinstance(instance, bpmn2_Rendering)

@given(instance=bpmn2_DataAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_dataassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_DataAssociation)

@given(instance=DataAssociation_strategy)
@settings(max_examples=50)
def test_dataassociation_instantiation(instance):
    assert isinstance(instance, DataAssociation)

@given(instance=bpmn2_EventDefinition_strategy)
@settings(max_examples=50)
def test_bpmn2_eventdefinition_instantiation(instance):
    assert isinstance(instance, bpmn2_EventDefinition)

@given(instance=Event_strategy)
@settings(max_examples=50)
def test_event_instantiation(instance):
    assert isinstance(instance, Event)

@given(instance=bpmn2_ThrowEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_throwevent_instantiation(instance):
    assert isinstance(instance, bpmn2_ThrowEvent)

@given(instance=bpmn2_CatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_catchevent_instantiation(instance):
    assert isinstance(instance, bpmn2_CatchEvent)



@given(instance=bpmn2_CatchEvent_strategy)
def test_bpmn2_catchevent_parallelMultiple_setter(instance):
    original = instance.parallelMultiple
    instance.parallelMultiple = original
    assert instance.parallelMultiple == original

@given(instance=CatchEvent_strategy)
@settings(max_examples=50)
def test_catchevent_instantiation(instance):
    assert isinstance(instance, CatchEvent)

@given(instance=bpmn2_StartEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_startevent_instantiation(instance):
    assert isinstance(instance, bpmn2_StartEvent)



@given(instance=bpmn2_StartEvent_strategy)
def test_bpmn2_startevent_isInterrupting_setter(instance):
    original = instance.isInterrupting
    instance.isInterrupting = original
    assert instance.isInterrupting == original

@given(instance=bpmn2_IntermediateCatchEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_intermediatecatchevent_instantiation(instance):
    assert isinstance(instance, bpmn2_IntermediateCatchEvent)

@given(instance=bpmn2_DataOutputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_dataoutputassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_DataOutputAssociation)

@given(instance=bpmn2_DataInputAssociation_strategy)
@settings(max_examples=50)
def test_bpmn2_datainputassociation_instantiation(instance):
    assert isinstance(instance, bpmn2_DataInputAssociation)

@given(instance=bpmn2_BoundaryEvent_strategy)
@settings(max_examples=50)
def test_bpmn2_boundaryevent_instantiation(instance):
    assert isinstance(instance, bpmn2_BoundaryEvent)



@given(instance=bpmn2_BoundaryEvent_strategy)
def test_bpmn2_boundaryevent_cancelActivity_setter(instance):
    original = instance.cancelActivity
    instance.cancelActivity = original
    assert instance.cancelActivity == original

@given(instance=bpmn2_LoopCharacteristics_strategy)
@settings(max_examples=50)
def test_bpmn2_loopcharacteristics_instantiation(instance):
    assert isinstance(instance, bpmn2_LoopCharacteristics)

@given(instance=FlowNode_strategy)
@settings(max_examples=50)
def test_flownode_instantiation(instance):
    assert isinstance(instance, FlowNode)

@given(instance=bpmn2_ChoreographyActivity_strategy)
@settings(max_examples=50)
def test_bpmn2_choreographyactivity_instantiation(instance):
    assert isinstance(instance, bpmn2_ChoreographyActivity)



@given(instance=bpmn2_ChoreographyActivity_strategy)
def test_bpmn2_choreographyactivity_loopType_setter(instance):
    original = instance.loopType
    instance.loopType = original
    assert instance.loopType == original

@given(instance=bpmn2_Event_strategy)
@settings(max_examples=50)
def test_bpmn2_event_instantiation(instance):
    assert isinstance(instance, bpmn2_Event)

@given(instance=bpmn2_Gateway_strategy)
@settings(max_examples=50)
def test_bpmn2_gateway_instantiation(instance):
    assert isinstance(instance, bpmn2_Gateway)



@given(instance=bpmn2_Gateway_strategy)
def test_bpmn2_gateway_gatewayDirection_setter(instance):
    original = instance.gatewayDirection
    instance.gatewayDirection = original
    assert instance.gatewayDirection == original

@given(instance=bpmn2_Activity_strategy)
@settings(max_examples=50)
def test_bpmn2_activity_instantiation(instance):
    assert isinstance(instance, bpmn2_Activity)



@given(instance=bpmn2_Activity_strategy)
def test_bpmn2_activity_isForCompensation_setter(instance):
    original = instance.isForCompensation
    instance.isForCompensation = original
    assert instance.isForCompensation == original



@given(instance=bpmn2_Activity_strategy)
def test_bpmn2_activity_startQuantity_setter(instance):
    original = instance.startQuantity
    instance.startQuantity = original
    assert instance.startQuantity == original



@given(instance=bpmn2_Activity_strategy)
def test_bpmn2_activity_completionQuantity_setter(instance):
    original = instance.completionQuantity
    instance.completionQuantity = original
    assert instance.completionQuantity == original

@given(instance=Activity_strategy)
@settings(max_examples=50)
def test_activity_instantiation(instance):
    assert isinstance(instance, Activity)

@given(instance=bpmn2_CallActivity_strategy)
@settings(max_examples=50)
def test_bpmn2_callactivity_instantiation(instance):
    assert isinstance(instance, bpmn2_CallActivity)

@given(instance=bpmn2_SubProcess_strategy)
@settings(max_examples=50)
def test_bpmn2_subprocess_instantiation(instance):
    assert isinstance(instance, bpmn2_SubProcess)



@given(instance=bpmn2_SubProcess_strategy)
def test_bpmn2_subprocess_triggeredByEvent_setter(instance):
    original = instance.triggeredByEvent
    instance.triggeredByEvent = original
    assert instance.triggeredByEvent == original

@given(instance=bpmn2_Task_strategy)
@settings(max_examples=50)
def test_bpmn2_task_instantiation(instance):
    assert isinstance(instance, bpmn2_Task)

@given(instance=Task_strategy)
@settings(max_examples=50)
def test_task_instantiation(instance):
    assert isinstance(instance, Task)

@given(instance=bpmn2_SendTask_strategy)
@settings(max_examples=50)
def test_bpmn2_sendtask_instantiation(instance):
    assert isinstance(instance, bpmn2_SendTask)



@given(instance=bpmn2_SendTask_strategy)
def test_bpmn2_sendtask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_ScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2_scripttask_instantiation(instance):
    assert isinstance(instance, bpmn2_ScriptTask)



@given(instance=bpmn2_ScriptTask_strategy)
def test_bpmn2_scripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original



@given(instance=bpmn2_ScriptTask_strategy)
def test_bpmn2_scripttask_scriptFormat_setter(instance):
    original = instance.scriptFormat
    instance.scriptFormat = original
    assert instance.scriptFormat == original

@given(instance=bpmn2_BusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2_businessruletask_instantiation(instance):
    assert isinstance(instance, bpmn2_BusinessRuleTask)



@given(instance=bpmn2_BusinessRuleTask_strategy)
def test_bpmn2_businessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_ReceiveTask_strategy)
@settings(max_examples=50)
def test_bpmn2_receivetask_instantiation(instance):
    assert isinstance(instance, bpmn2_ReceiveTask)



@given(instance=bpmn2_ReceiveTask_strategy)
def test_bpmn2_receivetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original



@given(instance=bpmn2_ReceiveTask_strategy)
def test_bpmn2_receivetask_instantiate_setter(instance):
    original = instance.instantiate
    instance.instantiate = original
    assert instance.instantiate == original

@given(instance=bpmn2_ServiceTask_strategy)
@settings(max_examples=50)
def test_bpmn2_servicetask_instantiation(instance):
    assert isinstance(instance, bpmn2_ServiceTask)



@given(instance=bpmn2_ServiceTask_strategy)
def test_bpmn2_servicetask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_UserTask_strategy)
@settings(max_examples=50)
def test_bpmn2_usertask_instantiation(instance):
    assert isinstance(instance, bpmn2_UserTask)



@given(instance=bpmn2_UserTask_strategy)
def test_bpmn2_usertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_ManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2_manualtask_instantiation(instance):
    assert isinstance(instance, bpmn2_ManualTask)

@given(instance=GlobalTask_strategy)
@settings(max_examples=50)
def test_globaltask_instantiation(instance):
    assert isinstance(instance, GlobalTask)

@given(instance=bpmn2_GlobalScriptTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globalscripttask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalScriptTask)



@given(instance=bpmn2_GlobalScriptTask_strategy)
def test_bpmn2_globalscripttask_scriptLanguage_setter(instance):
    original = instance.scriptLanguage
    instance.scriptLanguage = original
    assert instance.scriptLanguage == original



@given(instance=bpmn2_GlobalScriptTask_strategy)
def test_bpmn2_globalscripttask_script_setter(instance):
    original = instance.script
    instance.script = original
    assert instance.script == original

@given(instance=bpmn2_GlobalUserTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globalusertask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalUserTask)



@given(instance=bpmn2_GlobalUserTask_strategy)
def test_bpmn2_globalusertask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_GlobalBusinessRuleTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globalbusinessruletask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalBusinessRuleTask)



@given(instance=bpmn2_GlobalBusinessRuleTask_strategy)
def test_bpmn2_globalbusinessruletask_implementation_setter(instance):
    original = instance.implementation
    instance.implementation = original
    assert instance.implementation == original

@given(instance=bpmn2_GlobalManualTask_strategy)
@settings(max_examples=50)
def test_bpmn2_globalmanualtask_instantiation(instance):
    assert isinstance(instance, bpmn2_GlobalManualTask)
