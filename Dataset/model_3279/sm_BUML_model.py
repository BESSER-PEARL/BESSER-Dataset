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
sm_State = Class(name="sm_State")
sm_Variable = Class(name="sm_Variable")
sm_StateMachine = Class(name="sm_StateMachine")

# sm_State class attributes and methods

# sm_Variable class attributes and methods

# sm_StateMachine class attributes and methods

# Relationships
states1: BinaryAssociation = BinaryAssociation(
    name="states1",
    ends={
        Property(name="sm_State2", type=sm_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_StateMachine", type=sm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input0: BinaryAssociation = BinaryAssociation(
    name="input0",
    ends={
        Property(name="sm_Variable", type=sm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="sm_State", type=sm_Variable, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sm",
    types={sm_State, sm_Variable, sm_StateMachine},
    associations={states1, input0},
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