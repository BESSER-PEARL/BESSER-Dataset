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
TypeGraphBasic_TClass = Class(name="TypeGraphBasic::TClass")
TypeGraphBasic_TSignature = Class(name="TypeGraphBasic::TSignature", is_abstract=True)
TypeGraphBasic_TPackage = Class(name="TypeGraphBasic::TPackage")
TypeGraphBasic_TMember = Class(name="TypeGraphBasic::TMember", is_abstract=True)
TypeGraphBasic_TField = Class(name="TypeGraphBasic::TField")
TypeGraphBasic_TFieldSignature = Class(name="TypeGraphBasic::TFieldSignature")
TypeGraphBasic_TFieldDefinition = Class(name="TypeGraphBasic::TFieldDefinition")
TMember = Class(name="TMember")
TSignature = Class(name="TSignature")
TypeGraphBasic_TMethod = Class(name="TypeGraphBasic::TMethod")
TypeGraphBasic_TMethodSignature = Class(name="TypeGraphBasic::TMethodSignature")
TypeGraphBasic_TMethodDefinition = Class(name="TypeGraphBasic::TMethodDefinition")
TypeGraphBasic_TypeGraph = Class(name="TypeGraphBasic::TypeGraph")

# TypeGraphBasic_TClass class attributes and methods
TypeGraphBasic_TClass_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TClass.attributes={TypeGraphBasic_TClass_tName}

# TypeGraphBasic_TSignature class attributes and methods

# TypeGraphBasic_TPackage class attributes and methods
TypeGraphBasic_TPackage_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TPackage.attributes={TypeGraphBasic_TPackage_tName}

# TypeGraphBasic_TMember class attributes and methods

# TypeGraphBasic_TField class attributes and methods
TypeGraphBasic_TField_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TField.attributes={TypeGraphBasic_TField_tName}

# TypeGraphBasic_TFieldSignature class attributes and methods

# TypeGraphBasic_TFieldDefinition class attributes and methods

# TMember class attributes and methods

# TSignature class attributes and methods

# TypeGraphBasic_TMethod class attributes and methods
TypeGraphBasic_TMethod_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TMethod.attributes={TypeGraphBasic_TMethod_tName}

# TypeGraphBasic_TMethodSignature class attributes and methods

# TypeGraphBasic_TMethodDefinition class attributes and methods

# TypeGraphBasic_TypeGraph class attributes and methods
TypeGraphBasic_TypeGraph_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TypeGraph.attributes={TypeGraphBasic_TypeGraph_tName}

# Relationships
childClasses4: BinaryAssociation = BinaryAssociation(
    name="childClasses4",
    ends={
        Property(name="6", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="5", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
signature7: BinaryAssociation = BinaryAssociation(
    name="signature7",
    ends={
        Property(name="TypeGraphBasic_TSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass", type=TypeGraphBasic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
package8: BinaryAssociation = BinaryAssociation(
    name="package8",
    ends={
        Property(name="10", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1))
    }
)
defines11: BinaryAssociation = BinaryAssociation(
    name="defines11",
    ends={
        Property(name="TypeGraphBasic_TMember", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass12", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signatures13: BinaryAssociation = BinaryAssociation(
    name="signatures13",
    ends={
        Property(name="15", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hiding17: BinaryAssociation = BinaryAssociation(
    name="hiding17",
    ends={
        Property(name="19", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="18", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy21: BinaryAssociation = BinaryAssociation(
    name="hiddenBy21",
    ends={
        Property(name="23", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="22", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
parentClass1: BinaryAssociation = BinaryAssociation(
    name="parentClass1",
    ends={
        Property(name="2", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
signature24: BinaryAssociation = BinaryAssociation(
    name="signature24",
    ends={
        Property(name="26", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
definitions27: BinaryAssociation = BinaryAssociation(
    name="definitions27",
    ends={
        Property(name="29", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
field30: BinaryAssociation = BinaryAssociation(
    name="field30",
    ends={
        Property(name="32", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="31", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1))
    }
)
type33: BinaryAssociation = BinaryAssociation(
    name="type33",
    ends={
        Property(name="TypeGraphBasic_TClass34", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TFieldSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1))
    }
)
access36: BinaryAssociation = BinaryAssociation(
    name="access36",
    ends={
        Property(name="TypeGraphBasic_TMember37", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMember35", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999))
    }
)
signatures38: BinaryAssociation = BinaryAssociation(
    name="signatures38",
    ends={
        Property(name="40", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="39", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature41: BinaryAssociation = BinaryAssociation(
    name="signature41",
    ends={
        Property(name="43", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="42", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1))
    }
)
overriding45: BinaryAssociation = BinaryAssociation(
    name="overriding45",
    ends={
        Property(name="47", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="46", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 1))
    }
)
overloading53: BinaryAssociation = BinaryAssociation(
    name="overloading53",
    ends={
        Property(name="55", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="54", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloadedBy57: BinaryAssociation = BinaryAssociation(
    name="overloadedBy57",
    ends={
        Property(name="59", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="58", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
returnType60: BinaryAssociation = BinaryAssociation(
    name="returnType60",
    ends={
        Property(name="TypeGraphBasic_TClass61", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodDefinition", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
method62: BinaryAssociation = BinaryAssociation(
    name="method62",
    ends={
        Property(name="64", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="63", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1))
    }
)
definitions65: BinaryAssociation = BinaryAssociation(
    name="definitions65",
    ends={
        Property(name="67", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="66", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
paramList68: BinaryAssociation = BinaryAssociation(
    name="paramList68",
    ends={
        Property(name="TypeGraphBasic_TClass69", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
containedClasses70: BinaryAssociation = BinaryAssociation(
    name="containedClasses70",
    ends={
        Property(name="72", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="71", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
subpackage74: BinaryAssociation = BinaryAssociation(
    name="subpackage74",
    ends={
        Property(name="76", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="75", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
overriddenBy49: BinaryAssociation = BinaryAssociation(
    name="overriddenBy49",
    ends={
        Property(name="51", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="50", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
parent78: BinaryAssociation = BinaryAssociation(
    name="parent78",
    ends={
        Property(name="80", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="79", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
packages81: BinaryAssociation = BinaryAssociation(
    name="packages81",
    ends={
        Property(name="TypeGraphBasic_TPackage", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods82: BinaryAssociation = BinaryAssociation(
    name="methods82",
    ends={
        Property(name="TypeGraphBasic_TMethod", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph83", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields84: BinaryAssociation = BinaryAssociation(
    name="fields84",
    ends={
        Property(name="TypeGraphBasic_TField", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph85", type=TypeGraphBasic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes86: BinaryAssociation = BinaryAssociation(
    name="classes86",
    ends={
        Property(name="TypeGraphBasic_TClass88", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph87", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TypeGraphBasic_TFieldDefinition_TMember = Generalization(general=TMember, specific=TypeGraphBasic_TFieldDefinition)
gen_TypeGraphBasic_TFieldSignature_TSignature = Generalization(general=TSignature, specific=TypeGraphBasic_TFieldSignature)
gen_TypeGraphBasic_TMethodDefinition_TMember = Generalization(general=TMember, specific=TypeGraphBasic_TMethodDefinition)
gen_TypeGraphBasic_TMethodSignature_TSignature = Generalization(general=TSignature, specific=TypeGraphBasic_TMethodSignature)

# Domain Model
domain_model = DomainModel(
    name="TypeGraphBasic",
    types={TypeGraphBasic_TClass, TypeGraphBasic_TSignature, TypeGraphBasic_TPackage, TypeGraphBasic_TMember, TypeGraphBasic_TField, TypeGraphBasic_TFieldSignature, TypeGraphBasic_TFieldDefinition, TMember, TSignature, TypeGraphBasic_TMethod, TypeGraphBasic_TMethodSignature, TypeGraphBasic_TMethodDefinition, TypeGraphBasic_TypeGraph},
    associations={childClasses4, signature7, package8, defines11, signatures13, hiding17, hiddenBy21, parentClass1, signature24, definitions27, field30, type33, access36, signatures38, signature41, overriding45, overloading53, overloadedBy57, returnType60, method62, definitions65, paramList68, containedClasses70, subpackage74, overriddenBy49, parent78, packages81, methods82, fields84, classes86},
    generalizations={gen_TypeGraphBasic_TFieldDefinition_TMember, gen_TypeGraphBasic_TFieldSignature_TSignature, gen_TypeGraphBasic_TMethodDefinition_TMember, gen_TypeGraphBasic_TMethodSignature_TSignature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)