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
QualityMetrics_SimpleMetric = Class(name="QualityMetrics::SimpleMetric")
QualityMetrics_Metrics = Class(name="QualityMetrics::Metrics")
QualityMetrics_AggregatedIntegerMetric = Class(name="QualityMetrics::AggregatedIntegerMetric")
QualityMetrics_AggregatedRealMetric = Class(name="QualityMetrics::AggregatedRealMetric")
QualityMetrics_Metric = Class(name="QualityMetrics::Metric", is_abstract=True)
Metric = Class(name="Metric")

# QualityMetrics_SimpleMetric class attributes and methods
QualityMetrics_SimpleMetric_Value: Property = Property(name="Value", type=IntegerType)
QualityMetrics_SimpleMetric.attributes={QualityMetrics_SimpleMetric_Value}

# QualityMetrics_Metrics class attributes and methods
QualityMetrics_Metrics_TrafoName: Property = Property(name="TrafoName", type=StringType)
QualityMetrics_Metrics.attributes={QualityMetrics_Metrics_TrafoName}

# QualityMetrics_AggregatedIntegerMetric class attributes and methods
QualityMetrics_AggregatedIntegerMetric_Minimum: Property = Property(name="Minimum", type=IntegerType)
QualityMetrics_AggregatedIntegerMetric_Maximum: Property = Property(name="Maximum", type=IntegerType)
QualityMetrics_AggregatedIntegerMetric_Median: Property = Property(name="Median", type=IntegerType)
QualityMetrics_AggregatedIntegerMetric_Average: Property = Property(name="Average", type=FloatType)
QualityMetrics_AggregatedIntegerMetric_StandardDeviation: Property = Property(name="StandardDeviation", type=FloatType)
QualityMetrics_AggregatedIntegerMetric.attributes={QualityMetrics_AggregatedIntegerMetric_Minimum, QualityMetrics_AggregatedIntegerMetric_Average, QualityMetrics_AggregatedIntegerMetric_Maximum, QualityMetrics_AggregatedIntegerMetric_Median, QualityMetrics_AggregatedIntegerMetric_StandardDeviation}

# QualityMetrics_AggregatedRealMetric class attributes and methods
QualityMetrics_AggregatedRealMetric_Minimum: Property = Property(name="Minimum", type=FloatType)
QualityMetrics_AggregatedRealMetric_Maximum: Property = Property(name="Maximum", type=FloatType)
QualityMetrics_AggregatedRealMetric_Median: Property = Property(name="Median", type=FloatType)
QualityMetrics_AggregatedRealMetric_Average: Property = Property(name="Average", type=FloatType)
QualityMetrics_AggregatedRealMetric_StandardDeviation: Property = Property(name="StandardDeviation", type=FloatType)
QualityMetrics_AggregatedRealMetric.attributes={QualityMetrics_AggregatedRealMetric_Minimum, QualityMetrics_AggregatedRealMetric_Average, QualityMetrics_AggregatedRealMetric_Maximum, QualityMetrics_AggregatedRealMetric_Median, QualityMetrics_AggregatedRealMetric_StandardDeviation}

# QualityMetrics_Metric class attributes and methods
QualityMetrics_Metric_Metric: Property = Property(name="Metric", type=StringType)
QualityMetrics_Metric.attributes={QualityMetrics_Metric_Metric}

# Metric class attributes and methods

# Relationships
SimpleMetrics0: BinaryAssociation = BinaryAssociation(
    name="SimpleMetrics0",
    ends={
        Property(name="QualityMetrics_SimpleMetric", type=QualityMetrics_Metrics, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetrics_Metrics", type=QualityMetrics_SimpleMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AggregatedIntegerMetrics1: BinaryAssociation = BinaryAssociation(
    name="AggregatedIntegerMetrics1",
    ends={
        Property(name="QualityMetrics_AggregatedIntegerMetric", type=QualityMetrics_Metrics, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetrics_Metrics2", type=QualityMetrics_AggregatedIntegerMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
AggregatedRealMetrics3: BinaryAssociation = BinaryAssociation(
    name="AggregatedRealMetrics3",
    ends={
        Property(name="QualityMetrics_AggregatedRealMetric", type=QualityMetrics_Metrics, multiplicity=Multiplicity(1, 1)),
        Property(name="QualityMetrics_Metrics4", type=QualityMetrics_AggregatedRealMetric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_QualityMetrics_SimpleMetric_Metric = Generalization(general=Metric, specific=QualityMetrics_SimpleMetric)
gen_QualityMetrics_AggregatedIntegerMetric_Metric = Generalization(general=Metric, specific=QualityMetrics_AggregatedIntegerMetric)
gen_QualityMetrics_AggregatedRealMetric_Metric = Generalization(general=Metric, specific=QualityMetrics_AggregatedRealMetric)

# Domain Model
domain_model = DomainModel(
    name="QualityMetrics",
    types={QualityMetrics_SimpleMetric, QualityMetrics_Metrics, QualityMetrics_AggregatedIntegerMetric, QualityMetrics_AggregatedRealMetric, QualityMetrics_Metric, Metric},
    associations={SimpleMetrics0, AggregatedIntegerMetrics1, AggregatedRealMetrics3},
    generalizations={gen_QualityMetrics_SimpleMetric_Metric, gen_QualityMetrics_AggregatedIntegerMetric_Metric, gen_QualityMetrics_AggregatedRealMetric_Metric},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)