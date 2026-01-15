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
simplejava_Import = Class(name="simplejava::Import")
simplejava_ClassDeclaration = Class(name="simplejava::ClassDeclaration")
simplejava_SimpleJava = Class(name="simplejava::SimpleJava")
simplejava_PackageDeclaration = Class(name="simplejava::PackageDeclaration")
simplejava_SimpleParameter = Class(name="simplejava::SimpleParameter")
Parameter_ = Class(name="Parameter")
simplejava_Attribute = Class(name="simplejava::Attribute")
simplejava_GenericExpression = Class(name="simplejava::GenericExpression")
simplejava_Parameter = Class(name="simplejava::Parameter")
simplejava_Method = Class(name="simplejava::Method")
simplejava_Type = Class(name="simplejava::Type")
Statement = Class(name="Statement")
simplejava_Statement = Class(name="simplejava::Statement")
simplejava_SimpleStatement = Class(name="simplejava::SimpleStatement")
simplejava_SimpleVariableDeclaration = Class(name="simplejava::SimpleVariableDeclaration")
SimpleStatement = Class(name="SimpleStatement")
simplejava_MethodBlock = Class(name="simplejava::MethodBlock")
simplejava_IfStatement = Class(name="simplejava::IfStatement")
simplejava_ParanthesisOrBinaryExpression = Class(name="simplejava::ParanthesisOrBinaryExpression")
simplejava_VariableDeclaration = Class(name="simplejava::VariableDeclaration")
SimpleVariableDeclaration = Class(name="SimpleVariableDeclaration")
simplejava_Assignment = Class(name="simplejava::Assignment")
simplejava_ForInStatement = Class(name="simplejava::ForInStatement")
simplejava_ForStatement = Class(name="simplejava::ForStatement")
simplejava_MethodCall = Class(name="simplejava::MethodCall")
GenericExpression = Class(name="GenericExpression")
simplejava_WhileStatement = Class(name="simplejava::WhileStatement")
simplejava_ReturnStatement = Class(name="simplejava::ReturnStatement")
simplejava_NullExpression = Class(name="simplejava::NullExpression")
ConstantExpression = Class(name="ConstantExpression")
simplejava_IntegerExpression = Class(name="simplejava::IntegerExpression")
simplejava_BooleanExpression = Class(name="simplejava::BooleanExpression")
simplejava_StringExpression = Class(name="simplejava::StringExpression")
simplejava_UnaryExpression = Class(name="simplejava::UnaryExpression")
simplejava_ConstructorCall = Class(name="simplejava::ConstructorCall")
simplejava_ConstantExpression = Class(name="simplejava::ConstantExpression")
simplejava_VariableExpression = Class(name="simplejava::VariableExpression")

# simplejava_Import class attributes and methods
simplejava_Import_imported: Property = Property(name="imported", type=StringType)
simplejava_Import.attributes={simplejava_Import_imported}

# simplejava_ClassDeclaration class attributes and methods
simplejava_ClassDeclaration_name: Property = Property(name="name", type=StringType)
simplejava_ClassDeclaration.attributes={simplejava_ClassDeclaration_name}

# simplejava_SimpleJava class attributes and methods

# simplejava_PackageDeclaration class attributes and methods
simplejava_PackageDeclaration_name: Property = Property(name="name", type=StringType)
simplejava_PackageDeclaration.attributes={simplejava_PackageDeclaration_name}

# simplejava_SimpleParameter class attributes and methods

# Parameter class attributes and methods

# simplejava_Attribute class attributes and methods

# simplejava_GenericExpression class attributes and methods

# simplejava_Parameter class attributes and methods
simplejava_Parameter_name: Property = Property(name="name", type=StringType)
simplejava_Parameter.attributes={simplejava_Parameter_name}

# simplejava_Method class attributes and methods
simplejava_Method_static: Property = Property(name="static", type=BooleanType)
simplejava_Method_name: Property = Property(name="name", type=StringType)
simplejava_Method.attributes={simplejava_Method_static, simplejava_Method_name}

# simplejava_Type class attributes and methods
simplejava_Type_typeName: Property = Property(name="typeName", type=StringType)
simplejava_Type_isVoid: Property = Property(name="isVoid", type=BooleanType)
simplejava_Type_isArray: Property = Property(name="isArray", type=BooleanType)
simplejava_Type.attributes={simplejava_Type_isVoid, simplejava_Type_isArray, simplejava_Type_typeName}

# Statement class attributes and methods

# simplejava_Statement class attributes and methods

# simplejava_SimpleStatement class attributes and methods

# simplejava_SimpleVariableDeclaration class attributes and methods

# SimpleStatement class attributes and methods

# simplejava_MethodBlock class attributes and methods
simplejava_MethodBlock_generated: Property = Property(name="generated", type=BooleanType)
simplejava_MethodBlock.attributes={simplejava_MethodBlock_generated}

# simplejava_IfStatement class attributes and methods

# simplejava_ParanthesisOrBinaryExpression class attributes and methods
simplejava_ParanthesisOrBinaryExpression_type: Property = Property(name="type", type=StringType)
simplejava_ParanthesisOrBinaryExpression.attributes={simplejava_ParanthesisOrBinaryExpression_type}

# simplejava_VariableDeclaration class attributes and methods

# SimpleVariableDeclaration class attributes and methods

# simplejava_Assignment class attributes and methods

# simplejava_ForInStatement class attributes and methods

# simplejava_ForStatement class attributes and methods

# simplejava_MethodCall class attributes and methods
simplejava_MethodCall_thisObject: Property = Property(name="thisObject", type=BooleanType)
simplejava_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
simplejava_MethodCall.attributes={simplejava_MethodCall_thisObject, simplejava_MethodCall_methodName}

# GenericExpression class attributes and methods

# simplejava_WhileStatement class attributes and methods

# simplejava_ReturnStatement class attributes and methods

# simplejava_NullExpression class attributes and methods

# ConstantExpression class attributes and methods

# simplejava_IntegerExpression class attributes and methods
simplejava_IntegerExpression_value: Property = Property(name="value", type=IntegerType)
simplejava_IntegerExpression.attributes={simplejava_IntegerExpression_value}

# simplejava_BooleanExpression class attributes and methods
simplejava_BooleanExpression_value: Property = Property(name="value", type=BooleanType)
simplejava_BooleanExpression.attributes={simplejava_BooleanExpression_value}

# simplejava_StringExpression class attributes and methods
simplejava_StringExpression_value: Property = Property(name="value", type=StringType)
simplejava_StringExpression.attributes={simplejava_StringExpression_value}

# simplejava_UnaryExpression class attributes and methods
simplejava_UnaryExpression_type: Property = Property(name="type", type=StringType)
simplejava_UnaryExpression.attributes={simplejava_UnaryExpression_type}

# simplejava_ConstructorCall class attributes and methods

# simplejava_ConstantExpression class attributes and methods

# simplejava_VariableExpression class attributes and methods

# Relationships
imports1: BinaryAssociation = BinaryAssociation(
    name="imports1",
    ends={
        Property(name="simplejava_Import", type=simplejava_SimpleJava, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_SimpleJava2", type=simplejava_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clazz3: BinaryAssociation = BinaryAssociation(
    name="clazz3",
    ends={
        Property(name="simplejava_ClassDeclaration", type=simplejava_SimpleJava, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_SimpleJava4", type=simplejava_ClassDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="simplejava_PackageDeclaration", type=simplejava_SimpleJava, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_SimpleJava", type=simplejava_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="simplejava_GenericExpression", type=simplejava_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Attribute", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef12: BinaryAssociation = BinaryAssociation(
    name="typeRef12",
    ends={
        Property(name="simplejava_ClassDeclaration14", type=simplejava_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Type13", type=simplejava_ClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
attribute5: BinaryAssociation = BinaryAssociation(
    name="attribute5",
    ends={
        Property(name="simplejava_Parameter", type=simplejava_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ClassDeclaration6", type=simplejava_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
method7: BinaryAssociation = BinaryAssociation(
    name="method7",
    ends={
        Property(name="simplejava_Method", type=simplejava_ClassDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ClassDeclaration8", type=simplejava_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="simplejava_Type", type=simplejava_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Parameter10", type=simplejava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
content20: BinaryAssociation = BinaryAssociation(
    name="content20",
    ends={
        Property(name="simplejava_MethodBlock", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method21", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="simplejava_Statement", type=simplejava_MethodBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodBlock23", type=simplejava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType15: BinaryAssociation = BinaryAssociation(
    name="returnType15",
    ends={
        Property(name="simplejava_Type17", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method16", type=simplejava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter18: BinaryAssociation = BinaryAssociation(
    name="parameter18",
    ends={
        Property(name="simplejava_SimpleParameter", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method19", type=simplejava_SimpleParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter29: BinaryAssociation = BinaryAssociation(
    name="parameter29",
    ends={
        Property(name="simplejava_Parameter30", type=simplejava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Assignment", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
expression31: BinaryAssociation = BinaryAssociation(
    name="expression31",
    ends={
        Property(name="simplejava_GenericExpression33", type=simplejava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Assignment32", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition34: BinaryAssociation = BinaryAssociation(
    name="condition34",
    ends={
        Property(name="simplejava_ParanthesisOrBinaryExpression", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then35: BinaryAssociation = BinaryAssociation(
    name="then35",
    ends={
        Property(name="simplejava_MethodBlock37", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement36", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter24: BinaryAssociation = BinaryAssociation(
    name="parameter24",
    ends={
        Property(name="simplejava_SimpleParameter25", type=simplejava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableDeclaration", type=simplejava_SimpleParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression26: BinaryAssociation = BinaryAssociation(
    name="expression26",
    ends={
        Property(name="simplejava_GenericExpression28", type=simplejava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableDeclaration27", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
continuation45: BinaryAssociation = BinaryAssociation(
    name="continuation45",
    ends={
        Property(name="simplejava_SimpleStatement47", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement46", type=simplejava_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body48: BinaryAssociation = BinaryAssociation(
    name="body48",
    ends={
        Property(name="simplejava_Statement50", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement49", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
subparameter51: BinaryAssociation = BinaryAssociation(
    name="subparameter51",
    ends={
        Property(name="simplejava_SimpleParameter52", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement", type=simplejava_SimpleParameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression53: BinaryAssociation = BinaryAssociation(
    name="expression53",
    ends={
        Property(name="simplejava_GenericExpression55", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement54", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body56: BinaryAssociation = BinaryAssociation(
    name="body56",
    ends={
        Property(name="simplejava_Statement58", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement57", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else38: BinaryAssociation = BinaryAssociation(
    name="else38",
    ends={
        Property(name="simplejava_MethodBlock40", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement39", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init41: BinaryAssociation = BinaryAssociation(
    name="init41",
    ends={
        Property(name="simplejava_SimpleStatement", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement", type=simplejava_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition42: BinaryAssociation = BinaryAssociation(
    name="condition42",
    ends={
        Property(name="simplejava_GenericExpression44", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement43", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression64: BinaryAssociation = BinaryAssociation(
    name="expression64",
    ends={
        Property(name="simplejava_ReturnStatement", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="simplejava_GenericExpression65", type=simplejava_ReturnStatement, multiplicity=Multiplicity(1, 1))
    }
)
object66: BinaryAssociation = BinaryAssociation(
    name="object66",
    ends={
        Property(name="simplejava_Parameter67", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
method68: BinaryAssociation = BinaryAssociation(
    name="method68",
    ends={
        Property(name="simplejava_Method70", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall69", type=simplejava_Method, multiplicity=Multiplicity(0, 1))
    }
)
parameter71: BinaryAssociation = BinaryAssociation(
    name="parameter71",
    ends={
        Property(name="simplejava_GenericExpression73", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall72", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition59: BinaryAssociation = BinaryAssociation(
    name="condition59",
    ends={
        Property(name="simplejava_ParanthesisOrBinaryExpression60", type=simplejava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_WhileStatement", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body61: BinaryAssociation = BinaryAssociation(
    name="body61",
    ends={
        Property(name="simplejava_Statement63", type=simplejava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_WhileStatement62", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type74: BinaryAssociation = BinaryAssociation(
    name="type74",
    ends={
        Property(name="simplejava_Type75", type=simplejava_ConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ConstructorCall", type=simplejava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter76: BinaryAssociation = BinaryAssociation(
    name="parameter76",
    ends={
        Property(name="simplejava_ConstantExpression", type=simplejava_ConstructorCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ConstructorCall77", type=simplejava_ConstantExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
argument85: BinaryAssociation = BinaryAssociation(
    name="argument85",
    ends={
        Property(name="simplejava_GenericExpression87", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ParanthesisOrBinaryExpression86", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source78: BinaryAssociation = BinaryAssociation(
    name="source78",
    ends={
        Property(name="simplejava_GenericExpression79", type=simplejava_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_UnaryExpression", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable80: BinaryAssociation = BinaryAssociation(
    name="variable80",
    ends={
        Property(name="simplejava_Parameter81", type=simplejava_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableExpression", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
source82: BinaryAssociation = BinaryAssociation(
    name="source82",
    ends={
        Property(name="simplejava_GenericExpression84", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ParanthesisOrBinaryExpression83", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simplejava_SimpleParameter_Parameter = Generalization(general=Parameter_, specific=simplejava_SimpleParameter)
gen_simplejava_Attribute_Parameter = Generalization(general=Parameter_, specific=simplejava_Attribute)
gen_simplejava_MethodBlock_Statement = Generalization(general=Statement, specific=simplejava_MethodBlock)
gen_simplejava_SimpleVariableDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=simplejava_SimpleVariableDeclaration)
gen_simplejava_Assignment_Statement = Generalization(general=Statement, specific=simplejava_Assignment)
gen_simplejava_IfStatement_Statement = Generalization(general=Statement, specific=simplejava_IfStatement)
gen_simplejava_VariableDeclaration_Statement = Generalization(general=Statement, specific=simplejava_VariableDeclaration)
gen_simplejava_VariableDeclaration_SimpleVariableDeclaration = Generalization(general=SimpleVariableDeclaration, specific=simplejava_VariableDeclaration)
gen_simplejava_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=simplejava_Assignment)
gen_simplejava_ForInStatement_Statement = Generalization(general=Statement, specific=simplejava_ForInStatement)
gen_simplejava_ForStatement_Statement = Generalization(general=Statement, specific=simplejava_ForStatement)
gen_simplejava_MethodCall_Statement = Generalization(general=Statement, specific=simplejava_MethodCall)
gen_simplejava_MethodCall_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_MethodCall)
gen_simplejava_WhileStatement_Statement = Generalization(general=Statement, specific=simplejava_WhileStatement)
gen_simplejava_ReturnStatement_Statement = Generalization(general=Statement, specific=simplejava_ReturnStatement)
gen_simplejava_NullExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_NullExpression)
gen_simplejava_IntegerExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_IntegerExpression)
gen_simplejava_BooleanExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_BooleanExpression)
gen_simplejava_StringExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_StringExpression)
gen_simplejava_UnaryExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_UnaryExpression)
gen_simplejava_ConstructorCall_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_ConstructorCall)
gen_simplejava_ConstantExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_ConstantExpression)
gen_simplejava_VariableExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_VariableExpression)
gen_simplejava_ParanthesisOrBinaryExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_ParanthesisOrBinaryExpression)

# Domain Model
domain_model = DomainModel(
    name="simplejava",
    types={simplejava_Import, simplejava_ClassDeclaration, simplejava_SimpleJava, simplejava_PackageDeclaration, simplejava_SimpleParameter, Parameter_, simplejava_Attribute, simplejava_GenericExpression, simplejava_Parameter, simplejava_Method, simplejava_Type, Statement, simplejava_Statement, simplejava_SimpleStatement, simplejava_SimpleVariableDeclaration, SimpleStatement, simplejava_MethodBlock, simplejava_IfStatement, simplejava_ParanthesisOrBinaryExpression, simplejava_VariableDeclaration, SimpleVariableDeclaration, simplejava_Assignment, simplejava_ForInStatement, simplejava_ForStatement, simplejava_MethodCall, GenericExpression, simplejava_WhileStatement, simplejava_ReturnStatement, simplejava_NullExpression, ConstantExpression, simplejava_IntegerExpression, simplejava_BooleanExpression, simplejava_StringExpression, simplejava_UnaryExpression, simplejava_ConstructorCall, simplejava_ConstantExpression, simplejava_VariableExpression},
    associations={imports1, clazz3, package0, expression11, typeRef12, attribute5, method7, type9, content20, statements22, returnType15, parameter18, parameter29, expression31, condition34, then35, parameter24, expression26, continuation45, body48, subparameter51, expression53, body56, else38, init41, condition42, expression64, object66, method68, parameter71, condition59, body61, type74, parameter76, argument85, source78, variable80, source82},
    generalizations={gen_simplejava_SimpleParameter_Parameter, gen_simplejava_Attribute_Parameter, gen_simplejava_MethodBlock_Statement, gen_simplejava_SimpleVariableDeclaration_SimpleStatement, gen_simplejava_Assignment_Statement, gen_simplejava_IfStatement_Statement, gen_simplejava_VariableDeclaration_Statement, gen_simplejava_VariableDeclaration_SimpleVariableDeclaration, gen_simplejava_Assignment_SimpleStatement, gen_simplejava_ForInStatement_Statement, gen_simplejava_ForStatement_Statement, gen_simplejava_MethodCall_Statement, gen_simplejava_MethodCall_GenericExpression, gen_simplejava_WhileStatement_Statement, gen_simplejava_ReturnStatement_Statement, gen_simplejava_NullExpression_ConstantExpression, gen_simplejava_IntegerExpression_ConstantExpression, gen_simplejava_BooleanExpression_ConstantExpression, gen_simplejava_StringExpression_ConstantExpression, gen_simplejava_UnaryExpression_GenericExpression, gen_simplejava_ConstructorCall_GenericExpression, gen_simplejava_ConstantExpression_GenericExpression, gen_simplejava_VariableExpression_GenericExpression, gen_simplejava_ParanthesisOrBinaryExpression_GenericExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)