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
PN_Net = Class(name="PN::Net")
PN_Place = Class(name="PN::Place")
PN_Transition = Class(name="PN::Transition")

# PN_Net class attributes and methods
PN_Net_name: Property = Property(name="name", type=StringType)
PN_Net.attributes={PN_Net_name}

# PN_Place class attributes and methods
PN_Place_name: Property = Property(name="name", type=StringType)
PN_Place.attributes={PN_Place_name}

# PN_Transition class attributes and methods
PN_Transition_input: Property = Property(name="input", type=StringType)
PN_Transition.attributes={PN_Transition_input}

# Relationships
incoming3: BinaryAssociation = BinaryAssociation(
    name="incoming3",
    ends={
        Property(name="Transition", type=PN_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=PN_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing4: BinaryAssociation = BinaryAssociation(
    name="outgoing4",
    ends={
        Property(name="Transition5", type=PN_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=PN_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
from6: BinaryAssociation = BinaryAssociation(
    name="from6",
    ends={
        Property(name="Place", type=PN_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=PN_Place, multiplicity=Multiplicity(0, 9999))
    }
)
to7: BinaryAssociation = BinaryAssociation(
    name="to7",
    ends={
        Property(name="Place8", type=PN_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=PN_Place, multiplicity=Multiplicity(0, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="PN_Place", type=PN_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_Net", type=PN_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="PN_Transition", type=PN_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="PN_Net2", type=PN_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="PN",
    types={PN_Net, PN_Place, PN_Transition},
    associations={incoming3, outgoing4, from6, to7, places0, transitions1},
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