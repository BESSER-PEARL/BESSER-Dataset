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
gemoc_FSM = Class(name="gemoc::FSM")
gemoc_State = Class(name="gemoc::State")
gemoc_Transition = Class(name="gemoc::Transition")

# gemoc_FSM class attributes and methods
gemoc_FSM_name: Property = Property(name="name", type=StringType)
gemoc_FSM_m_print: Method = Method(name="print", parameters={})
gemoc_FSM.attributes={gemoc_FSM_name}
gemoc_FSM.methods={gemoc_FSM_m_print}

# gemoc_State class attributes and methods
gemoc_State_name: Property = Property(name="name", type=StringType)
gemoc_State.attributes={gemoc_State_name}

# gemoc_Transition class attributes and methods
gemoc_Transition_name: Property = Property(name="name", type=StringType)
gemoc_Transition_trigger: Property = Property(name="trigger", type=StringType)
gemoc_Transition.attributes={gemoc_Transition_name, gemoc_Transition_trigger}

# Relationships
state0: BinaryAssociation = BinaryAssociation(
    name="state0",
    ends={
        Property(name="gemoc_State", type=gemoc_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gemoc_FSM", type=gemoc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="gemoc_Transition", type=gemoc_FSM, multiplicity=Multiplicity(1, 1)),
        Property(name="gemoc_FSM2", type=gemoc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=gemoc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=gemoc_Transition, multiplicity=Multiplicity(0, 1))
    }
)
outcoming4: BinaryAssociation = BinaryAssociation(
    name="outcoming4",
    ends={
        Property(name="Transition5", type=gemoc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=gemoc_Transition, multiplicity=Multiplicity(0, 1))
    }
)
state6: BinaryAssociation = BinaryAssociation(
    name="state6",
    ends={
        Property(name="State", type=gemoc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=gemoc_State, multiplicity=Multiplicity(0, 1))
    }
)
src7: BinaryAssociation = BinaryAssociation(
    name="src7",
    ends={
        Property(name="State8", type=gemoc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outcoming", type=gemoc_State, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="gemoc",
    types={gemoc_FSM, gemoc_State, gemoc_Transition},
    associations={state0, transition1, incoming3, outcoming4, state6, src7},
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