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
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_Box = Class(name="petrinet::Box")
petrinet_Net = Class(name="petrinet::Net")

# petrinet_Place class attributes and methods
petrinet_Place_id: Property = Property(name="id", type=IntegerType)
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place.attributes={petrinet_Place_name, petrinet_Place_id}

# petrinet_Transition class attributes and methods
petrinet_Transition_id: Property = Property(name="id", type=IntegerType)
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name, petrinet_Transition_id}

# petrinet_Box class attributes and methods
petrinet_Box_id: Property = Property(name="id", type=IntegerType)
petrinet_Box_name: Property = Property(name="name", type=StringType)
petrinet_Box.attributes={petrinet_Box_id, petrinet_Box_name}

# petrinet_Net class attributes and methods

# Relationships
box11: BinaryAssociation = BinaryAssociation(
    name="box11",
    ends={
        Property(name="petrinet_Box13", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net12", type=petrinet_Box, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place14: BinaryAssociation = BinaryAssociation(
    name="place14",
    ends={
        Property(name="petrinet_Place16", type=petrinet_Box, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Box15", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
box1: BinaryAssociation = BinaryAssociation(
    name="box1",
    ends={
        Property(name="petrinet_Box", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition2", type=petrinet_Box, multiplicity=Multiplicity(0, 9999))
    }
)
place3: BinaryAssociation = BinaryAssociation(
    name="place3",
    ends={
        Property(name="petrinet_Place5", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition4", type=petrinet_Place, multiplicity=Multiplicity(0, 9999))
    }
)
place6: BinaryAssociation = BinaryAssociation(
    name="place6",
    ends={
        Property(name="petrinet_Place7", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition8: BinaryAssociation = BinaryAssociation(
    name="transition8",
    ends={
        Property(name="petrinet_Transition10", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net9", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Place, petrinet_Transition, petrinet_Box, petrinet_Net},
    associations={box11, place14, transition0, box1, place3, place6, transition8},
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