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
Delivery = Class(name="Delivery")
User = Class(name="User")
Payment = Class(name="Payment")
Discription = Class(name="Discription")

# Order class attributes and methods
Order_ID_: Property = Property(name="ID_", type=IntegerType)
Order_Type_: Property = Property(name="Type_", type=StringType)
Order_Size_: Property = Property(name="Size_", type=IntegerType)
Order_Quantity: Property = Property(name="Quantity", type=IntegerType)
Order.attributes={Order_Quantity, Order_Type_, Order_Size_, Order_ID_}

# Delivery class attributes and methods

# User class attributes and methods

# Payment class attributes and methods

# Discription class attributes and methods

# Relationships
Order_MyClass: BinaryAssociation = BinaryAssociation(
    name="Order_MyClass",
    ends={
        Property(name="myClass0", type=Delivery, multiplicity=Multiplicity(0, 1)),
        Property(name="order1", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_MyClass2: BinaryAssociation = BinaryAssociation(
    name="Order_MyClass2",
    ends={
        Property(name="myClass22", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="order3", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_MyClass3: BinaryAssociation = BinaryAssociation(
    name="Order_MyClass3",
    ends={
        Property(name="myClass34", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
MyClass2_MyClass: BinaryAssociation = BinaryAssociation(
    name="MyClass2_MyClass",
    ends={
        Property(name="myClass6", type=Delivery, multiplicity=Multiplicity(0, 1)),
        Property(name="myClass27", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Order_MyClass4: BinaryAssociation = BinaryAssociation(
    name="Order_MyClass4",
    ends={
        Property(name="myClass48", type=Discription, multiplicity=Multiplicity(0, 1)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_LTqG4NFiEeeLcIicqHdTUQ",
    types={Order, Delivery, User, Payment, Discription},
    associations={Order_MyClass, Order_MyClass2, Order_MyClass3, MyClass2_MyClass, Order_MyClass4},
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