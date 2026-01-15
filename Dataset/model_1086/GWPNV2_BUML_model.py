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
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Net = Class(name="PetriNet::Net")
PetriNet_PTArc = Class(name="PetriNet::PTArc")
PetriNet_TPArc = Class(name="PetriNet::TPArc")
PetriNet_Transition = Class(name="PetriNet::Transition")

# PetriNet_Place class attributes and methods

# PetriNet_Net class attributes and methods

# PetriNet_PTArc class attributes and methods

# PetriNet_TPArc class attributes and methods

# PetriNet_Transition class attributes and methods

# Relationships
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="1", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
out2: BinaryAssociation = BinaryAssociation(
    name="out2",
    ends={
        Property(name="4", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=PetriNet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in25: BinaryAssociation = BinaryAssociation(
    name="in25",
    ends={
        Property(name="7", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=PetriNet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
dst32: BinaryAssociation = BinaryAssociation(
    name="dst32",
    ends={
        Property(name="34", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="33", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src35: BinaryAssociation = BinaryAssociation(
    name="src35",
    ends={
        Property(name="37", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="36", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
net38: BinaryAssociation = BinaryAssociation(
    name="net38",
    ends={
        Property(name="40", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="39", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src41: BinaryAssociation = BinaryAssociation(
    name="src41",
    ends={
        Property(name="43", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="42", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst44: BinaryAssociation = BinaryAssociation(
    name="dst44",
    ends={
        Property(name="46", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="45", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
in211: BinaryAssociation = BinaryAssociation(
    name="in211",
    ends={
        Property(name="13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out14: BinaryAssociation = BinaryAssociation(
    name="out14",
    ends={
        Property(name="16", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="15", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
place17: BinaryAssociation = BinaryAssociation(
    name="place17",
    ends={
        Property(name="19", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition20: BinaryAssociation = BinaryAssociation(
    name="transition20",
    ends={
        Property(name="22", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=PetriNet_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ptArc23: BinaryAssociation = BinaryAssociation(
    name="ptArc23",
    ends={
        Property(name="25", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="24", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tpArc26: BinaryAssociation = BinaryAssociation(
    name="tpArc26",
    ends={
        Property(name="28", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
net29: BinaryAssociation = BinaryAssociation(
    name="net29",
    ends={
        Property(name="31", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="30", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_Place, PetriNet_Net, PetriNet_PTArc, PetriNet_TPArc, PetriNet_Transition},
    associations={net0, out2, in25, net8, dst32, src35, net38, src41, dst44, in211, out14, place17, transition20, ptArc23, tpArc26, net29},
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