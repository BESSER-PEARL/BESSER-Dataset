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
Type_of_car_UseCase = Class(name="Type_of_car_UseCase")
Type_of_Payment_UseCase = Class(name="Type_of_Payment_UseCase")
Reciept____Balance_UseCase = Class(name="Reciept____Balance_UseCase")
Cleaning_Management_UseCase = Class(name="Cleaning_Management_UseCase")
Powderized_Cleaning_UseCase = Class(name="Powderized_Cleaning_UseCase")
Water_Wash_UseCase = Class(name="Water_Wash_UseCase")
Brushing_UseCase = Class(name="Brushing_UseCase")
Delivery_Management_UseCase = Class(name="Delivery_Management_UseCase")
Delivery_Boy_Id_UseCase = Class(name="Delivery_Boy_Id_UseCase")
User = Class(name="User")
Cleaning_Management = Class(name="Cleaning_Management")
Money_Dispenser = Class(name="Money_Dispenser")
Primary_Info = Class(name="Primary_Info")
Payment = Class(name="Payment")
Service_Management = Class(name="Service_Management")
Owner = Class(name="Owner")
Staff = Class(name="Staff")
Client_Actor = Class(name="Client_Actor")
Payment_Actor = Class(name="Payment_Actor")
Cleaner_Actor = Class(name="Cleaner_Actor")
Deliver_Actor = Class(name="Deliver_Actor")
Payment_UseCase = Class(name="Payment_UseCase")
Info_UseCase = Class(name="Info_UseCase")
Type_of_wash_UseCase = Class(name="Type_of_wash_UseCase")
Client_Id___Name_UseCase = Class(name="Client_Id___Name_UseCase")

# Type_of_car_UseCase class attributes and methods

# Type_of_Payment_UseCase class attributes and methods

# Reciept____Balance_UseCase class attributes and methods

# Cleaning_Management_UseCase class attributes and methods

# Powderized_Cleaning_UseCase class attributes and methods

# Water_Wash_UseCase class attributes and methods

# Brushing_UseCase class attributes and methods

# Delivery_Management_UseCase class attributes and methods

# Delivery_Boy_Id_UseCase class attributes and methods

# User class attributes and methods

# Cleaning_Management class attributes and methods
Cleaning_Management_water: Property = Property(name="water", type=StringType)
Cleaning_Management_powderized_wash: Property = Property(name="powderized_wash", type=StringType)
Cleaning_Management_brushing: Property = Property(name="brushing", type=StringType)
Cleaning_Management.attributes={Cleaning_Management_powderized_wash, Cleaning_Management_water, Cleaning_Management_brushing}

# Money_Dispenser class attributes and methods

# Primary_Info class attributes and methods
Primary_Info_Type_of_wash: Property = Property(name="Type_of_wash", type=StringType)
Primary_Info_Type_of_car: Property = Property(name="Type_of_car", type=StringType)
Primary_Info.attributes={Primary_Info_Type_of_car, Primary_Info_Type_of_wash}

# Payment class attributes and methods
Payment_Type_of_payment: Property = Property(name="Type_of_payment", type=StringType)
Payment.attributes={Payment_Type_of_payment}

# Service_Management class attributes and methods
Service_Management_client_name: Property = Property(name="client_name", type=StringType)
Service_Management_client_key: Property = Property(name="client_key", type=StringType)
Service_Management_Staff_boy_id: Property = Property(name="Staff_boy_id", type=StringType)
Service_Management.attributes={Service_Management_client_name, Service_Management_Staff_boy_id, Service_Management_client_key}

# Owner class attributes and methods

# Staff class attributes and methods

# Client_Actor class attributes and methods

# Payment_Actor class attributes and methods

# Cleaner_Actor class attributes and methods

# Deliver_Actor class attributes and methods

# Payment_UseCase class attributes and methods

# Info_UseCase class attributes and methods

# Type_of_wash_UseCase class attributes and methods

# Client_Id___Name_UseCase class attributes and methods

# Relationships
Primary_Info_Payment: BinaryAssociation = BinaryAssociation(
    name="Primary_Info_Payment",
    ends={
        Property(name="payment0", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="primary_Info1", type=Primary_Info, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="Payment_Cleaning_Management",
    ends={
        Property(name="cleaning_Management2", type=Cleaning_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="payment3", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Delivering_Management: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Delivering_Management",
    ends={
        Property(name="delivering_Management4", type=Service_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management5", type=Cleaning_Management, multiplicity=Multiplicity(0, 1))
    }
)
User_Primary_Info: BinaryAssociation = BinaryAssociation(
    name="User_Primary_Info",
    ends={
        Property(name="primary_Info6", type=Primary_Info, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Payment: BinaryAssociation = BinaryAssociation(
    name="User_Payment",
    ends={
        Property(name="payment8", type=Payment, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="User_Cleaning_Management",
    ends={
        Property(name="cleaning_Management10", type=Cleaning_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=User, multiplicity=Multiplicity(0, 1))
    }
)
User_Delivering_Management: BinaryAssociation = BinaryAssociation(
    name="User_Delivering_Management",
    ends={
        Property(name="delivering_Management12", type=Service_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Money_Dispenser: BinaryAssociation = BinaryAssociation(
    name="Payment_Money_Dispenser",
    ends={
        Property(name="money_Dispenser14", type=Money_Dispenser, multiplicity=Multiplicity(0, 1)),
        Property(name="payment15", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Delivering_Management_Delivery_Boy: BinaryAssociation = BinaryAssociation(
    name="Delivering_Management_Delivery_Boy",
    ends={
        Property(name="Service_Provided16", type=Staff, multiplicity=Multiplicity(0, 1)),
        Property(name="delivering_Management17", type=Service_Management, multiplicity=Multiplicity(0, 1))
    }
)
Client_Info: BinaryAssociation = BinaryAssociation(
    name="Client_Info",
    ends={
        Property(name="info18", type=Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client19", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Info_Payment: BinaryAssociation = BinaryAssociation(
    name="Info_Payment",
    ends={
        Property(name="payment20", type=Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info21", type=Info_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Payment: BinaryAssociation = BinaryAssociation(
    name="Payment_Payment",
    ends={
        Property(name="payment22", type=Payment_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="payment23", type=Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Info_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="Info_Cleaning_Management",
    ends={
        Property(name="cleaning_Management24", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info25", type=Info_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Cleaner2: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Cleaner2",
    ends={
        Property(name="cleaner26", type=Cleaner_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management27", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Deliver_Delivery_Boy_Id: BinaryAssociation = BinaryAssociation(
    name="Deliver_Delivery_Boy_Id",
    ends={
        Property(name="delivery_Boy_Id28", type=Delivery_Boy_Id_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="deliver29", type=Deliver_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Delivery_Management: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Delivery_Management",
    ends={
        Property(name="delivery_Management30", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management31", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_Management_Deliver: BinaryAssociation = BinaryAssociation(
    name="Delivery_Management_Deliver",
    ends={
        Property(name="deliver32", type=Deliver_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_Management33", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Client_Delivery_Management: BinaryAssociation = BinaryAssociation(
    name="Client_Delivery_Management",
    ends={
        Property(name="delivery_Management34", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client35", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_4b505ef3_0999_453a_a975_b4c91f266482",
    types={Type_of_car_UseCase, Type_of_Payment_UseCase, Reciept____Balance_UseCase, Cleaning_Management_UseCase, Powderized_Cleaning_UseCase, Water_Wash_UseCase, Brushing_UseCase, Delivery_Management_UseCase, Delivery_Boy_Id_UseCase, User, Cleaning_Management, Money_Dispenser, Primary_Info, Payment, Service_Management, Owner, Staff, Client_Actor, Payment_Actor, Cleaner_Actor, Deliver_Actor, Payment_UseCase, Info_UseCase, Type_of_wash_UseCase, Client_Id___Name_UseCase},
    associations={Primary_Info_Payment, Payment_Cleaning_Management, Cleaning_Management_Delivering_Management, User_Primary_Info, User_Payment, User_Cleaning_Management, User_Delivering_Management, Payment_Money_Dispenser, Delivering_Management_Delivery_Boy, Client_Info, Info_Payment, Payment_Payment, Info_Cleaning_Management, Cleaning_Management_Cleaner2, Deliver_Delivery_Boy_Id, Cleaning_Management_Delivery_Management, Delivery_Management_Deliver, Client_Delivery_Management},
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