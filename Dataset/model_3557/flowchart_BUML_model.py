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
flowchartpck_Arc = Class(name="flowchartpck_Arc")
flowchartpck_NamedElement = Class(name="flowchartpck_NamedElement")
flowchartpck_Flowchart = Class(name="flowchartpck_Flowchart")
NamedElement = Class(name="NamedElement")
flowchartpck_Node = Class(name="flowchartpck_Node", is_abstract=True)
flowchartpck_RelationalExpression = Class(name="flowchartpck_RelationalExpression")
flowchartpck_Action = Class(name="flowchartpck_Action")
Node = Class(name="Node")
flowchartpck_Program = Class(name="flowchartpck_Program")
flowchartpck_Decision = Class(name="flowchartpck_Decision")
flowchartpck_Constraint = Class(name="flowchartpck_Constraint")
flowchartpck_Start = Class(name="flowchartpck_Start")
flowchartpck_End = Class(name="flowchartpck_End")
flowchartpck_RelationalConstraint = Class(name="flowchartpck_RelationalConstraint")
Constraint = Class(name="Constraint")
flowchartpck_Expression = Class(name="flowchartpck_Expression")
flowchartpck_Literal = Class(name="flowchartpck_Literal")
Expression = Class(name="Expression")
flowchartpck_IntegerLit = Class(name="flowchartpck_IntegerLit")
Literal = Class(name="Literal")
flowchartpck_StringLit = Class(name="flowchartpck_StringLit")
flowchartpck_BoolLit = Class(name="flowchartpck_BoolLit")
flowchartpck_ArithmeticExpression = Class(name="flowchartpck_ArithmeticExpression")
flowchartpck_Wait = Class(name="flowchartpck_Wait")
flowchartpck_VarReference = Class(name="flowchartpck_VarReference")
flowchartpck_Statement = Class(name="flowchartpck_Statement", is_abstract=True)
Statement = Class(name="Statement")
flowchartpck_Conditional = Class(name="flowchartpck_Conditional")
flowchartpck_Loop = Class(name="flowchartpck_Loop")
flowchartpck_ConsoleOutput = Class(name="flowchartpck_ConsoleOutput")
flowchartpck_Println = Class(name="flowchartpck_Println")
ConsoleOutput = Class(name="ConsoleOutput")
flowchartpck_Print = Class(name="flowchartpck_Print")
flowchartpck_Assignation = Class(name="flowchartpck_Assignation")
flowchartpck_VarDecl = Class(name="flowchartpck_VarDecl")

# flowchartpck_Arc class attributes and methods

# flowchartpck_NamedElement class attributes and methods
flowchartpck_NamedElement_name: Property = Property(name="name", type=StringType)
flowchartpck_NamedElement.attributes={flowchartpck_NamedElement_name}

# flowchartpck_Flowchart class attributes and methods

# NamedElement class attributes and methods

# flowchartpck_Node class attributes and methods

# flowchartpck_RelationalExpression class attributes and methods
flowchartpck_RelationalExpression_operator: Property = Property(name="operator", type=StringType)
flowchartpck_RelationalExpression.attributes={flowchartpck_RelationalExpression_operator}

# flowchartpck_Action class attributes and methods

# Node class attributes and methods

# flowchartpck_Program class attributes and methods

# flowchartpck_Decision class attributes and methods

# flowchartpck_Constraint class attributes and methods

# flowchartpck_Start class attributes and methods

# flowchartpck_End class attributes and methods

# flowchartpck_RelationalConstraint class attributes and methods

# Constraint class attributes and methods

# flowchartpck_Expression class attributes and methods

# flowchartpck_Literal class attributes and methods

# Expression class attributes and methods

# flowchartpck_IntegerLit class attributes and methods
flowchartpck_IntegerLit_value: Property = Property(name="value", type=IntegerType)
flowchartpck_IntegerLit.attributes={flowchartpck_IntegerLit_value}

# Literal class attributes and methods

# flowchartpck_StringLit class attributes and methods
flowchartpck_StringLit_value: Property = Property(name="value", type=StringType)
flowchartpck_StringLit.attributes={flowchartpck_StringLit_value}

# flowchartpck_BoolLit class attributes and methods
flowchartpck_BoolLit_value: Property = Property(name="value", type=BooleanType)
flowchartpck_BoolLit.attributes={flowchartpck_BoolLit_value}

# flowchartpck_ArithmeticExpression class attributes and methods
flowchartpck_ArithmeticExpression_operator: Property = Property(name="operator", type=StringType)
flowchartpck_ArithmeticExpression.attributes={flowchartpck_ArithmeticExpression_operator}

# flowchartpck_Wait class attributes and methods
flowchartpck_Wait_miliseconds: Property = Property(name="miliseconds", type=StringType)
flowchartpck_Wait.attributes={flowchartpck_Wait_miliseconds}

# flowchartpck_VarReference class attributes and methods
flowchartpck_VarReference_key: Property = Property(name="key", type=StringType)
flowchartpck_VarReference.attributes={flowchartpck_VarReference_key}

# flowchartpck_Statement class attributes and methods

# Statement class attributes and methods

# flowchartpck_Conditional class attributes and methods

# flowchartpck_Loop class attributes and methods

# flowchartpck_ConsoleOutput class attributes and methods
flowchartpck_ConsoleOutput_input: Property = Property(name="input", type=StringType)
flowchartpck_ConsoleOutput.attributes={flowchartpck_ConsoleOutput_input}

# flowchartpck_Println class attributes and methods

# ConsoleOutput class attributes and methods

# flowchartpck_Print class attributes and methods

# flowchartpck_Assignation class attributes and methods

# flowchartpck_VarDecl class attributes and methods
flowchartpck_VarDecl_key: Property = Property(name="key", type=StringType)
flowchartpck_VarDecl.attributes={flowchartpck_VarDecl_key}

# Relationships
arcs1: BinaryAssociation = BinaryAssociation(
    name="arcs1",
    ends={
        Property(name="flowchartpck_Arc", type=flowchartpck_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Flowchart2", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes0: BinaryAssociation = BinaryAssociation(
    name="nodes0",
    ends={
        Property(name="flowchartpck_Node", type=flowchartpck_Flowchart, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Flowchart", type=flowchartpck_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right14: BinaryAssociation = BinaryAssociation(
    name="right14",
    ends={
        Property(name="flowchartpck_Expression16", type=flowchartpck_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_ArithmeticExpression15", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left17: BinaryAssociation = BinaryAssociation(
    name="left17",
    ends={
        Property(name="flowchartpck_Expression18", type=flowchartpck_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalExpression", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
right19: BinaryAssociation = BinaryAssociation(
    name="right19",
    ends={
        Property(name="flowchartpck_Expression21", type=flowchartpck_RelationalExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalExpression20", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outgoing3: BinaryAssociation = BinaryAssociation(
    name="outgoing3",
    ends={
        Property(name="Arc", type=flowchartpck_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
incoming4: BinaryAssociation = BinaryAssociation(
    name="incoming4",
    ends={
        Property(name="Arc5", type=flowchartpck_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=flowchartpck_Arc, multiplicity=Multiplicity(0, 9999))
    }
)
source6: BinaryAssociation = BinaryAssociation(
    name="source6",
    ends={
        Property(name="Node", type=flowchartpck_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=flowchartpck_Node, multiplicity=Multiplicity(0, 1))
    }
)
target7: BinaryAssociation = BinaryAssociation(
    name="target7",
    ends={
        Property(name="Node8", type=flowchartpck_Arc, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=flowchartpck_Node, multiplicity=Multiplicity(0, 1))
    }
)
doProgram9: BinaryAssociation = BinaryAssociation(
    name="doProgram9",
    ends={
        Property(name="flowchartpck_Program", type=flowchartpck_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Action", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard10: BinaryAssociation = BinaryAssociation(
    name="guard10",
    ends={
        Property(name="flowchartpck_Constraint", type=flowchartpck_Decision, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Decision", type=flowchartpck_Constraint, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression11: BinaryAssociation = BinaryAssociation(
    name="expression11",
    ends={
        Property(name="flowchartpck_Expression", type=flowchartpck_RelationalConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_RelationalConstraint", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
left12: BinaryAssociation = BinaryAssociation(
    name="left12",
    ends={
        Property(name="flowchartpck_Expression13", type=flowchartpck_ArithmeticExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_ArithmeticExpression", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="flowchartpck_Expression43", type=flowchartpck_VarDecl, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_VarDecl42", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements22: BinaryAssociation = BinaryAssociation(
    name="statements22",
    ends={
        Property(name="flowchartpck_Statement", type=flowchartpck_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Program23", type=flowchartpck_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
thenInstructions24: BinaryAssociation = BinaryAssociation(
    name="thenInstructions24",
    ends={
        Property(name="flowchartpck_Program25", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
elseInstructions26: BinaryAssociation = BinaryAssociation(
    name="elseInstructions26",
    ends={
        Property(name="flowchartpck_Program28", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional27", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
condition29: BinaryAssociation = BinaryAssociation(
    name="condition29",
    ends={
        Property(name="flowchartpck_Expression31", type=flowchartpck_Conditional, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Conditional30", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
body32: BinaryAssociation = BinaryAssociation(
    name="body32",
    ends={
        Property(name="flowchartpck_Program33", type=flowchartpck_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Loop", type=flowchartpck_Program, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard34: BinaryAssociation = BinaryAssociation(
    name="guard34",
    ends={
        Property(name="flowchartpck_Expression36", type=flowchartpck_Loop, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Loop35", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
varRef37: BinaryAssociation = BinaryAssociation(
    name="varRef37",
    ends={
        Property(name="flowchartpck_VarDecl", type=flowchartpck_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Assignation", type=flowchartpck_VarDecl, multiplicity=Multiplicity(1, 1))
    }
)
expression38: BinaryAssociation = BinaryAssociation(
    name="expression38",
    ends={
        Property(name="flowchartpck_Expression40", type=flowchartpck_Assignation, multiplicity=Multiplicity(1, 1)),
        Property(name="flowchartpck_Assignation39", type=flowchartpck_Expression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_flowchartpck_Flowchart_NamedElement = Generalization(general=NamedElement, specific=flowchartpck_Flowchart)
gen_flowchartpck_RelationalExpression_Expression = Generalization(general=Expression, specific=flowchartpck_RelationalExpression)
gen_flowchartpck_Node_NamedElement = Generalization(general=NamedElement, specific=flowchartpck_Node)
gen_flowchartpck_Action_Node = Generalization(general=Node, specific=flowchartpck_Action)
gen_flowchartpck_Decision_Node = Generalization(general=Node, specific=flowchartpck_Decision)
gen_flowchartpck_Start_Node = Generalization(general=Node, specific=flowchartpck_Start)
gen_flowchartpck_End_Node = Generalization(general=Node, specific=flowchartpck_End)
gen_flowchartpck_RelationalConstraint_Constraint = Generalization(general=Constraint, specific=flowchartpck_RelationalConstraint)
gen_flowchartpck_Literal_Expression = Generalization(general=Expression, specific=flowchartpck_Literal)
gen_flowchartpck_IntegerLit_Literal = Generalization(general=Literal, specific=flowchartpck_IntegerLit)
gen_flowchartpck_StringLit_Literal = Generalization(general=Literal, specific=flowchartpck_StringLit)
gen_flowchartpck_BoolLit_Literal = Generalization(general=Literal, specific=flowchartpck_BoolLit)
gen_flowchartpck_ArithmeticExpression_Expression = Generalization(general=Expression, specific=flowchartpck_ArithmeticExpression)
gen_flowchartpck_Wait_Statement = Generalization(general=Statement, specific=flowchartpck_Wait)
gen_flowchartpck_VarDecl_Statement = Generalization(general=Statement, specific=flowchartpck_VarDecl)
gen_flowchartpck_VarReference_Expression = Generalization(general=Expression, specific=flowchartpck_VarReference)
gen_flowchartpck_Program_Statement = Generalization(general=Statement, specific=flowchartpck_Program)
gen_flowchartpck_Conditional_Statement = Generalization(general=Statement, specific=flowchartpck_Conditional)
gen_flowchartpck_Loop_Statement = Generalization(general=Statement, specific=flowchartpck_Loop)
gen_flowchartpck_ConsoleOutput_Statement = Generalization(general=Statement, specific=flowchartpck_ConsoleOutput)
gen_flowchartpck_Println_ConsoleOutput = Generalization(general=ConsoleOutput, specific=flowchartpck_Println)
gen_flowchartpck_Print_ConsoleOutput = Generalization(general=ConsoleOutput, specific=flowchartpck_Print)
gen_flowchartpck_Assignation_Statement = Generalization(general=Statement, specific=flowchartpck_Assignation)

# Domain Model
domain_model = DomainModel(
    name="flowchartpck",
    types={flowchartpck_Arc, flowchartpck_NamedElement, flowchartpck_Flowchart, NamedElement, flowchartpck_Node, flowchartpck_RelationalExpression, flowchartpck_Action, Node, flowchartpck_Program, flowchartpck_Decision, flowchartpck_Constraint, flowchartpck_Start, flowchartpck_End, flowchartpck_RelationalConstraint, Constraint, flowchartpck_Expression, flowchartpck_Literal, Expression, flowchartpck_IntegerLit, Literal, flowchartpck_StringLit, flowchartpck_BoolLit, flowchartpck_ArithmeticExpression, flowchartpck_Wait, flowchartpck_VarReference, flowchartpck_Statement, Statement, flowchartpck_Conditional, flowchartpck_Loop, flowchartpck_ConsoleOutput, flowchartpck_Println, ConsoleOutput, flowchartpck_Print, flowchartpck_Assignation, flowchartpck_VarDecl, ArithmeticOperator, RelationalOperator},
    associations={arcs1, nodes0, right14, left17, right19, outgoing3, incoming4, source6, target7, doProgram9, guard10, expression11, left12, expression41, statements22, thenInstructions24, elseInstructions26, condition29, body32, guard34, varRef37, expression38},
    generalizations={gen_flowchartpck_Flowchart_NamedElement, gen_flowchartpck_RelationalExpression_Expression, gen_flowchartpck_Node_NamedElement, gen_flowchartpck_Action_Node, gen_flowchartpck_Decision_Node, gen_flowchartpck_Start_Node, gen_flowchartpck_End_Node, gen_flowchartpck_RelationalConstraint_Constraint, gen_flowchartpck_Literal_Expression, gen_flowchartpck_IntegerLit_Literal, gen_flowchartpck_StringLit_Literal, gen_flowchartpck_BoolLit_Literal, gen_flowchartpck_ArithmeticExpression_Expression, gen_flowchartpck_Wait_Statement, gen_flowchartpck_VarDecl_Statement, gen_flowchartpck_VarReference_Expression, gen_flowchartpck_Program_Statement, gen_flowchartpck_Conditional_Statement, gen_flowchartpck_Loop_Statement, gen_flowchartpck_ConsoleOutput_Statement, gen_flowchartpck_Println_ConsoleOutput, gen_flowchartpck_Print_ConsoleOutput, gen_flowchartpck_Assignation_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)