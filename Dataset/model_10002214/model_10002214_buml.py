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
Transaccion = Class(name="Transaccion")
MyClass = Class(name="MyClass")
MyClass2 = Class(name="MyClass2")
MyClass3 = Class(name="MyClass3")
MyClass4 = Class(name="MyClass4")
MyClass5 = Class(name="MyClass5")
MyClass6 = Class(name="MyClass6")
MyClass7 = Class(name="MyClass7")
MyClass8 = Class(name="MyClass8")
MyClass9 = Class(name="MyClass9")
MyClass10 = Class(name="MyClass10")
MyClass11 = Class(name="MyClass11")
MyClass12 = Class(name="MyClass12")
MyClass13 = Class(name="MyClass13")
MyClass14 = Class(name="MyClass14")
MyClass15 = Class(name="MyClass15")
MyClass16 = Class(name="MyClass16")
MyClass17 = Class(name="MyClass17")
MyClass18 = Class(name="MyClass18")

# Transaccion class attributes and methods
Transaccion_atributo1: Property = Property(name="atributo1", type=StringType)
Transaccion.attributes={Transaccion_atributo1}

# MyClass class attributes and methods

# MyClass2 class attributes and methods

# MyClass3 class attributes and methods

# MyClass4 class attributes and methods

# MyClass5 class attributes and methods

# MyClass6 class attributes and methods

# MyClass7 class attributes and methods

# MyClass8 class attributes and methods

# MyClass9 class attributes and methods

# MyClass10 class attributes and methods

# MyClass11 class attributes and methods

# MyClass12 class attributes and methods

# MyClass13 class attributes and methods

# MyClass14 class attributes and methods

# MyClass15 class attributes and methods

# MyClass16 class attributes and methods

# MyClass17 class attributes and methods

# MyClass18 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_x9Nb4EyiEeeu8_4LH_yuyg",
    types={Transaccion, MyClass, MyClass2, MyClass3, MyClass4, MyClass5, MyClass6, MyClass7, MyClass8, MyClass9, MyClass10, MyClass11, MyClass12, MyClass13, MyClass14, MyClass15, MyClass16, MyClass17, MyClass18},
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