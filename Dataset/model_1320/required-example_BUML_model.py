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
StateMachinesModule_Transition = Class(name="StateMachinesModule::Transition")
StateMachinesModule_Constraint = Class(name="StateMachinesModule::Constraint")
StateMachinesModule_StateMachine = Class(name="StateMachinesModule::StateMachine")
StateMachinesModule_State = Class(name="StateMachinesModule::State")

# StateMachinesModule_Transition class attributes and methods

# StateMachinesModule_Constraint class attributes and methods
StateMachinesModule_Constraint_m_eval: Method = Method(name="eval", parameters={}, type=BooleanType)
StateMachinesModule_Constraint.methods={StateMachinesModule_Constraint_m_eval}

# StateMachinesModule_StateMachine class attributes and methods

# StateMachinesModule_State class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="StateMachinesModule_Transition", type=StateMachinesModule_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesModule_StateMachine2", type=StateMachinesModule_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guard3: BinaryAssociation = BinaryAssociation(
    name="guard3",
    ends={
        Property(name="StateMachinesModule_Constraint", type=StateMachinesModule_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesModule_Transition4", type=StateMachinesModule_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="StateMachinesModule_State", type=StateMachinesModule_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="StateMachinesModule_StateMachine", type=StateMachinesModule_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="StateMachinesModule",
    types={StateMachinesModule_Transition, StateMachinesModule_Constraint, StateMachinesModule_StateMachine, StateMachinesModule_State},
    associations={transitions1, guard3, states0},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)