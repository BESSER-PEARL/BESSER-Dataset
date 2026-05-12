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
UseCases_Classifier = Class(name="UseCases_Classifier")
Instance = Class(name="Instance")
UseCases_Instance = Class(name="UseCases_Instance")
Classifier = Class(name="Classifier")
UseCases_Actor = Class(name="UseCases_Actor")
UseCases_UseCase = Class(name="UseCases_UseCase")
Include = Class(name="Include")
Extend = Class(name="Extend")
ExtensionPoint = Class(name="ExtensionPoint")
UseCases_UseCaseInstance = Class(name="UseCases_UseCaseInstance")
UseCases_RelationShip = Class(name="UseCases_RelationShip", is_abstract=True)
UseCases_Include = Class(name="UseCases_Include")
RelationShip = Class(name="RelationShip")
UseCase = Class(name="UseCase")
UseCases_Extend = Class(name="UseCases_Extend")
BooleanExpression = Class(name="BooleanExpression")
UseCases_BooleanExpression = Class(name="UseCases_BooleanExpression")
UseCases_ModelElement = Class(name="UseCases_ModelElement", is_abstract=True)
UseCases_ExtensionPoint = Class(name="UseCases_ExtensionPoint")
ModelElement = Class(name="ModelElement")
LocationReference = Class(name="LocationReference")
UseCases_LocationReference = Class(name="UseCases_LocationReference")

# UseCases_Classifier class attributes and methods

# Instance class attributes and methods

# UseCases_Instance class attributes and methods

# Classifier class attributes and methods

# UseCases_Actor class attributes and methods

# UseCases_UseCase class attributes and methods
UseCases_UseCase_extensionPoint: Property = Property(name="extensionPoint", type=StringType)
UseCases_UseCase.attributes={UseCases_UseCase_extensionPoint}

# Include class attributes and methods

# Extend class attributes and methods

# ExtensionPoint class attributes and methods

# UseCases_UseCaseInstance class attributes and methods

# UseCases_RelationShip class attributes and methods

# UseCases_Include class attributes and methods

# RelationShip class attributes and methods

# UseCase class attributes and methods

# UseCases_Extend class attributes and methods

# BooleanExpression class attributes and methods

# UseCases_BooleanExpression class attributes and methods
UseCases_BooleanExpression_value: Property = Property(name="value", type=StringType)
UseCases_BooleanExpression.attributes={UseCases_BooleanExpression_value}

# UseCases_ModelElement class attributes and methods

# UseCases_ExtensionPoint class attributes and methods

# ModelElement class attributes and methods

# LocationReference class attributes and methods

# UseCases_LocationReference class attributes and methods
UseCases_LocationReference_value: Property = Property(name="value", type=StringType)
UseCases_LocationReference.attributes={UseCases_LocationReference_value}

# Relationships
instance0: BinaryAssociation = BinaryAssociation(
    name="instance0",
    ends={
        Property(name="Instance", type=UseCases_Classifier, multiplicity=Multiplicity(1, 1)),
        Property(name="classifier", type=Instance, multiplicity=Multiplicity(0, 9999))
    }
)
classifier1: BinaryAssociation = BinaryAssociation(
    name="classifier1",
    ends={
        Property(name="Classifier", type=UseCases_Instance, multiplicity=Multiplicity(1, 1)),
        Property(name="instance", type=Classifier, multiplicity=Multiplicity(1, 9999))
    }
)
includeAddition2: BinaryAssociation = BinaryAssociation(
    name="includeAddition2",
    ends={
        Property(name="Include", type=UseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="addition", type=Include, multiplicity=Multiplicity(1, 1))
    }
)
includeBase3: BinaryAssociation = BinaryAssociation(
    name="includeBase3",
    ends={
        Property(name="Include4", type=UseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base", type=Include, multiplicity=Multiplicity(1, 1))
    }
)
extendExtension5: BinaryAssociation = BinaryAssociation(
    name="extendExtension5",
    ends={
        Property(name="Extend", type=UseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="extension", type=Extend, multiplicity=Multiplicity(1, 1))
    }
)
extendBase6: BinaryAssociation = BinaryAssociation(
    name="extendBase6",
    ends={
        Property(name="Extend8", type=UseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="base7", type=Extend, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoints9: BinaryAssociation = BinaryAssociation(
    name="extensionPoints9",
    ends={
        Property(name="ExtensionPoint", type=UseCases_UseCase, multiplicity=Multiplicity(1, 1)),
        Property(name="useCase", type=ExtensionPoint, multiplicity=Multiplicity(0, 9999))
    }
)
addition10: BinaryAssociation = BinaryAssociation(
    name="addition10",
    ends={
        Property(name="UseCase", type=UseCases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includeAddition", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base11: BinaryAssociation = BinaryAssociation(
    name="base11",
    ends={
        Property(name="UseCase12", type=UseCases_Include, multiplicity=Multiplicity(1, 1)),
        Property(name="includeBase", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="BooleanExpression", type=UseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCases_Extend", type=BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
extension14: BinaryAssociation = BinaryAssociation(
    name="extension14",
    ends={
        Property(name="UseCase15", type=UseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extendExtension", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
base16: BinaryAssociation = BinaryAssociation(
    name="base16",
    ends={
        Property(name="UseCase17", type=UseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extendBase", type=UseCase, multiplicity=Multiplicity(1, 1))
    }
)
extensionPoint18: BinaryAssociation = BinaryAssociation(
    name="extensionPoint18",
    ends={
        Property(name="ExtensionPoint19", type=UseCases_Extend, multiplicity=Multiplicity(1, 1)),
        Property(name="extend", type=ExtensionPoint, multiplicity=Multiplicity(1, 9999))
    }
)
location20: BinaryAssociation = BinaryAssociation(
    name="location20",
    ends={
        Property(name="LocationReference", type=UseCases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="UseCases_ExtensionPoint", type=LocationReference, multiplicity=Multiplicity(1, 1))
    }
)
extend21: BinaryAssociation = BinaryAssociation(
    name="extend21",
    ends={
        Property(name="Extend22", type=UseCases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoint", type=Extend, multiplicity=Multiplicity(0, 9999))
    }
)
useCase23: BinaryAssociation = BinaryAssociation(
    name="useCase23",
    ends={
        Property(name="UseCase24", type=UseCases_ExtensionPoint, multiplicity=Multiplicity(1, 1)),
        Property(name="extensionPoints", type=UseCase, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_UseCases_Actor_Classifier = Generalization(general=Classifier, specific=UseCases_Actor)
gen_UseCases_UseCase_Classifier = Generalization(general=Classifier, specific=UseCases_UseCase)
gen_UseCases_UseCaseInstance_Instance = Generalization(general=Instance, specific=UseCases_UseCaseInstance)
gen_UseCases_Include_RelationShip = Generalization(general=RelationShip, specific=UseCases_Include)
gen_UseCases_Extend_RelationShip = Generalization(general=RelationShip, specific=UseCases_Extend)
gen_UseCases_ExtensionPoint_ModelElement = Generalization(general=ModelElement, specific=UseCases_ExtensionPoint)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={UseCases_Classifier, Instance, UseCases_Instance, Classifier, UseCases_Actor, UseCases_UseCase, Include, Extend, ExtensionPoint, UseCases_UseCaseInstance, UseCases_RelationShip, UseCases_Include, RelationShip, UseCase, UseCases_Extend, BooleanExpression, UseCases_BooleanExpression, UseCases_ModelElement, UseCases_ExtensionPoint, ModelElement, LocationReference, UseCases_LocationReference},
    associations={instance0, classifier1, includeAddition2, includeBase3, extendExtension5, extendBase6, extensionPoints9, addition10, base11, condition13, extension14, base16, extensionPoint18, location20, extend21, useCase23},
    generalizations={gen_UseCases_Actor_Classifier, gen_UseCases_UseCase_Classifier, gen_UseCases_UseCaseInstance_Instance, gen_UseCases_Include_RelationShip, gen_UseCases_Extend_RelationShip, gen_UseCases_ExtensionPoint_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)