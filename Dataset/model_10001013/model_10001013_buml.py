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
Customer = Class(name="Customer")
Order = Class(name="Order")
Item = Class(name="Item")
Customer_Actor = Class(name="Customer_Actor")
Manager_Actor = Class(name="Manager_Actor")
Login_UseCase = Class(name="Login_UseCase")
Manage_customer_accounts_UseCase = Class(name="Manage_customer_accounts_UseCase")
Update_Stock_UseCase = Class(name="Update_Stock_UseCase")
Place_Order_UseCase = Class(name="Place_Order_UseCase")
Manage_Orders_UseCase = Class(name="Manage_Orders_UseCase")
Generate_Reports_UseCase = Class(name="Generate_Reports_UseCase")
Update_Order_UseCase = Class(name="Update_Order_UseCase")
Register_UseCase = Class(name="Register_UseCase")
Special_order_UseCase = Class(name="Special_order_UseCase")
Stock = Class(name="Stock")
Manager = Class(name="Manager")
Customer1 = Class(name="Customer1")
Order1 = Class(name="Order1")
Item1 = Class(name="Item1")
Stock1 = Class(name="Stock1")
SpecialOrder = Class(name="SpecialOrder")
Manager1 = Class(name="Manager1")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_Customer_id: Property = Property(name="Customer_id", type=IntegerType)
Customer.attributes={Customer_Customer_id, Customer_name}

# Order class attributes and methods
Order_Order_id: Property = Property(name="Order_id", type=IntegerType)
Order_Cust_id: Property = Property(name="Cust_id", type=IntegerType)
Order.attributes={Order_Order_id, Order_Cust_id}

# Item class attributes and methods
Item_item_code: Property = Property(name="item_code", type=IntegerType)
Item_item_name: Property = Property(name="item_name", type=StringType)
Item.attributes={Item_item_name, Item_item_code}

# Customer_Actor class attributes and methods

# Manager_Actor class attributes and methods

# Login_UseCase class attributes and methods

# Manage_customer_accounts_UseCase class attributes and methods

# Update_Stock_UseCase class attributes and methods

# Place_Order_UseCase class attributes and methods

# Manage_Orders_UseCase class attributes and methods

# Generate_Reports_UseCase class attributes and methods

# Update_Order_UseCase class attributes and methods

# Register_UseCase class attributes and methods

# Special_order_UseCase class attributes and methods

# Stock class attributes and methods
Stock_items__: Property = Property(name="items__", type=Item)
Stock.attributes={Stock_items__}

# Manager class attributes and methods
Manager_name: Property = Property(name="name", type=StringType)
Manager.attributes={Manager_name}

# Customer1 class attributes and methods
Customer1_name: Property = Property(name="name", type=StringType)
Customer1_customerId: Property = Property(name="customerId", type=IntegerType)
Customer1_address: Property = Property(name="address", type=StringType)
Customer1_phone: Property = Property(name="phone", type=IntegerType)
Customer1.attributes={Customer1_phone, Customer1_name, Customer1_customerId, Customer1_address}

# Order1 class attributes and methods
Order1_orderId: Property = Property(name="orderId", type=IntegerType)
Order1_cust: Property = Property(name="cust", type=Customer_Actor)
Order1_orderDate: Property = Property(name="orderDate", type=StringType)
Order1_deliveryDate: Property = Property(name="deliveryDate", type=StringType)
Order1_totalAmount: Property = Property(name="totalAmount", type=FloatType)
Order1_conformationNo: Property = Property(name="conformationNo", type=IntegerType)
Order1.attributes={Order1_totalAmount, Order1_cust, Order1_conformationNo, Order1_orderId, Order1_orderDate, Order1_deliveryDate}

# Item1 class attributes and methods
Item1_itemCode: Property = Property(name="itemCode", type=IntegerType)
Item1_itemName: Property = Property(name="itemName", type=StringType)
Item1_itemCost: Property = Property(name="itemCost", type=FloatType)
Item1_itemCount: Property = Property(name="itemCount", type=StringType)
Item1.attributes={Item1_itemName, Item1_itemCount, Item1_itemCode, Item1_itemCost}

# Stock1 class attributes and methods
Stock1_items__: Property = Property(name="items__", type=Item)
Stock1.attributes={Stock1_items__}

# SpecialOrder class attributes and methods
SpecialOrder_orderRange: Property = Property(name="orderRange", type=IntegerType)
SpecialOrder_offerCode: Property = Property(name="offerCode", type=IntegerType)
SpecialOrder.attributes={SpecialOrder_orderRange, SpecialOrder_offerCode}

# Manager1 class attributes and methods
Manager1_id: Property = Property(name="id", type=StringType)
Manager1_name: Property = Property(name="name", type=StringType)
Manager1.attributes={Manager1_id, Manager1_name}

# Relationships
Manage_Orders_Manager: BinaryAssociation = BinaryAssociation(
    name="Manage_Orders_Manager",
    ends={
        Property(name="manager10", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Orders11", type=Manage_Orders_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Generate_Reports_Manager: BinaryAssociation = BinaryAssociation(
    name="Generate_Reports_Manager",
    ends={
        Property(name="manager12", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="generate_Reports13", type=Generate_Reports_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Update_Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Update_Order_Customer",
    ends={
        Property(name="customer14", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Order15", type=Update_Order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Update_Order_Manager: BinaryAssociation = BinaryAssociation(
    name="Update_Order_Manager",
    ends={
        Property(name="manager16", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_Order17", type=Update_Order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Login: BinaryAssociation = BinaryAssociation(
    name="Customer_Login",
    ends={
        Property(name="login18", type=Register_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer19", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Order",
    ends={
        Property(name="Customer_Order_00", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="Customer_Order_11", type=Customer, multiplicity=Multiplicity(1, 1))
    }
)
Manage_customer_accounts_Manager: BinaryAssociation = BinaryAssociation(
    name="Manage_customer_accounts_Manager",
    ends={
        Property(name="manager2", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_customer_accounts3", type=Manage_customer_accounts_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Register_Customer: BinaryAssociation = BinaryAssociation(
    name="Register_Customer",
    ends={
        Property(name="customer4", type=Customer_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="register5", type=Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manage_Stock_Manager: BinaryAssociation = BinaryAssociation(
    name="Manage_Stock_Manager",
    ends={
        Property(name="manager6", type=Manager_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Stock7", type=Update_Stock_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Place_Order: BinaryAssociation = BinaryAssociation(
    name="Customer_Place_Order",
    ends={
        Property(name="place_Order8", type=Place_Order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer9", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Item_Stock: BinaryAssociation = BinaryAssociation(
    name="Item_Stock",
    ends={
        Property(name="stock20", type=Stock, multiplicity=Multiplicity(1, 1)),
        Property(name="item21", type=Item, multiplicity=Multiplicity(0, 9999))
    }
)
Manager_Order: BinaryAssociation = BinaryAssociation(
    name="Manager_Order",
    ends={
        Property(name="order22", type=Order, multiplicity=Multiplicity(0, 9999)),
        Property(name="manager23", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)
Manager_Stock: BinaryAssociation = BinaryAssociation(
    name="Manager_Stock",
    ends={
        Property(name="stock24", type=Stock, multiplicity=Multiplicity(0, 9999)),
        Property(name="manager25", type=Manager, multiplicity=Multiplicity(1, 1))
    }
)
Customer_Order2: BinaryAssociation = BinaryAssociation(
    name="Customer_Order2",
    ends={
        Property(name="order26", type=Order1, multiplicity=Multiplicity(0, 9999)),
        Property(name="customer27", type=Customer1, multiplicity=Multiplicity(1, 1))
    }
)
Item_Stock2: BinaryAssociation = BinaryAssociation(
    name="Item_Stock2",
    ends={
        Property(name="stock28", type=Stock1, multiplicity=Multiplicity(1, 1)),
        Property(name="item29", type=Item1, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Item: BinaryAssociation = BinaryAssociation(
    name="Order_Item",
    ends={
        Property(name="item30", type=Item, multiplicity=Multiplicity(0, 9999)),
        Property(name="order31", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Stock_Manager: BinaryAssociation = BinaryAssociation(
    name="Stock_Manager",
    ends={
        Property(name="manager32", type=Manager1, multiplicity=Multiplicity(1, 1)),
        Property(name="stock33", type=Stock1, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Manager: BinaryAssociation = BinaryAssociation(
    name="Order_Manager",
    ends={
        Property(name="manager34", type=Manager1, multiplicity=Multiplicity(1, 1)),
        Property(name="order35", type=Order1, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_7b0fc0a3_9d4e_4cf2_b6de_f685d668b04e",
    types={Customer, Order, Item, Customer_Actor, Manager_Actor, Login_UseCase, Manage_customer_accounts_UseCase, Update_Stock_UseCase, Place_Order_UseCase, Manage_Orders_UseCase, Generate_Reports_UseCase, Update_Order_UseCase, Register_UseCase, Special_order_UseCase, Stock, Manager, Customer1, Order1, Item1, Stock1, SpecialOrder, Manager1},
    associations={Manage_Orders_Manager, Generate_Reports_Manager, Update_Order_Customer, Update_Order_Manager, Customer_Login, Customer_Order, Manage_customer_accounts_Manager, Register_Customer, Manage_Stock_Manager, Customer_Place_Order, Item_Stock, Manager_Order, Manager_Stock, Customer_Order2, Item_Stock2, Order_Item, Stock_Manager, Order_Manager},
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