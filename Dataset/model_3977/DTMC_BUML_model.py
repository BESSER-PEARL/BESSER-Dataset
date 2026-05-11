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
dtmc_State = Class(name="dtmc_State")
dtmc_DTMC = Class(name="dtmc_DTMC")
IDBase = Class(name="IDBase")
dtmc_Transition = Class(name="dtmc_Transition")
dtmc_Label = Class(name="dtmc_Label")

# dtmc_State class attributes and methods
dtmc_State_name: Property = Property(name="name", type=StringType)
dtmc_State.attributes={dtmc_State_name}

# dtmc_DTMC class attributes and methods
dtmc_DTMC_name: Property = Property(name="name", type=StringType)
dtmc_DTMC.attributes={dtmc_DTMC_name}

# IDBase class attributes and methods

# dtmc_Transition class attributes and methods
dtmc_Transition_prob: Property = Property(name="prob", type=FloatType)
dtmc_Transition.attributes={dtmc_Transition_prob}

# dtmc_Label class attributes and methods
dtmc_Label_name: Property = Property(name="name", type=StringType)
dtmc_Label.attributes={dtmc_Label_name}

# Relationships
States0: BinaryAssociation = BinaryAssociation(
    name="States0",
    ends={
        Property(name="dtmc_State", type=dtmc_DTMC, multiplicity=Multiplicity(1, 1)),
        Property(name="dtmc_DTMC", type=dtmc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState1: BinaryAssociation = BinaryAssociation(
    name="initialState1",
    ends={
        Property(name="dtmc_State3", type=dtmc_DTMC, multiplicity=Multiplicity(1, 1)),
        Property(name="dtmc_DTMC2", type=dtmc_State, multiplicity=Multiplicity(0, 1))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Transition", type=dtmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=dtmc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing5: BinaryAssociation = BinaryAssociation(
    name="outgoing5",
    ends={
        Property(name="Transition6", type=dtmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from_", type=dtmc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
labels7: BinaryAssociation = BinaryAssociation(
    name="labels7",
    ends={
        Property(name="Label", type=dtmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=dtmc_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_8: BinaryAssociation = BinaryAssociation(
    name="from_8",
    ends={
        Property(name="State", type=dtmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=dtmc_State, multiplicity=Multiplicity(1, 1))
    }
)
to9: BinaryAssociation = BinaryAssociation(
    name="to9",
    ends={
        Property(name="State10", type=dtmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=dtmc_State, multiplicity=Multiplicity(1, 1))
    }
)
state11: BinaryAssociation = BinaryAssociation(
    name="state11",
    ends={
        Property(name="State12", type=dtmc_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=dtmc_State, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dtmc_State_IDBase = Generalization(general=IDBase, specific=dtmc_State)
gen_dtmc_DTMC_IDBase = Generalization(general=IDBase, specific=dtmc_DTMC)
gen_dtmc_Transition_IDBase = Generalization(general=IDBase, specific=dtmc_Transition)
gen_dtmc_Label_IDBase = Generalization(general=IDBase, specific=dtmc_Label)

# Domain Model
domain_model = DomainModel(
    name="dtmc",
    types={dtmc_State, dtmc_DTMC, IDBase, dtmc_Transition, dtmc_Label},
    associations={States0, initialState1, incoming4, outgoing5, labels7, from_8, to9, state11},
    generalizations={gen_dtmc_State_IDBase, gen_dtmc_DTMC_IDBase, gen_dtmc_Transition_IDBase, gen_dtmc_Label_IDBase},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)