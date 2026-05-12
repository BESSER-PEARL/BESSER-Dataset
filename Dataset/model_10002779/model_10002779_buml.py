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
Manager = Class(name="Manager")
Tenant = Class(name="Tenant")
Owner = Class(name="Owner")
Administrator = Class(name="Administrator")
Payment = Class(name="Payment")
Requirement = Class(name="Requirement")
Request = Class(name="Request")
Management = Class(name="Management")
Buildings = Class(name="Buildings")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__address, Property__property_id, Property__property_type, Property__location}

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

# Manager class attributes and methods
Manager_manager_id: Property = Property(name="manager_id", type=StringType)
Manager_management_id: Property = Property(name="management_id", type=StringType)
Manager.attributes={Manager_management_id, Manager_manager_id}

# Tenant class attributes and methods
Tenant_tenant_id: Property = Property(name="tenant_id", type=StringType)
Tenant.attributes={Tenant_tenant_id}

# Owner class attributes and methods
Owner_owner_id: Property = Property(name="owner_id", type=StringType)
Owner_property_id: Property = Property(name="property_id", type=StringType)
Owner.attributes={Owner_owner_id, Owner_property_id}

# Administrator class attributes and methods
Administrator_admin_name: Property = Property(name="admin_name", type=StringType)
Administrator_password: Property = Property(name="password", type=StringType)
Administrator.attributes={Administrator_password, Administrator_admin_name}

# Payment class attributes and methods
Payment_pay_id: Property = Property(name="pay_id", type=IntegerType)
Payment_pay_mode: Property = Property(name="pay_mode", type=StringType)
Payment_card_no: Property = Property(name="card_no", type=StringType)
Payment_ex_date: Property = Property(name="ex_date", type=StringType)
Payment_pay_amount: Property = Property(name="pay_amount", type=StringType)
Payment.attributes={Payment_card_no, Payment_pay_amount, Payment_pay_id, Payment_pay_mode, Payment_ex_date}

# Requirement class attributes and methods
Requirement_user_id: Property = Property(name="user_id", type=StringType)
Requirement_requirement_type: Property = Property(name="requirement_type", type=StringType)
Requirement_req_description: Property = Property(name="req_description", type=StringType)
Requirement_requirement_location: Property = Property(name="requirement_location", type=StringType)
Requirement.attributes={Requirement_requirement_type, Requirement_user_id, Requirement_requirement_location, Requirement_req_description}

# Request class attributes and methods
Request_request_type: Property = Property(name="request_type", type=StringType)
Request_request_id: Property = Property(name="request_id", type=IntegerType)
Request_request_details: Property = Property(name="request_details", type=StringType)
Request_requser_id: Property = Property(name="requser_id", type=StringType)
Request.attributes={Request_request_details, Request_request_id, Request_request_type, Request_requser_id}

# Management class attributes and methods
Management_specialoffers: Property = Property(name="specialoffers", type=StringType)
Management_suggetions: Property = Property(name="suggetions", type=StringType)
Management.attributes={Management_suggetions, Management_specialoffers}

# Buildings class attributes and methods
Buildings_management_id: Property = Property(name="management_id", type=IntegerType)
Buildings_manager_id: Property = Property(name="manager_id", type=StringType)
Buildings_start_date: Property = Property(name="start_date", type=StringType)
Buildings_end_date: Property = Property(name="end_date", type=StringType)
Buildings.attributes={Buildings_management_id, Buildings_start_date, Buildings_end_date, Buildings_manager_id}

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
        Property(name="adds2", type=Buildings, multiplicity=Multiplicity(0, 9999)),
        Property(name="owner3", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)
Property_Seller: BinaryAssociation = BinaryAssociation(
    name="Property_Seller",
    ends={
        Property(name="owner4", type=Owner, multiplicity=Multiplicity(1, 1)),
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
        Property(name="user8", type=Tenant, multiplicity=Multiplicity(1, 1)),
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
    name="d922418c_b09b_46cc_b0da_bbbe6883c037",
    types={Property_, User, Reg_User, Unreg_User, Manager, Tenant, Owner, Administrator, Payment, Requirement, Request, Management, Buildings},
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