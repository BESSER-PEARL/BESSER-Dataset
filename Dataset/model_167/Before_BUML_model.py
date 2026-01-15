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

# lit_petriNets_Net class attributes and methods
lit_petriNets_Net_name: Property = Property(name="name", type=StringType)
lit_petriNets_Net.attributes={lit_petriNets_Net_name}

# lit_petriNets_Place class attributes and methods
lit_petriNets_Place_name: Property = Property(name="name", type=StringType)
lit_petriNets_Place.attributes={lit_petriNets_Place_name}

# lit_petriNets_Transition class attributes and methods
lit_petriNets_Transition_name: Property = Property(name="name", type=StringType)
lit_petriNets_Transition.attributes={lit_petriNets_Transition_name}

# Relationships
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
net3: BinaryAssociation = BinaryAssociation(
    name="net3",
    ends={
        Property(name="Net", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="places", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
net8: BinaryAssociation = BinaryAssociation(
    name="net8",
    ends={
        Property(name="Net9", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=lit_petriNets_Net, multiplicity=Multiplicity(1, 1))
    }
)
src10: BinaryAssociation = BinaryAssociation(
    name="src10",
    ends={
        Property(name="Place12", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="dst11", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 9999))
    }
)
dst13: BinaryAssociation = BinaryAssociation(
    name="dst13",
    ends={
        Property(name="Place15", type=lit_petriNets_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="src14", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 9999))
    }
)
src4: BinaryAssociation = BinaryAssociation(
    name="src4",
    ends={
        Property(name="Transition5", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="dst", type=lit_petriNets_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
dst6: BinaryAssociation = BinaryAssociation(
    name="dst6",
    ends={
        Property(name="Transition7", type=lit_petriNets_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="src", type=lit_petriNets_Transition, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="lit_petriNets",
    types={lit_petriNets_Net, lit_petriNets_Place, lit_petriNets_Transition},
    associations={places0, transitions1, net3, net8, src10, dst13, src4, dst6},
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