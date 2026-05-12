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
EOperator: Enumeration = Enumeration(
    name="EOperator",
    literals={
            EnumerationLiteral(name="Add"),
			EnumerationLiteral(name="Subtract"),
			EnumerationLiteral(name="Multiply"),
			EnumerationLiteral(name="Divide"),
			EnumerationLiteral(name="LowerThan"),
			EnumerationLiteral(name="GreaterThan"),
			EnumerationLiteral(name="LowerEqual"),
			EnumerationLiteral(name="GreaterEqual"),
			EnumerationLiteral(name="Equal"),
			EnumerationLiteral(name="NotEqual"),
			EnumerationLiteral(name="Not"),
			EnumerationLiteral(name="Negate"),
			EnumerationLiteral(name="Or"),
			EnumerationLiteral(name="And")
    }
)

EType: Enumeration = Enumeration(
    name="EType",
    literals={
            EnumerationLiteral(name="TBool"),
			EnumerationLiteral(name="TInt")
    }
)

# Classes
model_expression_IntConst = Class(name="model_expression_IntConst")
model_expression_Operation = Class(name="model_expression_Operation")
model_component_Component = Class(name="model_component_Component")
INamedElement = Class(name="INamedElement")
Port = Class(name="Port")
model_INamedElement = Class(name="model_INamedElement", is_abstract=True)
model_expression_IExpressionTerm = Class(name="model_expression_IExpressionTerm", is_abstract=True)
model_expression_Var = Class(name="model_expression_Var")
IExpressionTerm = Class(name="IExpressionTerm")
model_expression_BoolConst = Class(name="model_expression_BoolConst")
TransitionSegment = Class(name="TransitionSegment")
model_state_State = Class(name="model_state_State")
TransitionSegmentSpecification = Class(name="TransitionSegmentSpecification")
model_state_TransitionSegment = Class(name="model_state_TransitionSegment")
model_state_TransitionSegmentSpecification = Class(name="model_state_TransitionSegmentSpecification")
Action = Class(name="Action")
model_state_DataStateVariable = Class(name="model_state_DataStateVariable")
model_state_Action = Class(name="model_state_Action")
Var = Class(name="Var")
StateAutomaton = Class(name="StateAutomaton")
model_component_Port = Class(name="model_component_Port", is_abstract=True)
model_component_InputPort = Class(name="model_component_InputPort")
model_component_OutputPort = Class(name="model_component_OutputPort")
model_state_StateAutomaton = Class(name="model_state_StateAutomaton")
State = Class(name="State")

# model_expression_IntConst class attributes and methods
model_expression_IntConst_value: Property = Property(name="value", type=IntegerType)
model_expression_IntConst.attributes={model_expression_IntConst_value}

# model_expression_Operation class attributes and methods
model_expression_Operation_operator: Property = Property(name="operator", type=StringType)
model_expression_Operation.attributes={model_expression_Operation_operator}

# model_component_Component class attributes and methods

# INamedElement class attributes and methods

# Port class attributes and methods

# model_INamedElement class attributes and methods
model_INamedElement_name: Property = Property(name="name", type=StringType)
model_INamedElement.attributes={model_INamedElement_name}

# model_expression_IExpressionTerm class attributes and methods

# model_expression_Var class attributes and methods
model_expression_Var_identifier: Property = Property(name="identifier", type=StringType)
model_expression_Var.attributes={model_expression_Var_identifier}

# IExpressionTerm class attributes and methods

# model_expression_BoolConst class attributes and methods
model_expression_BoolConst_value: Property = Property(name="value", type=BooleanType)
model_expression_BoolConst.attributes={model_expression_BoolConst_value}

# TransitionSegment class attributes and methods

# model_state_State class attributes and methods
model_state_State_isInitial: Property = Property(name="isInitial", type=BooleanType)
model_state_State.attributes={model_state_State_isInitial}

# TransitionSegmentSpecification class attributes and methods

# model_state_TransitionSegment class attributes and methods

# model_state_TransitionSegmentSpecification class attributes and methods

# Action class attributes and methods

# model_state_DataStateVariable class attributes and methods
model_state_DataStateVariable_type: Property = Property(name="type", type=StringType)
model_state_DataStateVariable.attributes={model_state_DataStateVariable_type}

# model_state_Action class attributes and methods

# Var class attributes and methods

# StateAutomaton class attributes and methods

# model_component_Port class attributes and methods
model_component_Port_type: Property = Property(name="type", type=StringType)
model_component_Port.attributes={model_component_Port_type}

# model_component_InputPort class attributes and methods

# model_component_OutputPort class attributes and methods

# model_state_StateAutomaton class attributes and methods

# State class attributes and methods

# Relationships
arguments0: BinaryAssociation = BinaryAssociation(
    name="arguments0",
    ends={
        Property(name="IExpressionTerm", type=model_expression_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="model_expression_Operation", type=IExpressionTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputPorts1: BinaryAssociation = BinaryAssociation(
    name="inputPorts1",
    ends={
        Property(name="Port", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component", type=Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitions10: BinaryAssociation = BinaryAssociation(
    name="transitions10",
    ends={
        Property(name="TransitionSegment", type=model_state_StateAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_StateAutomaton11", type=TransitionSegment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
idleTransitionsSpecifications12: BinaryAssociation = BinaryAssociation(
    name="idleTransitionsSpecifications12",
    ends={
        Property(name="TransitionSegmentSpecification", type=model_state_State, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_State", type=TransitionSegmentSpecification, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sourceState13: BinaryAssociation = BinaryAssociation(
    name="sourceState13",
    ends={
        Property(name="State14", type=model_state_TransitionSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_TransitionSegment", type=State, multiplicity=Multiplicity(0, 1))
    }
)
targetState15: BinaryAssociation = BinaryAssociation(
    name="targetState15",
    ends={
        Property(name="State17", type=model_state_TransitionSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_TransitionSegment16", type=State, multiplicity=Multiplicity(0, 1))
    }
)
transitionSegmentSpecification18: BinaryAssociation = BinaryAssociation(
    name="transitionSegmentSpecification18",
    ends={
        Property(name="TransitionSegmentSpecification20", type=model_state_TransitionSegment, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_TransitionSegment19", type=TransitionSegmentSpecification, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
guard21: BinaryAssociation = BinaryAssociation(
    name="guard21",
    ends={
        Property(name="IExpressionTerm22", type=model_state_TransitionSegmentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_TransitionSegmentSpecification", type=IExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
actions23: BinaryAssociation = BinaryAssociation(
    name="actions23",
    ends={
        Property(name="Action", type=model_state_TransitionSegmentSpecification, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_TransitionSegmentSpecification24", type=Action, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
initialValue25: BinaryAssociation = BinaryAssociation(
    name="initialValue25",
    ends={
        Property(name="IExpressionTerm26", type=model_state_DataStateVariable, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_DataStateVariable", type=IExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
variable27: BinaryAssociation = BinaryAssociation(
    name="variable27",
    ends={
        Property(name="Var", type=model_state_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_Action", type=Var, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outputPorts2: BinaryAssociation = BinaryAssociation(
    name="outputPorts2",
    ends={
        Property(name="Port4", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component3", type=Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateAutomaton5: BinaryAssociation = BinaryAssociation(
    name="stateAutomaton5",
    ends={
        Property(name="StateAutomaton", type=model_component_Component, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Component6", type=StateAutomaton, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
initialValue7: BinaryAssociation = BinaryAssociation(
    name="initialValue7",
    ends={
        Property(name="IExpressionTerm8", type=model_component_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="model_component_Port", type=IExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
states9: BinaryAssociation = BinaryAssociation(
    name="states9",
    ends={
        Property(name="State", type=model_state_StateAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_StateAutomaton", type=State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value28: BinaryAssociation = BinaryAssociation(
    name="value28",
    ends={
        Property(name="IExpressionTerm30", type=model_state_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="model_state_Action29", type=IExpressionTerm, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_model_expression_IntConst_IExpressionTerm = Generalization(general=IExpressionTerm, specific=model_expression_IntConst)
gen_model_expression_Operation_IExpressionTerm = Generalization(general=IExpressionTerm, specific=model_expression_Operation)
gen_model_component_Component_INamedElement = Generalization(general=INamedElement, specific=model_component_Component)
gen_model_expression_Var_IExpressionTerm = Generalization(general=IExpressionTerm, specific=model_expression_Var)
gen_model_expression_BoolConst_IExpressionTerm = Generalization(general=IExpressionTerm, specific=model_expression_BoolConst)
gen_model_state_State_INamedElement = Generalization(general=INamedElement, specific=model_state_State)
gen_model_state_TransitionSegment_INamedElement = Generalization(general=INamedElement, specific=model_state_TransitionSegment)
gen_model_state_DataStateVariable_INamedElement = Generalization(general=INamedElement, specific=model_state_DataStateVariable)
gen_model_component_Port_INamedElement = Generalization(general=INamedElement, specific=model_component_Port)
gen_model_component_InputPort_Port = Generalization(general=Port, specific=model_component_InputPort)
gen_model_component_OutputPort_Port = Generalization(general=Port, specific=model_component_OutputPort)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_expression_IntConst, model_expression_Operation, model_component_Component, INamedElement, Port, model_INamedElement, model_expression_IExpressionTerm, model_expression_Var, IExpressionTerm, model_expression_BoolConst, TransitionSegment, model_state_State, TransitionSegmentSpecification, model_state_TransitionSegment, model_state_TransitionSegmentSpecification, Action, model_state_DataStateVariable, model_state_Action, Var, StateAutomaton, model_component_Port, model_component_InputPort, model_component_OutputPort, model_state_StateAutomaton, State, EOperator, EType},
    associations={arguments0, inputPorts1, transitions10, idleTransitionsSpecifications12, sourceState13, targetState15, transitionSegmentSpecification18, guard21, actions23, initialValue25, variable27, outputPorts2, stateAutomaton5, initialValue7, states9, value28},
    generalizations={gen_model_expression_IntConst_IExpressionTerm, gen_model_expression_Operation_IExpressionTerm, gen_model_component_Component_INamedElement, gen_model_expression_Var_IExpressionTerm, gen_model_expression_BoolConst_IExpressionTerm, gen_model_state_State_INamedElement, gen_model_state_TransitionSegment_INamedElement, gen_model_state_DataStateVariable_INamedElement, gen_model_component_Port_INamedElement, gen_model_component_InputPort_Port, gen_model_component_OutputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)