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
Product = Class(name="Product")
Furniture = Class(name="Furniture")
Appliacne = Class(name="Appliacne")
food = Class(name="food")
customers = Class(name="customers")
Employee = Class(name="Employee")
member = Class(name="member")
Admin_ = Class(name="Admin_")
Store = Class(name="Store")

# Product class attributes and methods
Product_ArrayList_food_: Property = Property(name="ArrayList_food_", type=StringType)
Product_typeOfItems: Property = Property(name="typeOfItems", type=IntegerType)
Product_ArrayList_furniture_: Property = Property(name="ArrayList_furniture_", type=StringType)
Product_ArrayList_appliance_: Property = Property(name="ArrayList_appliance_", type=StringType)
Product.attributes={Product_ArrayList_food_, Product_ArrayList_appliance_, Product_typeOfItems, Product_ArrayList_furniture_}

# Furniture class attributes and methods
Furniture_name: Property = Property(name="name", type=StringType)
Furniture_price: Property = Property(name="price", type=IntegerType)
Furniture.attributes={Furniture_name, Furniture_price}

# Appliacne class attributes and methods
Appliacne_name: Property = Property(name="name", type=StringType)
Appliacne_price: Property = Property(name="price", type=IntegerType)
Appliacne.attributes={Appliacne_price, Appliacne_name}

# food class attributes and methods
food_name: Property = Property(name="name", type=StringType)
food_price: Property = Property(name="price", type=IntegerType)
food.attributes={food_name, food_price}

# customers class attributes and methods
customers_name: Property = Property(name="name", type=StringType)
customers_shoppingCost: Property = Property(name="shoppingCost", type=IntegerType)
customers.attributes={customers_name, customers_shoppingCost}

# Employee class attributes and methods
Employee_salary: Property = Property(name="salary", type=IntegerType)
Employee_name: Property = Property(name="name", type=StringType)
Employee_Designation: Property = Property(name="Designation", type=StringType)
Employee_Password: Property = Property(name="Password", type=StringType)
Employee.attributes={Employee_name, Employee_Designation, Employee_Password, Employee_salary}

# member class attributes and methods
member_name: Property = Property(name="name", type=StringType)
member_password: Property = Property(name="password", type=StringType)
member_memberType: Property = Property(name="memberType", type=StringType)
member.attributes={member_password, member_memberType, member_name}

# Admin_ class attributes and methods
Admin__Password: Property = Property(name="Password", type=StringType)
Admin__ArrayList_member_: Property = Property(name="ArrayList_member_", type=StringType)
Admin__ArryList_Employee: Property = Property(name="ArryList_Employee", type=StringType)
Admin_.attributes={Admin__Password, Admin__ArryList_Employee, Admin__ArrayList_member_}

# Store class attributes and methods
Store_Sid: Property = Property(name="Sid", type=IntegerType)
Store_SName: Property = Property(name="SName", type=StringType)
Store.attributes={Store_SName, Store_Sid}

# Relationships
Items_Appliacne: BinaryAssociation = BinaryAssociation(
    name="Items_Appliacne",
    ends={
        Property(name="appliacne0", type=Appliacne, multiplicity=Multiplicity(1, 1)),
        Property(name="items1", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Items_Furniture: BinaryAssociation = BinaryAssociation(
    name="Items_Furniture",
    ends={
        Property(name="furniture2", type=Furniture, multiplicity=Multiplicity(0, 9999)),
        Property(name="items3", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Items_food: BinaryAssociation = BinaryAssociation(
    name="Items_food",
    ends={
        Property(name="food4", type=food, multiplicity=Multiplicity(1, 1)),
        Property(name="items5", type=Product, multiplicity=Multiplicity(0, 1))
    }
)
Admin__member: BinaryAssociation = BinaryAssociation(
    name="Admin__member",
    ends={
        Property(name="member6", type=member, multiplicity=Multiplicity(0, 1)),
        Property(name="admin_7", type=Admin_, multiplicity=Multiplicity(0, 1))
    }
)
Admin__Workers: BinaryAssociation = BinaryAssociation(
    name="Admin__Workers",
    ends={
        Property(name="workers8", type=Employee, multiplicity=Multiplicity(1, 1)),
        Property(name="admin_9", type=Admin_, multiplicity=Multiplicity(0, 1))
    }
)
member_Store: BinaryAssociation = BinaryAssociation(
    name="member_Store",
    ends={
        Property(name="store10", type=Store, multiplicity=Multiplicity(0, 1)),
        Property(name="member11", type=member, multiplicity=Multiplicity(0, 1))
    }
)
Store_Employee: BinaryAssociation = BinaryAssociation(
    name="Store_Employee",
    ends={
        Property(name="employee12", type=Employee, multiplicity=Multiplicity(0, 1)),
        Property(name="store13", type=Store, multiplicity=Multiplicity(0, 1))
    }
)
Store_Product: BinaryAssociation = BinaryAssociation(
    name="Store_Product",
    ends={
        Property(name="product14", type=Product, multiplicity=Multiplicity(0, 1)),
        Property(name="store15", type=Store, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="eb2e3754_86b5_4347_8434_71e3135183f5",
    types={Product, Furniture, Appliacne, food, customers, Employee, member, Admin_, Store},
    associations={Items_Appliacne, Items_Furniture, Items_food, Admin__member, Admin__Workers, member_Store, Store_Employee, Store_Product},
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