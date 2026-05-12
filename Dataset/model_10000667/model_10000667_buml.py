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
Items = Class(name="Items")
Store = Class(name="Store")
Order = Class(name="Order")
Employee = Class(name="Employee")
Inventory = Class(name="Inventory")
Menu = Class(name="Menu")
PurchaseOrder = Class(name="PurchaseOrder")
Vendor = Class(name="Vendor")
Customer = Class(name="Customer")

# Items class attributes and methods
Items_ItemID: Property = Property(name="ItemID", type=IntegerType)
Items_Name: Property = Property(name="Name", type=StringType)
Items.attributes={Items_ItemID, Items_Name}

# Store class attributes and methods
Store_StoreID: Property = Property(name="StoreID", type=IntegerType)
Store_Address: Property = Property(name="Address", type=StringType)
Store_Name: Property = Property(name="Name", type=StringType)
Store.attributes={Store_Address, Store_Name, Store_StoreID}

# Order class attributes and methods
Order_CustNumber: Property = Property(name="CustNumber", type=IntegerType)
Order_OrderID: Property = Property(name="OrderID", type=IntegerType)
Order_MenuItem: Property = Property(name="MenuItem", type=IntegerType)
Order_ItemName: Property = Property(name="ItemName", type=StringType)
Order_OrderDate: Property = Property(name="OrderDate", type=DateType)
Order.attributes={Order_OrderID, Order_OrderDate, Order_CustNumber, Order_MenuItem, Order_ItemName}

# Employee class attributes and methods
Employee_EmployeeID: Property = Property(name="EmployeeID", type=IntegerType)
Employee_Role: Property = Property(name="Role", type=StringType)
Employee_StoreID: Property = Property(name="StoreID", type=IntegerType)
Employee_Salary: Property = Property(name="Salary", type=FloatType)
Employee.attributes={Employee_EmployeeID, Employee_Salary, Employee_StoreID, Employee_Role}

# Inventory class attributes and methods
Inventory_ItemID: Property = Property(name="ItemID", type=IntegerType)
Inventory_StoreID: Property = Property(name="StoreID", type=IntegerType)
Inventory_Quantity: Property = Property(name="Quantity", type=FloatType)
Inventory.attributes={Inventory_StoreID, Inventory_ItemID, Inventory_Quantity}

# Menu class attributes and methods
Menu_MenuItem: Property = Property(name="MenuItem", type=StringType)
Menu.attributes={Menu_MenuItem}

# PurchaseOrder class attributes and methods
PurchaseOrder_PurchaseOrderID: Property = Property(name="PurchaseOrderID", type=IntegerType)
PurchaseOrder_VendorID: Property = Property(name="VendorID", type=IntegerType)
PurchaseOrder_ItemID: Property = Property(name="ItemID", type=IntegerType)
PurchaseOrder_Quantity: Property = Property(name="Quantity", type=FloatType)
PurchaseOrder_Price: Property = Property(name="Price", type=FloatType)
PurchaseOrder_Date: Property = Property(name="Date", type=DateType)
PurchaseOrder.attributes={PurchaseOrder_Date, PurchaseOrder_ItemID, PurchaseOrder_PurchaseOrderID, PurchaseOrder_Price, PurchaseOrder_VendorID, PurchaseOrder_Quantity}

# Vendor class attributes and methods
Vendor_VendorID: Property = Property(name="VendorID", type=IntegerType)
Vendor_ItemID: Property = Property(name="ItemID", type=IntegerType)
Vendor_Address: Property = Property(name="Address", type=StringType)
Vendor.attributes={Vendor_Address, Vendor_VendorID, Vendor_ItemID}

# Customer class attributes and methods
Customer_CustNumber: Property = Property(name="CustNumber", type=IntegerType)
Customer.attributes={Customer_CustNumber}

# Relationships
Menu_Order: BinaryAssociation = BinaryAssociation(
    name="Menu_Order",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="menu1", type=Menu, multiplicity=Multiplicity(1, 9999))
    }
)
Inventory_Store: BinaryAssociation = BinaryAssociation(
    name="Inventory_Store",
    ends={
        Property(name="store2", type=Store, multiplicity=Multiplicity(1, 9999)),
        Property(name="inventory3", type=Inventory, multiplicity=Multiplicity(1, 1))
    }
)
Vendor_PurchaseOrder: BinaryAssociation = BinaryAssociation(
    name="Vendor_PurchaseOrder",
    ends={
        Property(name="purchaseOrder4", type=PurchaseOrder, multiplicity=Multiplicity(1, 9999)),
        Property(name="vendor5", type=Vendor, multiplicity=Multiplicity(1, 1))
    }
)
Menu_Items: BinaryAssociation = BinaryAssociation(
    name="Menu_Items",
    ends={
        Property(name="items6", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="menu7", type=Menu, multiplicity=Multiplicity(0, 1))
    }
)
Inventory_Items2: BinaryAssociation = BinaryAssociation(
    name="Inventory_Items2",
    ends={
        Property(name="items8", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="inventory9", type=Inventory, multiplicity=Multiplicity(0, 1))
    }
)
Store_Employee: BinaryAssociation = BinaryAssociation(
    name="Store_Employee",
    ends={
        Property(name="employee10", type=Employee, multiplicity=Multiplicity(1, 9999)),
        Property(name="store11", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
PurchaseOrder_Items: BinaryAssociation = BinaryAssociation(
    name="PurchaseOrder_Items",
    ends={
        Property(name="items12", type=Items, multiplicity=Multiplicity(1, 9999)),
        Property(name="purchaseOrder13", type=PurchaseOrder, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(1, 9999)),
        Property(name="customer15", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_5365954a_f37f_4268_9899_bfab48f3effc",
    types={Items, Store, Order, Employee, Inventory, Menu, PurchaseOrder, Vendor, Customer},
    associations={Menu_Order, Inventory_Store, Vendor_PurchaseOrder, Menu_Items, Inventory_Items2, Store_Employee, PurchaseOrder_Items, Customer_Order},
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