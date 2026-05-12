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
Furniture = Class(name="Furniture")
Appliacne = Class(name="Appliacne")
food = Class(name="food")
customers = Class(name="customers")
Workers = Class(name="Workers")
member = Class(name="member")
Admin_ = Class(name="Admin_")

# Items class attributes and methods
Items_ArrayList_furniture_: Property = Property(name="ArrayList_furniture_", type=StringType)
Items_ArrayList_appliance_: Property = Property(name="ArrayList_appliance_", type=StringType)
Items_typeOfItems: Property = Property(name="typeOfItems", type=IntegerType)
Items_ArrayList_food_: Property = Property(name="ArrayList_food_", type=StringType)
Items.attributes={Items_ArrayList_furniture_, Items_ArrayList_food_, Items_ArrayList_appliance_, Items_typeOfItems}

# Furniture class attributes and methods
Furniture_name: Property = Property(name="name", type=StringType)
Furniture_price: Property = Property(name="price", type=IntegerType)
Furniture.attributes={Furniture_name, Furniture_price}

# Appliacne class attributes and methods
Appliacne_name: Property = Property(name="name", type=StringType)
Appliacne_price: Property = Property(name="price", type=IntegerType)
Appliacne.attributes={Appliacne_name, Appliacne_price}

# food class attributes and methods
food_name: Property = Property(name="name", type=StringType)
food_price: Property = Property(name="price", type=IntegerType)
food.attributes={food_price, food_name}

# customers class attributes and methods
customers_name: Property = Property(name="name", type=StringType)
customers_shoppingCost: Property = Property(name="shoppingCost", type=IntegerType)
customers.attributes={customers_shoppingCost, customers_name}

# Workers class attributes and methods
Workers_name: Property = Property(name="name", type=StringType)
Workers_Designation: Property = Property(name="Designation", type=StringType)
Workers_Password: Property = Property(name="Password", type=StringType)
Workers_salary: Property = Property(name="salary", type=IntegerType)
Workers.attributes={Workers_salary, Workers_Designation, Workers_name, Workers_Password}

# member class attributes and methods
member_name: Property = Property(name="name", type=StringType)
member_password: Property = Property(name="password", type=StringType)
member_memberType: Property = Property(name="memberType", type=StringType)
member.attributes={member_name, member_password, member_memberType}

# Admin_ class attributes and methods
Admin__Password: Property = Property(name="Password", type=StringType)
Admin__ArrayList_member_: Property = Property(name="ArrayList_member_", type=StringType)
Admin__ArrayList_worker_: Property = Property(name="ArrayList_worker_", type=StringType)
Admin_.attributes={Admin__ArrayList_member_, Admin__Password, Admin__ArrayList_worker_}

# Relationships
Items_Appliacne: BinaryAssociation = BinaryAssociation(
    name="Items_Appliacne",
    ends={
        Property(name="appliacne0", type=Appliacne, multiplicity=Multiplicity(1, 1)),
        Property(name="items1", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
Items_Furniture: BinaryAssociation = BinaryAssociation(
    name="Items_Furniture",
    ends={
        Property(name="furniture2", type=Furniture, multiplicity=Multiplicity(0, 9999)),
        Property(name="items3", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
Items_food: BinaryAssociation = BinaryAssociation(
    name="Items_food",
    ends={
        Property(name="food4", type=food, multiplicity=Multiplicity(1, 1)),
        Property(name="items5", type=Items, multiplicity=Multiplicity(0, 1))
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
        Property(name="workers8", type=Workers, multiplicity=Multiplicity(1, 1)),
        Property(name="admin_9", type=Admin_, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3370232a_4c8a_4cc5_900d_cd5173c9fbf5",
    types={Items, Furniture, Appliacne, food, customers, Workers, member, Admin_},
    associations={Items_Appliacne, Items_Furniture, Items_food, Admin__member, Admin__Workers},
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