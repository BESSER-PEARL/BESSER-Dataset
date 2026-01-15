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
TaskStatus: Enumeration = Enumeration(
    name="TaskStatus",
    literals={
            EnumerationLiteral(name="FINISHED"),
			EnumerationLiteral(name="PREPARED"),
			EnumerationLiteral(name="NOT_PREPARED"),
			EnumerationLiteral(name="PROCESSING")
    }
)

Language: Enumeration = Enumeration(
    name="Language",
    literals={
            EnumerationLiteral(name="Python"),
			EnumerationLiteral(name="Java")
    }
)

# Classes
workflow_TypedElement = Class(name="workflow::TypedElement")
workflow_NamedElement = Class(name="workflow::NamedElement")
workflow_SimpleTask = Class(name="workflow::SimpleTask", is_abstract=True)
AbstractTask = Class(name="AbstractTask")
workflow_AbstractTask = Class(name="workflow::AbstractTask", is_abstract=True)
NamedElement = Class(name="NamedElement")
workflow_TaskInput = Class(name="workflow::TaskInput", is_abstract=True)
workflow_TaskOutput = Class(name="workflow::TaskOutput")
workflow_CustomTask = Class(name="workflow::CustomTask")
workflow_Nsetter = Class(name="workflow::Nsetter")
Setter = Class(name="Setter")
workflow_IsInitSetter = Class(name="workflow::IsInitSetter")
Nsetter = Class(name="Nsetter")
workflow_IsNotInitSetter = Class(name="workflow::IsNotInitSetter")
IsInitSetter = Class(name="IsInitSetter")
workflow_BaseTask = Class(name="workflow::BaseTask")
TypedElement = Class(name="TypedElement")
workflow_LibraryFunction = Class(name="workflow::LibraryFunction")
workflow_Output = Class(name="workflow::Output")
workflow_Input = Class(name="workflow::Input")
workflow_LibraryTask = Class(name="workflow::LibraryTask")
SimpleTask = Class(name="SimpleTask")
workflow_Workflow = Class(name="workflow::Workflow")
workflow_Setter = Class(name="workflow::Setter")
TaskInput = Class(name="TaskInput")
workflow_Connection = Class(name="workflow::Connection")

# workflow_TypedElement class attributes and methods
workflow_TypedElement_typeAsString: Property = Property(name="typeAsString", type=StringType)
workflow_TypedElement_valueAsString: Property = Property(name="valueAsString", type=StringType)
workflow_TypedElement.attributes={workflow_TypedElement_typeAsString, workflow_TypedElement_valueAsString}

# workflow_NamedElement class attributes and methods
workflow_NamedElement_name: Property = Property(name="name", type=StringType)
workflow_NamedElement.attributes={workflow_NamedElement_name}

# workflow_SimpleTask class attributes and methods

# AbstractTask class attributes and methods

# workflow_AbstractTask class attributes and methods
workflow_AbstractTask_status: Property = Property(name="status", type=StringType)
workflow_AbstractTask.attributes={workflow_AbstractTask_status}

# NamedElement class attributes and methods

# workflow_TaskInput class attributes and methods

# workflow_TaskOutput class attributes and methods

# workflow_CustomTask class attributes and methods
workflow_CustomTask_runner: Property = Property(name="runner", type=StringType)
workflow_CustomTask.attributes={workflow_CustomTask_runner}

# workflow_Nsetter class attributes and methods

# Setter class attributes and methods

# workflow_IsInitSetter class attributes and methods

# Nsetter class attributes and methods

# workflow_IsNotInitSetter class attributes and methods

# IsInitSetter class attributes and methods

# workflow_BaseTask class attributes and methods

# TypedElement class attributes and methods

# workflow_LibraryFunction class attributes and methods
workflow_LibraryFunction_function: Property = Property(name="function", type=StringType)
workflow_LibraryFunction.attributes={workflow_LibraryFunction_function}

# workflow_Output class attributes and methods

# workflow_Input class attributes and methods

# workflow_LibraryTask class attributes and methods

# SimpleTask class attributes and methods

# workflow_Workflow class attributes and methods
workflow_Workflow_language: Property = Property(name="language", type=StringType)
workflow_Workflow.attributes={workflow_Workflow_language}

# workflow_Setter class attributes and methods

# TaskInput class attributes and methods

# workflow_Connection class attributes and methods

# Relationships
inputs0: BinaryAssociation = BinaryAssociation(
    name="inputs0",
    ends={
        Property(name="workflow_TaskInput", type=workflow_AbstractTask, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_AbstractTask", type=workflow_TaskInput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs1: BinaryAssociation = BinaryAssociation(
    name="outputs1",
    ends={
        Property(name="workflow_TaskOutput", type=workflow_AbstractTask, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_AbstractTask2", type=workflow_TaskOutput, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="workflow_AbstractTask4", type=workflow_BaseTask, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_BaseTask", type=workflow_AbstractTask, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outputs5: BinaryAssociation = BinaryAssociation(
    name="outputs5",
    ends={
        Property(name="workflow_Output", type=workflow_LibraryFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_LibraryFunction", type=workflow_Output, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
inputs6: BinaryAssociation = BinaryAssociation(
    name="inputs6",
    ends={
        Property(name="workflow_Input", type=workflow_LibraryFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_LibraryFunction7", type=workflow_Input, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
libraryfunction8: BinaryAssociation = BinaryAssociation(
    name="libraryfunction8",
    ends={
        Property(name="workflow_LibraryFunction9", type=workflow_LibraryTask, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_LibraryTask", type=workflow_LibraryFunction, multiplicity=Multiplicity(1, 1))
    }
)
baseTask10: BinaryAssociation = BinaryAssociation(
    name="baseTask10",
    ends={
        Property(name="workflow_BaseTask11", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Workflow", type=workflow_BaseTask, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
functions12: BinaryAssociation = BinaryAssociation(
    name="functions12",
    ends={
        Property(name="workflow_LibraryFunction14", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Workflow13", type=workflow_LibraryFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
taskoutput15: BinaryAssociation = BinaryAssociation(
    name="taskoutput15",
    ends={
        Property(name="workflow_TaskOutput16", type=workflow_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Connection", type=workflow_TaskOutput, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_workflow_SimpleTask_AbstractTask = Generalization(general=AbstractTask, specific=workflow_SimpleTask)
gen_workflow_AbstractTask_NamedElement = Generalization(general=NamedElement, specific=workflow_AbstractTask)
gen_workflow_CustomTask_SimpleTask = Generalization(general=SimpleTask, specific=workflow_CustomTask)
gen_workflow_Nsetter_Setter = Generalization(general=Setter, specific=workflow_Nsetter)
gen_workflow_IsInitSetter_Nsetter = Generalization(general=Nsetter, specific=workflow_IsInitSetter)
gen_workflow_IsNotInitSetter_IsInitSetter = Generalization(general=IsInitSetter, specific=workflow_IsNotInitSetter)
gen_workflow_Input_TypedElement = Generalization(general=TypedElement, specific=workflow_Input)
gen_workflow_Input_NamedElement = Generalization(general=NamedElement, specific=workflow_Input)
gen_workflow_BaseTask_AbstractTask = Generalization(general=AbstractTask, specific=workflow_BaseTask)
gen_workflow_TaskOutput_NamedElement = Generalization(general=NamedElement, specific=workflow_TaskOutput)
gen_workflow_TaskOutput_TypedElement = Generalization(general=TypedElement, specific=workflow_TaskOutput)
gen_workflow_TaskInput_NamedElement = Generalization(general=NamedElement, specific=workflow_TaskInput)
gen_workflow_LibraryFunction_NamedElement = Generalization(general=NamedElement, specific=workflow_LibraryFunction)
gen_workflow_LibraryTask_SimpleTask = Generalization(general=SimpleTask, specific=workflow_LibraryTask)
gen_workflow_Workflow_NamedElement = Generalization(general=NamedElement, specific=workflow_Workflow)
gen_workflow_Setter_TypedElement = Generalization(general=TypedElement, specific=workflow_Setter)
gen_workflow_Setter_TaskInput = Generalization(general=TaskInput, specific=workflow_Setter)
gen_workflow_Connection_TaskInput = Generalization(general=TaskInput, specific=workflow_Connection)
gen_workflow_Output_NamedElement = Generalization(general=NamedElement, specific=workflow_Output)
gen_workflow_Output_TypedElement = Generalization(general=TypedElement, specific=workflow_Output)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_TypedElement, workflow_NamedElement, workflow_SimpleTask, AbstractTask, workflow_AbstractTask, NamedElement, workflow_TaskInput, workflow_TaskOutput, workflow_CustomTask, workflow_Nsetter, Setter, workflow_IsInitSetter, Nsetter, workflow_IsNotInitSetter, IsInitSetter, workflow_BaseTask, TypedElement, workflow_LibraryFunction, workflow_Output, workflow_Input, workflow_LibraryTask, SimpleTask, workflow_Workflow, workflow_Setter, TaskInput, workflow_Connection, TaskStatus, Language},
    associations={inputs0, outputs1, children3, outputs5, inputs6, libraryfunction8, baseTask10, functions12, taskoutput15},
    generalizations={gen_workflow_SimpleTask_AbstractTask, gen_workflow_AbstractTask_NamedElement, gen_workflow_CustomTask_SimpleTask, gen_workflow_Nsetter_Setter, gen_workflow_IsInitSetter_Nsetter, gen_workflow_IsNotInitSetter_IsInitSetter, gen_workflow_Input_TypedElement, gen_workflow_Input_NamedElement, gen_workflow_BaseTask_AbstractTask, gen_workflow_TaskOutput_NamedElement, gen_workflow_TaskOutput_TypedElement, gen_workflow_TaskInput_NamedElement, gen_workflow_LibraryFunction_NamedElement, gen_workflow_LibraryTask_SimpleTask, gen_workflow_Workflow_NamedElement, gen_workflow_Setter_TypedElement, gen_workflow_Setter_TaskInput, gen_workflow_Connection_TaskInput, gen_workflow_Output_NamedElement, gen_workflow_Output_TypedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)