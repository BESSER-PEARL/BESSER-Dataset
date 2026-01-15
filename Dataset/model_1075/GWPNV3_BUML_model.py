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
PetriNet_TPArc = Class(name="PetriNet::TPArc")
PetriNet_Transition = Class(name="PetriNet::Transition")
PetriNet_Place = Class(name="PetriNet::Place")
PetriNet_Net = Class(name="PetriNet::Net")
PetriNet_PTArc = Class(name="PetriNet::PTArc")
PetriNet_Arc = Class(name="PetriNet::Arc", is_abstract=True)
Arc = Class(name="Arc")

# PetriNet_TPArc class attributes and methods

# PetriNet_Transition class attributes and methods

# PetriNet_Place class attributes and methods

# PetriNet_Net class attributes and methods

# PetriNet_PTArc class attributes and methods

# PetriNet_Arc class attributes and methods

# Arc class attributes and methods

# Relationships
in2: BinaryAssociation = BinaryAssociation(
    name="in2",
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
in5: BinaryAssociation = BinaryAssociation(
    name="in5",
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
transition12: BinaryAssociation = BinaryAssociation(
    name="transition12",
    ends={
        Property(name="Transition", type=PetriNet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net13", type=PetriNet_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dst14: BinaryAssociation = BinaryAssociation(
    name="dst14",
    ends={
        Property(name="Transition15", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src16: BinaryAssociation = BinaryAssociation(
    name="src16",
    ends={
        Property(name="Place17", type=PetriNet_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="Transition20", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out19", type=PetriNet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst21: BinaryAssociation = BinaryAssociation(
    name="dst21",
    ends={
        Property(name="Place23", type=PetriNet_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in22", type=PetriNet_Place, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_PetriNet_PTArc_Arc = Generalization(general=Arc, specific=PetriNet_PTArc)
gen_PetriNet_TPArc_Arc = Generalization(general=Arc, specific=PetriNet_TPArc)

# Domain Model
domain_model = DomainModel(
    name="PetriNet",
    types={PetriNet_TPArc, PetriNet_Transition, PetriNet_Place, PetriNet_Net, PetriNet_PTArc, PetriNet_Arc, Arc},
    associations={in2, net3, in5, out8, place11, net0, out1, transition12, dst14, src16, src18, dst21},
    generalizations={gen_PetriNet_PTArc_Arc, gen_PetriNet_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)