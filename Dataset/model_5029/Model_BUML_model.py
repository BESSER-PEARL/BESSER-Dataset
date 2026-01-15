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
ShipmentStatus: Enumeration = Enumeration(
    name="ShipmentStatus",
    literals={
            EnumerationLiteral(name="NEW"),
			EnumerationLiteral(name="ASSIGNED"),
			EnumerationLiteral(name="UNDERWAY"),
			EnumerationLiteral(name="DELIVERED")
    }
)

# Classes
pickupnet_Station = Class(name="pickupnet::Station")
pickupnet_Address = Class(name="pickupnet::Address")
pickupnet_GeoLocation = Class(name="pickupnet::GeoLocation")
pickupnet_Customer = Class(name="pickupnet::Customer")
pickupnet_Driver = Class(name="pickupnet::Driver")
pickupnet_Shipment = Class(name="pickupnet::Shipment")

# pickupnet_Station class attributes and methods
pickupnet_Station_m_registerCustomer: Method = Method(name="registerCustomer", parameters={Parameter(name='customer')})
pickupnet_Station_m_registerDriver: Method = Method(name="registerDriver", parameters={Parameter(name='driver')})
pickupnet_Station_m_acceptShipment: Method = Method(name="acceptShipment", parameters={Parameter(name='shipment')})
pickupnet_Station.methods={pickupnet_Station_m_registerCustomer, pickupnet_Station_m_acceptShipment, pickupnet_Station_m_registerDriver}

# pickupnet_Address class attributes and methods
pickupnet_Address_text: Property = Property(name="text", type=StringType)
pickupnet_Address.attributes={pickupnet_Address_text}

# pickupnet_GeoLocation class attributes and methods
pickupnet_GeoLocation_lat: Property = Property(name="lat", type=FloatType)
pickupnet_GeoLocation_lon: Property = Property(name="lon", type=FloatType)
pickupnet_GeoLocation.attributes={pickupnet_GeoLocation_lat, pickupnet_GeoLocation_lon}

# pickupnet_Customer class attributes and methods
pickupnet_Customer_id: Property = Property(name="id", type=StringType)
pickupnet_Customer_name: Property = Property(name="name", type=StringType)
pickupnet_Customer_twitterUserName: Property = Property(name="twitterUserName", type=StringType)
pickupnet_Customer.attributes={pickupnet_Customer_twitterUserName, pickupnet_Customer_id, pickupnet_Customer_name}

# pickupnet_Driver class attributes and methods
pickupnet_Driver_id: Property = Property(name="id", type=StringType)
pickupnet_Driver_name: Property = Property(name="name", type=StringType)
pickupnet_Driver.attributes={pickupnet_Driver_id, pickupnet_Driver_name}

# pickupnet_Shipment class attributes and methods
pickupnet_Shipment_id: Property = Property(name="id", type=StringType)
pickupnet_Shipment_status: Property = Property(name="status", type=StringType)
pickupnet_Shipment.attributes={pickupnet_Shipment_id, pickupnet_Shipment_status}

# Relationships
orderer9: BinaryAssociation = BinaryAssociation(
    name="orderer9",
    ends={
        Property(name="Customer", type=pickupnet_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="orders", type=pickupnet_Customer, multiplicity=Multiplicity(1, 1))
    }
)
shipToAddress10: BinaryAssociation = BinaryAssociation(
    name="shipToAddress10",
    ends={
        Property(name="pickupnet_Address", type=pickupnet_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Shipment11", type=pickupnet_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
pickUpAddress12: BinaryAssociation = BinaryAssociation(
    name="pickUpAddress12",
    ends={
        Property(name="pickupnet_Address14", type=pickupnet_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Shipment13", type=pickupnet_Address, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
geoLocation15: BinaryAssociation = BinaryAssociation(
    name="geoLocation15",
    ends={
        Property(name="pickupnet_GeoLocation", type=pickupnet_Address, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Address16", type=pickupnet_GeoLocation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
customers0: BinaryAssociation = BinaryAssociation(
    name="customers0",
    ends={
        Property(name="pickupnet_Customer", type=pickupnet_Station, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Station", type=pickupnet_Customer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
drivers1: BinaryAssociation = BinaryAssociation(
    name="drivers1",
    ends={
        Property(name="pickupnet_Driver", type=pickupnet_Station, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Station2", type=pickupnet_Driver, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
shipments3: BinaryAssociation = BinaryAssociation(
    name="shipments3",
    ends={
        Property(name="pickupnet_Shipment", type=pickupnet_Station, multiplicity=Multiplicity(1, 1)),
        Property(name="pickupnet_Station4", type=pickupnet_Shipment, multiplicity=Multiplicity(0, 9999))
    }
)
assignments5: BinaryAssociation = BinaryAssociation(
    name="assignments5",
    ends={
        Property(name="Shipment", type=pickupnet_Driver, multiplicity=Multiplicity(1, 1)),
        Property(name="driver", type=pickupnet_Shipment, multiplicity=Multiplicity(0, 9999))
    }
)
orders6: BinaryAssociation = BinaryAssociation(
    name="orders6",
    ends={
        Property(name="Shipment7", type=pickupnet_Customer, multiplicity=Multiplicity(1, 1)),
        Property(name="orderer", type=pickupnet_Shipment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
driver8: BinaryAssociation = BinaryAssociation(
    name="driver8",
    ends={
        Property(name="Driver", type=pickupnet_Shipment, multiplicity=Multiplicity(1, 1)),
        Property(name="assignments", type=pickupnet_Driver, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="pickupnet",
    types={pickupnet_Station, pickupnet_Address, pickupnet_GeoLocation, pickupnet_Customer, pickupnet_Driver, pickupnet_Shipment, ShipmentStatus},
    associations={orderer9, shipToAddress10, pickUpAddress12, geoLocation15, customers0, drivers1, shipments3, assignments5, orders6, driver8},
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