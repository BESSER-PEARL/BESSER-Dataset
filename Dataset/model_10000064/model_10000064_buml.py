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
User = Class(name="User")
Cleaning_Management = Class(name="Cleaning_Management")
Money_Dispenser = Class(name="Money_Dispenser")
Primary_Info = Class(name="Primary_Info")
Payment = Class(name="Payment")
Delivering_Management = Class(name="Delivering_Management")
Administrator = Class(name="Administrator")
Cleaner = Class(name="Cleaner")
Delivery_Boy = Class(name="Delivery_Boy")
Client_Actor = Class(name="Client_Actor")
Payer_UseCase = Class(name="Payer_UseCase")
donner_des_informayions_UseCase = Class(name="donner_des_informayions_UseCase")
choisir_le_type_de_lavage_UseCase = Class(name="choisir_le_type_de_lavage_UseCase")
D_finir_le_type_de_voiture_UseCase = Class(name="D_finir_le_type_de_voiture_UseCase")
choisir_le_type_de_payement_UseCase = Class(name="choisir_le_type_de_payement_UseCase")
Prendre_le_re_u_UseCase = Class(name="Prendre_le_re_u_UseCase")
Lavage_de_la_voiture__UseCase = Class(name="Lavage_de_la_voiture__UseCase")
Metre_de_la_mousse_UseCase = Class(name="Metre_de_la_mousse_UseCase")
Rincer_la_voiture__UseCase = Class(name="Rincer_la_voiture__UseCase")
Brosser_la_voiture_UseCase = Class(name="Brosser_la_voiture_UseCase")

# User class attributes and methods

# Cleaning_Management class attributes and methods
Cleaning_Management_water: Property = Property(name="water", type=StringType)
Cleaning_Management_powderized_wash: Property = Property(name="powderized_wash", type=StringType)
Cleaning_Management_brushing: Property = Property(name="brushing", type=StringType)
Cleaning_Management.attributes={Cleaning_Management_brushing, Cleaning_Management_water, Cleaning_Management_powderized_wash}

# Money_Dispenser class attributes and methods

# Primary_Info class attributes and methods
Primary_Info_Type_of_wash: Property = Property(name="Type_of_wash", type=StringType)
Primary_Info_Type_of_car: Property = Property(name="Type_of_car", type=StringType)
Primary_Info.attributes={Primary_Info_Type_of_wash, Primary_Info_Type_of_car}

# Payment class attributes and methods
Payment_Type_of_payment: Property = Property(name="Type_of_payment", type=StringType)
Payment.attributes={Payment_Type_of_payment}

# Delivering_Management class attributes and methods
Delivering_Management_client_name: Property = Property(name="client_name", type=StringType)
Delivering_Management_client_key: Property = Property(name="client_key", type=StringType)
Delivering_Management_deliver_boy_id: Property = Property(name="deliver_boy_id", type=StringType)
Delivering_Management.attributes={Delivering_Management_deliver_boy_id, Delivering_Management_client_name, Delivering_Management_client_key}

# Administrator class attributes and methods

# Cleaner class attributes and methods

# Delivery_Boy class attributes and methods

# Client_Actor class attributes and methods

# Payer_UseCase class attributes and methods

# donner_des_informayions_UseCase class attributes and methods

# choisir_le_type_de_lavage_UseCase class attributes and methods

# D_finir_le_type_de_voiture_UseCase class attributes and methods

# choisir_le_type_de_payement_UseCase class attributes and methods

# Prendre_le_re_u_UseCase class attributes and methods

# Lavage_de_la_voiture__UseCase class attributes and methods

# Metre_de_la_mousse_UseCase class attributes and methods

# Rincer_la_voiture__UseCase class attributes and methods

# Brosser_la_voiture_UseCase class attributes and methods

# Relationships
User_Delivering_Management: BinaryAssociation = BinaryAssociation(
    name="User_Delivering_Management",
    ends={
        Property(name="delivering_Management12", type=Delivering_Management, multiplicity=Multiplicity(0, 1)),
        Property(name="user13", type=User, multiplicity=Multiplicity(0, 1))
    }
)
Cleaning_Management_Cleaner: BinaryAssociation = BinaryAssociation(
    name="Cleaning_Management_Cleaner",
    ends={
        Property(name="cleaner14", type=Cleaner, multiplicity=Multiplicity(0, 1)),
        Property(name="cleaning_Management15", type=Cleaning_Management, multiplicity=Multiplicity(0, 1))
    }
)
Payment_Money_Dispenser: BinaryAssociation = BinaryAssociation(
    name="Payment_Money_Dispenser",
    ends={
        Property(name="money_Dispenser16", type=Money_Dispenser, multiplicity=Multiplicity(0, 1)),
        Property(name="payment17", type=Payment, multiplicity=Multiplicity(0, 1))
    }
)
Delivering_Management_Delivery_Boy: BinaryAssociation = BinaryAssociation(
    name="Delivering_Management_Delivery_Boy",
    ends={
        Property(name="delivery_Boy18", type=Delivery_Boy, multiplicity=Multiplicity(0, 1)),
        Property(name="delivering_Management19", type=Delivering_Management, multiplicity=Multiplicity(0, 1))
    }
)
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
        Property(name="delivering_Management4", type=Delivering_Management, multiplicity=Multiplicity(0, 1)),
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
Client_Info: BinaryAssociation = BinaryAssociation(
    name="Client_Info",
    ends={
        Property(name="info20", type=donner_des_informayions_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="client21", type=Client_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Info_Payment: BinaryAssociation = BinaryAssociation(
    name="Info_Payment",
    ends={
        Property(name="payment22", type=Payer_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info23", type=donner_des_informayions_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Info_Cleaning_Management: BinaryAssociation = BinaryAssociation(
    name="Info_Cleaning_Management",
    ends={
        Property(name="cleaning_Management24", type=Lavage_de_la_voiture__UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="info25", type=donner_des_informayions_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_09078ad6_fad7_4c9a_a94b_2883d2044eb4",
    types={User, Cleaning_Management, Money_Dispenser, Primary_Info, Payment, Delivering_Management, Administrator, Cleaner, Delivery_Boy, Client_Actor, Payer_UseCase, donner_des_informayions_UseCase, choisir_le_type_de_lavage_UseCase, D_finir_le_type_de_voiture_UseCase, choisir_le_type_de_payement_UseCase, Prendre_le_re_u_UseCase, Lavage_de_la_voiture__UseCase, Metre_de_la_mousse_UseCase, Rincer_la_voiture__UseCase, Brosser_la_voiture_UseCase},
    associations={User_Delivering_Management, Cleaning_Management_Cleaner, Payment_Money_Dispenser, Delivering_Management_Delivery_Boy, Primary_Info_Payment, Payment_Cleaning_Management, Cleaning_Management_Delivering_Management, User_Primary_Info, User_Payment, User_Cleaning_Management, Client_Info, Info_Payment, Info_Cleaning_Management},
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