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

# Enumerations
ParameterDirectionKind: Enumeration = Enumeration(
    name="ParameterDirectionKind",
    literals={
            EnumerationLiteral(name="out"),
			EnumerationLiteral(name="return"),
			EnumerationLiteral(name="in"),
			EnumerationLiteral(name="inout")
    }
)

# Classes
UML2_ProtocolStateMachine = Class(name="UML2::ProtocolStateMachine")
StateMachine = Class(name="StateMachine")
UML2_Parameter = Class(name="UML2::Parameter")
UML2_Activity = Class(name="UML2::Activity")
Behavior = Class(name="Behavior")
UML2_ParameterSet = Class(name="UML2::ParameterSet")
UML2_OpaqueExpression = Class(name="UML2::OpaqueExpression")
UML2_Behavior = Class(name="UML2::Behavior")
UML2_StateMachine = Class(name="UML2::StateMachine")
UML2_Expression = Class(name="UML2::Expression")
OpaqueExpression = Class(name="OpaqueExpression")
UML2_Interaction = Class(name="UML2::Interaction")

# UML2_ProtocolStateMachine class attributes and methods

# StateMachine class attributes and methods

# UML2_Parameter class attributes and methods
UML2_Parameter_direction: Property = Property(name="direction", type=StringType)
UML2_Parameter.attributes={UML2_Parameter_direction}

# UML2_Activity class attributes and methods

# Behavior class attributes and methods

# UML2_ParameterSet class attributes and methods

# UML2_OpaqueExpression class attributes and methods

# UML2_Behavior class attributes and methods

# UML2_StateMachine class attributes and methods

# UML2_Expression class attributes and methods

# OpaqueExpression class attributes and methods

# UML2_Interaction class attributes and methods

# Relationships
behavior0: BinaryAssociation = BinaryAssociation(
    name="behavior0",
    ends={
        Property(name="UML2_Behavior", type=UML2_OpaqueExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_OpaqueExpression", type=UML2_Behavior, multiplicity=Multiplicity(0, 1))
    }
)
ownedParameterSet1: BinaryAssociation = BinaryAssociation(
    name="ownedParameterSet1",
    ends={
        Property(name="UML2_ParameterSet", type=UML2_Behavior, multiplicity=Multiplicity(1, 1)),
        Property(name="UML2_Behavior2", type=UML2_ParameterSet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML2_ProtocolStateMachine_StateMachine = Generalization(general=StateMachine, specific=UML2_ProtocolStateMachine)
gen_UML2_Activity_Behavior = Generalization(general=Behavior, specific=UML2_Activity)
gen_UML2_StateMachine_Behavior = Generalization(general=Behavior, specific=UML2_StateMachine)
gen_UML2_Expression_OpaqueExpression = Generalization(general=OpaqueExpression, specific=UML2_Expression)
gen_UML2_Interaction_Behavior = Generalization(general=Behavior, specific=UML2_Interaction)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_ProtocolStateMachine, StateMachine, UML2_Parameter, UML2_Activity, Behavior, UML2_ParameterSet, UML2_OpaqueExpression, UML2_Behavior, UML2_StateMachine, UML2_Expression, OpaqueExpression, UML2_Interaction, ParameterDirectionKind},
    associations={behavior0, ownedParameterSet1},
    generalizations={gen_UML2_ProtocolStateMachine_StateMachine, gen_UML2_Activity_Behavior, gen_UML2_StateMachine_Behavior, gen_UML2_Expression_OpaqueExpression, gen_UML2_Interaction_Behavior},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)