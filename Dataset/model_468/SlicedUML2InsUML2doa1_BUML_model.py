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
Classifier = Class(name="Classifier")
UML2_DeploymentSpecification = Class(name="UML2::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2_DataType = Class(name="UML2::DataType")
UML2_LiteralString = Class(name="UML2::LiteralString")
LiteralSpecification = Class(name="LiteralSpecification")
UML2_Type = Class(name="UML2::Type")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
Property_ = Class(name="Property")
UML2_ObjectNode = Class(name="UML2::ObjectNode")
TypedElement = Class(name="TypedElement")
UML2_StateMachine = Class(name="UML2::StateMachine")
Behavior = Class(name="Behavior")
UML2_StructuredClassifier = Class(name="UML2::StructuredClassifier")
UML2_InstanceValue = Class(name="UML2::InstanceValue")
ValueSpecification = Class(name="ValueSpecification")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
Association = Class(name="Association")
UML2_TypedElement = Class(name="UML2::TypedElement")
UML2_InputPin = Class(name="UML2::InputPin")
Pin = Class(name="Pin")
UML2_ParameterableClassifier = Class(name="UML2::ParameterableClassifier")
UML2_Node = Class(name="UML2::Node")
Class_ = Class(name="Class")
UML2_ExpansionNode = Class(name="UML2::ExpansionNode")
ObjectNode = Class(name="ObjectNode")
UML2_ActivityParameterNode = Class(name="UML2::ActivityParameterNode")
UML2_TimeInterval = Class(name="UML2::TimeInterval")
Interval = Class(name="Interval")
UML2_Device = Class(name="UML2::Device")
Node = Class(name="Node")
UML2_Extension = Class(name="UML2::Extension")
UML2_Expression = Class(name="UML2::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2_Pin = Class(name="UML2::Pin")
UML2_Enumeration = Class(name="UML2::Enumeration")
DataType = Class(name="DataType")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_Port = Class(name="UML2::Port")
UML2_Component = Class(name="UML2::Component")
UML2_Interface = Class(name="UML2::Interface")
UML2_InformationItem = Class(name="UML2::InformationItem")
UML2_Association = Class(name="UML2::Association")
UML2_TimeExpression = Class(name="UML2::TimeExpression")
UML2_Interaction = Class(name="UML2::Interaction")
UML2_LiteralUnlimitedNatural = Class(name="UML2::LiteralUnlimitedNatural")
UML2_Parameter = Class(name="UML2::Parameter")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_Signal = Class(name="UML2::Signal")
UML2_LiteralSpecification = Class(name="UML2::LiteralSpecification")
UML2_ValueSpecification = Class(name="UML2::ValueSpecification")
UML2_PrimitiveType = Class(name="UML2::PrimitiveType")
UML2_Interval = Class(name="UML2::Interval")
UML2_Property = Class(name="UML2::Property")
StructuralFeature = Class(name="StructuralFeature")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
UML2_TemplateableClassifier = Class(name="UML2::TemplateableClassifier")
UML2_DestroyObjectAction = Class(name="UML2::DestroyObjectAction")
UML2_Operation = Class(name="UML2::Operation")
UML2_LiteralBoolean = Class(name="UML2::LiteralBoolean")
UML2_Actor = Class(name="UML2::Actor")
UML2_StructuralFeature = Class(name="UML2::StructuralFeature")
UML2_Artifact = Class(name="UML2::Artifact")
UML2_OutputPin = Class(name="UML2::OutputPin")
UML2_Duration = Class(name="UML2::Duration")
UML2_Classifier = Class(name="UML2::Classifier")
Type = Class(name="Type")
UML2_LiteralNull = Class(name="UML2::LiteralNull")
UML2_DataStoreNode = Class(name="UML2::DataStoreNode")
CentralBufferNode = Class(name="CentralBufferNode")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_Collaboration = Class(name="UML2::Collaboration")
BehavioredClassifier = Class(name="BehavioredClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
UML2_OpaqueExpression = Class(name="UML2::OpaqueExpression")
UML2_ValuePin = Class(name="UML2::ValuePin")
InputPin = Class(name="InputPin")
UML2_LiteralInteger = Class(name="UML2::LiteralInteger")
UML2_Variable = Class(name="UML2::Variable")
UML2_EncapsulatedClassifier = Class(name="UML2::EncapsulatedClassifier")
UML2_DurationInterval = Class(name="UML2::DurationInterval")
UML2_CentralBufferNode = Class(name="UML2::CentralBufferNode")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_Class = Class(name="UML2::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2_Activity = Class(name="UML2::Activity")

# Classifier class attributes and methods

# UML2_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2_DataType class attributes and methods

# UML2_LiteralString class attributes and methods

# LiteralSpecification class attributes and methods

# UML2_Type class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# Property class attributes and methods

# UML2_ObjectNode class attributes and methods

# TypedElement class attributes and methods

# UML2_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2_StructuredClassifier class attributes and methods

# UML2_InstanceValue class attributes and methods

# ValueSpecification class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# UML2_CommunicationPath class attributes and methods

# Association class attributes and methods

# UML2_TypedElement class attributes and methods

# UML2_InputPin class attributes and methods

# Pin class attributes and methods

# UML2_ParameterableClassifier class attributes and methods

# UML2_Node class attributes and methods

# Class class attributes and methods

# UML2_ExpansionNode class attributes and methods

# ObjectNode class attributes and methods

# UML2_ActivityParameterNode class attributes and methods

# UML2_TimeInterval class attributes and methods

# Interval class attributes and methods

# UML2_Device class attributes and methods

# Node class attributes and methods

# UML2_Extension class attributes and methods

# UML2_Expression class attributes and methods

# OpaqueExpression class attributes and methods

# UML2_Pin class attributes and methods

# UML2_Enumeration class attributes and methods

# DataType class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_Port class attributes and methods

# UML2_Component class attributes and methods

# UML2_Interface class attributes and methods

# UML2_InformationItem class attributes and methods

# UML2_Association class attributes and methods

# UML2_TimeExpression class attributes and methods

# UML2_Interaction class attributes and methods

# UML2_LiteralUnlimitedNatural class attributes and methods

# UML2_Parameter class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_Signal class attributes and methods

# UML2_LiteralSpecification class attributes and methods

# UML2_ValueSpecification class attributes and methods

# UML2_PrimitiveType class attributes and methods

# UML2_Interval class attributes and methods

# UML2_Property class attributes and methods

# StructuralFeature class attributes and methods

# UML2_UseCase class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# UML2_TemplateableClassifier class attributes and methods

# UML2_DestroyObjectAction class attributes and methods

# UML2_Operation class attributes and methods

# UML2_LiteralBoolean class attributes and methods

# UML2_Actor class attributes and methods

# UML2_StructuralFeature class attributes and methods

# UML2_Artifact class attributes and methods

# UML2_OutputPin class attributes and methods

# UML2_Duration class attributes and methods

# UML2_Classifier class attributes and methods

# Type class attributes and methods

# UML2_LiteralNull class attributes and methods

# UML2_DataStoreNode class attributes and methods

# CentralBufferNode class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_Collaboration class attributes and methods

# BehavioredClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# UML2_OpaqueExpression class attributes and methods

# UML2_ValuePin class attributes and methods

# InputPin class attributes and methods

# UML2_LiteralInteger class attributes and methods

# UML2_Variable class attributes and methods

# UML2_EncapsulatedClassifier class attributes and methods

# UML2_DurationInterval class attributes and methods

# UML2_CentralBufferNode class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2_Activity class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="UML2_Type", type=UML2_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_TypedElement", type=UML2_Type, multiplicity=Multiplicity(0, 1))
    }
)
target1: BinaryAssociation = BinaryAssociation(
    name="target1",
    ends={
        Property(name="UML2_InputPin", type=UML2_DestroyObjectAction, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_DestroyObjectAction", type=UML2_InputPin, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_UML2_Interface_Classifier = Generalization(general=Classifier, specific=UML2_Interface)
gen_UML2_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2_DeploymentSpecification)
gen_UML2_DataType_Classifier = Generalization(general=Classifier, specific=UML2_DataType)
gen_UML2_LiteralString_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralString)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)
gen_UML2_ObjectNode_TypedElement = Generalization(general=TypedElement, specific=UML2_ObjectNode)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_StructuredClassifier)
gen_UML2_InstanceValue_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_InstanceValue)
gen_UML2_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_BehavioredClassifier)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_InputPin_Pin = Generalization(general=Pin, specific=UML2_InputPin)
gen_UML2_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_ParameterableClassifier)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_ExpansionNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ExpansionNode)
gen_UML2_ActivityParameterNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_ActivityParameterNode)
gen_UML2_TimeInterval_Interval = Generalization(general=Interval, specific=UML2_TimeInterval)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2_Expression)
gen_UML2_Pin_ObjectNode = Generalization(general=ObjectNode, specific=UML2_Pin)
gen_UML2_Enumeration_DataType = Generalization(general=DataType, specific=UML2_Enumeration)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)
gen_UML2_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2_InformationItem)
gen_UML2_Association_Classifier = Generalization(general=Classifier, specific=UML2_Association)
gen_UML2_TimeExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_TimeExpression)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_LiteralUnlimitedNatural_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralUnlimitedNatural)
gen_UML2_Parameter_TypedElement = Generalization(general=TypedElement, specific=UML2_Parameter)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_Signal_Classifier = Generalization(general=Classifier, specific=UML2_Signal)
gen_UML2_LiteralSpecification_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_LiteralSpecification)
gen_UML2_ValueSpecification_TypedElement = Generalization(general=TypedElement, specific=UML2_ValueSpecification)
gen_UML2_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2_PrimitiveType)
gen_UML2_Interval_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Interval)
gen_UML2_Property_StructuralFeature = Generalization(general=StructuralFeature, specific=UML2_Property)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_TemplateableClassifier)
gen_UML2_Operation_TypedElement = Generalization(general=TypedElement, specific=UML2_Operation)
gen_UML2_LiteralBoolean_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralBoolean)
gen_UML2_Actor_Classifier = Generalization(general=Classifier, specific=UML2_Actor)
gen_UML2_StructuralFeature_TypedElement = Generalization(general=TypedElement, specific=UML2_StructuralFeature)
gen_UML2_Artifact_Classifier = Generalization(general=Classifier, specific=UML2_Artifact)
gen_UML2_OutputPin_Pin = Generalization(general=Pin, specific=UML2_OutputPin)
gen_UML2_Duration_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_Duration)
gen_UML2_Classifier_Type = Generalization(general=Type, specific=UML2_Classifier)
gen_UML2_LiteralNull_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralNull)
gen_UML2_DataStoreNode_CentralBufferNode = Generalization(general=CentralBufferNode, specific=UML2_DataStoreNode)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_Collaboration)
gen_UML2_OpaqueExpression_ValueSpecification = Generalization(general=ValueSpecification, specific=UML2_OpaqueExpression)
gen_UML2_ValuePin_InputPin = Generalization(general=InputPin, specific=UML2_ValuePin)
gen_UML2_LiteralInteger_LiteralSpecification = Generalization(general=LiteralSpecification, specific=UML2_LiteralInteger)
gen_UML2_Variable_TypedElement = Generalization(general=TypedElement, specific=UML2_Variable)
gen_UML2_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_EncapsulatedClassifier)
gen_UML2_DurationInterval_Interval = Generalization(general=Interval, specific=UML2_DurationInterval)
gen_UML2_CentralBufferNode_ObjectNode = Generalization(general=ObjectNode, specific=UML2_CentralBufferNode)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2_Class)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={Classifier, UML2_DeploymentSpecification, Artifact, UML2_DataType, UML2_LiteralString, LiteralSpecification, UML2_Type, UML2_ExtensionEnd, Property_, UML2_ObjectNode, TypedElement, UML2_StateMachine, Behavior, UML2_StructuredClassifier, UML2_InstanceValue, ValueSpecification, UML2_BehavioredClassifier, UML2_CommunicationPath, Association, UML2_TypedElement, UML2_InputPin, Pin, UML2_ParameterableClassifier, UML2_Node, Class_, UML2_ExpansionNode, ObjectNode, UML2_ActivityParameterNode, UML2_TimeInterval, Interval, UML2_Device, Node, UML2_Extension, UML2_Expression, OpaqueExpression, UML2_Pin, UML2_Enumeration, DataType, UML2_Stereotype, UML2_Port, UML2_Component, UML2_Interface, UML2_InformationItem, UML2_Association, UML2_TimeExpression, UML2_Interaction, UML2_LiteralUnlimitedNatural, UML2_Parameter, UML2_Behavior, UML2_Signal, UML2_LiteralSpecification, UML2_ValueSpecification, UML2_PrimitiveType, UML2_Interval, UML2_Property, StructuralFeature, UML2_UseCase, UML2_ExecutionEnvironment, UML2_TemplateableClassifier, UML2_DestroyObjectAction, UML2_Operation, UML2_LiteralBoolean, UML2_Actor, UML2_StructuralFeature, UML2_Artifact, UML2_OutputPin, UML2_Duration, UML2_Classifier, Type, UML2_LiteralNull, UML2_DataStoreNode, CentralBufferNode, UML2_AssociationClass, UML2_Collaboration, BehavioredClassifier, StructuredClassifier, UML2_OpaqueExpression, UML2_ValuePin, InputPin, UML2_LiteralInteger, UML2_Variable, UML2_EncapsulatedClassifier, UML2_DurationInterval, UML2_CentralBufferNode, UML2_ProtocolStateMachine, StateMachine, UML2_Class, EncapsulatedClassifier, UML2_Activity},
    associations={type0, target1},
    generalizations={gen_UML2_Interface_Classifier, gen_UML2_DeploymentSpecification_Artifact, gen_UML2_DataType_Classifier, gen_UML2_LiteralString_LiteralSpecification, gen_UML2_ExtensionEnd_Property, gen_UML2_ObjectNode_TypedElement, gen_UML2_StateMachine_Behavior, gen_UML2_StructuredClassifier_Classifier, gen_UML2_InstanceValue_ValueSpecification, gen_UML2_BehavioredClassifier_Classifier, gen_UML2_CommunicationPath_Association, gen_UML2_InputPin_Pin, gen_UML2_ParameterableClassifier_Classifier, gen_UML2_Node_Class, gen_UML2_ExpansionNode_ObjectNode, gen_UML2_ActivityParameterNode_ObjectNode, gen_UML2_TimeInterval_Interval, gen_UML2_Device_Node, gen_UML2_Extension_Association, gen_UML2_Expression_OpaqueExpression, gen_UML2_Pin_ObjectNode, gen_UML2_Enumeration_DataType, gen_UML2_Stereotype_Class, gen_UML2_Port_Property, gen_UML2_Component_Class, gen_UML2_InformationItem_Classifier, gen_UML2_Association_Classifier, gen_UML2_TimeExpression_ValueSpecification, gen_UML2_Interaction_Behavior, gen_UML2_LiteralUnlimitedNatural_LiteralSpecification, gen_UML2_Parameter_TypedElement, gen_UML2_Behavior_Class, gen_UML2_Signal_Classifier, gen_UML2_LiteralSpecification_ValueSpecification, gen_UML2_ValueSpecification_TypedElement, gen_UML2_PrimitiveType_DataType, gen_UML2_Interval_ValueSpecification, gen_UML2_Property_StructuralFeature, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_ExecutionEnvironment_Node, gen_UML2_TemplateableClassifier_Classifier, gen_UML2_Operation_TypedElement, gen_UML2_LiteralBoolean_LiteralSpecification, gen_UML2_Actor_Classifier, gen_UML2_StructuralFeature_TypedElement, gen_UML2_Artifact_Classifier, gen_UML2_OutputPin_Pin, gen_UML2_Duration_ValueSpecification, gen_UML2_Classifier_Type, gen_UML2_LiteralNull_LiteralSpecification, gen_UML2_DataStoreNode_CentralBufferNode, gen_UML2_AssociationClass_Class, gen_UML2_AssociationClass_Association, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_Collaboration_StructuredClassifier, gen_UML2_OpaqueExpression_ValueSpecification, gen_UML2_ValuePin_InputPin, gen_UML2_LiteralInteger_LiteralSpecification, gen_UML2_Variable_TypedElement, gen_UML2_EncapsulatedClassifier_StructuredClassifier, gen_UML2_DurationInterval_Interval, gen_UML2_CentralBufferNode_ObjectNode, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_Class_BehavioredClassifier, gen_UML2_Class_EncapsulatedClassifier, gen_UML2_Activity_Behavior},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)