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
metrics_Measurement = Class(name="metrics::Measurement", is_abstract=True)
metrics_ValueMeasurement = Class(name="metrics::ValueMeasurement")
Measurement = Class(name="Measurement")
metrics_LinkMeasurement = Class(name="metrics::LinkMeasurement")
ModelElement = Class(name="ModelElement")
metrics_ComplexMeasurement = Class(name="metrics::ComplexMeasurement")
metrics_Observation = Class(name="metrics::Observation")

# metrics_Measurement class attributes and methods
metrics_Measurement_tag: Property = Property(name="tag", type=StringType)
metrics_Measurement_name: Property = Property(name="name", type=StringType)
metrics_Measurement_error: Property = Property(name="error", type=StringType)
metrics_Measurement.attributes={metrics_Measurement_tag, metrics_Measurement_name, metrics_Measurement_error}

# metrics_ValueMeasurement class attributes and methods
metrics_ValueMeasurement_value: Property = Property(name="value", type=StringType)
metrics_ValueMeasurement.attributes={metrics_ValueMeasurement_value}

# Measurement class attributes and methods

# metrics_LinkMeasurement class attributes and methods

# ModelElement class attributes and methods

# metrics_ComplexMeasurement class attributes and methods

# metrics_Observation class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="ModelElement", type=metrics_LinkMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_LinkMeasurement", type=ModelElement, multiplicity=Multiplicity(0, 1))
    }
)
measurements1: BinaryAssociation = BinaryAssociation(
    name="measurements1",
    ends={
        Property(name="metrics_Measurement", type=metrics_ComplexMeasurement, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_ComplexMeasurement", type=metrics_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
measurements2: BinaryAssociation = BinaryAssociation(
    name="measurements2",
    ends={
        Property(name="metrics_Measurement3", type=metrics_Observation, multiplicity=Multiplicity(1, 1)),
        Property(name="metrics_Observation", type=metrics_Measurement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_metrics_ValueMeasurement_Measurement = Generalization(general=Measurement, specific=metrics_ValueMeasurement)
gen_metrics_LinkMeasurement_Measurement = Generalization(general=Measurement, specific=metrics_LinkMeasurement)
gen_metrics_ComplexMeasurement_Measurement = Generalization(general=Measurement, specific=metrics_ComplexMeasurement)

# Domain Model
domain_model = DomainModel(
    name="metrics",
    types={metrics_Measurement, metrics_ValueMeasurement, Measurement, metrics_LinkMeasurement, ModelElement, metrics_ComplexMeasurement, metrics_Observation},
    associations={elements0, measurements1, measurements2},
    generalizations={gen_metrics_ValueMeasurement_Measurement, gen_metrics_LinkMeasurement_Measurement, gen_metrics_ComplexMeasurement_Measurement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)