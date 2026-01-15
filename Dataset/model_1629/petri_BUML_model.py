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
petri_Place = Class(name="petri::Place")
petri_Transition = Class(name="petri::Transition")
petri_RedPetri = Class(name="petri::RedPetri")

# petri_Place class attributes and methods
petri_Place_name: Property = Property(name="name", type=StringType)
petri_Place_tokens: Property = Property(name="tokens", type=IntegerType)
petri_Place.attributes={petri_Place_tokens, petri_Place_name}

# petri_Transition class attributes and methods
petri_Transition_name: Property = Property(name="name", type=StringType)
petri_Transition.attributes={petri_Transition_name}

# petri_RedPetri class attributes and methods

# Relationships
connection0: BinaryAssociation = BinaryAssociation(
    name="connection0",
    ends={
        Property(name="petri_Transition", type=petri_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Place", type=petri_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
connection1: BinaryAssociation = BinaryAssociation(
    name="connection1",
    ends={
        Property(name="petri_Place3", type=petri_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_Transition2", type=petri_Place, multiplicity=Multiplicity(0, 9999))
    }
)
iniPlace4: BinaryAssociation = BinaryAssociation(
    name="iniPlace4",
    ends={
        Property(name="petri_Place5", type=petri_RedPetri, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_RedPetri", type=petri_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
iniTrans6: BinaryAssociation = BinaryAssociation(
    name="iniTrans6",
    ends={
        Property(name="petri_Transition8", type=petri_RedPetri, multiplicity=Multiplicity(1, 1)),
        Property(name="petri_RedPetri7", type=petri_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petri",
    types={petri_Place, petri_Transition, petri_RedPetri},
    associations={connection0, connection1, iniPlace4, iniTrans6},
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