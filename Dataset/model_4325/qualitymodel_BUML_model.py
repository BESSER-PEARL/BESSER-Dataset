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
AttributeAggregationOperator: Enumeration = Enumeration(
    name="AttributeAggregationOperator",
    literals={
            EnumerationLiteral(name="NEUTRALITY"),
			EnumerationLiteral(name="SIMULTANEITY"),
			EnumerationLiteral(name="REPLACEABILITY")
    }
)

MetricAggregationOperator: Enumeration = Enumeration(
    name="MetricAggregationOperator",
    literals={
            EnumerationLiteral(name="SUM"),
			EnumerationLiteral(name="AVERAGE"),
			EnumerationLiteral(name="MINIMUM"),
			EnumerationLiteral(name="MAXIMUM")
    }
)

MetricNormalizationKind: Enumeration = Enumeration(
    name="MetricNormalizationKind",
    literals={
            EnumerationLiteral(name="BENEFIT"),
			EnumerationLiteral(name="COST")
    }
)

# Classes
qualitymodel_LeafAttribute = Class(name="qualitymodel::LeafAttribute")
qualitymodel_Attribute = Class(name="qualitymodel::Attribute", is_abstract=True)
qualitymodel_CompositeAttribute = Class(name="qualitymodel::CompositeAttribute")
Attribute = Class(name="Attribute")
qualitymodel_Metric = Class(name="qualitymodel::Metric")
qualitymodel_HistoricalData = Class(name="qualitymodel::HistoricalData")
qualitymodel_Preference = Class(name="qualitymodel::Preference")
qualitymodel_ConfigurationProfile = Class(name="qualitymodel::ConfigurationProfile")

# qualitymodel_LeafAttribute class attributes and methods
qualitymodel_LeafAttribute_normalizationMin: Property = Property(name="normalizationMin", type=FloatType)
qualitymodel_LeafAttribute_normalizationMax: Property = Property(name="normalizationMax", type=FloatType)
qualitymodel_LeafAttribute_operator: Property = Property(name="operator", type=StringType)
qualitymodel_LeafAttribute_numSamples: Property = Property(name="numSamples", type=IntegerType)
qualitymodel_LeafAttribute_normalizationKind: Property = Property(name="normalizationKind", type=StringType)
qualitymodel_LeafAttribute_m_calculateAverage: Method = Method(name="calculateAverage", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_LeafAttribute_m_calculateMinimum: Method = Method(name="calculateMinimum", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_LeafAttribute_m_calculateMaximum: Method = Method(name="calculateMaximum", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_LeafAttribute_m_calculateSum: Method = Method(name="calculateSum", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_LeafAttribute.attributes={qualitymodel_LeafAttribute_numSamples, qualitymodel_LeafAttribute_operator, qualitymodel_LeafAttribute_normalizationKind, qualitymodel_LeafAttribute_normalizationMax, qualitymodel_LeafAttribute_normalizationMin}
qualitymodel_LeafAttribute.methods={qualitymodel_LeafAttribute_m_calculateSum, qualitymodel_LeafAttribute_m_calculateAverage, qualitymodel_LeafAttribute_m_calculateMinimum, qualitymodel_LeafAttribute_m_calculateMaximum}

# qualitymodel_Attribute class attributes and methods
qualitymodel_Attribute_name: Property = Property(name="name", type=StringType)
qualitymodel_Attribute_m_calculate: Method = Method(name="calculate", parameters={Parameter(name='profile')}, type=StringType)
qualitymodel_Attribute.attributes={qualitymodel_Attribute_name}
qualitymodel_Attribute.methods={qualitymodel_Attribute_m_calculate}

# qualitymodel_CompositeAttribute class attributes and methods
qualitymodel_CompositeAttribute_operator: Property = Property(name="operator", type=StringType)
qualitymodel_CompositeAttribute_m_calculateNeutrality: Method = Method(name="calculateNeutrality", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_CompositeAttribute_m_calculateSimultaneity: Method = Method(name="calculateSimultaneity", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_CompositeAttribute_m_calculateReplaceability: Method = Method(name="calculateReplaceability", parameters={Parameter(name='profile')}, type=FloatType)
qualitymodel_CompositeAttribute.attributes={qualitymodel_CompositeAttribute_operator}
qualitymodel_CompositeAttribute.methods={qualitymodel_CompositeAttribute_m_calculateReplaceability, qualitymodel_CompositeAttribute_m_calculateNeutrality, qualitymodel_CompositeAttribute_m_calculateSimultaneity}

# Attribute class attributes and methods

# qualitymodel_Metric class attributes and methods
qualitymodel_Metric_resourceName: Property = Property(name="resourceName", type=StringType)
qualitymodel_Metric_data: Property = Property(name="data", type=StringType)
qualitymodel_Metric_probeName: Property = Property(name="probeName", type=StringType)
qualitymodel_Metric_descriptionName: Property = Property(name="descriptionName", type=StringType)
qualitymodel_Metric.attributes={qualitymodel_Metric_descriptionName, qualitymodel_Metric_data, qualitymodel_Metric_resourceName, qualitymodel_Metric_probeName}

# qualitymodel_HistoricalData class attributes and methods
qualitymodel_HistoricalData_instant: Property = Property(name="instant", type=StringType)
qualitymodel_HistoricalData_value: Property = Property(name="value", type=FloatType)
qualitymodel_HistoricalData.attributes={qualitymodel_HistoricalData_instant, qualitymodel_HistoricalData_value}

# qualitymodel_Preference class attributes and methods
qualitymodel_Preference_weight: Property = Property(name="weight", type=FloatType)
qualitymodel_Preference_threshold: Property = Property(name="threshold", type=FloatType)
qualitymodel_Preference.attributes={qualitymodel_Preference_weight, qualitymodel_Preference_threshold}

# qualitymodel_ConfigurationProfile class attributes and methods
qualitymodel_ConfigurationProfile_ID: Property = Property(name="ID", type=IntegerType)
qualitymodel_ConfigurationProfile.attributes={qualitymodel_ConfigurationProfile_ID}

# Relationships
attribute0: BinaryAssociation = BinaryAssociation(
    name="attribute0",
    ends={
        Property(name="qualitymodel_LeafAttribute", type=qualitymodel_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_Metric", type=qualitymodel_LeafAttribute, multiplicity=Multiplicity(1, 1))
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="qualitymodel_Attribute", type=qualitymodel_CompositeAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_CompositeAttribute", type=qualitymodel_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attribute2: BinaryAssociation = BinaryAssociation(
    name="attribute2",
    ends={
        Property(name="qualitymodel_Attribute3", type=qualitymodel_HistoricalData, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_HistoricalData", type=qualitymodel_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
attribute4: BinaryAssociation = BinaryAssociation(
    name="attribute4",
    ends={
        Property(name="qualitymodel_Attribute5", type=qualitymodel_Preference, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_Preference", type=qualitymodel_Attribute, multiplicity=Multiplicity(1, 1))
    }
)
preference6: BinaryAssociation = BinaryAssociation(
    name="preference6",
    ends={
        Property(name="qualitymodel_Preference7", type=qualitymodel_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_ConfigurationProfile", type=qualitymodel_Preference, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metric8: BinaryAssociation = BinaryAssociation(
    name="metric8",
    ends={
        Property(name="qualitymodel_Metric10", type=qualitymodel_ConfigurationProfile, multiplicity=Multiplicity(1, 1)),
        Property(name="qualitymodel_ConfigurationProfile9", type=qualitymodel_Metric, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_qualitymodel_CompositeAttribute_Attribute = Generalization(general=Attribute, specific=qualitymodel_CompositeAttribute)
gen_qualitymodel_LeafAttribute_Attribute = Generalization(general=Attribute, specific=qualitymodel_LeafAttribute)

# Domain Model
domain_model = DomainModel(
    name="qualitymodel",
    types={qualitymodel_LeafAttribute, qualitymodel_Attribute, qualitymodel_CompositeAttribute, Attribute, qualitymodel_Metric, qualitymodel_HistoricalData, qualitymodel_Preference, qualitymodel_ConfigurationProfile, AttributeAggregationOperator, MetricAggregationOperator, MetricNormalizationKind},
    associations={attribute0, children1, attribute2, attribute4, preference6, metric8},
    generalizations={gen_qualitymodel_CompositeAttribute_Attribute, gen_qualitymodel_LeafAttribute_Attribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)