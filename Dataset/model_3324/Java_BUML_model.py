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
Java_Package = Class(name="Java_Package")
ObjectType = Class(name="ObjectType")
Java_Type = Class(name="Java_Type", is_abstract=True)
Field = Class(name="Field")
Method_ = Class(name="Method")
Java_Interface = Class(name="Java_Interface")
MethodSignature = Class(name="MethodSignature")
Java_MethodSignature = Class(name="Java_MethodSignature")
Parameter_ = Class(name="Parameter")
Java_Method = Class(name="Java_Method")
Statement = Class(name="Statement")
Annotation = Class(name="Annotation")
Java_Parameter = Class(name="Java_Parameter")
Java_Field = Class(name="Java_Field")
Java_VoidType = Class(name="Java_VoidType")
Type = Class(name="Type")
Java_ObjectType = Class(name="Java_ObjectType", is_abstract=True)
Package = Class(name="Package")
Java_PrimitiveType = Class(name="Java_PrimitiveType")
Java_Class = Class(name="Java_Class")
Interface = Class(name="Interface")
Class_ = Class(name="Class")
Java_VariableDeclaration = Class(name="Java_VariableDeclaration")
Java_Assignment = Class(name="Java_Assignment")
Java_Return = Class(name="Java_Return")
Java_Annotation = Class(name="Java_Annotation")
Java_Statement = Class(name="Java_Statement", is_abstract=True)
Java_MethodCall = Class(name="Java_MethodCall")

# Java_Package class attributes and methods
Java_Package_name: Property = Property(name="name", type=StringType)
Java_Package.attributes={Java_Package_name}

# ObjectType class attributes and methods

# Java_Type class attributes and methods
Java_Type_name: Property = Property(name="name", type=StringType)
Java_Type.attributes={Java_Type_name}

# Field class attributes and methods

# Method class attributes and methods

# Java_Interface class attributes and methods

# MethodSignature class attributes and methods

# Java_MethodSignature class attributes and methods
Java_MethodSignature_name: Property = Property(name="name", type=StringType)
Java_MethodSignature_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_MethodSignature_isProtected: Property = Property(name="isProtected", type=BooleanType)
Java_MethodSignature_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
Java_MethodSignature_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_MethodSignature.attributes={Java_MethodSignature_isStatic, Java_MethodSignature_isPrivate, Java_MethodSignature_name, Java_MethodSignature_isProtected, Java_MethodSignature_isPublic}

# Parameter class attributes and methods

# Java_Method class attributes and methods

# Statement class attributes and methods

# Annotation class attributes and methods

# Java_Parameter class attributes and methods
Java_Parameter_name: Property = Property(name="name", type=StringType)
Java_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
Java_Parameter.attributes={Java_Parameter_defaultValue, Java_Parameter_name}

# Java_Field class attributes and methods
Java_Field_name: Property = Property(name="name", type=StringType)
Java_Field_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_Field_isProtected: Property = Property(name="isProtected", type=BooleanType)
Java_Field_isPrivate: Property = Property(name="isPrivate", type=BooleanType)
Java_Field_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_Field.attributes={Java_Field_isPublic, Java_Field_isProtected, Java_Field_isPrivate, Java_Field_name, Java_Field_isStatic}

# Java_VoidType class attributes and methods

# Type class attributes and methods

# Java_ObjectType class attributes and methods

# Package class attributes and methods

# Java_PrimitiveType class attributes and methods

# Java_Class class attributes and methods
Java_Class_isPublic: Property = Property(name="isPublic", type=BooleanType)
Java_Class_isStatic: Property = Property(name="isStatic", type=BooleanType)
Java_Class.attributes={Java_Class_isStatic, Java_Class_isPublic}

# Interface class attributes and methods

# Class class attributes and methods

# Java_VariableDeclaration class attributes and methods
Java_VariableDeclaration_variableName: Property = Property(name="variableName", type=StringType)
Java_VariableDeclaration.attributes={Java_VariableDeclaration_variableName}

# Java_Assignment class attributes and methods
Java_Assignment_objectId: Property = Property(name="objectId", type=StringType)
Java_Assignment_fieldName: Property = Property(name="fieldName", type=StringType)
Java_Assignment_variableExpr: Property = Property(name="variableExpr", type=StringType)
Java_Assignment.attributes={Java_Assignment_fieldName, Java_Assignment_objectId, Java_Assignment_variableExpr}

# Java_Return class attributes and methods
Java_Return_objectId: Property = Property(name="objectId", type=StringType)
Java_Return_fieldName: Property = Property(name="fieldName", type=StringType)
Java_Return.attributes={Java_Return_fieldName, Java_Return_objectId}

# Java_Annotation class attributes and methods
Java_Annotation_sentenceText: Property = Property(name="sentenceText", type=StringType)
Java_Annotation_type: Property = Property(name="type", type=StringType)
Java_Annotation.attributes={Java_Annotation_sentenceText, Java_Annotation_type}

# Java_Statement class attributes and methods

# Java_MethodCall class attributes and methods
Java_MethodCall_variableName: Property = Property(name="variableName", type=StringType)
Java_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
Java_MethodCall.attributes={Java_MethodCall_variableName, Java_MethodCall_methodName}

# Relationships
content0: BinaryAssociation = BinaryAssociation(
    name="content0",
    ends={
        Property(name="ObjectType", type=Java_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=ObjectType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superclass3: BinaryAssociation = BinaryAssociation(
    name="superclass3",
    ends={
        Property(name="Class", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class4", type=Class_, multiplicity=Multiplicity(0, 1))
    }
)
field5: BinaryAssociation = BinaryAssociation(
    name="field5",
    ends={
        Property(name="Field", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="owner6", type=Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method7: BinaryAssociation = BinaryAssociation(
    name="method7",
    ends={
        Property(name="Method", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class8", type=Method_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superinterface9: BinaryAssociation = BinaryAssociation(
    name="superinterface9",
    ends={
        Property(name="Interface10", type=Java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Interface", type=Interface, multiplicity=Multiplicity(0, 1))
    }
)
methodDeclaration11: BinaryAssociation = BinaryAssociation(
    name="methodDeclaration11",
    ends={
        Property(name="MethodSignature", type=Java_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Interface12", type=MethodSignature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType13: BinaryAssociation = BinaryAssociation(
    name="returnType13",
    ends={
        Property(name="Type", type=Java_MethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodSignature", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
parameters14: BinaryAssociation = BinaryAssociation(
    name="parameters14",
    ends={
        Property(name="Parameter", type=Java_MethodSignature, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_MethodSignature15", type=Parameter_, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements16: BinaryAssociation = BinaryAssociation(
    name="statements16",
    ends={
        Property(name="Statement", type=Java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Method", type=Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
annotation17: BinaryAssociation = BinaryAssociation(
    name="annotation17",
    ends={
        Property(name="Annotation", type=Java_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Method18", type=Annotation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type19: BinaryAssociation = BinaryAssociation(
    name="type19",
    ends={
        Property(name="Type20", type=Java_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Parameter", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="Package", type=Java_ObjectType, multiplicity=Multiplicity(1, 1)),
        Property(name="content", type=Package, multiplicity=Multiplicity(1, 1))
    }
)
implements2: BinaryAssociation = BinaryAssociation(
    name="implements2",
    ends={
        Property(name="Interface", type=Java_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Class", type=Interface, multiplicity=Multiplicity(0, 9999))
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="Type26", type=Java_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_VariableDeclaration", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
type21: BinaryAssociation = BinaryAssociation(
    name="type21",
    ends={
        Property(name="Type22", type=Java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="Java_Field", type=Type, multiplicity=Multiplicity(1, 1))
    }
)
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="Class24", type=Java_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="field", type=Class_, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Java_Interface_ObjectType = Generalization(general=ObjectType, specific=Java_Interface)
gen_Java_Method_MethodSignature = Generalization(general=MethodSignature, specific=Java_Method)
gen_Java_VoidType_Type = Generalization(general=Type, specific=Java_VoidType)
gen_Java_ObjectType_Type = Generalization(general=Type, specific=Java_ObjectType)
gen_Java_PrimitiveType_Type = Generalization(general=Type, specific=Java_PrimitiveType)
gen_Java_Class_ObjectType = Generalization(general=ObjectType, specific=Java_Class)
gen_Java_VariableDeclaration_Statement = Generalization(general=Statement, specific=Java_VariableDeclaration)
gen_Java_Assignment_Statement = Generalization(general=Statement, specific=Java_Assignment)
gen_Java_Return_Statement = Generalization(general=Statement, specific=Java_Return)
gen_Java_MethodCall_Statement = Generalization(general=Statement, specific=Java_MethodCall)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={Java_Package, ObjectType, Java_Type, Field, Method_, Java_Interface, MethodSignature, Java_MethodSignature, Parameter_, Java_Method, Statement, Annotation, Java_Parameter, Java_Field, Java_VoidType, Type, Java_ObjectType, Package, Java_PrimitiveType, Java_Class, Interface, Class_, Java_VariableDeclaration, Java_Assignment, Java_Return, Java_Annotation, Java_Statement, Java_MethodCall},
    associations={content0, superclass3, field5, method7, superinterface9, methodDeclaration11, returnType13, parameters14, statements16, annotation17, type19, owner1, implements2, type25, type21, owner23},
    generalizations={gen_Java_Interface_ObjectType, gen_Java_Method_MethodSignature, gen_Java_VoidType_Type, gen_Java_ObjectType_Type, gen_Java_PrimitiveType_Type, gen_Java_Class_ObjectType, gen_Java_VariableDeclaration_Statement, gen_Java_Assignment_Statement, gen_Java_Return_Statement, gen_Java_MethodCall_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)