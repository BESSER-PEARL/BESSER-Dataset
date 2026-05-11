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
services_Service = Class(name="services_Service")
services_ServiceForecast = Class(name="services_ServiceForecast")
services_ServiceMonitor = Class(name="services_ServiceMonitor")
services_ServiceUser = Class(name="services_ServiceUser")
services_EObject = Class(name="services_EObject")
services_NetXResource = Class(name="services_NetXResource")
services_Expression = Class(name="services_Expression")
services_ServiceDistribution = Class(name="services_ServiceDistribution")
services_ServiceForecastUsers = Class(name="services_ServiceForecastUsers")
services_ResourceForecast = Class(name="services_ResourceForecast")
services_Value = Class(name="services_Value")
services_DateTimeRange = Class(name="services_DateTimeRange")
services_ServiceProfile = Class(name="services_ServiceProfile")
services_ResourceMonitor = Class(name="services_ResourceMonitor")

# services_CFSService class attributes and methods
services_CFSService_provider: Property = Property(name="provider", type=StringType)
services_CFSService_scenario: Property = Property(name="scenario", type=StringType)
services_CFSService.attributes={services_CFSService_provider, services_CFSService_scenario}

# Service class attributes and methods

# services_CIID class attributes and methods
services_CIID_commonCIID: Property = Property(name="commonCIID", type=StringType)
services_CIID_localCIID: Property = Property(name="localCIID", type=StringType)
services_CIID.attributes={services_CIID_commonCIID, services_CIID_localCIID}

# services_RFSService class attributes and methods
services_RFSService_functionalCategory: Property = Property(name="functionalCategory", type=StringType)
services_RFSService.attributes={services_RFSService_functionalCategory}

# services_Service class attributes and methods
services_Service_serviceClass: Property = Property(name="serviceClass", type=StringType)
services_Service_serviceDescription: Property = Property(name="serviceDescription", type=StringType)
services_Service_serviceName: Property = Property(name="serviceName", type=StringType)
services_Service_serviceCategory: Property = Property(name="serviceCategory", type=StringType)
services_Service.attributes={services_Service_serviceDescription, services_Service_serviceClass, services_Service_serviceName, services_Service_serviceCategory}

# services_ServiceForecast class attributes and methods
services_ServiceForecast_name: Property = Property(name="name", type=StringType)
services_ServiceForecast_revision: Property = Property(name="revision", type=StringType)
services_ServiceForecast.attributes={services_ServiceForecast_name, services_ServiceForecast_revision}

# services_ServiceMonitor class attributes and methods
services_ServiceMonitor_name: Property = Property(name="name", type=StringType)
services_ServiceMonitor_revision: Property = Property(name="revision", type=StringType)
services_ServiceMonitor.attributes={services_ServiceMonitor_name, services_ServiceMonitor_revision}

# services_ServiceUser class attributes and methods
services_ServiceUser_name: Property = Property(name="name", type=StringType)
services_ServiceUser.attributes={services_ServiceUser_name}

# services_EObject class attributes and methods

# services_NetXResource class attributes and methods

# services_Expression class attributes and methods

# services_ServiceDistribution class attributes and methods

# services_ServiceForecastUsers class attributes and methods

# services_ResourceForecast class attributes and methods

# services_Value class attributes and methods

# services_DateTimeRange class attributes and methods

# services_ServiceProfile class attributes and methods
services_ServiceProfile_name: Property = Property(name="name", type=StringType)
services_ServiceProfile.attributes={services_ServiceProfile_name}

# services_ResourceMonitor class attributes and methods

# Relationships
cIID4: BinaryAssociation = BinaryAssociation(
    name="cIID4",
    ends={
        Property(name="services_CIID", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service", type=services_CIID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
services6: BinaryAssociation = BinaryAssociation(
    name="services6",
    ends={
        Property(name="services_Service7", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service5", type=services_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceForecasts8: BinaryAssociation = BinaryAssociation(
    name="serviceForecasts8",
    ends={
        Property(name="services_ServiceForecast", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service9", type=services_ServiceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceMonitors10: BinaryAssociation = BinaryAssociation(
    name="serviceMonitors10",
    ends={
        Property(name="services_ServiceMonitor", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service11", type=services_ServiceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="services_EObject", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService", type=services_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
toleranceRefs1: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs1",
    ends={
        Property(name="services_EObject3", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService2", type=services_EObject, multiplicity=Multiplicity(0, 9999))
    }
)
serviceResources16: BinaryAssociation = BinaryAssociation(
    name="serviceResources16",
    ends={
        Property(name="services_NetXResource", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution17", type=services_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs18: BinaryAssociation = BinaryAssociation(
    name="expressionRefs18",
    ends={
        Property(name="services_Expression", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution19", type=services_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
serviceUserRefs12: BinaryAssociation = BinaryAssociation(
    name="serviceUserRefs12",
    ends={
        Property(name="services_ServiceUser", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service13", type=services_ServiceUser, multiplicity=Multiplicity(0, 9999))
    }
)
serviceDistribution14: BinaryAssociation = BinaryAssociation(
    name="serviceDistribution14",
    ends={
        Property(name="services_ServiceDistribution", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service15", type=services_ServiceDistribution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceForecastUsers22: BinaryAssociation = BinaryAssociation(
    name="serviceForecastUsers22",
    ends={
        Property(name="services_ServiceForecastUsers", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast23", type=services_ServiceForecastUsers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceForecasts24: BinaryAssociation = BinaryAssociation(
    name="resourceForecasts24",
    ends={
        Property(name="services_ResourceForecast", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast25", type=services_ResourceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userValues26: BinaryAssociation = BinaryAssociation(
    name="userValues26",
    ends={
        Property(name="services_Value", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers27", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUserRef28: BinaryAssociation = BinaryAssociation(
    name="serviceUserRef28",
    ends={
        Property(name="services_ServiceUser30", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers29", type=services_ServiceUser, multiplicity=Multiplicity(0, 1))
    }
)
period20: BinaryAssociation = BinaryAssociation(
    name="period20",
    ends={
        Property(name="services_DateTimeRange", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast21", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
profileResources36: BinaryAssociation = BinaryAssociation(
    name="profileResources36",
    ends={
        Property(name="services_NetXResource37", type=services_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceProfile", type=services_NetXResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceProfile38: BinaryAssociation = BinaryAssociation(
    name="serviceProfile38",
    ends={
        Property(name="services_ServiceProfile40", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser39", type=services_ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
period31: BinaryAssociation = BinaryAssociation(
    name="period31",
    ends={
        Property(name="services_DateTimeRange33", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor32", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resourceMonitors34: BinaryAssociation = BinaryAssociation(
    name="resourceMonitors34",
    ends={
        Property(name="services_ResourceMonitor", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor35", type=services_ResourceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs41: BinaryAssociation = BinaryAssociation(
    name="expressionRefs41",
    ends={
        Property(name="services_Expression43", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser42", type=services_Expression, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_services_CFSService_Service = Generalization(general=Service, specific=services_CFSService)
gen_services_RFSService_Service = Generalization(general=Service, specific=services_RFSService)

# Domain Model
domain_model = DomainModel(
    name="services",
    types={services_CFSService, Service, services_CIID, services_RFSService, services_Service, services_ServiceForecast, services_ServiceMonitor, services_ServiceUser, services_EObject, services_NetXResource, services_Expression, services_ServiceDistribution, services_ServiceForecastUsers, services_ResourceForecast, services_Value, services_DateTimeRange, services_ServiceProfile, services_ResourceMonitor, ServiceClassType},
    associations={cIID4, services6, serviceForecasts8, serviceMonitors10, nodes0, toleranceRefs1, serviceResources16, expressionRefs18, serviceUserRefs12, serviceDistribution14, serviceForecastUsers22, resourceForecasts24, userValues26, serviceUserRef28, period20, profileResources36, serviceProfile38, period31, resourceMonitors34, expressionRefs41},
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