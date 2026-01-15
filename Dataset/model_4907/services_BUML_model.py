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
ResourceOriginType: Enumeration = Enumeration(
    name="ResourceOriginType",
    literals={
            EnumerationLiteral(name="InBound"),
			EnumerationLiteral(name="OutBound"),
			EnumerationLiteral(name="Internal")
    }
)

ServiceClassType: Enumeration = Enumeration(
    name="ServiceClassType",
    literals={
            EnumerationLiteral(name="Gold"),
			EnumerationLiteral(name="Silver"),
			EnumerationLiteral(name="Bronze")
    }
)

# Classes
services_CFSService = Class(name="services::CFSService")
Service = Class(name="Service")
services_DerivedResource = Class(name="services::DerivedResource")
BaseResource = Class(name="BaseResource")
services_Value = Class(name="services::Value")
services_CIID = Class(name="services::CIID")
Base = Class(name="Base")
services_RFSService = Class(name="services::RFSService")
services_Node = Class(name="services::Node")
services_DistributionEntry = Class(name="services::DistributionEntry")
services_NetXResource = Class(name="services::NetXResource")
services_Service = Class(name="services::Service")
services_Lifecycle = Class(name="services::Lifecycle")
services_ServiceForecast = Class(name="services::ServiceForecast")
services_Tolerance = Class(name="services::Tolerance")
services_ServiceDistribution = Class(name="services::ServiceDistribution")
services_ServiceMonitor = Class(name="services::ServiceMonitor")
services_ServiceUser = Class(name="services::ServiceUser")
services_Expression = Class(name="services::Expression")
services_DateTimeRange = Class(name="services::DateTimeRange")
services_ServiceForecastUsers = Class(name="services::ServiceForecastUsers")
services_ResourceForecast = Class(name="services::ResourceForecast")
services_ServiceProfile = Class(name="services::ServiceProfile")
services_ResourceMonitor = Class(name="services::ResourceMonitor")

# services_CFSService class attributes and methods
services_CFSService_provider: Property = Property(name="provider", type=StringType)
services_CFSService_scenario: Property = Property(name="scenario", type=StringType)
services_CFSService.attributes={services_CFSService_provider, services_CFSService_scenario}

# Service class attributes and methods

# services_DerivedResource class attributes and methods

# BaseResource class attributes and methods

# services_Value class attributes and methods

# services_CIID class attributes and methods
services_CIID_localCIID: Property = Property(name="localCIID", type=StringType)
services_CIID_commonCIID: Property = Property(name="commonCIID", type=StringType)
services_CIID.attributes={services_CIID_localCIID, services_CIID_commonCIID}

# Base class attributes and methods

# services_RFSService class attributes and methods
services_RFSService_functionalCategory: Property = Property(name="functionalCategory", type=StringType)
services_RFSService.attributes={services_RFSService_functionalCategory}

# services_Node class attributes and methods

# services_DistributionEntry class attributes and methods
services_DistributionEntry_resourceOrigin: Property = Property(name="resourceOrigin", type=StringType)
services_DistributionEntry.attributes={services_DistributionEntry_resourceOrigin}

# services_NetXResource class attributes and methods

# services_Service class attributes and methods
services_Service_serviceCategory: Property = Property(name="serviceCategory", type=StringType)
services_Service_serviceClass: Property = Property(name="serviceClass", type=StringType)
services_Service_serviceDescription: Property = Property(name="serviceDescription", type=StringType)
services_Service_serviceName: Property = Property(name="serviceName", type=StringType)
services_Service.attributes={services_Service_serviceCategory, services_Service_serviceClass, services_Service_serviceName, services_Service_serviceDescription}

# services_Lifecycle class attributes and methods

# services_ServiceForecast class attributes and methods
services_ServiceForecast_revision: Property = Property(name="revision", type=StringType)
services_ServiceForecast_name: Property = Property(name="name", type=StringType)
services_ServiceForecast.attributes={services_ServiceForecast_revision, services_ServiceForecast_name}

# services_Tolerance class attributes and methods

# services_ServiceDistribution class attributes and methods

# services_ServiceMonitor class attributes and methods
services_ServiceMonitor_revision: Property = Property(name="revision", type=StringType)
services_ServiceMonitor_name: Property = Property(name="name", type=StringType)
services_ServiceMonitor.attributes={services_ServiceMonitor_revision, services_ServiceMonitor_name}

# services_ServiceUser class attributes and methods
services_ServiceUser_description: Property = Property(name="description", type=StringType)
services_ServiceUser_name: Property = Property(name="name", type=StringType)
services_ServiceUser.attributes={services_ServiceUser_name, services_ServiceUser_description}

# services_Expression class attributes and methods

# services_DateTimeRange class attributes and methods

# services_ServiceForecastUsers class attributes and methods

# services_ResourceForecast class attributes and methods

# services_ServiceProfile class attributes and methods
services_ServiceProfile_name: Property = Property(name="name", type=StringType)
services_ServiceProfile.attributes={services_ServiceProfile_name}

# services_ResourceMonitor class attributes and methods

# Relationships
values0: BinaryAssociation = BinaryAssociation(
    name="values0",
    ends={
        Property(name="services_Value", type=services_DerivedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="services_DerivedResource", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
forecastValues1: BinaryAssociation = BinaryAssociation(
    name="forecastValues1",
    ends={
        Property(name="services_Value3", type=services_DerivedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="services_DerivedResource2", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
trendedValues4: BinaryAssociation = BinaryAssociation(
    name="trendedValues4",
    ends={
        Property(name="services_Value6", type=services_DerivedResource, multiplicity=Multiplicity(1, 1)),
        Property(name="services_DerivedResource5", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
distribution8: BinaryAssociation = BinaryAssociation(
    name="distribution8",
    ends={
        Property(name="services_DerivedResource10", type=services_DistributionEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="services_DistributionEntry9", type=services_DerivedResource, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes11: BinaryAssociation = BinaryAssociation(
    name="nodes11",
    ends={
        Property(name="services_Node", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService", type=services_Node, multiplicity=Multiplicity(0, 9999))
    }
)
resourceRef7: BinaryAssociation = BinaryAssociation(
    name="resourceRef7",
    ends={
        Property(name="services_NetXResource", type=services_DistributionEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="services_DistributionEntry", type=services_NetXResource, multiplicity=Multiplicity(0, 1))
    }
)
cIID14: BinaryAssociation = BinaryAssociation(
    name="cIID14",
    ends={
        Property(name="services_CIID", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service", type=services_CIID, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lifecycle15: BinaryAssociation = BinaryAssociation(
    name="lifecycle15",
    ends={
        Property(name="services_Lifecycle", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service16", type=services_Lifecycle, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
services18: BinaryAssociation = BinaryAssociation(
    name="services18",
    ends={
        Property(name="services_Service19", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service17", type=services_Service, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceForecasts20: BinaryAssociation = BinaryAssociation(
    name="serviceForecasts20",
    ends={
        Property(name="services_ServiceForecast", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service21", type=services_ServiceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toleranceRefs12: BinaryAssociation = BinaryAssociation(
    name="toleranceRefs12",
    ends={
        Property(name="services_Tolerance", type=services_RFSService, multiplicity=Multiplicity(1, 1)),
        Property(name="services_RFSService13", type=services_Tolerance, multiplicity=Multiplicity(0, 9999))
    }
)
serviceDistribution26: BinaryAssociation = BinaryAssociation(
    name="serviceDistribution26",
    ends={
        Property(name="services_ServiceDistribution", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service27", type=services_ServiceDistribution, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceMonitors22: BinaryAssociation = BinaryAssociation(
    name="serviceMonitors22",
    ends={
        Property(name="services_ServiceMonitor", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service23", type=services_ServiceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUserRefs24: BinaryAssociation = BinaryAssociation(
    name="serviceUserRefs24",
    ends={
        Property(name="services_ServiceUser", type=services_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="services_Service25", type=services_ServiceUser, multiplicity=Multiplicity(0, 9999))
    }
)
distributionEntries28: BinaryAssociation = BinaryAssociation(
    name="distributionEntries28",
    ends={
        Property(name="services_DistributionEntry30", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution29", type=services_DistributionEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRefs31: BinaryAssociation = BinaryAssociation(
    name="expressionRefs31",
    ends={
        Property(name="services_Expression", type=services_ServiceDistribution, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceDistribution32", type=services_Expression, multiplicity=Multiplicity(0, 9999))
    }
)
period33: BinaryAssociation = BinaryAssociation(
    name="period33",
    ends={
        Property(name="services_DateTimeRange", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast34", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceForecastUsers35: BinaryAssociation = BinaryAssociation(
    name="serviceForecastUsers35",
    ends={
        Property(name="services_ServiceForecastUsers", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast36", type=services_ServiceForecastUsers, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceForecasts37: BinaryAssociation = BinaryAssociation(
    name="resourceForecasts37",
    ends={
        Property(name="services_ResourceForecast", type=services_ServiceForecast, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecast38", type=services_ResourceForecast, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
userValues39: BinaryAssociation = BinaryAssociation(
    name="userValues39",
    ends={
        Property(name="services_Value41", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers40", type=services_Value, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceUserRef42: BinaryAssociation = BinaryAssociation(
    name="serviceUserRef42",
    ends={
        Property(name="services_ServiceUser44", type=services_ServiceForecastUsers, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceForecastUsers43", type=services_ServiceUser, multiplicity=Multiplicity(0, 1))
    }
)
period45: BinaryAssociation = BinaryAssociation(
    name="period45",
    ends={
        Property(name="services_DateTimeRange47", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor46", type=services_DateTimeRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
profileResources50: BinaryAssociation = BinaryAssociation(
    name="profileResources50",
    ends={
        Property(name="services_DerivedResource51", type=services_ServiceProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceProfile", type=services_DerivedResource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceMonitors48: BinaryAssociation = BinaryAssociation(
    name="resourceMonitors48",
    ends={
        Property(name="services_ResourceMonitor", type=services_ServiceMonitor, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceMonitor49", type=services_ResourceMonitor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expressionRef55: BinaryAssociation = BinaryAssociation(
    name="expressionRef55",
    ends={
        Property(name="services_Expression57", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser56", type=services_Expression, multiplicity=Multiplicity(0, 1))
    }
)
serviceProfile52: BinaryAssociation = BinaryAssociation(
    name="serviceProfile52",
    ends={
        Property(name="services_ServiceProfile54", type=services_ServiceUser, multiplicity=Multiplicity(1, 1)),
        Property(name="services_ServiceUser53", type=services_ServiceProfile, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_services_CFSService_Service = Generalization(general=Service, specific=services_CFSService)
gen_services_DerivedResource_BaseResource = Generalization(general=BaseResource, specific=services_DerivedResource)
gen_services_CIID_Base = Generalization(general=Base, specific=services_CIID)
gen_services_RFSService_Service = Generalization(general=Service, specific=services_RFSService)
gen_services_DistributionEntry_Base = Generalization(general=Base, specific=services_DistributionEntry)
gen_services_Service_Base = Generalization(general=Base, specific=services_Service)
gen_services_ServiceForecast_Base = Generalization(general=Base, specific=services_ServiceForecast)
gen_services_ServiceDistribution_Base = Generalization(general=Base, specific=services_ServiceDistribution)
gen_services_ServiceForecastUsers_Base = Generalization(general=Base, specific=services_ServiceForecastUsers)
gen_services_ServiceMonitor_Base = Generalization(general=Base, specific=services_ServiceMonitor)
gen_services_ServiceProfile_Base = Generalization(general=Base, specific=services_ServiceProfile)
gen_services_ServiceUser_Base = Generalization(general=Base, specific=services_ServiceUser)

# Domain Model
domain_model = DomainModel(
    name="services",
    types={services_CFSService, Service, services_DerivedResource, BaseResource, services_Value, services_CIID, Base, services_RFSService, services_Node, services_DistributionEntry, services_NetXResource, services_Service, services_Lifecycle, services_ServiceForecast, services_Tolerance, services_ServiceDistribution, services_ServiceMonitor, services_ServiceUser, services_Expression, services_DateTimeRange, services_ServiceForecastUsers, services_ResourceForecast, services_ServiceProfile, services_ResourceMonitor, ResourceOriginType, ServiceClassType},
    associations={values0, forecastValues1, trendedValues4, distribution8, nodes11, resourceRef7, cIID14, lifecycle15, services18, serviceForecasts20, toleranceRefs12, serviceDistribution26, serviceMonitors22, serviceUserRefs24, distributionEntries28, expressionRefs31, period33, serviceForecastUsers35, resourceForecasts37, userValues39, serviceUserRef42, period45, profileResources50, resourceMonitors48, expressionRef55, serviceProfile52},
    generalizations={gen_services_CFSService_Service, gen_services_DerivedResource_BaseResource, gen_services_CIID_Base, gen_services_RFSService_Service, gen_services_DistributionEntry_Base, gen_services_Service_Base, gen_services_ServiceForecast_Base, gen_services_ServiceDistribution_Base, gen_services_ServiceForecastUsers_Base, gen_services_ServiceMonitor_Base, gen_services_ServiceProfile_Base, gen_services_ServiceUser_Base},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)