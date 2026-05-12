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
Order.attributes={Order_ID_, Order_Type_, Order_Quantity, Order_Size_}

# Delivery class attributes and methods
Delivery_Date: Property = Property(name="Date", type=StringType)
Delivery_Name: Property = Property(name="Name", type=StringType)
Delivery_Type: Property = Property(name="Type", type=StringType)
Delivery.attributes={Delivery_Type, Delivery_Date, Delivery_Name}

# User class attributes and methods
User_Name_: Property = Property(name="Name_", type=StringType)
User_Address_: Property = Property(name="Address_", type=StringType)
User_Phone_number: Property = Property(name="Phone_number", type=IntegerType)
User_Email_: Property = Property(name="Email_", type=StringType)
User_Phone_number1: Property = Property(name="Phone_number1", type=IntegerType)
User.attributes={User_Email_, User_Phone_number, User_Address_, User_Name_, User_Phone_number1}

# Payment class attributes and methods
Payment_Amount: Property = Property(name="Amount", type=IntegerType)
Payment_Date_off: Property = Property(name="Date_off", type=StringType)
Payment.attributes={Payment_Date_off, Payment_Amount}

# Discription class attributes and methods
Discription_Emil: Property = Property(name="Emil", type=StringType)
Discription_Discription: Property = Property(name="Discription", type=StringType)
Discription.attributes={Discription_Emil, Discription_Discription}

# Domain Model
domain_model = DomainModel(
    name="_9b0a4c76_fcde_4c25_9f23_0bb7fb65b1cc",
    types={Order, Delivery, User, Payment, Discription},
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