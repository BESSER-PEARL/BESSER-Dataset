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
Gato = Class(name="Gato")

# Gato class attributes and methods
Gato_Nombre: Property = Property(name="Nombre", type=StringType)
Gato_Raza: Property = Property(name="Raza", type=StringType)
Gato_Color: Property = Property(name="Color", type=StringType)
Gato.attributes={Gato_Color, Gato_Raza, Gato_Nombre}

# Domain Model
domain_model = DomainModel(
    name="_KBIOAFnYEeiyA_1nwijzkg",
    types={Gato},
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