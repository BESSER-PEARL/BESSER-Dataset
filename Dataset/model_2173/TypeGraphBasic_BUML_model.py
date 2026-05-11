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
TypeGraphBasic_TClass = Class(name="TypeGraphBasic_TClass")
TypeGraphBasic_TPackage = Class(name="TypeGraphBasic_TPackage")
TypeGraphBasic_TSignature = Class(name="TypeGraphBasic_TSignature", is_abstract=True)
TypeGraphBasic_TMember = Class(name="TypeGraphBasic_TMember", is_abstract=True)
TypeGraphBasic_TField = Class(name="TypeGraphBasic_TField")
TypeGraphBasic_TFieldSignature = Class(name="TypeGraphBasic_TFieldSignature")
TypeGraphBasic_TFieldDefinition = Class(name="TypeGraphBasic_TFieldDefinition")
TMember = Class(name="TMember")
TSignature = Class(name="TSignature")
TypeGraphBasic_TMethod = Class(name="TypeGraphBasic_TMethod")
TypeGraphBasic_TMethodSignature = Class(name="TypeGraphBasic_TMethodSignature")
TypeGraphBasic_TMethodDefinition = Class(name="TypeGraphBasic_TMethodDefinition")
TypeGraphBasic_TParameterList = Class(name="TypeGraphBasic_TParameterList")
TypeGraphBasic_TParameter = Class(name="TypeGraphBasic_TParameter")
TypeGraphBasic_TypeGraph = Class(name="TypeGraphBasic_TypeGraph")

# TypeGraphBasic_TClass class attributes and methods
TypeGraphBasic_TClass_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TClass.attributes={TypeGraphBasic_TClass_tName}

# TypeGraphBasic_TPackage class attributes and methods
TypeGraphBasic_TPackage_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TPackage.attributes={TypeGraphBasic_TPackage_tName}

# TypeGraphBasic_TSignature class attributes and methods

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

# TypeGraphBasic_TParameterList class attributes and methods

# TypeGraphBasic_TParameter class attributes and methods

# TypeGraphBasic_TypeGraph class attributes and methods
TypeGraphBasic_TypeGraph_tName: Property = Property(name="tName", type=StringType)
TypeGraphBasic_TypeGraph.attributes={TypeGraphBasic_TypeGraph_tName}

# Relationships
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="TPackage", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="containedClasses", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1))
    }
)
signature1: BinaryAssociation = BinaryAssociation(
    name="signature1",
    ends={
        Property(name="TypeGraphBasic_TSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass", type=TypeGraphBasic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
defines2: BinaryAssociation = BinaryAssociation(
    name="defines2",
    ends={
        Property(name="TypeGraphBasic_TMember", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass3", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentClass5: BinaryAssociation = BinaryAssociation(
    name="parentClass5",
    ends={
        Property(name="TClass", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="childClasses", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
childClasses7: BinaryAssociation = BinaryAssociation(
    name="childClasses7",
    ends={
        Property(name="TClass8", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="parentClass", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
signatures9: BinaryAssociation = BinaryAssociation(
    name="signatures9",
    ends={
        Property(name="TFieldSignature", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="field", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature10: BinaryAssociation = BinaryAssociation(
    name="signature10",
    ends={
        Property(name="TFieldSignature11", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
hiding13: BinaryAssociation = BinaryAssociation(
    name="hiding13",
    ends={
        Property(name="TFieldDefinition", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiddenBy", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy15: BinaryAssociation = BinaryAssociation(
    name="hiddenBy15",
    ends={
        Property(name="TFieldDefinition16", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiding", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
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
signatures25: BinaryAssociation = BinaryAssociation(
    name="signatures25",
    ends={
        Property(name="TMethodSignature", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
overloadedBy38: BinaryAssociation = BinaryAssociation(
    name="overloadedBy38",
    ends={
        Property(name="TMethodDefinition39", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overloading", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
returnType40: BinaryAssociation = BinaryAssociation(
    name="returnType40",
    ends={
        Property(name="TypeGraphBasic_TClass41", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodDefinition", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
method42: BinaryAssociation = BinaryAssociation(
    name="method42",
    ends={
        Property(name="TMethod", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures43", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(1, 1))
    }
)
paramList44: BinaryAssociation = BinaryAssociation(
    name="paramList44",
    ends={
        Property(name="TypeGraphBasic_TParameterList", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodSignature", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions45: BinaryAssociation = BinaryAssociation(
    name="definitions45",
    ends={
        Property(name="TMethodDefinition47", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature46", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
containedClasses48: BinaryAssociation = BinaryAssociation(
    name="containedClasses48",
    ends={
        Property(name="TClass49", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
subpackage51: BinaryAssociation = BinaryAssociation(
    name="subpackage51",
    ends={
        Property(name="TPackage52", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent54: BinaryAssociation = BinaryAssociation(
    name="parent54",
    ends={
        Property(name="TPackage55", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="subpackage", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
next57: BinaryAssociation = BinaryAssociation(
    name="next57",
    ends={
        Property(name="TParameter", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
previous59: BinaryAssociation = BinaryAssociation(
    name="previous59",
    ends={
        Property(name="TParameter60", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
tClass61: BinaryAssociation = BinaryAssociation(
    name="tClass61",
    ends={
        Property(name="TypeGraphBasic_TClass62", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameter", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1))
    }
)
entries63: BinaryAssociation = BinaryAssociation(
    name="entries63",
    ends={
        Property(name="TypeGraphBasic_TParameter65", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameterList64", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first66: BinaryAssociation = BinaryAssociation(
    name="first66",
    ends={
        Property(name="TypeGraphBasic_TParameter68", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameterList67", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
packages69: BinaryAssociation = BinaryAssociation(
    name="packages69",
    ends={
        Property(name="TypeGraphBasic_TPackage", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods70: BinaryAssociation = BinaryAssociation(
    name="methods70",
    ends={
        Property(name="TypeGraphBasic_TMethod", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph71", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields72: BinaryAssociation = BinaryAssociation(
    name="fields72",
    ends={
        Property(name="TypeGraphBasic_TField", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph73", type=TypeGraphBasic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes74: BinaryAssociation = BinaryAssociation(
    name="classes74",
    ends={
        Property(name="TypeGraphBasic_TClass76", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph75", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
    types={TypeGraphBasic_TClass, TypeGraphBasic_TPackage, TypeGraphBasic_TSignature, TypeGraphBasic_TMember, TypeGraphBasic_TField, TypeGraphBasic_TFieldSignature, TypeGraphBasic_TFieldDefinition, TMember, TSignature, TypeGraphBasic_TMethod, TypeGraphBasic_TMethodSignature, TypeGraphBasic_TMethodDefinition, TypeGraphBasic_TParameterList, TypeGraphBasic_TParameter, TypeGraphBasic_TypeGraph},
    associations={package0, signature1, defines2, parentClass5, childClasses7, signatures9, signature10, hiding13, hiddenBy15, definitions17, field19, type20, access23, signatures25, signature26, overriding30, overriddenBy32, overloading35, overloadedBy38, returnType40, method42, paramList44, definitions45, containedClasses48, subpackage51, parent54, next57, previous59, tClass61, entries63, first66, packages69, methods70, fields72, classes74},
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