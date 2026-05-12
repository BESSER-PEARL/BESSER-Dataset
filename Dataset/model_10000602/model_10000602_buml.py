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

# Enumerations
CustomerType: Enumeration = Enumeration(
    name="CustomerType",
    literals={
            
    }
)

# Classes
Customer = Class(name="Customer")
ActiveRecord = Class(name="ActiveRecord")
ConnectionInterface_Interface = Class(name="ConnectionInterface_Interface")
Car = Class(name="Car")
Sale = Class(name="Sale")
RepairPart = Class(name="RepairPart")
Repair = Class(name="Repair")
Customer_Actor = Class(name="Customer_Actor")
Enquire_for_Cars_UseCase = Class(name="Enquire_for_Cars_UseCase")
Purchase_Car_UseCase = Class(name="Purchase_Car_UseCase")
Send_for_Repair_UseCase = Class(name="Send_for_Repair_UseCase")
Dealer_Actor = Class(name="Dealer_Actor")
Maintenance_Team_Actor = Class(name="Maintenance_Team_Actor")
Repair_Part_Purchase_UseCase = Class(name="Repair_Part_Purchase_UseCase")
Check_for_Parts_UseCase = Class(name="Check_for_Parts_UseCase")
Check_Car_Stock_UseCase = Class(name="Check_Car_Stock_UseCase")
Compute_Billables_UseCase = Class(name="Compute_Billables_UseCase")
Order_Cars_UseCase = Class(name="Order_Cars_UseCase")
Manufacturer_Actor = Class(name="Manufacturer_Actor")

# Customer class attributes and methods
Customer_name: Property = Property(name="name", type=StringType)
Customer_address: Property = Property(name="address", type=StringType)
Customer_type: Property = Property(name="type", type=CustomerType)
Customer.attributes={Customer_name, Customer_type, Customer_address}

# ActiveRecord class attributes and methods
ActiveRecord_connection: Property = Property(name="connection", type=ConnectionInterface_Interface)
ActiveRecord_id: Property = Property(name="id", type=IntegerType)
ActiveRecord.attributes={ActiveRecord_id, ActiveRecord_connection}

# ConnectionInterface_Interface class attributes and methods

# Car class attributes and methods
Car_name: Property = Property(name="name", type=StringType)
Car_manufacturer: Property = Property(name="manufacturer", type=StringType)
Car_stock: Property = Property(name="stock", type=IntegerType)
Car_cost: Property = Property(name="cost", type=StringType)
Car.attributes={Car_name, Car_cost, Car_stock, Car_manufacturer}

# Sale class attributes and methods
Sale_date: Property = Property(name="date", type=DateType)
Sale_customer: Property = Property(name="customer", type=Customer)
Sale_car: Property = Property(name="car", type=Car)
Sale_billable: Property = Property(name="billable", type=StringType)
Sale.attributes={Sale_customer, Sale_billable, Sale_car, Sale_date}

# RepairPart class attributes and methods
RepairPart_name: Property = Property(name="name", type=StringType)
RepairPart_cost: Property = Property(name="cost", type=StringType)
RepairPart_stock: Property = Property(name="stock", type=IntegerType)
RepairPart.attributes={RepairPart_name, RepairPart_stock, RepairPart_cost}

# Repair class attributes and methods
Repair_car: Property = Property(name="car", type=Car)
Repair_customer: Property = Property(name="customer", type=Customer)
Repair_part: Property = Property(name="part", type=RepairPart)
Repair_date: Property = Property(name="date", type=DateType)
Repair.attributes={Repair_date, Repair_part, Repair_car, Repair_customer}

# Customer_Actor class attributes and methods

# Enquire_for_Cars_UseCase class attributes and methods

# Purchase_Car_UseCase class attributes and methods

# Send_for_Repair_UseCase class attributes and methods

# Dealer_Actor class attributes and methods

# Maintenance_Team_Actor class attributes and methods

# Repair_Part_Purchase_UseCase class attributes and methods

# Check_for_Parts_UseCase class attributes and methods

# Check_Car_Stock_UseCase class attributes and methods

# Compute_Billables_UseCase class attributes and methods

# Order_Cars_UseCase class attributes and methods

# Manufacturer_Actor class attributes and methods

# Relationships
Customer_Enquire_for_Cars: BinaryAssociation = BinaryAssociation(
    name="Customer_Enquire_for_Cars",
    ends={
        Property(name="enquire_for_Cars0", type=Enquire_for_Cars_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer1", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Purchase_Car: BinaryAssociation = BinaryAssociation(
    name="Customer_Purchase_Car",
    ends={
        Property(name="purchase_Car2", type=Purchase_Car_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer3", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Customer_Send_for_Repair: BinaryAssociation = BinaryAssociation(
    name="Customer_Send_for_Repair",
    ends={
        Property(name="send_for_Repair4", type=Send_for_Repair_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="customer5", type=Customer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Enquire_for_Cars: BinaryAssociation = BinaryAssociation(
    name="Dealer_Enquire_for_Cars",
    ends={
        Property(name="enquire_for_Cars6", type=Enquire_for_Cars_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer7", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Purchase_Car: BinaryAssociation = BinaryAssociation(
    name="Dealer_Purchase_Car",
    ends={
        Property(name="purchase_Car8", type=Purchase_Car_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer9", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Send_for_Repair: BinaryAssociation = BinaryAssociation(
    name="Dealer_Send_for_Repair",
    ends={
        Property(name="send_for_Repair10", type=Send_for_Repair_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer11", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Maintenance_Team_Send_for_Repair: BinaryAssociation = BinaryAssociation(
    name="Maintenance_Team_Send_for_Repair",
    ends={
        Property(name="send_for_Repair12", type=Send_for_Repair_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="maintenance_Team13", type=Maintenance_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Maintenance_Team_Repair_Part_Purchase: BinaryAssociation = BinaryAssociation(
    name="Maintenance_Team_Repair_Part_Purchase",
    ends={
        Property(name="repair_Part_Purchase14", type=Repair_Part_Purchase_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="maintenance_Team15", type=Maintenance_Team_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dealer_Order_Cars: BinaryAssociation = BinaryAssociation(
    name="Dealer_Order_Cars",
    ends={
        Property(name="order_Cars16", type=Order_Cars_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="dealer17", type=Dealer_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Manufacturer_Order_Cars: BinaryAssociation = BinaryAssociation(
    name="Manufacturer_Order_Cars",
    ends={
        Property(name="order_Cars18", type=Order_Cars_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="manufacturer19", type=Manufacturer_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_49a47981_58a0_482a_8e2d_4be712253b85",
    types={Customer, ActiveRecord, ConnectionInterface_Interface, Car, Sale, RepairPart, Repair, Customer_Actor, Enquire_for_Cars_UseCase, Purchase_Car_UseCase, Send_for_Repair_UseCase, Dealer_Actor, Maintenance_Team_Actor, Repair_Part_Purchase_UseCase, Check_for_Parts_UseCase, Check_Car_Stock_UseCase, Compute_Billables_UseCase, Order_Cars_UseCase, Manufacturer_Actor, CustomerType},
    associations={Customer_Enquire_for_Cars, Customer_Purchase_Car, Customer_Send_for_Repair, Dealer_Enquire_for_Cars, Dealer_Purchase_Car, Dealer_Send_for_Repair, Maintenance_Team_Send_for_Repair, Maintenance_Team_Repair_Part_Purchase, Dealer_Order_Cars, Manufacturer_Order_Cars},
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