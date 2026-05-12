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
useCase_Includes = Class(name="useCase_Includes")
useCase_Extends = Class(name="useCase_Extends")
useCase_UseCase = Class(name="useCase_UseCase")
useCase_Subsystem = Class(name="useCase_Subsystem")
useCase_Actor = Class(name="useCase_Actor")
useCase_Case = Class(name="useCase_Case")
useCase_ExtensionPoint = Class(name="useCase_ExtensionPoint")
useCase_Inheritance = Class(name="useCase_Inheritance")
useCase_Uses = Class(name="useCase_Uses")

# useCase_Includes class attributes and methods
useCase_Includes_name: Property = Property(name="name", type=StringType)
useCase_Includes_rules: Property = Property(name="rules", type=StringType)
useCase_Includes.attributes={useCase_Includes_name, useCase_Includes_rules}

# useCase_Extends class attributes and methods
useCase_Extends_name: Property = Property(name="name", type=StringType)
useCase_Extends_rules: Property = Property(name="rules", type=StringType)
useCase_Extends.attributes={useCase_Extends_name, useCase_Extends_rules}

# useCase_UseCase class attributes and methods

# useCase_Subsystem class attributes and methods
useCase_Subsystem_name: Property = Property(name="name", type=StringType)
useCase_Subsystem.attributes={useCase_Subsystem_name}

# useCase_Actor class attributes and methods
useCase_Actor_name: Property = Property(name="name", type=StringType)
useCase_Actor.attributes={useCase_Actor_name}

# useCase_Case class attributes and methods
useCase_Case_name: Property = Property(name="name", type=StringType)
useCase_Case.attributes={useCase_Case_name}

# useCase_ExtensionPoint class attributes and methods
useCase_ExtensionPoint_name: Property = Property(name="name", type=StringType)
useCase_ExtensionPoint.attributes={useCase_ExtensionPoint_name}

# useCase_Inheritance class attributes and methods
useCase_Inheritance_name: Property = Property(name="name", type=StringType)
useCase_Inheritance.attributes={useCase_Inheritance_name}

# useCase_Uses class attributes and methods
useCase_Uses_name: Property = Property(name="name", type=StringType)
useCase_Uses_multiplicity: Property = Property(name="multiplicity", type=StringType)
useCase_Uses.attributes={useCase_Uses_multiplicity, useCase_Uses_name}

# Relationships
includes7: BinaryAssociation = BinaryAssociation(
    name="includes7",
    ends={
        Property(name="useCase_Includes", type=useCase_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Case8", type=useCase_Includes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extends9: BinaryAssociation = BinaryAssociation(
    name="extends9",
    ends={
        Property(name="useCase_Extends", type=useCase_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Case10", type=useCase_Extends, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
systems0: BinaryAssociation = BinaryAssociation(
    name="systems0",
    ends={
        Property(name="useCase_Subsystem", type=useCase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_UseCase", type=useCase_Subsystem, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
actors1: BinaryAssociation = BinaryAssociation(
    name="actors1",
    ends={
        Property(name="useCase_Actor", type=useCase_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_UseCase2", type=useCase_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cases3: BinaryAssociation = BinaryAssociation(
    name="cases3",
    ends={
        Property(name="useCase_Case", type=useCase_Subsystem, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Subsystem4", type=useCase_Case, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
extensions5: BinaryAssociation = BinaryAssociation(
    name="extensions5",
    ends={
        Property(name="useCase_ExtensionPoint", type=useCase_Case, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Case6", type=useCase_ExtensionPoint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inheritances11: BinaryAssociation = BinaryAssociation(
    name="inheritances11",
    ends={
        Property(name="useCase_Inheritance", type=useCase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Actor12", type=useCase_Inheritance, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uses13: BinaryAssociation = BinaryAssociation(
    name="uses13",
    ends={
        Property(name="useCase_Uses", type=useCase_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase_Actor14", type=useCase_Uses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="useCase",
    types={useCase_Includes, useCase_Extends, useCase_UseCase, useCase_Subsystem, useCase_Actor, useCase_Case, useCase_ExtensionPoint, useCase_Inheritance, useCase_Uses},
    associations={includes7, extends9, systems0, actors1, cases3, extensions5, inheritances11, uses13},
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