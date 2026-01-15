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
basic_TAccess = Class(name="basic::TAccess")
TElementWithId = Class(name="TElementWithId")
basic_TMember = Class(name="basic::TMember", is_abstract=True)
basic_TAnnotatable = Class(name="basic::TAnnotatable", is_abstract=True)
basic_TAnnotation = Class(name="basic::TAnnotation")
basic_TAnnotationType = Class(name="basic::TAnnotationType")
basic_TClass = Class(name="basic::TClass")
TAbstractType = Class(name="TAbstractType")
basic_TInterface = Class(name="basic::TInterface")
basic_TElementWithId = Class(name="basic::TElementWithId", is_abstract=True)
basic_TField = Class(name="basic::TField")
basic_TFieldSignature = Class(name="basic::TFieldSignature")
basic_TypeGraph = Class(name="basic::TypeGraph")
basic_TFieldDefinition = Class(name="basic::TFieldDefinition")
TMember = Class(name="TMember")
TSignature = Class(name="TSignature")
basic_TAbstractType = Class(name="basic::TAbstractType", is_abstract=True)
TAnnotatable = Class(name="TAnnotatable")
basic_TPackage = Class(name="basic::TPackage")
basic_TMethod = Class(name="basic::TMethod")
basic_TMethodSignature = Class(name="basic::TMethodSignature")
basic_TMethodDefinition = Class(name="basic::TMethodDefinition")
basic_TParameterList = Class(name="basic::TParameterList")
basic_TParameter = Class(name="basic::TParameter")
basic_TSignature = Class(name="basic::TSignature", is_abstract=True)

# basic_TAccess class attributes and methods

# TElementWithId class attributes and methods

# basic_TMember class attributes and methods

# basic_TAnnotatable class attributes and methods

# basic_TAnnotation class attributes and methods

# basic_TAnnotationType class attributes and methods

# basic_TClass class attributes and methods

# TAbstractType class attributes and methods

# basic_TInterface class attributes and methods

# basic_TElementWithId class attributes and methods
basic_TElementWithId_ID: Property = Property(name="ID", type=IntegerType)
basic_TElementWithId.attributes={basic_TElementWithId_ID}

# basic_TField class attributes and methods
basic_TField_tName: Property = Property(name="tName", type=StringType)
basic_TField.attributes={basic_TField_tName}

# basic_TFieldSignature class attributes and methods

# basic_TypeGraph class attributes and methods
basic_TypeGraph_tName: Property = Property(name="tName", type=StringType)
basic_TypeGraph.attributes={basic_TypeGraph_tName}

# basic_TFieldDefinition class attributes and methods

# TMember class attributes and methods

# TSignature class attributes and methods

# basic_TAbstractType class attributes and methods
basic_TAbstractType_tName: Property = Property(name="tName", type=StringType)
basic_TAbstractType_tLib: Property = Property(name="tLib", type=BooleanType)
basic_TAbstractType.attributes={basic_TAbstractType_tName, basic_TAbstractType_tLib}

# TAnnotatable class attributes and methods

# basic_TPackage class attributes and methods
basic_TPackage_tName: Property = Property(name="tName", type=StringType)
basic_TPackage.attributes={basic_TPackage_tName}

# basic_TMethod class attributes and methods
basic_TMethod_tName: Property = Property(name="tName", type=StringType)
basic_TMethod.attributes={basic_TMethod_tName}

# basic_TMethodSignature class attributes and methods

# basic_TMethodDefinition class attributes and methods

# basic_TParameterList class attributes and methods

# basic_TParameter class attributes and methods

# basic_TSignature class attributes and methods

# Relationships
tTarget0: BinaryAssociation = BinaryAssociation(
    name="tTarget0",
    ends={
        Property(name="1", type=basic_TAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=basic_TMember, multiplicity=Multiplicity(1, 1))
    }
)
tSource2: BinaryAssociation = BinaryAssociation(
    name="tSource2",
    ends={
        Property(name="4", type=basic_TAccess, multiplicity=Multiplicity(1, 1)),
        Property(name="3", type=basic_TMember, multiplicity=Multiplicity(1, 1))
    }
)
tAnnotation5: BinaryAssociation = BinaryAssociation(
    name="tAnnotation5",
    ends={
        Property(name="7", type=basic_TAnnotatable, multiplicity=Multiplicity(1, 1)),
        Property(name="6", type=basic_TAnnotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tAnnotated8: BinaryAssociation = BinaryAssociation(
    name="tAnnotated8",
    ends={
        Property(name="10", type=basic_TAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="9", type=basic_TAnnotatable, multiplicity=Multiplicity(1, 1))
    }
)
type11: BinaryAssociation = BinaryAssociation(
    name="type11",
    ends={
        Property(name="13", type=basic_TAnnotation, multiplicity=Multiplicity(1, 1)),
        Property(name="12", type=basic_TAnnotationType, multiplicity=Multiplicity(1, 1))
    }
)
parentClass15: BinaryAssociation = BinaryAssociation(
    name="parentClass15",
    ends={
        Property(name="17", type=basic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="16", type=basic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
childClasses19: BinaryAssociation = BinaryAssociation(
    name="childClasses19",
    ends={
        Property(name="20", type=basic_TClass, multiplicity=Multiplicity(0, 9999)),
        Property(name="21", type=basic_TClass, multiplicity=Multiplicity(1, 1))
    }
)
tAccessing55: BinaryAssociation = BinaryAssociation(
    name="tAccessing55",
    ends={
        Property(name="57", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="56", type=basic_TAccess, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements22: BinaryAssociation = BinaryAssociation(
    name="implements22",
    ends={
        Property(name="24", type=basic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="23", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
signatures25: BinaryAssociation = BinaryAssociation(
    name="signatures25",
    ends={
        Property(name="27", type=basic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="26", type=basic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
pg28: BinaryAssociation = BinaryAssociation(
    name="pg28",
    ends={
        Property(name="30", type=basic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="29", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
signature31: BinaryAssociation = BinaryAssociation(
    name="signature31",
    ends={
        Property(name="33", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="32", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
hiding35: BinaryAssociation = BinaryAssociation(
    name="hiding35",
    ends={
        Property(name="37", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="36", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy39: BinaryAssociation = BinaryAssociation(
    name="hiddenBy39",
    ends={
        Property(name="41", type=basic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="40", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
definitions42: BinaryAssociation = BinaryAssociation(
    name="definitions42",
    ends={
        Property(name="44", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="43", type=basic_TFieldDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
field45: BinaryAssociation = BinaryAssociation(
    name="field45",
    ends={
        Property(name="47", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="46", type=basic_TField, multiplicity=Multiplicity(1, 1))
    }
)
type48: BinaryAssociation = BinaryAssociation(
    name="type48",
    ends={
        Property(name="basic_TAbstractType", type=basic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TFieldSignature", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
definedBy49: BinaryAssociation = BinaryAssociation(
    name="definedBy49",
    ends={
        Property(name="51", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="50", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
accessedBy52: BinaryAssociation = BinaryAssociation(
    name="accessedBy52",
    ends={
        Property(name="54", type=basic_TMember, multiplicity=Multiplicity(1, 1)),
        Property(name="53", type=basic_TAccess, multiplicity=Multiplicity(0, 9999))
    }
)
pg95: BinaryAssociation = BinaryAssociation(
    name="pg95",
    ends={
        Property(name="97", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="96", type=basic_TypeGraph, multiplicity=Multiplicity(0, 1))
    }
)
pg58: BinaryAssociation = BinaryAssociation(
    name="pg58",
    ends={
        Property(name="60", type=basic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="59", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
signatures61: BinaryAssociation = BinaryAssociation(
    name="signatures61",
    ends={
        Property(name="63", type=basic_TMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="62", type=basic_TMethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature64: BinaryAssociation = BinaryAssociation(
    name="signature64",
    ends={
        Property(name="66", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="65", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1))
    }
)
overriding68: BinaryAssociation = BinaryAssociation(
    name="overriding68",
    ends={
        Property(name="70", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="69", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 1))
    }
)
overriddenBy72: BinaryAssociation = BinaryAssociation(
    name="overriddenBy72",
    ends={
        Property(name="74", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="73", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloading76: BinaryAssociation = BinaryAssociation(
    name="overloading76",
    ends={
        Property(name="78", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="77", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
overloadedBy80: BinaryAssociation = BinaryAssociation(
    name="overloadedBy80",
    ends={
        Property(name="82", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="81", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
returnType83: BinaryAssociation = BinaryAssociation(
    name="returnType83",
    ends={
        Property(name="basic_TAbstractType84", type=basic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodDefinition", type=basic_TAbstractType, multiplicity=Multiplicity(0, 1))
    }
)
method85: BinaryAssociation = BinaryAssociation(
    name="method85",
    ends={
        Property(name="87", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="86", type=basic_TMethod, multiplicity=Multiplicity(1, 1))
    }
)
paramList88: BinaryAssociation = BinaryAssociation(
    name="paramList88",
    ends={
        Property(name="basic_TParameterList", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodSignature", type=basic_TParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
definitions89: BinaryAssociation = BinaryAssociation(
    name="definitions89",
    ends={
        Property(name="91", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="90", type=basic_TMethodDefinition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType92: BinaryAssociation = BinaryAssociation(
    name="returnType92",
    ends={
        Property(name="basic_TAbstractType94", type=basic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TMethodSignature93", type=basic_TAbstractType, multiplicity=Multiplicity(0, 1))
    }
)
methods133: BinaryAssociation = BinaryAssociation(
    name="methods133",
    ends={
        Property(name="135", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="134", type=basic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subpackage99: BinaryAssociation = BinaryAssociation(
    name="subpackage99",
    ends={
        Property(name="101", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="100", type=basic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent103: BinaryAssociation = BinaryAssociation(
    name="parent103",
    ends={
        Property(name="105", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="104", type=basic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
classes106: BinaryAssociation = BinaryAssociation(
    name="classes106",
    ends={
        Property(name="basic_TClass", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces107: BinaryAssociation = BinaryAssociation(
    name="interfaces107",
    ends={
        Property(name="basic_TInterface", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage108", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTypes109: BinaryAssociation = BinaryAssociation(
    name="ownedTypes109",
    ends={
        Property(name="111", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="110", type=basic_TAbstractType, multiplicity=Multiplicity(0, 9999))
    }
)
typeGraph112: BinaryAssociation = BinaryAssociation(
    name="typeGraph112",
    ends={
        Property(name="basic_TypeGraph", type=basic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TPackage113", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
next115: BinaryAssociation = BinaryAssociation(
    name="next115",
    ends={
        Property(name="117", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="116", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
previous119: BinaryAssociation = BinaryAssociation(
    name="previous119",
    ends={
        Property(name="121", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="120", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
type122: BinaryAssociation = BinaryAssociation(
    name="type122",
    ends={
        Property(name="basic_TAbstractType123", type=basic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameter", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1))
    }
)
entries124: BinaryAssociation = BinaryAssociation(
    name="entries124",
    ends={
        Property(name="basic_TParameter126", type=basic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameterList125", type=basic_TParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first127: BinaryAssociation = BinaryAssociation(
    name="first127",
    ends={
        Property(name="basic_TParameter129", type=basic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TParameterList128", type=basic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
packages130: BinaryAssociation = BinaryAssociation(
    name="packages130",
    ends={
        Property(name="132", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="131", type=basic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields136: BinaryAssociation = BinaryAssociation(
    name="fields136",
    ends={
        Property(name="138", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="137", type=basic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes139: BinaryAssociation = BinaryAssociation(
    name="classes139",
    ends={
        Property(name="basic_TClass141", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph140", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
interfaces142: BinaryAssociation = BinaryAssociation(
    name="interfaces142",
    ends={
        Property(name="basic_TInterface144", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph143", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
ownedTypes145: BinaryAssociation = BinaryAssociation(
    name="ownedTypes145",
    ends={
        Property(name="147", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="146", type=basic_TAbstractType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tAnnotationTypes148: BinaryAssociation = BinaryAssociation(
    name="tAnnotationTypes148",
    ends={
        Property(name="basic_TAnnotationType", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TypeGraph149", type=basic_TAnnotationType, multiplicity=Multiplicity(0, 9999))
    }
)
implementedBy150: BinaryAssociation = BinaryAssociation(
    name="implementedBy150",
    ends={
        Property(name="152", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="151", type=basic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
parentInterfaces154: BinaryAssociation = BinaryAssociation(
    name="parentInterfaces154",
    ends={
        Property(name="156", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="155", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
childInterfaces158: BinaryAssociation = BinaryAssociation(
    name="childInterfaces158",
    ends={
        Property(name="160", type=basic_TInterface, multiplicity=Multiplicity(1, 1)),
        Property(name="159", type=basic_TInterface, multiplicity=Multiplicity(0, 9999))
    }
)
pg161: BinaryAssociation = BinaryAssociation(
    name="pg161",
    ends={
        Property(name="163", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="162", type=basic_TypeGraph, multiplicity=Multiplicity(1, 1))
    }
)
package164: BinaryAssociation = BinaryAssociation(
    name="package164",
    ends={
        Property(name="166", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="165", type=basic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
signature167: BinaryAssociation = BinaryAssociation(
    name="signature167",
    ends={
        Property(name="basic_TSignature", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="basic_TAbstractType168", type=basic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
defines169: BinaryAssociation = BinaryAssociation(
    name="defines169",
    ends={
        Property(name="171", type=basic_TAbstractType, multiplicity=Multiplicity(1, 1)),
        Property(name="170", type=basic_TMember, multiplicity=Multiplicity(0, 9999))
    }
)
annotations172: BinaryAssociation = BinaryAssociation(
    name="annotations172",
    ends={
        Property(name="174", type=basic_TAnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="173", type=basic_TAnnotation, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_basic_TAccess_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAccess)
gen_basic_TAnnotation_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAnnotation)
gen_basic_TClass_TAbstractType = Generalization(general=TAbstractType, specific=basic_TClass)
gen_basic_TField_TElementWithId = Generalization(general=TElementWithId, specific=basic_TField)
gen_basic_TFieldDefinition_TMember = Generalization(general=TMember, specific=basic_TFieldDefinition)
gen_basic_TFieldSignature_TSignature = Generalization(general=TSignature, specific=basic_TFieldSignature)
gen_basic_TMember_TElementWithId = Generalization(general=TElementWithId, specific=basic_TMember)
gen_basic_TMember_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TMember)
gen_basic_TPackage_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TPackage)
gen_basic_TPackage_TElementWithId = Generalization(general=TElementWithId, specific=basic_TPackage)
gen_basic_TMethod_TElementWithId = Generalization(general=TElementWithId, specific=basic_TMethod)
gen_basic_TMethodDefinition_TMember = Generalization(general=TMember, specific=basic_TMethodDefinition)
gen_basic_TMethodSignature_TSignature = Generalization(general=TSignature, specific=basic_TMethodSignature)
gen_basic_TParameter_TElementWithId = Generalization(general=TElementWithId, specific=basic_TParameter)
gen_basic_TParameterList_TElementWithId = Generalization(general=TElementWithId, specific=basic_TParameterList)
gen_basic_TSignature_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TSignature)
gen_basic_TSignature_TElementWithId = Generalization(general=TElementWithId, specific=basic_TSignature)
gen_basic_TypeGraph_TElementWithId = Generalization(general=TElementWithId, specific=basic_TypeGraph)
gen_basic_TInterface_TAbstractType = Generalization(general=TAbstractType, specific=basic_TInterface)
gen_basic_TAbstractType_TElementWithId = Generalization(general=TElementWithId, specific=basic_TAbstractType)
gen_basic_TAbstractType_TAnnotatable = Generalization(general=TAnnotatable, specific=basic_TAbstractType)
gen_basic_TAnnotationType_TAbstractType = Generalization(general=TAbstractType, specific=basic_TAnnotationType)

# Domain Model
domain_model = DomainModel(
    name="basic",
    types={basic_TAccess, TElementWithId, basic_TMember, basic_TAnnotatable, basic_TAnnotation, basic_TAnnotationType, basic_TClass, TAbstractType, basic_TInterface, basic_TElementWithId, basic_TField, basic_TFieldSignature, basic_TypeGraph, basic_TFieldDefinition, TMember, TSignature, basic_TAbstractType, TAnnotatable, basic_TPackage, basic_TMethod, basic_TMethodSignature, basic_TMethodDefinition, basic_TParameterList, basic_TParameter, basic_TSignature},
    associations={tTarget0, tSource2, tAnnotation5, tAnnotated8, type11, parentClass15, childClasses19, tAccessing55, implements22, signatures25, pg28, signature31, hiding35, hiddenBy39, definitions42, field45, type48, definedBy49, accessedBy52, pg95, pg58, signatures61, signature64, overriding68, overriddenBy72, overloading76, overloadedBy80, returnType83, method85, paramList88, definitions89, returnType92, methods133, subpackage99, parent103, classes106, interfaces107, ownedTypes109, typeGraph112, next115, previous119, type122, entries124, first127, packages130, fields136, classes139, interfaces142, ownedTypes145, tAnnotationTypes148, implementedBy150, parentInterfaces154, childInterfaces158, pg161, package164, signature167, defines169, annotations172},
    generalizations={gen_basic_TAccess_TElementWithId, gen_basic_TAnnotation_TElementWithId, gen_basic_TClass_TAbstractType, gen_basic_TField_TElementWithId, gen_basic_TFieldDefinition_TMember, gen_basic_TFieldSignature_TSignature, gen_basic_TMember_TElementWithId, gen_basic_TMember_TAnnotatable, gen_basic_TPackage_TAnnotatable, gen_basic_TPackage_TElementWithId, gen_basic_TMethod_TElementWithId, gen_basic_TMethodDefinition_TMember, gen_basic_TMethodSignature_TSignature, gen_basic_TParameter_TElementWithId, gen_basic_TParameterList_TElementWithId, gen_basic_TSignature_TAnnotatable, gen_basic_TSignature_TElementWithId, gen_basic_TypeGraph_TElementWithId, gen_basic_TInterface_TAbstractType, gen_basic_TAbstractType_TElementWithId, gen_basic_TAbstractType_TAnnotatable, gen_basic_TAnnotationType_TAbstractType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)