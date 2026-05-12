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
Advertiser = Class(name="Advertiser")
Buyer = Class(name="Buyer")
Seller = Class(name="Seller")
Administrator = Class(name="Administrator")
Payment = Class(name="Payment")
Requirement = Class(name="Requirement")
Request = Class(name="Request")
Management = Class(name="Management")
Advertiesment = Class(name="Advertiesment")
Buyer_Actor = Class(name="Buyer_Actor")
Login_UseCase = Class(name="Login_UseCase")
Forgot_Password_UseCase = Class(name="Forgot_Password_UseCase")
Username__Password_UseCase = Class(name="Username__Password_UseCase")
Registration_UseCase = Class(name="Registration_UseCase")
Search_Property_UseCase = Class(name="Search_Property_UseCase")
State_UseCase = Class(name="State_UseCase")
Price_UseCase = Class(name="Price_UseCase")
City_UseCase = Class(name="City_UseCase")
Liked_Property_UseCase = Class(name="Liked_Property_UseCase")
Add_property_to_whishlist_UseCase = Class(name="Add_property_to_whishlist_UseCase")
Sales_Team_Actor = Class(name="Sales_Team_Actor")
Buyer_Component = Class(name="Buyer_Component")
View_the_Buyers_List_UseCase = Class(name="View_the_Buyers_List_UseCase")
Meeting_With_the_Clent_UseCase = Class(name="Meeting_With_the_Clent_UseCase")
Owner_Agent_Other_Actor = Class(name="Owner_Agent_Other_Actor")
Owener_Agent_Component = Class(name="Owener_Agent_Component")
Seller_UseCase = Class(name="Seller_UseCase")
Seller_Component = Class(name="Seller_Component")
Registartion_external = Class(name="Registartion_external")
Manage_Property_external = Class(name="Manage_Property_external")
Login_external = Class(name="Login_external")
View_All_Posted_Properties_external = Class(name="View_All_Posted_Properties_external")
Logout_external = Class(name="Logout_external")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__property_type, Property__location, Property__address, Property__property_id}

# User class attributes and methods
User_email: Property = Property(name="email", type=StringType)
User_location: Property = Property(name="location", type=StringType)
User.attributes={User_location, User_email}

# Reg_User class attributes and methods
Reg_User_username: Property = Property(name="username", type=StringType)
Reg_User_password: Property = Property(name="password", type=StringType)
Reg_User_Address: Property = Property(name="Address", type=StringType)
Reg_User.attributes={Reg_User_username, Reg_User_Address, Reg_User_password}

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
Seller.attributes={Seller_seller_id, Seller_property_id}

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
Payment.attributes={Payment_pay_mode, Payment_pay_id, Payment_pay_amount, Payment_card_no, Payment_ex_date}

# Requirement class attributes and methods
Requirement_requirement_type: Property = Property(name="requirement_type", type=StringType)
Requirement_req_description: Property = Property(name="req_description", type=StringType)
Requirement_requirement_location: Property = Property(name="requirement_location", type=StringType)
Requirement_user_id: Property = Property(name="user_id", type=StringType)
Requirement.attributes={Requirement_user_id, Requirement_req_description, Requirement_requirement_location, Requirement_requirement_type}

# Request class attributes and methods
Request_request_type: Property = Property(name="request_type", type=StringType)
Request_request_id: Property = Property(name="request_id", type=IntegerType)
Request_request_details: Property = Property(name="request_details", type=StringType)
Request_requser_id: Property = Property(name="requser_id", type=StringType)
Request.attributes={Request_request_id, Request_request_type, Request_requser_id, Request_request_details}

# Management class attributes and methods
Management_specialoffers: Property = Property(name="specialoffers", type=StringType)
Management_suggetions: Property = Property(name="suggetions", type=StringType)
Management.attributes={Management_suggetions, Management_specialoffers}

# Advertiesment class attributes and methods
Advertiesment_end_date: Property = Property(name="end_date", type=StringType)
Advertiesment_advertiesment_id: Property = Property(name="advertiesment_id", type=IntegerType)
Advertiesment_advertiser_id: Property = Property(name="advertiser_id", type=StringType)
Advertiesment_start_date: Property = Property(name="start_date", type=StringType)
Advertiesment.attributes={Advertiesment_advertiser_id, Advertiesment_end_date, Advertiesment_start_date, Advertiesment_advertiesment_id}

# Buyer_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Forgot_Password_UseCase class attributes and methods

# Username__Password_UseCase class attributes and methods

# Registration_UseCase class attributes and methods

# Search_Property_UseCase class attributes and methods

# State_UseCase class attributes and methods

# Price_UseCase class attributes and methods

# City_UseCase class attributes and methods

# Liked_Property_UseCase class attributes and methods

# Add_property_to_whishlist_UseCase class attributes and methods

# Sales_Team_Actor class attributes and methods

# Buyer_Component class attributes and methods

# View_the_Buyers_List_UseCase class attributes and methods

# Meeting_With_the_Clent_UseCase class attributes and methods

# Owner_Agent_Other_Actor class attributes and methods

# Owener_Agent_Component class attributes and methods

# Seller_UseCase class attributes and methods

# Seller_Component class attributes and methods

# Registartion_external class attributes and methods

# Manage_Property_external class attributes and methods

# Login_external class attributes and methods

# View_All_Posted_Properties_external class attributes and methods

# Logout_external class attributes and methods

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
Buyer_Login: BinaryAssociation = BinaryAssociation(
    name="Buyer_Login",
    ends={
        Property(name="login18", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="buyer19", type=Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Buyer_Search_Property: BinaryAssociation = BinaryAssociation(
    name="Buyer_Search_Property",
    ends={
        Property(name="search_Property20", type=Search_Property_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="buyer21", type=Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_Login: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_Login",
    ends={
        Property(name="login22", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team23", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_View_the_Buyers_List: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_View_the_Buyers_List",
    ends={
        Property(name="view_the_Buyers_List24", type=View_the_Buyers_List_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team25", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_Meeting_With_the_Clent: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_Meeting_With_the_Clent",
    ends={
        Property(name="meeting_With_the_Clent26", type=Meeting_With_the_Clent_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team27", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Owner_Agent_Registartion: BinaryAssociation = BinaryAssociation(
    name="Owner_Agent_Registartion",
    ends={
        Property(name="registartion28", type=Registartion_external, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_Agent29", type=Owner_Agent_Other_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Owner_Agent_Manage_Property: BinaryAssociation = BinaryAssociation(
    name="Owner_Agent_Manage_Property",
    ends={
        Property(name="manage_Property30", type=Manage_Property_external, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_Agent31", type=Owner_Agent_Other_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Owner_Agent_Login: BinaryAssociation = BinaryAssociation(
    name="Owner_Agent_Login",
    ends={
        Property(name="login32", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_Agent33", type=Owner_Agent_Other_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Owner_Agent_View_All_Posted_Properties: BinaryAssociation = BinaryAssociation(
    name="Owner_Agent_View_All_Posted_Properties",
    ends={
        Property(name="view_All_Posted_Properties34", type=View_All_Posted_Properties_external, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_Agent35", type=Owner_Agent_Other_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Owner_Agent_Logout: BinaryAssociation = BinaryAssociation(
    name="Owner_Agent_Logout",
    ends={
        Property(name="logout36", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="owner_Agent37", type=Owner_Agent_Other_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="dffa3802_e3d2_46e9_81a9_3e81073e524d",
    types={Property_, User, Reg_User, Unreg_User, Advertiser, Buyer, Seller, Administrator, Payment, Requirement, Request, Management, Advertiesment, Buyer_Actor, Login_UseCase, Forgot_Password_UseCase, Username__Password_UseCase, Registration_UseCase, Search_Property_UseCase, State_UseCase, Price_UseCase, City_UseCase, Liked_Property_UseCase, Add_property_to_whishlist_UseCase, Sales_Team_Actor, Buyer_Component, View_the_Buyers_List_UseCase, Meeting_With_the_Clent_UseCase, Owner_Agent_Other_Actor, Owener_Agent_Component, Seller_UseCase, Seller_Component, Registartion_external, Manage_Property_external, Login_external, View_All_Posted_Properties_external, Logout_external},
    associations={User_Administrator, Advertiser_Advertiesment, Property_Seller, User_Request, Property_Buyer, Reg_User_Requirement, Property_Management, Payment_Reg_User, Payment_Property, Buyer_Login, Buyer_Search_Property, Sales_Team_Login, Sales_Team_View_the_Buyers_List, Sales_Team_Meeting_With_the_Clent, Owner_Agent_Registartion, Owner_Agent_Manage_Property, Owner_Agent_Login, Owner_Agent_View_All_Posted_Properties, Owner_Agent_Logout},
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