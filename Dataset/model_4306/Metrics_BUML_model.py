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
metrics_MetricsSet = Class(name="metrics::MetricsSet")
metrics_Metric = Class(name="metrics::Metric")

# metrics_MetricsSet class attributes and methods
metrics_MetricsSet_name: Property = Property(name="name", type=StringType)
metrics_MetricsSet.attributes={metrics_MetricsSet_name}

# metrics_Metric class attributes and methods
metrics_Metric_name: Property = Property(name="name", type=StringType)
metrics_Metric_value: Property = Property(name="value", type=StringType)
metrics_Metric.attributes={metrics_Metric_value, metrics_Metric_name}

# Relationships
metrics0: BinaryAssociation = BinaryAssociation(
    name="metrics0",
    ends={
        Property(name="metrics_Metric", type=metrics_MetricsSet, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricsSet", type=metrics_Metric, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_MetricsSet, metrics_Metric},
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