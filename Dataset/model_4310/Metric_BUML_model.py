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
metric_AggregatedIntegerMetric = Class(name="metric::AggregatedIntegerMetric")
Metric = Class(name="Metric")
metric_AggregatedRealMetric = Class(name="metric::AggregatedRealMetric")
metric_SimpleMetric = Class(name="metric::SimpleMetric")
metric_Container = Class(name="metric::Container")
metric_Metric = Class(name="metric::Metric", is_abstract=True)

# metric_AggregatedIntegerMetric class attributes and methods
metric_AggregatedIntegerMetric_minimum: Property = Property(name="minimum", type=StringType)
metric_AggregatedIntegerMetric_maximum: Property = Property(name="maximum", type=StringType)
metric_AggregatedIntegerMetric_median: Property = Property(name="median", type=StringType)
metric_AggregatedIntegerMetric_average: Property = Property(name="average", type=FloatType)
metric_AggregatedIntegerMetric_standardDeviation: Property = Property(name="standardDeviation", type=FloatType)
metric_AggregatedIntegerMetric.attributes={metric_AggregatedIntegerMetric_standardDeviation, metric_AggregatedIntegerMetric_average, metric_AggregatedIntegerMetric_minimum, metric_AggregatedIntegerMetric_maximum, metric_AggregatedIntegerMetric_median}

# Metric class attributes and methods

# metric_AggregatedRealMetric class attributes and methods
metric_AggregatedRealMetric_minimum: Property = Property(name="minimum", type=FloatType)
metric_AggregatedRealMetric_maximum: Property = Property(name="maximum", type=FloatType)
metric_AggregatedRealMetric_median: Property = Property(name="median", type=FloatType)
metric_AggregatedRealMetric_average: Property = Property(name="average", type=FloatType)
metric_AggregatedRealMetric_standardDeviation: Property = Property(name="standardDeviation", type=FloatType)
metric_AggregatedRealMetric.attributes={metric_AggregatedRealMetric_median, metric_AggregatedRealMetric_average, metric_AggregatedRealMetric_maximum, metric_AggregatedRealMetric_minimum, metric_AggregatedRealMetric_standardDeviation}

# metric_SimpleMetric class attributes and methods
metric_SimpleMetric_value: Property = Property(name="value", type=StringType)
metric_SimpleMetric.attributes={metric_SimpleMetric_value}

# metric_Container class attributes and methods

# metric_Metric class attributes and methods
metric_Metric_description: Property = Property(name="description", type=StringType)
metric_Metric_code: Property = Property(name="code", type=StringType)
metric_Metric_name: Property = Property(name="name", type=StringType)
metric_Metric.attributes={metric_Metric_code, metric_Metric_name, metric_Metric_description}

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="metric_Metric", type=metric_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="metric_Container", type=metric_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metric_AggregatedIntegerMetric_Metric = Generalization(general=Metric, specific=metric_AggregatedIntegerMetric)
gen_metric_AggregatedRealMetric_Metric = Generalization(general=Metric, specific=metric_AggregatedRealMetric)
gen_metric_SimpleMetric_Metric = Generalization(general=Metric, specific=metric_SimpleMetric)

# Domain Model
domain_model = DomainModel(
    name="metric",
    types={metric_AggregatedIntegerMetric, Metric, metric_AggregatedRealMetric, metric_SimpleMetric, metric_Container, metric_Metric},
    associations={metrics0},
    generalizations={gen_metric_AggregatedIntegerMetric_Metric, gen_metric_AggregatedRealMetric_Metric, gen_metric_SimpleMetric_Metric},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)