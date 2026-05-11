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
iDM_Test_StateMachine = Class(name="iDM_Test_StateMachine")
iDM_Test_State = Class(name="iDM_Test_State")
iDM_Test_Transition = Class(name="iDM_Test_Transition")

# iDM_Test_StateMachine class attributes and methods
iDM_Test_StateMachine_name: Property = Property(name="name", type=StringType)
iDM_Test_StateMachine.attributes={iDM_Test_StateMachine_name}

# iDM_Test_State class attributes and methods
iDM_Test_State_name: Property = Property(name="name", type=StringType)
iDM_Test_State.attributes={iDM_Test_State_name}

# iDM_Test_Transition class attributes and methods
iDM_Test_Transition_name: Property = Property(name="name", type=StringType)
iDM_Test_Transition.attributes={iDM_Test_Transition_name}

# Relationships
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State", type=iDM_Test_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=iDM_Test_State, multiplicity=Multiplicity(0, 1))
    }
)
from_10: BinaryAssociation = BinaryAssociation(
    name="from_10",
    ends={
        Property(name="State11", type=iDM_Test_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomming", type=iDM_Test_State, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="iDM_Test_State", type=iDM_Test_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="iDM_Test_StateMachine", type=iDM_Test_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="iDM_Test_Transition", type=iDM_Test_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="iDM_Test_StateMachine2", type=iDM_Test_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
init3: BinaryAssociation = BinaryAssociation(
    name="init3",
    ends={
        Property(name="iDM_Test_State5", type=iDM_Test_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="iDM_Test_StateMachine4", type=iDM_Test_State, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing6: BinaryAssociation = BinaryAssociation(
    name="outgoing6",
    ends={
        Property(name="Transition", type=iDM_Test_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=iDM_Test_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
incomming7: BinaryAssociation = BinaryAssociation(
    name="incomming7",
    ends={
        Property(name="Transition8", type=iDM_Test_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=iDM_Test_Transition, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="iDM_Test",
    types={iDM_Test_StateMachine, iDM_Test_State, iDM_Test_Transition},
    associations={to9, from_10, states0, transition1, init3, outgoing6, incomming7},
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