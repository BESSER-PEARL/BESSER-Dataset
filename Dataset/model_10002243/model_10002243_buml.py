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
Customer_Actor = Class(name="Customer_Actor")
Add_To_Cart_UseCase = Class(name="Add_To_Cart_UseCase")
Place_Order_UseCase = Class(name="Place_Order_UseCase")
Rating_UseCase = Class(name="Rating_UseCase")
View_Order_Details_UseCase = Class(name="View_Order_Details_UseCase")
Track_Order_UseCase = Class(name="Track_Order_UseCase")
Make_Payment_UseCase = Class(name="Make_Payment_UseCase")
Sign_Up_UseCase = Class(name="Sign_Up_UseCase")
Login_UseCase = Class(name="Login_UseCase")
Cutomer = Class(name="Cutomer")
System_Order = Class(name="System_Order")
Payment = Class(name="Payment")
Wallet = Class(name="Wallet")
Cash_On_Delivery = Class(name="Cash_On_Delivery")

# Customer_Actor class attributes and methods

# Add_To_Cart_UseCase class attributes and methods

# Place_Order_UseCase class attributes and methods

# Rating_UseCase class attributes and methods

# View_Order_Details_UseCase class attributes and methods

# Track_Order_UseCase class attributes and methods

# Make_Payment_UseCase class attributes and methods

# Sign_Up_UseCase class attributes and methods

# Login_UseCase class attributes and methods

# Cutomer class attributes and methods

# System_Order class attributes and methods

# Payment class attributes and methods
Payment_Amount: Property = Property(name="Amount", type=IntegerType)
Payment.attributes={Payment_Amount}

# Wallet class attributes and methods

# Cash_On_Delivery class attributes and methods

# Relationships
Customer_Add_To_Cart: BinaryAssociation = BinaryAssociation(
    name="Customer_Add_To_Cart",
    ends={
        Property(name="add_To_Cart0", type=Add_To_Cart_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Place_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Place_Order",
    ends={
        Property(name="place_Order2", type=Place_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Rating: BinaryAssociation = BinaryAssociation(
    name="Customer_Rating",
    ends={
        Property(name="rating4", type=Rating_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_View_Order_Details: BinaryAssociation = BinaryAssociation(
    name="Customer_View_Order_Details",
    ends={
        Property(name="view_Order_Details6", type=View_Order_Details_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Track_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Track_Order",
    ends={
        Property(name="track_Order8", type=Track_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Make_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Make_Payment",
    ends={
        Property(name="make_Payment10", type=Make_Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer11", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Sign_Up: BinaryAssociation = BinaryAssociation(
    name="Customer_Sign_Up",
    ends={
        Property(name="sign_Up12", type=Sign_Up_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cutomer_System_Order: BinaryAssociation = BinaryAssociation(
    name="Cutomer_System_Order",
    ends={
        Property(name="Cutomer_System_Order_014", type=System_Order, multiplicity=Multiplicity(1, 1)),
        Property(name="Cutomer_System_Order_115", type=Cutomer, multiplicity=Multiplicity(1, 1))
    }
)
System_Order_Payment: BinaryAssociation = BinaryAssociation(
    name="System_Order_Payment",
    ends={
        Property(name="System_Order_Payment_016", type=Payment, multiplicity=Multiplicity(1, 1)),
        Property(name="System_Order_Payment_117", type=System_Order, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ytgKYJ4nEemddr62D2Sizg",
    types={Customer_Actor, Add_To_Cart_UseCase, Place_Order_UseCase, Rating_UseCase, View_Order_Details_UseCase, Track_Order_UseCase, Make_Payment_UseCase, Sign_Up_UseCase, Login_UseCase, Cutomer, System_Order, Payment, Wallet, Cash_On_Delivery},
    associations={Customer_Add_To_Cart, Customer_Place_Order, Customer_Rating, Customer_View_Order_Details, Customer_Track_Order, Customer_Make_Payment, Customer_Sign_Up, Cutomer_System_Order, System_Order_Payment},
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