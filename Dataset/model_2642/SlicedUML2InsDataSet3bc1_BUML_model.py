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
UML2_BehavioralFeature = Class(name="UML2::BehavioralFeature")
UML2_Class = Class(name="UML2::Class")
BehavioredClassifier = Class(name="BehavioredClassifier")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_Node = Class(name="UML2::Node")
Class_ = Class(name="Class")
UML2_StateMachine = Class(name="UML2::StateMachine")
Behavior = Class(name="Behavior")
UML2_Device = Class(name="UML2::Device")
Node = Class(name="Node")
UML2_Reception = Class(name="UML2::Reception")
BehavioralFeature = Class(name="BehavioralFeature")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_Operation = Class(name="UML2::Operation")
UML2_UseCase = Class(name="UML2::UseCase")
UML2_Collaboration = Class(name="UML2::Collaboration")
UML2_Activity = Class(name="UML2::Activity")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_BehavioredClassifier = Class(name="UML2::BehavioredClassifier")
UML2_Component = Class(name="UML2::Component")
UML2_Interaction = Class(name="UML2::Interaction")

# UML2_BehavioralFeature class attributes and methods

# UML2_Class class attributes and methods

# BehavioredClassifier class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_Node class attributes and methods

# Class class attributes and methods

# UML2_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2_Device class attributes and methods

# Node class attributes and methods

# UML2_Reception class attributes and methods

# BehavioralFeature class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_Operation class attributes and methods

# UML2_UseCase class attributes and methods

# UML2_Collaboration class attributes and methods

# UML2_Activity class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_BehavioredClassifier class attributes and methods

# UML2_Component class attributes and methods

# UML2_Interaction class attributes and methods

# Relationships
ownedBehavior0: BinaryAssociation = BinaryAssociation(
    name="ownedBehavior0",
    ends={
        Property(name="UML2_Behavior", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier", type=UML2_Behavior, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classifierBehavior1: BinaryAssociation = BinaryAssociation(
    name="classifierBehavior1",
    ends={
        Property(name="UML2_Behavior3", type=UML2_BehavioredClassifier, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_BehavioredClassifier2", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
specification4: BinaryAssociation = BinaryAssociation(
    name="specification4",
    ends={
        Property(name="UML2_BehavioralFeature", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior5", type=UML2_BehavioralFeature, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_UML2_Class_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Class)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_Reception_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Reception)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_Operation_BehavioralFeature = Generalization(general=BehavioralFeature, specific=UML2_Operation)
gen_UML2_UseCase_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_UseCase)
gen_UML2_Collaboration_BehavioredClassifier = Generalization(general=BehavioredClassifier, specific=UML2_Collaboration)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_BehavioralFeature, UML2_Class, BehavioredClassifier, UML2_ProtocolStateMachine, StateMachine, UML2_Node, Class_, UML2_StateMachine, Behavior, UML2_Device, Node, UML2_Reception, BehavioralFeature, UML2_Behavior, UML2_AssociationClass, UML2_Operation, UML2_UseCase, UML2_Collaboration, UML2_Activity, UML2_ExecutionEnvironment, UML2_Stereotype, UML2_BehavioredClassifier, UML2_Component, UML2_Interaction},
    associations={ownedBehavior0, classifierBehavior1, specification4},
    generalizations={gen_UML2_Class_BehavioredClassifier, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_Node_Class, gen_UML2_StateMachine_Behavior, gen_UML2_Device_Node, gen_UML2_Reception_BehavioralFeature, gen_UML2_AssociationClass_Class, gen_UML2_Operation_BehavioralFeature, gen_UML2_UseCase_BehavioredClassifier, gen_UML2_Collaboration_BehavioredClassifier, gen_UML2_Activity_Behavior, gen_UML2_ExecutionEnvironment_Node, gen_UML2_Stereotype_Class, gen_UML2_Interaction_Behavior, gen_UML2_Behavior_Class, gen_UML2_Component_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)