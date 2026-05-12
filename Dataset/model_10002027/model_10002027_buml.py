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
Order = Class(name="Order")
Store = Class(name="Store")
Furnace = Class(name="Furnace")
Dishwasher = Class(name="Dishwasher")
KitchenRange = Class(name="KitchenRange")
ClothesDryer = Class(name="ClothesDryer")
Fridge = Class(name="Fridge")
ClothesWasher = Class(name="ClothesWasher")
BackOrder = Class(name="BackOrder")
OrderList = Class(name="OrderList")
Appliance = Class(name="Appliance")
Customer = Class(name="Customer")

# Order class attributes and methods
Order_appliance: Property = Property(name="appliance", type=Appliance)
Order_customer: Property = Property(name="customer", type=Customer)
Order.attributes={Order_appliance, Order_customer}

# Store class attributes and methods
Store_inventory: Property = Property(name="inventory", type=StringType)
Store_customers: Property = Property(name="customers", type=StringType)
Store_orders: Property = Property(name="orders", type=StringType)
Store_sales: Property = Property(name="sales", type=StringType)
Store.attributes={Store_customers, Store_inventory, Store_sales, Store_orders}

# Furnace class attributes and methods
Furnace_maximumHeatOutput: Property = Property(name="maximumHeatOutput", type=StringType)
Furnace.attributes={Furnace_maximumHeatOutput}

# Dishwasher class attributes and methods

# KitchenRange class attributes and methods

# ClothesDryer class attributes and methods
ClothesDryer_repairPlan: Property = Property(name="repairPlan", type=StringType)
ClothesDryer.attributes={ClothesDryer_repairPlan}

# Fridge class attributes and methods
Fridge_capacity: Property = Property(name="capacity", type=StringType)
Fridge.attributes={Fridge_capacity}

# ClothesWasher class attributes and methods
ClothesWasher_repairPlan: Property = Property(name="repairPlan", type=StringType)
ClothesWasher.attributes={ClothesWasher_repairPlan}

# BackOrder class attributes and methods
BackOrder_backOrderList: Property = Property(name="backOrderList", type=Order)
BackOrder.attributes={BackOrder_backOrderList}

# OrderList class attributes and methods
OrderList_orderList: Property = Property(name="orderList", type=Order)
OrderList.attributes={OrderList_orderList}

# Appliance class attributes and methods
Appliance_Price: Property = Property(name="Price", type=StringType)
Appliance_Brand: Property = Property(name="Brand", type=StringType)
Appliance_Model: Property = Property(name="Model", type=StringType)
Appliance_Stock: Property = Property(name="Stock", type=IntegerType)
Appliance.attributes={Appliance_Model, Appliance_Price, Appliance_Brand, Appliance_Stock}

# Customer class attributes and methods
Customer_phoneNumber: Property = Property(name="phoneNumber", type=IntegerType)
Customer_name: Property = Property(name="name", type=StringType)
Customer_customerID: Property = Property(name="customerID", type=IntegerType)
Customer.attributes={Customer_name, Customer_customerID, Customer_phoneNumber}

# Relationships
Store_BackOrder: BinaryAssociation = BinaryAssociation(
    name="Store_BackOrder",
    ends={
        Property(name="backOrder0", type=BackOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="store1", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_OrderList: BinaryAssociation = BinaryAssociation(
    name="Store_OrderList",
    ends={
        Property(name="orderList2", type=OrderList, multiplicity=Multiplicity(1, 1)),
        Property(name="store3", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Store: BinaryAssociation = BinaryAssociation(
    name="Customer_Store",
    ends={
        Property(name="store4", type=Store, multiplicity=Multiplicity(1, 1)),
        Property(name="customer5", type=Customer, multiplicity=Multiplicity(0, 9999))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="order6", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer27", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Store_Appliance: BinaryAssociation = BinaryAssociation(
    name="Store_Appliance",
    ends={
        Property(name="appliance8", type=Appliance, multiplicity=Multiplicity(0, 9999)),
        Property(name="store9", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Store_Order: BinaryAssociation = BinaryAssociation(
    name="Store_Order",
    ends={
        Property(name="order10", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="store11", type=Store, multiplicity=Multiplicity(1, 1))
    }
)
Order_Appliance: BinaryAssociation = BinaryAssociation(
    name="Order_Appliance",
    ends={
        Property(name="appliance212", type=Appliance, multiplicity=Multiplicity(0, 9999)),
        Property(name="order13", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Order_OrderList: BinaryAssociation = BinaryAssociation(
    name="Order_OrderList",
    ends={
        Property(name="orderList14", type=OrderList, multiplicity=Multiplicity(1, 1)),
        Property(name="order15", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_BackOrder: BinaryAssociation = BinaryAssociation(
    name="Order_BackOrder",
    ends={
        Property(name="backOrder16", type=BackOrder, multiplicity=Multiplicity(1, 1)),
        Property(name="order17", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kVVbINpMEeiJYbNjsZ3wUw",
    types={Order, Store, Furnace, Dishwasher, KitchenRange, ClothesDryer, Fridge, ClothesWasher, BackOrder, OrderList, Appliance, Customer},
    associations={Store_BackOrder, Store_OrderList, Customer_Store, Customer_Order, Store_Appliance, Store_Order, Order_Appliance, Order_OrderList, Order_BackOrder},
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