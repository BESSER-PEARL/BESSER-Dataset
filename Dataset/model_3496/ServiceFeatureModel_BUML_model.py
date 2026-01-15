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
servicefeaturemodel_PossibleConfigurations = Class(name="servicefeaturemodel::PossibleConfigurations")
servicefeaturemodel_AttributeTypes = Class(name="servicefeaturemodel::AttributeTypes")
servicefeaturemodel_Service = Class(name="servicefeaturemodel::Service")
servicefeaturemodel_ServiceFeatureDiagram = Class(name="servicefeaturemodel::ServiceFeatureDiagram")
servicefeaturemodel_OptionalServiceFeature = Class(name="servicefeaturemodel::OptionalServiceFeature")
ServiceFeature = Class(name="ServiceFeature")
servicefeaturemodel_ServiceFeature = Class(name="servicefeaturemodel::ServiceFeature", is_abstract=True)
servicefeaturemodel_Attribute = Class(name="servicefeaturemodel::Attribute")
servicefeaturemodel_Variant = Class(name="servicefeaturemodel::Variant", is_abstract=True)
servicefeaturemodel_Requires = Class(name="servicefeaturemodel::Requires")
servicefeaturemodel_Excludes = Class(name="servicefeaturemodel::Excludes")
servicefeaturemodel_Configuration = Class(name="servicefeaturemodel::Configuration")
servicefeaturemodel_AttributeType = Class(name="servicefeaturemodel::AttributeType")
servicefeaturemodel_ModifyRelationship = Class(name="servicefeaturemodel::ModifyRelationship", is_abstract=True)
servicefeaturemodel_OR = Class(name="servicefeaturemodel::OR")
Variant = Class(name="Variant")
servicefeaturemodel_XOR = Class(name="servicefeaturemodel::XOR")
servicefeaturemodel_Preference = Class(name="servicefeaturemodel::Preference")
servicefeaturemodel_MandatoryServiceFeature = Class(name="servicefeaturemodel::MandatoryServiceFeature")
servicefeaturemodel_AttributeToAttributeModifyRelationship = Class(name="servicefeaturemodel::AttributeToAttributeModifyRelationship")
ModifyRelationship = Class(name="ModifyRelationship")
servicefeaturemodel_FeatureToAttributeModifyRelationship = Class(name="servicefeaturemodel::FeatureToAttributeModifyRelationship")

# servicefeaturemodel_PossibleConfigurations class attributes and methods

# servicefeaturemodel_AttributeTypes class attributes and methods

# servicefeaturemodel_Service class attributes and methods
servicefeaturemodel_Service_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Service_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_Service_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Service.attributes={servicefeaturemodel_Service_description, servicefeaturemodel_Service_id, servicefeaturemodel_Service_name}

# servicefeaturemodel_ServiceFeatureDiagram class attributes and methods
servicefeaturemodel_ServiceFeatureDiagram_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_ServiceFeatureDiagram_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
servicefeaturemodel_ServiceFeatureDiagram.attributes={servicefeaturemodel_ServiceFeatureDiagram_description, servicefeaturemodel_ServiceFeatureDiagram_name, servicefeaturemodel_ServiceFeatureDiagram_id}
servicefeaturemodel_ServiceFeatureDiagram.methods={servicefeaturemodel_ServiceFeatureDiagram_m_validate}

# servicefeaturemodel_OptionalServiceFeature class attributes and methods

# ServiceFeature class attributes and methods

# servicefeaturemodel_ServiceFeature class attributes and methods
servicefeaturemodel_ServiceFeature_associatedGSMElement: Property = Property(name="associatedGSMElement", type=StringType)
servicefeaturemodel_ServiceFeature_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_ServiceFeature_featureType: Property = Property(name="featureType", type=StringType)
servicefeaturemodel_ServiceFeature_required: Property = Property(name="required", type=BooleanType)
servicefeaturemodel_ServiceFeature_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_ServiceFeature_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_ServiceFeature_minAmount: Property = Property(name="minAmount", type=IntegerType)
servicefeaturemodel_ServiceFeature_maxAmount: Property = Property(name="maxAmount", type=IntegerType)
servicefeaturemodel_ServiceFeature_mapsToGSMElement: Property = Property(name="mapsToGSMElement", type=BooleanType)
servicefeaturemodel_ServiceFeature_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
servicefeaturemodel_ServiceFeature.attributes={servicefeaturemodel_ServiceFeature_associatedGSMElement, servicefeaturemodel_ServiceFeature_id, servicefeaturemodel_ServiceFeature_description, servicefeaturemodel_ServiceFeature_required, servicefeaturemodel_ServiceFeature_mapsToGSMElement, servicefeaturemodel_ServiceFeature_maxAmount, servicefeaturemodel_ServiceFeature_minAmount, servicefeaturemodel_ServiceFeature_featureType, servicefeaturemodel_ServiceFeature_name}
servicefeaturemodel_ServiceFeature.methods={servicefeaturemodel_ServiceFeature_m_validate}

# servicefeaturemodel_Attribute class attributes and methods
servicefeaturemodel_Attribute_instantiationValue: Property = Property(name="instantiationValue", type=StringType)
servicefeaturemodel_Attribute_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Attribute.attributes={servicefeaturemodel_Attribute_id, servicefeaturemodel_Attribute_instantiationValue}

# servicefeaturemodel_Variant class attributes and methods

# servicefeaturemodel_Requires class attributes and methods

# servicefeaturemodel_Excludes class attributes and methods

# servicefeaturemodel_Configuration class attributes and methods
servicefeaturemodel_Configuration_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_Configuration_id: Property = Property(name="id", type=StringType)
servicefeaturemodel_Configuration_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Configuration_m_validate: Method = Method(name="validate", parameters={Parameter(name='context'), Parameter(name='diagnostic')}, type=BooleanType)
servicefeaturemodel_Configuration.attributes={servicefeaturemodel_Configuration_description, servicefeaturemodel_Configuration_name, servicefeaturemodel_Configuration_id}
servicefeaturemodel_Configuration.methods={servicefeaturemodel_Configuration_m_validate}

# servicefeaturemodel_AttributeType class attributes and methods
servicefeaturemodel_AttributeType_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_AttributeType_domain: Property = Property(name="domain", type=StringType)
servicefeaturemodel_AttributeType_aggregationRule: Property = Property(name="aggregationRule", type=StringType)
servicefeaturemodel_AttributeType_scaleOrder: Property = Property(name="scaleOrder", type=StringType)
servicefeaturemodel_AttributeType_toBeEvaluated: Property = Property(name="toBeEvaluated", type=BooleanType)
servicefeaturemodel_AttributeType_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_AttributeType_customAttributeTypePriority: Property = Property(name="customAttributeTypePriority", type=IntegerType)
servicefeaturemodel_AttributeType_requirement: Property = Property(name="requirement", type=StringType)
servicefeaturemodel_AttributeType.attributes={servicefeaturemodel_AttributeType_aggregationRule, servicefeaturemodel_AttributeType_domain, servicefeaturemodel_AttributeType_name, servicefeaturemodel_AttributeType_customAttributeTypePriority, servicefeaturemodel_AttributeType_scaleOrder, servicefeaturemodel_AttributeType_toBeEvaluated, servicefeaturemodel_AttributeType_description, servicefeaturemodel_AttributeType_requirement}

# servicefeaturemodel_ModifyRelationship class attributes and methods
servicefeaturemodel_ModifyRelationship_name: Property = Property(name="name", type=StringType)
servicefeaturemodel_ModifyRelationship_orderNumber: Property = Property(name="orderNumber", type=IntegerType)
servicefeaturemodel_ModifyRelationship_function: Property = Property(name="function", type=StringType)
servicefeaturemodel_ModifyRelationship_targetParameterName: Property = Property(name="targetParameterName", type=StringType)
servicefeaturemodel_ModifyRelationship.attributes={servicefeaturemodel_ModifyRelationship_name, servicefeaturemodel_ModifyRelationship_targetParameterName, servicefeaturemodel_ModifyRelationship_function, servicefeaturemodel_ModifyRelationship_orderNumber}

# servicefeaturemodel_OR class attributes and methods
servicefeaturemodel_OR_minFeaturesToChoose: Property = Property(name="minFeaturesToChoose", type=IntegerType)
servicefeaturemodel_OR_maxFeaturesToChoose: Property = Property(name="maxFeaturesToChoose", type=IntegerType)
servicefeaturemodel_OR.attributes={servicefeaturemodel_OR_maxFeaturesToChoose, servicefeaturemodel_OR_minFeaturesToChoose}

# Variant class attributes and methods

# servicefeaturemodel_XOR class attributes and methods

# servicefeaturemodel_Preference class attributes and methods
servicefeaturemodel_Preference_creationDate: Property = Property(name="creationDate", type=DateType)
servicefeaturemodel_Preference_description: Property = Property(name="description", type=StringType)
servicefeaturemodel_Preference_value: Property = Property(name="value", type=FloatType)
servicefeaturemodel_Preference_stakeholderGroup: Property = Property(name="stakeholderGroup", type=StringType)
servicefeaturemodel_Preference.attributes={servicefeaturemodel_Preference_stakeholderGroup, servicefeaturemodel_Preference_value, servicefeaturemodel_Preference_description, servicefeaturemodel_Preference_creationDate}

# servicefeaturemodel_MandatoryServiceFeature class attributes and methods

# servicefeaturemodel_AttributeToAttributeModifyRelationship class attributes and methods
servicefeaturemodel_AttributeToAttributeModifyRelationship_triggerParameterName: Property = Property(name="triggerParameterName", type=StringType)
servicefeaturemodel_AttributeToAttributeModifyRelationship.attributes={servicefeaturemodel_AttributeToAttributeModifyRelationship_triggerParameterName}

# ModifyRelationship class attributes and methods

# servicefeaturemodel_FeatureToAttributeModifyRelationship class attributes and methods

# Relationships
enables1: BinaryAssociation = BinaryAssociation(
    name="enables1",
    ends={
        Property(name="servicefeaturemodel_PossibleConfigurations", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service2", type=servicefeaturemodel_PossibleConfigurations, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
has3: BinaryAssociation = BinaryAssociation(
    name="has3",
    ends={
        Property(name="servicefeaturemodel_AttributeTypes", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service4", type=servicefeaturemodel_AttributeTypes, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
representedBy0: BinaryAssociation = BinaryAssociation(
    name="representedBy0",
    ends={
        Property(name="servicefeaturemodel_ServiceFeatureDiagram", type=servicefeaturemodel_Service, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Service", type=servicefeaturemodel_ServiceFeatureDiagram, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
describedBy5: BinaryAssociation = BinaryAssociation(
    name="describedBy5",
    ends={
        Property(name="servicefeaturemodel_Attribute", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsVariant6: BinaryAssociation = BinaryAssociation(
    name="containsVariant6",
    ends={
        Property(name="servicefeaturemodel_Variant", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature7", type=servicefeaturemodel_Variant, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
containsRequires8: BinaryAssociation = BinaryAssociation(
    name="containsRequires8",
    ends={
        Property(name="servicefeaturemodel_Requires", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature9", type=servicefeaturemodel_Requires, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsExcludes10: BinaryAssociation = BinaryAssociation(
    name="containsExcludes10",
    ends={
        Property(name="servicefeaturemodel_Excludes", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature11", type=servicefeaturemodel_Excludes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
decomposesInto13: BinaryAssociation = BinaryAssociation(
    name="decomposesInto13",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature14", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeature12", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ofAttributeType15: BinaryAssociation = BinaryAssociation(
    name="ofAttributeType15",
    ends={
        Property(name="servicefeaturemodel_AttributeType", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Attribute16", type=servicefeaturemodel_AttributeType, multiplicity=Multiplicity(1, 1))
    }
)
containsModifyRelationship17: BinaryAssociation = BinaryAssociation(
    name="containsModifyRelationship17",
    ends={
        Property(name="servicefeaturemodel_ModifyRelationship", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Attribute18", type=servicefeaturemodel_ModifyRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
requiresServiceFeature19: BinaryAssociation = BinaryAssociation(
    name="requiresServiceFeature19",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature21", type=servicefeaturemodel_Requires, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Requires20", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)
excludesServiceFeature22: BinaryAssociation = BinaryAssociation(
    name="excludesServiceFeature22",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature24", type=servicefeaturemodel_Excludes, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Excludes23", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)
containsFeatures25: BinaryAssociation = BinaryAssociation(
    name="containsFeatures25",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature27", type=servicefeaturemodel_ServiceFeatureDiagram, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_ServiceFeatureDiagram26", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains37: BinaryAssociation = BinaryAssociation(
    name="contains37",
    ends={
        Property(name="servicefeaturemodel_Configuration39", type=servicefeaturemodel_PossibleConfigurations, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_PossibleConfigurations38", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains40: BinaryAssociation = BinaryAssociation(
    name="contains40",
    ends={
        Property(name="servicefeaturemodel_AttributeType42", type=servicefeaturemodel_AttributeTypes, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_AttributeTypes41", type=servicefeaturemodel_AttributeType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
groups28: BinaryAssociation = BinaryAssociation(
    name="groups28",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature29", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(0, 9999))
    }
)
evaluatedBy30: BinaryAssociation = BinaryAssociation(
    name="evaluatedBy30",
    ends={
        Property(name="servicefeaturemodel_Preference", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration31", type=servicefeaturemodel_Preference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
describedBy32: BinaryAssociation = BinaryAssociation(
    name="describedBy32",
    ends={
        Property(name="servicefeaturemodel_Attribute34", type=servicefeaturemodel_Configuration, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Configuration33", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains35: BinaryAssociation = BinaryAssociation(
    name="contains35",
    ends={
        Property(name="servicefeaturemodel_OptionalServiceFeature", type=servicefeaturemodel_Variant, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_Variant36", type=servicefeaturemodel_OptionalServiceFeature, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
triggeredByAttribute43: BinaryAssociation = BinaryAssociation(
    name="triggeredByAttribute43",
    ends={
        Property(name="servicefeaturemodel_Attribute44", type=servicefeaturemodel_AttributeToAttributeModifyRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_AttributeToAttributeModifyRelationship", type=servicefeaturemodel_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
triggeredByServiceFeature45: BinaryAssociation = BinaryAssociation(
    name="triggeredByServiceFeature45",
    ends={
        Property(name="servicefeaturemodel_ServiceFeature46", type=servicefeaturemodel_FeatureToAttributeModifyRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="servicefeaturemodel_FeatureToAttributeModifyRelationship", type=servicefeaturemodel_ServiceFeature, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_servicefeaturemodel_OptionalServiceFeature_ServiceFeature = Generalization(general=ServiceFeature, specific=servicefeaturemodel_OptionalServiceFeature)
gen_servicefeaturemodel_OR_Variant = Generalization(general=Variant, specific=servicefeaturemodel_OR)
gen_servicefeaturemodel_XOR_Variant = Generalization(general=Variant, specific=servicefeaturemodel_XOR)
gen_servicefeaturemodel_MandatoryServiceFeature_ServiceFeature = Generalization(general=ServiceFeature, specific=servicefeaturemodel_MandatoryServiceFeature)
gen_servicefeaturemodel_AttributeToAttributeModifyRelationship_ModifyRelationship = Generalization(general=ModifyRelationship, specific=servicefeaturemodel_AttributeToAttributeModifyRelationship)
gen_servicefeaturemodel_FeatureToAttributeModifyRelationship_ModifyRelationship = Generalization(general=ModifyRelationship, specific=servicefeaturemodel_FeatureToAttributeModifyRelationship)

# Domain Model
domain_model = DomainModel(
    name="servicefeaturemodel",
    types={servicefeaturemodel_PossibleConfigurations, servicefeaturemodel_AttributeTypes, servicefeaturemodel_Service, servicefeaturemodel_ServiceFeatureDiagram, servicefeaturemodel_OptionalServiceFeature, ServiceFeature, servicefeaturemodel_ServiceFeature, servicefeaturemodel_Attribute, servicefeaturemodel_Variant, servicefeaturemodel_Requires, servicefeaturemodel_Excludes, servicefeaturemodel_Configuration, servicefeaturemodel_AttributeType, servicefeaturemodel_ModifyRelationship, servicefeaturemodel_OR, Variant, servicefeaturemodel_XOR, servicefeaturemodel_Preference, servicefeaturemodel_MandatoryServiceFeature, servicefeaturemodel_AttributeToAttributeModifyRelationship, ModifyRelationship, servicefeaturemodel_FeatureToAttributeModifyRelationship, AttributeDomain, AggregationRules, ScaleOrders, FeatureTypes},
    associations={enables1, has3, representedBy0, describedBy5, containsVariant6, containsRequires8, containsExcludes10, decomposesInto13, ofAttributeType15, containsModifyRelationship17, requiresServiceFeature19, excludesServiceFeature22, containsFeatures25, contains37, contains40, groups28, evaluatedBy30, describedBy32, contains35, triggeredByAttribute43, triggeredByServiceFeature45},
    generalizations={gen_servicefeaturemodel_OptionalServiceFeature_ServiceFeature, gen_servicefeaturemodel_OR_Variant, gen_servicefeaturemodel_XOR_Variant, gen_servicefeaturemodel_MandatoryServiceFeature_ServiceFeature, gen_servicefeaturemodel_AttributeToAttributeModifyRelationship_ModifyRelationship, gen_servicefeaturemodel_FeatureToAttributeModifyRelationship_ModifyRelationship},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)