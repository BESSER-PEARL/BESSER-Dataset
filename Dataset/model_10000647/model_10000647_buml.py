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
Gato.attributes={Gato_raza, Gato_color, Gato_nombre}

# Domain Model
domain_model = DomainModel(
    name="_503d76a6_cc0b_4fab_9e1e_9a254a26ec4a",
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