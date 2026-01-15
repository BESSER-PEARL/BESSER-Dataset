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
netxstudio_Library = Class(name="netxstudio::Library")
netxstudio_Network = Class(name="netxstudio::Network")
netxstudio_Function = Class(name="netxstudio::Function")
netxstudio_Equipment = Class(name="netxstudio::Equipment")
netxstudio_Metric = Class(name="netxstudio::Metric")
netxstudio_Parameter = Class(name="netxstudio::Parameter")
netxstudio_Protocol = Class(name="netxstudio::Protocol")
netxstudio_Company = Class(name="netxstudio::Company")
netxstudio_Tolerance = Class(name="netxstudio::Tolerance")
netxstudio_Expression = Class(name="netxstudio::Expression")
netxstudio_User = Class(name="netxstudio::User")
netxstudio_Country = Class(name="netxstudio::Country")
netxstudio_Site = Class(name="netxstudio::Site")
netxstudio_Unit = Class(name="netxstudio::Unit")
netxstudio_RFSService = Class(name="netxstudio::RFSService")
netxstudio_Meta = Class(name="netxstudio::Meta")
netxstudio_Room = Class(name="netxstudio::Room")

# netxstudio_Library class attributes and methods
netxstudio_Library_description: Property = Property(name="description", type=StringType)
netxstudio_Library_name: Property = Property(name="name", type=StringType)
netxstudio_Library_version: Property = Property(name="version", type=StringType)
netxstudio_Library.attributes={netxstudio_Library_description, netxstudio_Library_version, netxstudio_Library_name}

# netxstudio_Network class attributes and methods

# netxstudio_Function class attributes and methods

# netxstudio_Equipment class attributes and methods

# netxstudio_Metric class attributes and methods

# netxstudio_Parameter class attributes and methods

# netxstudio_Protocol class attributes and methods

# netxstudio_Company class attributes and methods

# netxstudio_Tolerance class attributes and methods

# netxstudio_Expression class attributes and methods

# netxstudio_User class attributes and methods

# netxstudio_Country class attributes and methods

# netxstudio_Site class attributes and methods

# netxstudio_Unit class attributes and methods

# netxstudio_RFSService class attributes and methods

# netxstudio_Meta class attributes and methods

# netxstudio_Room class attributes and methods

# Relationships
networks0: BinaryAssociation = BinaryAssociation(
    name="networks0",
    ends={
        Property(name="netxstudio_Network", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library", type=netxstudio_Network, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functions1: BinaryAssociation = BinaryAssociation(
    name="functions1",
    ends={
        Property(name="netxstudio_Function", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library2", type=netxstudio_Function, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
equipments3: BinaryAssociation = BinaryAssociation(
    name="equipments3",
    ends={
        Property(name="netxstudio_Equipment", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library4", type=netxstudio_Equipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metrics5: BinaryAssociation = BinaryAssociation(
    name="metrics5",
    ends={
        Property(name="netxstudio_Metric", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library6", type=netxstudio_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
protocols9: BinaryAssociation = BinaryAssociation(
    name="protocols9",
    ends={
        Property(name="netxstudio_Protocol", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library10", type=netxstudio_Protocol, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
companies11: BinaryAssociation = BinaryAssociation(
    name="companies11",
    ends={
        Property(name="netxstudio_Company", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library12", type=netxstudio_Company, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tolerances13: BinaryAssociation = BinaryAssociation(
    name="tolerances13",
    ends={
        Property(name="netxstudio_Tolerance", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library14", type=netxstudio_Tolerance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressions15: BinaryAssociation = BinaryAssociation(
    name="expressions15",
    ends={
        Property(name="netxstudio_Expression", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library16", type=netxstudio_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
users17: BinaryAssociation = BinaryAssociation(
    name="users17",
    ends={
        Property(name="netxstudio_User", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library18", type=netxstudio_User, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters7: BinaryAssociation = BinaryAssociation(
    name="parameters7",
    ends={
        Property(name="netxstudio_Parameter", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library8", type=netxstudio_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
countries21: BinaryAssociation = BinaryAssociation(
    name="countries21",
    ends={
        Property(name="netxstudio_Country", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library22", type=netxstudio_Country, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sites23: BinaryAssociation = BinaryAssociation(
    name="sites23",
    ends={
        Property(name="netxstudio_Site", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library24", type=netxstudio_Site, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
units25: BinaryAssociation = BinaryAssociation(
    name="units25",
    ends={
        Property(name="netxstudio_Unit", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library26", type=netxstudio_Unit, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services27: BinaryAssociation = BinaryAssociation(
    name="services27",
    ends={
        Property(name="netxstudio_RFSService", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library28", type=netxstudio_RFSService, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
versions29: BinaryAssociation = BinaryAssociation(
    name="versions29",
    ends={
        Property(name="netxstudio_Meta", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library30", type=netxstudio_Meta, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms19: BinaryAssociation = BinaryAssociation(
    name="rooms19",
    ends={
        Property(name="netxstudio_Room", type=netxstudio_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="netxstudio_Library20", type=netxstudio_Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="netxstudio",
    types={netxstudio_Library, netxstudio_Network, netxstudio_Function, netxstudio_Equipment, netxstudio_Metric, netxstudio_Parameter, netxstudio_Protocol, netxstudio_Company, netxstudio_Tolerance, netxstudio_Expression, netxstudio_User, netxstudio_Country, netxstudio_Site, netxstudio_Unit, netxstudio_RFSService, netxstudio_Meta, netxstudio_Room},
    associations={networks0, functions1, equipments3, metrics5, protocols9, companies11, tolerances13, expressions15, users17, parameters7, countries21, sites23, units25, services27, versions29, rooms19},
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