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
Admin = Class(name="Admin")
Customer = Class(name="Customer")
System_order = Class(name="System_order")
Payment = Class(name="Payment")
Bank = Class(name="Bank")
Cash_on_delievery = Class(name="Cash_on_delievery")
Food_Items = Class(name="Food_Items")
Category = Class(name="Category")

# User class attributes and methods
User_User_ID: Property = Property(name="User_ID", type=IntegerType)
User_User_Type: Property = Property(name="User_Type", type=StringType)
User_User_Name: Property = Property(name="User_Name", type=StringType)
User_User_Password: Property = Property(name="User_Password", type=StringType)
User.attributes={User_User_Password, User_User_Type, User_User_Name, User_User_ID}

# Admin class attributes and methods

# Customer class attributes and methods

# System_order class attributes and methods
System_order_Customer_ID: Property = Property(name="Customer_ID", type=IntegerType)
System_order_Customer_Name: Property = Property(name="Customer_Name", type=StringType)
System_order_Order_ID: Property = Property(name="Order_ID", type=IntegerType)
System_order_Date: Property = Property(name="Date", type=IntegerType)
System_order_Time: Property = Property(name="Time", type=IntegerType)
System_order_Delivery_Charges: Property = Property(name="Delivery_Charges", type=IntegerType)
System_order_Total: Property = Property(name="Total", type=IntegerType)
System_order_Payment_Option: Property = Property(name="Payment_Option", type=StringType)
System_order.attributes={System_order_Total, System_order_Customer_ID, System_order_Delivery_Charges, System_order_Payment_Option, System_order_Customer_Name, System_order_Time, System_order_Order_ID, System_order_Date}

# Payment class attributes and methods
Payment_Payment_Option: Property = Property(name="Payment_Option", type=StringType)
Payment_Amount: Property = Property(name="Amount", type=IntegerType)
Payment.attributes={Payment_Amount, Payment_Payment_Option}

# Bank class attributes and methods
Bank_Account_no: Property = Property(name="Account_no", type=IntegerType)
Bank_Account_type: Property = Property(name="Account_type", type=StringType)
Bank_Online_payment_ID_and_password: Property = Property(name="Online_payment_ID_and_password", type=StringType)
Bank.attributes={Bank_Account_no, Bank_Account_type, Bank_Online_payment_ID_and_password}

# Cash_on_delievery class attributes and methods
Cash_on_delievery_Customer_Name: Property = Property(name="Customer_Name", type=StringType)
Cash_on_delievery_Address: Property = Property(name="Address", type=StringType)
Cash_on_delievery_Phone_number: Property = Property(name="Phone_number", type=IntegerType)
Cash_on_delievery_Amount: Property = Property(name="Amount", type=StringType)
Cash_on_delievery.attributes={Cash_on_delievery_Amount, Cash_on_delievery_Phone_number, Cash_on_delievery_Customer_Name, Cash_on_delievery_Address}

# Food_Items class attributes and methods
Food_Items_Items_ID: Property = Property(name="Items_ID", type=IntegerType)
Food_Items_Item_Name: Property = Property(name="Item_Name", type=StringType)
Food_Items_Items_Manage: Property = Property(name="Items_Manage", type=Admin)
Food_Items_item_photo: Property = Property(name="item_photo", type=StringType)
Food_Items_Items_Price: Property = Property(name="Items_Price", type=IntegerType)
Food_Items_Items_Detail: Property = Property(name="Items_Detail", type=StringType)
Food_Items.attributes={Food_Items_Items_Detail, Food_Items_Items_Price, Food_Items_Items_ID, Food_Items_item_photo, Food_Items_Items_Manage, Food_Items_Item_Name}

# Category class attributes and methods
Category_ID: Property = Property(name="ID", type=IntegerType)
Category_Type: Property = Property(name="Type", type=StringType)
Category.attributes={Category_Type, Category_ID}

# Relationships
System_order_Payment: BinaryAssociation = BinaryAssociation(
    name="System_order_Payment",
    ends={
        Property(name="System_order_Payment_00", type=Payment, multiplicity=Multiplicity(1, 9999)),
        Property(name="System_order_Payment_11", type=System_order, multiplicity=Multiplicity(1, 9999))
    }
)
System_order_Customer: BinaryAssociation = BinaryAssociation(
    name="System_order_Customer",
    ends={
        Property(name="System_order_Customer_02", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="System_order_Customer_13", type=System_order, multiplicity=Multiplicity(0, 1))
    }
)
Food_Items_Category: BinaryAssociation = BinaryAssociation(
    name="Food_Items_Category",
    ends={
        Property(name="Food_Items_Category_04", type=Category, multiplicity=Multiplicity(1, 1)),
        Property(name="Food_Items_Category_15", type=Food_Items, multiplicity=Multiplicity(0, 9999))
    }
)
Admin_Food_Items: BinaryAssociation = BinaryAssociation(
    name="Admin_Food_Items",
    ends={
        Property(name="Admin_Food_Items_06", type=Food_Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="Admin_Food_Items_17", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Food_Items: BinaryAssociation = BinaryAssociation(
    name="Customer_Food_Items",
    ends={
        Property(name="food_Items8", type=Food_Items, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_CsPxQDt0EeqTDpmqRhKD9Q",
    types={User, Admin, Customer, System_order, Payment, Bank, Cash_on_delievery, Food_Items, Category},
    associations={System_order_Payment, System_order_Customer, Food_Items_Category, Admin_Food_Items, Customer_Food_Items},
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