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
ctmc_Label = Class(name="ctmc::Label")
ctmc_Transition = Class(name="ctmc::Transition")
ctmc_CTMC = Class(name="ctmc::CTMC")
ctmc_State = Class(name="ctmc::State")

# ctmc_Label class attributes and methods
ctmc_Label_text: Property = Property(name="text", type=StringType)
ctmc_Label.attributes={ctmc_Label_text}

# ctmc_Transition class attributes and methods
ctmc_Transition_name: Property = Property(name="name", type=StringType)
ctmc_Transition_probability: Property = Property(name="probability", type=FloatType)
ctmc_Transition_duration: Property = Property(name="duration", type=FloatType)
ctmc_Transition.attributes={ctmc_Transition_duration, ctmc_Transition_name, ctmc_Transition_probability}

# ctmc_CTMC class attributes and methods
ctmc_CTMC_name: Property = Property(name="name", type=StringType)
ctmc_CTMC.attributes={ctmc_CTMC_name}

# ctmc_State class attributes and methods
ctmc_State_name: Property = Property(name="name", type=StringType)
ctmc_State_exitRate: Property = Property(name="exitRate", type=FloatType)
ctmc_State.attributes={ctmc_State_exitRate, ctmc_State_name}

# Relationships
labels1: BinaryAssociation = BinaryAssociation(
    name="labels1",
    ends={
        Property(name="Label", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="state", type=ctmc_Label, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out2: BinaryAssociation = BinaryAssociation(
    name="out2",
    ends={
        Property(name="Transition", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=ctmc_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
in3: BinaryAssociation = BinaryAssociation(
    name="in3",
    ends={
        Property(name="Transition4", type=ctmc_State, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=ctmc_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
from5: BinaryAssociation = BinaryAssociation(
    name="from5",
    ends={
        Property(name="State", type=ctmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=ctmc_State, multiplicity=Multiplicity(1, 1))
    }
)
to6: BinaryAssociation = BinaryAssociation(
    name="to6",
    ends={
        Property(name="State7", type=ctmc_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=ctmc_State, multiplicity=Multiplicity(1, 1))
    }
)
state8: BinaryAssociation = BinaryAssociation(
    name="state8",
    ends={
        Property(name="State9", type=ctmc_Label, multiplicity=Multiplicity(1, 1)),
        Property(name="labels", type=ctmc_State, multiplicity=Multiplicity(0, 1))
    }
)
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="ctmc_State", type=ctmc_CTMC, multiplicity=Multiplicity(1, 1)),
        Property(name="ctmc_CTMC", type=ctmc_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ctmc",
    types={ctmc_Label, ctmc_Transition, ctmc_CTMC, ctmc_State},
    associations={labels1, out2, in3, from5, to6, state8, states0},
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