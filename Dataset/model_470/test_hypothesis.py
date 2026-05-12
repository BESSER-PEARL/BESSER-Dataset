import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ObjectNode,
    UML2_ActivityParameterNode,
    StructuredClassifier,
    UML2_EncapsulatedClassifier,
    EncapsulatedClassifier,
    BehavioredClassifier,
    UML2_Collaboration,
    UML2_Class,
    Behavior,
    UML2_Interaction,
    Type,
    UML2_Classifier,
    Property,
    UML2_ExtensionEnd,
    LiteralSpecification,
    UML2_LiteralUnlimitedNatural,
    UML2_LiteralNull,
    UML2_LiteralInteger,
    UML2_LiteralBoolean,
    UML2_LiteralString,
    UML2_CentralBufferNode,
    UML2_Port,
    StateMachine,
    UML2_ProtocolStateMachine,
    UML2_ExpansionNode,
    CentralBufferNode,
    UML2_DataStoreNode,
    OpaqueExpression,
    UML2_Expression,
    TypedElement,
    UML2_ObjectNode,
    UML2_ValueSpecification,
    UML2_Operation,
    InputPin,
    UML2_ValuePin,
    Class,
    UML2_Component,
    UML2_Behavior,
    UML2_Stereotype,
    Node,
    UML2_ExecutionEnvironment,
    UML2_Device,
    Pin,
    UML2_InputPin,
    UML2_OutputPin,
    Artifact,
    UML2_DeploymentSpecification,
    ValueSpecification,
    UML2_LiteralSpecification,
    UML2_OpaqueExpression,
    UML2_Interval,
    DataType,
    UML2_PrimitiveType,
    UML2_Enumeration,
    Classifier,
    UML2_Association,
    UML2_Interface,
    UML2_Actor,
    UML2_Artifact,
    UML2_InformationItem,
    UML2_ParameterableClassifier,
    UML2_DataType,
    UML2_Type,
    UML2_TypedElement,
    Association,
    UML2_AssociationClass,
    UML2_Extension,
    UML2_CommunicationPath,
    UML2_TimeExpression,
    UML2_Pin,
    UML2_Duration,
    UML2_BehavioredClassifier,
    UML2_Activity,
    UML2_Signal,
    UML2_StructuralFeature,
    UML2_UseCase,
    UML2_Variable,
    UML2_TestIdentityAction,
    UML2_StateMachine,
    UML2_InstanceValue,
    UML2_Node,
    UML2_Parameter,
    StructuralFeature,
    UML2_Property,
    Interval,
    UML2_DurationInterval,
    UML2_TimeInterval,
    UML2_StructuredClassifier,
    UML2_TemplateableClassifier,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_objectnode_is_not_abstract():
    assert not inspect.isabstract(ObjectNode)


def test_objectnode_constructor_exists():
    assert callable(ObjectNode.__init__)


def test_objectnode_constructor_args():
    sig = inspect.signature(ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activityparameternode_is_not_abstract():
    assert not inspect.isabstract(UML2_ActivityParameterNode)


def test_uml2_activityparameternode_constructor_exists():
    assert callable(UML2_ActivityParameterNode.__init__)


def test_uml2_activityparameternode_constructor_args():
    sig = inspect.signature(UML2_ActivityParameterNode.__init__)
    params = list(sig.parameters.keys())



def test_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(StructuredClassifier)


def test_structuredclassifier_constructor_exists():
    assert callable(StructuredClassifier.__init__)


def test_structuredclassifier_constructor_args():
    sig = inspect.signature(StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_EncapsulatedClassifier)


def test_uml2_encapsulatedclassifier_constructor_exists():
    assert callable(UML2_EncapsulatedClassifier.__init__)


def test_uml2_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(UML2_EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_encapsulatedclassifier_is_not_abstract():
    assert not inspect.isabstract(EncapsulatedClassifier)


def test_encapsulatedclassifier_constructor_exists():
    assert callable(EncapsulatedClassifier.__init__)


def test_encapsulatedclassifier_constructor_args():
    sig = inspect.signature(EncapsulatedClassifier.__init__)
    params = list(sig.parameters.keys())



def test_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(BehavioredClassifier)


def test_behavioredclassifier_constructor_exists():
    assert callable(BehavioredClassifier.__init__)


def test_behavioredclassifier_constructor_args():
    sig = inspect.signature(BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_collaboration_is_not_abstract():
    assert not inspect.isabstract(UML2_Collaboration)


def test_uml2_collaboration_constructor_exists():
    assert callable(UML2_Collaboration.__init__)


def test_uml2_collaboration_constructor_args():
    sig = inspect.signature(UML2_Collaboration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_class_is_not_abstract():
    assert not inspect.isabstract(UML2_Class)


def test_uml2_class_constructor_exists():
    assert callable(UML2_Class.__init__)


def test_uml2_class_constructor_args():
    sig = inspect.signature(UML2_Class.__init__)
    params = list(sig.parameters.keys())



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interaction_is_not_abstract():
    assert not inspect.isabstract(UML2_Interaction)


def test_uml2_interaction_constructor_exists():
    assert callable(UML2_Interaction.__init__)


def test_uml2_interaction_constructor_args():
    sig = inspect.signature(UML2_Interaction.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2_classifier_is_not_abstract():
    assert not inspect.isabstract(UML2_Classifier)


def test_uml2_classifier_constructor_exists():
    assert callable(UML2_Classifier.__init__)


def test_uml2_classifier_constructor_args():
    sig = inspect.signature(UML2_Classifier.__init__)
    params = list(sig.parameters.keys())



def test_property_is_not_abstract():
    assert not inspect.isabstract(Property)


def test_property_constructor_exists():
    assert callable(Property.__init__)


def test_property_constructor_args():
    sig = inspect.signature(Property.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extensionend_is_not_abstract():
    assert not inspect.isabstract(UML2_ExtensionEnd)


def test_uml2_extensionend_constructor_exists():
    assert callable(UML2_ExtensionEnd.__init__)


def test_uml2_extensionend_constructor_args():
    sig = inspect.signature(UML2_ExtensionEnd.__init__)
    params = list(sig.parameters.keys())



def test_literalspecification_is_not_abstract():
    assert not inspect.isabstract(LiteralSpecification)


def test_literalspecification_constructor_exists():
    assert callable(LiteralSpecification.__init__)


def test_literalspecification_constructor_args():
    sig = inspect.signature(LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalunlimitednatural_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralUnlimitedNatural)


def test_uml2_literalunlimitednatural_constructor_exists():
    assert callable(UML2_LiteralUnlimitedNatural.__init__)


def test_uml2_literalunlimitednatural_constructor_args():
    sig = inspect.signature(UML2_LiteralUnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalnull_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralNull)


def test_uml2_literalnull_constructor_exists():
    assert callable(UML2_LiteralNull.__init__)


def test_uml2_literalnull_constructor_args():
    sig = inspect.signature(UML2_LiteralNull.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalinteger_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralInteger)


def test_uml2_literalinteger_constructor_exists():
    assert callable(UML2_LiteralInteger.__init__)


def test_uml2_literalinteger_constructor_args():
    sig = inspect.signature(UML2_LiteralInteger.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalboolean_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralBoolean)


def test_uml2_literalboolean_constructor_exists():
    assert callable(UML2_LiteralBoolean.__init__)


def test_uml2_literalboolean_constructor_args():
    sig = inspect.signature(UML2_LiteralBoolean.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalstring_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralString)


def test_uml2_literalstring_constructor_exists():
    assert callable(UML2_LiteralString.__init__)


def test_uml2_literalstring_constructor_args():
    sig = inspect.signature(UML2_LiteralString.__init__)
    params = list(sig.parameters.keys())



def test_uml2_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(UML2_CentralBufferNode)


def test_uml2_centralbuffernode_constructor_exists():
    assert callable(UML2_CentralBufferNode.__init__)


def test_uml2_centralbuffernode_constructor_args():
    sig = inspect.signature(UML2_CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_port_is_not_abstract():
    assert not inspect.isabstract(UML2_Port)


def test_uml2_port_constructor_exists():
    assert callable(UML2_Port.__init__)


def test_uml2_port_constructor_args():
    sig = inspect.signature(UML2_Port.__init__)
    params = list(sig.parameters.keys())



def test_statemachine_is_not_abstract():
    assert not inspect.isabstract(StateMachine)


def test_statemachine_constructor_exists():
    assert callable(StateMachine.__init__)


def test_statemachine_constructor_args():
    sig = inspect.signature(StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_protocolstatemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_ProtocolStateMachine)


def test_uml2_protocolstatemachine_constructor_exists():
    assert callable(UML2_ProtocolStateMachine.__init__)


def test_uml2_protocolstatemachine_constructor_args():
    sig = inspect.signature(UML2_ProtocolStateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expansionnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ExpansionNode)


def test_uml2_expansionnode_constructor_exists():
    assert callable(UML2_ExpansionNode.__init__)


def test_uml2_expansionnode_constructor_args():
    sig = inspect.signature(UML2_ExpansionNode.__init__)
    params = list(sig.parameters.keys())



def test_centralbuffernode_is_not_abstract():
    assert not inspect.isabstract(CentralBufferNode)


def test_centralbuffernode_constructor_exists():
    assert callable(CentralBufferNode.__init__)


def test_centralbuffernode_constructor_args():
    sig = inspect.signature(CentralBufferNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datastorenode_is_not_abstract():
    assert not inspect.isabstract(UML2_DataStoreNode)


def test_uml2_datastorenode_constructor_exists():
    assert callable(UML2_DataStoreNode.__init__)


def test_uml2_datastorenode_constructor_args():
    sig = inspect.signature(UML2_DataStoreNode.__init__)
    params = list(sig.parameters.keys())



def test_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(OpaqueExpression)


def test_opaqueexpression_constructor_exists():
    assert callable(OpaqueExpression.__init__)


def test_opaqueexpression_constructor_args():
    sig = inspect.signature(OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_expression_is_not_abstract():
    assert not inspect.isabstract(UML2_Expression)


def test_uml2_expression_constructor_exists():
    assert callable(UML2_Expression.__init__)


def test_uml2_expression_constructor_args():
    sig = inspect.signature(UML2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_uml2_objectnode_is_not_abstract():
    assert not inspect.isabstract(UML2_ObjectNode)


def test_uml2_objectnode_constructor_exists():
    assert callable(UML2_ObjectNode.__init__)


def test_uml2_objectnode_constructor_args():
    sig = inspect.signature(UML2_ObjectNode.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuespecification_is_not_abstract():
    assert not inspect.isabstract(UML2_ValueSpecification)


def test_uml2_valuespecification_constructor_exists():
    assert callable(UML2_ValueSpecification.__init__)


def test_uml2_valuespecification_constructor_args():
    sig = inspect.signature(UML2_ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_operation_is_not_abstract():
    assert not inspect.isabstract(UML2_Operation)


def test_uml2_operation_constructor_exists():
    assert callable(UML2_Operation.__init__)


def test_uml2_operation_constructor_args():
    sig = inspect.signature(UML2_Operation.__init__)
    params = list(sig.parameters.keys())



def test_inputpin_is_not_abstract():
    assert not inspect.isabstract(InputPin)


def test_inputpin_constructor_exists():
    assert callable(InputPin.__init__)


def test_inputpin_constructor_args():
    sig = inspect.signature(InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_valuepin_is_not_abstract():
    assert not inspect.isabstract(UML2_ValuePin)


def test_uml2_valuepin_constructor_exists():
    assert callable(UML2_ValuePin.__init__)


def test_uml2_valuepin_constructor_args():
    sig = inspect.signature(UML2_ValuePin.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_uml2_component_is_not_abstract():
    assert not inspect.isabstract(UML2_Component)


def test_uml2_component_constructor_exists():
    assert callable(UML2_Component.__init__)


def test_uml2_component_constructor_args():
    sig = inspect.signature(UML2_Component.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavior_is_not_abstract():
    assert not inspect.isabstract(UML2_Behavior)


def test_uml2_behavior_constructor_exists():
    assert callable(UML2_Behavior.__init__)


def test_uml2_behavior_constructor_args():
    sig = inspect.signature(UML2_Behavior.__init__)
    params = list(sig.parameters.keys())



def test_uml2_stereotype_is_not_abstract():
    assert not inspect.isabstract(UML2_Stereotype)


def test_uml2_stereotype_constructor_exists():
    assert callable(UML2_Stereotype.__init__)


def test_uml2_stereotype_constructor_args():
    sig = inspect.signature(UML2_Stereotype.__init__)
    params = list(sig.parameters.keys())



def test_node_is_not_abstract():
    assert not inspect.isabstract(Node)


def test_node_constructor_exists():
    assert callable(Node.__init__)


def test_node_constructor_args():
    sig = inspect.signature(Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_executionenvironment_is_not_abstract():
    assert not inspect.isabstract(UML2_ExecutionEnvironment)


def test_uml2_executionenvironment_constructor_exists():
    assert callable(UML2_ExecutionEnvironment.__init__)


def test_uml2_executionenvironment_constructor_args():
    sig = inspect.signature(UML2_ExecutionEnvironment.__init__)
    params = list(sig.parameters.keys())



def test_uml2_device_is_not_abstract():
    assert not inspect.isabstract(UML2_Device)


def test_uml2_device_constructor_exists():
    assert callable(UML2_Device.__init__)


def test_uml2_device_constructor_args():
    sig = inspect.signature(UML2_Device.__init__)
    params = list(sig.parameters.keys())



def test_pin_is_not_abstract():
    assert not inspect.isabstract(Pin)


def test_pin_constructor_exists():
    assert callable(Pin.__init__)


def test_pin_constructor_args():
    sig = inspect.signature(Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_inputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_InputPin)


def test_uml2_inputpin_constructor_exists():
    assert callable(UML2_InputPin.__init__)


def test_uml2_inputpin_constructor_args():
    sig = inspect.signature(UML2_InputPin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_outputpin_is_not_abstract():
    assert not inspect.isabstract(UML2_OutputPin)


def test_uml2_outputpin_constructor_exists():
    assert callable(UML2_OutputPin.__init__)


def test_uml2_outputpin_constructor_args():
    sig = inspect.signature(UML2_OutputPin.__init__)
    params = list(sig.parameters.keys())



def test_artifact_is_not_abstract():
    assert not inspect.isabstract(Artifact)


def test_artifact_constructor_exists():
    assert callable(Artifact.__init__)


def test_artifact_constructor_args():
    sig = inspect.signature(Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_deploymentspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_DeploymentSpecification)


def test_uml2_deploymentspecification_constructor_exists():
    assert callable(UML2_DeploymentSpecification.__init__)


def test_uml2_deploymentspecification_constructor_args():
    sig = inspect.signature(UML2_DeploymentSpecification.__init__)
    params = list(sig.parameters.keys())



def test_valuespecification_is_not_abstract():
    assert not inspect.isabstract(ValueSpecification)


def test_valuespecification_constructor_exists():
    assert callable(ValueSpecification.__init__)


def test_valuespecification_constructor_args():
    sig = inspect.signature(ValueSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_literalspecification_is_not_abstract():
    assert not inspect.isabstract(UML2_LiteralSpecification)


def test_uml2_literalspecification_constructor_exists():
    assert callable(UML2_LiteralSpecification.__init__)


def test_uml2_literalspecification_constructor_args():
    sig = inspect.signature(UML2_LiteralSpecification.__init__)
    params = list(sig.parameters.keys())



def test_uml2_opaqueexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_OpaqueExpression)


def test_uml2_opaqueexpression_constructor_exists():
    assert callable(UML2_OpaqueExpression.__init__)


def test_uml2_opaqueexpression_constructor_args():
    sig = inspect.signature(UML2_OpaqueExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interval_is_not_abstract():
    assert not inspect.isabstract(UML2_Interval)


def test_uml2_interval_constructor_exists():
    assert callable(UML2_Interval.__init__)


def test_uml2_interval_constructor_args():
    sig = inspect.signature(UML2_Interval.__init__)
    params = list(sig.parameters.keys())



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_primitivetype_is_not_abstract():
    assert not inspect.isabstract(UML2_PrimitiveType)


def test_uml2_primitivetype_constructor_exists():
    assert callable(UML2_PrimitiveType.__init__)


def test_uml2_primitivetype_constructor_args():
    sig = inspect.signature(UML2_PrimitiveType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_enumeration_is_not_abstract():
    assert not inspect.isabstract(UML2_Enumeration)


def test_uml2_enumeration_constructor_exists():
    assert callable(UML2_Enumeration.__init__)


def test_uml2_enumeration_constructor_args():
    sig = inspect.signature(UML2_Enumeration.__init__)
    params = list(sig.parameters.keys())



def test_classifier_is_not_abstract():
    assert not inspect.isabstract(Classifier)


def test_classifier_constructor_exists():
    assert callable(Classifier.__init__)


def test_classifier_constructor_args():
    sig = inspect.signature(Classifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_association_is_not_abstract():
    assert not inspect.isabstract(UML2_Association)


def test_uml2_association_constructor_exists():
    assert callable(UML2_Association.__init__)


def test_uml2_association_constructor_args():
    sig = inspect.signature(UML2_Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_interface_is_not_abstract():
    assert not inspect.isabstract(UML2_Interface)


def test_uml2_interface_constructor_exists():
    assert callable(UML2_Interface.__init__)


def test_uml2_interface_constructor_args():
    sig = inspect.signature(UML2_Interface.__init__)
    params = list(sig.parameters.keys())



def test_uml2_actor_is_not_abstract():
    assert not inspect.isabstract(UML2_Actor)


def test_uml2_actor_constructor_exists():
    assert callable(UML2_Actor.__init__)


def test_uml2_actor_constructor_args():
    sig = inspect.signature(UML2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_uml2_artifact_is_not_abstract():
    assert not inspect.isabstract(UML2_Artifact)


def test_uml2_artifact_constructor_exists():
    assert callable(UML2_Artifact.__init__)


def test_uml2_artifact_constructor_args():
    sig = inspect.signature(UML2_Artifact.__init__)
    params = list(sig.parameters.keys())



def test_uml2_informationitem_is_not_abstract():
    assert not inspect.isabstract(UML2_InformationItem)


def test_uml2_informationitem_constructor_exists():
    assert callable(UML2_InformationItem.__init__)


def test_uml2_informationitem_constructor_args():
    sig = inspect.signature(UML2_InformationItem.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameterableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_ParameterableClassifier)


def test_uml2_parameterableclassifier_constructor_exists():
    assert callable(UML2_ParameterableClassifier.__init__)


def test_uml2_parameterableclassifier_constructor_args():
    sig = inspect.signature(UML2_ParameterableClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_datatype_is_not_abstract():
    assert not inspect.isabstract(UML2_DataType)


def test_uml2_datatype_constructor_exists():
    assert callable(UML2_DataType.__init__)


def test_uml2_datatype_constructor_args():
    sig = inspect.signature(UML2_DataType.__init__)
    params = list(sig.parameters.keys())



def test_uml2_type_is_not_abstract():
    assert not inspect.isabstract(UML2_Type)


def test_uml2_type_constructor_exists():
    assert callable(UML2_Type.__init__)


def test_uml2_type_constructor_args():
    sig = inspect.signature(UML2_Type.__init__)
    params = list(sig.parameters.keys())



def test_uml2_typedelement_is_not_abstract():
    assert not inspect.isabstract(UML2_TypedElement)


def test_uml2_typedelement_constructor_exists():
    assert callable(UML2_TypedElement.__init__)


def test_uml2_typedelement_constructor_args():
    sig = inspect.signature(UML2_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_association_is_not_abstract():
    assert not inspect.isabstract(Association)


def test_association_constructor_exists():
    assert callable(Association.__init__)


def test_association_constructor_args():
    sig = inspect.signature(Association.__init__)
    params = list(sig.parameters.keys())



def test_uml2_associationclass_is_not_abstract():
    assert not inspect.isabstract(UML2_AssociationClass)


def test_uml2_associationclass_constructor_exists():
    assert callable(UML2_AssociationClass.__init__)


def test_uml2_associationclass_constructor_args():
    sig = inspect.signature(UML2_AssociationClass.__init__)
    params = list(sig.parameters.keys())



def test_uml2_extension_is_not_abstract():
    assert not inspect.isabstract(UML2_Extension)


def test_uml2_extension_constructor_exists():
    assert callable(UML2_Extension.__init__)


def test_uml2_extension_constructor_args():
    sig = inspect.signature(UML2_Extension.__init__)
    params = list(sig.parameters.keys())



def test_uml2_communicationpath_is_not_abstract():
    assert not inspect.isabstract(UML2_CommunicationPath)


def test_uml2_communicationpath_constructor_exists():
    assert callable(UML2_CommunicationPath.__init__)


def test_uml2_communicationpath_constructor_args():
    sig = inspect.signature(UML2_CommunicationPath.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeexpression_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeExpression)


def test_uml2_timeexpression_constructor_exists():
    assert callable(UML2_TimeExpression.__init__)


def test_uml2_timeexpression_constructor_args():
    sig = inspect.signature(UML2_TimeExpression.__init__)
    params = list(sig.parameters.keys())



def test_uml2_pin_is_not_abstract():
    assert not inspect.isabstract(UML2_Pin)


def test_uml2_pin_constructor_exists():
    assert callable(UML2_Pin.__init__)


def test_uml2_pin_constructor_args():
    sig = inspect.signature(UML2_Pin.__init__)
    params = list(sig.parameters.keys())



def test_uml2_duration_is_not_abstract():
    assert not inspect.isabstract(UML2_Duration)


def test_uml2_duration_constructor_exists():
    assert callable(UML2_Duration.__init__)


def test_uml2_duration_constructor_args():
    sig = inspect.signature(UML2_Duration.__init__)
    params = list(sig.parameters.keys())



def test_uml2_behavioredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_BehavioredClassifier)


def test_uml2_behavioredclassifier_constructor_exists():
    assert callable(UML2_BehavioredClassifier.__init__)


def test_uml2_behavioredclassifier_constructor_args():
    sig = inspect.signature(UML2_BehavioredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_activity_is_not_abstract():
    assert not inspect.isabstract(UML2_Activity)


def test_uml2_activity_constructor_exists():
    assert callable(UML2_Activity.__init__)


def test_uml2_activity_constructor_args():
    sig = inspect.signature(UML2_Activity.__init__)
    params = list(sig.parameters.keys())



def test_uml2_signal_is_not_abstract():
    assert not inspect.isabstract(UML2_Signal)


def test_uml2_signal_constructor_exists():
    assert callable(UML2_Signal.__init__)


def test_uml2_signal_constructor_args():
    sig = inspect.signature(UML2_Signal.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuralFeature)


def test_uml2_structuralfeature_constructor_exists():
    assert callable(UML2_StructuralFeature.__init__)


def test_uml2_structuralfeature_constructor_args():
    sig = inspect.signature(UML2_StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_usecase_is_not_abstract():
    assert not inspect.isabstract(UML2_UseCase)


def test_uml2_usecase_constructor_exists():
    assert callable(UML2_UseCase.__init__)


def test_uml2_usecase_constructor_args():
    sig = inspect.signature(UML2_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_uml2_variable_is_not_abstract():
    assert not inspect.isabstract(UML2_Variable)


def test_uml2_variable_constructor_exists():
    assert callable(UML2_Variable.__init__)


def test_uml2_variable_constructor_args():
    sig = inspect.signature(UML2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_uml2_testidentityaction_is_not_abstract():
    assert not inspect.isabstract(UML2_TestIdentityAction)


def test_uml2_testidentityaction_constructor_exists():
    assert callable(UML2_TestIdentityAction.__init__)


def test_uml2_testidentityaction_constructor_args():
    sig = inspect.signature(UML2_TestIdentityAction.__init__)
    params = list(sig.parameters.keys())



def test_uml2_statemachine_is_not_abstract():
    assert not inspect.isabstract(UML2_StateMachine)


def test_uml2_statemachine_constructor_exists():
    assert callable(UML2_StateMachine.__init__)


def test_uml2_statemachine_constructor_args():
    sig = inspect.signature(UML2_StateMachine.__init__)
    params = list(sig.parameters.keys())



def test_uml2_instancevalue_is_not_abstract():
    assert not inspect.isabstract(UML2_InstanceValue)


def test_uml2_instancevalue_constructor_exists():
    assert callable(UML2_InstanceValue.__init__)


def test_uml2_instancevalue_constructor_args():
    sig = inspect.signature(UML2_InstanceValue.__init__)
    params = list(sig.parameters.keys())



def test_uml2_node_is_not_abstract():
    assert not inspect.isabstract(UML2_Node)


def test_uml2_node_constructor_exists():
    assert callable(UML2_Node.__init__)


def test_uml2_node_constructor_args():
    sig = inspect.signature(UML2_Node.__init__)
    params = list(sig.parameters.keys())



def test_uml2_parameter_is_not_abstract():
    assert not inspect.isabstract(UML2_Parameter)


def test_uml2_parameter_constructor_exists():
    assert callable(UML2_Parameter.__init__)


def test_uml2_parameter_constructor_args():
    sig = inspect.signature(UML2_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_structuralfeature_is_not_abstract():
    assert not inspect.isabstract(StructuralFeature)


def test_structuralfeature_constructor_exists():
    assert callable(StructuralFeature.__init__)


def test_structuralfeature_constructor_args():
    sig = inspect.signature(StructuralFeature.__init__)
    params = list(sig.parameters.keys())



def test_uml2_property_is_not_abstract():
    assert not inspect.isabstract(UML2_Property)


def test_uml2_property_constructor_exists():
    assert callable(UML2_Property.__init__)


def test_uml2_property_constructor_args():
    sig = inspect.signature(UML2_Property.__init__)
    params = list(sig.parameters.keys())



def test_interval_is_not_abstract():
    assert not inspect.isabstract(Interval)


def test_interval_constructor_exists():
    assert callable(Interval.__init__)


def test_interval_constructor_args():
    sig = inspect.signature(Interval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_durationinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_DurationInterval)


def test_uml2_durationinterval_constructor_exists():
    assert callable(UML2_DurationInterval.__init__)


def test_uml2_durationinterval_constructor_args():
    sig = inspect.signature(UML2_DurationInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_timeinterval_is_not_abstract():
    assert not inspect.isabstract(UML2_TimeInterval)


def test_uml2_timeinterval_constructor_exists():
    assert callable(UML2_TimeInterval.__init__)


def test_uml2_timeinterval_constructor_args():
    sig = inspect.signature(UML2_TimeInterval.__init__)
    params = list(sig.parameters.keys())



def test_uml2_structuredclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_StructuredClassifier)


def test_uml2_structuredclassifier_constructor_exists():
    assert callable(UML2_StructuredClassifier.__init__)


def test_uml2_structuredclassifier_constructor_args():
    sig = inspect.signature(UML2_StructuredClassifier.__init__)
    params = list(sig.parameters.keys())



def test_uml2_templateableclassifier_is_not_abstract():
    assert not inspect.isabstract(UML2_TemplateableClassifier)


def test_uml2_templateableclassifier_constructor_exists():
    assert callable(UML2_TemplateableClassifier.__init__)


def test_uml2_templateableclassifier_constructor_args():
    sig = inspect.signature(UML2_TemplateableClassifier.__init__)
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
ObjectNode_strategy = st.builds(
    ObjectNode,
)
UML2_ActivityParameterNode_strategy = st.builds(
    UML2_ActivityParameterNode,
)
StructuredClassifier_strategy = st.builds(
    StructuredClassifier,
)
UML2_EncapsulatedClassifier_strategy = st.builds(
    UML2_EncapsulatedClassifier,
)
EncapsulatedClassifier_strategy = st.builds(
    EncapsulatedClassifier,
)
BehavioredClassifier_strategy = st.builds(
    BehavioredClassifier,
)
UML2_Collaboration_strategy = st.builds(
    UML2_Collaboration,
)
UML2_Class_strategy = st.builds(
    UML2_Class,
)
Behavior_strategy = st.builds(
    Behavior,
)
UML2_Interaction_strategy = st.builds(
    UML2_Interaction,
)
Type_strategy = st.builds(
    Type,
)
UML2_Classifier_strategy = st.builds(
    UML2_Classifier,
)
Property_strategy = st.builds(
    Property,
)
UML2_ExtensionEnd_strategy = st.builds(
    UML2_ExtensionEnd,
)
LiteralSpecification_strategy = st.builds(
    LiteralSpecification,
)
UML2_LiteralUnlimitedNatural_strategy = st.builds(
    UML2_LiteralUnlimitedNatural,
)
UML2_LiteralNull_strategy = st.builds(
    UML2_LiteralNull,
)
UML2_LiteralInteger_strategy = st.builds(
    UML2_LiteralInteger,
)
UML2_LiteralBoolean_strategy = st.builds(
    UML2_LiteralBoolean,
)
UML2_LiteralString_strategy = st.builds(
    UML2_LiteralString,
)
UML2_CentralBufferNode_strategy = st.builds(
    UML2_CentralBufferNode,
)
UML2_Port_strategy = st.builds(
    UML2_Port,
)
StateMachine_strategy = st.builds(
    StateMachine,
)
UML2_ProtocolStateMachine_strategy = st.builds(
    UML2_ProtocolStateMachine,
)
UML2_ExpansionNode_strategy = st.builds(
    UML2_ExpansionNode,
)
CentralBufferNode_strategy = st.builds(
    CentralBufferNode,
)
UML2_DataStoreNode_strategy = st.builds(
    UML2_DataStoreNode,
)
OpaqueExpression_strategy = st.builds(
    OpaqueExpression,
)
UML2_Expression_strategy = st.builds(
    UML2_Expression,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
UML2_ObjectNode_strategy = st.builds(
    UML2_ObjectNode,
)
UML2_ValueSpecification_strategy = st.builds(
    UML2_ValueSpecification,
)
UML2_Operation_strategy = st.builds(
    UML2_Operation,
)
InputPin_strategy = st.builds(
    InputPin,
)
UML2_ValuePin_strategy = st.builds(
    UML2_ValuePin,
)
Class_strategy = st.builds(
    Class,
)
UML2_Component_strategy = st.builds(
    UML2_Component,
)
UML2_Behavior_strategy = st.builds(
    UML2_Behavior,
)
UML2_Stereotype_strategy = st.builds(
    UML2_Stereotype,
)
Node_strategy = st.builds(
    Node,
)
UML2_ExecutionEnvironment_strategy = st.builds(
    UML2_ExecutionEnvironment,
)
UML2_Device_strategy = st.builds(
    UML2_Device,
)
Pin_strategy = st.builds(
    Pin,
)
UML2_InputPin_strategy = st.builds(
    UML2_InputPin,
)
UML2_OutputPin_strategy = st.builds(
    UML2_OutputPin,
)
Artifact_strategy = st.builds(
    Artifact,
)
UML2_DeploymentSpecification_strategy = st.builds(
    UML2_DeploymentSpecification,
)
ValueSpecification_strategy = st.builds(
    ValueSpecification,
)
UML2_LiteralSpecification_strategy = st.builds(
    UML2_LiteralSpecification,
)
UML2_OpaqueExpression_strategy = st.builds(
    UML2_OpaqueExpression,
)
UML2_Interval_strategy = st.builds(
    UML2_Interval,
)
DataType_strategy = st.builds(
    DataType,
)
UML2_PrimitiveType_strategy = st.builds(
    UML2_PrimitiveType,
)
UML2_Enumeration_strategy = st.builds(
    UML2_Enumeration,
)
Classifier_strategy = st.builds(
    Classifier,
)
UML2_Association_strategy = st.builds(
    UML2_Association,
)
UML2_Interface_strategy = st.builds(
    UML2_Interface,
)
UML2_Actor_strategy = st.builds(
    UML2_Actor,
)
UML2_Artifact_strategy = st.builds(
    UML2_Artifact,
)
UML2_InformationItem_strategy = st.builds(
    UML2_InformationItem,
)
UML2_ParameterableClassifier_strategy = st.builds(
    UML2_ParameterableClassifier,
)
UML2_DataType_strategy = st.builds(
    UML2_DataType,
)
UML2_Type_strategy = st.builds(
    UML2_Type,
)
UML2_TypedElement_strategy = st.builds(
    UML2_TypedElement,
)
Association_strategy = st.builds(
    Association,
)
UML2_AssociationClass_strategy = st.builds(
    UML2_AssociationClass,
)
UML2_Extension_strategy = st.builds(
    UML2_Extension,
)
UML2_CommunicationPath_strategy = st.builds(
    UML2_CommunicationPath,
)
UML2_TimeExpression_strategy = st.builds(
    UML2_TimeExpression,
)
UML2_Pin_strategy = st.builds(
    UML2_Pin,
)
UML2_Duration_strategy = st.builds(
    UML2_Duration,
)
UML2_BehavioredClassifier_strategy = st.builds(
    UML2_BehavioredClassifier,
)
UML2_Activity_strategy = st.builds(
    UML2_Activity,
)
UML2_Signal_strategy = st.builds(
    UML2_Signal,
)
UML2_StructuralFeature_strategy = st.builds(
    UML2_StructuralFeature,
)
UML2_UseCase_strategy = st.builds(
    UML2_UseCase,
)
UML2_Variable_strategy = st.builds(
    UML2_Variable,
)
UML2_TestIdentityAction_strategy = st.builds(
    UML2_TestIdentityAction,
)
UML2_StateMachine_strategy = st.builds(
    UML2_StateMachine,
)
UML2_InstanceValue_strategy = st.builds(
    UML2_InstanceValue,
)
UML2_Node_strategy = st.builds(
    UML2_Node,
)
UML2_Parameter_strategy = st.builds(
    UML2_Parameter,
)
StructuralFeature_strategy = st.builds(
    StructuralFeature,
)
UML2_Property_strategy = st.builds(
    UML2_Property,
)
Interval_strategy = st.builds(
    Interval,
)
UML2_DurationInterval_strategy = st.builds(
    UML2_DurationInterval,
)
UML2_TimeInterval_strategy = st.builds(
    UML2_TimeInterval,
)
UML2_StructuredClassifier_strategy = st.builds(
    UML2_StructuredClassifier,
)
UML2_TemplateableClassifier_strategy = st.builds(
    UML2_TemplateableClassifier,
)

@given(instance=ObjectNode_strategy)
@settings(max_examples=50)
def test_objectnode_instantiation(instance):
    assert isinstance(instance, ObjectNode)

@given(instance=UML2_ActivityParameterNode_strategy)
@settings(max_examples=50)
def test_uml2_activityparameternode_instantiation(instance):
    assert isinstance(instance, UML2_ActivityParameterNode)

@given(instance=StructuredClassifier_strategy)
@settings(max_examples=50)
def test_structuredclassifier_instantiation(instance):
    assert isinstance(instance, StructuredClassifier)

@given(instance=UML2_EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_uml2_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, UML2_EncapsulatedClassifier)

@given(instance=EncapsulatedClassifier_strategy)
@settings(max_examples=50)
def test_encapsulatedclassifier_instantiation(instance):
    assert isinstance(instance, EncapsulatedClassifier)

@given(instance=BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, BehavioredClassifier)

@given(instance=UML2_Collaboration_strategy)
@settings(max_examples=50)
def test_uml2_collaboration_instantiation(instance):
    assert isinstance(instance, UML2_Collaboration)

@given(instance=UML2_Class_strategy)
@settings(max_examples=50)
def test_uml2_class_instantiation(instance):
    assert isinstance(instance, UML2_Class)

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=UML2_Interaction_strategy)
@settings(max_examples=50)
def test_uml2_interaction_instantiation(instance):
    assert isinstance(instance, UML2_Interaction)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=UML2_Classifier_strategy)
@settings(max_examples=50)
def test_uml2_classifier_instantiation(instance):
    assert isinstance(instance, UML2_Classifier)

@given(instance=Property_strategy)
@settings(max_examples=50)
def test_property_instantiation(instance):
    assert isinstance(instance, Property)

@given(instance=UML2_ExtensionEnd_strategy)
@settings(max_examples=50)
def test_uml2_extensionend_instantiation(instance):
    assert isinstance(instance, UML2_ExtensionEnd)

@given(instance=LiteralSpecification_strategy)
@settings(max_examples=50)
def test_literalspecification_instantiation(instance):
    assert isinstance(instance, LiteralSpecification)

@given(instance=UML2_LiteralUnlimitedNatural_strategy)
@settings(max_examples=50)
def test_uml2_literalunlimitednatural_instantiation(instance):
    assert isinstance(instance, UML2_LiteralUnlimitedNatural)

@given(instance=UML2_LiteralNull_strategy)
@settings(max_examples=50)
def test_uml2_literalnull_instantiation(instance):
    assert isinstance(instance, UML2_LiteralNull)

@given(instance=UML2_LiteralInteger_strategy)
@settings(max_examples=50)
def test_uml2_literalinteger_instantiation(instance):
    assert isinstance(instance, UML2_LiteralInteger)

@given(instance=UML2_LiteralBoolean_strategy)
@settings(max_examples=50)
def test_uml2_literalboolean_instantiation(instance):
    assert isinstance(instance, UML2_LiteralBoolean)

@given(instance=UML2_LiteralString_strategy)
@settings(max_examples=50)
def test_uml2_literalstring_instantiation(instance):
    assert isinstance(instance, UML2_LiteralString)

@given(instance=UML2_CentralBufferNode_strategy)
@settings(max_examples=50)
def test_uml2_centralbuffernode_instantiation(instance):
    assert isinstance(instance, UML2_CentralBufferNode)

@given(instance=UML2_Port_strategy)
@settings(max_examples=50)
def test_uml2_port_instantiation(instance):
    assert isinstance(instance, UML2_Port)

@given(instance=StateMachine_strategy)
@settings(max_examples=50)
def test_statemachine_instantiation(instance):
    assert isinstance(instance, StateMachine)

@given(instance=UML2_ProtocolStateMachine_strategy)
@settings(max_examples=50)
def test_uml2_protocolstatemachine_instantiation(instance):
    assert isinstance(instance, UML2_ProtocolStateMachine)

@given(instance=UML2_ExpansionNode_strategy)
@settings(max_examples=50)
def test_uml2_expansionnode_instantiation(instance):
    assert isinstance(instance, UML2_ExpansionNode)

@given(instance=CentralBufferNode_strategy)
@settings(max_examples=50)
def test_centralbuffernode_instantiation(instance):
    assert isinstance(instance, CentralBufferNode)

@given(instance=UML2_DataStoreNode_strategy)
@settings(max_examples=50)
def test_uml2_datastorenode_instantiation(instance):
    assert isinstance(instance, UML2_DataStoreNode)

@given(instance=OpaqueExpression_strategy)
@settings(max_examples=50)
def test_opaqueexpression_instantiation(instance):
    assert isinstance(instance, OpaqueExpression)

@given(instance=UML2_Expression_strategy)
@settings(max_examples=50)
def test_uml2_expression_instantiation(instance):
    assert isinstance(instance, UML2_Expression)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=UML2_ObjectNode_strategy)
@settings(max_examples=50)
def test_uml2_objectnode_instantiation(instance):
    assert isinstance(instance, UML2_ObjectNode)

@given(instance=UML2_ValueSpecification_strategy)
@settings(max_examples=50)
def test_uml2_valuespecification_instantiation(instance):
    assert isinstance(instance, UML2_ValueSpecification)

@given(instance=UML2_Operation_strategy)
@settings(max_examples=50)
def test_uml2_operation_instantiation(instance):
    assert isinstance(instance, UML2_Operation)

@given(instance=InputPin_strategy)
@settings(max_examples=50)
def test_inputpin_instantiation(instance):
    assert isinstance(instance, InputPin)

@given(instance=UML2_ValuePin_strategy)
@settings(max_examples=50)
def test_uml2_valuepin_instantiation(instance):
    assert isinstance(instance, UML2_ValuePin)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=UML2_Component_strategy)
@settings(max_examples=50)
def test_uml2_component_instantiation(instance):
    assert isinstance(instance, UML2_Component)

@given(instance=UML2_Behavior_strategy)
@settings(max_examples=50)
def test_uml2_behavior_instantiation(instance):
    assert isinstance(instance, UML2_Behavior)

@given(instance=UML2_Stereotype_strategy)
@settings(max_examples=50)
def test_uml2_stereotype_instantiation(instance):
    assert isinstance(instance, UML2_Stereotype)

@given(instance=Node_strategy)
@settings(max_examples=50)
def test_node_instantiation(instance):
    assert isinstance(instance, Node)

@given(instance=UML2_ExecutionEnvironment_strategy)
@settings(max_examples=50)
def test_uml2_executionenvironment_instantiation(instance):
    assert isinstance(instance, UML2_ExecutionEnvironment)

@given(instance=UML2_Device_strategy)
@settings(max_examples=50)
def test_uml2_device_instantiation(instance):
    assert isinstance(instance, UML2_Device)

@given(instance=Pin_strategy)
@settings(max_examples=50)
def test_pin_instantiation(instance):
    assert isinstance(instance, Pin)

@given(instance=UML2_InputPin_strategy)
@settings(max_examples=50)
def test_uml2_inputpin_instantiation(instance):
    assert isinstance(instance, UML2_InputPin)

@given(instance=UML2_OutputPin_strategy)
@settings(max_examples=50)
def test_uml2_outputpin_instantiation(instance):
    assert isinstance(instance, UML2_OutputPin)

@given(instance=Artifact_strategy)
@settings(max_examples=50)
def test_artifact_instantiation(instance):
    assert isinstance(instance, Artifact)

@given(instance=UML2_DeploymentSpecification_strategy)
@settings(max_examples=50)
def test_uml2_deploymentspecification_instantiation(instance):
    assert isinstance(instance, UML2_DeploymentSpecification)

@given(instance=ValueSpecification_strategy)
@settings(max_examples=50)
def test_valuespecification_instantiation(instance):
    assert isinstance(instance, ValueSpecification)

@given(instance=UML2_LiteralSpecification_strategy)
@settings(max_examples=50)
def test_uml2_literalspecification_instantiation(instance):
    assert isinstance(instance, UML2_LiteralSpecification)

@given(instance=UML2_OpaqueExpression_strategy)
@settings(max_examples=50)
def test_uml2_opaqueexpression_instantiation(instance):
    assert isinstance(instance, UML2_OpaqueExpression)

@given(instance=UML2_Interval_strategy)
@settings(max_examples=50)
def test_uml2_interval_instantiation(instance):
    assert isinstance(instance, UML2_Interval)

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=UML2_PrimitiveType_strategy)
@settings(max_examples=50)
def test_uml2_primitivetype_instantiation(instance):
    assert isinstance(instance, UML2_PrimitiveType)

@given(instance=UML2_Enumeration_strategy)
@settings(max_examples=50)
def test_uml2_enumeration_instantiation(instance):
    assert isinstance(instance, UML2_Enumeration)

@given(instance=Classifier_strategy)
@settings(max_examples=50)
def test_classifier_instantiation(instance):
    assert isinstance(instance, Classifier)

@given(instance=UML2_Association_strategy)
@settings(max_examples=50)
def test_uml2_association_instantiation(instance):
    assert isinstance(instance, UML2_Association)

@given(instance=UML2_Interface_strategy)
@settings(max_examples=50)
def test_uml2_interface_instantiation(instance):
    assert isinstance(instance, UML2_Interface)

@given(instance=UML2_Actor_strategy)
@settings(max_examples=50)
def test_uml2_actor_instantiation(instance):
    assert isinstance(instance, UML2_Actor)

@given(instance=UML2_Artifact_strategy)
@settings(max_examples=50)
def test_uml2_artifact_instantiation(instance):
    assert isinstance(instance, UML2_Artifact)

@given(instance=UML2_InformationItem_strategy)
@settings(max_examples=50)
def test_uml2_informationitem_instantiation(instance):
    assert isinstance(instance, UML2_InformationItem)

@given(instance=UML2_ParameterableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_parameterableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_ParameterableClassifier)

@given(instance=UML2_DataType_strategy)
@settings(max_examples=50)
def test_uml2_datatype_instantiation(instance):
    assert isinstance(instance, UML2_DataType)

@given(instance=UML2_Type_strategy)
@settings(max_examples=50)
def test_uml2_type_instantiation(instance):
    assert isinstance(instance, UML2_Type)

@given(instance=UML2_TypedElement_strategy)
@settings(max_examples=50)
def test_uml2_typedelement_instantiation(instance):
    assert isinstance(instance, UML2_TypedElement)

@given(instance=Association_strategy)
@settings(max_examples=50)
def test_association_instantiation(instance):
    assert isinstance(instance, Association)

@given(instance=UML2_AssociationClass_strategy)
@settings(max_examples=50)
def test_uml2_associationclass_instantiation(instance):
    assert isinstance(instance, UML2_AssociationClass)

@given(instance=UML2_Extension_strategy)
@settings(max_examples=50)
def test_uml2_extension_instantiation(instance):
    assert isinstance(instance, UML2_Extension)

@given(instance=UML2_CommunicationPath_strategy)
@settings(max_examples=50)
def test_uml2_communicationpath_instantiation(instance):
    assert isinstance(instance, UML2_CommunicationPath)

@given(instance=UML2_TimeExpression_strategy)
@settings(max_examples=50)
def test_uml2_timeexpression_instantiation(instance):
    assert isinstance(instance, UML2_TimeExpression)

@given(instance=UML2_Pin_strategy)
@settings(max_examples=50)
def test_uml2_pin_instantiation(instance):
    assert isinstance(instance, UML2_Pin)

@given(instance=UML2_Duration_strategy)
@settings(max_examples=50)
def test_uml2_duration_instantiation(instance):
    assert isinstance(instance, UML2_Duration)

@given(instance=UML2_BehavioredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_behavioredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_BehavioredClassifier)

@given(instance=UML2_Activity_strategy)
@settings(max_examples=50)
def test_uml2_activity_instantiation(instance):
    assert isinstance(instance, UML2_Activity)

@given(instance=UML2_Signal_strategy)
@settings(max_examples=50)
def test_uml2_signal_instantiation(instance):
    assert isinstance(instance, UML2_Signal)

@given(instance=UML2_StructuralFeature_strategy)
@settings(max_examples=50)
def test_uml2_structuralfeature_instantiation(instance):
    assert isinstance(instance, UML2_StructuralFeature)

@given(instance=UML2_UseCase_strategy)
@settings(max_examples=50)
def test_uml2_usecase_instantiation(instance):
    assert isinstance(instance, UML2_UseCase)

@given(instance=UML2_Variable_strategy)
@settings(max_examples=50)
def test_uml2_variable_instantiation(instance):
    assert isinstance(instance, UML2_Variable)

@given(instance=UML2_TestIdentityAction_strategy)
@settings(max_examples=50)
def test_uml2_testidentityaction_instantiation(instance):
    assert isinstance(instance, UML2_TestIdentityAction)

@given(instance=UML2_StateMachine_strategy)
@settings(max_examples=50)
def test_uml2_statemachine_instantiation(instance):
    assert isinstance(instance, UML2_StateMachine)

@given(instance=UML2_InstanceValue_strategy)
@settings(max_examples=50)
def test_uml2_instancevalue_instantiation(instance):
    assert isinstance(instance, UML2_InstanceValue)

@given(instance=UML2_Node_strategy)
@settings(max_examples=50)
def test_uml2_node_instantiation(instance):
    assert isinstance(instance, UML2_Node)

@given(instance=UML2_Parameter_strategy)
@settings(max_examples=50)
def test_uml2_parameter_instantiation(instance):
    assert isinstance(instance, UML2_Parameter)

@given(instance=StructuralFeature_strategy)
@settings(max_examples=50)
def test_structuralfeature_instantiation(instance):
    assert isinstance(instance, StructuralFeature)

@given(instance=UML2_Property_strategy)
@settings(max_examples=50)
def test_uml2_property_instantiation(instance):
    assert isinstance(instance, UML2_Property)

@given(instance=Interval_strategy)
@settings(max_examples=50)
def test_interval_instantiation(instance):
    assert isinstance(instance, Interval)

@given(instance=UML2_DurationInterval_strategy)
@settings(max_examples=50)
def test_uml2_durationinterval_instantiation(instance):
    assert isinstance(instance, UML2_DurationInterval)

@given(instance=UML2_TimeInterval_strategy)
@settings(max_examples=50)
def test_uml2_timeinterval_instantiation(instance):
    assert isinstance(instance, UML2_TimeInterval)

@given(instance=UML2_StructuredClassifier_strategy)
@settings(max_examples=50)
def test_uml2_structuredclassifier_instantiation(instance):
    assert isinstance(instance, UML2_StructuredClassifier)

@given(instance=UML2_TemplateableClassifier_strategy)
@settings(max_examples=50)
def test_uml2_templateableclassifier_instantiation(instance):
    assert isinstance(instance, UML2_TemplateableClassifier)
