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
Manager_Owner = Class(name="Manager_Owner")
Chef = Class(name="Chef")
Bartender = Class(name="Bartender")
Karyawan = Class(name="Karyawan")
Kasir = Class(name="Kasir")
Report = Class(name="Report")
Order = Class(name="Order")
Customer = Class(name="Customer")
DrinksItem = Class(name="DrinksItem")
FoodItem = Class(name="FoodItem")
MenuItem = Class(name="MenuItem")
Menu = Class(name="Menu")

# Manager_Owner class attributes and methods

# Chef class attributes and methods
Chef_staff_Id: Property = Property(name="staff_Id", type=StringType)
Chef_name: Property = Property(name="name", type=StringType)
Chef.attributes={Chef_name, Chef_staff_Id}

# Bartender class attributes and methods
Bartender_staff_Id: Property = Property(name="staff_Id", type=StringType)
Bartender_name: Property = Property(name="name", type=StringType)
Bartender.attributes={Bartender_name, Bartender_staff_Id}

# Karyawan class attributes and methods
Karyawan_staff_Id: Property = Property(name="staff_Id", type=StringType)
Karyawan_name: Property = Property(name="name", type=StringType)
Karyawan_contact: Property = Property(name="contact", type=StringType)
Karyawan.attributes={Karyawan_name, Karyawan_staff_Id, Karyawan_contact}

# Kasir class attributes and methods
Kasir_order_id: Property = Property(name="order_id", type=StringType)
Kasir_cust_id: Property = Property(name="cust_id", type=StringType)
Kasir.attributes={Kasir_cust_id, Kasir_order_id}

# Report class attributes and methods
Report_profit: Property = Property(name="profit", type=StringType)
Report_orders: Property = Property(name="orders", type=StringType)
Report_totalSales: Property = Property(name="totalSales", type=StringType)
Report.attributes={Report_profit, Report_totalSales, Report_orders}

# Order class attributes and methods
Order_order_Id: Property = Property(name="order_Id", type=StringType)
Order_cust_id: Property = Property(name="cust_id", type=StringType)
Order_cust_name: Property = Property(name="cust_name", type=StringType)
Order_numTable: Property = Property(name="numTable", type=IntegerType)
Order_foodItem: Property = Property(name="foodItem", type=FoodItem)
Order_drinksItem: Property = Property(name="drinksItem", type=DrinksItem)
Order.attributes={Order_cust_id, Order_foodItem, Order_order_Id, Order_drinksItem, Order_numTable, Order_cust_name}

# Customer class attributes and methods
Customer_cust_name: Property = Property(name="cust_name", type=StringType)
Customer_cust_Id: Property = Property(name="cust_Id", type=StringType)
Customer.attributes={Customer_cust_name, Customer_cust_Id}

# DrinksItem class attributes and methods
DrinksItem_drinkType: Property = Property(name="drinkType", type=StringType)
DrinksItem.attributes={DrinksItem_drinkType}

# FoodItem class attributes and methods
FoodItem_drinkType: Property = Property(name="drinkType", type=StringType)
FoodItem.attributes={FoodItem_drinkType}

# MenuItem class attributes and methods
MenuItem_item_Id: Property = Property(name="item_Id", type=IntegerType)
MenuItem_item_price: Property = Property(name="item_price", type=IntegerType)
MenuItem_available: Property = Property(name="available", type=BooleanType)
MenuItem_quantity: Property = Property(name="quantity", type=IntegerType)
MenuItem_item_description: Property = Property(name="item_description", type=StringType)
MenuItem.attributes={MenuItem_available, MenuItem_item_description, MenuItem_quantity, MenuItem_item_Id, MenuItem_item_price}

# Menu class attributes and methods
Menu_foodItem: Property = Property(name="foodItem", type=FoodItem)
Menu_drinksItem: Property = Property(name="drinksItem", type=DrinksItem)
Menu_category: Property = Property(name="category", type=StringType)
Menu.attributes={Menu_drinksItem, Menu_category, Menu_foodItem}

# Relationships
Order_DrinksItem: BinaryAssociation = BinaryAssociation(
    name="Order_DrinksItem",
    ends={
        Property(name="order0", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="drinksItem21", type=DrinksItem, multiplicity=Multiplicity(0, 1))
    }
)
Order_FoodItem: BinaryAssociation = BinaryAssociation(
    name="Order_FoodItem",
    ends={
        Property(name="order2", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="foodItem23", type=FoodItem, multiplicity=Multiplicity(0, 1))
    }
)
MenuItem_Menu: BinaryAssociation = BinaryAssociation(
    name="MenuItem_Menu",
    ends={
        Property(name="menuItem4", type=MenuItem, multiplicity=Multiplicity(0, 1)),
        Property(name="menu5", type=Menu, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_toUTwHjlEeqeQcxm9hmzHw",
    types={Manager_Owner, Chef, Bartender, Karyawan, Kasir, Report, Order, Customer, DrinksItem, FoodItem, MenuItem, Menu},
    associations={Order_DrinksItem, Order_FoodItem, MenuItem_Menu},
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