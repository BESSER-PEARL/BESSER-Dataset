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
Booking = Class(name="Booking")
Customer = Class(name="Customer")
Admin = Class(name="Admin")
Room = Class(name="Room")
Payment = Class(name="Payment")
Hotel = Class(name="Hotel")
Debit_Card = Class(name="Debit_Card")
Credit_Card = Class(name="Credit_Card")

# Booking class attributes and methods
Booking_Id: Property = Property(name="Id", type=StringType)
Booking_Date: Property = Property(name="Date", type=StringType)
Booking_Description: Property = Property(name="Description", type=StringType)
Booking_Type: Property = Property(name="Type", type=StringType)
Booking.attributes={Booking_Type, Booking_Description, Booking_Date, Booking_Id}

# Customer class attributes and methods
Customer_Address: Property = Property(name="Address", type=StringType)
Customer_Mobile_no___Email: Property = Property(name="Mobile_no___Email", type=StringType)
Customer_Name: Property = Property(name="Name", type=StringType)
Customer_Id: Property = Property(name="Id", type=StringType)
Customer.attributes={Customer_Id, Customer_Mobile_no___Email, Customer_Name, Customer_Address}

# Admin class attributes and methods
Admin_Name: Property = Property(name="Name", type=StringType)
Admin_Id: Property = Property(name="Id", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin.attributes={Admin_Password, Admin_Name, Admin_Id}

# Room class attributes and methods
Room_Room_Id: Property = Property(name="Room_Id", type=StringType)
Room_Room_number: Property = Property(name="Room_number", type=StringType)
Room_Room_type: Property = Property(name="Room_type", type=StringType)
Room_Room_description: Property = Property(name="Room_description", type=StringType)
Room.attributes={Room_Room_description, Room_Room_Id, Room_Room_number, Room_Room_type}

# Payment class attributes and methods
Payment_Customer_s_Id: Property = Property(name="Customer_s_Id", type=StringType)
Payment_Amount: Property = Property(name="Amount", type=StringType)
Payment_Payment_Description: Property = Property(name="Payment_Description", type=StringType)
Payment_Payment_Date: Property = Property(name="Payment_Date", type=StringType)
Payment.attributes={Payment_Payment_Date, Payment_Customer_s_Id, Payment_Payment_Description, Payment_Amount}

# Hotel class attributes and methods
Hotel_Hotel_ID: Property = Property(name="Hotel_ID", type=StringType)
Hotel_Hotel_Name: Property = Property(name="Hotel_Name", type=StringType)
Hotel_Hotel_Type: Property = Property(name="Hotel_Type", type=StringType)
Hotel_Hotel_Address: Property = Property(name="Hotel_Address", type=StringType)
Hotel_Hotel_Rent: Property = Property(name="Hotel_Rent", type=StringType)
Hotel.attributes={Hotel_Hotel_Rent, Hotel_Hotel_Address, Hotel_Hotel_Type, Hotel_Hotel_Name, Hotel_Hotel_ID}

# Debit_Card class attributes and methods
Debit_Card_Pin_No_: Property = Property(name="Pin_No_", type=StringType)
Debit_Card_Card_No_: Property = Property(name="Card_No_", type=StringType)
Debit_Card.attributes={Debit_Card_Pin_No_, Debit_Card_Card_No_}

# Credit_Card class attributes and methods
Credit_Card_Pin_No_: Property = Property(name="Pin_No_", type=StringType)
Credit_Card_Card_No_: Property = Property(name="Card_No_", type=StringType)
Credit_Card.attributes={Credit_Card_Pin_No_, Credit_Card_Card_No_}

# Relationships
Admin_Booking: BinaryAssociation = BinaryAssociation(
    name="Admin_Booking",
    ends={
        Property(name="booking0", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Room: BinaryAssociation = BinaryAssociation(
    name="Admin_Room",
    ends={
        Property(name="room2", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Room_Hotel: BinaryAssociation = BinaryAssociation(
    name="Room_Hotel",
    ends={
        Property(name="hotel4", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="room5", type=Room, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Payment: BinaryAssociation = BinaryAssociation(
    name="Customer_Payment",
    ends={
        Property(name="payment6", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Debit_Card: BinaryAssociation = BinaryAssociation(
    name="Payment_Debit_Card",
    ends={
        Property(name="debit_Card8", type=Debit_Card, multiplicity=Multiplicity(0, 1)),
        Property(name="payment9", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Credit_Card: BinaryAssociation = BinaryAssociation(
    name="Payment_Credit_Card",
    ends={
        Property(name="credit_Card10", type=Credit_Card, multiplicity=Multiplicity(0, 1)),
        Property(name="payment11", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Booking_Hotel: BinaryAssociation = BinaryAssociation(
    name="Booking_Hotel",
    ends={
        Property(name="hotel12", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="booking13", type=Booking, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Hotel: BinaryAssociation = BinaryAssociation(
    name="Customer_Hotel",
    ends={
        Property(name="hotel14", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="customer15", type=Customer, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Hotel: BinaryAssociation = BinaryAssociation(
    name="Admin_Hotel",
    ends={
        Property(name="hotel16", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="admin17", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Booking: BinaryAssociation = BinaryAssociation(
    name="Payment_Booking",
    ends={
        Property(name="booking18", type=Booking, multiplicity=Multiplicity(0, 1)),
        Property(name="payment19", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Room: BinaryAssociation = BinaryAssociation(
    name="Payment_Room",
    ends={
        Property(name="room20", type=Room, multiplicity=Multiplicity(0, 1)),
        Property(name="payment21", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Hotel: BinaryAssociation = BinaryAssociation(
    name="Payment_Hotel",
    ends={
        Property(name="hotel22", type=Hotel, multiplicity=Multiplicity(0, 1)),
        Property(name="payment23", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="a6ccc83a_0641_4507_b7e0_a8232a10f176",
    types={Booking, Customer, Admin, Room, Payment, Hotel, Debit_Card, Credit_Card},
    associations={Admin_Booking, Admin_Room, Room_Hotel, Customer_Payment, Payment_Debit_Card, Payment_Credit_Card, Booking_Hotel, Customer_Hotel, Admin_Hotel, Payment_Booking, Payment_Room, Payment_Hotel},
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