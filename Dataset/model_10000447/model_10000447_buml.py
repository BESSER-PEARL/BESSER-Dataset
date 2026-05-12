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
robotWaiter = Class(name="robotWaiter")
Host = Class(name="Host")
Table = Class(name="Table")
Items = Class(name="Items")
Chef = Class(name="Chef")
cost = Class(name="cost")
app = Class(name="app")
Food = Class(name="Food")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_numberPeople: Property = Property(name="numberPeople", type=IntegerType)
Customer.attributes={Customer_numberPeople, Customer_name}

# robotWaiter class attributes and methods

# Host class attributes and methods
Host_ID: Property = Property(name="ID", type=StringType)
Host_shift: Property = Property(name="shift", type=StringType)
Host.attributes={Host_ID, Host_shift}

# Table class attributes and methods
Table_tableNumber: Property = Property(name="tableNumber", type=IntegerType)
Table_seats: Property = Property(name="seats", type=IntegerType)
Table.attributes={Table_seats, Table_tableNumber}

# Items class attributes and methods

# Chef class attributes and methods

# cost class attributes and methods

# app class attributes and methods

# Food class attributes and methods
Food_food_id: Property = Property(name="food_id", type=StringType)
Food_name: Property = Property(name="name", type=StringType)
Food_price: Property = Property(name="price", type=FloatType)
Food_prepared: Property = Property(name="prepared", type=BooleanType)
Food_served: Property = Property(name="served", type=BooleanType)
Food.attributes={Food_food_id, Food_prepared, Food_price, Food_served, Food_name}

# Relationships
Host_Customer: BinaryAssociation = BinaryAssociation(
    name="Host_Customer",
    ends={
        Property(name="customer0", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="host1", type=Host, multiplicity=Multiplicity(0, 1))
    }
)
Table_Customer: BinaryAssociation = BinaryAssociation(
    name="Table_Customer",
    ends={
        Property(name="customer2", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="table3", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
robotWaiter_Customer: BinaryAssociation = BinaryAssociation(
    name="robotWaiter_Customer",
    ends={
        Property(name="customer4", type=Customer, multiplicity=Multiplicity(0, 1)),
        Property(name="robotWaiter5", type=robotWaiter, multiplicity=Multiplicity(0, 1))
    }
)
Table_app: BinaryAssociation = BinaryAssociation(
    name="Table_app",
    ends={
        Property(name="app6", type=app, multiplicity=Multiplicity(0, 1)),
        Property(name="table7", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
Items_Bill: BinaryAssociation = BinaryAssociation(
    name="Items_Bill",
    ends={
        Property(name="bill8", type=cost, multiplicity=Multiplicity(0, 1)),
        Property(name="items9", type=Items, multiplicity=Multiplicity(0, 1))
    }
)
Food_Items: BinaryAssociation = BinaryAssociation(
    name="Food_Items",
    ends={
        Property(name="items10", type=Items, multiplicity=Multiplicity(0, 1)),
        Property(name="food11", type=Food, multiplicity=Multiplicity(0, 1))
    }
)
app__Food: BinaryAssociation = BinaryAssociation(
    name="app__Food",
    ends={
        Property(name="food12", type=Food, multiplicity=Multiplicity(0, 1)),
        Property(name="app13", type=app, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_37defbbd_452c_4850_a393_71c269055bbb",
    types={Customer, robotWaiter, Host, Table, Items, Chef, cost, app, Food},
    associations={Host_Customer, Table_Customer, robotWaiter_Customer, Table_app, Items_Bill, Food_Items, app__Food},
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