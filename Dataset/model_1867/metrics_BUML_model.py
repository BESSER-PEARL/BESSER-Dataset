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
MetricKind: Enumeration = Enumeration(
    name="MetricKind",
    literals={
            EnumerationLiteral(name="FILE"),
			EnumerationLiteral(name="RDMS")
    }
)

# Classes
metrics_Metric = Class(name="metrics::Metric")
metrics_MetricLibrary = Class(name="metrics::MetricLibrary")
metrics_MetricSource = Class(name="metrics::MetricSource")

# metrics_Metric class attributes and methods

# metrics_MetricLibrary class attributes and methods
metrics_MetricLibrary_name: Property = Property(name="name", type=StringType)
metrics_MetricLibrary.attributes={metrics_MetricLibrary_name}

# metrics_MetricSource class attributes and methods
metrics_MetricSource_lastContact: Property = Property(name="lastContact", type=StringType)
metrics_MetricSource_lastPurge: Property = Property(name="lastPurge", type=StringType)
metrics_MetricSource_mappingFile: Property = Property(name="mappingFile", type=StringType)
metrics_MetricSource_metrickind: Property = Property(name="metrickind", type=StringType)
metrics_MetricSource_metricLocation: Property = Property(name="metricLocation", type=StringType)
metrics_MetricSource_name: Property = Property(name="name", type=StringType)
metrics_MetricSource.attributes={metrics_MetricSource_name, metrics_MetricSource_mappingFile, metrics_MetricSource_lastPurge, metrics_MetricSource_metrickind, metrics_MetricSource_lastContact, metrics_MetricSource_metricLocation}

# Relationships
metricRefs1: BinaryAssociation = BinaryAssociation(
    name="metricRefs1",
    ends={
        Property(name="networks.ecoreMetric", type=metrics_MetricSource, multiplicity=Multiplicity(1, 1)),
        Property(name="metricSource", type=metrics_Metric, multiplicity=Multiplicity(0, 9999))
    }
)
metricSources0: BinaryAssociation = BinaryAssociation(
    name="metricSources0",
    ends={
        Property(name="metrics_MetricSource", type=metrics_MetricLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_MetricLibrary", type=metrics_MetricSource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_Metric, metrics_MetricLibrary, metrics_MetricSource, MetricKind},
    associations={metricRefs1, metricSources0},
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