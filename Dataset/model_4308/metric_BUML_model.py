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
simple_metrics_MetricsSet = Class(name="simple::metrics::MetricsSet")
simple_metrics_Metric = Class(name="simple::metrics::Metric")

# simple_metrics_MetricsSet class attributes and methods
simple_metrics_MetricsSet_name: Property = Property(name="name", type=StringType)
simple_metrics_MetricsSet.attributes={simple_metrics_MetricsSet_name}

# simple_metrics_Metric class attributes and methods
simple_metrics_Metric_name: Property = Property(name="name", type=StringType)
simple_metrics_Metric_value: Property = Property(name="value", type=StringType)
simple_metrics_Metric.attributes={simple_metrics_Metric_name, simple_metrics_Metric_value}

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="simple_metrics_Metric", type=simple_metrics_MetricsSet, multiplicity=Multiplicity(1, 1)),
        Property(name="simple_metrics_MetricsSet", type=simple_metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="simple_metrics",
    types={simple_metrics_MetricsSet, simple_metrics_Metric},
    associations={metrics0},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)