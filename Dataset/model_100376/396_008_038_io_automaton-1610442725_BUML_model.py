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
IOAutomaton_Automaton = Class(name="IOAutomaton_Automaton")
IOAutomaton_State = Class(name="IOAutomaton_State")
IOAutomaton_Input = Class(name="IOAutomaton_Input")
IOAutomaton_Activation = Class(name="IOAutomaton_Activation")
IOAutomaton_Transition = Class(name="IOAutomaton_Transition")
IOAutomaton_Output = Class(name="IOAutomaton_Output")
IOAutomaton_Operation = Class(name="IOAutomaton_Operation")
IOAutomaton_Object = Class(name="IOAutomaton_Object")
IOAutomaton_ReturnValue = Class(name="IOAutomaton_ReturnValue")

# IOAutomaton_Automaton class attributes and methods
IOAutomaton_Automaton_name: Property = Property(name="name", type=StringType)
IOAutomaton_Automaton.attributes={IOAutomaton_Automaton_name}

# IOAutomaton_State class attributes and methods
IOAutomaton_State_name: Property = Property(name="name", type=StringType)
IOAutomaton_State.attributes={IOAutomaton_State_name}

# IOAutomaton_Input class attributes and methods
IOAutomaton_Input_name: Property = Property(name="name", type=StringType)
IOAutomaton_Input.attributes={IOAutomaton_Input_name}

# IOAutomaton_Activation class attributes and methods
IOAutomaton_Activation_name: Property = Property(name="name", type=StringType)
IOAutomaton_Activation.attributes={IOAutomaton_Activation_name}

# IOAutomaton_Transition class attributes and methods
IOAutomaton_Transition_name: Property = Property(name="name", type=StringType)
IOAutomaton_Transition.attributes={IOAutomaton_Transition_name}

# IOAutomaton_Output class attributes and methods
IOAutomaton_Output_name: Property = Property(name="name", type=StringType)
IOAutomaton_Output.attributes={IOAutomaton_Output_name}

# IOAutomaton_Operation class attributes and methods
IOAutomaton_Operation_name: Property = Property(name="name", type=StringType)
IOAutomaton_Operation.attributes={IOAutomaton_Operation_name}

# IOAutomaton_Object class attributes and methods
IOAutomaton_Object_name: Property = Property(name="name", type=StringType)
IOAutomaton_Object.attributes={IOAutomaton_Object_name}

# IOAutomaton_ReturnValue class attributes and methods
IOAutomaton_ReturnValue_name: Property = Property(name="name", type=StringType)
IOAutomaton_ReturnValue_isVoid: Property = Property(name="isVoid", type=BooleanType)
IOAutomaton_ReturnValue.attributes={IOAutomaton_ReturnValue_name, IOAutomaton_ReturnValue_isVoid}

# Relationships
z0: BinaryAssociation = BinaryAssociation(
    name="z0",
    ends={
        Property(name="IOAutomaton_State", type=IOAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Automaton", type=IOAutomaton_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ingoing1: BinaryAssociation = BinaryAssociation(
    name="ingoing1",
    ends={
        Property(name="IOAutomaton_Input", type=IOAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Automaton2", type=IOAutomaton_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outcoming3: BinaryAssociation = BinaryAssociation(
    name="outcoming3",
    ends={
        Property(name="IOAutomaton_Activation", type=IOAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Automaton4", type=IOAutomaton_Activation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
delta5: BinaryAssociation = BinaryAssociation(
    name="delta5",
    ends={
        Property(name="IOAutomaton_Transition", type=IOAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Automaton6", type=IOAutomaton_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
preState10: BinaryAssociation = BinaryAssociation(
    name="preState10",
    ends={
        Property(name="IOAutomaton_State12", type=IOAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Transition11", type=IOAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
postState13: BinaryAssociation = BinaryAssociation(
    name="postState13",
    ends={
        Property(name="IOAutomaton_State15", type=IOAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Transition14", type=IOAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
input16: BinaryAssociation = BinaryAssociation(
    name="input16",
    ends={
        Property(name="IOAutomaton_Input18", type=IOAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Transition17", type=IOAutomaton_Input, multiplicity=Multiplicity(1, 1))
    }
)
activation19: BinaryAssociation = BinaryAssociation(
    name="activation19",
    ends={
        Property(name="IOAutomaton_Activation21", type=IOAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Transition20", type=IOAutomaton_Activation, multiplicity=Multiplicity(1, 1))
    }
)
z07: BinaryAssociation = BinaryAssociation(
    name="z07",
    ends={
        Property(name="IOAutomaton_State9", type=IOAutomaton_Automaton, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Automaton8", type=IOAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
operation26: BinaryAssociation = BinaryAssociation(
    name="operation26",
    ends={
        Property(name="IOAutomaton_Operation", type=IOAutomaton_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Input27", type=IOAutomaton_Operation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
operation28: BinaryAssociation = BinaryAssociation(
    name="operation28",
    ends={
        Property(name="IOAutomaton_Operation30", type=IOAutomaton_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Output29", type=IOAutomaton_Operation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
outObject31: BinaryAssociation = BinaryAssociation(
    name="outObject31",
    ends={
        Property(name="IOAutomaton_Object", type=IOAutomaton_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Output32", type=IOAutomaton_Object, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
output22: BinaryAssociation = BinaryAssociation(
    name="output22",
    ends={
        Property(name="IOAutomaton_Output", type=IOAutomaton_Activation, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Activation23", type=IOAutomaton_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnValue24: BinaryAssociation = BinaryAssociation(
    name="returnValue24",
    ends={
        Property(name="IOAutomaton_ReturnValue", type=IOAutomaton_Activation, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Activation25", type=IOAutomaton_ReturnValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
returnValue33: BinaryAssociation = BinaryAssociation(
    name="returnValue33",
    ends={
        Property(name="IOAutomaton_ReturnValue35", type=IOAutomaton_Output, multiplicity=Multiplicity(1, 1)),
        Property(name="IOAutomaton_Output34", type=IOAutomaton_ReturnValue, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="IOAutomaton",
    types={IOAutomaton_Automaton, IOAutomaton_State, IOAutomaton_Input, IOAutomaton_Activation, IOAutomaton_Transition, IOAutomaton_Output, IOAutomaton_Operation, IOAutomaton_Object, IOAutomaton_ReturnValue},
    associations={z0, ingoing1, outcoming3, delta5, preState10, postState13, input16, activation19, z07, operation26, operation28, outObject31, output22, returnValue24, returnValue33},
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