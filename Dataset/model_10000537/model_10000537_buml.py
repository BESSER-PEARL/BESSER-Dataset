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
Brushing_UseCase = Class(name="Brushing_UseCase")
Delivery_Management_UseCase = Class(name="Delivery_Management_UseCase")
Delivery_Boy_Id_UseCase = Class(name="Delivery_Boy_Id_UseCase")
Client_Id___Name_UseCase = Class(name="Client_Id___Name_UseCase")
Usuario = Class(name="Usuario")
Gestion_de_Limpieza = Class(name="Gestion_de_Limpieza")
Dispensador_de_dinero = Class(name="Dispensador_de_dinero")
Informacion_Primaria = Class(name="Informacion_Primaria")
PAGO = Class(name="PAGO")
Delivering_Management = Class(name="Delivering_Management")
Administrator = Class(name="Administrator")
Limpiador = Class(name="Limpiador")
Delivery_Boy = Class(name="Delivery_Boy")
Client_Actor = Class(name="Client_Actor")
Payment_Actor = Class(name="Payment_Actor")
Cleaner_Actor = Class(name="Cleaner_Actor")
Deliver_Actor = Class(name="Deliver_Actor")
Payment_UseCase = Class(name="Payment_UseCase")
Info_UseCase = Class(name="Info_UseCase")
Type_of_wash_UseCase = Class(name="Type_of_wash_UseCase")
Type_of_car_UseCase = Class(name="Type_of_car_UseCase")
Type_of_Payment_UseCase = Class(name="Type_of_Payment_UseCase")
Reciept____Balance_UseCase = Class(name="Reciept____Balance_UseCase")
Cleaning_Management_UseCase = Class(name="Cleaning_Management_UseCase")
Powderized_Cleaning_UseCase = Class(name="Powderized_Cleaning_UseCase")
Water_Wash_UseCase = Class(name="Water_Wash_UseCase")

# Brushing_UseCase class attributes and methods

# Delivery_Management_UseCase class attributes and methods

# Delivery_Boy_Id_UseCase class attributes and methods

# Client_Id___Name_UseCase class attributes and methods

# Usuario class attributes and methods

# Gestion_de_Limpieza class attributes and methods
Gestion_de_Limpieza_water: Property = Property(name="water", type=StringType)
Gestion_de_Limpieza_powderized_wash: Property = Property(name="powderized_wash", type=StringType)
Gestion_de_Limpieza_brushing: Property = Property(name="brushing", type=StringType)
Gestion_de_Limpieza.attributes={Gestion_de_Limpieza_water, Gestion_de_Limpieza_powderized_wash, Gestion_de_Limpieza_brushing}

# Dispensador_de_dinero class attributes and methods

# Informacion_Primaria class attributes and methods
Informacion_Primaria_Type_of_wash: Property = Property(name="Type_of_wash", type=StringType)
Informacion_Primaria_Type_of_car: Property = Property(name="Type_of_car", type=StringType)
Informacion_Primaria.attributes={Informacion_Primaria_Type_of_car, Informacion_Primaria_Type_of_wash}

# PAGO class attributes and methods
PAGO_Type_of_payment: Property = Property(name="Type_of_payment", type=StringType)
PAGO.attributes={PAGO_Type_of_payment}

# Delivering_Management class attributes and methods
Delivering_Management_client_name: Property = Property(name="client_name", type=StringType)
Delivering_Management_client_key: Property = Property(name="client_key", type=StringType)
Delivering_Management_deliver_boy_id: Property = Property(name="deliver_boy_id", type=StringType)
Delivering_Management.attributes={Delivering_Management_deliver_boy_id, Delivering_Management_client_name, Delivering_Management_client_key}

# Administrator class attributes and methods

# Limpiador class attributes and methods

# Delivery_Boy class attributes and methods

# Client_Actor class attributes and methods

# Payment_Actor class attributes and methods

# Cleaner_Actor class attributes and methods

# Deliver_Actor class attributes and methods

# Payment_UseCase class attributes and methods

# Info_UseCase class attributes and methods

# Type_of_wash_UseCase class attributes and methods

# Type_of_car_UseCase class attributes and methods

# Type_of_Payment_UseCase class attributes and methods

# Reciept____Balance_UseCase class attributes and methods

# Cleaning_Management_UseCase class attributes and methods

# Powderized_Cleaning_UseCase class attributes and methods

# Water_Wash_UseCase class attributes and methods

# Relationships
Primary_Info_Payment: BinaryAssociation = BinaryAssociation(
    name="Primary_Info_Payment",
    ends={
        Property(name="payment0", type=PAGO, multiplicity=Multiplicity(0, 1)),
        Property(name="primary_Info1", type=Informacion_Primaria, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="Payment_Cleaning_Management",
    ends={
        Property(name="cleaning_Management2", type=Gestion_de_Limpieza, multiplicity=Multiplicity(0, 1)),
        Property(name="payment3", type=PAGO, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Delivering_Management: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Delivering_Management",
    ends={
        Property(name="delivering_Management4", type=Delivering_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management5", type=Gestion_de_Limpieza, multiplicity=Multiplicity(0, 1))
    }
)
User_Primary_Info: BinaryAssociation = BinaryAssociation(
    name="User_Primary_Info",
    ends={
        Property(name="primary_Info6", type=Informacion_Primaria, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=Usuario, multiplicity=Multiplicity(0, 1))
    }
)
User_Payment: BinaryAssociation = BinaryAssociation(
    name="User_Payment",
    ends={
        Property(name="payment8", type=PAGO, multiplicity=Multiplicity(0, 1)),
        Property(name="user9", type=Usuario, multiplicity=Multiplicity(0, 1))
    }
)
User_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="User_Cleaning_Management",
    ends={
        Property(name="cleaning_Management10", type=Gestion_de_Limpieza, multiplicity=Multiplicity(0, 1)),
        Property(name="user11", type=Usuario, multiplicity=Multiplicity(0, 1))
    }
)
User_Delivering_Management: BinaryAssociation = BinaryAssociation(
    name="User_Delivering_Management",
    ends={
        Property(name="delivering_Management12", type=Delivering_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=Usuario, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Cleaner: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Cleaner",
    ends={
        Property(name="cleaner14", type=Limpiador, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management15", type=Gestion_de_Limpieza, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Money_Dispenser: BinaryAssociation = BinaryAssociation(
    name="Payment_Money_Dispenser",
    ends={
        Property(name="money_Dispenser16", type=Dispensador_de_dinero, multiplicity=Multiplicity(0, 1)),
        Property(name="payment17", type=PAGO, multiplicity=Multiplicity(0, 1))
    }
)
Delivering_Management_Delivery_Boy: BinaryAssociation = BinaryAssociation(
    name="Delivering_Management_Delivery_Boy",
    ends={
        Property(name="delivery_Boy18", type=Delivery_Boy, multiplicity=Multiplicity(0, 1)),
        Property(name="delivering_Management19", type=Delivering_Management, multiplicity=Multiplicity(0, 1))
    }
)
Client_Info: BinaryAssociation = BinaryAssociation(
    name="Client_Info",
    ends={
        Property(name="info20", type=Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client21", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Info_Payment: BinaryAssociation = BinaryAssociation(
    name="Info_Payment",
    ends={
        Property(name="payment22", type=Payment_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info23", type=Info_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Payment: BinaryAssociation = BinaryAssociation(
    name="Payment_Payment",
    ends={
        Property(name="payment24", type=Payment_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="payment25", type=Payment_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Info_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="Info_Cleaning_Management",
    ends={
        Property(name="cleaning_Management26", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info27", type=Info_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Cleaner2: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Cleaner2",
    ends={
        Property(name="cleaner28", type=Cleaner_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management29", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Deliver_Delivery_Boy_Id: BinaryAssociation = BinaryAssociation(
    name="Deliver_Delivery_Boy_Id",
    ends={
        Property(name="delivery_Boy_Id30", type=Delivery_Boy_Id_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="deliver31", type=Deliver_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Delivery_Management: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Delivery_Management",
    ends={
        Property(name="delivery_Management32", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management33", type=Cleaning_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Delivery_Management_Deliver: BinaryAssociation = BinaryAssociation(
    name="Delivery_Management_Deliver",
    ends={
        Property(name="deliver34", type=Deliver_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="delivery_Management35", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Client_Delivery_Management: BinaryAssociation = BinaryAssociation(
    name="Client_Delivery_Management",
    ends={
        Property(name="delivery_Management36", type=Delivery_Management_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client37", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_419e14cd_42d1_48e4_ab80_ddc8d94f014c",
    types={Brushing_UseCase, Delivery_Management_UseCase, Delivery_Boy_Id_UseCase, Client_Id___Name_UseCase, Usuario, Gestion_de_Limpieza, Dispensador_de_dinero, Informacion_Primaria, PAGO, Delivering_Management, Administrator, Limpiador, Delivery_Boy, Client_Actor, Payment_Actor, Cleaner_Actor, Deliver_Actor, Payment_UseCase, Info_UseCase, Type_of_wash_UseCase, Type_of_car_UseCase, Type_of_Payment_UseCase, Reciept____Balance_UseCase, Cleaning_Management_UseCase, Powderized_Cleaning_UseCase, Water_Wash_UseCase},
    associations={Primary_Info_Payment, Payment_Cleaning_Management, Cleaning_Management_Delivering_Management, User_Primary_Info, User_Payment, User_Cleaning_Management, User_Delivering_Management, Cleaning_Management_Cleaner, Payment_Money_Dispenser, Delivering_Management_Delivery_Boy, Client_Info, Info_Payment, Payment_Payment, Info_Cleaning_Management, Cleaning_Management_Cleaner2, Deliver_Delivery_Boy_Id, Cleaning_Management_Delivery_Management, Delivery_Management_Deliver, Client_Delivery_Management},
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