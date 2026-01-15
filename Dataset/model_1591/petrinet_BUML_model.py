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
petrinet_Net = Class(name="petrinet::Net")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")

# petrinet_Net class attributes and methods

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_name, petrinet_Place_tokens}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition.attributes={petrinet_Transition_name}

# Relationships
place0: BinaryAssociation = BinaryAssociation(
    name="place0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition1: BinaryAssociation = BinaryAssociation(
    name="transition1",
    ends={
        Property(name="petrinet_Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petrinet_Transition4", type=petrinet_Place, multiplicity=Multiplicity(1, 9999)),
        Property(name="petrinet_Place5", type=petrinet_Transition, multiplicity=Multiplicity(1, 1))
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="petrinet_Place8", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition7", type=petrinet_Place, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Net, petrinet_Place, petrinet_Transition},
    associations={place0, transition1, input3, output6},
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