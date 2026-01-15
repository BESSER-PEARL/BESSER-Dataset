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

# Enumerations
ArithmeticOperator: Enumeration = Enumeration(
    name="ArithmeticOperator",
    literals={
            EnumerationLiteral(name="plus"),
			EnumerationLiteral(name="minus"),
			EnumerationLiteral(name="mult"),
			EnumerationLiteral(name="div")
    }
)

BooleanOperator: Enumeration = Enumeration(
    name="BooleanOperator",
    literals={
            EnumerationLiteral(name="equal"),
			EnumerationLiteral(name="diff"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="lowerThan")
    }
)

# Classes
Logo_LogoProgram = Class(name="Logo::LogoProgram")
Logo_Right = Class(name="Logo::Right")
Logo_Literal = Class(name="Logo::Literal", is_abstract=True)
Expression = Class(name="Expression")
Logo_Integer = Class(name="Logo::Integer")
Literal = Class(name="Literal")
Logo_Void = Class(name="Logo::Void")
Logo_Double = Class(name="Logo::Double")
Logo_String = Class(name="Logo::String")
Logo_Boolean = Class(name="Logo::Boolean")
Logo_VarDecl = Class(name="Logo::VarDecl")
Logo_VarReference = Class(name="Logo::VarReference")
Logo_Instruction = Class(name="Logo::Instruction", is_abstract=True)
Logo_Primitive = Class(name="Logo::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
Logo_Forward = Class(name="Logo::Forward")
Primitive = Class(name="Primitive")
Logo_Expression = Class(name="Logo::Expression", is_abstract=True)
Logo_Back = Class(name="Logo::Back")
Logo_Left = Class(name="Logo::Left")
Logo_BinaryExpr = Class(name="Logo::BinaryExpr", is_abstract=True)
Logo_ArithmeticExpr = Class(name="Logo::ArithmeticExpr")
BinaryExpr = Class(name="BinaryExpr")
Logo_BooleanExpr = Class(name="Logo::BooleanExpr")
Logo_Procedure = Class(name="Logo::Procedure")
Logo_ProcedureCall = Class(name="Logo::ProcedureCall")
Logo_ControlStructure = Class(name="Logo::ControlStructure", is_abstract=True)
Logo_If = Class(name="Logo::If")
ControlStructure = Class(name="ControlStructure")
Logo_Block = Class(name="Logo::Block")
Logo_While = Class(name="Logo::While")
Logo_Assignation = Class(name="Logo::Assignation")

# Logo_LogoProgram class attributes and methods

# Logo_Right class attributes and methods

# Logo_Literal class attributes and methods

# Expression class attributes and methods

# Logo_Integer class attributes and methods
Logo_Integer_value: Property = Property(name="value", type=IntegerType)
Logo_Integer.attributes={Logo_Integer_value}

# Literal class attributes and methods

# Logo_Void class attributes and methods

# Logo_Double class attributes and methods
Logo_Double_value: Property = Property(name="value", type=FloatType)
Logo_Double.attributes={Logo_Double_value}

# Logo_String class attributes and methods
Logo_String_value: Property = Property(name="value", type=StringType)
Logo_String.attributes={Logo_String_value}

# Logo_Boolean class attributes and methods
Logo_Boolean_value: Property = Property(name="value", type=BooleanType)
Logo_Boolean.attributes={Logo_Boolean_value}

# Logo_VarDecl class attributes and methods
Logo_VarDecl_name: Property = Property(name="name", type=StringType)
Logo_VarDecl.attributes={Logo_VarDecl_name}

# Logo_VarReference class attributes and methods

# Logo_Instruction class attributes and methods

# Logo_Primitive class attributes and methods

# Instruction class attributes and methods

# Logo_Forward class attributes and methods

# Primitive class attributes and methods

# Logo_Expression class attributes and methods

# Logo_Back class attributes and methods

# Logo_Left class attributes and methods

# Logo_BinaryExpr class attributes and methods

# Logo_ArithmeticExpr class attributes and methods
Logo_ArithmeticExpr_operator: Property = Property(name="operator", type=StringType)
Logo_ArithmeticExpr.attributes={Logo_ArithmeticExpr_operator}

# BinaryExpr class attributes and methods

# Logo_BooleanExpr class attributes and methods
Logo_BooleanExpr_operator: Property = Property(name="operator", type=StringType)
Logo_BooleanExpr.attributes={Logo_BooleanExpr_operator}

# Logo_Procedure class attributes and methods
Logo_Procedure_name: Property = Property(name="name", type=StringType)
Logo_Procedure.attributes={Logo_Procedure_name}

# Logo_ProcedureCall class attributes and methods

# Logo_ControlStructure class attributes and methods

# Logo_If class attributes and methods

# ControlStructure class attributes and methods

# Logo_Block class attributes and methods

# Logo_While class attributes and methods

# Logo_Assignation class attributes and methods

# Relationships
angle4: BinaryAssociation = BinaryAssociation(
    name="angle4",
    ends={
        Property(name="Logo_Expression5", type=Logo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Left", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="Logo_Expression7", type=Logo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Right", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expr8: BinaryAssociation = BinaryAssociation(
    name="expr8",
    ends={
        Property(name="Logo_Expression9", type=Logo_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_VarDecl", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref10: BinaryAssociation = BinaryAssociation(
    name="ref10",
    ends={
        Property(name="Logo_VarDecl11", type=Logo_VarReference, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_VarReference", type=Logo_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
instructions0: BinaryAssociation = BinaryAssociation(
    name="instructions0",
    ends={
        Property(name="Logo_Instruction", type=Logo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_LogoProgram", type=Logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps1: BinaryAssociation = BinaryAssociation(
    name="steps1",
    ends={
        Property(name="Logo_Expression", type=Logo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Forward", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps2: BinaryAssociation = BinaryAssociation(
    name="steps2",
    ends={
        Property(name="Logo_Expression3", type=Logo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Back", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftExpr24: BinaryAssociation = BinaryAssociation(
    name="leftExpr24",
    ends={
        Property(name="Logo_Expression25", type=Logo_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_BinaryExpr", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rightExpr26: BinaryAssociation = BinaryAssociation(
    name="rightExpr26",
    ends={
        Property(name="Logo_Expression28", type=Logo_BinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_BinaryExpr27", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body29: BinaryAssociation = BinaryAssociation(
    name="body29",
    ends={
        Property(name="Logo_Block30", type=Logo_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Procedure", type=Logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
returnType31: BinaryAssociation = BinaryAssociation(
    name="returnType31",
    ends={
        Property(name="Logo_Literal", type=Logo_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Procedure32", type=Logo_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ref33: BinaryAssociation = BinaryAssociation(
    name="ref33",
    ends={
        Property(name="Logo_Procedure34", type=Logo_ProcedureCall, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_ProcedureCall", type=Logo_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
body12: BinaryAssociation = BinaryAssociation(
    name="body12",
    ends={
        Property(name="Logo_Block", type=Logo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_If", type=Logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition13: BinaryAssociation = BinaryAssociation(
    name="condition13",
    ends={
        Property(name="Logo_Expression15", type=Logo_If, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_If14", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
instructions16: BinaryAssociation = BinaryAssociation(
    name="instructions16",
    ends={
        Property(name="Logo_Instruction18", type=Logo_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Block17", type=Logo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
body19: BinaryAssociation = BinaryAssociation(
    name="body19",
    ends={
        Property(name="Logo_Block20", type=Logo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_While", type=Logo_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard21: BinaryAssociation = BinaryAssociation(
    name="guard21",
    ends={
        Property(name="Logo_Expression23", type=Logo_While, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_While22", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
ref35: BinaryAssociation = BinaryAssociation(
    name="ref35",
    ends={
        Property(name="Logo_VarDecl36", type=Logo_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Assignation", type=Logo_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expr37: BinaryAssociation = BinaryAssociation(
    name="expr37",
    ends={
        Property(name="Logo_Expression39", type=Logo_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="Logo_Assignation38", type=Logo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_Logo_Right_Primitive = Generalization(general=Primitive, specific=Logo_Right)
gen_Logo_Expression_Instruction = Generalization(general=Instruction, specific=Logo_Expression)
gen_Logo_Literal_Expression = Generalization(general=Expression, specific=Logo_Literal)
gen_Logo_Integer_Literal = Generalization(general=Literal, specific=Logo_Integer)
gen_Logo_Void_Literal = Generalization(general=Literal, specific=Logo_Void)
gen_Logo_Double_Literal = Generalization(general=Literal, specific=Logo_Double)
gen_Logo_String_Literal = Generalization(general=Literal, specific=Logo_String)
gen_Logo_Boolean_Literal = Generalization(general=Literal, specific=Logo_Boolean)
gen_Logo_VarDecl_Instruction = Generalization(general=Instruction, specific=Logo_VarDecl)
gen_Logo_VarReference_Expression = Generalization(general=Expression, specific=Logo_VarReference)
gen_Logo_Primitive_Instruction = Generalization(general=Instruction, specific=Logo_Primitive)
gen_Logo_Forward_Primitive = Generalization(general=Primitive, specific=Logo_Forward)
gen_Logo_Back_Primitive = Generalization(general=Primitive, specific=Logo_Back)
gen_Logo_Left_Primitive = Generalization(general=Primitive, specific=Logo_Left)
gen_Logo_BinaryExpr_Expression = Generalization(general=Expression, specific=Logo_BinaryExpr)
gen_Logo_ArithmeticExpr_BinaryExpr = Generalization(general=BinaryExpr, specific=Logo_ArithmeticExpr)
gen_Logo_BooleanExpr_BinaryExpr = Generalization(general=BinaryExpr, specific=Logo_BooleanExpr)
gen_Logo_Procedure_Instruction = Generalization(general=Instruction, specific=Logo_Procedure)
gen_Logo_ProcedureCall_Expression = Generalization(general=Expression, specific=Logo_ProcedureCall)
gen_Logo_ControlStructure_Instruction = Generalization(general=Instruction, specific=Logo_ControlStructure)
gen_Logo_If_ControlStructure = Generalization(general=ControlStructure, specific=Logo_If)
gen_Logo_Block_ControlStructure = Generalization(general=ControlStructure, specific=Logo_Block)
gen_Logo_While_ControlStructure = Generalization(general=ControlStructure, specific=Logo_While)
gen_Logo_Assignation_Instruction = Generalization(general=Instruction, specific=Logo_Assignation)

# Domain Model
domain_model = DomainModel(
    name="Logo",
    types={Logo_LogoProgram, Logo_Right, Logo_Literal, Expression, Logo_Integer, Literal, Logo_Void, Logo_Double, Logo_String, Logo_Boolean, Logo_VarDecl, Logo_VarReference, Logo_Instruction, Logo_Primitive, Instruction, Logo_Forward, Primitive, Logo_Expression, Logo_Back, Logo_Left, Logo_BinaryExpr, Logo_ArithmeticExpr, BinaryExpr, Logo_BooleanExpr, Logo_Procedure, Logo_ProcedureCall, Logo_ControlStructure, Logo_If, ControlStructure, Logo_Block, Logo_While, Logo_Assignation, ArithmeticOperator, BooleanOperator},
    associations={angle4, angle6, expr8, ref10, instructions0, steps1, steps2, leftExpr24, rightExpr26, body29, returnType31, ref33, body12, condition13, instructions16, body19, guard21, ref35, expr37},
    generalizations={gen_Logo_Right_Primitive, gen_Logo_Expression_Instruction, gen_Logo_Literal_Expression, gen_Logo_Integer_Literal, gen_Logo_Void_Literal, gen_Logo_Double_Literal, gen_Logo_String_Literal, gen_Logo_Boolean_Literal, gen_Logo_VarDecl_Instruction, gen_Logo_VarReference_Expression, gen_Logo_Primitive_Instruction, gen_Logo_Forward_Primitive, gen_Logo_Back_Primitive, gen_Logo_Left_Primitive, gen_Logo_BinaryExpr_Expression, gen_Logo_ArithmeticExpr_BinaryExpr, gen_Logo_BooleanExpr_BinaryExpr, gen_Logo_Procedure_Instruction, gen_Logo_ProcedureCall_Expression, gen_Logo_ControlStructure_Instruction, gen_Logo_If_ControlStructure, gen_Logo_Block_ControlStructure, gen_Logo_While_ControlStructure, gen_Logo_Assignation_Instruction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)