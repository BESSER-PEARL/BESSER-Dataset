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
overloads_SuperClass = Class(name="overloads::SuperClass")
overloads_SubClass = Class(name="overloads::SubClass")
SuperClass = Class(name="SuperClass")

# overloads_SuperClass class attributes and methods
overloads_SuperClass_m_notOverloaded: Method = Method(name="notOverloaded", parameters={Parameter(name='par')}, type=StringType)
overloads_SuperClass_m_overloaded: Method = Method(name="overloaded", parameters={Parameter(name='par')}, type=StringType)
overloads_SuperClass.methods={overloads_SuperClass_m_overloaded, overloads_SuperClass_m_notOverloaded}

# overloads_SubClass class attributes and methods
overloads_SubClass_m_notOverloaded: Method = Method(name="notOverloaded", parameters={Parameter(name='par')}, type=StringType)
overloads_SubClass_m_overloaded: Method = Method(name="overloaded", parameters={Parameter(name='par')}, type=StringType)
overloads_SubClass.methods={overloads_SubClass_m_overloaded, overloads_SubClass_m_notOverloaded}

# SuperClass class attributes and methods

# Generalizations
gen_overloads_SubClass_SuperClass = Generalization(general=SuperClass, specific=overloads_SubClass)

# Domain Model
domain_model = DomainModel(
    name="overloads",
    types={overloads_SuperClass, overloads_SubClass, SuperClass},
    associations={},
    generalizations={gen_overloads_SubClass_SuperClass},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)