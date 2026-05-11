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
robot_Robot = Class(name="robot_Robot")
NamedElement = Class(name="NamedElement")
robot_Scenario = Class(name="robot_Scenario")
robot_StatementBlock = Class(name="robot_StatementBlock")
robot_ControlStatement = Class(name="robot_ControlStatement", is_abstract=True)
robot_ExecuteStatement = Class(name="robot_ExecuteStatement")
robot_ForwardStatement = Class(name="robot_ForwardStatement")
ControlStatement = Class(name="ControlStatement")
robot_IfStatement = Class(name="robot_IfStatement")
ConditionalStatement = Class(name="ConditionalStatement")
robot_PrintStatement = Class(name="robot_PrintStatement")
robot_RightStatement = Class(name="robot_RightStatement")
robot_Statement = Class(name="robot_Statement", is_abstract=True)
robot_Connection = Class(name="robot_Connection")
robot_NamedElement = Class(name="robot_NamedElement", is_abstract=True)
robot_ObjectAheadCondition = Class(name="robot_ObjectAheadCondition")
Condition = Class(name="Condition")
robot_TrueCondition = Class(name="robot_TrueCondition")
robot_Condition = Class(name="robot_Condition")
robot_ConditionalStatement = Class(name="robot_ConditionalStatement", is_abstract=True)
Statement = Class(name="Statement")
robot_UntilStatement = Class(name="robot_UntilStatement")
robot_WhileStatement = Class(name="robot_WhileStatement")

# robot_Robot class attributes and methods

# NamedElement class attributes and methods

# robot_Scenario class attributes and methods

# robot_StatementBlock class attributes and methods

# robot_ControlStatement class attributes and methods
robot_ControlStatement_value: Property = Property(name="value", type=IntegerType)
robot_ControlStatement.attributes={robot_ControlStatement_value}

# robot_ExecuteStatement class attributes and methods

# robot_ForwardStatement class attributes and methods

# ControlStatement class attributes and methods

# robot_IfStatement class attributes and methods

# ConditionalStatement class attributes and methods

# robot_PrintStatement class attributes and methods
robot_PrintStatement_text: Property = Property(name="text", type=StringType)
robot_PrintStatement.attributes={robot_PrintStatement_text}

# robot_RightStatement class attributes and methods

# robot_Statement class attributes and methods

# robot_Connection class attributes and methods
robot_Connection_ip: Property = Property(name="ip", type=StringType)
robot_Connection_port: Property = Property(name="port", type=IntegerType)
robot_Connection.attributes={robot_Connection_ip, robot_Connection_port}

# robot_NamedElement class attributes and methods
robot_NamedElement_name: Property = Property(name="name", type=StringType)
robot_NamedElement.attributes={robot_NamedElement_name}

# robot_ObjectAheadCondition class attributes and methods

# Condition class attributes and methods

# robot_TrueCondition class attributes and methods

# robot_Condition class attributes and methods

# robot_ConditionalStatement class attributes and methods

# Statement class attributes and methods

# robot_UntilStatement class attributes and methods

# robot_WhileStatement class attributes and methods

# Relationships
scenarii0: BinaryAssociation = BinaryAssociation(
    name="scenarii0",
    ends={
        Property(name="robot_Scenario", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot", type=robot_Scenario, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
global_1: BinaryAssociation = BinaryAssociation(
    name="global_1",
    ends={
        Property(name="robot_StatementBlock", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot2", type=robot_StatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition11: BinaryAssociation = BinaryAssociation(
    name="condition11",
    ends={
        Property(name="robot_Condition", type=robot_ConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_ConditionalStatement", type=robot_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statementBlock12: BinaryAssociation = BinaryAssociation(
    name="statementBlock12",
    ends={
        Property(name="robot_StatementBlock14", type=robot_ConditionalStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_ConditionalStatement13", type=robot_StatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
destination15: BinaryAssociation = BinaryAssociation(
    name="destination15",
    ends={
        Property(name="robot_Scenario16", type=robot_ExecuteStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_ExecuteStatement", type=robot_Scenario, multiplicity=Multiplicity(1, 1))
    }
)
initial3: BinaryAssociation = BinaryAssociation(
    name="initial3",
    ends={
        Property(name="robot_Scenario5", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot4", type=robot_Scenario, multiplicity=Multiplicity(0, 1))
    }
)
connection6: BinaryAssociation = BinaryAssociation(
    name="connection6",
    ends={
        Property(name="robot_Connection", type=robot_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Robot7", type=robot_Connection, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
statementBlock8: BinaryAssociation = BinaryAssociation(
    name="statementBlock8",
    ends={
        Property(name="robot_StatementBlock10", type=robot_Scenario, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_Scenario9", type=robot_StatementBlock, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
statements17: BinaryAssociation = BinaryAssociation(
    name="statements17",
    ends={
        Property(name="robot_Statement", type=robot_StatementBlock, multiplicity=Multiplicity(1, 1)),
        Property(name="robot_StatementBlock18", type=robot_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_robot_Robot_NamedElement = Generalization(general=NamedElement, specific=robot_Robot)
gen_robot_ControlStatement_Statement = Generalization(general=Statement, specific=robot_ControlStatement)
gen_robot_ExecuteStatement_Statement = Generalization(general=Statement, specific=robot_ExecuteStatement)
gen_robot_ForwardStatement_ControlStatement = Generalization(general=ControlStatement, specific=robot_ForwardStatement)
gen_robot_IfStatement_ConditionalStatement = Generalization(general=ConditionalStatement, specific=robot_IfStatement)
gen_robot_PrintStatement_Statement = Generalization(general=Statement, specific=robot_PrintStatement)
gen_robot_RightStatement_ControlStatement = Generalization(general=ControlStatement, specific=robot_RightStatement)
gen_robot_Scenario_NamedElement = Generalization(general=NamedElement, specific=robot_Scenario)
gen_robot_ObjectAheadCondition_Condition = Generalization(general=Condition, specific=robot_ObjectAheadCondition)
gen_robot_TrueCondition_Condition = Generalization(general=Condition, specific=robot_TrueCondition)
gen_robot_ConditionalStatement_Statement = Generalization(general=Statement, specific=robot_ConditionalStatement)
gen_robot_UntilStatement_ConditionalStatement = Generalization(general=ConditionalStatement, specific=robot_UntilStatement)
gen_robot_WhileStatement_ConditionalStatement = Generalization(general=ConditionalStatement, specific=robot_WhileStatement)

# Domain Model
domain_model = DomainModel(
    name="robot",
    types={robot_Robot, NamedElement, robot_Scenario, robot_StatementBlock, robot_ControlStatement, robot_ExecuteStatement, robot_ForwardStatement, ControlStatement, robot_IfStatement, ConditionalStatement, robot_PrintStatement, robot_RightStatement, robot_Statement, robot_Connection, robot_NamedElement, robot_ObjectAheadCondition, Condition, robot_TrueCondition, robot_Condition, robot_ConditionalStatement, Statement, robot_UntilStatement, robot_WhileStatement},
    associations={scenarii0, global_1, condition11, statementBlock12, destination15, initial3, connection6, statementBlock8, statements17},
    generalizations={gen_robot_Robot_NamedElement, gen_robot_ControlStatement_Statement, gen_robot_ExecuteStatement_Statement, gen_robot_ForwardStatement_ControlStatement, gen_robot_IfStatement_ConditionalStatement, gen_robot_PrintStatement_Statement, gen_robot_RightStatement_ControlStatement, gen_robot_Scenario_NamedElement, gen_robot_ObjectAheadCondition_Condition, gen_robot_TrueCondition_Condition, gen_robot_ConditionalStatement_Statement, gen_robot_UntilStatement_ConditionalStatement, gen_robot_WhileStatement_ConditionalStatement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)