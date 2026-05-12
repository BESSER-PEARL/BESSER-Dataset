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
Property_ = Class(name="Property")
User = Class(name="User")
Reg_User = Class(name="Reg_User")
Unreg_User = Class(name="Unreg_User")
Buyer = Class(name="Buyer")
Seller = Class(name="Seller")
Administrator = Class(name="Administrator")
Requirement = Class(name="Requirement")
Request = Class(name="Request")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__address, Property__location, Property__property_id, Property__property_type}

# User class attributes and methods
User_email: Property = Property(name="email", type=StringType)
User_location: Property = Property(name="location", type=StringType)
User.attributes={User_location, User_email}

# Reg_User class attributes and methods
Reg_User_username: Property = Property(name="username", type=StringType)
Reg_User_password: Property = Property(name="password", type=StringType)
Reg_User_Address: Property = Property(name="Address", type=StringType)
Reg_User.attributes={Reg_User_password, Reg_User_Address, Reg_User_username}

# Unreg_User class attributes and methods

# Buyer class attributes and methods
Buyer_buyer_id: Property = Property(name="buyer_id", type=StringType)
Buyer.attributes={Buyer_buyer_id}

# Seller class attributes and methods
Seller_seller_id: Property = Property(name="seller_id", type=StringType)
Seller_property_id: Property = Property(name="property_id", type=StringType)
Seller.attributes={Seller_seller_id, Seller_property_id}

# Administrator class attributes and methods
Administrator_admin_name: Property = Property(name="admin_name", type=StringType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_password, Administrator_admin_name}

# Requirement class attributes and methods
Requirement_requirement_type: Property = Property(name="requirement_type", type=StringType)
Requirement_req_description: Property = Property(name="req_description", type=StringType)
Requirement_requirement_location: Property = Property(name="requirement_location", type=StringType)
Requirement_user_id: Property = Property(name="user_id", type=StringType)
Requirement.attributes={Requirement_req_description, Requirement_requirement_type, Requirement_user_id, Requirement_requirement_location}

# Request class attributes and methods
Request_request_type: Property = Property(name="request_type", type=StringType)
Request_request_id: Property = Property(name="request_id", type=IntegerType)
Request_request_details: Property = Property(name="request_details", type=StringType)
Request_requser_id: Property = Property(name="requser_id", type=StringType)
Request.attributes={Request_request_details, Request_request_id, Request_request_type, Request_requser_id}

# Relationships
User_Administrator: BinaryAssociation = BinaryAssociation(
    name="User_Administrator",
    ends={
        Property(name="administrator0", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="employee1", type=User, multiplicity=Multiplicity(1, 9999))
    }
)
Property_Seller: BinaryAssociation = BinaryAssociation(
    name="Property_Seller",
    ends={
        Property(name="owner2", type=Seller, multiplicity=Multiplicity(1, 1)),
        Property(name="property3", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
User_Request: BinaryAssociation = BinaryAssociation(
    name="User_Request",
    ends={
        Property(name="request4", type=Request, multiplicity=Multiplicity(0, 9999)),
        Property(name="user5", type=User, multiplicity=Multiplicity(1, 1))
    }
)
Property_Buyer: BinaryAssociation = BinaryAssociation(
    name="Property_Buyer",
    ends={
        Property(name="user6", type=Buyer, multiplicity=Multiplicity(1, 1)),
        Property(name="property7", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
Reg_User_Requirement: BinaryAssociation = BinaryAssociation(
    name="Reg_User_Requirement",
    ends={
        Property(name="requirement8", type=Requirement, multiplicity=Multiplicity(0, 9999)),
        Property(name="user9", type=Reg_User, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_26c74990_1071_4c03_8079_de6988ede9c2",
    types={Property_, User, Reg_User, Unreg_User, Buyer, Seller, Administrator, Requirement, Request},
    associations={User_Administrator, Property_Seller, User_Request, Property_Buyer, Reg_User_Requirement},
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