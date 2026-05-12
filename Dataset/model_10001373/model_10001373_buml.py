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
Discription = Class(name="Discription")
Payment = Class(name="Payment")

# Order class attributes and methods
Order_ID: Property = Property(name="ID", type=IntegerType)
Order_Quantity: Property = Property(name="Quantity", type=IntegerType)
Order_Type: Property = Property(name="Type", type=StringType)
Order_Size: Property = Property(name="Size", type=IntegerType)
Order.attributes={Order_Size, Order_ID, Order_Quantity, Order_Type}

# Delivery class attributes and methods
Delivery_Date: Property = Property(name="Date", type=StringType)
Delivery_Type: Property = Property(name="Type", type=StringType)
Delivery_Name: Property = Property(name="Name", type=StringType)
Delivery.attributes={Delivery_Name, Delivery_Type, Delivery_Date}

# User class attributes and methods
User_Name: Property = Property(name="Name", type=StringType)
User_Phone_num: Property = Property(name="Phone_num", type=IntegerType)
User_Address: Property = Property(name="Address", type=StringType)
User_Email: Property = Property(name="Email", type=StringType)
User.attributes={User_Name, User_Phone_num, User_Address, User_Email}

# Discription class attributes and methods
Discription_Email: Property = Property(name="Email", type=StringType)
Discription_Discription: Property = Property(name="Discription", type=StringType)
Discription.attributes={Discription_Discription, Discription_Email}

# Payment class attributes and methods
Payment_Amount: Property = Property(name="Amount", type=IntegerType)
Payment_Date_off: Property = Property(name="Date_off", type=StringType)
Payment.attributes={Payment_Date_off, Payment_Amount}

# Relationships
Order_Delivery: BinaryAssociation = BinaryAssociation(
    name="Order_Delivery",
    ends={
        Property(name="delivery0", type=Delivery, multiplicity=Multiplicity(0, 1)),
        Property(name="order1", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
User_Delivery: BinaryAssociation = BinaryAssociation(
    name="User_Delivery",
    ends={
        Property(name="delivery2", type=Delivery, multiplicity=Multiplicity(0, 1)),
        Property(name="User_Delivery_13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Order_Payment: BinaryAssociation = BinaryAssociation(
    name="Order_Payment",
    ends={
        Property(name="payment4", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="order5", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_Discription: BinaryAssociation = BinaryAssociation(
    name="Order_Discription",
    ends={
        Property(name="discription6", type=Discription, multiplicity=Multiplicity(0, 1)),
        Property(name="order7", type=Order, multiplicity=Multiplicity(0, 1))
    }
)
Order_User: BinaryAssociation = BinaryAssociation(
    name="Order_User",
    ends={
        Property(name="user8", type=User, multiplicity=Multiplicity(0, 1)),
        Property(name="order9", type=Order, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_2zA4IN9pEeeAyLDAJ12_fg",
    types={Order, Delivery, User, Discription, Payment},
    associations={Order_Delivery, User_Delivery, Order_Payment, Order_Discription, Order_User},
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