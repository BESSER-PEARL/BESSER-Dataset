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
lit_petriNets_Transition = Class(name="lit_petriNets_Transition")
lit_petriNets_Arc = Class(name="lit_petriNets_Arc", is_abstract=True)
lit_petriNets_Net = Class(name="lit_petriNets_Net")
lit_petriNets_Place = Class(name="lit_petriNets_Place")
Arc = Class(name="Arc")
lit_petriNets_PTArc = Class(name="lit_petriNets_PTArc")
lit_petriNets_TPArc = Class(name="lit_petriNets_TPArc")

# lit_petriNets_Transition class attributes and methods
lit_petriNets_Transition_name: Property = Property(name="name", type=StringType)
lit_petriNets_Transition.attributes={lit_petriNets_Transition_name}

# lit_petriNets_Arc class attributes and methods

# lit_petriNets_Net class attributes and methods

# lit_petriNets_Place class attributes and methods
lit_petriNets_Place_name: Property = Property(name="name", type=StringType)
lit_petriNets_Place.attributes={lit_petriNets_Place_name}

# Arc class attributes and methods

# lit_petriNets_PTArc class attributes and methods

# lit_petriNets_TPArc class attributes and methods

# Relationships
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
        Property(name="Arc", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net4", type=lit_petriNets_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=lit_petriNets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
out13: BinaryAssociation = BinaryAssociation(
    name="out13",
    ends={
        Property(name="TPArc15", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 9999))
    }
)
src16: BinaryAssociation = BinaryAssociation(
    name="src16",
    ends={
        Property(name="Place17", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
net5: BinaryAssociation = BinaryAssociation(
    name="net5",
    ends={
        Property(name="Net", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
out6: BinaryAssociation = BinaryAssociation(
    name="out6",
    ends={
        Property(name="PTArc", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=lit_petriNets_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
in_7: BinaryAssociation = BinaryAssociation(
    name="in_7",
    ends={
        Property(name="TPArc", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=lit_petriNets_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
in_10: BinaryAssociation = BinaryAssociation(
    name="in_10",
    ends={
        Property(name="PTArc12", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
dst18: BinaryAssociation = BinaryAssociation(
    name="dst18",
    ends={
        Property(name="Transition19", type=lit_petriNets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src20: BinaryAssociation = BinaryAssociation(
    name="src20",
    ends={
        Property(name="Transition22", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out21", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst23: BinaryAssociation = BinaryAssociation(
    name="dst23",
    ends={
        Property(name="Place25", type=lit_petriNets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_24", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1))
    }
)
net26: BinaryAssociation = BinaryAssociation(
    name="net26",
    ends={
        Property(name="Net27", type=lit_petriNets_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_lit_petriNets_PTArc_Arc = Generalization(general=Arc, specific=lit_petriNets_PTArc)
gen_lit_petriNets_TPArc_Arc = Generalization(general=Arc, specific=lit_petriNets_TPArc)

# Domain Model
domain_model = DomainModel(
    name="lit_petriNets",
    types={lit_petriNets_Transition, lit_petriNets_Arc, lit_petriNets_Net, lit_petriNets_Place, Arc, lit_petriNets_PTArc, lit_petriNets_TPArc},
    associations={transitions1, arcs3, places0, out13, src16, net5, out6, in_7, net8, in_10, dst18, src20, dst23, net26},
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