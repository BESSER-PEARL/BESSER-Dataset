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
gseq_Operation = Class(name="gseq::Operation", is_abstract=True)
gseq_Program = Class(name="gseq::Program")
gseq_Method = Class(name="gseq::Method")
IntegerExpression = Class(name="IntegerExpression")
gseq_BooleanExpression = Class(name="gseq::BooleanExpression", is_abstract=True)
gseq_If = Class(name="gseq::If")
gseq_True = Class(name="gseq::True")
BooleanExpression = Class(name="BooleanExpression")
gseq_False = Class(name="gseq::False")
gseq_MethodCall = Class(name="gseq::MethodCall")
gseq_Print = Class(name="gseq::Print")
Operation = Class(name="Operation")
gseq_Const = Class(name="gseq::Const")
gseq_Var = Class(name="gseq::Var")
gseq_Assign = Class(name="gseq::Assign")
gseq_Plus = Class(name="gseq::Plus")
gseq_Equality = Class(name="gseq::Equality")
gseq_IntegerExpression = Class(name="gseq::IntegerExpression", is_abstract=True)
gseq_Not = Class(name="gseq::Not")
gseq_And = Class(name="gseq::And")
gseq_GreaterThan = Class(name="gseq::GreaterThan")
gseq_While = Class(name="gseq::While")

# gseq_Operation class attributes and methods
gseq_Operation_m_execute: Method = Method(name="execute", parameters={})
gseq_Operation.methods={gseq_Operation_m_execute}

# gseq_Program class attributes and methods
gseq_Program_m_init: Method = Method(name="init", parameters={})
gseq_Program.methods={gseq_Program_m_init}

# gseq_Method class attributes and methods
gseq_Method_name: Property = Property(name="name", type=StringType)
gseq_Method_m_call: Method = Method(name="call", parameters={})
gseq_Method.attributes={gseq_Method_name}
gseq_Method.methods={gseq_Method_m_call}

# IntegerExpression class attributes and methods

# gseq_BooleanExpression class attributes and methods
gseq_BooleanExpression_m_bvalue: Method = Method(name="bvalue", parameters={}, type=BooleanType)
gseq_BooleanExpression_m_pretty: Method = Method(name="pretty", parameters={}, type=StringType)
gseq_BooleanExpression.methods={gseq_BooleanExpression_m_bvalue, gseq_BooleanExpression_m_pretty}

# gseq_If class attributes and methods

# gseq_True class attributes and methods

# BooleanExpression class attributes and methods

# gseq_False class attributes and methods

# gseq_MethodCall class attributes and methods

# gseq_Print class attributes and methods
gseq_Print_m_print: Method = Method(name="print", parameters={})
gseq_Print.methods={gseq_Print_m_print}

# Operation class attributes and methods

# gseq_Const class attributes and methods
gseq_Const_value: Property = Property(name="value", type=StringType)
gseq_Const.attributes={gseq_Const_value}

# gseq_Var class attributes and methods
gseq_Var_varName: Property = Property(name="varName", type=StringType)
gseq_Var.attributes={gseq_Var_varName}

# gseq_Assign class attributes and methods
gseq_Assign_varName: Property = Property(name="varName", type=StringType)
gseq_Assign.attributes={gseq_Assign_varName}

# gseq_Plus class attributes and methods

# gseq_Equality class attributes and methods

# gseq_IntegerExpression class attributes and methods
gseq_IntegerExpression_m_ivalue: Method = Method(name="ivalue", parameters={}, type=StringType)
gseq_IntegerExpression_m_pretty: Method = Method(name="pretty", parameters={}, type=StringType)
gseq_IntegerExpression.methods={gseq_IntegerExpression_m_ivalue, gseq_IntegerExpression_m_pretty}

# gseq_Not class attributes and methods

# gseq_And class attributes and methods

# gseq_GreaterThan class attributes and methods

# gseq_While class attributes and methods

# Relationships
methods0: BinaryAssociation = BinaryAssociation(
    name="methods0",
    ends={
        Property(name="Method", type=gseq_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="inProgram", type=gseq_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
startMethod1: BinaryAssociation = BinaryAssociation(
    name="startMethod1",
    ends={
        Property(name="gseq_Method", type=gseq_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Program", type=gseq_Method, multiplicity=Multiplicity(1, 1))
    }
)
operations2: BinaryAssociation = BinaryAssociation(
    name="operations2",
    ends={
        Property(name="Operation", type=gseq_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="executedBy", type=gseq_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
toPrint7: BinaryAssociation = BinaryAssociation(
    name="toPrint7",
    ends={
        Property(name="gseq_Operation", type=gseq_Print, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Print", type=gseq_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
methodToCall8: BinaryAssociation = BinaryAssociation(
    name="methodToCall8",
    ends={
        Property(name="Method9", type=gseq_MethodCall, multiplicity=Multiplicity(1, 1)),
        Property(name="calledBy", type=gseq_Method, multiplicity=Multiplicity(1, 1))
    }
)
elseBranch10: BinaryAssociation = BinaryAssociation(
    name="elseBranch10",
    ends={
        Property(name="gseq_Operation11", type=gseq_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_If", type=gseq_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
thenBranch12: BinaryAssociation = BinaryAssociation(
    name="thenBranch12",
    ends={
        Property(name="gseq_Operation14", type=gseq_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_If13", type=gseq_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
conditionIf15: BinaryAssociation = BinaryAssociation(
    name="conditionIf15",
    ends={
        Property(name="gseq_BooleanExpression", type=gseq_If, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_If16", type=gseq_BooleanExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
inProgram3: BinaryAssociation = BinaryAssociation(
    name="inProgram3",
    ends={
        Property(name="Program", type=gseq_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methods", type=gseq_Program, multiplicity=Multiplicity(1, 1))
    }
)
calledBy4: BinaryAssociation = BinaryAssociation(
    name="calledBy4",
    ends={
        Property(name="MethodCall", type=gseq_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="methodToCall", type=gseq_MethodCall, multiplicity=Multiplicity(0, 9999))
    }
)
executedBy5: BinaryAssociation = BinaryAssociation(
    name="executedBy5",
    ends={
        Property(name="Method6", type=gseq_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="operations", type=gseq_Method, multiplicity=Multiplicity(0, 1))
    }
)
leftAnd23: BinaryAssociation = BinaryAssociation(
    name="leftAnd23",
    ends={
        Property(name="gseq_And", type=gseq_BooleanExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_BooleanExpression24", type=gseq_And, multiplicity=Multiplicity(1, 1))
    }
)
rightAnd25: BinaryAssociation = BinaryAssociation(
    name="rightAnd25",
    ends={
        Property(name="gseq_BooleanExpression27", type=gseq_And, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_And26", type=gseq_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
assignedExpression28: BinaryAssociation = BinaryAssociation(
    name="assignedExpression28",
    ends={
        Property(name="gseq_IntegerExpression29", type=gseq_Assign, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Assign", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftPlus30: BinaryAssociation = BinaryAssociation(
    name="leftPlus30",
    ends={
        Property(name="gseq_IntegerExpression31", type=gseq_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Plus", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftEquality17: BinaryAssociation = BinaryAssociation(
    name="leftEquality17",
    ends={
        Property(name="gseq_IntegerExpression", type=gseq_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Equality", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightEquality18: BinaryAssociation = BinaryAssociation(
    name="rightEquality18",
    ends={
        Property(name="gseq_IntegerExpression20", type=gseq_Equality, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Equality19", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1))
    }
)
notExpression21: BinaryAssociation = BinaryAssociation(
    name="notExpression21",
    ends={
        Property(name="gseq_BooleanExpression22", type=gseq_Not, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Not", type=gseq_BooleanExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightPlus32: BinaryAssociation = BinaryAssociation(
    name="rightPlus32",
    ends={
        Property(name="gseq_IntegerExpression34", type=gseq_Plus, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_Plus33", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
leftGreaterThan35: BinaryAssociation = BinaryAssociation(
    name="leftGreaterThan35",
    ends={
        Property(name="gseq_IntegerExpression36", type=gseq_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_GreaterThan", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1))
    }
)
rightGreaterThan37: BinaryAssociation = BinaryAssociation(
    name="rightGreaterThan37",
    ends={
        Property(name="gseq_IntegerExpression39", type=gseq_GreaterThan, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_GreaterThan38", type=gseq_IntegerExpression, multiplicity=Multiplicity(0, 1))
    }
)
whileCondition40: BinaryAssociation = BinaryAssociation(
    name="whileCondition40",
    ends={
        Property(name="gseq_BooleanExpression41", type=gseq_While, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_While", type=gseq_BooleanExpression, multiplicity=Multiplicity(0, 1))
    }
)
whileExpression42: BinaryAssociation = BinaryAssociation(
    name="whileExpression42",
    ends={
        Property(name="gseq_IntegerExpression44", type=gseq_While, multiplicity=Multiplicity(1, 1)),
        Property(name="gseq_While43", type=gseq_IntegerExpression, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_gseq_MethodCall_IntegerExpression = Generalization(general=IntegerExpression, specific=gseq_MethodCall)
gen_gseq_BooleanExpression_Operation = Generalization(general=Operation, specific=gseq_BooleanExpression)
gen_gseq_If_Operation = Generalization(general=Operation, specific=gseq_If)
gen_gseq_True_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_True)
gen_gseq_False_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_False)
gen_gseq_Print_Operation = Generalization(general=Operation, specific=gseq_Print)
gen_gseq_IntegerExpression_Operation = Generalization(general=Operation, specific=gseq_IntegerExpression)
gen_gseq_Const_IntegerExpression = Generalization(general=IntegerExpression, specific=gseq_Const)
gen_gseq_Var_IntegerExpression = Generalization(general=IntegerExpression, specific=gseq_Var)
gen_gseq_Assign_Operation = Generalization(general=Operation, specific=gseq_Assign)
gen_gseq_Plus_IntegerExpression = Generalization(general=IntegerExpression, specific=gseq_Plus)
gen_gseq_Equality_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_Equality)
gen_gseq_Not_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_Not)
gen_gseq_And_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_And)
gen_gseq_GreaterThan_BooleanExpression = Generalization(general=BooleanExpression, specific=gseq_GreaterThan)
gen_gseq_While_Operation = Generalization(general=Operation, specific=gseq_While)

# Domain Model
domain_model = DomainModel(
    name="gseq",
    types={gseq_Operation, gseq_Program, gseq_Method, IntegerExpression, gseq_BooleanExpression, gseq_If, gseq_True, BooleanExpression, gseq_False, gseq_MethodCall, gseq_Print, Operation, gseq_Const, gseq_Var, gseq_Assign, gseq_Plus, gseq_Equality, gseq_IntegerExpression, gseq_Not, gseq_And, gseq_GreaterThan, gseq_While},
    associations={methods0, startMethod1, operations2, toPrint7, methodToCall8, elseBranch10, thenBranch12, conditionIf15, inProgram3, calledBy4, executedBy5, leftAnd23, rightAnd25, assignedExpression28, leftPlus30, leftEquality17, rightEquality18, notExpression21, rightPlus32, leftGreaterThan35, rightGreaterThan37, whileCondition40, whileExpression42},
    generalizations={gen_gseq_MethodCall_IntegerExpression, gen_gseq_BooleanExpression_Operation, gen_gseq_If_Operation, gen_gseq_True_BooleanExpression, gen_gseq_False_BooleanExpression, gen_gseq_Print_Operation, gen_gseq_IntegerExpression_Operation, gen_gseq_Const_IntegerExpression, gen_gseq_Var_IntegerExpression, gen_gseq_Assign_Operation, gen_gseq_Plus_IntegerExpression, gen_gseq_Equality_BooleanExpression, gen_gseq_Not_BooleanExpression, gen_gseq_And_BooleanExpression, gen_gseq_GreaterThan_BooleanExpression, gen_gseq_While_Operation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)