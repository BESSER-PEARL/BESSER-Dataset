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
Java_ObjectType = Class(name="Java::ObjectType", is_abstract=True)
Package = Class(name="Package")
Java_PrimitiveType = Class(name="Java::PrimitiveType")
Java_Class = Class(name="Java::Class")
Java_Package = Class(name="Java::Package")
ObjectType = Class(name="ObjectType")
Java_Type = Class(name="Java::Type", is_abstract=True)
Java_VoidType = Class(name="Java::VoidType")
Type = Class(name="Type")
Java_MethodSignature = Class(name="Java::MethodSignature")
Interface = Class(name="Interface")
Class_ = Class(name="Class")
Field = Class(name="Field")
Method_ = Class(name="Method")
Java_Interface = Class(name="Java::Interface")
MethodSignature = Class(name="MethodSignature")
Java_Statement = Class(name="Java::Statement", is_abstract=True)
Java_MethodCall = Class(name="Java::MethodCall")
Java_VariableDeclaration = Class(name="Java::VariableDeclaration")
Java_Assignment = Class(name="Java::Assignment")
Parameter_ = Class(name="Parameter")
Java_Method = Class(name="Java::Method")
Statement = Class(name="Statement")
Annotation = Class(name="Annotation")
Java_Parameter = Class(name="Java::Parameter")
Java_Field = Class(name="Java::Field")
Java_Return = Class(name="Java::Return")
Java_Annotation = Class(name="Java::Annotation")

# Java_ObjectType class attributes and methods

# Package class attributes and methods

# Java_PrimitiveType class attributes and methods

# Java_Class class attributes and methods
Java_Class_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_Class_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_Class.attributes={Java_Class_isStatic, Java_Class_isPublic}

# Java_Package class attributes and methods
Java_Package_name: Property = Property(name="name", type=StringType)
Java_Package.attributes={Java_Package_name}

# ObjectType class attributes and methods

# Java_Type class attributes and methods
Java_Type_name: Property = Property(name="name", type=StringType)
Java_Type.attributes={Java_Type_name}

# Java_VoidType class attributes and methods

# Type class attributes and methods

# Java_MethodSignature class attributes and methods
Java_MethodSignature_name: Property = Property(name="name", type=StringType)
Java_MethodSignature_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_MethodSignature_isProtected: Property = Property(name="isProtected", type=BooleanType)
Java_MethodSignature_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
Java_MethodSignature_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_MethodSignature.attributes={Java_MethodSignature_isPrivate, Java_MethodSignature_isProtected, Java_MethodSignature_isPublic, Java_MethodSignature_isStatic, Java_MethodSignature_name}

# Interface class attributes and methods

# Class class attributes and methods

# Field class attributes and methods

# Method class attributes and methods

# Java_Interface class attributes and methods

# MethodSignature class attributes and methods

# Java_Statement class attributes and methods

# Java_MethodCall class attributes and methods
Java_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
Java_MethodCall_variableName: Property = Property(name="variableName", type=StringType)
Java_MethodCall.attributes={Java_MethodCall_methodName, Java_MethodCall_variableName}

# Java_VariableDeclaration class attributes and methods
Java_VariableDeclaration_variableName: Property = Property(name="variableName", type=StringType)
Java_VariableDeclaration.attributes={Java_VariableDeclaration_variableName}

# Java_Assignment class attributes and methods
Java_Assignment_objectId: Property = Property(name="objectId", type=StringType)
Java_Assignment_fieldName: Property = Property(name="fieldName", type=StringType)
Java_Assignment_variableExpr: Property = Property(name="variableExpr", type=StringType)
Java_Assignment.attributes={Java_Assignment_fieldName, Java_Assignment_objectId, Java_Assignment_variableExpr}

# Parameter class attributes and methods

# Java_Method class attributes and methods

# Statement class attributes and methods

# Annotation class attributes and methods

# Java_Parameter class attributes and methods
Java_Parameter_name: Property = Property(name="name", type=StringType)
Java_Parameter.attributes={Java_Parameter_name}

# Java_Field class attributes and methods
Java_Field_name: Property = Property(name="name", type=StringType)
Java_Field_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_Field_isProtected: Property = Property(name="isProtected", type=BooleanType)
Java_Field_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
Java_Field_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_Field.attributes={Java_Field_isProtected, Java_Field_name, Java_Field_isStatic, Java_Field_isPublic, Java_Field_isPrivate}

# Java_Return class attributes and methods
Java_Return_objectId: Property = Property(name="objectId", type=StringType)
Java_Return_fieldName: Property = Property(name="fieldName", type=StringType)
Java_Return.attributes={Java_Return_fieldName, Java_Return_objectId}

# Java_Annotation class attributes and methods
Java_Annotation_sentenceText: Property = Property(name="sentenceText", type=StringType)
Java_Annotation_type: Property = Property(name="type", type=StringType)
Java_Annotation.attributes={Java_Annotation_type, Java_Annotation_sentenceText}

# Relationships
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="#3", type=Java_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="02", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="#", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="0", type=ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType16: BinaryAssociation = BinaryAssociation(
    name="returnType16",
    ends={
        Property(name="Type", type=Java_MethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodSignature", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
implements4: BinaryAssociation = BinaryAssociation(
    name="implements4",
    ends={
        Property(name="Interface", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
superclass5: BinaryAssociation = BinaryAssociation(
    name="superclass5",
    ends={
        Property(name="Class", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class6", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
field7: BinaryAssociation = BinaryAssociation(
    name="field7",
    ends={
        Property(name="#9", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="08", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method10: BinaryAssociation = BinaryAssociation(
    name="method10",
    ends={
        Property(name="Method", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class11", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superinterface12: BinaryAssociation = BinaryAssociation(
    name="superinterface12",
    ends={
        Property(name="Interface13", type=Java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Interface", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
methodDeclaration14: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration14",
    ends={
        Property(name="MethodSignature", type=Java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Interface15", type=MethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type24: BinaryAssociation = BinaryAssociation(
    name="type24",
    ends={
        Property(name="Type25", type=Java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Field", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
owner26: BinaryAssociation = BinaryAssociation(
    name="owner26",
    ends={
        Property(name="#28", type=Java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="027", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)
type29: BinaryAssociation = BinaryAssociation(
    name="type29",
    ends={
        Property(name="Type30", type=Java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_VariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
parameters17: BinaryAssociation = BinaryAssociation(
    name="parameters17",
    ends={
        Property(name="Parameter", type=Java_MethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodSignature18", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements19: BinaryAssociation = BinaryAssociation(
    name="statements19",
    ends={
        Property(name="Statement", type=Java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Method", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation20: BinaryAssociation = BinaryAssociation(
    name="annotation20",
    ends={
        Property(name="Annotation", type=Java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Method21", type=Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type22: BinaryAssociation = BinaryAssociation(
    name="type22",
    ends={
        Property(name="Type23", type=Java_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Parameter", type=Type, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Java_ObjectType_Type = Generalization(general=Type, specific=Java_ObjectType)
gen_Java_PrimitiveType_Type = Generalization(general=Type, specific=Java_PrimitiveType)
gen_Java_Class_ObjectType = Generalization(general=ObjectType, specific=Java_Class)
gen_Java_VoidType_Type = Generalization(general=Type, specific=Java_VoidType)
gen_Java_Interface_ObjectType = Generalization(general=ObjectType, specific=Java_Interface)
gen_Java_MethodCall_Statement = Generalization(general=Statement, specific=Java_MethodCall)
gen_Java_VariableDeclaration_Statement = Generalization(general=Statement, specific=Java_VariableDeclaration)
gen_Java_Method_MethodSignature = Generalization(general=MethodSignature, specific=Java_Method)
gen_Java_Assignment_Statement = Generalization(general=Statement, specific=Java_Assignment)
gen_Java_Return_Statement = Generalization(general=Statement, specific=Java_Return)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Java_ObjectType, Package, Java_PrimitiveType, Java_Class, Java_Package, ObjectType, Java_Type, Java_VoidType, Type, Java_MethodSignature, Interface, Class_, Field, Method_, Java_Interface, MethodSignature, Java_Statement, Java_MethodCall, Java_VariableDeclaration, Java_Assignment, Parameter_, Java_Method, Statement, Annotation, Java_Parameter, Java_Field, Java_Return, Java_Annotation},
    associations={owner1, content0, returnType16, implements4, superclass5, field7, method10, superinterface12, methodDeclaration14, type24, owner26, type29, parameters17, statements19, annotation20, type22},
    generalizations={gen_Java_ObjectType_Type, gen_Java_PrimitiveType_Type, gen_Java_Class_ObjectType, gen_Java_VoidType_Type, gen_Java_Interface_ObjectType, gen_Java_MethodCall_Statement, gen_Java_VariableDeclaration_Statement, gen_Java_Method_MethodSignature, gen_Java_Assignment_Statement, gen_Java_Return_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)