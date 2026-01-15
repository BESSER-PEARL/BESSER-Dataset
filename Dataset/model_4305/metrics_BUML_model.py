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
metrics_MetricSource = Class(name="metrics::MetricSource")
metrics_Value = Class(name="metrics::Value")

# metrics_MetricSource class attributes and methods
metrics_MetricSource_lastContact: Property = Property(name="lastContact", type=StringType)
metrics_MetricSource_lastPurge: Property = Property(name="lastPurge", type=StringType)
metrics_MetricSource_location: Property = Property(name="location", type=StringType)
metrics_MetricSource_metrickind: Property = Property(name="metrickind", type=StringType)
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_name, metrics_MetricSource_metrickind, metrics_MetricSource_location, metrics_MetricSource_lastPurge, metrics_MetricSource_lastContact}

# metrics_Value class attributes and methods

# Relationships
metricValues0: BinaryAssociation = BinaryAssociation(
    name="metricValues0",
    ends={
        Property(name="metrics_MetricSource", type=metrics_Value, multiplicity=Multiplicity(0, 9999)),
        Property(name="metrics_Value", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_MetricSource, metrics_Value},
    associations={metricValues0},
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