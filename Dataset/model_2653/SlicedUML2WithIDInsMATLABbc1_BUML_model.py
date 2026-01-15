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
UML2WithID_Device = Class(name="UML2WithID::Device")
Node = Class(name="Node")
Element = Class(name="Element")
UML2WithID_ProtocolStateMachine = Class(name="UML2WithID::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2WithID_Collaboration = Class(name="UML2WithID::Collaboration")
BehavioredClassifier = Class(name="BehavioredClassifier")
UML2WithID_BehavioralFeature = Class(name="UML2WithID::BehavioralFeature", is_abstract=True)
UML2WithID_Stereotype = Class(name="UML2WithID::Stereotype")
Class_ = Class(name="Class")
UML2WithID_Reception = Class(name="UML2WithID::Reception")
BehavioralFeature = Class(name="BehavioralFeature")
UML2WithID_Operation = Class(name="UML2WithID::Operation")
UML2WithID_BehavioredClassifier = Class(name="UML2WithID::BehavioredClassifier", is_abstract=True)
UML2WithID_Behavior = Class(name="UML2WithID::Behavior", is_abstract=True)
UML2WithID_StateMachine = Class(name="UML2WithID::StateMachine")
Behavior = Class(name="Behavior")
UML2WithID_UseCase = Class(name="UML2WithID::UseCase")
UML2WithID_ExecutionEnvironment = Class(name="UML2WithID::ExecutionEnvironment")
UML2WithID_Interaction = Class(name="UML2WithID::Interaction")
UML2WithID_Component = Class(name="UML2WithID::Component")
UML2WithID_AssociationClass = Class(name="UML2WithID::AssociationClass")
UML2WithID_Node = Class(name="UML2WithID::Node")
UML2WithID_Activity = Class(name="UML2WithID::Activity")
UML2WithID_Class = Class(name="UML2WithID::Class")
UML2WithID_Element = Class(name="UML2WithID::Element", is_abstract=True)

# UML2WithID_Device class attributes and methods

# Node class attributes and methods

# Element class attributes and methods

# UML2WithID_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2WithID_Collaboration class attributes and methods

# BehavioredClassifier class attributes and methods

# UML2WithID_BehavioralFeature class attributes and methods

# UML2WithID_Stereotype class attributes and methods

# Class class attributes and methods

# UML2WithID_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# UML2WithID_Operation class attributes and methods

# UML2WithID_BehavioredClassifier class attributes and methods

# UML2WithID_Behavior class attributes and methods

# UML2WithID_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2WithID_UseCase class attributes and methods

# UML2WithID_ExecutionEnvironment class attributes and methods

# UML2WithID_Interaction class attributes and methods

# UML2WithID_Component class attributes and methods

# UML2WithID_AssociationClass class attributes and methods

# UML2WithID_Node class attributes and methods

# UML2WithID_Activity class attributes and methods

# UML2WithID_Class class attributes and methods

# UML2WithID_Element class attributes and methods
UML2WithID_Element_ID: Property = Property(name="ID", type=StringType)
UML2WithID_Element.attributes={UML2WithID_Element_ID}

# Relationships
ownedBehavior0: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior0",
    ends={
        Property(name="UML2WithID_Behavior", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_BehavioredClassifier", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior1: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior1",
    ends={
        Property(name="UML2WithID_BehavioredClassifier2", type=UML2WithID_Behavior, multiplicity=Multiplicity(0, 1)),
        Property(name="UML2WithID_Behavior3", type=UML2WithID_BehavioredClassifier, multiplicity=Multiplicity(1, 1))
    }
)
specification4: BinaryAssociation = BinaryAssociation(
    name="specification4",
    ends={
        Property(name="UML2WithID_BehavioralFeature", type=UML2WithID_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2WithID_Behavior5", type=UML2WithID_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML2WithID_Device_Node = Generalization(general=Node, specific=UML2WithID_Device)
gen_UML2WithID_Device_Element = Generalization(general=Element, specific=UML2WithID_Device)
gen_UML2WithID_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_ProtocolStateMachine_Element = Generalization(general=Element, specific=UML2WithID_ProtocolStateMachine)
gen_UML2WithID_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Collaboration)
gen_UML2WithID_Collaboration_Element = Generalization(general=Element, specific=UML2WithID_Collaboration)
gen_UML2WithID_BehavioralFeature_Element = Generalization(general=Element, specific=UML2WithID_BehavioralFeature)
gen_UML2WithID_Stereotype_Class = Generalization(general=Class_, specific=UML2WithID_Stereotype)
gen_UML2WithID_Stereotype_Element = Generalization(general=Element, specific=UML2WithID_Stereotype)
gen_UML2WithID_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Reception)
gen_UML2WithID_Reception_Element = Generalization(general=Element, specific=UML2WithID_Reception)
gen_UML2WithID_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2WithID_Operation)
gen_UML2WithID_Operation_Element = Generalization(general=Element, specific=UML2WithID_Operation)
gen_UML2WithID_BehavioredClassifier_Element = Generalization(general=Element, specific=UML2WithID_BehavioredClassifier)
gen_UML2WithID_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2WithID_StateMachine)
gen_UML2WithID_StateMachine_Element = Generalization(general=Element, specific=UML2WithID_StateMachine)
gen_UML2WithID_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_UseCase)
gen_UML2WithID_UseCase_Element = Generalization(general=Element, specific=UML2WithID_UseCase)
gen_UML2WithID_Behavior_Class = Generalization(general=Class_, specific=UML2WithID_Behavior)
gen_UML2WithID_Behavior_Element = Generalization(general=Element, specific=UML2WithID_Behavior)
gen_UML2WithID_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_ExecutionEnvironment_Element = Generalization(general=Element, specific=UML2WithID_ExecutionEnvironment)
gen_UML2WithID_Interaction_Behavior = Generalization(general=Behavior, specific=UML2WithID_Interaction)
gen_UML2WithID_Interaction_Element = Generalization(general=Element, specific=UML2WithID_Interaction)
gen_UML2WithID_Component_Class = Generalization(general=Class_, specific=UML2WithID_Component)
gen_UML2WithID_Component_Element = Generalization(general=Element, specific=UML2WithID_Component)
gen_UML2WithID_AssociationClass_Class = Generalization(general=Class_, specific=UML2WithID_AssociationClass)
gen_UML2WithID_AssociationClass_Element = Generalization(general=Element, specific=UML2WithID_AssociationClass)
gen_UML2WithID_Node_Class = Generalization(general=Class_, specific=UML2WithID_Node)
gen_UML2WithID_Node_Element = Generalization(general=Element, specific=UML2WithID_Node)
gen_UML2WithID_Activity_Behavior = Generalization(general=Behavior, specific=UML2WithID_Activity)
gen_UML2WithID_Activity_Element = Generalization(general=Element, specific=UML2WithID_Activity)
gen_UML2WithID_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2WithID_Class)
gen_UML2WithID_Class_Element = Generalization(general=Element, specific=UML2WithID_Class)

# Domain Model
domain_model = DomainModel(
    name="UML2WithID",
    types={UML2WithID_Device, Node, Element, UML2WithID_ProtocolStateMachine, StateMachine, UML2WithID_Collaboration, BehavioredClassifier, UML2WithID_BehavioralFeature, UML2WithID_Stereotype, Class_, UML2WithID_Reception, BehavioralFeature, UML2WithID_Operation, UML2WithID_BehavioredClassifier, UML2WithID_Behavior, UML2WithID_StateMachine, Behavior, UML2WithID_UseCase, UML2WithID_ExecutionEnvironment, UML2WithID_Interaction, UML2WithID_Component, UML2WithID_AssociationClass, UML2WithID_Node, UML2WithID_Activity, UML2WithID_Class, UML2WithID_Element},
    associations={ownedBehavior0, classifierBehavior1, specification4},
    generalizations={gen_UML2WithID_Device_Node, gen_UML2WithID_Device_Element, gen_UML2WithID_ProtocolStateMachine_StateMachine, gen_UML2WithID_ProtocolStateMachine_Element, gen_UML2WithID_Collaboration_BehavioredClassifier, gen_UML2WithID_Collaboration_Element, gen_UML2WithID_BehavioralFeature_Element, gen_UML2WithID_Stereotype_Class, gen_UML2WithID_Stereotype_Element, gen_UML2WithID_Reception_BehavioralFeature, gen_UML2WithID_Reception_Element, gen_UML2WithID_Operation_BehavioralFeature, gen_UML2WithID_Operation_Element, gen_UML2WithID_BehavioredClassifier_Element, gen_UML2WithID_StateMachine_Behavior, gen_UML2WithID_StateMachine_Element, gen_UML2WithID_UseCase_BehavioredClassifier, gen_UML2WithID_UseCase_Element, gen_UML2WithID_Behavior_Class, gen_UML2WithID_Behavior_Element, gen_UML2WithID_ExecutionEnvironment_Node, gen_UML2WithID_ExecutionEnvironment_Element, gen_UML2WithID_Interaction_Behavior, gen_UML2WithID_Interaction_Element, gen_UML2WithID_Component_Class, gen_UML2WithID_Component_Element, gen_UML2WithID_AssociationClass_Class, gen_UML2WithID_AssociationClass_Element, gen_UML2WithID_Node_Class, gen_UML2WithID_Node_Element, gen_UML2WithID_Activity_Behavior, gen_UML2WithID_Activity_Element, gen_UML2WithID_Class_BehavioredClassifier, gen_UML2WithID_Class_Element},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)