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
petrinetv3_Net = Class(name="petrinetv3::Net")
petrinetv3_Place = Class(name="petrinetv3::Place")
petrinetv3_Transition = Class(name="petrinetv3::Transition")
petrinetv3_Token = Class(name="petrinetv3::Token")

# petrinetv3_Net class attributes and methods

# petrinetv3_Place class attributes and methods
petrinetv3_Place_name: Property = Property(name="name", type=StringType)
petrinetv3_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
petrinetv3_Place.attributes={petrinetv3_Place_initialTokens, petrinetv3_Place_name}

# petrinetv3_Transition class attributes and methods
petrinetv3_Transition_clock: Property = Property(name="clock", type=IntegerType)
petrinetv3_Transition_name: Property = Property(name="name", type=StringType)
petrinetv3_Transition_tmin: Property = Property(name="tmin", type=IntegerType)
petrinetv3_Transition_tmax: Property = Property(name="tmax", type=IntegerType)
petrinetv3_Transition.attributes={petrinetv3_Transition_tmax, petrinetv3_Transition_clock, petrinetv3_Transition_tmin, petrinetv3_Transition_name}

# petrinetv3_Token class attributes and methods

# Relationships
input2: BinaryAssociation = BinaryAssociation(
    name="input2",
    ends={
        Property(name="petrinetv3_Place3", type=petrinetv3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3_Transition", type=petrinetv3_Place, multiplicity=Multiplicity(1, 9999))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinetv3_Place", type=petrinetv3_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3_Net", type=petrinetv3_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="Transition", type=petrinetv3_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNet", type=petrinetv3_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNet7: BinaryAssociation = BinaryAssociation(
    name="parentNet7",
    ends={
        Property(name="Net", type=petrinetv3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="transitions", type=petrinetv3_Net, multiplicity=Multiplicity(1, 1))
    }
)
output4: BinaryAssociation = BinaryAssociation(
    name="output4",
    ends={
        Property(name="petrinetv3_Place6", type=petrinetv3_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3_Transition5", type=petrinetv3_Place, multiplicity=Multiplicity(1, 9999))
    }
)
tokens8: BinaryAssociation = BinaryAssociation(
    name="tokens8",
    ends={
        Property(name="petrinetv3_Token", type=petrinetv3_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv3_Place9", type=petrinetv3_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinetv3",
    types={petrinetv3_Net, petrinetv3_Place, petrinetv3_Transition, petrinetv3_Token},
    associations={input2, places0, transitions1, parentNet7, output4, tokens8},
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