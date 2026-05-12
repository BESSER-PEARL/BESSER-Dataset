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
Rent = Class(name="Rent")
Buyer = Class(name="Buyer")
Seller = Class(name="Seller")
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
Supplier_Component = Class(name="Supplier_Component")
Landlord_Actor = Class(name="Landlord_Actor")
Broker_Actor = Class(name="Broker_Actor")
Demand_Component = Class(name="Demand_Component")
Tenants_Buyer_Actor = Class(name="Tenants_Buyer_Actor")
Cient_Relationship_Team_Actor = Class(name="Cient_Relationship_Team_Actor")
Clent_Realtionship_Team_Demand_Lead_Mgmt__Component = Class(name="Clent_Realtionship_Team_Demand_Lead_Mgmt__Component")
Clent_Relationship_Team_Actor = Class(name="Clent_Relationship_Team_Actor")
Supply_Lead_Management_Client_Relationship_Team__Component = Class(name="Supply_Lead_Management_Client_Relationship_Team__Component")
Client_Relationship_Team_Actor = Class(name="Client_Relationship_Team_Actor")
Property_Onbording__Component = Class(name="Property_Onbording__Component")
Client_Relationship_Team_Actor1 = Class(name="Client_Relationship_Team_Actor1")
Property1 = Class(name="Property1")
User1 = Class(name="User1")
Client_Relationship_Team = Class(name="Client_Relationship_Team")
Owner = Class(name="Owner")
Presales_team = Class(name="Presales_team")
ResidentialApartment = Class(name="ResidentialApartment")
IndependentHouse = Class(name="IndependentHouse")
Login_external = Class(name="Login_external")
Register_external = Class(name="Register_external")
Add_Property_external = Class(name="Add_Property_external")
Assign_Transaction_Type_external = Class(name="Assign_Transaction_Type_external")
Select_Homzhub_Service_external = Class(name="Select_Homzhub_Service_external")
Log_In_Interest_external = Class(name="Log_In_Interest_external")
Like_A_Property_external = Class(name="Like_A_Property_external")
Assign_Lead_to_Client_Relationship_Team_external = Class(name="Assign_Lead_to_Client_Relationship_Team_external")
Create_Property_Mgmt_Lead_external = Class(name="Create_Property_Mgmt_Lead_external")
Recieve_s_Lead_external = Class(name="Recieve_s_Lead_external")
Visit_Scheduled_external = Class(name="Visit_Scheduled_external")
Look_For_Supply_external = Class(name="Look_For_Supply_external")
Property_Onboarding___Readiness_external = Class(name="Property_Onboarding___Readiness_external")
HH_Service_Selected_external = Class(name="HH_Service_Selected_external")
Reacives_Lead_external = Class(name="Reacives_Lead_external")
Look_For_Tenants_external = Class(name="Look_For_Tenants_external")
Search_Property_external = Class(name="Search_Property_external")
Add_Property_Deatilas_external = Class(name="Add_Property_Deatilas_external")

# Property class attributes and methods
Property__property_id: Property = Property(name="property_id", type=StringType)
Property__property_type: Property = Property(name="property_type", type=StringType)
Property__address: Property = Property(name="address", type=StringType)
Property__location: Property = Property(name="location", type=StringType)
Property_.attributes={Property__location, Property__property_type, Property__property_id, Property__address}

# User class attributes and methods
User_email: Property = Property(name="email", type=StringType)
User_location: Property = Property(name="location", type=StringType)
User.attributes={User_email, User_location}

# Reg_User class attributes and methods
Reg_User_username: Property = Property(name="username", type=StringType)
Reg_User_password: Property = Property(name="password", type=StringType)
Reg_User_Address: Property = Property(name="Address", type=StringType)
Reg_User.attributes={Reg_User_username, Reg_User_Address, Reg_User_password}

# Unreg_User class attributes and methods

# Rent class attributes and methods
Rent_rent_id: Property = Property(name="rent_id", type=StringType)
Rent.attributes={Rent_rent_id}

# Buyer class attributes and methods
Buyer_buyer_id: Property = Property(name="buyer_id", type=StringType)
Buyer.attributes={Buyer_buyer_id}

# Seller class attributes and methods
Seller_seller_id: Property = Property(name="seller_id", type=StringType)
Seller_property_id: Property = Property(name="property_id", type=StringType)
Seller.attributes={Seller_property_id, Seller_seller_id}

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

# Supplier_Component class attributes and methods

# Landlord_Actor class attributes and methods

# Broker_Actor class attributes and methods

# Demand_Component class attributes and methods

# Tenants_Buyer_Actor class attributes and methods

# Cient_Relationship_Team_Actor class attributes and methods

# Clent_Realtionship_Team_Demand_Lead_Mgmt__Component class attributes and methods

# Clent_Relationship_Team_Actor class attributes and methods

# Supply_Lead_Management_Client_Relationship_Team__Component class attributes and methods

# Client_Relationship_Team_Actor class attributes and methods

# Property_Onbording__Component class attributes and methods

# Client_Relationship_Team_Actor1 class attributes and methods

# Property1 class attributes and methods
Property1_property_id: Property = Property(name="property_id", type=StringType)
Property1_property_type: Property = Property(name="property_type", type=StringType)
Property1_address: Property = Property(name="address", type=StringType)
Property1_location: Property = Property(name="location", type=StringType)
Property1.attributes={Property1_property_type, Property1_location, Property1_address, Property1_property_id}

# User1 class attributes and methods
User1_email: Property = Property(name="email", type=StringType)
User1_password: Property = Property(name="password", type=StringType)
User1.attributes={User1_email, User1_password}

# Client_Relationship_Team class attributes and methods
Client_Relationship_Team_username: Property = Property(name="username", type=StringType)
Client_Relationship_Team_password: Property = Property(name="password", type=StringType)
Client_Relationship_Team.attributes={Client_Relationship_Team_password, Client_Relationship_Team_username}

# Owner class attributes and methods
Owner_name: Property = Property(name="name", type=StringType)
Owner_Address: Property = Property(name="Address", type=StringType)
Owner.attributes={Owner_name, Owner_Address}

# Presales_team class attributes and methods
Presales_team_usename: Property = Property(name="usename", type=StringType)
Presales_team_password: Property = Property(name="password", type=StringType)
Presales_team.attributes={Presales_team_usename, Presales_team_password}

# ResidentialApartment class attributes and methods
ResidentialApartment_Size: Property = Property(name="Size", type=StringType)
ResidentialApartment_BEDROOMS: Property = Property(name="BEDROOMS", type=StringType)
ResidentialApartment_PARKING: Property = Property(name="PARKING", type=StringType)
ResidentialApartment_MAINTAINENCE: Property = Property(name="MAINTAINENCE", type=StringType)
ResidentialApartment_Price: Property = Property(name="Price", type=StringType)
ResidentialApartment.attributes={ResidentialApartment_PARKING, ResidentialApartment_BEDROOMS, ResidentialApartment_Price, ResidentialApartment_Size, ResidentialApartment_MAINTAINENCE}

# IndependentHouse class attributes and methods
IndependentHouse_Size: Property = Property(name="Size", type=StringType)
IndependentHouse_Bedroom: Property = Property(name="Bedroom", type=StringType)
IndependentHouse_Bathroom: Property = Property(name="Bathroom", type=StringType)
IndependentHouse_YardSpace: Property = Property(name="YardSpace", type=StringType)
IndependentHouse_Price: Property = Property(name="Price", type=StringType)
IndependentHouse.attributes={IndependentHouse_Size, IndependentHouse_Price, IndependentHouse_Bathroom, IndependentHouse_YardSpace, IndependentHouse_Bedroom}

# Login_external class attributes and methods

# Register_external class attributes and methods

# Add_Property_external class attributes and methods

# Assign_Transaction_Type_external class attributes and methods

# Select_Homzhub_Service_external class attributes and methods

# Log_In_Interest_external class attributes and methods

# Like_A_Property_external class attributes and methods

# Assign_Lead_to_Client_Relationship_Team_external class attributes and methods

# Create_Property_Mgmt_Lead_external class attributes and methods

# Recieve_s_Lead_external class attributes and methods

# Visit_Scheduled_external class attributes and methods

# Look_For_Supply_external class attributes and methods

# Property_Onboarding___Readiness_external class attributes and methods

# HH_Service_Selected_external class attributes and methods

# Reacives_Lead_external class attributes and methods

# Look_For_Tenants_external class attributes and methods

# Search_Property_external class attributes and methods

# Add_Property_Deatilas_external class attributes and methods

# Relationships
Client_Relationship_Team_Add_Property_Deatilas: BinaryAssociation = BinaryAssociation(
    name="Client_Relationship_Team_Add_Property_Deatilas",
    ends={
        Property(name="add_Property_Deatilas56", type=Add_Property_Deatilas_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_Relationship_Team57", type=Client_Relationship_Team_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Property_Seller: BinaryAssociation = BinaryAssociation(
    name="Property_Seller",
    ends={
        Property(name="owner0", type=Seller, multiplicity=Multiplicity(1, 1)),
        Property(name="property1", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
Property_Buyer: BinaryAssociation = BinaryAssociation(
    name="Property_Buyer",
    ends={
        Property(name="user2", type=Buyer, multiplicity=Multiplicity(1, 1)),
        Property(name="property3", type=Property_, multiplicity=Multiplicity(0, 9999))
    }
)
Buyer_Login: BinaryAssociation = BinaryAssociation(
    name="Buyer_Login",
    ends={
        Property(name="login4", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="buyer5", type=Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Buyer_Search_Property: BinaryAssociation = BinaryAssociation(
    name="Buyer_Search_Property",
    ends={
        Property(name="search_Property6", type=Search_Property_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="buyer7", type=Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_Login: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_Login",
    ends={
        Property(name="login8", type=Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team9", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_View_the_Buyers_List: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_View_the_Buyers_List",
    ends={
        Property(name="view_the_Buyers_List10", type=View_the_Buyers_List_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team11", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Sales_Team_Meeting_With_the_Clent: BinaryAssociation = BinaryAssociation(
    name="Sales_Team_Meeting_With_the_Clent",
    ends={
        Property(name="meeting_With_the_Clent12", type=Meeting_With_the_Clent_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="sales_Team13", type=Sales_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Landlord_________________________________________Supplier: BinaryAssociation = BinaryAssociation(
    name="Landlord_________________________________________Supplier",
    ends={
        Property(name="Supplier14", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="landlord15", type=Landlord_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Landlord_Register: BinaryAssociation = BinaryAssociation(
    name="Landlord_Register",
    ends={
        Property(name="register16", type=Register_external, multiplicity=Multiplicity(0, 1)),
        Property(name="landlord17", type=Landlord_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Landlord_Add_Property: BinaryAssociation = BinaryAssociation(
    name="Landlord_Add_Property",
    ends={
        Property(name="add_Property18", type=Add_Property_external, multiplicity=Multiplicity(0, 1)),
        Property(name="landlord19", type=Landlord_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Landlord_Broker: BinaryAssociation = BinaryAssociation(
    name="Landlord_Broker",
    ends={
        Property(name="broker20", type=Broker_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="landlord21", type=Landlord_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Landlord_Assign_Transaction_Type: BinaryAssociation = BinaryAssociation(
    name="Landlord_Assign_Transaction_Type",
    ends={
        Property(name="assign_Transaction_Type22", type=Assign_Transaction_Type_external, multiplicity=Multiplicity(0, 1)),
        Property(name="landlord23", type=Landlord_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Broker_Select_Homzhub_Service: BinaryAssociation = BinaryAssociation(
    name="Broker_Select_Homzhub_Service",
    ends={
        Property(name="select_Homzhub_Service24", type=Select_Homzhub_Service_external, multiplicity=Multiplicity(0, 1)),
        Property(name="broker25", type=Broker_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tenants_Buyer_Log_In_Interest: BinaryAssociation = BinaryAssociation(
    name="Tenants_Buyer_Log_In_Interest",
    ends={
        Property(name="log_In_Interest26", type=Log_In_Interest_external, multiplicity=Multiplicity(0, 1)),
        Property(name="tenants_Buyer27", type=Tenants_Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tenants_Buyer_Like_A_Property: BinaryAssociation = BinaryAssociation(
    name="Tenants_Buyer_Like_A_Property",
    ends={
        Property(name="like_A_Property28", type=Like_A_Property_external, multiplicity=Multiplicity(0, 1)),
        Property(name="tenants_Buyer29", type=Tenants_Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tenants_Buyer_Login: BinaryAssociation = BinaryAssociation(
    name="Tenants_Buyer_Login",
    ends={
        Property(name="login30", type=Login_external, multiplicity=Multiplicity(0, 1)),
        Property(name="tenants_Buyer31", type=Tenants_Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tenants_Buyer_Register: BinaryAssociation = BinaryAssociation(
    name="Tenants_Buyer_Register",
    ends={
        Property(name="register32", type=Register_external, multiplicity=Multiplicity(0, 1)),
        Property(name="tenants_Buyer33", type=Tenants_Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cient_Relationship_Team_Assign_Lead_to_Client_Relationship_Team: BinaryAssociation = BinaryAssociation(
    name="Cient_Relationship_Team_Assign_Lead_to_Client_Relationship_Team",
    ends={
        Property(name="assign_Lead_to_Client_Relationship_Team34", type=Assign_Lead_to_Client_Relationship_Team_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cient_Relationship_Team35", type=Cient_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cient_Relationship_Team_Assign_Transaction_Type: BinaryAssociation = BinaryAssociation(
    name="Cient_Relationship_Team_Assign_Transaction_Type",
    ends={
        Property(name="assign_Transaction_Type36", type=Assign_Transaction_Type_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cient_Relationship_Team37", type=Cient_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cient_Relationship_Team_Create_Property_Mgmt_Lead: BinaryAssociation = BinaryAssociation(
    name="Cient_Relationship_Team_Create_Property_Mgmt_Lead",
    ends={
        Property(name="create_Property_Mgmt_Lead38", type=Create_Property_Mgmt_Lead_external, multiplicity=Multiplicity(0, 1)),
        Property(name="cient_Relationship_Team39", type=Cient_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clent_Relationship_Team_Clent_Realtionship_Team_Demand_Lead_Mgmt_: BinaryAssociation = BinaryAssociation(
    name="Clent_Relationship_Team_Clent_Realtionship_Team_Demand_Lead_Mgmt_",
    ends={
        Property(name="clent_Realtionship_Team_Demand_Lead_Mgmt_40", type=Recieve_s_Lead_external, multiplicity=Multiplicity(0, 1)),
        Property(name="clent_Relationship_Team41", type=Clent_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clent_Relationship_Team_Visit_Scheduled: BinaryAssociation = BinaryAssociation(
    name="Clent_Relationship_Team_Visit_Scheduled",
    ends={
        Property(name="visit_Scheduled42", type=Visit_Scheduled_external, multiplicity=Multiplicity(0, 1)),
        Property(name="clent_Relationship_Team43", type=Clent_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Clent_Relationship_Team_Look_For_Supply: BinaryAssociation = BinaryAssociation(
    name="Clent_Relationship_Team_Look_For_Supply",
    ends={
        Property(name="look_For_Supply44", type=Look_For_Supply_external, multiplicity=Multiplicity(0, 1)),
        Property(name="clent_Relationship_Team45", type=Clent_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
HH_Service_Selected_Property_Onboarding___Readiness: BinaryAssociation = BinaryAssociation(
    name="HH_Service_Selected_Property_Onboarding___Readiness",
    ends={
        Property(name="property_Onboarding___Readiness46", type=Property_Onboarding___Readiness_external, multiplicity=Multiplicity(0, 1)),
        Property(name="hH_Service_Selected47", type=HH_Service_Selected_external, multiplicity=Multiplicity(0, 1))
    }
)
Client_Relationship_Team_Reacives_Lead: BinaryAssociation = BinaryAssociation(
    name="Client_Relationship_Team_Reacives_Lead",
    ends={
        Property(name="reacives_Lead48", type=Reacives_Lead_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_Relationship_Team49", type=Client_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_Relationship_Team_HH_Service_Selected: BinaryAssociation = BinaryAssociation(
    name="Client_Relationship_Team_HH_Service_Selected",
    ends={
        Property(name="hH_Service_Selected50", type=HH_Service_Selected_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_Relationship_Team51", type=Client_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Client_Relationship_Team_Look_For_Tenants: BinaryAssociation = BinaryAssociation(
    name="Client_Relationship_Team_Look_For_Tenants",
    ends={
        Property(name="look_For_Tenants52", type=Look_For_Tenants_external, multiplicity=Multiplicity(0, 1)),
        Property(name="client_Relationship_Team53", type=Client_Relationship_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tenants_Buyer_Search_Property: BinaryAssociation = BinaryAssociation(
    name="Tenants_Buyer_Search_Property",
    ends={
        Property(name="search_Property54", type=Search_Property_external, multiplicity=Multiplicity(0, 1)),
        Property(name="tenants_Buyer55", type=Tenants_Buyer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Property_Client_Relationship_Team: BinaryAssociation = BinaryAssociation(
    name="Property_Client_Relationship_Team",
    ends={
        Property(name="client_Relationship_Team58", type=Client_Relationship_Team, multiplicity=Multiplicity(0, 1)),
        Property(name="property59", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
Property_Owner: BinaryAssociation = BinaryAssociation(
    name="Property_Owner",
    ends={
        Property(name="owner60", type=Owner, multiplicity=Multiplicity(0, 1)),
        Property(name="property61", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)
Property_IndependentHouse: BinaryAssociation = BinaryAssociation(
    name="Property_IndependentHouse",
    ends={
        Property(name="Property_IndependentHouse_062", type=IndependentHouse, multiplicity=Multiplicity(0, 1)),
        Property(name="property63", type=Property_, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4b475496_6249_44df_bbbe_87a9dbdf1d59",
    types={Property_, User, Reg_User, Unreg_User, Rent, Buyer, Seller, Buyer_Actor, Login_UseCase, Forgot_Password_UseCase, Username__Password_UseCase, Registration_UseCase, Search_Property_UseCase, State_UseCase, Price_UseCase, City_UseCase, Liked_Property_UseCase, Add_property_to_whishlist_UseCase, Sales_Team_Actor, Buyer_Component, View_the_Buyers_List_UseCase, Meeting_With_the_Clent_UseCase, Supplier_Component, Landlord_Actor, Broker_Actor, Demand_Component, Tenants_Buyer_Actor, Cient_Relationship_Team_Actor, Clent_Realtionship_Team_Demand_Lead_Mgmt__Component, Clent_Relationship_Team_Actor, Supply_Lead_Management_Client_Relationship_Team__Component, Client_Relationship_Team_Actor, Property_Onbording__Component, Client_Relationship_Team_Actor1, Property1, User1, Client_Relationship_Team, Owner, Presales_team, ResidentialApartment, IndependentHouse, Login_external, Register_external, Add_Property_external, Assign_Transaction_Type_external, Select_Homzhub_Service_external, Log_In_Interest_external, Like_A_Property_external, Assign_Lead_to_Client_Relationship_Team_external, Create_Property_Mgmt_Lead_external, Recieve_s_Lead_external, Visit_Scheduled_external, Look_For_Supply_external, Property_Onboarding___Readiness_external, HH_Service_Selected_external, Reacives_Lead_external, Look_For_Tenants_external, Search_Property_external, Add_Property_Deatilas_external},
    associations={Client_Relationship_Team_Add_Property_Deatilas, Property_Seller, Property_Buyer, Buyer_Login, Buyer_Search_Property, Sales_Team_Login, Sales_Team_View_the_Buyers_List, Sales_Team_Meeting_With_the_Clent, Landlord_________________________________________Supplier, Landlord_Register, Landlord_Add_Property, Landlord_Broker, Landlord_Assign_Transaction_Type, Broker_Select_Homzhub_Service, Tenants_Buyer_Log_In_Interest, Tenants_Buyer_Like_A_Property, Tenants_Buyer_Login, Tenants_Buyer_Register, Cient_Relationship_Team_Assign_Lead_to_Client_Relationship_Team, Cient_Relationship_Team_Assign_Transaction_Type, Cient_Relationship_Team_Create_Property_Mgmt_Lead, Clent_Relationship_Team_Clent_Realtionship_Team_Demand_Lead_Mgmt_, Clent_Relationship_Team_Visit_Scheduled, Clent_Relationship_Team_Look_For_Supply, HH_Service_Selected_Property_Onboarding___Readiness, Client_Relationship_Team_Reacives_Lead, Client_Relationship_Team_HH_Service_Selected, Client_Relationship_Team_Look_For_Tenants, Tenants_Buyer_Search_Property, Property_Client_Relationship_Team, Property_Owner, Property_IndependentHouse},
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