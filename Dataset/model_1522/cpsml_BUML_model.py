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
cpsml_System = Class(name="cpsml::System")
cpsml_Variable = Class(name="cpsml::Variable")
cpsml_State = Class(name="cpsml::State")
cpsml_Transition = Class(name="cpsml::Transition", is_abstract=True)
cpsml_ODE = Class(name="cpsml::ODE")
cpsml_ComTransition = Class(name="cpsml::ComTransition")
cpsml_ProbTransition = Class(name="cpsml::ProbTransition")
Transition = Class(name="Transition")
cpsml_Function = Class(name="cpsml::Function")
cpsml_Condition = Class(name="cpsml::Condition")
cpsml_Interval = Class(name="cpsml::Interval")
cpsml_IndeVariable = Class(name="cpsml::IndeVariable")
cpsml_DeVariable = Class(name="cpsml::DeVariable")
cpsml_Fright = Class(name="cpsml::Fright")

# cpsml_System class attributes and methods
cpsml_System_name: Property = Property(name="name", type=StringType)
cpsml_System.attributes={cpsml_System_name}

# cpsml_Variable class attributes and methods
cpsml_Variable_value: Property = Property(name="value", type=FloatType)
cpsml_Variable.attributes={cpsml_Variable_value}

# cpsml_State class attributes and methods
cpsml_State_name: Property = Property(name="name", type=StringType)
cpsml_State.attributes={cpsml_State_name}

# cpsml_Transition class attributes and methods
cpsml_Transition_name: Property = Property(name="name", type=StringType)
cpsml_Transition_event: Property = Property(name="event", type=StringType)
cpsml_Transition_guard: Property = Property(name="guard", type=StringType)
cpsml_Transition_action: Property = Property(name="action", type=StringType)
cpsml_Transition.attributes={cpsml_Transition_action, cpsml_Transition_event, cpsml_Transition_name, cpsml_Transition_guard}

# cpsml_ODE class attributes and methods
cpsml_ODE_name: Property = Property(name="name", type=StringType)
cpsml_ODE.attributes={cpsml_ODE_name}

# cpsml_ComTransition class attributes and methods

# cpsml_ProbTransition class attributes and methods
cpsml_ProbTransition_probability: Property = Property(name="probability", type=FloatType)
cpsml_ProbTransition.attributes={cpsml_ProbTransition_probability}

# Transition class attributes and methods

# cpsml_Function class attributes and methods
cpsml_Function_name: Property = Property(name="name", type=StringType)
cpsml_Function.attributes={cpsml_Function_name}

# cpsml_Condition class attributes and methods
cpsml_Condition_name: Property = Property(name="name", type=StringType)
cpsml_Condition.attributes={cpsml_Condition_name}

# cpsml_Interval class attributes and methods
cpsml_Interval_name: Property = Property(name="name", type=StringType)
cpsml_Interval_left: Property = Property(name="left", type=FloatType)
cpsml_Interval_right: Property = Property(name="right", type=FloatType)
cpsml_Interval_subinterval: Property = Property(name="subinterval", type=FloatType)
cpsml_Interval.attributes={cpsml_Interval_subinterval, cpsml_Interval_right, cpsml_Interval_name, cpsml_Interval_left}

# cpsml_IndeVariable class attributes and methods
cpsml_IndeVariable_name: Property = Property(name="name", type=StringType)
cpsml_IndeVariable.attributes={cpsml_IndeVariable_name}

# cpsml_DeVariable class attributes and methods
cpsml_DeVariable_name: Property = Property(name="name", type=StringType)
cpsml_DeVariable.attributes={cpsml_DeVariable_name}

# cpsml_Fright class attributes and methods
cpsml_Fright_name: Property = Property(name="name", type=StringType)
cpsml_Fright.attributes={cpsml_Fright_name}

# Relationships
ownedvariables0: BinaryAssociation = BinaryAssociation(
    name="ownedvariables0",
    ends={
        Property(name="cpsml_Variable", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System", type=cpsml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedvariable1: BinaryAssociation = BinaryAssociation(
    name="relatedvariable1",
    ends={
        Property(name="cpsml_Variable3", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System2", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
ownedStates4: BinaryAssociation = BinaryAssociation(
    name="ownedStates4",
    ends={
        Property(name="cpsml_State", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System5", type=cpsml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedTransitions6: BinaryAssociation = BinaryAssociation(
    name="ownedTransitions6",
    ends={
        Property(name="cpsml_Transition", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System7", type=cpsml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialState8: BinaryAssociation = BinaryAssociation(
    name="initialState8",
    ends={
        Property(name="cpsml_State10", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System9", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ownedodes11: BinaryAssociation = BinaryAssociation(
    name="ownedodes11",
    ends={
        Property(name="cpsml_ODE", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System12", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
slaveode13: BinaryAssociation = BinaryAssociation(
    name="slaveode13",
    ends={
        Property(name="cpsml_ODE15", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State14", type=cpsml_ODE, multiplicity=Multiplicity(1, 1))
    }
)
outgoingComTransitions16: BinaryAssociation = BinaryAssociation(
    name="outgoingComTransitions16",
    ends={
        Property(name="ComTransition", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="csrc", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingComTransitions17: BinaryAssociation = BinaryAssociation(
    name="incomingComTransitions17",
    ends={
        Property(name="ComTransition18", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ctgt", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingProbTransitions19: BinaryAssociation = BinaryAssociation(
    name="outgoingProbTransitions19",
    ends={
        Property(name="ProbTransition", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="psrc", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingProbTransitions20: BinaryAssociation = BinaryAssociation(
    name="incomingProbTransitions20",
    ends={
        Property(name="ProbTransition21", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="ptgt", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subStates23: BinaryAssociation = BinaryAssociation(
    name="subStates23",
    ends={
        Property(name="cpsml_State24", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State22", type=cpsml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialsubstate26: BinaryAssociation = BinaryAssociation(
    name="initialsubstate26",
    ends={
        Property(name="cpsml_State27", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State25", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
subtransitions28: BinaryAssociation = BinaryAssociation(
    name="subtransitions28",
    ends={
        Property(name="cpsml_Transition30", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State29", type=cpsml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subodes31: BinaryAssociation = BinaryAssociation(
    name="subodes31",
    ends={
        Property(name="cpsml_ODE33", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State32", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrelatedvariables34: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariables34",
    ends={
        Property(name="cpsml_Variable36", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State35", type=cpsml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrelatedvariable37: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariable37",
    ends={
        Property(name="cpsml_Variable39", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State38", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
relatedvariable240: BinaryAssociation = BinaryAssociation(
    name="relatedvariable240",
    ends={
        Property(name="cpsml_Variable42", type=cpsml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Transition41", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
csrc43: BinaryAssociation = BinaryAssociation(
    name="csrc43",
    ends={
        Property(name="State", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingComTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ctgt44: BinaryAssociation = BinaryAssociation(
    name="ctgt44",
    ends={
        Property(name="State45", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingComTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
psrc46: BinaryAssociation = BinaryAssociation(
    name="psrc46",
    ends={
        Property(name="State47", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingProbTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ptgt48: BinaryAssociation = BinaryAssociation(
    name="ptgt48",
    ends={
        Property(name="State49", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingProbTransitions", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
function50: BinaryAssociation = BinaryAssociation(
    name="function50",
    ends={
        Property(name="cpsml_Function", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE51", type=cpsml_Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
condition52: BinaryAssociation = BinaryAssociation(
    name="condition52",
    ends={
        Property(name="cpsml_Condition", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE53", type=cpsml_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interval54: BinaryAssociation = BinaryAssociation(
    name="interval54",
    ends={
        Property(name="cpsml_Interval", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE55", type=cpsml_Interval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indevariable56: BinaryAssociation = BinaryAssociation(
    name="indevariable56",
    ends={
        Property(name="cpsml_IndeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function57", type=cpsml_IndeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
devariable58: BinaryAssociation = BinaryAssociation(
    name="devariable58",
    ends={
        Property(name="cpsml_DeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function59", type=cpsml_DeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fright60: BinaryAssociation = BinaryAssociation(
    name="fright60",
    ends={
        Property(name="cpsml_Fright", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function61", type=cpsml_Fright, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cpsml_ComTransition_Transition = Generalization(general=Transition, specific=cpsml_ComTransition)
gen_cpsml_ProbTransition_Transition = Generalization(general=Transition, specific=cpsml_ProbTransition)

# Domain Model
domain_model = DomainModel(
    name="cpsml",
    types={cpsml_System, cpsml_Variable, cpsml_State, cpsml_Transition, cpsml_ODE, cpsml_ComTransition, cpsml_ProbTransition, Transition, cpsml_Function, cpsml_Condition, cpsml_Interval, cpsml_IndeVariable, cpsml_DeVariable, cpsml_Fright},
    associations={ownedvariables0, relatedvariable1, ownedStates4, ownedTransitions6, initialState8, ownedodes11, slaveode13, outgoingComTransitions16, incomingComTransitions17, outgoingProbTransitions19, incomingProbTransitions20, subStates23, initialsubstate26, subtransitions28, subodes31, subrelatedvariables34, subrelatedvariable37, relatedvariable240, csrc43, ctgt44, psrc46, ptgt48, function50, condition52, interval54, indevariable56, devariable58, fright60},
    generalizations={gen_cpsml_ComTransition_Transition, gen_cpsml_ProbTransition_Transition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)