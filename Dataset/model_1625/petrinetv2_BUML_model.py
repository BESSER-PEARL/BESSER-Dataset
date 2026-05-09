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
petrinetv2_Net = Class(name="petrinetv2_Net")
petrinetv2_Place = Class(name="petrinetv2_Place")
petrinetv2_Token = Class(name="petrinetv2_Token")
petrinetv2_Transition = Class(name="petrinetv2_Transition")

# petrinetv2_Net class attributes and methods

# petrinetv2_Place class attributes and methods
petrinetv2_Place_name: Property = Property(name="name", type=StringType)
petrinetv2_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
petrinetv2_Place.attributes={petrinetv2_Place_name, petrinetv2_Place_initialTokens}

# petrinetv2_Token class attributes and methods

# petrinetv2_Transition class attributes and methods
petrinetv2_Transition_name: Property = Property(name="name", type=StringType)
petrinetv2_Transition.attributes={petrinetv2_Transition_name}

# Relationships
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinetv2_Place", type=petrinetv2_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv2_Net", type=petrinetv2_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="petrinetv2_Place8", type=petrinetv2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv2_Transition7", type=petrinetv2_Place, multiplicity=Multiplicity(1, 9999))
    }
)
tokens9: BinaryAssociation = BinaryAssociation(
    name="tokens9",
    ends={
        Property(name="petrinetv2_Token", type=petrinetv2_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv2_Place10", type=petrinetv2_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinetv2_Transition", type=petrinetv2_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv2_Net2", type=petrinetv2_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petrinetv2_Place5", type=petrinetv2_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetv2_Transition4", type=petrinetv2_Place, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinetv2",
    types={petrinetv2_Net, petrinetv2_Place, petrinetv2_Token, petrinetv2_Transition},
    associations={places0, output6, tokens9, transitions1, input3},
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