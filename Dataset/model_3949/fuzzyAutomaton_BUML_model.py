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
TNormType: Enumeration = Enumeration(
    name="TNormType",
    literals={
            EnumerationLiteral(name="HAMACHER"),
			EnumerationLiteral(name="GODEL")
    }
)

FuzzyRelationType: Enumeration = Enumeration(
    name="FuzzyRelationType",
    literals={
            EnumerationLiteral(name="EQ"),
			EnumerationLiteral(name="GTE"),
			EnumerationLiteral(name="LTE"),
			EnumerationLiteral(name="TERN")
    }
)

# Classes
fuzzyAutomaton_FuzzyAutomaton = Class(name="fuzzyAutomaton::FuzzyAutomaton")
fuzzyAutomaton_State = Class(name="fuzzyAutomaton::State")
fuzzyAutomaton_Transition = Class(name="fuzzyAutomaton::Transition")
fuzzyAutomaton_VariableSet = Class(name="fuzzyAutomaton::VariableSet")
fuzzyAutomaton_TransitionFeature = Class(name="fuzzyAutomaton::TransitionFeature")
fuzzyAutomaton_Variable = Class(name="fuzzyAutomaton::Variable")
fuzzyAutomaton_FuzzyConstraint = Class(name="fuzzyAutomaton::FuzzyConstraint")
fuzzyAutomaton_VarTransformation = Class(name="fuzzyAutomaton::VarTransformation")
fuzzyAutomaton_Input = Class(name="fuzzyAutomaton::Input")
Action = Class(name="Action")
fuzzyAutomaton_Action = Class(name="fuzzyAutomaton::Action", is_abstract=True)
fuzzyAutomaton_Output = Class(name="fuzzyAutomaton::Output")
fuzzyAutomaton_FuzzyRelation = Class(name="fuzzyAutomaton::FuzzyRelation")
fuzzyAutomaton_VarUpdate = Class(name="fuzzyAutomaton::VarUpdate")

# fuzzyAutomaton_FuzzyAutomaton class attributes and methods
fuzzyAutomaton_FuzzyAutomaton_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_FuzzyAutomaton_tNorm: Property = Property(name="tNorm", type=StringType)
fuzzyAutomaton_FuzzyAutomaton.attributes={fuzzyAutomaton_FuzzyAutomaton_name, fuzzyAutomaton_FuzzyAutomaton_tNorm}

# fuzzyAutomaton_State class attributes and methods
fuzzyAutomaton_State_isInitial: Property = Property(name="isInitial", type=StringType)
fuzzyAutomaton_State.attributes={fuzzyAutomaton_State_isInitial}

# fuzzyAutomaton_Transition class attributes and methods

# fuzzyAutomaton_VariableSet class attributes and methods
fuzzyAutomaton_VariableSet_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_VariableSet.attributes={fuzzyAutomaton_VariableSet_name}

# fuzzyAutomaton_TransitionFeature class attributes and methods
fuzzyAutomaton_TransitionFeature_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_TransitionFeature.attributes={fuzzyAutomaton_TransitionFeature_name}

# fuzzyAutomaton_Variable class attributes and methods
fuzzyAutomaton_Variable_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_Variable_value: Property = Property(name="value", type=StringType)
fuzzyAutomaton_Variable.attributes={fuzzyAutomaton_Variable_value, fuzzyAutomaton_Variable_name}

# fuzzyAutomaton_FuzzyConstraint class attributes and methods
fuzzyAutomaton_FuzzyConstraint_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_FuzzyConstraint_tNorm: Property = Property(name="tNorm", type=StringType)
fuzzyAutomaton_FuzzyConstraint.attributes={fuzzyAutomaton_FuzzyConstraint_tNorm, fuzzyAutomaton_FuzzyConstraint_name}

# fuzzyAutomaton_VarTransformation class attributes and methods
fuzzyAutomaton_VarTransformation_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_VarTransformation.attributes={fuzzyAutomaton_VarTransformation_name}

# fuzzyAutomaton_Input class attributes and methods

# Action class attributes and methods

# fuzzyAutomaton_Action class attributes and methods
fuzzyAutomaton_Action_name: Property = Property(name="name", type=StringType)
fuzzyAutomaton_Action.attributes={fuzzyAutomaton_Action_name}

# fuzzyAutomaton_Output class attributes and methods
fuzzyAutomaton_Output_expression: Property = Property(name="expression", type=StringType)
fuzzyAutomaton_Output.attributes={fuzzyAutomaton_Output_expression}

# fuzzyAutomaton_FuzzyRelation class attributes and methods
fuzzyAutomaton_FuzzyRelation_tFRelation: Property = Property(name="tFRelation", type=StringType)
fuzzyAutomaton_FuzzyRelation_expression1: Property = Property(name="expression1", type=StringType)
fuzzyAutomaton_FuzzyRelation_expression2: Property = Property(name="expression2", type=StringType)
fuzzyAutomaton_FuzzyRelation_expression3: Property = Property(name="expression3", type=StringType)
fuzzyAutomaton_FuzzyRelation_delta: Property = Property(name="delta", type=StringType)
fuzzyAutomaton_FuzzyRelation.attributes={fuzzyAutomaton_FuzzyRelation_expression3, fuzzyAutomaton_FuzzyRelation_tFRelation, fuzzyAutomaton_FuzzyRelation_expression1, fuzzyAutomaton_FuzzyRelation_delta, fuzzyAutomaton_FuzzyRelation_expression2}

# fuzzyAutomaton_VarUpdate class attributes and methods
fuzzyAutomaton_VarUpdate_expression: Property = Property(name="expression", type=StringType)
fuzzyAutomaton_VarUpdate.attributes={fuzzyAutomaton_VarUpdate_expression}

# Relationships
states0: BinaryAssociation = BinaryAssociation(
    name="states0",
    ends={
        Property(name="fuzzyAutomaton_State", type=fuzzyAutomaton_FuzzyAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_FuzzyAutomaton", type=fuzzyAutomaton_State, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="fuzzyAutomaton_Transition", type=fuzzyAutomaton_FuzzyAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_FuzzyAutomaton2", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variableSet3: BinaryAssociation = BinaryAssociation(
    name="variableSet3",
    ends={
        Property(name="fuzzyAutomaton_VariableSet", type=fuzzyAutomaton_FuzzyAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_FuzzyAutomaton4", type=fuzzyAutomaton_VariableSet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="State", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fuzzyAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="State12", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fuzzyAutomaton_State, multiplicity=Multiplicity(1, 1))
    }
)
feature13: BinaryAssociation = BinaryAssociation(
    name="feature13",
    ends={
        Property(name="TransitionFeature", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="featureToTransition", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 1))
    }
)
variables14: BinaryAssociation = BinaryAssociation(
    name="variables14",
    ends={
        Property(name="fuzzyAutomaton_Variable", type=fuzzyAutomaton_VariableSet, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_VariableSet15", type=fuzzyAutomaton_Variable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
transitionFeatures5: BinaryAssociation = BinaryAssociation(
    name="transitionFeatures5",
    ends={
        Property(name="fuzzyAutomaton_TransitionFeature", type=fuzzyAutomaton_FuzzyAutomaton, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_FuzzyAutomaton6", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
incoming7: BinaryAssociation = BinaryAssociation(
    name="incoming7",
    ends={
        Property(name="Transition", type=fuzzyAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing8: BinaryAssociation = BinaryAssociation(
    name="outgoing8",
    ends={
        Property(name="Transition9", type=fuzzyAutomaton_State, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(0, 9999))
    }
)
fuzzyConstraint20: BinaryAssociation = BinaryAssociation(
    name="fuzzyConstraint20",
    ends={
        Property(name="fuzzyAutomaton_FuzzyConstraint", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_TransitionFeature21", type=fuzzyAutomaton_FuzzyConstraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
varTransformation22: BinaryAssociation = BinaryAssociation(
    name="varTransformation22",
    ends={
        Property(name="fuzzyAutomaton_VarTransformation", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_TransitionFeature23", type=fuzzyAutomaton_VarTransformation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parameters24: BinaryAssociation = BinaryAssociation(
    name="parameters24",
    ends={
        Property(name="fuzzyAutomaton_Variable25", type=fuzzyAutomaton_Input, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_Input", type=fuzzyAutomaton_Variable, multiplicity=Multiplicity(0, 9999))
    }
)
featureToTransition16: BinaryAssociation = BinaryAssociation(
    name="featureToTransition16",
    ends={
        Property(name="Transition17", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="feature", type=fuzzyAutomaton_Transition, multiplicity=Multiplicity(1, 9999))
    }
)
action18: BinaryAssociation = BinaryAssociation(
    name="action18",
    ends={
        Property(name="fuzzyAutomaton_Action", type=fuzzyAutomaton_TransitionFeature, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_TransitionFeature19", type=fuzzyAutomaton_Action, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fuzzyRelations26: BinaryAssociation = BinaryAssociation(
    name="fuzzyRelations26",
    ends={
        Property(name="fuzzyAutomaton_FuzzyRelation", type=fuzzyAutomaton_FuzzyConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_FuzzyConstraint27", type=fuzzyAutomaton_FuzzyRelation, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
varUpdates28: BinaryAssociation = BinaryAssociation(
    name="varUpdates28",
    ends={
        Property(name="fuzzyAutomaton_VarUpdate", type=fuzzyAutomaton_VarTransformation, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_VarTransformation29", type=fuzzyAutomaton_VarUpdate, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
variable30: BinaryAssociation = BinaryAssociation(
    name="variable30",
    ends={
        Property(name="fuzzyAutomaton_Variable32", type=fuzzyAutomaton_VarUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="fuzzyAutomaton_VarUpdate31", type=fuzzyAutomaton_Variable, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_fuzzyAutomaton_Input_Action = Generalization(general=Action, specific=fuzzyAutomaton_Input)
gen_fuzzyAutomaton_Output_Action = Generalization(general=Action, specific=fuzzyAutomaton_Output)

# Domain Model
domain_model = DomainModel(
    name="fuzzyAutomaton",
    types={fuzzyAutomaton_FuzzyAutomaton, fuzzyAutomaton_State, fuzzyAutomaton_Transition, fuzzyAutomaton_VariableSet, fuzzyAutomaton_TransitionFeature, fuzzyAutomaton_Variable, fuzzyAutomaton_FuzzyConstraint, fuzzyAutomaton_VarTransformation, fuzzyAutomaton_Input, Action, fuzzyAutomaton_Action, fuzzyAutomaton_Output, fuzzyAutomaton_FuzzyRelation, fuzzyAutomaton_VarUpdate, TNormType, FuzzyRelationType},
    associations={states0, transitions1, variableSet3, source10, target11, feature13, variables14, transitionFeatures5, incoming7, outgoing8, fuzzyConstraint20, varTransformation22, parameters24, featureToTransition16, action18, fuzzyRelations26, varUpdates28, variable30},
    generalizations={gen_fuzzyAutomaton_Input_Action, gen_fuzzyAutomaton_Output_Action},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)