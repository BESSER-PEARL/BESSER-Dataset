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
TSignature = Class(name="TSignature")
TypeGraphBasic_TClass = Class(name="TypeGraphBasic::TClass")
TypeGraphBasic_TPackage = Class(name="TypeGraphBasic::TPackage")
TypeGraphBasic_TSignature = Class(name="TypeGraphBasic::TSignature", is_abstract=True)
TypeGraphBasic_TMember = Class(name="TypeGraphBasic::TMember", is_abstract=True)
TypeGraphBasic_TField = Class(name="TypeGraphBasic::TField")
TypeGraphBasic_TFieldSignature = Class(name="TypeGraphBasic::TFieldSignature")
TypeGraphBasic_TFieldDefinition = Class(name="TypeGraphBasic::TFieldDefinition")
TMember = Class(name="TMember")
TypeGraphBasic_TMethod = Class(name="TypeGraphBasic::TMethod")
TypeGraphBasic_TMethodSignature = Class(name="TypeGraphBasic::TMethodSignature")
TypeGraphBasic_TMethodDefinition = Class(name="TypeGraphBasic::TMethodDefinition")
TypeGraphBasic_TParameterList = Class(name="TypeGraphBasic::TParameterList")
TypeGraphBasic_TParameter = Class(name="TypeGraphBasic::TParameter")
TypeGraphBasic_TypeGraph = Class(name="TypeGraphBasic::TypeGraph")

# TSignature class attributes and methods

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
hiding20: BinaryAssociation = BinaryAssociation(
    name="hiding20",
    ends={
        Property(name="22", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="21", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 1))
    }
)
hiddenBy24: BinaryAssociation = BinaryAssociation(
    name="hiddenBy24",
    ends={
        Property(name="26", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="25", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
definitions27: BinaryAssociation = BinaryAssociation(
    name="definitions27",
    ends={
        Property(name="29", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="28", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="1", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1))
    }
)
signature2: BinaryAssociation = BinaryAssociation(
    name="signature2",
    ends={
        Property(name="TypeGraphBasic_TSignature", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass", type=TypeGraphBasic_TSignature, multiplicity=Multiplicity(0, 9999))
    }
)
defines3: BinaryAssociation = BinaryAssociation(
    name="defines3",
    ends={
        Property(name="TypeGraphBasic_TMember", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TClass4", type=TypeGraphBasic_TMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentClass6: BinaryAssociation = BinaryAssociation(
    name="parentClass6",
    ends={
        Property(name="8", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="7", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 1))
    }
)
childClasses10: BinaryAssociation = BinaryAssociation(
    name="childClasses10",
    ends={
        Property(name="12", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1)),
        Property(name="11", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
signatures13: BinaryAssociation = BinaryAssociation(
    name="signatures13",
    ends={
        Property(name="15", type=TypeGraphBasic_TField, multiplicity=Multiplicity(1, 1)),
        Property(name="14", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
signature16: BinaryAssociation = BinaryAssociation(
    name="signature16",
    ends={
        Property(name="18", type=TypeGraphBasic_TFieldDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="17", type=TypeGraphBasic_TFieldSignature, multiplicity=Multiplicity(1, 1))
    }
)
definitions66: BinaryAssociation = BinaryAssociation(
    name="definitions66",
    ends={
        Property(name="68", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="67", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
    }
)
containedClasses69: BinaryAssociation = BinaryAssociation(
    name="containedClasses69",
    ends={
        Property(name="71", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="70", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999))
    }
)
subpackage73: BinaryAssociation = BinaryAssociation(
    name="subpackage73",
    ends={
        Property(name="75", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="74", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
overriddenBy49: BinaryAssociation = BinaryAssociation(
    name="overriddenBy49",
    ends={
        Property(name="51", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="50", type=TypeGraphBasic_TMethodDefinition, multiplicity=Multiplicity(0, 9999))
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
paramList65: BinaryAssociation = BinaryAssociation(
    name="paramList65",
    ends={
        Property(name="TypeGraphBasic_TParameterList", type=TypeGraphBasic_TMethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TMethodSignature", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent77: BinaryAssociation = BinaryAssociation(
    name="parent77",
    ends={
        Property(name="79", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(1, 1)),
        Property(name="78", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 1))
    }
)
next81: BinaryAssociation = BinaryAssociation(
    name="next81",
    ends={
        Property(name="83", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="82", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
previous85: BinaryAssociation = BinaryAssociation(
    name="previous85",
    ends={
        Property(name="87", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="86", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
tClass88: BinaryAssociation = BinaryAssociation(
    name="tClass88",
    ends={
        Property(name="TypeGraphBasic_TClass89", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameter", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(1, 1))
    }
)
entries90: BinaryAssociation = BinaryAssociation(
    name="entries90",
    ends={
        Property(name="TypeGraphBasic_TParameter92", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameterList91", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
first93: BinaryAssociation = BinaryAssociation(
    name="first93",
    ends={
        Property(name="TypeGraphBasic_TParameter95", type=TypeGraphBasic_TParameterList, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TParameterList94", type=TypeGraphBasic_TParameter, multiplicity=Multiplicity(0, 1))
    }
)
packages96: BinaryAssociation = BinaryAssociation(
    name="packages96",
    ends={
        Property(name="TypeGraphBasic_TPackage", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph", type=TypeGraphBasic_TPackage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods97: BinaryAssociation = BinaryAssociation(
    name="methods97",
    ends={
        Property(name="TypeGraphBasic_TMethod", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph98", type=TypeGraphBasic_TMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields99: BinaryAssociation = BinaryAssociation(
    name="fields99",
    ends={
        Property(name="TypeGraphBasic_TField", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph100", type=TypeGraphBasic_TField, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes101: BinaryAssociation = BinaryAssociation(
    name="classes101",
    ends={
        Property(name="TypeGraphBasic_TClass103", type=TypeGraphBasic_TypeGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeGraphBasic_TypeGraph102", type=TypeGraphBasic_TClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
    types={TSignature, TypeGraphBasic_TClass, TypeGraphBasic_TPackage, TypeGraphBasic_TSignature, TypeGraphBasic_TMember, TypeGraphBasic_TField, TypeGraphBasic_TFieldSignature, TypeGraphBasic_TFieldDefinition, TMember, TypeGraphBasic_TMethod, TypeGraphBasic_TMethodSignature, TypeGraphBasic_TMethodDefinition, TypeGraphBasic_TParameterList, TypeGraphBasic_TParameter, TypeGraphBasic_TypeGraph},
    associations={hiding20, hiddenBy24, definitions27, package0, signature2, defines3, parentClass6, childClasses10, signatures13, signature16, definitions66, containedClasses69, subpackage73, field30, type33, access36, signatures38, signature41, overriding45, overriddenBy49, overloading53, overloadedBy57, returnType60, method62, paramList65, parent77, next81, previous85, tClass88, entries90, first93, packages96, methods97, fields99, classes101},
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