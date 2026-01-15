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
simplejava_Parameter = Class(name="simplejava::Parameter")
simplejava_Method = Class(name="simplejava::Method")
simplejava_Type = Class(name="simplejava::Type")
simplejava_SimpleJava = Class(name="simplejava::SimpleJava")
simplejava_PackageDeclaration = Class(name="simplejava::PackageDeclaration")
simplejava_Import = Class(name="simplejava::Import")
simplejava_ClassDeclaration = Class(name="simplejava::ClassDeclaration")
Statement = Class(name="Statement")
simplejava_Statement = Class(name="simplejava::Statement")
simplejava_SimpleStatement = Class(name="simplejava::SimpleStatement")
simplejava_SimpleVariableDeclaration = Class(name="simplejava::SimpleVariableDeclaration")
SimpleStatement = Class(name="SimpleStatement")
simplejava_VariableDeclaration = Class(name="simplejava::VariableDeclaration")
SimpleVariableDeclaration = Class(name="SimpleVariableDeclaration")
simplejava_GenericExpression = Class(name="simplejava::GenericExpression")
simplejava_Assignment = Class(name="simplejava::Assignment")
simplejava_MethodBlock = Class(name="simplejava::MethodBlock")
simplejava_ForStatement = Class(name="simplejava::ForStatement")
simplejava_ForInStatement = Class(name="simplejava::ForInStatement")
simplejava_IfStatement = Class(name="simplejava::IfStatement")
simplejava_ParanthesisOrBinaryExpression = Class(name="simplejava::ParanthesisOrBinaryExpression")
simplejava_ReturnStatement = Class(name="simplejava::ReturnStatement")
simplejava_MethodCall = Class(name="simplejava::MethodCall")
GenericExpression = Class(name="GenericExpression")
simplejava_WhileStatement = Class(name="simplejava::WhileStatement")
simplejava_UnaryExpression = Class(name="simplejava::UnaryExpression")
simplejava_VariableExpression = Class(name="simplejava::VariableExpression")
simplejava_ConstantExpression = Class(name="simplejava::ConstantExpression")
simplejava_NullExpression = Class(name="simplejava::NullExpression")
ConstantExpression = Class(name="ConstantExpression")
simplejava_IntegerExpression = Class(name="simplejava::IntegerExpression")
simplejava_BooleanExpression = Class(name="simplejava::BooleanExpression")
simplejava_StringExpression = Class(name="simplejava::StringExpression")

# simplejava_Parameter class attributes and methods
simplejava_Parameter_name: Property = Property(name="name", type=StringType)
simplejava_Parameter.attributes={simplejava_Parameter_name}

# simplejava_Method class attributes and methods
simplejava_Method_static: Property = Property(name="static", type=BooleanType)
simplejava_Method_name: Property = Property(name="name", type=StringType)
simplejava_Method.attributes={simplejava_Method_name, simplejava_Method_static}

# simplejava_Type class attributes and methods
simplejava_Type_typeName: Property = Property(name="typeName", type=StringType)
simplejava_Type.attributes={simplejava_Type_typeName}

# simplejava_SimpleJava class attributes and methods

# simplejava_PackageDeclaration class attributes and methods
simplejava_PackageDeclaration_name: Property = Property(name="name", type=StringType)
simplejava_PackageDeclaration.attributes={simplejava_PackageDeclaration_name}

# simplejava_Import class attributes and methods
simplejava_Import_imported: Property = Property(name="imported", type=StringType)
simplejava_Import.attributes={simplejava_Import_imported}

# simplejava_ClassDeclaration class attributes and methods
simplejava_ClassDeclaration_name: Property = Property(name="name", type=StringType)
simplejava_ClassDeclaration.attributes={simplejava_ClassDeclaration_name}

# Statement class attributes and methods

# simplejava_Statement class attributes and methods

# simplejava_SimpleStatement class attributes and methods

# simplejava_SimpleVariableDeclaration class attributes and methods

# SimpleStatement class attributes and methods

# simplejava_VariableDeclaration class attributes and methods

# SimpleVariableDeclaration class attributes and methods

# simplejava_GenericExpression class attributes and methods

# simplejava_Assignment class attributes and methods

# simplejava_MethodBlock class attributes and methods
simplejava_MethodBlock_generated: Property = Property(name="generated", type=BooleanType)
simplejava_MethodBlock.attributes={simplejava_MethodBlock_generated}

# simplejava_ForStatement class attributes and methods

# simplejava_ForInStatement class attributes and methods

# simplejava_IfStatement class attributes and methods

# simplejava_ParanthesisOrBinaryExpression class attributes and methods
simplejava_ParanthesisOrBinaryExpression_type: Property = Property(name="type", type=StringType)
simplejava_ParanthesisOrBinaryExpression.attributes={simplejava_ParanthesisOrBinaryExpression_type}

# simplejava_ReturnStatement class attributes and methods

# simplejava_MethodCall class attributes and methods
simplejava_MethodCall_thisObject: Property = Property(name="thisObject", type=BooleanType)
simplejava_MethodCall_methodName: Property = Property(name="methodName", type=StringType)
simplejava_MethodCall.attributes={simplejava_MethodCall_thisObject, simplejava_MethodCall_methodName}

# GenericExpression class attributes and methods

# simplejava_WhileStatement class attributes and methods

# simplejava_UnaryExpression class attributes and methods
simplejava_UnaryExpression_type: Property = Property(name="type", type=StringType)
simplejava_UnaryExpression.attributes={simplejava_UnaryExpression_type}

# simplejava_VariableExpression class attributes and methods

# simplejava_ConstantExpression class attributes and methods

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

# Relationships
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
package0: BinaryAssociation = BinaryAssociation(
    name="package0",
    ends={
        Property(name="simplejava_PackageDeclaration", type=simplejava_SimpleJava, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_SimpleJava", type=simplejava_PackageDeclaration, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
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
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="simplejava_Statement", type=simplejava_MethodBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodBlock23", type=simplejava_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameter24: BinaryAssociation = BinaryAssociation(
    name="parameter24",
    ends={
        Property(name="simplejava_Parameter25", type=simplejava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableDeclaration", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression26: BinaryAssociation = BinaryAssociation(
    name="expression26",
    ends={
        Property(name="simplejava_GenericExpression", type=simplejava_VariableDeclaration, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableDeclaration27", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
typeRef11: BinaryAssociation = BinaryAssociation(
    name="typeRef11",
    ends={
        Property(name="simplejava_ClassDeclaration13", type=simplejava_Type, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Type12", type=simplejava_ClassDeclaration, multiplicity=Multiplicity(0, 1))
    }
)
returnType14: BinaryAssociation = BinaryAssociation(
    name="returnType14",
    ends={
        Property(name="simplejava_Type16", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method15", type=simplejava_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter17: BinaryAssociation = BinaryAssociation(
    name="parameter17",
    ends={
        Property(name="simplejava_Parameter19", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method18", type=simplejava_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
content20: BinaryAssociation = BinaryAssociation(
    name="content20",
    ends={
        Property(name="simplejava_MethodBlock", type=simplejava_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Method21", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
then34: BinaryAssociation = BinaryAssociation(
    name="then34",
    ends={
        Property(name="simplejava_MethodBlock36", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement35", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
else37: BinaryAssociation = BinaryAssociation(
    name="else37",
    ends={
        Property(name="simplejava_MethodBlock39", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement38", type=simplejava_MethodBlock, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
init40: BinaryAssociation = BinaryAssociation(
    name="init40",
    ends={
        Property(name="simplejava_SimpleStatement", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement", type=simplejava_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition41: BinaryAssociation = BinaryAssociation(
    name="condition41",
    ends={
        Property(name="simplejava_GenericExpression43", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement42", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
continuation44: BinaryAssociation = BinaryAssociation(
    name="continuation44",
    ends={
        Property(name="simplejava_SimpleStatement46", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement45", type=simplejava_SimpleStatement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body47: BinaryAssociation = BinaryAssociation(
    name="body47",
    ends={
        Property(name="simplejava_Statement49", type=simplejava_ForStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForStatement48", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameter28: BinaryAssociation = BinaryAssociation(
    name="parameter28",
    ends={
        Property(name="simplejava_Parameter29", type=simplejava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Assignment", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
expression30: BinaryAssociation = BinaryAssociation(
    name="expression30",
    ends={
        Property(name="simplejava_GenericExpression32", type=simplejava_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_Assignment31", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition33: BinaryAssociation = BinaryAssociation(
    name="condition33",
    ends={
        Property(name="simplejava_ParanthesisOrBinaryExpression", type=simplejava_IfStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_IfStatement", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body60: BinaryAssociation = BinaryAssociation(
    name="body60",
    ends={
        Property(name="simplejava_Statement62", type=simplejava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_WhileStatement61", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression63: BinaryAssociation = BinaryAssociation(
    name="expression63",
    ends={
        Property(name="simplejava_GenericExpression64", type=simplejava_ReturnStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ReturnStatement", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
object65: BinaryAssociation = BinaryAssociation(
    name="object65",
    ends={
        Property(name="simplejava_Parameter66", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
method67: BinaryAssociation = BinaryAssociation(
    name="method67",
    ends={
        Property(name="simplejava_Method69", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall68", type=simplejava_Method, multiplicity=Multiplicity(0, 1))
    }
)
parameter70: BinaryAssociation = BinaryAssociation(
    name="parameter70",
    ends={
        Property(name="simplejava_GenericExpression72", type=simplejava_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_MethodCall71", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subparameter50: BinaryAssociation = BinaryAssociation(
    name="subparameter50",
    ends={
        Property(name="simplejava_Parameter51", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression52: BinaryAssociation = BinaryAssociation(
    name="expression52",
    ends={
        Property(name="simplejava_GenericExpression54", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement53", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
body55: BinaryAssociation = BinaryAssociation(
    name="body55",
    ends={
        Property(name="simplejava_Statement57", type=simplejava_ForInStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ForInStatement56", type=simplejava_Statement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition58: BinaryAssociation = BinaryAssociation(
    name="condition58",
    ends={
        Property(name="simplejava_ParanthesisOrBinaryExpression59", type=simplejava_WhileStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_WhileStatement", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source73: BinaryAssociation = BinaryAssociation(
    name="source73",
    ends={
        Property(name="simplejava_GenericExpression74", type=simplejava_UnaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_UnaryExpression", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable75: BinaryAssociation = BinaryAssociation(
    name="variable75",
    ends={
        Property(name="simplejava_Parameter76", type=simplejava_VariableExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_VariableExpression", type=simplejava_Parameter, multiplicity=Multiplicity(0, 1))
    }
)
source77: BinaryAssociation = BinaryAssociation(
    name="source77",
    ends={
        Property(name="simplejava_GenericExpression79", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ParanthesisOrBinaryExpression78", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
argument80: BinaryAssociation = BinaryAssociation(
    name="argument80",
    ends={
        Property(name="simplejava_GenericExpression82", type=simplejava_ParanthesisOrBinaryExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="simplejava_ParanthesisOrBinaryExpression81", type=simplejava_GenericExpression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_simplejava_MethodBlock_Statement = Generalization(general=Statement, specific=simplejava_MethodBlock)
gen_simplejava_SimpleVariableDeclaration_SimpleStatement = Generalization(general=SimpleStatement, specific=simplejava_SimpleVariableDeclaration)
gen_simplejava_VariableDeclaration_Statement = Generalization(general=Statement, specific=simplejava_VariableDeclaration)
gen_simplejava_VariableDeclaration_SimpleVariableDeclaration = Generalization(general=SimpleVariableDeclaration, specific=simplejava_VariableDeclaration)
gen_simplejava_ForStatement_Statement = Generalization(general=Statement, specific=simplejava_ForStatement)
gen_simplejava_ForInStatement_Statement = Generalization(general=Statement, specific=simplejava_ForInStatement)
gen_simplejava_Assignment_SimpleStatement = Generalization(general=SimpleStatement, specific=simplejava_Assignment)
gen_simplejava_Assignment_Statement = Generalization(general=Statement, specific=simplejava_Assignment)
gen_simplejava_IfStatement_Statement = Generalization(general=Statement, specific=simplejava_IfStatement)
gen_simplejava_ReturnStatement_Statement = Generalization(general=Statement, specific=simplejava_ReturnStatement)
gen_simplejava_MethodCall_Statement = Generalization(general=Statement, specific=simplejava_MethodCall)
gen_simplejava_MethodCall_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_MethodCall)
gen_simplejava_WhileStatement_Statement = Generalization(general=Statement, specific=simplejava_WhileStatement)
gen_simplejava_UnaryExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_UnaryExpression)
gen_simplejava_VariableExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_VariableExpression)
gen_simplejava_ParanthesisOrBinaryExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_ParanthesisOrBinaryExpression)
gen_simplejava_ConstantExpression_GenericExpression = Generalization(general=GenericExpression, specific=simplejava_ConstantExpression)
gen_simplejava_NullExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_NullExpression)
gen_simplejava_IntegerExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_IntegerExpression)
gen_simplejava_BooleanExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_BooleanExpression)
gen_simplejava_StringExpression_ConstantExpression = Generalization(general=ConstantExpression, specific=simplejava_StringExpression)

# Domain Model
domain_model = DomainModel(
    name="simplejava",
    types={simplejava_Parameter, simplejava_Method, simplejava_Type, simplejava_SimpleJava, simplejava_PackageDeclaration, simplejava_Import, simplejava_ClassDeclaration, Statement, simplejava_Statement, simplejava_SimpleStatement, simplejava_SimpleVariableDeclaration, SimpleStatement, simplejava_VariableDeclaration, SimpleVariableDeclaration, simplejava_GenericExpression, simplejava_Assignment, simplejava_MethodBlock, simplejava_ForStatement, simplejava_ForInStatement, simplejava_IfStatement, simplejava_ParanthesisOrBinaryExpression, simplejava_ReturnStatement, simplejava_MethodCall, GenericExpression, simplejava_WhileStatement, simplejava_UnaryExpression, simplejava_VariableExpression, simplejava_ConstantExpression, simplejava_NullExpression, ConstantExpression, simplejava_IntegerExpression, simplejava_BooleanExpression, simplejava_StringExpression},
    associations={attribute5, method7, type9, package0, imports1, clazz3, statements22, parameter24, expression26, typeRef11, returnType14, parameter17, content20, then34, else37, init40, condition41, continuation44, body47, parameter28, expression30, condition33, body60, expression63, object65, method67, parameter70, subparameter50, expression52, body55, condition58, source73, variable75, source77, argument80},
    generalizations={gen_simplejava_MethodBlock_Statement, gen_simplejava_SimpleVariableDeclaration_SimpleStatement, gen_simplejava_VariableDeclaration_Statement, gen_simplejava_VariableDeclaration_SimpleVariableDeclaration, gen_simplejava_ForStatement_Statement, gen_simplejava_ForInStatement_Statement, gen_simplejava_Assignment_SimpleStatement, gen_simplejava_Assignment_Statement, gen_simplejava_IfStatement_Statement, gen_simplejava_ReturnStatement_Statement, gen_simplejava_MethodCall_Statement, gen_simplejava_MethodCall_GenericExpression, gen_simplejava_WhileStatement_Statement, gen_simplejava_UnaryExpression_GenericExpression, gen_simplejava_VariableExpression_GenericExpression, gen_simplejava_ParanthesisOrBinaryExpression_GenericExpression, gen_simplejava_ConstantExpression_GenericExpression, gen_simplejava_NullExpression_ConstantExpression, gen_simplejava_IntegerExpression_ConstantExpression, gen_simplejava_BooleanExpression_ConstantExpression, gen_simplejava_StringExpression_ConstantExpression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)