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
Food = Class(name="Food")
Material = Class(name="Material")
Table = Class(name="Table")
Food_Category = Class(name="Food_Category")
Customer = Class(name="Customer")
Food_Sub_Category = Class(name="Food_Sub_Category")
Food_Items = Class(name="Food_Items")
Chef = Class(name="Chef")
Order = Class(name="Order")

# Food class attributes and methods
Food_food_id: Property = Property(name="food_id", type=IntegerType)
Food_food_name: Property = Property(name="food_name", type=StringType)
Food_Category_id: Property = Property(name="Category_id", type=IntegerType)
Food.attributes={Food_Category_id, Food_food_name, Food_food_id}

# Material class attributes and methods
Material_Material_id: Property = Property(name="Material_id", type=IntegerType)
Material_Material_name: Property = Property(name="Material_name", type=StringType)
Material_Stock: Property = Property(name="Stock", type=StringType)
Material_Stock1: Property = Property(name="Stock1", type=StringType)
Material_Unit: Property = Property(name="Unit", type=StringType)
Material.attributes={Material_Unit, Material_Stock, Material_Material_name, Material_Material_id, Material_Stock1}

# Table class attributes and methods
Table_Table_id: Property = Property(name="Table_id", type=IntegerType)
Table_Table_num: Property = Property(name="Table_num", type=IntegerType)
Table_Status: Property = Property(name="Status", type=StringType)
Table.attributes={Table_Table_id, Table_Status, Table_Table_num}

# Food_Category class attributes and methods
Food_Category_Category_id: Property = Property(name="Category_id", type=IntegerType)
Food_Category_Category_name: Property = Property(name="Category_name", type=StringType)
Food_Category_Category_descp: Property = Property(name="Category_descp", type=StringType)
Food_Category_Category_image: Property = Property(name="Category_image", type=StringType)
Food_Category_sub_id: Property = Property(name="sub_id", type=IntegerType)
Food_Category.attributes={Food_Category_Category_descp, Food_Category_Category_name, Food_Category_Category_image, Food_Category_Category_id, Food_Category_sub_id}

# Customer class attributes and methods
Customer_Customer_id: Property = Property(name="Customer_id", type=IntegerType)
Customer_Customer_name: Property = Property(name="Customer_name", type=StringType)
Customer_Status: Property = Property(name="Status", type=StringType)
Customer_TimeStamp: Property = Property(name="TimeStamp", type=StringType)
Customer_Table_id: Property = Property(name="Table_id", type=IntegerType)
Customer.attributes={Customer_TimeStamp, Customer_Table_id, Customer_Customer_name, Customer_Customer_id, Customer_Status}

# Food_Sub_Category class attributes and methods
Food_Sub_Category_sub_id: Property = Property(name="sub_id", type=IntegerType)
Food_Sub_Category_sub_name: Property = Property(name="sub_name", type=StringType)
Food_Sub_Category_sub_descp: Property = Property(name="sub_descp", type=StringType)
Food_Sub_Category_sub_image: Property = Property(name="sub_image", type=StringType)
Food_Sub_Category.attributes={Food_Sub_Category_sub_name, Food_Sub_Category_sub_descp, Food_Sub_Category_sub_image, Food_Sub_Category_sub_id}

# Food_Items class attributes and methods
Food_Items_Items_id: Property = Property(name="Items_id", type=IntegerType)
Food_Items_Food_id: Property = Property(name="Food_id", type=IntegerType)
Food_Items_Material_id: Property = Property(name="Material_id", type=IntegerType)
Food_Items_quantity: Property = Property(name="quantity", type=IntegerType)
Food_Items.attributes={Food_Items_Food_id, Food_Items_quantity, Food_Items_Items_id, Food_Items_Material_id}

# Chef class attributes and methods
Chef_Chef_id: Property = Property(name="Chef_id", type=IntegerType)
Chef_Chef_name: Property = Property(name="Chef_name", type=StringType)
Chef_Speciality: Property = Property(name="Speciality", type=StringType)
Chef_Status: Property = Property(name="Status", type=StringType)
Chef_order_id: Property = Property(name="order_id", type=IntegerType)
Chef.attributes={Chef_Status, Chef_Chef_id, Chef_order_id, Chef_Chef_name, Chef_Speciality}

# Order class attributes and methods
Order_Order_id: Property = Property(name="Order_id", type=IntegerType)
Order_Order_num: Property = Property(name="Order_num", type=IntegerType)
Order_Order_status: Property = Property(name="Order_status", type=StringType)
Order_Order_edit: Property = Property(name="Order_edit", type=StringType)
Order_Order_delete: Property = Property(name="Order_delete", type=StringType)
Order.attributes={Order_Order_delete, Order_Order_edit, Order_Order_id, Order_Order_status, Order_Order_num}

# Domain Model
domain_model = DomainModel(
    name="_IffysPLLEee2hpeWh535Sw",
    types={Food, Material, Table, Food_Category, Customer, Food_Sub_Category, Food_Items, Chef, Order},
    associations={},
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