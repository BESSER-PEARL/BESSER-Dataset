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
UML2WithID_Property = Class(name="UML2WithID::Property")
Element = Class(name="Element")
UML2WithID_CommunicationPath = Class(name="UML2WithID::CommunicationPath")
Association = Class(name="Association")
UML2WithID_StructuredClassifier = Class(name="UML2WithID::StructuredClassifier", is_abstract=True)
Classifier = Class(name="Classifier")
UML2WithID_ParameterableClassifier = Class(name="UML2WithID::ParameterableClassifier", is_abstract=True)
UML2WithID_Interaction = Class(name="UML2WithID::Interaction")
Behavior = Class(name="Behavior")
UML2WithID_AssociationClass = Class(name="UML2WithID::AssociationClass")
UML2WithID_BehavioredClassifier = Class(name="UML2WithID::BehavioredClassifier", is_abstract=True)
UML2WithID_Artifact = Class(name="UML2WithID::Artifact")
UML2WithID_Port = Class(name="UML2WithID::Port")
Property_ = Class(name="Property")
UML2WithID_Behavior = Class(name="UML2WithID::Behavior", is_abstract=True)
UML2WithID_Device = Class(name="UML2WithID::Device")
Node = Class(name="Node")
UML2WithID_TemplateableClassifier = Class(name="UML2WithID::TemplateableClassifier", is_abstract=True)
UML2WithID_Generalization = Class(name="UML2WithID::Generalization")
UML2WithID_Classifier = Class(name="UML2WithID::Classifier", is_abstract=True)
UML2WithID_PrimitiveType = Class(name="UML2WithID::PrimitiveType")
DataType = Class(name="DataType")
UML2WithID_ProtocolStateMachine = Class(name="UML2WithID::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2WithID_DeploymentSpecification = Class(name="UML2WithID::DeploymentSpecification")
Artifact = Class(name="Artifact")
UML2WithID_Interface = Class(name="UML2WithID::Interface")
UML2WithID_Component = Class(name="UML2WithID::Component")
Class_ = Class(name="Class")
UML2WithID_Extension = Class(name="UML2WithID::Extension")
UML2WithID_Stereotype = Class(name="UML2WithID::Stereotype")
UML2WithID_Activity = Class(name="UML2WithID::Activity")
UML2WithID_InformationItem = Class(name="UML2WithID::InformationItem")
UML2WithID_Node = Class(name="UML2WithID::Node")
UML2WithID_Association = Class(name="UML2WithID::Association")
UML2WithID_Actor = Class(name="UML2WithID::Actor")
UML2WithID_ExecutionEnvironment = Class(name="UML2WithID::ExecutionEnvironment")
UML2WithID_Class = Class(name="UML2WithID::Class")
EncapsulatedClassifier = Class(name="EncapsulatedClassifier")
UML2WithID_StateMachine = Class(name="UML2WithID::StateMachine")
UML2WithID_Signal = Class(name="UML2WithID::Signal")
UML2WithID_UseCase = Class(name="UML2WithID::UseCase")
UML2WithID_Collaboration = Class(name="UML2WithID::Collaboration")
BehavioredClassifier = Class(name="BehavioredClassifier")
StructuredClassifier = Class(name="StructuredClassifier")
UML2WithID_EncapsulatedClassifier = Class(name="UML2WithID::EncapsulatedClassifier", is_abstract=True)
UML2WithID_DataType = Class(name="UML2WithID::DataType")
UML2WithID_ExtensionEnd = Class(name="UML2WithID::ExtensionEnd")
UML2WithID_Enumeration = Class(name="UML2WithID::Enumeration")
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)

# UML2WithID_Property class attributes and methods

# Element class attributes and methods

# UML2WithID_CommunicationPath class attributes and methods

# Association class attributes and methods

# UML2WithID_StructuredClassifier class attributes and methods

# Classifier class attributes and methods

# UML2WithID_ParameterableClassifier class attributes and methods

# UML2WithID_Interaction class attributes and methods

# Behavior class attributes and methods

# UML2WithID_AssociationClass class attributes and methods

# UML2WithID_BehavioredClassifier class attributes and methods

# UML2WithID_Artifact class attributes and methods

# UML2WithID_Port class attributes and methods

# Property class attributes and methods

# UML2WithID_Behavior class attributes and methods

# UML2WithID_Device class attributes and methods

# Node class attributes and methods

# UML2WithID_TemplateableClassifier class attributes and methods

# UML2WithID_Generalization class attributes and methods

# UML2WithID_Classifier class attributes and methods

# UML2WithID_PrimitiveType class attributes and methods

# DataType class attributes and methods

# UML2WithID_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2WithID_DeploymentSpecification class attributes and methods

# Artifact class attributes and methods

# UML2WithID_Interface class attributes and methods

# UML2WithID_Component class attributes and methods

# Class class attributes and methods

# UML2WithID_Extension class attributes and methods

# UML2WithID_Stereotype class attributes and methods

# UML2WithID_Activity class attributes and methods

# UML2WithID_InformationItem class attributes and methods

# UML2WithID_Node class attributes and methods

# UML2WithID_Association class attributes and methods

# UML2WithID_Actor class attributes and methods

# UML2WithID_ExecutionEnvironment class attributes and methods

# UML2WithID_Class class attributes and methods

# EncapsulatedClassifier class attributes and methods

# UML2WithID_StateMachine class attributes and methods

# UML2WithID_Signal class attributes and methods

# UML2WithID_UseCase class attributes and methods

# UML2WithID_Collaboration class attributes and methods

# BehavioredClassifier class attributes and methods

# StructuredClassifier class attributes and methods

# UML2WithID_EncapsulatedClassifier class attributes and methods

# UML2WithID_DataType class attributes and methods

# UML2WithID_ExtensionEnd class attributes and methods

# UML2WithID_Enumeration class attributes and methods

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# Relationships
general0: BinaryAssociation = BinaryAssociation(
    name="general0",
    ends={
        Property(name="UML2WithID_Classifier", type=UML2WithID_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Generalization", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1))
    }
)
memberEnd1: BinaryAssociation = BinaryAssociation(
    name="memberEnd1",
    ends={
        Property(name="UML2WithID_Property", type=UML2WithID_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Association", type=UML2WithID_Property, multiplicity=Multiplicity(2, 9999))
    }
)
generalization2: BinaryAssociation = BinaryAssociation(
    name="generalization2",
    ends={
        Property(name="UML2WithID_Generalization4", type=UML2WithID_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Classifier3", type=UML2WithID_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2WithID_Property_Element = Generalization(general=Element, specific=UML2WithID_Property)
gen_UML2WithID_CommunicationPath_Association = Generalization(general=Association, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_CommunicationPath_Element = Generalization(general=Element, specific=UML2WithID_CommunicationPath)
gen_UML2WithID_StructuredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_StructuredClassifier)
gen_UML2WithID_StructuredClassifier_Element = Generalization(general=Element, specific=UML2WithID_StructuredClassifier)
gen_UML2WithID_ParameterableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_ParameterableClassifier)
gen_UML2WithID_ParameterableClassifier_Element = Generalization(general=Element, specific=UML2WithID_ParameterableClassifier)
gen_UML2WithID_Interaction_Behavior = Generalization(general=Behavior, specific=UML2WithID_Interaction)
gen_UML2WithID_Interaction_Element = Generalization(general=Element, specific=UML2WithID_Interaction)
gen_UML2WithID_AssociationClass_Class = Generalization(general=Class_, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Association = Generalization(general=Association, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Element = Generalization(general=Element, specific=UML2WithID_AssociationClass)
gen_UML2WithID_BehavioredClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_BehavioredClassifier_Element = Generalization(general=Element, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_Artifact_Classifier = Generalization(general=Classifier, specific=UML2WithID_Artifact)
gen_UML2WithID_Artifact_Element = Generalization(general=Element, specific=UML2WithID_Artifact)
gen_UML2WithID_Port_Property = Generalization(general=Property_, specific=UML2WithID_Port)
gen_UML2WithID_Port_Element = Generalization(general=Element, specific=UML2WithID_Port)
gen_UML2WithID_Behavior_Class = Generalization(general=Class_, specific=UML2WithID_Behavior)
gen_UML2WithID_Behavior_Element = Generalization(general=Element, specific=UML2WithID_Behavior)
gen_UML2WithID_Device_Node = Generalization(general=Node, specific=UML2WithID_Device)
gen_UML2WithID_Device_Element = Generalization(general=Element, specific=UML2WithID_Device)
gen_UML2WithID_TemplateableClassifier_Classifier = Generalization(general=Classifier, specific=UML2WithID_TemplateableClassifier)
gen_UML2WithID_TemplateableClassifier_Element = Generalization(general=Element, specific=UML2WithID_TemplateableClassifier)
gen_UML2WithID_Generalization_Element = Generalization(general=Element, specific=UML2WithID_Generalization)
gen_UML2WithID_PrimitiveType_DataType = Generalization(general=DataType, specific=UML2WithID_PrimitiveType)
gen_UML2WithID_PrimitiveType_Element = Generalization(general=Element, specific=UML2WithID_PrimitiveType)
gen_UML2WithID_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_ProtocolStateMachine_Element = Generalization(general=Element, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_DeploymentSpecification_Artifact = Generalization(general=Artifact, specific=UML2WithID_DeploymentSpecification)
gen_UML2WithID_DeploymentSpecification_Element = Generalization(general=Element, specific=UML2WithID_DeploymentSpecification)
gen_UML2WithID_Interface_Classifier = Generalization(general=Classifier, specific=UML2WithID_Interface)
gen_UML2WithID_Interface_Element = Generalization(general=Element, specific=UML2WithID_Interface)
gen_UML2WithID_Component_Class = Generalization(general=Class_, specific=UML2WithID_Component)
gen_UML2WithID_Component_Element = Generalization(general=Element, specific=UML2WithID_Component)
gen_UML2WithID_Extension_Association = Generalization(general=Association, specific=UML2WithID_Extension)
gen_UML2WithID_Extension_Element = Generalization(general=Element, specific=UML2WithID_Extension)
gen_UML2WithID_Stereotype_Class = Generalization(general=Class_, specific=UML2WithID_Stereotype)
gen_UML2WithID_Stereotype_Element = Generalization(general=Element, specific=UML2WithID_Stereotype)
gen_UML2WithID_Enumeration_Element = Generalization(general=Element, specific=UML2WithID_Enumeration)
gen_UML2WithID_Activity_Behavior = Generalization(general=Behavior, specific=UML2WithID_Activity)
gen_UML2WithID_Activity_Element = Generalization(general=Element, specific=UML2WithID_Activity)
gen_UML2WithID_InformationItem_Classifier = Generalization(general=Classifier, specific=UML2WithID_InformationItem)
gen_UML2WithID_InformationItem_Element = Generalization(general=Element, specific=UML2WithID_InformationItem)
gen_UML2WithID_Node_Class = Generalization(general=Class_, specific=UML2WithID_Node)
gen_UML2WithID_Node_Element = Generalization(general=Element, specific=UML2WithID_Node)
gen_UML2WithID_Association_Classifier = Generalization(general=Classifier, specific=UML2WithID_Association)
gen_UML2WithID_Association_Element = Generalization(general=Element, specific=UML2WithID_Association)
gen_UML2WithID_Actor_Classifier = Generalization(general=Classifier, specific=UML2WithID_Actor)
gen_UML2WithID_Actor_Element = Generalization(general=Element, specific=UML2WithID_Actor)
gen_UML2WithID_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_ExecutionEnvironment_Element = Generalization(general=Element, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_EncapsulatedClassifier = Generalization(general=EncapsulatedClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_Element = Generalization(general=Element, specific=UML2WithID_Class)
gen_UML2WithID_Classifier_Element = Generalization(general=Element, specific=UML2WithID_Classifier)
gen_UML2WithID_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2WithID_StateMachine)
gen_UML2WithID_StateMachine_Element = Generalization(general=Element, specific=UML2WithID_StateMachine)
gen_UML2WithID_Signal_Classifier = Generalization(general=Classifier, specific=UML2WithID_Signal)
gen_UML2WithID_Signal_Element = Generalization(general=Element, specific=UML2WithID_Signal)
gen_UML2WithID_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_UseCase)
gen_UML2WithID_UseCase_Element = Generalization(general=Element, specific=UML2WithID_UseCase)
gen_UML2WithID_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_Element = Generalization(general=Element, specific=UML2WithID_Collaboration)
gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier = Generalization(general=StructuredClassifier, specific=UML2WithID_EncapsulatedClassifier)
gen_UML2WithID_EncapsulatedClassifier_Element = Generalization(general=Element, specific=UML2WithID_EncapsulatedClassifier)
gen_UML2WithID_DataType_Classifier = Generalization(general=Classifier, specific=UML2WithID_DataType)
gen_UML2WithID_DataType_Element = Generalization(general=Element, specific=UML2WithID_DataType)
gen_UML2WithID_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_ExtensionEnd_Element = Generalization(general=Element, specific=UML2WithID_ExtensionEnd)
gen_UML2WithID_Enumeration_DataType = Generalization(general=DataType, specific=UML2WithID_Enumeration)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={UML2WithID_Property, Element, UML2WithID_CommunicationPath, Association, UML2WithID_StructuredClassifier, Classifier, UML2WithID_ParameterableClassifier, UML2WithID_Interaction, Behavior, UML2WithID_AssociationClass, UML2WithID_BehavioredClassifier, UML2WithID_Artifact, UML2WithID_Port, Property_, UML2WithID_Behavior, UML2WithID_Device, Node, UML2WithID_TemplateableClassifier, UML2WithID_Generalization, UML2WithID_Classifier, UML2WithID_PrimitiveType, DataType, UML2WithID_ProtocolStateMachine, StateMachine, UML2WithID_DeploymentSpecification, Artifact, UML2WithID_Interface, UML2WithID_Component, Class_, UML2WithID_Extension, UML2WithID_Stereotype, UML2WithID_Activity, UML2WithID_InformationItem, UML2WithID_Node, UML2WithID_Association, UML2WithID_Actor, UML2WithID_ExecutionEnvironment, UML2WithID_Class, EncapsulatedClassifier, UML2WithID_StateMachine, UML2WithID_Signal, UML2WithID_UseCase, UML2WithID_Collaboration, BehavioredClassifier, StructuredClassifier, UML2WithID_EncapsulatedClassifier, UML2WithID_DataType, UML2WithID_ExtensionEnd, UML2WithID_Enumeration, UML2WithID_Element},
    associations={general0, memberEnd1, generalization2},
    generalizations={gen_UML2WithID_Property_Element, gen_UML2WithID_CommunicationPath_Association, gen_UML2WithID_CommunicationPath_Element, gen_UML2WithID_StructuredClassifier_Classifier, gen_UML2WithID_StructuredClassifier_Element, gen_UML2WithID_ParameterableClassifier_Classifier, gen_UML2WithID_ParameterableClassifier_Element, gen_UML2WithID_Interaction_Behavior, gen_UML2WithID_Interaction_Element, gen_UML2WithID_AssociationClass_Class, gen_UML2WithID_AssociationClass_Association, gen_UML2WithID_AssociationClass_Element, gen_UML2WithID_BehavioredClassifier_Classifier, gen_UML2WithID_BehavioredClassifier_Element, gen_UML2WithID_Artifact_Classifier, gen_UML2WithID_Artifact_Element, gen_UML2WithID_Port_Property, gen_UML2WithID_Port_Element, gen_UML2WithID_Behavior_Class, gen_UML2WithID_Behavior_Element, gen_UML2WithID_Device_Node, gen_UML2WithID_Device_Element, gen_UML2WithID_TemplateableClassifier_Classifier, gen_UML2WithID_TemplateableClassifier_Element, gen_UML2WithID_Generalization_Element, gen_UML2WithID_PrimitiveType_DataType, gen_UML2WithID_PrimitiveType_Element, gen_UML2WithID_ProtocolStateMachine_StateMachine, gen_UML2WithID_ProtocolStateMachine_Element, gen_UML2WithID_DeploymentSpecification_Artifact, gen_UML2WithID_DeploymentSpecification_Element, gen_UML2WithID_Interface_Classifier, gen_UML2WithID_Interface_Element, gen_UML2WithID_Component_Class, gen_UML2WithID_Component_Element, gen_UML2WithID_Extension_Association, gen_UML2WithID_Extension_Element, gen_UML2WithID_Stereotype_Class, gen_UML2WithID_Stereotype_Element, gen_UML2WithID_Enumeration_Element, gen_UML2WithID_Activity_Behavior, gen_UML2WithID_Activity_Element, gen_UML2WithID_InformationItem_Classifier, gen_UML2WithID_InformationItem_Element, gen_UML2WithID_Node_Class, gen_UML2WithID_Node_Element, gen_UML2WithID_Association_Classifier, gen_UML2WithID_Association_Element, gen_UML2WithID_Actor_Classifier, gen_UML2WithID_Actor_Element, gen_UML2WithID_ExecutionEnvironment_Node, gen_UML2WithID_ExecutionEnvironment_Element, gen_UML2WithID_Class_BehavioredClassifier, gen_UML2WithID_Class_EncapsulatedClassifier, gen_UML2WithID_Class_Element, gen_UML2WithID_Classifier_Element, gen_UML2WithID_StateMachine_Behavior, gen_UML2WithID_StateMachine_Element, gen_UML2WithID_Signal_Classifier, gen_UML2WithID_Signal_Element, gen_UML2WithID_UseCase_BehavioredClassifier, gen_UML2WithID_UseCase_Element, gen_UML2WithID_Collaboration_BehavioredClassifier, gen_UML2WithID_Collaboration_StructuredClassifier, gen_UML2WithID_Collaboration_Element, gen_UML2WithID_EncapsulatedClassifier_StructuredClassifier, gen_UML2WithID_EncapsulatedClassifier_Element, gen_UML2WithID_DataType_Classifier, gen_UML2WithID_DataType_Element, gen_UML2WithID_ExtensionEnd_Property, gen_UML2WithID_ExtensionEnd_Element, gen_UML2WithID_Enumeration_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)