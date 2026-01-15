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
UML2_Artifact = Class(name="UML2::Artifact")
Classifier = Class(name="Classifier")
UML2_Classifier = Class(name="UML2::Classifier")
UML2_Collaboration = Class(name="UML2::Collaboration")
BehavioredClassifier = Class(name="BehavioredClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_Interface = Class(name="UML2::Interface")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_StateMachine = Class(name="UML2::StateMachine")
UML2_InformationItem = Class(name="UML2::InformationItem")
UML2_DeploymentSpecification = Class(name="UML2::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2_StructuredClassifier = Class(name="UML2::StructuredClassifier")
UML2_Association = Class(name="UML2::Association")
UML2_Signal = Class(name="UML2::Signal")
UML2_TemplateableClassifier = Class(name="UML2::TemplateableClassifier")
UML2_Extension = Class(name="UML2::Extension")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier")
UML2_Device = Class(name="UML2::Device")
Node = Class(name="Node")
UML2_EncapsulatedClassifier = Class(name="UML2::EncapsulatedClassifier")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
Class_ = Class(name="Class")
Association = Class(name="Association")
UML2_Activity = Class(name="UML2::Activity")
Behavior = Class(name="Behavior")
UML2_Interaction = Class(name="UML2::Interaction")
UML2_CommunicationPath = Class(name="UML2::CommunicationPath")
UML2_Class = Class(name="UML2::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2_Node = Class(name="UML2::Node")
UML2_DataType = Class(name="UML2::DataType")
UML2_Component = Class(name="UML2::Component")
UML2_ParameterableClassifier = Class(name="UML2::ParameterableClassifier")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_Actor = Class(name="UML2::Actor")
UML2_PrimitiveType = Class(name="UML2::PrimitiveType")
DataType = Class(name="DataType")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_Enumeration = Class(name="UML2::Enumeration")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")

# UML2_Artifact class attributes and methods

# Classifier class attributes and methods

# UML2_Classifier class attributes and methods
UML2_Classifier_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
UML2_Classifier.attributes={UML2_Classifier_isAbstract}

# UML2_Collaboration class attributes and methods

# BehavioredClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_Interface class attributes and methods

# UML2_UseCase class attributes and methods

# UML2_StateMachine class attributes and methods

# UML2_InformationItem class attributes and methods

# UML2_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2_StructuredClassifier class attributes and methods

# UML2_Association class attributes and methods

# UML2_Signal class attributes and methods

# UML2_TemplateableClassifier class attributes and methods

# UML2_Extension class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# UML2_Device class attributes and methods

# Node class attributes and methods

# UML2_EncapsulatedClassifier class attributes and methods

# UML2_AssociationClass class attributes and methods

# Class class attributes and methods

# Association class attributes and methods

# UML2_Activity class attributes and methods

# Behavior class attributes and methods

# UML2_Interaction class attributes and methods

# UML2_CommunicationPath class attributes and methods

# UML2_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2_Node class attributes and methods

# UML2_DataType class attributes and methods

# UML2_Component class attributes and methods

# UML2_ParameterableClassifier class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_Actor class attributes and methods

# UML2_PrimitiveType class attributes and methods

# DataType class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_Enumeration class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# Generalizations
gen_UML2_Artifact_Classifier = Generalization(general=Classifier, specific=UML2_Artifact)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_Collaboration)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_Interface_Classifier = Generalization(general=Classifier, specific=UML2_Interface)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2_InformationItem)
gen_UML2_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2_DeploymentSpecification)
gen_UML2_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_StructuredClassifier)
gen_UML2_Association_Classifier = Generalization(general=Classifier, specific=UML2_Association)
gen_UML2_Signal_Classifier = Generalization(general=Classifier, specific=UML2_Signal)
gen_UML2_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_TemplateableClassifier)
gen_UML2_Extension_Association = Generalization(general=Association, specific=UML2_Extension)
gen_UML2_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2_BehavioredClassifier)
gen_UML2_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2_EncapsulatedClassifier)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_AssociationClass_Association = Generalization(general=Association, specific=UML2_AssociationClass)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_CommunicationPath_Association = Generalization(general=Association, specific=UML2_CommunicationPath)
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2_Class)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_DataType_Classifier = Generalization(general=Classifier, specific=UML2_DataType)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)
gen_UML2_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2_ParameterableClassifier)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_Actor_Classifier = Generalization(general=Classifier, specific=UML2_Actor)
gen_UML2_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2_PrimitiveType)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_Enumeration_DataType = Generalization(general=DataType, specific=UML2_Enumeration)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_Artifact, Classifier, UML2_Classifier, UML2_Collaboration, BehavioredClassifier, StructuredClassifier, UML2_Behavior, UML2_Interface, UML2_UseCase, UML2_StateMachine, UML2_InformationItem, UML2_DeploymentSpecification, Artifact, UML2_StructuredClassifier, UML2_Association, UML2_Signal, UML2_TemplateableClassifier, UML2_Extension, UML2_BehavioredClassifier, UML2_Device, Node, UML2_EncapsulatedClassifier, UML2_AssociationClass, Class_, Association, UML2_Activity, Behavior, UML2_Interaction, UML2_CommunicationPath, UML2_Class, EncapsulatedClassifier, UML2_Node, UML2_DataType, UML2_Component, UML2_ParameterableClassifier, UML2_ProtocolStateMachine, StateMachine, UML2_Actor, UML2_PrimitiveType, DataType, UML2_Stereotype, UML2_Enumeration, UML2_ExecutionEnvironment},
    associations={},
    generalizations={gen_UML2_Artifact_Classifier, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_Collaboration_StructuredClassifier, gen_UML2_Behavior_Class, gen_UML2_Interface_Classifier, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_StateMachine_Behavior, gen_UML2_InformationItem_Classifier, gen_UML2_DeploymentSpecification_Artifact, gen_UML2_StructuredClassifier_Classifier, gen_UML2_Association_Classifier, gen_UML2_Signal_Classifier, gen_UML2_TemplateableClassifier_Classifier, gen_UML2_Extension_Association, gen_UML2_BehavioredClassifier_Classifier, gen_UML2_EncapsulatedClassifier_StructuredClassifier, gen_UML2_AssociationClass_Class, gen_UML2_AssociationClass_Association, gen_UML2_Activity_Behavior, gen_UML2_Interaction_Behavior, gen_UML2_Device_Node, gen_UML2_CommunicationPath_Association, gen_UML2_Class_BehavioredClassifier, gen_UML2_Class_EncapsulatedClassifier, gen_UML2_Node_Class, gen_UML2_DataType_Classifier, gen_UML2_Component_Class, gen_UML2_ParameterableClassifier_Classifier, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_Actor_Classifier, gen_UML2_PrimitiveType_DataType, gen_UML2_Stereotype_Class, gen_UML2_Enumeration_DataType, gen_UML2_ExecutionEnvironment_Node},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)