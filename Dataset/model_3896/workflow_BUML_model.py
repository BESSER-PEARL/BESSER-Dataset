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
workflow_Workflow = Class(name="workflow::Workflow")
workflow_Recipe = Class(name="workflow::Recipe")
workflow_Statement = Class(name="workflow::Statement", is_abstract=True)
workflow_Parameter = Class(name="workflow::Parameter", is_abstract=True)
workflow_Condition = Class(name="workflow::Condition")
Statement = Class(name="Statement")
workflow_Program = Class(name="workflow::Program")
Parameter_ = Class(name="Parameter")
workflow_OutputParameter = Class(name="workflow::OutputParameter")
workflow_ForEach = Class(name="workflow::ForEach")
workflow_SimpleCommand = Class(name="workflow::SimpleCommand")
workflow_InputParameter = Class(name="workflow::InputParameter")

# workflow_Workflow class attributes and methods
workflow_Workflow_name: Property = Property(name="name", type=StringType)
workflow_Workflow.attributes={workflow_Workflow_name}

# workflow_Recipe class attributes and methods
workflow_Recipe_name: Property = Property(name="name", type=StringType)
workflow_Recipe.attributes={workflow_Recipe_name}

# workflow_Statement class attributes and methods
workflow_Statement_exec_order: Property = Property(name="exec_order", type=IntegerType)
workflow_Statement.attributes={workflow_Statement_exec_order}

# workflow_Parameter class attributes and methods
workflow_Parameter_option: Property = Property(name="option", type=StringType)
workflow_Parameter_data: Property = Property(name="data", type=StringType)
workflow_Parameter.attributes={workflow_Parameter_option, workflow_Parameter_data}

# workflow_Condition class attributes and methods
workflow_Condition_description: Property = Property(name="description", type=StringType)
workflow_Condition_expression: Property = Property(name="expression", type=StringType)
workflow_Condition.attributes={workflow_Condition_description, workflow_Condition_expression}

# Statement class attributes and methods

# workflow_Program class attributes and methods
workflow_Program_name_exec: Property = Property(name="name_exec", type=StringType)
workflow_Program_description: Property = Property(name="description", type=StringType)
workflow_Program_exec_order: Property = Property(name="exec_order", type=IntegerType)
workflow_Program.attributes={workflow_Program_exec_order, workflow_Program_description, workflow_Program_name_exec}

# Parameter class attributes and methods

# workflow_OutputParameter class attributes and methods

# workflow_ForEach class attributes and methods
workflow_ForEach_element: Property = Property(name="element", type=StringType)
workflow_ForEach_sequence: Property = Property(name="sequence", type=StringType)
workflow_ForEach.attributes={workflow_ForEach_element, workflow_ForEach_sequence}

# workflow_SimpleCommand class attributes and methods
workflow_SimpleCommand_description: Property = Property(name="description", type=StringType)
workflow_SimpleCommand.attributes={workflow_SimpleCommand_description}

# workflow_InputParameter class attributes and methods

# Relationships
recipes0: BinaryAssociation = BinaryAssociation(
    name="recipes0",
    ends={
        Property(name="workflow_Recipe", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Workflow", type=workflow_Recipe, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
commands1: BinaryAssociation = BinaryAssociation(
    name="commands1",
    ends={
        Property(name="workflow_Statement", type=workflow_Recipe, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Recipe2", type=workflow_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
then_branch3: BinaryAssociation = BinaryAssociation(
    name="then_branch3",
    ends={
        Property(name="workflow_Statement4", type=workflow_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Condition", type=workflow_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
else_branch5: BinaryAssociation = BinaryAssociation(
    name="else_branch5",
    ends={
        Property(name="workflow_Statement7", type=workflow_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Condition6", type=workflow_Statement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
link_to_outputparameter11: BinaryAssociation = BinaryAssociation(
    name="link_to_outputparameter11",
    ends={
        Property(name="workflow_OutputParameter", type=workflow_InputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_InputParameter", type=workflow_OutputParameter, multiplicity=Multiplicity(0, 1))
    }
)
link_to_inputparameter12: BinaryAssociation = BinaryAssociation(
    name="link_to_inputparameter12",
    ends={
        Property(name="workflow_InputParameter14", type=workflow_OutputParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_OutputParameter13", type=workflow_InputParameter, multiplicity=Multiplicity(0, 1))
    }
)
statements15: BinaryAssociation = BinaryAssociation(
    name="statements15",
    ends={
        Property(name="workflow_Statement16", type=workflow_ForEach, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_ForEach", type=workflow_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters8: BinaryAssociation = BinaryAssociation(
    name="parameters8",
    ends={
        Property(name="workflow_Parameter", type=workflow_Program, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Program", type=workflow_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
programs9: BinaryAssociation = BinaryAssociation(
    name="programs9",
    ends={
        Property(name="workflow_Program10", type=workflow_SimpleCommand, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_SimpleCommand", type=workflow_Program, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_workflow_Condition_Statement = Generalization(general=Statement, specific=workflow_Condition)
gen_workflow_InputParameter_Parameter = Generalization(general=Parameter_, specific=workflow_InputParameter)
gen_workflow_OutputParameter_Parameter = Generalization(general=Parameter_, specific=workflow_OutputParameter)
gen_workflow_ForEach_Statement = Generalization(general=Statement, specific=workflow_ForEach)
gen_workflow_SimpleCommand_Statement = Generalization(general=Statement, specific=workflow_SimpleCommand)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_Workflow, workflow_Recipe, workflow_Statement, workflow_Parameter, workflow_Condition, Statement, workflow_Program, Parameter_, workflow_OutputParameter, workflow_ForEach, workflow_SimpleCommand, workflow_InputParameter},
    associations={recipes0, commands1, then_branch3, else_branch5, link_to_outputparameter11, link_to_inputparameter12, statements15, parameters8, programs9},
    generalizations={gen_workflow_Condition_Statement, gen_workflow_InputParameter_Parameter, gen_workflow_OutputParameter_Parameter, gen_workflow_ForEach_Statement, gen_workflow_SimpleCommand_Statement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)