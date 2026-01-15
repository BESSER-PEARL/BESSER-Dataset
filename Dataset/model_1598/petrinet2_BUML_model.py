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
petrinet2_Net = Class(name="petrinet2::Net")
petrinet2_Place = Class(name="petrinet2::Place")
petrinet2_Transition = Class(name="petrinet2::Transition")

# petrinet2_Net class attributes and methods
petrinet2_Net_name: Property = Property(name="name", type=StringType)
petrinet2_Net.attributes={petrinet2_Net_name}

# petrinet2_Place class attributes and methods
petrinet2_Place_name: Property = Property(name="name", type=StringType)
petrinet2_Place.attributes={petrinet2_Place_name}

# petrinet2_Transition class attributes and methods
petrinet2_Transition_name: Property = Property(name="name", type=StringType)
petrinet2_Transition.attributes={petrinet2_Transition_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet2_Place", type=petrinet2_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Net", type=petrinet2_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet2_Transition", type=petrinet2_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Net2", type=petrinet2_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petrinet2_Place5", type=petrinet2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Transition4", type=petrinet2_Place, multiplicity=Multiplicity(1, 9999))
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="petrinet2_Place8", type=petrinet2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet2_Transition7", type=petrinet2_Place, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet2",
    types={petrinet2_Net, petrinet2_Place, petrinet2_Transition},
    associations={places0, transitions1, input3, output6},
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