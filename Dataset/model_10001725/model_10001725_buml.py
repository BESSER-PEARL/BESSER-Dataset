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
Gato_nombre: Property = Property(name="nombre", type=StringType)
Gato_raza: Property = Property(name="raza", type=StringType)
Gato_color: Property = Property(name="color", type=StringType)
Gato.attributes={Gato_color, Gato_raza, Gato_nombre}

# Domain Model
domain_model = DomainModel(
    name="_R6OG8Fh0EeioG62n2D5JZQ",
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