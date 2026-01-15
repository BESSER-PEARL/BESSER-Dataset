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

RelationalOperator: Enumeration = Enumeration(
    name="RelationalOperator",
    literals={
            EnumerationLiteral(name="lessThan"),
			EnumerationLiteral(name="greaterThan"),
			EnumerationLiteral(name="equals"),
			EnumerationLiteral(name="notEqual"),
			EnumerationLiteral(name="lessThanOrEqualTo"),
			EnumerationLiteral(name="greaterThanOrEqualTo")
    }
)

# Classes
kmLogo_LogoProgram = Class(name="kmLogo::LogoProgram")
kmLogo_VarDecl = Class(name="kmLogo::VarDecl")
kmLogo_Instruction = Class(name="kmLogo::Instruction", is_abstract=True)
kmLogo_Primitive = Class(name="kmLogo::Primitive", is_abstract=True)
Instruction = Class(name="Instruction")
kmLogo_Back = Class(name="kmLogo::Back")
Primitive = Class(name="Primitive")
kmLogo_Expression = Class(name="kmLogo::Expression", is_abstract=True)
kmLogo_Forward = Class(name="kmLogo::Forward")
kmLogo_Left = Class(name="kmLogo::Left")
kmLogo_Right = Class(name="kmLogo::Right")
kmLogo_PenDown = Class(name="kmLogo::PenDown")
kmLogo_PenUp = Class(name="kmLogo::PenUp")
kmLogo_Clear = Class(name="kmLogo::Clear")
kmLogo_Literal = Class(name="kmLogo::Literal")
Expression = Class(name="Expression")
kmLogo_IntegerLit = Class(name="kmLogo::IntegerLit")
Literal = Class(name="Literal")
kmLogo_StringLit = Class(name="kmLogo::StringLit")
kmLogo_RelationalExpression = Class(name="kmLogo::RelationalExpression")
kmLogo_VarReference = Class(name="kmLogo::VarReference")
kmLogo_BoolLit = Class(name="kmLogo::BoolLit")
kmLogo_ArithmeticExpression = Class(name="kmLogo::ArithmeticExpression")

# kmLogo_LogoProgram class attributes and methods

# kmLogo_VarDecl class attributes and methods
kmLogo_VarDecl_key: Property = Property(name="key", type=StringType)
kmLogo_VarDecl.attributes={kmLogo_VarDecl_key}

# kmLogo_Instruction class attributes and methods

# kmLogo_Primitive class attributes and methods

# Instruction class attributes and methods

# kmLogo_Back class attributes and methods

# Primitive class attributes and methods

# kmLogo_Expression class attributes and methods

# kmLogo_Forward class attributes and methods

# kmLogo_Left class attributes and methods

# kmLogo_Right class attributes and methods

# kmLogo_PenDown class attributes and methods

# kmLogo_PenUp class attributes and methods

# kmLogo_Clear class attributes and methods

# kmLogo_Literal class attributes and methods

# Expression class attributes and methods

# kmLogo_IntegerLit class attributes and methods
kmLogo_IntegerLit_value: Property = Property(name="value", type=IntegerType)
kmLogo_IntegerLit.attributes={kmLogo_IntegerLit_value}

# Literal class attributes and methods

# kmLogo_StringLit class attributes and methods
kmLogo_StringLit_value: Property = Property(name="value", type=StringType)
kmLogo_StringLit.attributes={kmLogo_StringLit_value}

# kmLogo_RelationalExpression class attributes and methods
kmLogo_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
kmLogo_RelationalExpression.attributes={kmLogo_RelationalExpression_operator}

# kmLogo_VarReference class attributes and methods
kmLogo_VarReference_key: Property = Property(name="key", type=StringType)
kmLogo_VarReference.attributes={kmLogo_VarReference_key}

# kmLogo_BoolLit class attributes and methods
kmLogo_BoolLit_value: Property = Property(name="value", type=BooleanType)
kmLogo_BoolLit.attributes={kmLogo_BoolLit_value}

# kmLogo_ArithmeticExpression class attributes and methods
kmLogo_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
kmLogo_ArithmeticExpression.attributes={kmLogo_ArithmeticExpression_operator}

# Relationships
variables0: BinaryAssociation = BinaryAssociation(
    name="variables0",
    ends={
        Property(name="kmLogo_VarDecl", type=kmLogo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_LogoProgram", type=kmLogo_VarDecl, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
instructions1: BinaryAssociation = BinaryAssociation(
    name="instructions1",
    ends={
        Property(name="kmLogo_Instruction", type=kmLogo_LogoProgram, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_LogoProgram2", type=kmLogo_Instruction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
steps3: BinaryAssociation = BinaryAssociation(
    name="steps3",
    ends={
        Property(name="kmLogo_Expression", type=kmLogo_Back, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Back", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
steps4: BinaryAssociation = BinaryAssociation(
    name="steps4",
    ends={
        Property(name="kmLogo_Expression5", type=kmLogo_Forward, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Forward", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
angle6: BinaryAssociation = BinaryAssociation(
    name="angle6",
    ends={
        Property(name="kmLogo_Expression7", type=kmLogo_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Left", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
angle8: BinaryAssociation = BinaryAssociation(
    name="angle8",
    ends={
        Property(name="kmLogo_Expression9", type=kmLogo_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_Right", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left15: BinaryAssociation = BinaryAssociation(
    name="left15",
    ends={
        Property(name="kmLogo_Expression16", type=kmLogo_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_RelationalExpression", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right17: BinaryAssociation = BinaryAssociation(
    name="right17",
    ends={
        Property(name="kmLogo_Expression19", type=kmLogo_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_RelationalExpression18", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression20: BinaryAssociation = BinaryAssociation(
    name="expression20",
    ends={
        Property(name="kmLogo_Expression22", type=kmLogo_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_VarDecl21", type=kmLogo_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left10: BinaryAssociation = BinaryAssociation(
    name="left10",
    ends={
        Property(name="kmLogo_Expression11", type=kmLogo_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ArithmeticExpression", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right12: BinaryAssociation = BinaryAssociation(
    name="right12",
    ends={
        Property(name="kmLogo_Expression14", type=kmLogo_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="kmLogo_ArithmeticExpression13", type=kmLogo_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_kmLogo_Primitive_Instruction = Generalization(general=Instruction, specific=kmLogo_Primitive)
gen_kmLogo_Back_Primitive = Generalization(general=Primitive, specific=kmLogo_Back)
gen_kmLogo_Forward_Primitive = Generalization(general=Primitive, specific=kmLogo_Forward)
gen_kmLogo_Left_Primitive = Generalization(general=Primitive, specific=kmLogo_Left)
gen_kmLogo_Right_Primitive = Generalization(general=Primitive, specific=kmLogo_Right)
gen_kmLogo_PenDown_Primitive = Generalization(general=Primitive, specific=kmLogo_PenDown)
gen_kmLogo_PenUp_Primitive = Generalization(general=Primitive, specific=kmLogo_PenUp)
gen_kmLogo_Clear_Primitive = Generalization(general=Primitive, specific=kmLogo_Clear)
gen_kmLogo_Literal_Expression = Generalization(general=Expression, specific=kmLogo_Literal)
gen_kmLogo_IntegerLit_Literal = Generalization(general=Literal, specific=kmLogo_IntegerLit)
gen_kmLogo_StringLit_Literal = Generalization(general=Literal, specific=kmLogo_StringLit)
gen_kmLogo_RelationalExpression_Expression = Generalization(general=Expression, specific=kmLogo_RelationalExpression)
gen_kmLogo_VarReference_Expression = Generalization(general=Expression, specific=kmLogo_VarReference)
gen_kmLogo_VarDecl_Instruction = Generalization(general=Instruction, specific=kmLogo_VarDecl)
gen_kmLogo_BoolLit_Literal = Generalization(general=Literal, specific=kmLogo_BoolLit)
gen_kmLogo_ArithmeticExpression_Expression = Generalization(general=Expression, specific=kmLogo_ArithmeticExpression)

# Domain Model
domain_model = DomainModel(
    name="kmLogo",
    types={kmLogo_LogoProgram, kmLogo_VarDecl, kmLogo_Instruction, kmLogo_Primitive, Instruction, kmLogo_Back, Primitive, kmLogo_Expression, kmLogo_Forward, kmLogo_Left, kmLogo_Right, kmLogo_PenDown, kmLogo_PenUp, kmLogo_Clear, kmLogo_Literal, Expression, kmLogo_IntegerLit, Literal, kmLogo_StringLit, kmLogo_RelationalExpression, kmLogo_VarReference, kmLogo_BoolLit, kmLogo_ArithmeticExpression, ArithmeticOperator, RelationalOperator},
    associations={variables0, instructions1, steps3, steps4, angle6, angle8, left15, right17, expression20, left10, right12},
    generalizations={gen_kmLogo_Primitive_Instruction, gen_kmLogo_Back_Primitive, gen_kmLogo_Forward_Primitive, gen_kmLogo_Left_Primitive, gen_kmLogo_Right_Primitive, gen_kmLogo_PenDown_Primitive, gen_kmLogo_PenUp_Primitive, gen_kmLogo_Clear_Primitive, gen_kmLogo_Literal_Expression, gen_kmLogo_IntegerLit_Literal, gen_kmLogo_StringLit_Literal, gen_kmLogo_RelationalExpression_Expression, gen_kmLogo_VarReference_Expression, gen_kmLogo_VarDecl_Instruction, gen_kmLogo_BoolLit_Literal, gen_kmLogo_ArithmeticExpression_Expression},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)