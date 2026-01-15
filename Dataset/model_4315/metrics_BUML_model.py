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
FixedMetricRetentionPeriod: Enumeration = Enumeration(
    name="FixedMetricRetentionPeriod",
    literals={
            EnumerationLiteral(name="Always"),
			EnumerationLiteral(name="OneYear"),
			EnumerationLiteral(name="OneMonth"),
			EnumerationLiteral(name="OneWeek")
    }
)

# Classes
metrics_Addon = Class(name="metrics::Addon")
metrics_Metric = Class(name="metrics::Metric")
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_MetricRetentionRules = Class(name="metrics::MetricRetentionRules")
metrics_MetricAggregationRules = Class(name="metrics::MetricAggregationRules")
Base = Class(name="Base")
metrics_MetricAggregationRule = Class(name="metrics::MetricAggregationRule")
Rule = Class(name="Rule")
metrics_EObject = Class(name="metrics::EObject")
metrics_MetricRetentionPeriods = Class(name="metrics::MetricRetentionPeriods")
metrics_MetricRetentionRule = Class(name="metrics::MetricRetentionRule")

# metrics_Addon class attributes and methods

# metrics_Metric class attributes and methods
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric.attributes={metrics_Metric_name}

# metrics_MetricSource class attributes and methods
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_name}

# metrics_MetricRetentionRules class attributes and methods

# metrics_MetricAggregationRules class attributes and methods

# Base class attributes and methods

# metrics_MetricAggregationRule class attributes and methods
metrics_MetricAggregationRule_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricAggregationRule_period: Property = Property(name="period", type=StringType)
metrics_MetricAggregationRule.attributes={metrics_MetricAggregationRule_intervalHint, metrics_MetricAggregationRule_period}

# Rule class attributes and methods

# metrics_EObject class attributes and methods

# metrics_MetricRetentionPeriods class attributes and methods
metrics_MetricRetentionPeriods_metricRetentionPeriods: Property = Property(name="metricRetentionPeriods", type=StringType)
metrics_MetricRetentionPeriods.attributes={metrics_MetricRetentionPeriods_metricRetentionPeriods}

# metrics_MetricRetentionRule class attributes and methods
metrics_MetricRetentionRule_intervalHint: Property = Property(name="intervalHint", type=StringType)
metrics_MetricRetentionRule_period: Property = Property(name="period", type=StringType)
metrics_MetricRetentionRule.attributes={metrics_MetricRetentionRule_period, metrics_MetricRetentionRule_intervalHint}

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="metrics_Metric", type=metrics_Addon, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Addon", type=metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricSources1: BinaryAssociation = BinaryAssociation(
    name="metricSources1",
    ends={
        Property(name="metrics_MetricSource", type=metrics_Addon, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Addon2", type=metrics_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricRetentionRuleSets3: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRuleSets3",
    ends={
        Property(name="metrics_MetricRetentionRules", type=metrics_Addon, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Addon4", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricAggregationRuleSets5: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRuleSets5",
    ends={
        Property(name="metrics_MetricAggregationRules", type=metrics_Addon, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Addon6", type=metrics_MetricAggregationRules, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricAggregationRuleSet7: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRuleSet7",
    ends={
        Property(name="metrics_MetricAggregationRules9", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric8", type=metrics_MetricAggregationRules, multiplicity=Multiplicity(0, 1))
    }
)
metricRetentionRuleSet10: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRuleSet10",
    ends={
        Property(name="metrics_MetricRetentionRules12", type=metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Metric11", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(0, 1))
    }
)
metricRetentionRules17: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRules17",
    ends={
        Property(name="metrics_MetricRetentionRule", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricRetentionRules18", type=metrics_MetricRetentionRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
aggregationExpression13: BinaryAssociation = BinaryAssociation(
    name="aggregationExpression13",
    ends={
        Property(name="metrics_EObject", type=metrics_MetricAggregationRule, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricAggregationRule", type=metrics_EObject, multiplicity=Multiplicity(0, 1))
    }
)
metricAggregationRules14: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRules14",
    ends={
        Property(name="metrics_MetricAggregationRule16", type=metrics_MetricAggregationRules, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricAggregationRules15", type=metrics_MetricAggregationRule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metricAggregationRuleSet19: BinaryAssociation = BinaryAssociation(
    name="metricAggregationRuleSet19",
    ends={
        Property(name="metrics_MetricAggregationRules21", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource20", type=metrics_MetricAggregationRules, multiplicity=Multiplicity(0, 1))
    }
)
metricRetentionRuleSet22: BinaryAssociation = BinaryAssociation(
    name="metricRetentionRuleSet22",
    ends={
        Property(name="metrics_MetricRetentionRules24", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricSource23", type=metrics_MetricRetentionRules, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_metrics_Metric_Base = Generalization(general=Base, specific=metrics_Metric)
gen_metrics_MetricAggregationRule_Rule = Generalization(general=Rule, specific=metrics_MetricAggregationRule)
gen_metrics_MetricRetentionRule_Rule = Generalization(general=Rule, specific=metrics_MetricRetentionRule)
gen_metrics_MetricSource_Base = Generalization(general=Base, specific=metrics_MetricSource)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_Addon, metrics_Metric, metrics_MetricSource, metrics_MetricRetentionRules, metrics_MetricAggregationRules, Base, metrics_MetricAggregationRule, Rule, metrics_EObject, metrics_MetricRetentionPeriods, metrics_MetricRetentionRule, FixedMetricRetentionPeriod},
    associations={metrics0, metricSources1, metricRetentionRuleSets3, metricAggregationRuleSets5, metricAggregationRuleSet7, metricRetentionRuleSet10, metricRetentionRules17, aggregationExpression13, metricAggregationRules14, metricAggregationRuleSet19, metricRetentionRuleSet22},
    generalizations={gen_metrics_Metric_Base, gen_metrics_MetricAggregationRule_Rule, gen_metrics_MetricRetentionRule_Rule, gen_metrics_MetricSource_Base},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)