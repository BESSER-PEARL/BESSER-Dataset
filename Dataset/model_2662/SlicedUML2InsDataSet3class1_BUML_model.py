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
UML2_StateMachine = Class(name="UML2::StateMachine")
Behavior = Class(name="Behavior")
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_ExecutionEnvironment = Class(name="UML2::ExecutionEnvironment")
Node = Class(name="Node")
UML2_Behavior = Class(name="UML2::Behavior")
Class_ = Class(name="Class")
UML2_Device = Class(name="UML2::Device")
UML2_Class = Class(name="UML2::Class")
UML2_Reception = Class(name="UML2::Reception")
UML2_AssociationClass = Class(name="UML2::AssociationClass")
UML2_Stereotype = Class(name="UML2::Stereotype")
UML2_Activity = Class(name="UML2::Activity")
UML2_Node = Class(name="UML2::Node")
UML2_Interaction = Class(name="UML2::Interaction")
UML2_Component = Class(name="UML2::Component")

# UML2_StateMachine class attributes and methods

# Behavior class attributes and methods

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_ExecutionEnvironment class attributes and methods

# Node class attributes and methods

# UML2_Behavior class attributes and methods

# Class class attributes and methods

# UML2_Device class attributes and methods

# UML2_Class class attributes and methods
UML2_Class_isActive: Property = Property(name="isActive", type=BooleanType)
UML2_Class.attributes={UML2_Class_isActive}

# UML2_Reception class attributes and methods

# UML2_AssociationClass class attributes and methods

# UML2_Stereotype class attributes and methods

# UML2_Activity class attributes and methods

# UML2_Node class attributes and methods

# UML2_Interaction class attributes and methods

# UML2_Component class attributes and methods

# Relationships
ownedReception0: BinaryAssociation = BinaryAssociation(
    name="ownedReception0",
    ends={
        Property(name="UML2_Reception", type=UML2_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Class", type=UML2_Reception, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_ExecutionEnvironment_Node = Generalization(general=Node, specific=UML2_ExecutionEnvironment)
gen_UML2_Behavior_Class = Generalization(general=Class_, specific=UML2_Behavior)
gen_UML2_Device_Node = Generalization(general=Node, specific=UML2_Device)
gen_UML2_AssociationClass_Class = Generalization(general=Class_, specific=UML2_AssociationClass)
gen_UML2_Stereotype_Class = Generalization(general=Class_, specific=UML2_Stereotype)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_Node_Class = Generalization(general=Class_, specific=UML2_Node)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)
gen_UML2_Component_Class = Generalization(general=Class_, specific=UML2_Component)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_StateMachine, Behavior, UML2_ProtocolStateMachine, StateMachine, UML2_ExecutionEnvironment, Node, UML2_Behavior, Class_, UML2_Device, UML2_Class, UML2_Reception, UML2_AssociationClass, UML2_Stereotype, UML2_Activity, UML2_Node, UML2_Interaction, UML2_Component},
    associations={ownedReception0},
    generalizations={gen_UML2_StateMachine_Behavior, gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_ExecutionEnvironment_Node, gen_UML2_Behavior_Class, gen_UML2_Device_Node, gen_UML2_AssociationClass_Class, gen_UML2_Stereotype_Class, gen_UML2_Activity_Behavior, gen_UML2_Node_Class, gen_UML2_Interaction_Behavior, gen_UML2_Component_Class},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)