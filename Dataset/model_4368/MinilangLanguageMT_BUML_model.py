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
minilang_Line = Class(name="minilang_Line")
minilang_Program = Class(name="minilang_Program")
minilang_Method = Class(name="minilang_Method")
minilang_Variable = Class(name="minilang_Variable")
minilang_Constant = Class(name="minilang_Constant")
Value = Class(name="Value")
minilang_VariableRef = Class(name="minilang_VariableRef")
minilang_Block = Class(name="minilang_Block")
minilang_Statement = Class(name="minilang_Statement", is_abstract=True)
minilang_IfStmt = Class(name="minilang_IfStmt")
Statement = Class(name="Statement")
minilang_Condition = Class(name="minilang_Condition", is_abstract=True)
minilang_GreaterThan = Class(name="minilang_GreaterThan")
Condition = Class(name="Condition")
minilang_Value = Class(name="minilang_Value", is_abstract=True)
minilang_VariableAffect = Class(name="minilang_VariableAffect")
minilang_Sum = Class(name="minilang_Sum")
BinaryOperation = Class(name="BinaryOperation")
minilang_Modulo = Class(name="minilang_Modulo")
minilang_BinaryOperation = Class(name="minilang_BinaryOperation", is_abstract=True)
minilang_CallMethod = Class(name="minilang_CallMethod")
minilang_Move = Class(name="minilang_Move")
minilang_RotateRight = Class(name="minilang_RotateRight")
minilang_RotateLeft = Class(name="minilang_RotateLeft")

# minilang_Line class attributes and methods
minilang_Line_x1: Property = Property(name="x1", type=FloatType)
minilang_Line_y1: Property = Property(name="y1", type=FloatType)
minilang_Line_x2: Property = Property(name="x2", type=FloatType)
minilang_Line_y2: Property = Property(name="y2", type=FloatType)
minilang_Line.attributes={minilang_Line_y1, minilang_Line_y2, minilang_Line_x2, minilang_Line_x1}

# minilang_Program class attributes and methods
minilang_Program_distance: Property = Property(name="distance", type=FloatType)
minilang_Program_x: Property = Property(name="x", type=FloatType)
minilang_Program_y: Property = Property(name="y", type=FloatType)
minilang_Program_angle: Property = Property(name="angle", type=StringType)
minilang_Program_m_mainK3: Method = Method(name="mainK3", parameters={})
minilang_Program.attributes={minilang_Program_y, minilang_Program_distance, minilang_Program_x, minilang_Program_angle}
minilang_Program.methods={minilang_Program_m_mainK3}

# minilang_Method class attributes and methods
minilang_Method_name: Property = Property(name="name", type=StringType)
minilang_Method_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_Method.attributes={minilang_Method_name}
minilang_Method.methods={minilang_Method_m_executeK3}

# minilang_Variable class attributes and methods
minilang_Variable_name: Property = Property(name="name", type=StringType)
minilang_Variable_value: Property = Property(name="value", type=FloatType)
minilang_Variable.attributes={minilang_Variable_value, minilang_Variable_name}

# minilang_Constant class attributes and methods
minilang_Constant_value: Property = Property(name="value", type=FloatType)
minilang_Constant_m_valueK3: Method = Method(name="valueK3", parameters={})
minilang_Constant.attributes={minilang_Constant_value}
minilang_Constant.methods={minilang_Constant_m_valueK3}

# Value class attributes and methods

# minilang_VariableRef class attributes and methods
minilang_VariableRef_m_valueK3: Method = Method(name="valueK3", parameters={})
minilang_VariableRef.methods={minilang_VariableRef_m_valueK3}

# minilang_Block class attributes and methods
minilang_Block_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_Block.methods={minilang_Block_m_executeK3}

# minilang_Statement class attributes and methods
minilang_Statement_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_Statement.methods={minilang_Statement_m_executeK3}

# minilang_IfStmt class attributes and methods
minilang_IfStmt_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_IfStmt.methods={minilang_IfStmt_m_executeK3}

# Statement class attributes and methods

# minilang_Condition class attributes and methods
minilang_Condition_m_evalK3: Method = Method(name="evalK3", parameters={})
minilang_Condition.methods={minilang_Condition_m_evalK3}

# minilang_GreaterThan class attributes and methods
minilang_GreaterThan_m_evalK3: Method = Method(name="evalK3", parameters={})
minilang_GreaterThan.methods={minilang_GreaterThan_m_evalK3}

# Condition class attributes and methods

# minilang_Value class attributes and methods
minilang_Value_m_valueK3: Method = Method(name="valueK3", parameters={})
minilang_Value.methods={minilang_Value_m_valueK3}

# minilang_VariableAffect class attributes and methods
minilang_VariableAffect_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_VariableAffect.methods={minilang_VariableAffect_m_executeK3}

# minilang_Sum class attributes and methods
minilang_Sum_m_valueK3: Method = Method(name="valueK3", parameters={})
minilang_Sum.methods={minilang_Sum_m_valueK3}

# BinaryOperation class attributes and methods

# minilang_Modulo class attributes and methods
minilang_Modulo_m_valueK3: Method = Method(name="valueK3", parameters={})
minilang_Modulo.methods={minilang_Modulo_m_valueK3}

# minilang_BinaryOperation class attributes and methods

# minilang_CallMethod class attributes and methods
minilang_CallMethod_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_CallMethod.methods={minilang_CallMethod_m_executeK3}

# minilang_Move class attributes and methods
minilang_Move_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_Move.methods={minilang_Move_m_executeK3}

# minilang_RotateRight class attributes and methods
minilang_RotateRight_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_RotateRight.methods={minilang_RotateRight_m_executeK3}

# minilang_RotateLeft class attributes and methods
minilang_RotateLeft_m_executeK3: Method = Method(name="executeK3", parameters={})
minilang_RotateLeft.methods={minilang_RotateLeft_m_executeK3}

# Relationships
lines4: BinaryAssociation = BinaryAssociation(
    name="lines4",
    ends={
        Property(name="minilang_Line", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program5", type=minilang_Line, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="Method", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="program", type=minilang_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mainMethod1: BinaryAssociation = BinaryAssociation(
    name="mainMethod1",
    ends={
        Property(name="minilang_Method", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program", type=minilang_Method, multiplicity=Multiplicity(1, 1))
    }
)
variables2: BinaryAssociation = BinaryAssociation(
    name="variables2",
    ends={
        Property(name="minilang_Variable", type=minilang_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Program3", type=minilang_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
program6: BinaryAssociation = BinaryAssociation(
    name="program6",
    ends={
        Property(name="Program", type=minilang_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=minilang_Program, multiplicity=Multiplicity(1, 1))
    }
)
block7: BinaryAssociation = BinaryAssociation(
    name="block7",
    ends={
        Property(name="minilang_Block", type=minilang_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Method8", type=minilang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements9: BinaryAssociation = BinaryAssociation(
    name="statements9",
    ends={
        Property(name="minilang_Statement", type=minilang_Block, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_Block10", type=minilang_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenBranch11: BinaryAssociation = BinaryAssociation(
    name="thenBranch11",
    ends={
        Property(name="minilang_Block12", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt", type=minilang_Block, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
elseBranch13: BinaryAssociation = BinaryAssociation(
    name="elseBranch13",
    ends={
        Property(name="minilang_Block15", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt14", type=minilang_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition16: BinaryAssociation = BinaryAssociation(
    name="condition16",
    ends={
        Property(name="minilang_Condition", type=minilang_IfStmt, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_IfStmt17", type=minilang_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left18: BinaryAssociation = BinaryAssociation(
    name="left18",
    ends={
        Property(name="minilang_Value", type=minilang_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_GreaterThan", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="minilang_Value21", type=minilang_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_GreaterThan20", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
variable22: BinaryAssociation = BinaryAssociation(
    name="variable22",
    ends={
        Property(name="minilang_Variable23", type=minilang_VariableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableRef", type=minilang_Variable, multiplicity=Multiplicity(1, 1))
    }
)
variable24: BinaryAssociation = BinaryAssociation(
    name="variable24",
    ends={
        Property(name="minilang_Variable25", type=minilang_VariableAffect, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableAffect", type=minilang_Variable, multiplicity=Multiplicity(1, 1))
    }
)
value26: BinaryAssociation = BinaryAssociation(
    name="value26",
    ends={
        Property(name="minilang_Value28", type=minilang_VariableAffect, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_VariableAffect27", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right29: BinaryAssociation = BinaryAssociation(
    name="right29",
    ends={
        Property(name="minilang_Value30", type=minilang_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BinaryOperation", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left31: BinaryAssociation = BinaryAssociation(
    name="left31",
    ends={
        Property(name="minilang_Value33", type=minilang_BinaryOperation, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_BinaryOperation32", type=minilang_Value, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
method34: BinaryAssociation = BinaryAssociation(
    name="method34",
    ends={
        Property(name="minilang_Method35", type=minilang_CallMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="minilang_CallMethod", type=minilang_Method, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_minilang_Constant_Value = Generalization(general=Value, specific=minilang_Constant)
gen_minilang_VariableRef_Value = Generalization(general=Value, specific=minilang_VariableRef)
gen_minilang_IfStmt_Statement = Generalization(general=Statement, specific=minilang_IfStmt)
gen_minilang_GreaterThan_Condition = Generalization(general=Condition, specific=minilang_GreaterThan)
gen_minilang_VariableAffect_Statement = Generalization(general=Statement, specific=minilang_VariableAffect)
gen_minilang_Sum_BinaryOperation = Generalization(general=BinaryOperation, specific=minilang_Sum)
gen_minilang_Modulo_BinaryOperation = Generalization(general=BinaryOperation, specific=minilang_Modulo)
gen_minilang_BinaryOperation_Value = Generalization(general=Value, specific=minilang_BinaryOperation)
gen_minilang_CallMethod_Statement = Generalization(general=Statement, specific=minilang_CallMethod)
gen_minilang_Move_Statement = Generalization(general=Statement, specific=minilang_Move)
gen_minilang_RotateRight_Statement = Generalization(general=Statement, specific=minilang_RotateRight)
gen_minilang_RotateLeft_Statement = Generalization(general=Statement, specific=minilang_RotateLeft)

# Domain Model
domain_model = DomainModel(
    name="minilang",
    types={minilang_Line, minilang_Program, minilang_Method, minilang_Variable, minilang_Constant, Value, minilang_VariableRef, minilang_Block, minilang_Statement, minilang_IfStmt, Statement, minilang_Condition, minilang_GreaterThan, Condition, minilang_Value, minilang_VariableAffect, minilang_Sum, BinaryOperation, minilang_Modulo, minilang_BinaryOperation, minilang_CallMethod, minilang_Move, minilang_RotateRight, minilang_RotateLeft, Cardinals},
    associations={lines4, methods0, mainMethod1, variables2, program6, block7, statements9, thenBranch11, elseBranch13, condition16, left18, right19, variable22, variable24, value26, right29, left31, method34},
    generalizations={gen_minilang_Constant_Value, gen_minilang_VariableRef_Value, gen_minilang_IfStmt_Statement, gen_minilang_GreaterThan_Condition, gen_minilang_VariableAffect_Statement, gen_minilang_Sum_BinaryOperation, gen_minilang_Modulo_BinaryOperation, gen_minilang_BinaryOperation_Value, gen_minilang_CallMethod_Statement, gen_minilang_Move_Statement, gen_minilang_RotateRight_Statement, gen_minilang_RotateLeft_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)