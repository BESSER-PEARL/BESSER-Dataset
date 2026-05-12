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
Class_ = Class(name="Class")
Class2 = Class(name="Class2")

# Gato class attributes and methods
Gato_nombre: Property = Property(name="nombre", type=StringType)
Gato_raza: Property = Property(name="raza", type=StringType)
Gato_color: Property = Property(name="color", type=StringType)
Gato.attributes={Gato_nombre, Gato_color, Gato_raza}

# Class class attributes and methods

# Class2 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_mNc6IFrmEeiyA_1nwijzkg",
    types={Gato, Class_, Class2},
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