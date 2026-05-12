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
Transactions = Class(name="Transactions")
Order = Class(name="Order")
Terminal = Class(name="Terminal")
Online_Portal = Class(name="Online_Portal")
Product = Class(name="Product")
Service = Class(name="Service")
Store = Class(name="Store")
Manager = Class(name="Manager")
Employee = Class(name="Employee")
Customer = Class(name="Customer")
Inventory = Class(name="Inventory")
Customer_Data = Class(name="Customer_Data")

# Transactions class attributes and methods
Transactions_Customer: Property = Property(name="Customer", type=StringType)
Transactions_Order: Property = Property(name="Order", type=StringType)
Transactions.attributes={Transactions_Customer, Transactions_Order}

# Order class attributes and methods
Order_Product: Property = Property(name="Product", type=StringType)
Order_Service: Property = Property(name="Service", type=StringType)
Order.attributes={Order_Service, Order_Product}

# Terminal class attributes and methods
Terminal_Current_Employee: Property = Property(name="Current_Employee", type=StringType)
Terminal.attributes={Terminal_Current_Employee}

# Online_Portal class attributes and methods
Online_Portal_StoreLocation: Property = Property(name="StoreLocation", type=StringType)
Online_Portal.attributes={Online_Portal_StoreLocation}

# Product class attributes and methods
Product_Company: Property = Property(name="Company", type=StringType)
Product.attributes={Product_Company}

# Service class attributes and methods
Service_Terms: Property = Property(name="Terms", type=StringType)
Service_Info: Property = Property(name="Info", type=StringType)
Service.attributes={Service_Info, Service_Terms}

# Store class attributes and methods

# Manager class attributes and methods

# Employee class attributes and methods

# Customer class attributes and methods

# Inventory class attributes and methods
Inventory_Products: Property = Property(name="Products", type=StringType)
Inventory_Services: Property = Property(name="Services", type=StringType)
Inventory.attributes={Inventory_Services, Inventory_Products}

# Customer_Data class attributes and methods
Customer_Data_Name: Property = Property(name="Name", type=StringType)
Customer_Data_Contact: Property = Property(name="Contact", type=StringType)
Customer_Data.attributes={Customer_Data_Contact, Customer_Data_Name}

# Relationships
Store_Manager: BinaryAssociation = BinaryAssociation(
    name="Store_Manager",
    ends={
        Property(name="manager0", type=Manager, multiplicity=Multiplicity(1, 1)),
        Property(name="store1", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_Employee: BinaryAssociation = BinaryAssociation(
    name="Store_Employee",
    ends={
        Property(name="employee2", type=Employee, multiplicity=Multiplicity(1, 9999)),
        Property(name="store3", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_Customer: BinaryAssociation = BinaryAssociation(
    name="Store_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="store5", type=Store, multiplicity=Multiplicity(0, 1))
    }
)
Store_Inventory: BinaryAssociation = BinaryAssociation(
    name="Store_Inventory",
    ends={
        Property(name="inventory6", type=Inventory, multiplicity=Multiplicity(1, 1)),
        Property(name="store7", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_Transactions: BinaryAssociation = BinaryAssociation(
    name="Store_Transactions",
    ends={
        Property(name="transactions8", type=Transactions, multiplicity=Multiplicity(1, 1)),
        Property(name="store9", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_Customer_Data: BinaryAssociation = BinaryAssociation(
    name="Store_Customer_Data",
    ends={
        Property(name="customer_Data10", type=Customer_Data, multiplicity=Multiplicity(1, 1)),
        Property(name="store11", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Customer_Data: BinaryAssociation = BinaryAssociation(
    name="Customer_Customer_Data",
    ends={
        Property(name="customer_Data12", type=Customer_Data, multiplicity=Multiplicity(0, 1)),
        Property(name="customer13", type=Customer, multiplicity=Multiplicity(1, 9999))
    }
)
Customer_Data_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Data_Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="customer_Data15", type=Customer_Data, multiplicity=Multiplicity(0, 9999))
    }
)
Transactions_Order: BinaryAssociation = BinaryAssociation(
    name="Transactions_Order",
    ends={
        Property(name="order16", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="transactions17", type=Transactions, multiplicity=Multiplicity(1, 1))
    }
)
Terminal_Inventory: BinaryAssociation = BinaryAssociation(
    name="Terminal_Inventory",
    ends={
        Property(name="inventory18", type=Inventory, multiplicity=Multiplicity(0, 9999)),
        Property(name="terminal19", type=Terminal, multiplicity=Multiplicity(0, 9999))
    }
)
Terminal_Transactions: BinaryAssociation = BinaryAssociation(
    name="Terminal_Transactions",
    ends={
        Property(name="transactions20", type=Transactions, multiplicity=Multiplicity(0, 9999)),
        Property(name="terminal21", type=Terminal, multiplicity=Multiplicity(0, 9999))
    }
)
Terminal_Customer_Data: BinaryAssociation = BinaryAssociation(
    name="Terminal_Customer_Data",
    ends={
        Property(name="customer_Data22", type=Customer_Data, multiplicity=Multiplicity(0, 9999)),
        Property(name="terminal23", type=Terminal, multiplicity=Multiplicity(0, 9999))
    }
)
Employee_Terminal: BinaryAssociation = BinaryAssociation(
    name="Employee_Terminal",
    ends={
        Property(name="terminal24", type=Terminal, multiplicity=Multiplicity(0, 9999)),
        Property(name="employee25", type=Employee, multiplicity=Multiplicity(0, 9999))
    }
)
Manager_Terminal: BinaryAssociation = BinaryAssociation(
    name="Manager_Terminal",
    ends={
        Property(name="terminal26", type=Terminal, multiplicity=Multiplicity(0, 9999)),
        Property(name="manager27", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Employee: BinaryAssociation = BinaryAssociation(
    name="Customer_Employee",
    ends={
        Property(name="employee28", type=Employee, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer29", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Manager: BinaryAssociation = BinaryAssociation(
    name="Customer_Manager",
    ends={
        Property(name="manager30", type=Manager, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer31", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
Online_Portal_Inventory: BinaryAssociation = BinaryAssociation(
    name="Online_Portal_Inventory",
    ends={
        Property(name="inventory32", type=Inventory, multiplicity=Multiplicity(0, 1)),
        Property(name="online_Portal33", type=Online_Portal, multiplicity=Multiplicity(1, 1))
    }
)
Online_Portal_Transactions: BinaryAssociation = BinaryAssociation(
    name="Online_Portal_Transactions",
    ends={
        Property(name="transactions34", type=Transactions, multiplicity=Multiplicity(0, 1)),
        Property(name="online_Portal35", type=Online_Portal, multiplicity=Multiplicity(1, 1))
    }
)
Online_Portal_Customer_Data: BinaryAssociation = BinaryAssociation(
    name="Online_Portal_Customer_Data",
    ends={
        Property(name="customer_Data36", type=Customer_Data, multiplicity=Multiplicity(0, 1)),
        Property(name="online_Portal37", type=Online_Portal, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Online_Portal: BinaryAssociation = BinaryAssociation(
    name="Customer_Online_Portal",
    ends={
        Property(name="online_Portal38", type=Online_Portal, multiplicity=Multiplicity(1, 1)),
        Property(name="customer39", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
Store_Product: BinaryAssociation = BinaryAssociation(
    name="Store_Product",
    ends={
        Property(name="product40", type=Product, multiplicity=Multiplicity(0, 9999)),
        Property(name="store41", type=Store, multiplicity=Multiplicity(0, 9999))
    }
)
Store_Service: BinaryAssociation = BinaryAssociation(
    name="Store_Service",
    ends={
        Property(name="service42", type=Service, multiplicity=Multiplicity(0, 9999)),
        Property(name="store43", type=Store, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_OW3KcEkJEeie_NQr4yovPw",
    types={Transactions, Order, Terminal, Online_Portal, Product, Service, Store, Manager, Employee, Customer, Inventory, Customer_Data},
    associations={Store_Manager, Store_Employee, Store_Customer, Store_Inventory, Store_Transactions, Store_Customer_Data, Customer_Customer_Data, Customer_Data_Order, Transactions_Order, Terminal_Inventory, Terminal_Transactions, Terminal_Customer_Data, Employee_Terminal, Manager_Terminal, Customer_Employee, Customer_Manager, Online_Portal_Inventory, Online_Portal_Transactions, Online_Portal_Customer_Data, Customer_Online_Portal, Store_Product, Store_Service},
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