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
User = Class(name="User")
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
Property_ = Class(name="Property")

# User class attributes and methods
User_email: Property = Property(name="email", type=StringType)
User_location: Property = Property(name="location", type=StringType)
User.attributes={User_location, User_email}

# Reg_User class attributes and methods
Reg_User_username: Property = Property(name="username", type=StringType)
Reg_User_password: Property = Property(name="password", type=StringType)
Reg_User_Address: Property = Property(name="Address", type=StringType)
Reg_User.attributes={Reg_User_password, Reg_User_username, Reg_User_Address}

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
Payment.attributes={Payment_card_no, Payment_pay_id, Payment_pay_amount, Payment_ex_date, Payment_pay_mode}

# Requirement class attributes and methods
Requirement_requirement_type: Property = Property(name="requirement_type", type=StringType)
Requirement_req_description: Property = Property(name="req_description", type=StringType)
Requirement_requirement_location: Property = Property(name="requirement_location", type=StringType)
Requirement_user_id: Property = Property(name="user_id", type=StringType)
Requirement.attributes={Requirement_requirement_type, Requirement_req_description, Requirement_user_id, Requirement_requirement_location}

# Request class attributes and methods
Request_request_type: Property = Property(name="request_type", type=StringType)
Request_request_id: Property = Property(name="request_id", type=IntegerType)
Request_request_details: Property = Property(name="request_details", type=StringType)
Request_requser_id: Property = Property(name="requser_id", type=StringType)
Request.attributes={Request_request_details, Request_request_type, Request_requser_id, Request_request_id}

# Management class attributes and methods
Management_specialoffers: Property = Property(name="specialoffers", type=StringType)
Management_suggetions: Property = Property(name="suggetions", type=StringType)
Management.attributes={Management_specialoffers, Management_suggetions}

# Advertiesment class attributes and methods
Advertiesment_advertiesment_id: Property = Property(name="advertiesment_id", type=IntegerType)
Advertiesment_advertiser_id: Property = Property(name="advertiser_id", type=StringType)
Advertiesment_start_date: Property = Property(name="start_date", type=StringType)
Advertiesment_end_date: Property = Property(name="end_date", type=StringType)
Advertiesment.attributes={Advertiesment_advertiesment_id, Advertiesment_end_date, Advertiesment_advertiser_id, Advertiesment_start_date}

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__property_type, Property__property_id, Property__location, Property__address}

# Relationships
User_Administrator: BinaryAssociation = BinaryAssociation(
    name="User_Administrator",
    ends={
        Property(name="administrator0", type=Administrator, multiplicity=Multiplicity(1, 1)),
        Property(name="employee1", type=User, multiplicity=Multiplicity(1, 9999))
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
        Property(name="user7", type=User, multiplicity=Multiplicity(1, 1))
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
    name="_61c7714b_21bf_49cb_8fba_c19097cd3ee0",
    types={User, Reg_User, Unreg_User, Advertiser, Buyer, Seller, Administrator, Payment, Requirement, Request, Management, Advertiesment, Property_},
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