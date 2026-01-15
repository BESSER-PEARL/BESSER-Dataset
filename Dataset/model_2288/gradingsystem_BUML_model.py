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
MinRequirementsType: Enumeration = Enumeration(
    name="MinRequirementsType",
    literals={
            EnumerationLiteral(name="Percentage"),
			EnumerationLiteral(name="Absolute")
    }
)

# Classes
gradingsystem_GradingSystem = Class(name="gradingsystem::GradingSystem")
gradingsystem_Course = Class(name="gradingsystem::Course")
gradingsystem_Grading = Class(name="gradingsystem::Grading")
gradingsystem_MinRequirement = Class(name="gradingsystem::MinRequirement")
gradingsystem_ConcreteTask = Class(name="gradingsystem::ConcreteTask")
Task = Class(name="Task")
gradingsystem_TaskGroup = Class(name="gradingsystem::TaskGroup")
gradingsystem_GradingScheme = Class(name="gradingsystem::GradingScheme")
gradingsystem_Grade = Class(name="gradingsystem::Grade")
gradingsystem_Task = Class(name="gradingsystem::Task", is_abstract=True)

# gradingsystem_GradingSystem class attributes and methods

# gradingsystem_Course class attributes and methods
gradingsystem_Course_name: Property = Property(name="name", type=StringType)
gradingsystem_Course.attributes={gradingsystem_Course_name}

# gradingsystem_Grading class attributes and methods
gradingsystem_Grading_semester: Property = Property(name="semester", type=StringType)
gradingsystem_Grading.attributes={gradingsystem_Grading_semester}

# gradingsystem_MinRequirement class attributes and methods
gradingsystem_MinRequirement_value: Property = Property(name="value", type=IntegerType)
gradingsystem_MinRequirement_type: Property = Property(name="type", type=StringType)
gradingsystem_MinRequirement.attributes={gradingsystem_MinRequirement_type, gradingsystem_MinRequirement_value}

# gradingsystem_ConcreteTask class attributes and methods
gradingsystem_ConcreteTask_maxPoints: Property = Property(name="maxPoints", type=IntegerType)
gradingsystem_ConcreteTask.attributes={gradingsystem_ConcreteTask_maxPoints}

# Task class attributes and methods

# gradingsystem_TaskGroup class attributes and methods

# gradingsystem_GradingScheme class attributes and methods

# gradingsystem_Grade class attributes and methods
gradingsystem_Grade_name: Property = Property(name="name", type=StringType)
gradingsystem_Grade_requiredPoints: Property = Property(name="requiredPoints", type=IntegerType)
gradingsystem_Grade.attributes={gradingsystem_Grade_requiredPoints, gradingsystem_Grade_name}

# gradingsystem_Task class attributes and methods
gradingsystem_Task_name: Property = Property(name="name", type=StringType)
gradingsystem_Task.attributes={gradingsystem_Task_name}

# Relationships
courses0: BinaryAssociation = BinaryAssociation(
    name="courses0",
    ends={
        Property(name="gradingsystem_Course", type=gradingsystem_GradingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_GradingSystem", type=gradingsystem_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
minRequirement3: BinaryAssociation = BinaryAssociation(
    name="minRequirement3",
    ends={
        Property(name="gradingsystem_MinRequirement", type=gradingsystem_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_Task", type=gradingsystem_MinRequirement, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contains4: BinaryAssociation = BinaryAssociation(
    name="contains4",
    ends={
        Property(name="gradingsystem_Task5", type=gradingsystem_TaskGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_TaskGroup", type=gradingsystem_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
grades6: BinaryAssociation = BinaryAssociation(
    name="grades6",
    ends={
        Property(name="gradingsystem_Grade", type=gradingsystem_GradingScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_GradingScheme", type=gradingsystem_Grade, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
minRequirementNotFulfilledGrade7: BinaryAssociation = BinaryAssociation(
    name="minRequirementNotFulfilledGrade7",
    ends={
        Property(name="gradingsystem_Grade9", type=gradingsystem_GradingScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_GradingScheme8", type=gradingsystem_Grade, multiplicity=Multiplicity(1, 1))
    }
)
gradings1: BinaryAssociation = BinaryAssociation(
    name="gradings1",
    ends={
        Property(name="gradingsystem_Grading", type=gradingsystem_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_Course2", type=gradingsystem_Grading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tasks10: BinaryAssociation = BinaryAssociation(
    name="tasks10",
    ends={
        Property(name="gradingsystem_Task12", type=gradingsystem_Grading, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_Grading11", type=gradingsystem_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
gradingScheme13: BinaryAssociation = BinaryAssociation(
    name="gradingScheme13",
    ends={
        Property(name="gradingsystem_GradingScheme15", type=gradingsystem_Grading, multiplicity=Multiplicity(1, 1)),
        Property(name="gradingsystem_Grading14", type=gradingsystem_GradingScheme, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)

# Generalizations
gen_gradingsystem_ConcreteTask_Task = Generalization(general=Task, specific=gradingsystem_ConcreteTask)
gen_gradingsystem_TaskGroup_Task = Generalization(general=Task, specific=gradingsystem_TaskGroup)

# Domain Model
domain_model = DomainModel(
    name="gradingsystem",
    types={gradingsystem_GradingSystem, gradingsystem_Course, gradingsystem_Grading, gradingsystem_MinRequirement, gradingsystem_ConcreteTask, Task, gradingsystem_TaskGroup, gradingsystem_GradingScheme, gradingsystem_Grade, gradingsystem_Task, MinRequirementsType},
    associations={courses0, minRequirement3, contains4, grades6, minRequirementNotFulfilledGrade7, gradings1, tasks10, gradingScheme13},
    generalizations={gen_gradingsystem_ConcreteTask_Task, gen_gradingsystem_TaskGroup_Task},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)