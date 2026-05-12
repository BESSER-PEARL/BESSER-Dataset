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
Table = Class(name="Table")
Order = Class(name="Order")
meal = Class(name="meal")
Waiter = Class(name="Waiter")
app = Class(name="app")
system = Class(name="system")
Chef = Class(name="Chef")
manger = Class(name="manger")
customer = Class(name="customer")

# Table class attributes and methods
Table_numSeats: Property = Property(name="numSeats", type=IntegerType)
Table_table_id: Property = Property(name="table_id", type=StringType)
Table_avaliable: Property = Property(name="avaliable", type=BooleanType)
Table.attributes={Table_table_id, Table_avaliable, Table_numSeats}

# Order class attributes and methods
Order_order_id: Property = Property(name="order_id", type=StringType)
Order_foodList: Property = Property(name="foodList", type=StringType)
Order.attributes={Order_foodList, Order_order_id}

# meal class attributes and methods
meal_meal_id: Property = Property(name="meal_id", type=StringType)
meal_name: Property = Property(name="name", type=StringType)
meal_price: Property = Property(name="price", type=FloatType)
meal_prepared: Property = Property(name="prepared", type=BooleanType)
meal_served: Property = Property(name="served", type=BooleanType)
meal.attributes={meal_served, meal_prepared, meal_price, meal_meal_id, meal_name}

# Waiter class attributes and methods

# app class attributes and methods
app_user_id: Property = Property(name="user_id", type=StringType)
app_name: Property = Property(name="name", type=StringType)
app.attributes={app_user_id, app_name}

# system class attributes and methods
system_user_id: Property = Property(name="user_id", type=StringType)
system_name: Property = Property(name="name", type=StringType)
system.attributes={system_name, system_user_id}

# Chef class attributes and methods

# manger class attributes and methods

# customer class attributes and methods

# Relationships
Order_Food: BinaryAssociation = BinaryAssociation(
    name="Order_Food",
    ends={
        Property(name="orde0", type=meal, multiplicity=Multiplicity(1, 9999)),
        Property(name="has1", type=Order, multiplicity=Multiplicity(1, 1))
    }
)
Waiter_Table: BinaryAssociation = BinaryAssociation(
    name="Waiter_Table",
    ends={
        Property(name="table2", type=Table, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter3", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)
Table_app: BinaryAssociation = BinaryAssociation(
    name="Table_app",
    ends={
        Property(name="app4", type=app, multiplicity=Multiplicity(0, 1)),
        Property(name="table5", type=Table, multiplicity=Multiplicity(0, 1))
    }
)
app_Order: BinaryAssociation = BinaryAssociation(
    name="app_Order",
    ends={
        Property(name="order6", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="app7", type=app, multiplicity=Multiplicity(0, 1))
    }
)
system_app: BinaryAssociation = BinaryAssociation(
    name="system_app",
    ends={
        Property(name="app8", type=app, multiplicity=Multiplicity(0, 1)),
        Property(name="system9", type=system, multiplicity=Multiplicity(0, 1))
    }
)
Chef_system: BinaryAssociation = BinaryAssociation(
    name="Chef_system",
    ends={
        Property(name="system10", type=system, multiplicity=Multiplicity(0, 1)),
        Property(name="chef11", type=Chef, multiplicity=Multiplicity(0, 1))
    }
)
manger_system: BinaryAssociation = BinaryAssociation(
    name="manger_system",
    ends={
        Property(name="system12", type=system, multiplicity=Multiplicity(0, 1)),
        Property(name="manger13", type=manger, multiplicity=Multiplicity(0, 1))
    }
)
customer__Order: BinaryAssociation = BinaryAssociation(
    name="customer__Order",
    ends={
        Property(name="order14", type=Order, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=customer, multiplicity=Multiplicity(0, 1))
    }
)
Waiter_app: BinaryAssociation = BinaryAssociation(
    name="Waiter_app",
    ends={
        Property(name="app16", type=app, multiplicity=Multiplicity(0, 1)),
        Property(name="waiter17", type=Waiter, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_959c8e85_0480_42f0_9916_b57462b85cb9",
    types={Table, Order, meal, Waiter, app, system, Chef, manger, customer},
    associations={Order_Food, Waiter_Table, Table_app, app_Order, system_app, Chef_system, manger_system, customer__Order, Waiter_app},
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