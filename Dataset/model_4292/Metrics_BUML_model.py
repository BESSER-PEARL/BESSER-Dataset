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
Metrics_Metric = Class(name="Metrics::Metric")
MetricValue = Class(name="MetricValue")
Metrics_MetricValue = Class(name="Metrics::MetricValue", is_abstract=True)
Metrics_StringMetricValue = Class(name="Metrics::StringMetricValue")
Metrics_BooleanMetricValue = Class(name="Metrics::BooleanMetricValue")
Metrics_IntegerMetricValue = Class(name="Metrics::IntegerMetricValue")
Metrics_DoubleMetricValue = Class(name="Metrics::DoubleMetricValue")

# Metrics_Metric class attributes and methods
Metrics_Metric_name: Property = Property(name="name", type=StringType)
Metrics_Metric.attributes={Metrics_Metric_name}

# MetricValue class attributes and methods

# Metrics_MetricValue class attributes and methods
Metrics_MetricValue_tag: Property = Property(name="tag", type=StringType)
Metrics_MetricValue.attributes={Metrics_MetricValue_tag}

# Metrics_StringMetricValue class attributes and methods
Metrics_StringMetricValue_value: Property = Property(name="value", type=StringType)
Metrics_StringMetricValue.attributes={Metrics_StringMetricValue_value}

# Metrics_BooleanMetricValue class attributes and methods
Metrics_BooleanMetricValue_value: Property = Property(name="value", type=StringType)
Metrics_BooleanMetricValue.attributes={Metrics_BooleanMetricValue_value}

# Metrics_IntegerMetricValue class attributes and methods
Metrics_IntegerMetricValue_value: Property = Property(name="value", type=StringType)
Metrics_IntegerMetricValue.attributes={Metrics_IntegerMetricValue_value}

# Metrics_DoubleMetricValue class attributes and methods
Metrics_DoubleMetricValue_value: Property = Property(name="value", type=StringType)
Metrics_DoubleMetricValue.attributes={Metrics_DoubleMetricValue_value}

# Relationships
values0: BinaryAssociation = BinaryAssociation(
    name="values0",
    ends={
        Property(name="MetricValue", type=Metrics_Metric, multiplicity=Multiplicity(1, 1)),
        Property(name="Metrics_Metric", type=MetricValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Metrics_StringMetricValue_MetricValue = Generalization(general=MetricValue, specific=Metrics_StringMetricValue)
gen_Metrics_BooleanMetricValue_MetricValue = Generalization(general=MetricValue, specific=Metrics_BooleanMetricValue)
gen_Metrics_IntegerMetricValue_MetricValue = Generalization(general=MetricValue, specific=Metrics_IntegerMetricValue)
gen_Metrics_DoubleMetricValue_MetricValue = Generalization(general=MetricValue, specific=Metrics_DoubleMetricValue)

# Domain Model
domain_model = DomainModel(
    name="Metrics",
    types={Metrics_Metric, MetricValue, Metrics_MetricValue, Metrics_StringMetricValue, Metrics_BooleanMetricValue, Metrics_IntegerMetricValue, Metrics_DoubleMetricValue},
    associations={values0},
    generalizations={gen_Metrics_StringMetricValue_MetricValue, gen_Metrics_BooleanMetricValue_MetricValue, gen_Metrics_IntegerMetricValue_MetricValue, gen_Metrics_DoubleMetricValue_MetricValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)