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
Users = Class(name="Users")
Reg_User = Class(name="Reg_User")
Unreg_User = Class(name="Unreg_User")
Advertiser = Class(name="Advertiser")
Buyer = Class(name="Buyer")
Seller = Class(name="Seller")
Administrator = Class(name="Administrator")
Payment = Class(name="Payment")
Requirement = Class(name="Requirement")
Request = Class(name="Request")
Management = Class(name="Management")
Advertiesment = Class(name="Advertiesment")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__property_id, Property__property_type, Property__location, Property__address}

# Users class attributes and methods
Users_role_id: Property = Property(name="role_id", type=StringType)
Users_name: Property = Property(name="name", type=StringType)
Users.attributes={Users_name, Users_role_id}

# Reg_User class attributes and methods
Reg_User_username: Property = Property(name="username", type=StringType)
Reg_User_password: Property = Property(name="password", type=StringType)
Reg_User_Address: Property = Property(name="Address", type=StringType)
Reg_User.attributes={Reg_User_password, Reg_User_Address, Reg_User_username}

# Unreg_User class attributes and methods

# Advertiser class attributes and methods
Advertiser_advertiser_id: Property = Property(name="advertiser_id", type=StringType)
Advertiser_advertiesment_id: Property = Property(name="advertiesment_id", type=StringType)
Advertiser.attributes={Advertiser_advertiser_id, Advertiser_advertiesment_id}

# Buyer class attributes and methods
Buyer_buyer_id: Property = Property(name="buyer_id", type=StringType)
Buyer.attributes={Buyer_buyer_id}

# Seller class attributes and methods
Seller_seller_id: Property = Property(name="seller_id", type=StringType)
Seller_property_id: Property = Property(name="property_id", type=StringType)
Seller.attributes={Seller_property_id, Seller_seller_id}

# Administrator class attributes and methods
Administrator_admin_name: Property = Property(name="admin_name", type=StringType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_admin_name, Administrator_password}

# Payment class attributes and methods
Payment_pay_id: Property = Property(name="pay_id", type=IntegerType)
Payment_pay_mode: Property = Property(name="pay_mode", type=StringType)
Payment_card_no: Property = Property(name="card_no", type=StringType)
Payment_ex_date: Property = Property(name="ex_date", type=StringType)
Payment_pay_amount: Property = Property(name="pay_amount", type=StringType)
Payment.attributes={Payment_ex_date, Payment_pay_id, Payment_pay_mode, Payment_pay_amount, Payment_card_no}

# Requirement class attributes and methods
Requirement_requirement_location: Property = Property(name="requirement_location", type=StringType)
Requirement_user_id: Property = Property(name="user_id", type=StringType)
Requirement_requirement_type: Property = Property(name="requirement_type", type=StringType)
Requirement_req_description: Property = Property(name="req_description", type=StringType)
Requirement.attributes={Requirement_requirement_location, Requirement_user_id, Requirement_req_description, Requirement_requirement_type}

# Request class attributes and methods
Request_request_type: Property = Property(name="request_type", type=StringType)
Request_request_id: Property = Property(name="request_id", type=IntegerType)
Request_request_details: Property = Property(name="request_details", type=StringType)
Request_requser_id: Property = Property(name="requser_id", type=StringType)
Request.attributes={Request_request_details, Request_request_id, Request_requser_id, Request_request_type}

# Management class attributes and methods
Management_specialoffers: Property = Property(name="specialoffers", type=StringType)
Management_suggetions: Property = Property(name="suggetions", type=StringType)
Management.attributes={Management_suggetions, Management_specialoffers}

# Advertiesment class attributes and methods
Advertiesment_advertiesment_id: Property = Property(name="advertiesment_id", type=IntegerType)
Advertiesment_advertiser_id: Property = Property(name="advertiser_id", type=StringType)
Advertiesment_start_date: Property = Property(name="start_date", type=StringType)
Advertiesment_end_date: Property = Property(name="end_date", type=StringType)
Advertiesment.attributes={Advertiesment_end_date, Advertiesment_advertiesment_id, Advertiesment_advertiser_id, Advertiesment_start_date}

# Relationships
User_Administrator: BinaryAssociation = BinaryAssociation(
    name="User_Administrator",
    ends={
        Property(name="administrator0", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="employee1", type=Users, multiplicity=Multiplicity(1, 9999))
    }
)
Advertiser_Advertiesment: BinaryAssociation = BinaryAssociation(
    name="Advertiser_Advertiesment",
    ends={
        Property(name="adds2", type=Advertiesment, multiplicity=Multiplicity(0, 9999)),
        Property(name="owner3", type=Advertiser, multiplicity=Multiplicity(1, 1))
    }
)
Property_Seller: BinaryAssociation = BinaryAssociation(
    name="Property_Seller",
    ends={
        Property(name="owner4", type=Seller, multiplicity=Multiplicity(1, 1)),
        Property(name="property5", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
User_Request: BinaryAssociation = BinaryAssociation(
    name="User_Request",
    ends={
        Property(name="request6", type=Request, multiplicity=Multiplicity(0, 9999)),
        Property(name="user7", type=Users, multiplicity=Multiplicity(1, 1))
    }
)
Property_Buyer: BinaryAssociation = BinaryAssociation(
    name="Property_Buyer",
    ends={
        Property(name="user8", type=Buyer, multiplicity=Multiplicity(1, 1)),
        Property(name="property9", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
Reg_User_Requirement: BinaryAssociation = BinaryAssociation(
    name="Reg_User_Requirement",
    ends={
        Property(name="requirement10", type=Requirement, multiplicity=Multiplicity(0, 9999)),
        Property(name="user11", type=Reg_User, multiplicity=Multiplicity(1, 9999))
    }
)
Property_Management: BinaryAssociation = BinaryAssociation(
    name="Property_Management",
    ends={
        Property(name="management12", type=Management, multiplicity=Multiplicity(0, 9999)),
        Property(name="property13", type=Property_, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Reg_User: BinaryAssociation = BinaryAssociation(
    name="Payment_Reg_User",
    ends={
        Property(name="reg_User14", type=Reg_User, multiplicity=Multiplicity(1, 9999)),
        Property(name="payment15", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)
Payment_Property: BinaryAssociation = BinaryAssociation(
    name="Payment_Property",
    ends={
        Property(name="property16", type=Property_, multiplicity=Multiplicity(0, 9999)),
        Property(name="payment17", type=Payment, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="d171fde1_9d81_494b_900b_0d4f5f84fda9",
    types={Property_, Users, Reg_User, Unreg_User, Advertiser, Buyer, Seller, Administrator, Payment, Requirement, Request, Management, Advertiesment},
    associations={User_Administrator, Advertiser_Advertiesment, Property_Seller, User_Request, Property_Buyer, Reg_User_Requirement, Property_Management, Payment_Reg_User, Payment_Property},
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