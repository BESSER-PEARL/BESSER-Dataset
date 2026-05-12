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
Sensoren = Class(name="Sensoren")
T_rsensor = Class(name="T_rsensor")
Fenstersensor = Class(name="Fenstersensor")
Bewegungssensor = Class(name="Bewegungssensor")

# Sensoren class attributes and methods
Sensoren_sensorID: Property = Property(name="sensorID", type=IntegerType)
Sensoren.attributes={Sensoren_sensorID}

# T_rsensor class attributes and methods
T_rsensor_t_rsensorID: Property = Property(name="t_rsensorID", type=IntegerType)
T_rsensor.attributes={T_rsensor_t_rsensorID}

# Fenstersensor class attributes and methods
Fenstersensor_fenstersensorID: Property = Property(name="fenstersensorID", type=IntegerType)
Fenstersensor.attributes={Fenstersensor_fenstersensorID}

# Bewegungssensor class attributes and methods
Bewegungssensor_bewegungssensorID: Property = Property(name="bewegungssensorID", type=IntegerType)
Bewegungssensor.attributes={Bewegungssensor_bewegungssensorID}

# Domain Model
domain_model = DomainModel(
    name="_qADf0KMOEemlGeJsLESUmg",
    types={Sensoren, T_rsensor, Fenstersensor, Bewegungssensor},
    associations={},
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