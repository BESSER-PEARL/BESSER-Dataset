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
model_IServiceInfo = Class(name="model::IServiceInfo")
model_IServiceID = Class(name="model::IServiceID")
model_IServiceTypeID = Class(name="model::IServiceTypeID")
model_INetwork = Class(name="model::INetwork")
model_IHost = Class(name="model::IHost")

# model_IServiceInfo class attributes and methods
model_IServiceInfo_ecfServiceInfo: Property = Property(name="ecfServiceInfo", type=StringType)
model_IServiceInfo_ecfName: Property = Property(name="ecfName", type=StringType)
model_IServiceInfo_ecfLocation: Property = Property(name="ecfLocation", type=StringType)
model_IServiceInfo_ecfPriority: Property = Property(name="ecfPriority", type=IntegerType)
model_IServiceInfo_ecfWeight: Property = Property(name="ecfWeight", type=IntegerType)
model_IServiceInfo.attributes={model_IServiceInfo_ecfServiceInfo, model_IServiceInfo_ecfName, model_IServiceInfo_ecfPriority, model_IServiceInfo_ecfWeight, model_IServiceInfo_ecfLocation}

# model_IServiceID class attributes and methods
model_IServiceID_ecfServiceID: Property = Property(name="ecfServiceID", type=StringType)
model_IServiceID_ecfServiceName: Property = Property(name="ecfServiceName", type=StringType)
model_IServiceID.attributes={model_IServiceID_ecfServiceID, model_IServiceID_ecfServiceName}

# model_IServiceTypeID class attributes and methods
model_IServiceTypeID_ecfServiceTypeID: Property = Property(name="ecfServiceTypeID", type=StringType)
model_IServiceTypeID_ecfNamingAuthority: Property = Property(name="ecfNamingAuthority", type=StringType)
model_IServiceTypeID_ecfServices: Property = Property(name="ecfServices", type=StringType)
model_IServiceTypeID_ecfProtocols: Property = Property(name="ecfProtocols", type=StringType)
model_IServiceTypeID_ecfScopes: Property = Property(name="ecfScopes", type=StringType)
model_IServiceTypeID_ecfServiceName: Property = Property(name="ecfServiceName", type=StringType)
model_IServiceTypeID.attributes={model_IServiceTypeID_ecfServiceTypeID, model_IServiceTypeID_ecfProtocols, model_IServiceTypeID_ecfScopes, model_IServiceTypeID_ecfServices, model_IServiceTypeID_ecfNamingAuthority, model_IServiceTypeID_ecfServiceName}

# model_INetwork class attributes and methods

# model_IHost class attributes and methods
model_IHost_name: Property = Property(name="name", type=StringType)
model_IHost_address: Property = Property(name="address", type=StringType)
model_IHost.attributes={model_IHost_name, model_IHost_address}

# Relationships
serviceID0: BinaryAssociation = BinaryAssociation(
    name="serviceID0",
    ends={
        Property(name="model_IServiceID", type=model_IServiceInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IServiceInfo", type=model_IServiceID, multiplicity=Multiplicity(0, 1))
    }
)
serviceTypeID5: BinaryAssociation = BinaryAssociation(
    name="serviceTypeID5",
    ends={
        Property(name="model_IServiceTypeID", type=model_IServiceID, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IServiceID6", type=model_IServiceTypeID, multiplicity=Multiplicity(0, 1))
    }
)
hosts1: BinaryAssociation = BinaryAssociation(
    name="hosts1",
    ends={
        Property(name="model_IHost", type=model_INetwork, multiplicity=Multiplicity(1, 1)),
        Property(name="model_INetwork", type=model_IHost, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services2: BinaryAssociation = BinaryAssociation(
    name="services2",
    ends={
        Property(name="model_IServiceInfo4", type=model_IHost, multiplicity=Multiplicity(1, 1)),
        Property(name="model_IHost3", type=model_IServiceInfo, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_IServiceInfo, model_IServiceID, model_IServiceTypeID, model_INetwork, model_IHost},
    associations={serviceID0, serviceTypeID5, hosts1, services2},
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