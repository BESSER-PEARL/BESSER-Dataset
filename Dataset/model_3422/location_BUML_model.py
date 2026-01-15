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
AltitudeMode: Enumeration = Enumeration(
    name="AltitudeMode",
    literals={
            EnumerationLiteral(name="absolute"),
			EnumerationLiteral(name="clampToGround"),
			EnumerationLiteral(name="relativeToGround")
    }
)

# Classes
location_Location = Class(name="location::Location")
location_Area = Class(name="location::Area")

# location_Location class attributes and methods
location_Location_name: Property = Property(name="name", type=StringType)
location_Location_description: Property = Property(name="description", type=StringType)
location_Location_phoneNumber: Property = Property(name="phoneNumber", type=StringType)
location_Location_street: Property = Property(name="street", type=StringType)
location_Location_city: Property = Property(name="city", type=StringType)
location_Location_state: Property = Property(name="state", type=StringType)
location_Location_postalCode: Property = Property(name="postalCode", type=StringType)
location_Location_country: Property = Property(name="country", type=StringType)
location_Location_longitude: Property = Property(name="longitude", type=FloatType)
location_Location_latitude: Property = Property(name="latitude", type=FloatType)
location_Location_altitude: Property = Property(name="altitude", type=FloatType)
location_Location_altitudeMode: Property = Property(name="altitudeMode", type=StringType)
location_Location_comments: Property = Property(name="comments", type=StringType)
location_Location_m_getCoordinates: Method = Method(name="getCoordinates", parameters={}, type=StringType)
location_Location_m_getAddress: Method = Method(name="getAddress", parameters={}, type=StringType)
location_Location_m_containsPoint: Method = Method(name="containsPoint", parameters={Parameter(name='point')}, type=BooleanType)
location_Location_m_locate: Method = Method(name="locate", parameters={Parameter(name='point')}, type=StringType)
location_Location.attributes={location_Location_country, location_Location_longitude, location_Location_phoneNumber, location_Location_altitude, location_Location_name, location_Location_state, location_Location_city, location_Location_postalCode, location_Location_latitude, location_Location_description, location_Location_comments, location_Location_street, location_Location_altitudeMode}
location_Location.methods={location_Location_m_getCoordinates, location_Location_m_containsPoint, location_Location_m_getAddress, location_Location_m_locate}

# location_Area class attributes and methods
location_Area_name: Property = Property(name="name", type=StringType)
location_Area_boundary: Property = Property(name="boundary", type=StringType)
location_Area_comments: Property = Property(name="comments", type=StringType)
location_Area_m_getAreaMeasurement: Method = Method(name="getAreaMeasurement", parameters={}, type=FloatType)
location_Area_m_containsPoint: Method = Method(name="containsPoint", parameters={Parameter(name='point')}, type=BooleanType)
location_Area.attributes={location_Area_boundary, location_Area_comments, location_Area_name}
location_Area.methods={location_Area_m_containsPoint, location_Area_m_getAreaMeasurement}

# Relationships
areas0: BinaryAssociation = BinaryAssociation(
    name="areas0",
    ends={
        Property(name="location_Area", type=location_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="location_Location", type=location_Area, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="location",
    types={location_Location, location_Area, AltitudeMode},
    associations={areas0},
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