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
Actor = Class(name="Actor")
Listing = Class(name="Listing")
Apartment = Class(name="Apartment")
House = Class(name="House")
RealEstateAgent = Class(name="RealEstateAgent")
RegisteredUser = Class(name="RegisteredUser")
Administrator = Class(name="Administrator")

# Actor class attributes and methods
Actor_name: Property = Property(name="name", type=StringType)
Actor_username: Property = Property(name="username", type=StringType)
Actor_password: Property = Property(name="password", type=StringType)
Actor.attributes={Actor_username, Actor_password, Actor_name}

# Listing class attributes and methods
Listing_address: Property = Property(name="address", type=StringType)
Listing_numberOfBedroms: Property = Property(name="numberOfBedroms", type=IntegerType)
Listing_numberOfBathrooms: Property = Property(name="numberOfBathrooms", type=IntegerType)
Listing_kitchen: Property = Property(name="kitchen", type=IntegerType)
Listing_livingRooom: Property = Property(name="livingRooom", type=IntegerType)
Listing_furnished: Property = Property(name="furnished", type=BooleanType)
Listing_parkingPossibilities: Property = Property(name="parkingPossibilities", type=IntegerType)
Listing_image: Property = Property(name="image", type=StringType)
Listing_video: Property = Property(name="video", type=StringType)
Listing.attributes={Listing_parkingPossibilities, Listing_kitchen, Listing_numberOfBedroms, Listing_address, Listing_image, Listing_video, Listing_numberOfBathrooms, Listing_furnished, Listing_livingRooom}

# Apartment class attributes and methods
Apartment_size: Property = Property(name="size", type=IntegerType)
Apartment_lease: Property = Property(name="lease", type=IntegerType)
Apartment_securityDeposit: Property = Property(name="securityDeposit", type=IntegerType)
Apartment_monthlyRent: Property = Property(name="monthlyRent", type=IntegerType)
Apartment.attributes={Apartment_securityDeposit, Apartment_size, Apartment_monthlyRent, Apartment_lease}

# House class attributes and methods
House_numberOfFloors: Property = Property(name="numberOfFloors", type=IntegerType)
House_sizeOfProperty: Property = Property(name="sizeOfProperty", type=IntegerType)
House_price: Property = Property(name="price", type=IntegerType)
House_fees: Property = Property(name="fees", type=IntegerType)
House.attributes={House_numberOfFloors, House_sizeOfProperty, House_price, House_fees}

# RealEstateAgent class attributes and methods
RealEstateAgent_listings: Property = Property(name="listings", type=StringType)
RealEstateAgent.attributes={RealEstateAgent_listings}

# RegisteredUser class attributes and methods

# Administrator class attributes and methods

# Relationships
Actor_Listing: BinaryAssociation = BinaryAssociation(
    name="Actor_Listing",
    ends={
        Property(name="listing0", type=Listing, multiplicity=Multiplicity(0, 9999)),
        Property(name="actor1", type=Actor, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_30c0abe1_7254_458a_a3a8_21538f1d223b",
    types={Actor, Listing, Apartment, House, RealEstateAgent, RegisteredUser, Administrator},
    associations={Actor_Listing},
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