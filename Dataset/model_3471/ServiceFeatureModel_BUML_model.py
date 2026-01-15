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
AttributeDomain: Enumeration = Enumeration(
    name="AttributeDomain",
    literals={
            EnumerationLiteral(name="Continuous"),
			EnumerationLiteral(name="Boolean")
    }
)

AggregationRules: Enumeration = Enumeration(
    name="AggregationRules",
    literals={
            EnumerationLiteral(name="Sum"),
			EnumerationLiteral(name="Product"),
			EnumerationLiteral(name="AtLeastOnce"),
			EnumerationLiteral(name="Minimum"),
			EnumerationLiteral(name="Maximum")
    }
)

ScaleOrders: Enumeration = Enumeration(
    name="ScaleOrders",
    literals={
            EnumerationLiteral(name="HigherIsBetter"),
			EnumerationLiteral(name="LowerIsBetter"),
			EnumerationLiteral(name="ExistenceIsBetter")
    }
)

FeatureTypes: Enumeration = Enumeration(
    name="FeatureTypes",
    literals={
            EnumerationLiteral(name="GroupingFeature"),
			EnumerationLiteral(name="AbstractFeature"),
			EnumerationLiteral(name="InstanceFeature")
    }
)

# Classes
servicefeaturemodel_Service = Class(name="servicefeaturemodel::Service")
servicefeaturemodel_ServiceFeatureDiagram = Class(name="servicefeaturemodel::ServiceFeatureDiagram")
servicefeaturemodel_Configurations = Class(name="servicefeaturemodel::Configurations")
servicefeaturemodel_AttributeTypes = Class(name="servicefeaturemodel::AttributeTypes")
servicefeaturemodel_Excludes = Class(name="servicefeaturemodel::Excludes")
servicefeaturemodel_OptionalServiceFeature = Class(name="servicefeaturemodel::OptionalServiceFeature")
ServiceFeature = Class(name="ServiceFeature")
servicefeaturemodel_AttributeType = Class(name="servicefeaturemodel::AttributeType")
servicefeaturemodel_ServiceFeature = Class(name="servicefeaturemodel::ServiceFeature", is_abstract=True)
servicefeaturemodel_Attribute = Class(name="servicefeaturemodel::Attribute")
servicefeaturemodel_GroupRelationship = Class(name="servicefeaturemodel::GroupRelationship", is_abstract=True)
servicefeaturemodel_Requires = Class(name="servicefeaturemodel::Requires")
servicefeaturemodel_XOR = Class(name="servicefeaturemodel::XOR")
servicefeaturemodel_Configuration = Class(name="servicefeaturemodel::Configuration")
servicefeaturemodel_OR = Class(name="servicefeaturemodel::OR")
GroupRelationship = Class(name="GroupRelationship")
servicefeaturemodel_MandatoryServiceFeature = Class(name="servicefeaturemodel::MandatoryServiceFeature")
servicefeaturemodel_Preference = Class(name="servicefeaturemodel::Preference")

# servicefeaturemodel_Service class attributes and methods
servicefeaturemodel_Service_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Service_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Service_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_Service.attributes={servicefeaturemodel_Service_description, servicefeaturemodel_Service_name, servicefeaturemodel_Service_id}

# servicefeaturemodel_ServiceFeatureDiagram class attributes and methods
servicefeaturemodel_ServiceFeatureDiagram_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram.attributes={servicefeaturemodel_ServiceFeatureDiagram_name, servicefeaturemodel_ServiceFeatureDiagram_id, servicefeaturemodel_ServiceFeatureDiagram_description}

# servicefeaturemodel_Configurations class attributes and methods

# servicefeaturemodel_AttributeTypes class attributes and methods

# servicefeaturemodel_Excludes class attributes and methods

# servicefeaturemodel_OptionalServiceFeature class attributes and methods
servicefeaturemodel_OptionalServiceFeature_featureType: Property = Property(name="featureType", type=StringType)
servicefeaturemodel_OptionalServiceFeature.attributes={servicefeaturemodel_OptionalServiceFeature_featureType}

# ServiceFeature class attributes and methods

# servicefeaturemodel_AttributeType class attributes and methods
servicefeaturemodel_AttributeType_requirementWeight: Property = Property(name="requirementWeight", type=StringType)
servicefeaturemodel_AttributeType_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_AttributeType_domain: Property = Property(name="domain", type=StringType)
servicefeaturemodel_AttributeType_aggregationRule: Property = Property(name="aggregationRule", type=StringType)
servicefeaturemodel_AttributeType_scaleOrder: Property = Property(name="scaleOrder", type=StringType)
servicefeaturemodel_AttributeType_toBeEvaluated: Property = Property(name="toBeEvaluated", type=BooleanType)
servicefeaturemodel_AttributeType_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_AttributeType_customAttributeTypePriority: Property = Property(name="customAttributeTypePriority", type=IntegerType)
servicefeaturemodel_AttributeType_requirement: Property = Property(name="requirement", type=StringType)
servicefeaturemodel_AttributeType.attributes={servicefeaturemodel_AttributeType_aggregationRule, servicefeaturemodel_AttributeType_toBeEvaluated, servicefeaturemodel_AttributeType_name, servicefeaturemodel_AttributeType_requirement, servicefeaturemodel_AttributeType_scaleOrder, servicefeaturemodel_AttributeType_requirementWeight, servicefeaturemodel_AttributeType_domain, servicefeaturemodel_AttributeType_description, servicefeaturemodel_AttributeType_customAttributeTypePriority}

# servicefeaturemodel_ServiceFeature class attributes and methods
servicefeaturemodel_ServiceFeature_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_ServiceFeature_required: Property = Property(name="required", type=BooleanType)
servicefeaturemodel_ServiceFeature_requirementWeight: Property = Property(name="requirementWeight", type=StringType)
servicefeaturemodel_ServiceFeature_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_ServiceFeature_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_ServiceFeature.attributes={servicefeaturemodel_ServiceFeature_requirementWeight, servicefeaturemodel_ServiceFeature_id, servicefeaturemodel_ServiceFeature_description, servicefeaturemodel_ServiceFeature_required, servicefeaturemodel_ServiceFeature_name}

# servicefeaturemodel_Attribute class attributes and methods
servicefeaturemodel_Attribute_instantiationValue: Property = Property(name="instantiationValue", type=StringType)
servicefeaturemodel_Attribute_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Attribute.attributes={servicefeaturemodel_Attribute_id, servicefeaturemodel_Attribute_instantiationValue}

# servicefeaturemodel_GroupRelationship class attributes and methods

# servicefeaturemodel_Requires class attributes and methods

# servicefeaturemodel_XOR class attributes and methods

# servicefeaturemodel_Configuration class attributes and methods
servicefeaturemodel_Configuration_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_Configuration_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Configuration_selected: Property = Property(name="selected", type=BooleanType)
servicefeaturemodel_Configuration_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Configuration_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
servicefeaturemodel_Configuration.attributes={servicefeaturemodel_Configuration_selected, servicefeaturemodel_Configuration_description, servicefeaturemodel_Configuration_name, servicefeaturemodel_Configuration_id}
servicefeaturemodel_Configuration.methods={servicefeaturemodel_Configuration_m_validate}

# servicefeaturemodel_OR class attributes and methods
servicefeaturemodel_OR_minFeaturesToChoose: Property = Property(name="minFeaturesToChoose", type=IntegerType)
servicefeaturemodel_OR_maxFeaturesToChoose: Property = Property(name="maxFeaturesToChoose", type=IntegerType)
servicefeaturemodel_OR.attributes={servicefeaturemodel_OR_minFeaturesToChoose, servicefeaturemodel_OR_maxFeaturesToChoose}

# GroupRelationship class attributes and methods

# servicefeaturemodel_MandatoryServiceFeature class attributes and methods
servicefeaturemodel_MandatoryServiceFeature_featureTypes: Property = Property(name="featureTypes", type=StringType)
servicefeaturemodel_MandatoryServiceFeature.attributes={servicefeaturemodel_MandatoryServiceFeature_featureTypes}

# servicefeaturemodel_Preference class attributes and methods
servicefeaturemodel_Preference_creationDate: Property = Property(name="creationDate", type=DateType)
servicefeaturemodel_Preference_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Preference_value: Property = Property(name="value", type=FloatType)
servicefeaturemodel_Preference_stakeholderGroup: Property = Property(name="stakeholderGroup", type=StringType)
servicefeaturemodel_Preference.attributes={servicefeaturemodel_Preference_description, servicefeaturemodel_Preference_value, servicefeaturemodel_Preference_stakeholderGroup, servicefeaturemodel_Preference_creationDate}

# Relationships
serviceFeatureDiagram0: BinaryAssociation = BinaryAssociation(
    name="serviceFeatureDiagram0",
    ends={
        Property(name="servicefeaturemodel_ServiceFeatureDiagram", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service", type=servicefeaturemodel_ServiceFeatureDiagram, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
configurations1: BinaryAssociation = BinaryAssociation(
    name="configurations1",
    ends={
        Property(name="servicefeaturemodel_Configurations", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service2", type=servicefeaturemodel_Configurations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
attributeTypes3: BinaryAssociation = BinaryAssociation(
    name="attributeTypes3",
    ends={
        Property(name="servicefeaturemodel_AttributeTypes", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service4", type=servicefeaturemodel_AttributeTypes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
requires8: BinaryAssociation = BinaryAssociation(
    name="requires8",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature9", type=servicefeaturemodel_Requires, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="servicefeaturemodel_Requires", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)
excludes10: BinaryAssociation = BinaryAssociation(
    name="excludes10",
    ends={
        Property(name="servicefeaturemodel_Excludes", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature11", type=servicefeaturemodel_Excludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceFeatures13: BinaryAssociation = BinaryAssociation(
    name="serviceFeatures13",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature14", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature12", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeType15: BinaryAssociation = BinaryAssociation(
    name="attributeType15",
    ends={
        Property(name="servicefeaturemodel_AttributeType", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Attribute16", type=servicefeaturemodel_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
attributes5: BinaryAssociation = BinaryAssociation(
    name="attributes5",
    ends={
        Property(name="servicefeaturemodel_Attribute", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groupRelationship6: BinaryAssociation = BinaryAssociation(
    name="groupRelationship6",
    ends={
        Property(name="servicefeaturemodel_GroupRelationship", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature7", type=servicefeaturemodel_GroupRelationship, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
serviceFeatures23: BinaryAssociation = BinaryAssociation(
    name="serviceFeatures23",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature25", type=servicefeaturemodel_ServiceFeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeatureDiagram24", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceFeature17: BinaryAssociation = BinaryAssociation(
    name="serviceFeature17",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature19", type=servicefeaturemodel_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Requires18", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)
serviceFeature20: BinaryAssociation = BinaryAssociation(
    name="serviceFeature20",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature22", type=servicefeaturemodel_Excludes, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Excludes21", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)
optionalServiceFeatures33: BinaryAssociation = BinaryAssociation(
    name="optionalServiceFeatures33",
    ends={
        Property(name="servicefeaturemodel_OptionalServiceFeature", type=servicefeaturemodel_GroupRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_GroupRelationship34", type=servicefeaturemodel_OptionalServiceFeature, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
configurations35: BinaryAssociation = BinaryAssociation(
    name="configurations35",
    ends={
        Property(name="servicefeaturemodel_Configuration37", type=servicefeaturemodel_Configurations, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configurations36", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributeTypes38: BinaryAssociation = BinaryAssociation(
    name="attributeTypes38",
    ends={
        Property(name="servicefeaturemodel_AttributeType40", type=servicefeaturemodel_AttributeTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_AttributeTypes39", type=servicefeaturemodel_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
serviceFeatures26: BinaryAssociation = BinaryAssociation(
    name="serviceFeatures26",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature27", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999))
    }
)
preferences28: BinaryAssociation = BinaryAssociation(
    name="preferences28",
    ends={
        Property(name="servicefeaturemodel_Preference", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration29", type=servicefeaturemodel_Preference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="servicefeaturemodel_Attribute32", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration31", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_servicefeaturemodel_OptionalServiceFeature_ServiceFeature = Generalization(general=ServiceFeature, specific=servicefeaturemodel_OptionalServiceFeature)
gen_servicefeaturemodel_XOR_GroupRelationship = Generalization(general=GroupRelationship, specific=servicefeaturemodel_XOR)
gen_servicefeaturemodel_OR_GroupRelationship = Generalization(general=GroupRelationship, specific=servicefeaturemodel_OR)
gen_servicefeaturemodel_MandatoryServiceFeature_ServiceFeature = Generalization(general=ServiceFeature, specific=servicefeaturemodel_MandatoryServiceFeature)

# Domain Model
domain_model = DomainModel(
    name="servicefeaturemodel",
    types={servicefeaturemodel_Service, servicefeaturemodel_ServiceFeatureDiagram, servicefeaturemodel_Configurations, servicefeaturemodel_AttributeTypes, servicefeaturemodel_Excludes, servicefeaturemodel_OptionalServiceFeature, ServiceFeature, servicefeaturemodel_AttributeType, servicefeaturemodel_ServiceFeature, servicefeaturemodel_Attribute, servicefeaturemodel_GroupRelationship, servicefeaturemodel_Requires, servicefeaturemodel_XOR, servicefeaturemodel_Configuration, servicefeaturemodel_OR, GroupRelationship, servicefeaturemodel_MandatoryServiceFeature, servicefeaturemodel_Preference, AttributeDomain, AggregationRules, ScaleOrders, FeatureTypes},
    associations={serviceFeatureDiagram0, configurations1, attributeTypes3, requires8, excludes10, serviceFeatures13, attributeType15, attributes5, groupRelationship6, serviceFeatures23, serviceFeature17, serviceFeature20, optionalServiceFeatures33, configurations35, attributeTypes38, serviceFeatures26, preferences28, attributes30},
    generalizations={gen_servicefeaturemodel_OptionalServiceFeature_ServiceFeature, gen_servicefeaturemodel_XOR_GroupRelationship, gen_servicefeaturemodel_OR_GroupRelationship, gen_servicefeaturemodel_MandatoryServiceFeature_ServiceFeature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)