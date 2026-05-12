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

# Enumerations
cards: Enumeration = Enumeration(
    name="cards",
    literals={
            EnumerationLiteral(name="small"),
			EnumerationLiteral(name="medium"),
			EnumerationLiteral(name="big")
    }
)

# Classes
maps_PublicSpace = Class(name="maps_PublicSpace", is_abstract=True)
maps_map = Class(name="maps_map")
maps_Road = Class(name="maps_Road", is_abstract=True)
maps_Street = Class(name="maps_Street")
Road = Class(name="Road")
maps_Boulevard = Class(name="maps_Boulevard")
maps_Pedestrian = Class(name="maps_Pedestrian")
maps_Garden = Class(name="maps_Garden")
PublicSpace = Class(name="PublicSpace")
maps_Square = Class(name="maps_Square")

# maps_PublicSpace class attributes and methods
maps_PublicSpace_name: Property = Property(name="name", type=StringType)
maps_PublicSpace.attributes={maps_PublicSpace_name}

# maps_map class attributes and methods
maps_map_name: Property = Property(name="name", type=StringType)
maps_map_isCity: Property = Property(name="isCity", type=BooleanType)
maps_map_country: Property = Property(name="country", type=StringType)
maps_map_size: Property = Property(name="size", type=StringType)
maps_map.attributes={maps_map_name, maps_map_country, maps_map_isCity, maps_map_size}

# maps_Road class attributes and methods
maps_Road_name: Property = Property(name="name", type=StringType)
maps_Road_length: Property = Property(name="length", type=IntegerType)
maps_Road_district: Property = Property(name="district", type=StringType)
maps_Road.attributes={maps_Road_length, maps_Road_district, maps_Road_name}

# maps_Street class attributes and methods

# Road class attributes and methods

# maps_Boulevard class attributes and methods

# maps_Pedestrian class attributes and methods

# maps_Garden class attributes and methods

# PublicSpace class attributes and methods

# maps_Square class attributes and methods

# Relationships
spaces1: BinaryAssociation = BinaryAssociation(
    name="spaces1",
    ends={
        Property(name="maps_PublicSpace", type=maps_map, multiplicity=Multiplicity(1, 1)),
        Property(name="maps_map2", type=maps_PublicSpace, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
border3: BinaryAssociation = BinaryAssociation(
    name="border3",
    ends={
        Property(name="PublicSpace", type=maps_Road, multiplicity=Multiplicity(1, 1)),
        Property(name="borderedBy", type=maps_PublicSpace, multiplicity=Multiplicity(0, 9999))
    }
)
meet5: BinaryAssociation = BinaryAssociation(
    name="meet5",
    ends={
        Property(name="maps_Road6", type=maps_Road, multiplicity=Multiplicity(1, 1)),
        Property(name="maps_Road4", type=maps_Road, multiplicity=Multiplicity(0, 9999))
    }
)
borderedBy7: BinaryAssociation = BinaryAssociation(
    name="borderedBy7",
    ends={
        Property(name="Road", type=maps_PublicSpace, multiplicity=Multiplicity(1, 1)),
        Property(name="border", type=maps_Road, multiplicity=Multiplicity(1, 9999))
    }
)
roads0: BinaryAssociation = BinaryAssociation(
    name="roads0",
    ends={
        Property(name="maps_Road", type=maps_map, multiplicity=Multiplicity(1, 1)),
        Property(name="maps_map", type=maps_Road, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_maps_Square_PublicSpace = Generalization(general=PublicSpace, specific=maps_Square)
gen_maps_Street_Road = Generalization(general=Road, specific=maps_Street)
gen_maps_Boulevard_Road = Generalization(general=Road, specific=maps_Boulevard)
gen_maps_Pedestrian_Road = Generalization(general=Road, specific=maps_Pedestrian)
gen_maps_Garden_PublicSpace = Generalization(general=PublicSpace, specific=maps_Garden)


# OCL Constraints
Unnamed: Constraint = Constraint(
    name="Unnamed",
    context=maps_Road,
    expression="context Road inv: length > 1",
    language="OCL"
)
Unnamed1: Constraint = Constraint(
    name="Unnamed1",
    context=maps_map,
    expression="context map inv: roads->forAll(n1, n2 | n1.name <> n2.name)",
    language="OCL"
)
Unnamed2: Constraint = Constraint(
    name="Unnamed2",
    context=maps_map,
    expression="context map inv: spaces->forAll(n1, n2 | n1.name <> n2.name)",
    language="OCL"
)
Unnamed3: Constraint = Constraint(
    name="Unnamed3",
    context=maps_map,
    expression="context map inv: roads->forAll(n1, n2 | n1.length <> n2.length)",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="maps",
    types={maps_PublicSpace, maps_map, maps_Road, maps_Street, Road, maps_Boulevard, maps_Pedestrian, maps_Garden, PublicSpace, maps_Square, cards},
    associations={spaces1, border3, meet5, borderedBy7, roads0},
    constraints={Unnamed, Unnamed1, Unnamed2, Unnamed3},
    generalizations={gen_maps_Square_PublicSpace, gen_maps_Street_Road, gen_maps_Boulevard_Road, gen_maps_Pedestrian_Road, gen_maps_Garden_PublicSpace},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)