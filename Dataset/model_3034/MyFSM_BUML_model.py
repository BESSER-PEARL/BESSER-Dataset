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
myfsm_Trans = Class(name="myfsm::Trans")
myfsm_Machine = Class(name="myfsm::Machine")
myfsm_State = Class(name="myfsm::State")

# myfsm_Trans class attributes and methods
myfsm_Trans_event: Property = Property(name="event", type=StringType)
myfsm_Trans.attributes={myfsm_Trans_event}

# myfsm_Machine class attributes and methods
myfsm_Machine_name: Property = Property(name="name", type=StringType)
myfsm_Machine.attributes={myfsm_Machine_name}

# myfsm_State class attributes and methods
myfsm_State_name: Property = Property(name="name", type=StringType)
myfsm_State.attributes={myfsm_State_name}

# Relationships
transitions4: BinaryAssociation = BinaryAssociation(
    name="transitions4",
    ends={
        Property(name="myfsm_Trans", type=myfsm_State, multiplicity=Multiplicity(1, 1)),
        Property(name="myfsm_State5", type=myfsm_Trans, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="myfsm_State", type=myfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="myfsm_Machine", type=myfsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initial1: BinaryAssociation = BinaryAssociation(
    name="initial1",
    ends={
        Property(name="myfsm_State3", type=myfsm_Machine, multiplicity=Multiplicity(1, 1)),
        Property(name="myfsm_Machine2", type=myfsm_State, multiplicity=Multiplicity(0, 1))
    }
)
target6: BinaryAssociation = BinaryAssociation(
    name="target6",
    ends={
        Property(name="myfsm_State8", type=myfsm_Trans, multiplicity=Multiplicity(1, 1)),
        Property(name="myfsm_Trans7", type=myfsm_State, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="myfsm",
    types={myfsm_Trans, myfsm_Machine, myfsm_State},
    associations={transitions4, states0, initial1, target6},
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