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
Cardinals: Enumeration = Enumeration(
    name="Cardinals",
    literals={
            EnumerationLiteral(name="NORTH"),
			EnumerationLiteral(name="EAST"),
			EnumerationLiteral(name="SOUTH"),
			EnumerationLiteral(name="WEST")
    }
)

# Classes
minilang_Program = Class(name="minilang::Program")
minilang_Method = Class(name="minilang::Method")
minilang_Variable = Class(name="minilang::Variable")
minilang_Line = Class(name="minilang::Line")
minilang_Condition = Class(name="minilang::Condition", is_abstract=True)
minilang_GreaterThan = Class(name="minilang::GreaterThan")
Condition = Class(name="Condition")
minilang_Value = Class(name="minilang::Value", is_abstract=True)
minilang_Constant = Class(name="minilang::Constant")
Value = Class(name="Value")
minilang_VariableRef = Class(name="minilang::VariableRef")
minilang_VariableAffect = Class(name="minilang::VariableAffect")
minilang_Sum = Class(name="minilang::Sum")
BinaryOperation = Class(name="BinaryOperation")
minilang_Modulo = Class(name="minilang::Modulo")
minilang_BinaryOperation = Class(name="minilang::BinaryOperation", is_abstract=True)
minilang_Block = Class(name="minilang::Block")
minilang_Statement = Class(name="minilang::Statement", is_abstract=True)
minilang_IfStmt = Class(name="minilang::IfStmt")
Statement = Class(name="Statement")
minilang_CallMethod = Class(name="minilang::CallMethod")
minilang_Move = Class(name="minilang::Move")
minilang_RotateRight = Class(name="minilang::RotateRight")
minilang_RotateLeft = Class(name="minilang::RotateLeft")

# minilang_Program class attributes and methods
minilang_Program_x: Property = Property(name="x", type=FloatType)
minilang_Program_y: Property = Property(name="y", type=FloatType)
minilang_Program_angle: Property = Property(name="angle", type=StringType)
minilang_Program_distance: Property = Property(name="distance", type=FloatType)
minilang_Program.attributes={minilang_Program_angle, minilang_Program_x, minilang_Program_y, minilang_Program_distance}

# minilang_Method class attributes and methods
minilang_Method_name: Property = Property(name="name", type=StringType)
minilang_Method.attributes={minilang_Method_name}

# minilang_Variable class attributes and methods
minilang_Variable_name: Property = Property(name="name", type=StringType)
minilang_Variable_value: Property = Property(name="value", type=FloatType)
minilang_Variable.attributes={minilang_Variable_name, minilang_Variable_value}

# minilang_Line class attributes and methods
minilang_Line_y2: Property = Property(name="y2", type=FloatType)
minilang_Line_x1: Property = Property(name="x1", type=FloatType)
minilang_Line_y1: Property = Property(name="y1", type=FloatType)
minilang_Line_x2: Property = Property(name="x2", type=FloatType)
minilang_Line.attributes={minilang_Line_x1, minilang_Line_y2, minilang_Line_y1, minilang_Line_x2}

# minilang_Condition class attributes and methods

# minilang_GreaterThan class attributes and methods

# Condition class attributes and methods

# minilang_Value class attributes and methods

# minilang_Constant class attributes and methods
minilang_Constant_value: Property = Property(name="value", type=FloatType)
minilang_Constant.attributes={minilang_Constant_value}

# Value class attributes and methods

# minilang_VariableRef class attributes and methods

# minilang_VariableAffect class attributes and methods

# minilang_Sum class attributes and methods

# BinaryOperation class attributes and methods

# minilang_Modulo class attributes and methods

# minilang_BinaryOperation class attributes and methods

# minilang_Block class attributes and methods

# minilang_Statement class attributes and methods

# minilang_IfStmt class attributes and methods

# Statement class attributes and methods

# minilang_CallMethod class attributes and methods

# minilang_Move class attributes and methods

# minilang_RotateRight class attributes and methods

# minilang_RotateLeft class attributes and methods

# Relationships
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="1", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=minilang_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainMethod2: BinaryAssociation = BinaryAssociation(
    name="mainMethod2",
    ends={
        Property(name="minilang_Method", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program", type=minilang_Method, multiplicity=Multiplicity(1, 1))
    }
)
variables3: BinaryAssociation = BinaryAssociation(
    name="variables3",
    ends={
        Property(name="minilang_Variable", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program4", type=minilang_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lines5: BinaryAssociation = BinaryAssociation(
    name="lines5",
    ends={
        Property(name="minilang_Line", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program6", type=minilang_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elseBranch16: BinaryAssociation = BinaryAssociation(
    name="elseBranch16",
    ends={
        Property(name="minilang_Block18", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt17", type=minilang_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition19: BinaryAssociation = BinaryAssociation(
    name="condition19",
    ends={
        Property(name="minilang_Condition", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt20", type=minilang_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left21: BinaryAssociation = BinaryAssociation(
    name="left21",
    ends={
        Property(name="minilang_Value", type=minilang_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_GreaterThan", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right22: BinaryAssociation = BinaryAssociation(
    name="right22",
    ends={
        Property(name="minilang_Value24", type=minilang_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_GreaterThan23", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable25: BinaryAssociation = BinaryAssociation(
    name="variable25",
    ends={
        Property(name="minilang_Variable26", type=minilang_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableRef", type=minilang_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variable27: BinaryAssociation = BinaryAssociation(
    name="variable27",
    ends={
        Property(name="minilang_Variable28", type=minilang_VariableAffect, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableAffect", type=minilang_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value29: BinaryAssociation = BinaryAssociation(
    name="value29",
    ends={
        Property(name="minilang_Value31", type=minilang_VariableAffect, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableAffect30", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="minilang_Value33", type=minilang_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BinaryOperation", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
program7: BinaryAssociation = BinaryAssociation(
    name="program7",
    ends={
        Property(name="9", type=minilang_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="8", type=minilang_Program, multiplicity=Multiplicity(1, 1))
    }
)
block10: BinaryAssociation = BinaryAssociation(
    name="block10",
    ends={
        Property(name="minilang_Block", type=minilang_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Method11", type=minilang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements12: BinaryAssociation = BinaryAssociation(
    name="statements12",
    ends={
        Property(name="minilang_Statement", type=minilang_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Block13", type=minilang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenBranch14: BinaryAssociation = BinaryAssociation(
    name="thenBranch14",
    ends={
        Property(name="minilang_Block15", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt", type=minilang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left34: BinaryAssociation = BinaryAssociation(
    name="left34",
    ends={
        Property(name="minilang_Value36", type=minilang_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BinaryOperation35", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method37: BinaryAssociation = BinaryAssociation(
    name="method37",
    ends={
        Property(name="minilang_Method38", type=minilang_CallMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_CallMethod", type=minilang_Method, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_minilang_GreaterThan_Condition = Generalization(general=Condition, specific=minilang_GreaterThan)
gen_minilang_Constant_Value = Generalization(general=Value, specific=minilang_Constant)
gen_minilang_VariableRef_Value = Generalization(general=Value, specific=minilang_VariableRef)
gen_minilang_VariableAffect_Statement = Generalization(general=Statement, specific=minilang_VariableAffect)
gen_minilang_Sum_BinaryOperation = Generalization(general=BinaryOperation, specific=minilang_Sum)
gen_minilang_Modulo_BinaryOperation = Generalization(general=BinaryOperation, specific=minilang_Modulo)
gen_minilang_BinaryOperation_Value = Generalization(general=Value, specific=minilang_BinaryOperation)
gen_minilang_IfStmt_Statement = Generalization(general=Statement, specific=minilang_IfStmt)
gen_minilang_CallMethod_Statement = Generalization(general=Statement, specific=minilang_CallMethod)
gen_minilang_Move_Statement = Generalization(general=Statement, specific=minilang_Move)
gen_minilang_RotateRight_Statement = Generalization(general=Statement, specific=minilang_RotateRight)
gen_minilang_RotateLeft_Statement = Generalization(general=Statement, specific=minilang_RotateLeft)

# Domain Model
domain_model = DomainModel(
    name="minilang",
    types={minilang_Program, minilang_Method, minilang_Variable, minilang_Line, minilang_Condition, minilang_GreaterThan, Condition, minilang_Value, minilang_Constant, Value, minilang_VariableRef, minilang_VariableAffect, minilang_Sum, BinaryOperation, minilang_Modulo, minilang_BinaryOperation, minilang_Block, minilang_Statement, minilang_IfStmt, Statement, minilang_CallMethod, minilang_Move, minilang_RotateRight, minilang_RotateLeft, Cardinals},
    associations={methods0, mainMethod2, variables3, lines5, elseBranch16, condition19, left21, right22, variable25, variable27, value29, right32, program7, block10, statements12, thenBranch14, left34, method37},
    generalizations={gen_minilang_GreaterThan_Condition, gen_minilang_Constant_Value, gen_minilang_VariableRef_Value, gen_minilang_VariableAffect_Statement, gen_minilang_Sum_BinaryOperation, gen_minilang_Modulo_BinaryOperation, gen_minilang_BinaryOperation_Value, gen_minilang_IfStmt_Statement, gen_minilang_CallMethod_Statement, gen_minilang_Move_Statement, gen_minilang_RotateRight_Statement, gen_minilang_RotateLeft_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)