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
TypeGraphBasic_TMember = Class(name="TypeGraphBasic::TMember", is_abstract=True)
TypeGraphBasic_TClass = Class(name="TypeGraphBasic::TClass")
TypeGraphBasic_TSignature = Class(name="TypeGraphBasic::TSignature", is_abstract=True)
TypeGraphBasic_TPackage = Class(name="TypeGraphBasic::TPackage")
TSignature = Class(name="TSignature")
TypeGraphBasic_TField = Class(name="TypeGraphBasic::TField")
TypeGraphBasic_TFieldSignature = Class(name="TypeGraphBasic::TFieldSignature")
TypeGraphBasic_TFieldDefinition = Class(name="TypeGraphBasic::TFieldDefinition")
TMember = Class(name="TMember")
TypeGraphBasic_TMethodDefinition = Class(name="TypeGraphBasic::TMethodDefinition")
TypeGraphBasic_TMethod = Class(name="TypeGraphBasic::TMethod")
TypeGraphBasic_TMethodSignature = Class(name="TypeGraphBasic::TMethodSignature")
TypeGraphBasic_TypeGraph = Class(name="TypeGraphBasic::TypeGraph")

# TypeGraphBasic_TMember class attributes and methods

# TypeGraphBasic_TClass class attributes and methods
TypeGraphBasic_TClass_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TClass.attributes={TypeGraphBasic_TClass_tName}

# TypeGraphBasic_TSignature class attributes and methods

# TypeGraphBasic_TPackage class attributes and methods
TypeGraphBasic_TPackage_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TPackage.attributes={TypeGraphBasic_TPackage_tName}

# TSignature class attributes and methods

# TypeGraphBasic_TField class attributes and methods
TypeGraphBasic_TField_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TField.attributes={TypeGraphBasic_TField_tName}

# TypeGraphBasic_TFieldSignature class attributes and methods

# TypeGraphBasic_TFieldDefinition class attributes and methods

# TMember class attributes and methods

# TypeGraphBasic_TMethodDefinition class attributes and methods

# TypeGraphBasic_TMethod class attributes and methods
TypeGraphBasic_TMethod_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TMethod.attributes={TypeGraphBasic_TMethod_tName}

# TypeGraphBasic_TMethodSignature class attributes and methods

# TypeGraphBasic_TypeGraph class attributes and methods
TypeGraphBasic_TypeGraph_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TypeGraph.attributes={TypeGraphBasic_TypeGraph_tName}

# Relationships
defines7: BinaryAssociation = BinaryAssociation(
    name="defines7",
    ends={
        Property(name="TypeGraphBasic_TMember", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass8", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentClass1: BinaryAssociation = BinaryAssociation(
    name="parentClass1",
    ends={
        Property(name="TClass", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="childClasses", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
childClasses3: BinaryAssociation = BinaryAssociation(
    name="childClasses3",
    ends={
        Property(name="TClass4", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="parentClass", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
signature5: BinaryAssociation = BinaryAssociation(
    name="signature5",
    ends={
        Property(name="TypeGraphBasic_TSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass", type=TypeGraphBasic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
package6: BinaryAssociation = BinaryAssociation(
    name="package6",
    ends={
        Property(name="TPackage", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="containedClasses", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1))
    }
)
signature15: BinaryAssociation = BinaryAssociation(
    name="signature15",
    ends={
        Property(name="TFieldSignature16", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
signatures9: BinaryAssociation = BinaryAssociation(
    name="signatures9",
    ends={
        Property(name="TFieldSignature", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="field", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hiding11: BinaryAssociation = BinaryAssociation(
    name="hiding11",
    ends={
        Property(name="TFieldDefinition", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiddenBy", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy13: BinaryAssociation = BinaryAssociation(
    name="hiddenBy13",
    ends={
        Property(name="TFieldDefinition14", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiding", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
signatures25: BinaryAssociation = BinaryAssociation(
    name="signatures25",
    ends={
        Property(name="TMethodSignature", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
definitions17: BinaryAssociation = BinaryAssociation(
    name="definitions17",
    ends={
        Property(name="TFieldDefinition18", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
field19: BinaryAssociation = BinaryAssociation(
    name="field19",
    ends={
        Property(name="TField", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1))
    }
)
type20: BinaryAssociation = BinaryAssociation(
    name="type20",
    ends={
        Property(name="TypeGraphBasic_TClass21", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TFieldSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1))
    }
)
access23: BinaryAssociation = BinaryAssociation(
    name="access23",
    ends={
        Property(name="TypeGraphBasic_TMember24", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMember22", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999))
    }
)
overloadedBy38: BinaryAssociation = BinaryAssociation(
    name="overloadedBy38",
    ends={
        Property(name="overloading", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999)),
        Property(name="TMethodDefinition39", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1))
    }
)
returnType40: BinaryAssociation = BinaryAssociation(
    name="returnType40",
    ends={
        Property(name="TypeGraphBasic_TClass41", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodDefinition", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
signature26: BinaryAssociation = BinaryAssociation(
    name="signature26",
    ends={
        Property(name="TMethodSignature28", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions27", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1))
    }
)
overriding30: BinaryAssociation = BinaryAssociation(
    name="overriding30",
    ends={
        Property(name="TMethodDefinition", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overriddenBy", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 1))
    }
)
overriddenBy32: BinaryAssociation = BinaryAssociation(
    name="overriddenBy32",
    ends={
        Property(name="TMethodDefinition33", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overriding", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloading35: BinaryAssociation = BinaryAssociation(
    name="overloading35",
    ends={
        Property(name="TMethodDefinition36", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overloadedBy", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
subpackage52: BinaryAssociation = BinaryAssociation(
    name="subpackage52",
    ends={
        Property(name="TPackage53", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent55: BinaryAssociation = BinaryAssociation(
    name="parent55",
    ends={
        Property(name="TPackage56", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="subpackage", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
method42: BinaryAssociation = BinaryAssociation(
    name="method42",
    ends={
        Property(name="TMethod", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures43", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1))
    }
)
definitions44: BinaryAssociation = BinaryAssociation(
    name="definitions44",
    ends={
        Property(name="TMethodDefinition46", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature45", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
paramList47: BinaryAssociation = BinaryAssociation(
    name="paramList47",
    ends={
        Property(name="TypeGraphBasic_TClass48", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
containedClasses49: BinaryAssociation = BinaryAssociation(
    name="containedClasses49",
    ends={
        Property(name="TClass50", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
packages57: BinaryAssociation = BinaryAssociation(
    name="packages57",
    ends={
        Property(name="TypeGraphBasic_TPackage", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods58: BinaryAssociation = BinaryAssociation(
    name="methods58",
    ends={
        Property(name="TypeGraphBasic_TMethod", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph59", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields60: BinaryAssociation = BinaryAssociation(
    name="fields60",
    ends={
        Property(name="TypeGraphBasic_TField", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph61", type=TypeGraphBasic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes62: BinaryAssociation = BinaryAssociation(
    name="classes62",
    ends={
        Property(name="TypeGraphBasic_TClass64", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph63", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_TypeGraphBasic_TFieldSignature_TSignature = Generalization(general=TSignature, specific=TypeGraphBasic_TFieldSignature)
gen_TypeGraphBasic_TFieldDefinition_TMember = Generalization(general=TMember, specific=TypeGraphBasic_TFieldDefinition)
gen_TypeGraphBasic_TMethodDefinition_TMember = Generalization(general=TMember, specific=TypeGraphBasic_TMethodDefinition)
gen_TypeGraphBasic_TMethodSignature_TSignature = Generalization(general=TSignature, specific=TypeGraphBasic_TMethodSignature)

# Domain Model
domain_model = DomainModel(
    name="TypeGraphBasic",
    types={TypeGraphBasic_TMember, TypeGraphBasic_TClass, TypeGraphBasic_TSignature, TypeGraphBasic_TPackage, TSignature, TypeGraphBasic_TField, TypeGraphBasic_TFieldSignature, TypeGraphBasic_TFieldDefinition, TMember, TypeGraphBasic_TMethodDefinition, TypeGraphBasic_TMethod, TypeGraphBasic_TMethodSignature, TypeGraphBasic_TypeGraph},
    associations={defines7, parentClass1, childClasses3, signature5, package6, signature15, signatures9, hiding11, hiddenBy13, signatures25, definitions17, field19, type20, access23, overloadedBy38, returnType40, signature26, overriding30, overriddenBy32, overloading35, subpackage52, parent55, method42, definitions44, paramList47, containedClasses49, packages57, methods58, fields60, classes62},
    generalizations={gen_TypeGraphBasic_TFieldSignature_TSignature, gen_TypeGraphBasic_TFieldDefinition_TMember, gen_TypeGraphBasic_TMethodDefinition_TMember, gen_TypeGraphBasic_TMethodSignature_TSignature},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)