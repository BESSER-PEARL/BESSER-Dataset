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
E: Enumeration = Enumeration(
    name="E",
    literals={
            
    }
)

# Classes
a_C = Class(name="a::C")
a_C2 = Class(name="a::C2")
a_Zug = Class(name="a::Zug")

# a_C class attributes and methods
a_C_a: Property = Property(name="a", type=StringType)
a_C_m_o: Method = Method(name="o", parameters={Parameter(name='p')})
a_C.attributes={a_C_a}
a_C.methods={a_C_m_o}

# a_C2 class attributes and methods

# a_Zug class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="a",
    types={a_C, a_C2, a_Zug, E},
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