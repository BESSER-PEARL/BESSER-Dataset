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
Map_Map = Class(name="Map::Map")
Map_Address = Class(name="Map::Address")

# Map_Map class attributes and methods

# Map_Address class attributes and methods
Map_Address_longitude: Property = Property(name="longitude", type=FloatType)
Map_Address_latitude: Property = Property(name="latitude", type=FloatType)
Map_Address_description: Property = Property(name="description", type=StringType)
Map_Address_name: Property = Property(name="name", type=StringType)
Map_Address_telephone: Property = Property(name="telephone", type=StringType)
Map_Address_downtown: Property = Property(name="downtown", type=BooleanType)
Map_Address_pictures: Property = Property(name="pictures", type=StringType)
Map_Address.attributes={Map_Address_longitude, Map_Address_name, Map_Address_telephone, Map_Address_pictures, Map_Address_latitude, Map_Address_description, Map_Address_downtown}

# Relationships
addresses0: BinaryAssociation = BinaryAssociation(
    name="addresses0",
    ends={
        Property(name="Map_Address", type=Map_Map, multiplicity=Multiplicity(1, 1)),
        Property(name="Map_Map", type=Map_Address, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="Map",
    types={Map_Map, Map_Address},
    associations={addresses0},
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