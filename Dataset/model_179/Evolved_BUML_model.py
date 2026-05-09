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
petrinets_Net = Class(name="petrinets_Net")
petrinets_Place = Class(name="petrinets_Place")
petrinets_Transition = Class(name="petrinets_Transition")
Arc = Class(name="Arc")
petrinets_Arc = Class(name="petrinets_Arc", is_abstract=True)
petrinets_TPArc = Class(name="petrinets_TPArc")
petrinets_PTArc = Class(name="petrinets_PTArc")

# petrinets_Net class attributes and methods

# petrinets_Place class attributes and methods
petrinets_Place_name: Property = Property(name="name", type=StringType)
petrinets_Place.attributes={petrinets_Place_name}

# petrinets_Transition class attributes and methods
petrinets_Transition_name: Property = Property(name="name", type=StringType)
petrinets_Transition.attributes={petrinets_Transition_name}

# Arc class attributes and methods

# petrinets_Arc class attributes and methods

# petrinets_TPArc class attributes and methods

# petrinets_PTArc class attributes and methods

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="Place", type=petrinets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net", type=petrinets_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net16: BinaryAssociation = BinaryAssociation(
    name="net16",
    ends={
        Property(name="Net17", type=petrinets_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="arcs", type=petrinets_Net, multiplicity=Multiplicity(1, 1))
    }
)
src18: BinaryAssociation = BinaryAssociation(
    name="src18",
    ends={
        Property(name="Place19", type=petrinets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out", type=petrinets_Place, multiplicity=Multiplicity(1, 1))
    }
)
dst20: BinaryAssociation = BinaryAssociation(
    name="dst20",
    ends={
        Property(name="Transition21", type=petrinets_PTArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_", type=petrinets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
src22: BinaryAssociation = BinaryAssociation(
    name="src22",
    ends={
        Property(name="Transition24", type=petrinets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="out23", type=petrinets_Transition, multiplicity=Multiplicity(1, 1))
    }
)
dst25: BinaryAssociation = BinaryAssociation(
    name="dst25",
    ends={
        Property(name="Place27", type=petrinets_TPArc, multiplicity=Multiplicity(1, 1)),
        Property(name="in_26", type=petrinets_Place, multiplicity=Multiplicity(1, 1))
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net2", type=petrinets_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs3: BinaryAssociation = BinaryAssociation(
    name="arcs3",
    ends={
        Property(name="Arc", type=petrinets_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="net4", type=petrinets_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net5: BinaryAssociation = BinaryAssociation(
    name="net5",
    ends={
        Property(name="Net", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=petrinets_Net, multiplicity=Multiplicity(1, 1))
    }
)
in_6: BinaryAssociation = BinaryAssociation(
    name="in_6",
    ends={
        Property(name="TPArc", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=petrinets_TPArc, multiplicity=Multiplicity(0, 9999))
    }
)
out7: BinaryAssociation = BinaryAssociation(
    name="out7",
    ends={
        Property(name="PTArc", type=petrinets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=petrinets_PTArc, multiplicity=Multiplicity(0, 9999))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinets_Net, multiplicity=Multiplicity(1, 1))
    }
)
in_10: BinaryAssociation = BinaryAssociation(
    name="in_10",
    ends={
        Property(name="PTArc12", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=petrinets_PTArc, multiplicity=Multiplicity(1, 9999))
    }
)
out13: BinaryAssociation = BinaryAssociation(
    name="out13",
    ends={
        Property(name="TPArc15", type=petrinets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=petrinets_TPArc, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_petrinets_PTArc_Arc = Generalization(general=Arc, specific=petrinets_PTArc)
gen_petrinets_TPArc_Arc = Generalization(general=Arc, specific=petrinets_TPArc)

# Domain Model
domain_model = DomainModel(
    name="petrinets",
    types={petrinets_Net, petrinets_Place, petrinets_Transition, Arc, petrinets_Arc, petrinets_TPArc, petrinets_PTArc},
    associations={places0, net16, src18, dst20, src22, dst25, transitions1, arcs3, net5, in_6, out7, net8, in_10, out13},
    generalizations={gen_petrinets_PTArc_Arc, gen_petrinets_TPArc_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)