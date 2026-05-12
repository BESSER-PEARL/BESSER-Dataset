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
Class_ = Class(name="Class")
Registered_User_Actor = Class(name="Registered_User_Actor")
Login_UseCase = Class(name="Login_UseCase")
non_Registered_Actor = Class(name="non_Registered_Actor")
Register_Login_UseCase = Class(name="Register_Login_UseCase")
UseCase_UseCase = Class(name="UseCase_UseCase")
Order_Online_UseCase = Class(name="Order_Online_UseCase")
Delivery_UseCase = Class(name="Delivery_UseCase")
Collection_UseCase = Class(name="Collection_UseCase")
UseCase2_UseCase = Class(name="UseCase2_UseCase")
UseCase3_UseCase = Class(name="UseCase3_UseCase")
login_for_SavedInfo_UseCase = Class(name="login_for_SavedInfo_UseCase")
mobile_pinCode_UseCase = Class(name="mobile_pinCode_UseCase")
address_info_deliverypage_UseCase = Class(name="address_info_deliverypage_UseCase")
Menu_UseCase = Class(name="Menu_UseCase")
Select_Items_UseCase = Class(name="Select_Items_UseCase")
Edit_cart__address_info_UseCase = Class(name="Edit_cart__address_info_UseCase")
Checkout_UseCase = Class(name="Checkout_UseCase")
payment_UseCase = Class(name="payment_UseCase")
cash_UseCase = Class(name="cash_UseCase")
card_UseCase = Class(name="card_UseCase")
Terms_policies_UseCase = Class(name="Terms_policies_UseCase")
PayPal_UseCase = Class(name="PayPal_UseCase")
Voucher_Loyalty_Code_UseCase = Class(name="Voucher_Loyalty_Code_UseCase")
Actor_Actor = Class(name="Actor_Actor")
User_Information_UseCase = Class(name="User_Information_UseCase")

# Class class attributes and methods
Class__attribute: Property = Property(name="attribute", type=StringType)
Class_.attributes={Class__attribute}

# Registered_User_Actor class attributes and methods

# Login_UseCase class attributes and methods

# non_Registered_Actor class attributes and methods

# Register_Login_UseCase class attributes and methods

# UseCase_UseCase class attributes and methods

# Order_Online_UseCase class attributes and methods

# Delivery_UseCase class attributes and methods

# Collection_UseCase class attributes and methods

# UseCase2_UseCase class attributes and methods

# UseCase3_UseCase class attributes and methods

# login_for_SavedInfo_UseCase class attributes and methods

# mobile_pinCode_UseCase class attributes and methods

# address_info_deliverypage_UseCase class attributes and methods

# Menu_UseCase class attributes and methods

# Select_Items_UseCase class attributes and methods

# Edit_cart__address_info_UseCase class attributes and methods

# Checkout_UseCase class attributes and methods

# payment_UseCase class attributes and methods

# cash_UseCase class attributes and methods

# card_UseCase class attributes and methods

# Terms_policies_UseCase class attributes and methods

# PayPal_UseCase class attributes and methods

# Voucher_Loyalty_Code_UseCase class attributes and methods

# Actor_Actor class attributes and methods

# User_Information_UseCase class attributes and methods

# Relationships
Actor_Login: BinaryAssociation = BinaryAssociation(
    name="Actor_Login",
    ends={
        Property(name="actor0", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login1", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
non_user_Register: BinaryAssociation = BinaryAssociation(
    name="non_user_Register",
    ends={
        Property(name="non_user2", type=non_Registered_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="register3", type=Register_Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
non_user_Order_Online: BinaryAssociation = BinaryAssociation(
    name="non_user_Order_Online",
    ends={
        Property(name="non_user4", type=non_Registered_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="order_Online5", type=Order_Online_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Order_Online_login_for_SavedInfo: BinaryAssociation = BinaryAssociation(
    name="Order_Online_login_for_SavedInfo",
    ends={
        Property(name="order_Online6", type=Order_Online_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="login_for_SavedInfo7", type=login_for_SavedInfo_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Order_Online: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Order_Online",
    ends={
        Property(name="registered_User8", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="order_Online9", type=Order_Online_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Order_Online2: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Order_Online2",
    ends={
        Property(name="registered_User10", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="order_Online11", type=Order_Online_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_address_info_deliverypage: BinaryAssociation = BinaryAssociation(
    name="Delivery_address_info_deliverypage",
    ends={
        Property(name="delivery12", type=Delivery_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="address_info_deliverypage13", type=address_info_deliverypage_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Register_Login: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Register_Login",
    ends={
        Property(name="registered_User14", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="register_Login15", type=Register_Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Delivery: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Delivery",
    ends={
        Property(name="registered_User16", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery17", type=Delivery_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Registered_User_Collection: BinaryAssociation = BinaryAssociation(
    name="Registered_User_Collection",
    ends={
        Property(name="registered_User18", type=Registered_User_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="collection19", type=Collection_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_GhkqEIXQEeqgBLhX7Ryhyw",
    types={Class_, Registered_User_Actor, Login_UseCase, non_Registered_Actor, Register_Login_UseCase, UseCase_UseCase, Order_Online_UseCase, Delivery_UseCase, Collection_UseCase, UseCase2_UseCase, UseCase3_UseCase, login_for_SavedInfo_UseCase, mobile_pinCode_UseCase, address_info_deliverypage_UseCase, Menu_UseCase, Select_Items_UseCase, Edit_cart__address_info_UseCase, Checkout_UseCase, payment_UseCase, cash_UseCase, card_UseCase, Terms_policies_UseCase, PayPal_UseCase, Voucher_Loyalty_Code_UseCase, Actor_Actor, User_Information_UseCase},
    associations={Actor_Login, non_user_Register, non_user_Order_Online, Order_Online_login_for_SavedInfo, Registered_User_Order_Online, Registered_User_Order_Online2, Delivery_address_info_deliverypage, Registered_User_Register_Login, Registered_User_Delivery, Registered_User_Collection},
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