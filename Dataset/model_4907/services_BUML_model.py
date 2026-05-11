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
ServiceClassType: Enumeration = Enumeration(
    name="ServiceClassType",
    literals={
            EnumerationLiteral(name="Gold"),
			EnumerationLiteral(name="Silver"),
			EnumerationLiteral(name="Bronze")
    }
)

# Classes
services_CFSService = Class(name="services_CFSService")
Service = Class(name="Service")
services_CIID = Class(name="services_CIID")
services_RFSService = Class(name="services_RFSService")
services_Tolerance = Class(name="services_Tolerance")
services_Service = Class(name="services_Service")
services_Node = Class(name="services_Node")
services_ServiceForecast = Class(name="services_ServiceForecast")
services_ServiceMonitor = Class(name="services_ServiceMonitor")
services_ServiceDistribution = Class(name="services_ServiceDistribution")
services_ServiceUser = Class(name="services_ServiceUser")
services_NetXResource = Class(name="services_NetXResource")
services_Expression = Class(name="services_Expression")
services_DateTimeRange = Class(name="services_DateTimeRange")
services_ResourceForecast = Class(name="services_ResourceForecast")
services_ServiceForecastUsers = Class(name="services_ServiceForecastUsers")
services_ResourceMonitor = Class(name="services_ResourceMonitor")
services_ServiceProfile = Class(name="services_ServiceProfile")
services_Value = Class(name="services_Value")

# services_CFSService class attributes and methods
services_CFSService_provider: Property = Property(name="provider", type=StringType)
services_CFSService_scenario: Property = Property(name="scenario", type=StringType)
services_CFSService.attributes={services_CFSService_scenario, services_CFSService_provider}

# Service class attributes and methods

# services_CIID class attributes and methods
services_CIID_commonCIID: Property = Property(name="commonCIID", type=StringType)
services_CIID_localCIID: Property = Property(name="localCIID", type=StringType)
services_CIID.attributes={services_CIID_localCIID, services_CIID_commonCIID}

# services_RFSService class attributes and methods
services_RFSService_functionalCategory: Property = Property(name="functionalCategory", type=StringType)
services_RFSService.attributes={services_RFSService_functionalCategory}

# services_Tolerance class attributes and methods

# services_Service class attributes and methods
services_Service_serviceCategory: Property = Property(name="serviceCategory", type=StringType)
services_Service_serviceClass: Property = Property(name="serviceClass", type=StringType)
services_Service_serviceName: Property = Property(name="serviceName", type=StringType)
services_Service_serviceDescription: Property = Property(name="serviceDescription", type=StringType)
services_Service.attributes={services_Service_serviceClass, services_Service_serviceCategory, services_Service_serviceName, services_Service_serviceDescription}

# services_Node class attributes and methods

# services_ServiceForecast class attributes and methods
services_ServiceForecast_name: Property = Property(name="name", type=StringType)
services_ServiceForecast_revision: Property = Property(name="revision", type=StringType)
services_ServiceForecast.attributes={services_ServiceForecast_revision, services_ServiceForecast_name}

# services_ServiceMonitor class attributes and methods
services_ServiceMonitor_name: Property = Property(name="name", type=StringType)
services_ServiceMonitor_revision: Property = Property(name="revision", type=StringType)
services_ServiceMonitor.attributes={services_ServiceMonitor_name, services_ServiceMonitor_revision}

# services_ServiceDistribution class attributes and methods

# services_ServiceUser class attributes and methods
services_ServiceUser_name: Property = Property(name="name", type=StringType)
services_ServiceUser.attributes={services_ServiceUser_name}

# services_NetXResource class attributes and methods

# services_Expression class attributes and methods

# services_DateTimeRange class attributes and methods

# services_ResourceForecast class attributes and methods

# services_ServiceForecastUsers class attributes and methods

# services_ResourceMonitor class attributes and methods

# services_ServiceProfile class attributes and methods
services_ServiceProfile_name: Property = Property(name="name", type=StringType)
services_ServiceProfile.attributes={services_ServiceProfile_name}

# services_Value class attributes and methods

# Relationships
toleranceRefs1: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs1",
    ends={
        Property(name="services_Tolerance", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService2", type=services_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="services_Node", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService", type=services_Node, multiplicity=Multiplicity(0, 9999))
    }
)
services5: BinaryAssociation = BinaryAssociation(
    name="services5",
    ends={
        Property(name="services_Service6", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service4", type=services_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceForecasts7: BinaryAssociation = BinaryAssociation(
    name="serviceForecasts7",
    ends={
        Property(name="services_ServiceForecast", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service8", type=services_ServiceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceMonitors9: BinaryAssociation = BinaryAssociation(
    name="serviceMonitors9",
    ends={
        Property(name="services_ServiceMonitor", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service10", type=services_ServiceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cIID3: BinaryAssociation = BinaryAssociation(
    name="cIID3",
    ends={
        Property(name="services_CIID", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service", type=services_CIID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceDistribution13: BinaryAssociation = BinaryAssociation(
    name="serviceDistribution13",
    ends={
        Property(name="services_ServiceDistribution", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service14", type=services_ServiceDistribution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceUserRefs11: BinaryAssociation = BinaryAssociation(
    name="serviceUserRefs11",
    ends={
        Property(name="services_ServiceUser", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service12", type=services_ServiceUser, multiplicity=Multiplicity(0, 9999))
    }
)
expressionRefs17: BinaryAssociation = BinaryAssociation(
    name="expressionRefs17",
    ends={
        Property(name="services_Expression", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution18", type=services_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
period19: BinaryAssociation = BinaryAssociation(
    name="period19",
    ends={
        Property(name="services_DateTimeRange", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast20", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceResources15: BinaryAssociation = BinaryAssociation(
    name="serviceResources15",
    ends={
        Property(name="services_NetXResource", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution16", type=services_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceForecasts23: BinaryAssociation = BinaryAssociation(
    name="resourceForecasts23",
    ends={
        Property(name="services_ResourceForecast", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast24", type=services_ResourceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceForecastUsers21: BinaryAssociation = BinaryAssociation(
    name="serviceForecastUsers21",
    ends={
        Property(name="services_ServiceForecastUsers", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast22", type=services_ServiceForecastUsers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUserRef27: BinaryAssociation = BinaryAssociation(
    name="serviceUserRef27",
    ends={
        Property(name="services_ServiceUser29", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers28", type=services_ServiceUser, multiplicity=Multiplicity(0, 1))
    }
)
period30: BinaryAssociation = BinaryAssociation(
    name="period30",
    ends={
        Property(name="services_DateTimeRange32", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor31", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceMonitors33: BinaryAssociation = BinaryAssociation(
    name="resourceMonitors33",
    ends={
        Property(name="services_ResourceMonitor", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor34", type=services_ResourceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userValues25: BinaryAssociation = BinaryAssociation(
    name="userValues25",
    ends={
        Property(name="services_Value", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers26", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceProfile37: BinaryAssociation = BinaryAssociation(
    name="serviceProfile37",
    ends={
        Property(name="services_ServiceProfile39", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser38", type=services_ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expressionRefs40: BinaryAssociation = BinaryAssociation(
    name="expressionRefs40",
    ends={
        Property(name="services_Expression42", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser41", type=services_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
profileResources35: BinaryAssociation = BinaryAssociation(
    name="profileResources35",
    ends={
        Property(name="services_NetXResource36", type=services_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceProfile", type=services_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_services_CFSService_Service = Generalization(general=Service, specific=services_CFSService)
gen_services_RFSService_Service = Generalization(general=Service, specific=services_RFSService)

# Domain Model
domain_model = DomainModel(
    name="services",
    types={services_CFSService, Service, services_CIID, services_RFSService, services_Tolerance, services_Service, services_Node, services_ServiceForecast, services_ServiceMonitor, services_ServiceDistribution, services_ServiceUser, services_NetXResource, services_Expression, services_DateTimeRange, services_ResourceForecast, services_ServiceForecastUsers, services_ResourceMonitor, services_ServiceProfile, services_Value, ServiceClassType},
    associations={toleranceRefs1, nodes0, services5, serviceForecasts7, serviceMonitors9, cIID3, serviceDistribution13, serviceUserRefs11, expressionRefs17, period19, serviceResources15, resourceForecasts23, serviceForecastUsers21, serviceUserRef27, period30, resourceMonitors33, userValues25, serviceProfile37, expressionRefs40, profileResources35},
    generalizations={gen_services_CFSService_Service, gen_services_RFSService_Service},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)