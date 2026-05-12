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
Restaurant = Class(name="Restaurant")
MenuItem = Class(name="MenuItem")
FoodPackage = Class(name="FoodPackage")
FoodItem = Class(name="FoodItem")
Food = Class(name="Food")
Order = Class(name="Order")
Customer = Class(name="Customer")
RestaurantController = Class(name="RestaurantController")
OrderController = Class(name="OrderController")

# Restaurant class attributes and methods
Restaurant_Name: Property = Property(name="Name", type=StringType)
Restaurant_Address: Property = Property(name="Address", type=StringType)
Restaurant_PostCode: Property = Property(name="PostCode", type=IntegerType)
Restaurant_Menu: Property = Property(name="Menu", type=MenuItem)
Restaurant.attributes={Restaurant_PostCode, Restaurant_Name, Restaurant_Menu, Restaurant_Address}

# MenuItem class attributes and methods
MenuItem_Description: Property = Property(name="Description", type=StringType)
MenuItem.attributes={MenuItem_Description}

# FoodPackage class attributes and methods
FoodPackage_FoodList: Property = Property(name="FoodList", type=Food)
FoodPackage.attributes={FoodPackage_FoodList}

# FoodItem class attributes and methods
FoodItem_Food: Property = Property(name="Food", type=Food)
FoodItem.attributes={FoodItem_Food}

# Food class attributes and methods
Food_Price: Property = Property(name="Price", type=IntegerType)
Food_Calories: Property = Property(name="Calories", type=IntegerType)
Food_Vegetarian: Property = Property(name="Vegetarian", type=BooleanType)
Food.attributes={Food_Calories, Food_Vegetarian, Food_Price}

# Order class attributes and methods
Order_Restaurant: Property = Property(name="Restaurant", type=Restaurant)
Order_ItemList: Property = Property(name="ItemList", type=MenuItem)
Order_Customer: Property = Property(name="Customer", type=Customer)
Order.attributes={Order_Restaurant, Order_ItemList, Order_Customer}

# Customer class attributes and methods
Customer_Cellphone: Property = Property(name="Cellphone", type=StringType)
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_PostCode: Property = Property(name="PostCode", type=IntegerType)
Customer_FullName: Property = Property(name="FullName", type=StringType)
Customer_CreditCard: Property = Property(name="CreditCard", type=StringType)
Customer.attributes={Customer_Address, Customer_CreditCard, Customer_FullName, Customer_Cellphone, Customer_PostCode}

# RestaurantController class attributes and methods
RestaurantController_Restaurant: Property = Property(name="Restaurant", type=Restaurant)
RestaurantController.attributes={RestaurantController_Restaurant}

# OrderController class attributes and methods
OrderController_Order: Property = Property(name="Order", type=Order)
OrderController.attributes={OrderController_Order}

# Relationships
MenuItem_FoodItem: BinaryAssociation = BinaryAssociation(
    name="MenuItem_FoodItem",
    ends={
        Property(name="MenuItem_FoodItem_00", type=FoodItem, multiplicity=Multiplicity(0, 9999)),
        Property(name="MenuItem_FoodItem_11", type=MenuItem, multiplicity=Multiplicity(0, 9999))
    }
)
MenuItem_FoodPackage: BinaryAssociation = BinaryAssociation(
    name="MenuItem_FoodPackage",
    ends={
        Property(name="MenuItem_FoodPackage_02", type=FoodPackage, multiplicity=Multiplicity(0, 9999)),
        Property(name="MenuItem_FoodPackage_13", type=MenuItem, multiplicity=Multiplicity(0, 9999))
    }
)
FoodItem_Food: BinaryAssociation = BinaryAssociation(
    name="FoodItem_Food",
    ends={
        Property(name="FoodItem_Food_04", type=Food, multiplicity=Multiplicity(1, 1)),
        Property(name="FoodItem_Food_15", type=FoodItem, multiplicity=Multiplicity(0, 9999))
    }
)
FoodPackage_Food: BinaryAssociation = BinaryAssociation(
    name="FoodPackage_Food",
    ends={
        Property(name="FoodPackage_Food_06", type=Food, multiplicity=Multiplicity(1, 9999)),
        Property(name="FoodPackage_Food_17", type=FoodPackage, multiplicity=Multiplicity(0, 9999))
    }
)
Restaurant_MenuItem: BinaryAssociation = BinaryAssociation(
    name="Restaurant_MenuItem",
    ends={
        Property(name="Restaurant_MenuItem_08", type=MenuItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="Restaurant_MenuItem_19", type=Restaurant, multiplicity=Multiplicity(0, 9999))
    }
)
Order_MenuItem: BinaryAssociation = BinaryAssociation(
    name="Order_MenuItem",
    ends={
        Property(name="Order_MenuItem_010", type=MenuItem, multiplicity=Multiplicity(1, 9999)),
        Property(name="Order_MenuItem_111", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
OrderController_Order: BinaryAssociation = BinaryAssociation(
    name="OrderController_Order",
    ends={
        Property(name="OrderController_Order_018", type=Order, multiplicity=Multiplicity(1, 1)),
        Property(name="OrderController_Order_119", type=OrderController, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Restaurant: BinaryAssociation = BinaryAssociation(
    name="Order_Restaurant",
    ends={
        Property(name="Order_Restaurant_012", type=Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="Order_Restaurant_113", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
Order_Customer: BinaryAssociation = BinaryAssociation(
    name="Order_Customer",
    ends={
        Property(name="Order_Customer_014", type=Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="Order_Customer_115", type=Order, multiplicity=Multiplicity(0, 9999))
    }
)
RestaurantManager_Restaurant: BinaryAssociation = BinaryAssociation(
    name="RestaurantManager_Restaurant",
    ends={
        Property(name="RestaurantManager_Restaurant_016", type=Restaurant, multiplicity=Multiplicity(1, 9999)),
        Property(name="RestaurantManager_Restaurant_117", type=RestaurantController, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="f3a5bc18_425e_4cf7_8e9e_fd5f58839c21",
    types={Restaurant, MenuItem, FoodPackage, FoodItem, Food, Order, Customer, RestaurantController, OrderController},
    associations={MenuItem_FoodItem, MenuItem_FoodPackage, FoodItem_Food, FoodPackage_Food, Restaurant_MenuItem, Order_MenuItem, OrderController_Order, Order_Restaurant, Order_Customer, RestaurantManager_Restaurant},
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