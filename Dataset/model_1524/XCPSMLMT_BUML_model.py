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
cpsml_ODE = Class(name="cpsml::ODE")
cpsml_Variable = Class(name="cpsml::Variable")
cpsml_State = Class(name="cpsml::State")
cpsml_Transition = Class(name="cpsml::Transition", is_abstract=True)
cpsml_ComTransition = Class(name="cpsml::ComTransition")
cpsml_ProbTransition = Class(name="cpsml::ProbTransition")
cpsml_Function = Class(name="cpsml::Function")
cpsml_Condition = Class(name="cpsml::Condition")
Transition = Class(name="Transition")
cpsml_Interval = Class(name="cpsml::Interval")
cpsml_IndeVariable = Class(name="cpsml::IndeVariable")
cpsml_DeVariable = Class(name="cpsml::DeVariable")
cpsml_Fright = Class(name="cpsml::Fright")

# cpsml_System class attributes and methods
cpsml_System_name: Property = Property(name="name", type=StringType)
cpsml_System_ran: Property = Property(name="ran", type=StringType)
cpsml_System_sub: Property = Property(name="sub", type=IntegerType)
cpsml_System_y0label: Property = Property(name="y0label", type=IntegerType)
cpsml_System_m_main: Method = Method(name="main", parameters={})
cpsml_System_m_dojump: Method = Method(name="dojump", parameters={})
cpsml_System_m_callscilab: Method = Method(name="callscilab", parameters={})
cpsml_System_m_RealizeInitializeModel: Method = Method(name="RealizeInitializeModel", parameters={Parameter(name='arguments')})
cpsml_System.attributes={cpsml_System_ran, cpsml_System_sub, cpsml_System_name, cpsml_System_y0label}
cpsml_System.methods={cpsml_System_m_dojump, cpsml_System_m_RealizeInitializeModel, cpsml_System_m_main, cpsml_System_m_callscilab}

# cpsml_ODE class attributes and methods
cpsml_ODE_name: Property = Property(name="name", type=StringType)
cpsml_ODE.attributes={cpsml_ODE_name}

# cpsml_Variable class attributes and methods
cpsml_Variable_value: Property = Property(name="value", type=FloatType)
cpsml_Variable_Globalnv: Property = Property(name="Globalnv", type=FloatType)
cpsml_Variable.attributes={cpsml_Variable_value, cpsml_Variable_Globalnv}

# cpsml_State class attributes and methods
cpsml_State_name: Property = Property(name="name", type=BooleanType)
cpsml_State.attributes={cpsml_State_name}

# cpsml_Transition class attributes and methods
cpsml_Transition_name: Property = Property(name="name", type=StringType)
cpsml_Transition_event: Property = Property(name="event", type=StringType)
cpsml_Transition_guard: Property = Property(name="guard", type=StringType)
cpsml_Transition_action: Property = Property(name="action", type=StringType)
cpsml_Transition_m_holds: Method = Method(name="holds", parameters={})
cpsml_Transition.attributes={cpsml_Transition_name, cpsml_Transition_action, cpsml_Transition_event, cpsml_Transition_guard}
cpsml_Transition.methods={cpsml_Transition_m_holds}

# cpsml_ComTransition class attributes and methods

# cpsml_ProbTransition class attributes and methods
cpsml_ProbTransition_probability: Property = Property(name="probability", type=FloatType)
cpsml_ProbTransition.attributes={cpsml_ProbTransition_probability}

# cpsml_Function class attributes and methods
cpsml_Function_name: Property = Property(name="name", type=StringType)
cpsml_Function.attributes={cpsml_Function_name}

# cpsml_Condition class attributes and methods
cpsml_Condition_name: Property = Property(name="name", type=StringType)
cpsml_Condition.attributes={cpsml_Condition_name}

# Transition class attributes and methods

# cpsml_Interval class attributes and methods
cpsml_Interval_right: Property = Property(name="right", type=FloatType)
cpsml_Interval_subinterval: Property = Property(name="subinterval", type=FloatType)
cpsml_Interval_name: Property = Property(name="name", type=StringType)
cpsml_Interval_left: Property = Property(name="left", type=FloatType)
cpsml_Interval.attributes={cpsml_Interval_right, cpsml_Interval_subinterval, cpsml_Interval_left, cpsml_Interval_name}

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
ownedodes11: BinaryAssociation = BinaryAssociation(
    name="ownedodes11",
    ends={
        Property(name="cpsml_ODE", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System12", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
currentState13: BinaryAssociation = BinaryAssociation(
    name="currentState13",
    ends={
        Property(name="cpsml_State15", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System14", type=cpsml_State, multiplicity=Multiplicity(0, 1))
    }
)
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
slaveode21: BinaryAssociation = BinaryAssociation(
    name="slaveode21",
    ends={
        Property(name="cpsml_ODE23", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State22", type=cpsml_ODE, multiplicity=Multiplicity(1, 1))
    }
)
outgoingComTransitions24: BinaryAssociation = BinaryAssociation(
    name="outgoingComTransitions24",
    ends={
        Property(name="25", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingComTransitions26: BinaryAssociation = BinaryAssociation(
    name="incomingComTransitions26",
    ends={
        Property(name="28", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="27", type=cpsml_ComTransition, multiplicity=Multiplicity(0, 9999))
    }
)
fatherState16: BinaryAssociation = BinaryAssociation(
    name="fatherState16",
    ends={
        Property(name="cpsml_State18", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System17", type=cpsml_State, multiplicity=Multiplicity(0, 1))
    }
)
ptok19: BinaryAssociation = BinaryAssociation(
    name="ptok19",
    ends={
        Property(name="cpsml_ProbTransition", type=cpsml_System, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_System20", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 1))
    }
)
relatedvariable253: BinaryAssociation = BinaryAssociation(
    name="relatedvariable253",
    ends={
        Property(name="cpsml_Variable55", type=cpsml_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Transition54", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
outgoingProbTransitions29: BinaryAssociation = BinaryAssociation(
    name="outgoingProbTransitions29",
    ends={
        Property(name="31", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="30", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
incomingProbTransitions32: BinaryAssociation = BinaryAssociation(
    name="incomingProbTransitions32",
    ends={
        Property(name="34", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="33", type=cpsml_ProbTransition, multiplicity=Multiplicity(0, 9999))
    }
)
subStates36: BinaryAssociation = BinaryAssociation(
    name="subStates36",
    ends={
        Property(name="cpsml_State37", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State35", type=cpsml_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialsubstate39: BinaryAssociation = BinaryAssociation(
    name="initialsubstate39",
    ends={
        Property(name="cpsml_State40", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State38", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
subtransitions41: BinaryAssociation = BinaryAssociation(
    name="subtransitions41",
    ends={
        Property(name="cpsml_Transition43", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State42", type=cpsml_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subodes44: BinaryAssociation = BinaryAssociation(
    name="subodes44",
    ends={
        Property(name="cpsml_ODE46", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State45", type=cpsml_ODE, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrelatedvariables47: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariables47",
    ends={
        Property(name="cpsml_Variable49", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State48", type=cpsml_Variable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subrelatedvariable50: BinaryAssociation = BinaryAssociation(
    name="subrelatedvariable50",
    ends={
        Property(name="cpsml_Variable52", type=cpsml_State, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_State51", type=cpsml_Variable, multiplicity=Multiplicity(1, 1))
    }
)
function68: BinaryAssociation = BinaryAssociation(
    name="function68",
    ends={
        Property(name="cpsml_Function", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE69", type=cpsml_Function, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
csrc56: BinaryAssociation = BinaryAssociation(
    name="csrc56",
    ends={
        Property(name="58", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="57", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ctgt59: BinaryAssociation = BinaryAssociation(
    name="ctgt59",
    ends={
        Property(name="61", type=cpsml_ComTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="60", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
psrc62: BinaryAssociation = BinaryAssociation(
    name="psrc62",
    ends={
        Property(name="64", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="63", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
ptgt65: BinaryAssociation = BinaryAssociation(
    name="ptgt65",
    ends={
        Property(name="67", type=cpsml_ProbTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="66", type=cpsml_State, multiplicity=Multiplicity(1, 1))
    }
)
condition70: BinaryAssociation = BinaryAssociation(
    name="condition70",
    ends={
        Property(name="cpsml_Condition", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE71", type=cpsml_Condition, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
interval72: BinaryAssociation = BinaryAssociation(
    name="interval72",
    ends={
        Property(name="cpsml_Interval", type=cpsml_ODE, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_ODE73", type=cpsml_Interval, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
indevariable74: BinaryAssociation = BinaryAssociation(
    name="indevariable74",
    ends={
        Property(name="cpsml_IndeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function75", type=cpsml_IndeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
devariable76: BinaryAssociation = BinaryAssociation(
    name="devariable76",
    ends={
        Property(name="cpsml_DeVariable", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function77", type=cpsml_DeVariable, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fright78: BinaryAssociation = BinaryAssociation(
    name="fright78",
    ends={
        Property(name="cpsml_Fright", type=cpsml_Function, multiplicity=Multiplicity(1, 1)),
        Property(name="cpsml_Function79", type=cpsml_Fright, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_cpsml_ComTransition_Transition = Generalization(general=Transition, specific=cpsml_ComTransition)
gen_cpsml_ProbTransition_Transition = Generalization(general=Transition, specific=cpsml_ProbTransition)

# Domain Model
domain_model = DomainModel(
    name="cpsml",
    types={cpsml_System, cpsml_ODE, cpsml_Variable, cpsml_State, cpsml_Transition, cpsml_ComTransition, cpsml_ProbTransition, cpsml_Function, cpsml_Condition, Transition, cpsml_Interval, cpsml_IndeVariable, cpsml_DeVariable, cpsml_Fright},
    associations={ownedodes11, currentState13, ownedvariables0, relatedvariable1, ownedStates4, ownedTransitions6, initialState8, slaveode21, outgoingComTransitions24, incomingComTransitions26, fatherState16, ptok19, relatedvariable253, outgoingProbTransitions29, incomingProbTransitions32, subStates36, initialsubstate39, subtransitions41, subodes44, subrelatedvariables47, subrelatedvariable50, function68, csrc56, ctgt59, psrc62, ptgt65, condition70, interval72, indevariable74, devariable76, fright78},
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