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
basic_TElementWithId = Class(name="basic_TElementWithId", is_abstract=True)
basic_TField = Class(name="basic_TField")
basic_TFieldSignature = Class(name="basic_TFieldSignature")
basic_TAccess = Class(name="basic_TAccess")
TElementWithId = Class(name="TElementWithId")
basic_TMember = Class(name="basic_TMember", is_abstract=True)
basic_TAnnotatable = Class(name="basic_TAnnotatable", is_abstract=True)
basic_TAnnotation = Class(name="basic_TAnnotation")
basic_TAnnotationType = Class(name="basic_TAnnotationType")
basic_TClass = Class(name="basic_TClass")
TAbstractType = Class(name="TAbstractType")
basic_TInterface = Class(name="basic_TInterface")
basic_TMethodSignature = Class(name="basic_TMethodSignature")
basic_TMethodDefinition = Class(name="basic_TMethodDefinition")
basic_TypeGraph = Class(name="basic_TypeGraph")
basic_TFieldDefinition = Class(name="basic_TFieldDefinition")
TMember = Class(name="TMember")
TSignature = Class(name="TSignature")
basic_TAbstractType = Class(name="basic_TAbstractType", is_abstract=True)
TAnnotatable = Class(name="TAnnotatable")
basic_TMethod = Class(name="basic_TMethod")
basic_TParameterList = Class(name="basic_TParameterList")
basic_TPackage = Class(name="basic_TPackage")
basic_TParameter = Class(name="basic_TParameter")
basic_TSignature = Class(name="basic_TSignature", is_abstract=True)

# basic_TElementWithId class attributes and methods
basic_TElementWithId_ID: Property = Property(name="ID", type=IntegerType)
basic_TElementWithId.attributes={basic_TElementWithId_ID}

# basic_TField class attributes and methods
basic_TField_tName: Property = Property(name="tName", type=StringType)
basic_TField.attributes={basic_TField_tName}

# basic_TFieldSignature class attributes and methods

# basic_TAccess class attributes and methods

# TElementWithId class attributes and methods

# basic_TMember class attributes and methods

# basic_TAnnotatable class attributes and methods

# basic_TAnnotation class attributes and methods

# basic_TAnnotationType class attributes and methods

# basic_TClass class attributes and methods

# TAbstractType class attributes and methods

# basic_TInterface class attributes and methods

# basic_TMethodSignature class attributes and methods

# basic_TMethodDefinition class attributes and methods

# basic_TypeGraph class attributes and methods
basic_TypeGraph_tName: Property = Property(name="tName", type=StringType)
basic_TypeGraph.attributes={basic_TypeGraph_tName}

# basic_TFieldDefinition class attributes and methods

# TMember class attributes and methods

# TSignature class attributes and methods

# basic_TAbstractType class attributes and methods
basic_TAbstractType_tLib: Property = Property(name="tLib", type=BooleanType)
basic_TAbstractType_tName: Property = Property(name="tName", type=StringType)
basic_TAbstractType.attributes={basic_TAbstractType_tName, basic_TAbstractType_tLib}

# TAnnotatable class attributes and methods

# basic_TMethod class attributes and methods
basic_TMethod_tName: Property = Property(name="tName", type=StringType)
basic_TMethod.attributes={basic_TMethod_tName}

# basic_TParameterList class attributes and methods

# basic_TPackage class attributes and methods
basic_TPackage_tName: Property = Property(name="tName", type=StringType)
basic_TPackage.attributes={basic_TPackage_tName}

# basic_TParameter class attributes and methods

# basic_TSignature class attributes and methods

# Relationships
signatures12: BinaryAssociation = BinaryAssociation(
    name="signatures12",
    ends={
        Property(name="TFieldSignature", type=basic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="field", type=basic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tTarget0: BinaryAssociation = BinaryAssociation(
    name="tTarget0",
    ends={
        Property(name="TMember", type=basic_TAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="accessedBy", type=basic_TMember, multiplicity=Multiplicity(1, 1))
    }
)
tSource1: BinaryAssociation = BinaryAssociation(
    name="tSource1",
    ends={
        Property(name="TMember2", type=basic_TAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="tAccessing", type=basic_TMember, multiplicity=Multiplicity(1, 1))
    }
)
tAnnotation3: BinaryAssociation = BinaryAssociation(
    name="tAnnotation3",
    ends={
        Property(name="TAnnotation", type=basic_TAnnotatable, multiplicity=Multiplicity(1, 1)),
        Property(name="tAnnotated", type=basic_TAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tAnnotated4: BinaryAssociation = BinaryAssociation(
    name="tAnnotated4",
    ends={
        Property(name="TAnnotatable", type=basic_TAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="tAnnotation", type=basic_TAnnotatable, multiplicity=Multiplicity(1, 1))
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="TAnnotationType", type=basic_TAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="annotations", type=basic_TAnnotationType, multiplicity=Multiplicity(1, 1))
    }
)
parentClass7: BinaryAssociation = BinaryAssociation(
    name="parentClass7",
    ends={
        Property(name="TClass", type=basic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="childClasses", type=basic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
childClasses9: BinaryAssociation = BinaryAssociation(
    name="childClasses9",
    ends={
        Property(name="TClass10", type=basic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="parentClass", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
implements11: BinaryAssociation = BinaryAssociation(
    name="implements11",
    ends={
        Property(name="TInterface", type=basic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="implementedBy", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
pg29: BinaryAssociation = BinaryAssociation(
    name="pg29",
    ends={
        Property(name="TypeGraph30", type=basic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
signatures31: BinaryAssociation = BinaryAssociation(
    name="signatures31",
    ends={
        Property(name="TMethodSignature", type=basic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="method", type=basic_TMethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pg13: BinaryAssociation = BinaryAssociation(
    name="pg13",
    ends={
        Property(name="TypeGraph", type=basic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
signature14: BinaryAssociation = BinaryAssociation(
    name="signature14",
    ends={
        Property(name="TFieldSignature15", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
hiding17: BinaryAssociation = BinaryAssociation(
    name="hiding17",
    ends={
        Property(name="TFieldDefinition", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiddenBy", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy19: BinaryAssociation = BinaryAssociation(
    name="hiddenBy19",
    ends={
        Property(name="TFieldDefinition20", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="hiding", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
definitions21: BinaryAssociation = BinaryAssociation(
    name="definitions21",
    ends={
        Property(name="TFieldDefinition22", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field23: BinaryAssociation = BinaryAssociation(
    name="field23",
    ends={
        Property(name="TField", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures", type=basic_TField, multiplicity=Multiplicity(1, 1))
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="basic_TAbstractType", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TFieldSignature", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
definedBy25: BinaryAssociation = BinaryAssociation(
    name="definedBy25",
    ends={
        Property(name="TAbstractType", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="defines", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
accessedBy26: BinaryAssociation = BinaryAssociation(
    name="accessedBy26",
    ends={
        Property(name="TAccess", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="tTarget", type=basic_TAccess, multiplicity=Multiplicity(0, 9999))
    }
)
tAccessing27: BinaryAssociation = BinaryAssociation(
    name="tAccessing27",
    ends={
        Property(name="TAccess28", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="tSource", type=basic_TAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
interfaces65: BinaryAssociation = BinaryAssociation(
    name="interfaces65",
    ends={
        Property(name="basic_TInterface", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage66", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTypes67: BinaryAssociation = BinaryAssociation(
    name="ownedTypes67",
    ends={
        Property(name="TAbstractType68", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="package", type=basic_TAbstractType, multiplicity=Multiplicity(0, 9999))
    }
)
typeGraph69: BinaryAssociation = BinaryAssociation(
    name="typeGraph69",
    ends={
        Property(name="basic_TypeGraph", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage70", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
signature32: BinaryAssociation = BinaryAssociation(
    name="signature32",
    ends={
        Property(name="TMethodSignature34", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="definitions33", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1))
    }
)
overriding36: BinaryAssociation = BinaryAssociation(
    name="overriding36",
    ends={
        Property(name="TMethodDefinition", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overriddenBy", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 1))
    }
)
overriddenBy38: BinaryAssociation = BinaryAssociation(
    name="overriddenBy38",
    ends={
        Property(name="TMethodDefinition39", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overriding", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloading41: BinaryAssociation = BinaryAssociation(
    name="overloading41",
    ends={
        Property(name="TMethodDefinition42", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overloadedBy", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloadedBy44: BinaryAssociation = BinaryAssociation(
    name="overloadedBy44",
    ends={
        Property(name="TMethodDefinition45", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="overloading", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
returnType46: BinaryAssociation = BinaryAssociation(
    name="returnType46",
    ends={
        Property(name="basic_TAbstractType47", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodDefinition", type=basic_TAbstractType, multiplicity=Multiplicity(0, 1))
    }
)
method48: BinaryAssociation = BinaryAssociation(
    name="method48",
    ends={
        Property(name="TMethod", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signatures49", type=basic_TMethod, multiplicity=Multiplicity(1, 1))
    }
)
paramList50: BinaryAssociation = BinaryAssociation(
    name="paramList50",
    ends={
        Property(name="basic_TParameterList", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodSignature", type=basic_TParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions51: BinaryAssociation = BinaryAssociation(
    name="definitions51",
    ends={
        Property(name="TMethodDefinition53", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="signature52", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType54: BinaryAssociation = BinaryAssociation(
    name="returnType54",
    ends={
        Property(name="basic_TAbstractType56", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodSignature55", type=basic_TAbstractType, multiplicity=Multiplicity(0, 1))
    }
)
pg57: BinaryAssociation = BinaryAssociation(
    name="pg57",
    ends={
        Property(name="TypeGraph58", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="packages", type=basic_TypeGraph, multiplicity=Multiplicity(0, 1))
    }
)
subpackage60: BinaryAssociation = BinaryAssociation(
    name="subpackage60",
    ends={
        Property(name="TPackage", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=basic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent62: BinaryAssociation = BinaryAssociation(
    name="parent62",
    ends={
        Property(name="TPackage63", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="subpackage", type=basic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
classes64: BinaryAssociation = BinaryAssociation(
    name="classes64",
    ends={
        Property(name="basic_TClass", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
next72: BinaryAssociation = BinaryAssociation(
    name="next72",
    ends={
        Property(name="TParameter", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
previous74: BinaryAssociation = BinaryAssociation(
    name="previous74",
    ends={
        Property(name="TParameter75", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
type76: BinaryAssociation = BinaryAssociation(
    name="type76",
    ends={
        Property(name="basic_TAbstractType77", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameter", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
entries78: BinaryAssociation = BinaryAssociation(
    name="entries78",
    ends={
        Property(name="basic_TParameter80", type=basic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameterList79", type=basic_TParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first81: BinaryAssociation = BinaryAssociation(
    name="first81",
    ends={
        Property(name="basic_TParameter83", type=basic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameterList82", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
packages84: BinaryAssociation = BinaryAssociation(
    name="packages84",
    ends={
        Property(name="TPackage85", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pg", type=basic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods86: BinaryAssociation = BinaryAssociation(
    name="methods86",
    ends={
        Property(name="TMethod88", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pg87", type=basic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields89: BinaryAssociation = BinaryAssociation(
    name="fields89",
    ends={
        Property(name="TField91", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pg90", type=basic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes92: BinaryAssociation = BinaryAssociation(
    name="classes92",
    ends={
        Property(name="basic_TClass94", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph93", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces95: BinaryAssociation = BinaryAssociation(
    name="interfaces95",
    ends={
        Property(name="basic_TInterface97", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph96", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTypes98: BinaryAssociation = BinaryAssociation(
    name="ownedTypes98",
    ends={
        Property(name="TAbstractType100", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="pg99", type=basic_TAbstractType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tAnnotationTypes101: BinaryAssociation = BinaryAssociation(
    name="tAnnotationTypes101",
    ends={
        Property(name="basic_TAnnotationType", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph102", type=basic_TAnnotationType, multiplicity=Multiplicity(0, 9999))
    }
)
implementedBy103: BinaryAssociation = BinaryAssociation(
    name="implementedBy103",
    ends={
        Property(name="TClass104", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="implements", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
parentInterfaces106: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces106",
    ends={
        Property(name="TInterface107", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="childInterfaces", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
childInterfaces109: BinaryAssociation = BinaryAssociation(
    name="childInterfaces109",
    ends={
        Property(name="TInterface110", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="parentInterfaces", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
pg111: BinaryAssociation = BinaryAssociation(
    name="pg111",
    ends={
        Property(name="TypeGraph112", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTypes", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
package113: BinaryAssociation = BinaryAssociation(
    name="package113",
    ends={
        Property(name="TPackage115", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTypes114", type=basic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
signature116: BinaryAssociation = BinaryAssociation(
    name="signature116",
    ends={
        Property(name="basic_TSignature", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TAbstractType117", type=basic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
defines118: BinaryAssociation = BinaryAssociation(
    name="defines118",
    ends={
        Property(name="TMember119", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="definedBy", type=basic_TMember, multiplicity=Multiplicity(0, 9999))
    }
)
annotations120: BinaryAssociation = BinaryAssociation(
    name="annotations120",
    ends={
        Property(name="TAnnotation121", type=basic_TAnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=basic_TAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_basic_TField_TElementWithId = Generalization(general=TElementWithId, specific=basic_TField)
gen_basic_TAccess_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAccess)
gen_basic_TAnnotation_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAnnotation)
gen_basic_TClass_TAbstractType = Generalization(general=TAbstractType, specific=basic_TClass)
gen_basic_TMethodDefinition_TMember = Generalization(general=TMember, specific=basic_TMethodDefinition)
gen_basic_TFieldDefinition_TMember = Generalization(general=TMember, specific=basic_TFieldDefinition)
gen_basic_TFieldSignature_TSignature = Generalization(general=TSignature, specific=basic_TFieldSignature)
gen_basic_TMember_TElementWithId = Generalization(general=TElementWithId, specific=basic_TMember)
gen_basic_TMember_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TMember)
gen_basic_TMethod_TElementWithId = Generalization(general=TElementWithId, specific=basic_TMethod)
gen_basic_TMethodSignature_TSignature = Generalization(general=TSignature, specific=basic_TMethodSignature)
gen_basic_TPackage_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TPackage)
gen_basic_TPackage_TElementWithId = Generalization(general=TElementWithId, specific=basic_TPackage)
gen_basic_TInterface_TAbstractType = Generalization(general=TAbstractType, specific=basic_TInterface)
gen_basic_TParameter_TElementWithId = Generalization(general=TElementWithId, specific=basic_TParameter)
gen_basic_TParameterList_TElementWithId = Generalization(general=TElementWithId, specific=basic_TParameterList)
gen_basic_TSignature_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TSignature)
gen_basic_TSignature_TElementWithId = Generalization(general=TElementWithId, specific=basic_TSignature)
gen_basic_TypeGraph_TElementWithId = Generalization(general=TElementWithId, specific=basic_TypeGraph)
gen_basic_TAbstractType_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAbstractType)
gen_basic_TAbstractType_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TAbstractType)
gen_basic_TAnnotationType_TAbstractType = Generalization(general=TAbstractType, specific=basic_TAnnotationType)

# Domain Model
domain_model = DomainModel(
    name="basic",
    types={basic_TElementWithId, basic_TField, basic_TFieldSignature, basic_TAccess, TElementWithId, basic_TMember, basic_TAnnotatable, basic_TAnnotation, basic_TAnnotationType, basic_TClass, TAbstractType, basic_TInterface, basic_TMethodSignature, basic_TMethodDefinition, basic_TypeGraph, basic_TFieldDefinition, TMember, TSignature, basic_TAbstractType, TAnnotatable, basic_TMethod, basic_TParameterList, basic_TPackage, basic_TParameter, basic_TSignature},
    associations={signatures12, tTarget0, tSource1, tAnnotation3, tAnnotated4, type5, parentClass7, childClasses9, implements11, pg29, signatures31, pg13, signature14, hiding17, hiddenBy19, definitions21, field23, type24, definedBy25, accessedBy26, tAccessing27, interfaces65, ownedTypes67, typeGraph69, signature32, overriding36, overriddenBy38, overloading41, overloadedBy44, returnType46, method48, paramList50, definitions51, returnType54, pg57, subpackage60, parent62, classes64, next72, previous74, type76, entries78, first81, packages84, methods86, fields89, classes92, interfaces95, ownedTypes98, tAnnotationTypes101, implementedBy103, parentInterfaces106, childInterfaces109, pg111, package113, signature116, defines118, annotations120},
    generalizations={gen_basic_TField_TElementWithId, gen_basic_TAccess_TElementWithId, gen_basic_TAnnotation_TElementWithId, gen_basic_TClass_TAbstractType, gen_basic_TMethodDefinition_TMember, gen_basic_TFieldDefinition_TMember, gen_basic_TFieldSignature_TSignature, gen_basic_TMember_TElementWithId, gen_basic_TMember_TAnnotatable, gen_basic_TMethod_TElementWithId, gen_basic_TMethodSignature_TSignature, gen_basic_TPackage_TAnnotatable, gen_basic_TPackage_TElementWithId, gen_basic_TInterface_TAbstractType, gen_basic_TParameter_TElementWithId, gen_basic_TParameterList_TElementWithId, gen_basic_TSignature_TAnnotatable, gen_basic_TSignature_TElementWithId, gen_basic_TypeGraph_TElementWithId, gen_basic_TAbstractType_TElementWithId, gen_basic_TAbstractType_TAnnotatable, gen_basic_TAnnotationType_TAbstractType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)