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
UML2_Port = Class(name="UML2::Port")
Property_ = Class(name="Property")
UML2_ExtensionEnd = Class(name="UML2::ExtensionEnd")
UML2_Property = Class(name="UML2::Property")

# UML2_Port class attributes and methods

# Property class attributes and methods

# UML2_ExtensionEnd class attributes and methods

# UML2_Property class attributes and methods
UML2_Property_isDerived: Property = Property(name="isDerived", type=BooleanType)
UML2_Property_isDerivedUnion: Property = Property(name="isDerivedUnion", type=BooleanType)
UML2_Property.attributes={UML2_Property_isDerived, UML2_Property_isDerivedUnion}

# Generalizations
gen_UML2_Port_Property = Generalization(general=Property_, specific=UML2_Port)
gen_UML2_ExtensionEnd_Property = Generalization(general=Property_, specific=UML2_ExtensionEnd)

# Domain Model
domain_model = DomainModel(
    name="UML2",
    types={UML2_Port, Property_, UML2_ExtensionEnd, UML2_Property},
    associations={},
    generalizations={gen_UML2_Port_Property, gen_UML2_ExtensionEnd_Property},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)