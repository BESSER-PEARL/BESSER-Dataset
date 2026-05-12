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
Enumeration_: Enumeration = Enumeration(
    name="Enumeration",
    literals={
            
    }
)

Enumeration2: Enumeration = Enumeration(
    name="Enumeration2",
    literals={
            
    }
)

# Classes
Category = Class(name="Category")
Location = Class(name="Location")
Place = Class(name="Place")
PlaceDetail = Class(name="PlaceDetail")
MyClass2 = Class(name="MyClass2")
LocationConnector_Interface = Class(name="LocationConnector_Interface")
DistanceInfo = Class(name="DistanceInfo")
MyClass = Class(name="MyClass")
MyClass3 = Class(name="MyClass3")
LocationManager = Class(name="LocationManager")

# Category class attributes and methods
Category_Type: Property = Property(name="Type", type=StringType)
Category_Name: Property = Property(name="Name", type=StringType)
Category_Id: Property = Property(name="Id", type=IntegerType)
Category.attributes={Category_Name, Category_Id, Category_Type}

# Location class attributes and methods
Location_Latitude: Property = Property(name="Latitude", type=StringType)
Location_Longitude: Property = Property(name="Longitude", type=StringType)
Location.attributes={Location_Longitude, Location_Latitude}

# Place class attributes and methods
Place_Name: Property = Property(name="Name", type=StringType)
Place_Details: Property = Property(name="Details", type=StringType)
Place.attributes={Place_Details, Place_Name}

# PlaceDetail class attributes and methods
PlaceDetail_DistanceInfo: Property = Property(name="DistanceInfo", type=DistanceInfo)
PlaceDetail_Category: Property = Property(name="Category", type=Category)
PlaceDetail.attributes={PlaceDetail_Category, PlaceDetail_DistanceInfo}

# MyClass2 class attributes and methods

# LocationConnector_Interface class attributes and methods

# DistanceInfo class attributes and methods
DistanceInfo_Distaince: Property = Property(name="Distaince", type=StringType)
DistanceInfo_ShortestPath: Property = Property(name="ShortestPath", type=StringType)
DistanceInfo_TraficInfo: Property = Property(name="TraficInfo", type=StringType)
DistanceInfo.attributes={DistanceInfo_Distaince, DistanceInfo_TraficInfo, DistanceInfo_ShortestPath}

# MyClass class attributes and methods

# MyClass3 class attributes and methods

# LocationManager class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_nhSEkGhPEeiTTuxWefFgMg",
    types={Category, Location, Place, PlaceDetail, MyClass2, LocationConnector_Interface, DistanceInfo, MyClass, MyClass3, LocationManager, Enumeration_, Enumeration2},
    associations={},
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