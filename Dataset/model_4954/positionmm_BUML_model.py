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
TypeScript: Enumeration = Enumeration(
    name="TypeScript",
    literals={
            EnumerationLiteral(name="PreinstScript"),
			EnumerationLiteral(name="PostinstScript"),
			EnumerationLiteral(name="PrermScript"),
			EnumerationLiteral(name="PostrmScript")
    }
)

# Classes
positionmm_Counter = Class(name="positionmm::Counter")
NamedElement = Class(name="NamedElement")
positionmm_NamedElement = Class(name="positionmm::NamedElement")

# positionmm_Counter class attributes and methods
positionmm_Counter_position: Property = Property(name="position", type=IntegerType)
positionmm_Counter_script: Property = Property(name="script", type=StringType)
positionmm_Counter.attributes={positionmm_Counter_position, positionmm_Counter_script}

# NamedElement class attributes and methods

# positionmm_NamedElement class attributes and methods
positionmm_NamedElement_name: Property = Property(name="name", type=StringType)
positionmm_NamedElement.attributes={positionmm_NamedElement_name}

# Generalizations
gen_positionmm_Counter_NamedElement = Generalization(general=NamedElement, specific=positionmm_Counter)

# Domain Model
domain_model = DomainModel(
    name="positionmm",
    types={positionmm_Counter, NamedElement, positionmm_NamedElement, TypeScript},
    associations={},
    generalizations={gen_positionmm_Counter_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)