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
stateMachineActions_Model = Class(name="stateMachineActions_Model")
stateMachineActions_Action = Class(name="stateMachineActions_Action")
stateMachineActions_TERM = Class(name="stateMachineActions_TERM")
stateMachineActions_Assignment = Class(name="stateMachineActions_Assignment")
stateMachineActions_EventAction = Class(name="stateMachineActions_EventAction")
stateMachineActions_EXPRESSION = Class(name="stateMachineActions_EXPRESSION")
stateMachineActions_Parameters = Class(name="stateMachineActions_Parameters")

# stateMachineActions_Model class attributes and methods

# stateMachineActions_Action class attributes and methods

# stateMachineActions_TERM class attributes and methods
stateMachineActions_TERM_variable: Property = Property(name="variable", type=StringType)
stateMachineActions_TERM_constant: Property = Property(name="constant", type=IntegerType)
stateMachineActions_TERM.attributes={stateMachineActions_TERM_variable, stateMachineActions_TERM_constant}

# stateMachineActions_Assignment class attributes and methods
stateMachineActions_Assignment_leftvar: Property = Property(name="leftvar", type=StringType)
stateMachineActions_Assignment.attributes={stateMachineActions_Assignment_leftvar}

# stateMachineActions_EventAction class attributes and methods
stateMachineActions_EventAction_eventName: Property = Property(name="eventName", type=StringType)
stateMachineActions_EventAction_eventExtension: Property = Property(name="eventExtension", type=StringType)
stateMachineActions_EventAction.attributes={stateMachineActions_EventAction_eventExtension, stateMachineActions_EventAction_eventName}

# stateMachineActions_EXPRESSION class attributes and methods
stateMachineActions_EXPRESSION_operator: Property = Property(name="operator", type=StringType)
stateMachineActions_EXPRESSION.attributes={stateMachineActions_EXPRESSION_operator}

# stateMachineActions_Parameters class attributes and methods
stateMachineActions_Parameters_param: Property = Property(name="param", type=StringType)
stateMachineActions_Parameters.attributes={stateMachineActions_Parameters_param}

# Relationships
action0: BinaryAssociation = BinaryAssociation(
    name="action0",
    ends={
        Property(name="stateMachineActions_Action", type=stateMachineActions_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_Model", type=stateMachineActions_Action, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
firstTerm7: BinaryAssociation = BinaryAssociation(
    name="firstTerm7",
    ends={
        Property(name="stateMachineActions_TERM", type=stateMachineActions_EXPRESSION, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_EXPRESSION8", type=stateMachineActions_TERM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
secondTerm9: BinaryAssociation = BinaryAssociation(
    name="secondTerm9",
    ends={
        Property(name="stateMachineActions_TERM11", type=stateMachineActions_EXPRESSION, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_EXPRESSION10", type=stateMachineActions_TERM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
alone12: BinaryAssociation = BinaryAssociation(
    name="alone12",
    ends={
        Property(name="stateMachineActions_TERM14", type=stateMachineActions_EXPRESSION, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_EXPRESSION13", type=stateMachineActions_TERM, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
assignment1: BinaryAssociation = BinaryAssociation(
    name="assignment1",
    ends={
        Property(name="stateMachineActions_Assignment", type=stateMachineActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_Action2", type=stateMachineActions_Assignment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
eventAction3: BinaryAssociation = BinaryAssociation(
    name="eventAction3",
    ends={
        Property(name="stateMachineActions_EventAction", type=stateMachineActions_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_Action4", type=stateMachineActions_EventAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression5: BinaryAssociation = BinaryAssociation(
    name="expression5",
    ends={
        Property(name="stateMachineActions_EXPRESSION", type=stateMachineActions_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_Assignment6", type=stateMachineActions_EXPRESSION, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters18: BinaryAssociation = BinaryAssociation(
    name="parameters18",
    ends={
        Property(name="stateMachineActions_Parameters19", type=stateMachineActions_Parameters, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_Parameters17", type=stateMachineActions_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters15: BinaryAssociation = BinaryAssociation(
    name="parameters15",
    ends={
        Property(name="stateMachineActions_Parameters", type=stateMachineActions_EventAction, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachineActions_EventAction16", type=stateMachineActions_Parameters, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="stateMachineActions",
    types={stateMachineActions_Model, stateMachineActions_Action, stateMachineActions_TERM, stateMachineActions_Assignment, stateMachineActions_EventAction, stateMachineActions_EXPRESSION, stateMachineActions_Parameters},
    associations={action0, firstTerm7, secondTerm9, alone12, assignment1, eventAction3, expression5, parameters18, parameters15},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)