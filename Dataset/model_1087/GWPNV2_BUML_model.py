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
PetriNet_TPArc = Class(name="PetriNet_TPArc")
PetriNet_Transition = Class(name="PetriNet_Transition")
PetriNet_Place = Class(name="PetriNet_Place")
PetriNet_Net = Class(name="PetriNet_Net")
PetriNet_PTArc = Class(name="PetriNet_PTArc")

# PetriNet_TPArc class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Net class attributes and methods

# PetriNet_PTArc class attributes and methods

# Relationships
in22: BinaryAssociation = BinaryAssociation(
    name="in22",
    ends={
        Property(name="TPArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=PetriNet_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net4", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
in25: BinaryAssociation = BinaryAssociation(
    name="in25",
    ends={
        Property(name="PTArc7", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst6", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out8: BinaryAssociation = BinaryAssociation(
    name="out8",
    ends={
        Property(name="TPArc10", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src9", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
place11: BinaryAssociation = BinaryAssociation(
    name="place11",
    ends={
        Property(name="Place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=PetriNet_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transition12: BinaryAssociation = BinaryAssociation(
    name="transition12",
    ends={
        Property(name="Transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
net0: BinaryAssociation = BinaryAssociation(
    name="net0",
    ends={
        Property(name="Net", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="place", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
out1: BinaryAssociation = BinaryAssociation(
    name="out1",
    ends={
        Property(name="PTArc", type=PetriNet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=PetriNet_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
ptArc14: BinaryAssociation = BinaryAssociation(
    name="ptArc14",
    ends={
        Property(name="PTArc16", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net15", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
tpArc17: BinaryAssociation = BinaryAssociation(
    name="tpArc17",
    ends={
        Property(name="TPArc19", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net18", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
net20: BinaryAssociation = BinaryAssociation(
    name="net20",
    ends={
        Property(name="Net21", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="ptArc", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
dst22: BinaryAssociation = BinaryAssociation(
    name="dst22",
    ends={
        Property(name="Transition23", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in2", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src24: BinaryAssociation = BinaryAssociation(
    name="src24",
    ends={
        Property(name="Place25", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
net26: BinaryAssociation = BinaryAssociation(
    name="net26",
    ends={
        Property(name="Net27", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="tpArc", type=PetriNet_Net, multiplicity=Multiplicity(1, 1))
    }
)
src28: BinaryAssociation = BinaryAssociation(
    name="src28",
    ends={
        Property(name="Transition30", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out29", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst31: BinaryAssociation = BinaryAssociation(
    name="dst31",
    ends={
        Property(name="Place33", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in232", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_TPArc, PetriNet_Transition, PetriNet_Place, PetriNet_Net, PetriNet_PTArc},
    associations={in22, net3, in25, out8, place11, transition12, net0, out1, ptArc14, tpArc17, net20, dst22, src24, net26, src28, dst31},
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