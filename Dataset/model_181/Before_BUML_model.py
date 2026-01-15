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
lit_petriNets_Net = Class(name="lit::petriNets::Net")
lit_petriNets_Place = Class(name="lit::petriNets::Place")
lit_petriNets_Transition = Class(name="lit::petriNets::Transition")
lit_petriNets_Arc = Class(name="lit::petriNets::Arc", is_abstract=True)
lit_petriNets_TPArc = Class(name="lit::petriNets::TPArc")
lit_petriNets_PTArc = Class(name="lit::petriNets::PTArc")
Arc = Class(name="Arc")

# lit_petriNets_Net class attributes and methods

# lit_petriNets_Place class attributes and methods
lit_petriNets_Place_name: Property = Property(name="name", type=StringType)
lit_petriNets_Place.attributes={lit_petriNets_Place_name}

# lit_petriNets_Transition class attributes and methods
lit_petriNets_Transition_name: Property = Property(name="name", type=StringType)
lit_petriNets_Transition.attributes={lit_petriNets_Transition_name}

# lit_petriNets_Arc class attributes and methods

# lit_petriNets_TPArc class attributes and methods

# lit_petriNets_PTArc class attributes and methods

# Arc class attributes and methods

# Relationships
net7: BinaryAssociation = BinaryAssociation(
    name="net7",
    ends={
        Property(name="Net8", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=lit_petriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=lit_petriNets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="lit_petriNets_Arc", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="lit_petriNets_Net", type=lit_petriNets_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net4: BinaryAssociation = BinaryAssociation(
    name="net4",
    ends={
        Property(name="Net", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
in5: BinaryAssociation = BinaryAssociation(
    name="in5",
    ends={
        Property(name="TPArc", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=lit_petriNets_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
out6: BinaryAssociation = BinaryAssociation(
    name="out6",
    ends={
        Property(name="PTArc", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=lit_petriNets_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
src22: BinaryAssociation = BinaryAssociation(
    name="src22",
    ends={
        Property(name="Transition24", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out23", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst25: BinaryAssociation = BinaryAssociation(
    name="dst25",
    ends={
        Property(name="Place27", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in26", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
in9: BinaryAssociation = BinaryAssociation(
    name="in9",
    ends={
        Property(name="PTArc11", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst10", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out12: BinaryAssociation = BinaryAssociation(
    name="out12",
    ends={
        Property(name="TPArc14", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src13", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
net15: BinaryAssociation = BinaryAssociation(
    name="net15",
    ends={
        Property(name="lit_petriNets_Net17", type=lit_petriNets_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="lit_petriNets_Arc16", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="Place19", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
dst20: BinaryAssociation = BinaryAssociation(
    name="dst20",
    ends={
        Property(name="Transition21", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_lit_petriNets_PTArc_Arc = Generalization(general=Arc, specific=lit_petriNets_PTArc)
gen_lit_petriNets_TPArc_Arc = Generalization(general=Arc, specific=lit_petriNets_TPArc)

# Domain Model
domain_model = DomainModel(
    name="lit_petriNets",
    types={lit_petriNets_Net, lit_petriNets_Place, lit_petriNets_Transition, lit_petriNets_Arc, lit_petriNets_TPArc, lit_petriNets_PTArc, Arc},
    associations={net7, places0, transitions1, arcs3, net4, in5, out6, src22, dst25, in9, out12, net15, src18, dst20},
    generalizations={gen_lit_petriNets_PTArc_Arc, gen_lit_petriNets_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)