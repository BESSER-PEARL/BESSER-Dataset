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
ComputerParts = Class(name="ComputerParts")
Devices = Class(name="Devices")
Accessories = Class(name="Accessories")
customers = Class(name="customers")
Workers = Class(name="Workers")
member = Class(name="member")
Admin_ = Class(name="Admin_")

# Items class attributes and methods
Items_ArrayList_ComputerParts_: Property = Property(name="ArrayList_ComputerParts_", type=StringType)
Items_ArrayList_devices_: Property = Property(name="ArrayList_devices_", type=StringType)
Items_typeOfItems: Property = Property(name="typeOfItems", type=IntegerType)
Items_ArrayList_accessories_: Property = Property(name="ArrayList_accessories_", type=StringType)
Items.attributes={Items_ArrayList_ComputerParts_, Items_ArrayList_devices_, Items_typeOfItems, Items_ArrayList_accessories_}

# ComputerParts class attributes and methods
ComputerParts_name: Property = Property(name="name", type=StringType)
ComputerParts_price: Property = Property(name="price", type=IntegerType)
ComputerParts.attributes={ComputerParts_name, ComputerParts_price}

# Devices class attributes and methods
Devices_name: Property = Property(name="name", type=StringType)
Devices_price: Property = Property(name="price", type=IntegerType)
Devices.attributes={Devices_name, Devices_price}

# Accessories class attributes and methods
Accessories_name: Property = Property(name="name", type=StringType)
Accessories_price: Property = Property(name="price", type=IntegerType)
Accessories.attributes={Accessories_price, Accessories_name}

# customers class attributes and methods
customers_name: Property = Property(name="name", type=StringType)
customers_shoppingCost: Property = Property(name="shoppingCost", type=IntegerType)
customers.attributes={customers_shoppingCost, customers_name}

# Workers class attributes and methods
Workers_name: Property = Property(name="name", type=StringType)
Workers_Designation: Property = Property(name="Designation", type=StringType)
Workers_Password: Property = Property(name="Password", type=StringType)
Workers_salary: Property = Property(name="salary", type=IntegerType)
Workers.attributes={Workers_name, Workers_Designation, Workers_Password, Workers_salary}

# member class attributes and methods
member_name: Property = Property(name="name", type=StringType)
member_password: Property = Property(name="password", type=StringType)
member_memberType: Property = Property(name="memberType", type=StringType)
member.attributes={member_memberType, member_name, member_password}

# Admin_ class attributes and methods
Admin__Password: Property = Property(name="Password", type=StringType)
Admin__ArrayList_member_: Property = Property(name="ArrayList_member_", type=StringType)
Admin__ArrayList_worker_: Property = Property(name="ArrayList_worker_", type=StringType)
Admin_.attributes={Admin__ArrayList_worker_, Admin__Password, Admin__ArrayList_member_}

# Relationships
Items_Appliacne: BinaryAssociation = BinaryAssociation(
    name="Items_Appliacne",
    ends={
        Property(name="appliacne0", type=Devices, multiplicity=Multiplicity(1, 1)),
        Property(name="items1", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
Items_Furniture: BinaryAssociation = BinaryAssociation(
    name="Items_Furniture",
    ends={
        Property(name="furniture2", type=ComputerParts, multiplicity=Multiplicity(0, 9999)),
        Property(name="items3", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
Items_food: BinaryAssociation = BinaryAssociation(
    name="Items_food",
    ends={
        Property(name="food4", type=Accessories, multiplicity=Multiplicity(1, 1)),
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
    name="_vaW1gPWFEemTHo7LQdQL6Q",
    types={Items, ComputerParts, Devices, Accessories, customers, Workers, member, Admin_},
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