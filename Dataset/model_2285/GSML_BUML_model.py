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
MinRequirementType: Enumeration = Enumeration(
    name="MinRequirementType",
    literals={
            EnumerationLiteral(name="Absolute"),
			EnumerationLiteral(name="Relative")
    }
)

# Classes
gsml_Course = Class(name="gsml::Course")
gsml_Task = Class(name="gsml::Task", is_abstract=True)
gsml_Grading = Class(name="gsml::Grading")
gsml_GradingScheme = Class(name="gsml::GradingScheme")
gsml_Grade = Class(name="gsml::Grade")
gsml_ConcreteTask = Class(name="gsml::ConcreteTask")
Task = Class(name="Task")
gsml_TaskGroup = Class(name="gsml::TaskGroup")
gsml_GradingSystem = Class(name="gsml::GradingSystem")

# gsml_Course class attributes and methods
gsml_Course_Name: Property = Property(name="Name", type=StringType)
gsml_Course.attributes={gsml_Course_Name}

# gsml_Task class attributes and methods
gsml_Task_Name: Property = Property(name="Name", type=StringType)
gsml_Task_MinRequirement: Property = Property(name="MinRequirement", type=FloatType)
gsml_Task_MinRequirementType: Property = Property(name="MinRequirementType", type=StringType)
gsml_Task.attributes={gsml_Task_MinRequirement, gsml_Task_Name, gsml_Task_MinRequirementType}

# gsml_Grading class attributes and methods
gsml_Grading_Semester: Property = Property(name="Semester", type=StringType)
gsml_Grading.attributes={gsml_Grading_Semester}

# gsml_GradingScheme class attributes and methods

# gsml_Grade class attributes and methods
gsml_Grade_Name: Property = Property(name="Name", type=StringType)
gsml_Grade_RequiredPoints: Property = Property(name="RequiredPoints", type=FloatType)
gsml_Grade.attributes={gsml_Grade_Name, gsml_Grade_RequiredPoints}

# gsml_ConcreteTask class attributes and methods
gsml_ConcreteTask_MaxPoints: Property = Property(name="MaxPoints", type=FloatType)
gsml_ConcreteTask.attributes={gsml_ConcreteTask_MaxPoints}

# Task class attributes and methods

# gsml_TaskGroup class attributes and methods

# gsml_GradingSystem class attributes and methods

# Relationships
gradingScheme6: BinaryAssociation = BinaryAssociation(
    name="gradingScheme6",
    ends={
        Property(name="gsml_GradingScheme8", type=gsml_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Course7", type=gsml_GradingScheme, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
gradings0: BinaryAssociation = BinaryAssociation(
    name="gradings0",
    ends={
        Property(name="gsml_Grading", type=gsml_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Course", type=gsml_Grading, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gradingschemes1: BinaryAssociation = BinaryAssociation(
    name="gradingschemes1",
    ends={
        Property(name="gsml_GradingScheme", type=gsml_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Course2", type=gsml_GradingScheme, multiplicity=Multiplicity(0, 9999))
    }
)
gradingscheme3: BinaryAssociation = BinaryAssociation(
    name="gradingscheme3",
    ends={
        Property(name="gsml_GradingScheme5", type=gsml_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Course4", type=gsml_GradingScheme, multiplicity=Multiplicity(1, 1))
    }
)
contains9: BinaryAssociation = BinaryAssociation(
    name="contains9",
    ends={
        Property(name="gsml_Task", type=gsml_TaskGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_TaskGroup", type=gsml_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
gradingscheme17: BinaryAssociation = BinaryAssociation(
    name="gradingscheme17",
    ends={
        Property(name="gsml_GradingScheme19", type=gsml_Grading, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Grading18", type=gsml_GradingScheme, multiplicity=Multiplicity(1, 1))
    }
)
tasks20: BinaryAssociation = BinaryAssociation(
    name="tasks20",
    ends={
        Property(name="gsml_Task22", type=gsml_Grading, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Grading21", type=gsml_Task, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
grades10: BinaryAssociation = BinaryAssociation(
    name="grades10",
    ends={
        Property(name="gsml_Grade", type=gsml_GradingScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_GradingScheme11", type=gsml_Grade, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fallback12: BinaryAssociation = BinaryAssociation(
    name="fallback12",
    ends={
        Property(name="gsml_Grade14", type=gsml_GradingScheme, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_GradingScheme13", type=gsml_Grade, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
courses15: BinaryAssociation = BinaryAssociation(
    name="courses15",
    ends={
        Property(name="gsml_Course16", type=gsml_GradingSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_GradingSystem", type=gsml_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
has23: BinaryAssociation = BinaryAssociation(
    name="has23",
    ends={
        Property(name="gsml_Task25", type=gsml_Grading, multiplicity=Multiplicity(1, 1)),
        Property(name="gsml_Grading24", type=gsml_Task, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_gsml_ConcreteTask_Task = Generalization(general=Task, specific=gsml_ConcreteTask)
gen_gsml_TaskGroup_Task = Generalization(general=Task, specific=gsml_TaskGroup)

# Domain Model
domain_model = DomainModel(
    name="gsml",
    types={gsml_Course, gsml_Task, gsml_Grading, gsml_GradingScheme, gsml_Grade, gsml_ConcreteTask, Task, gsml_TaskGroup, gsml_GradingSystem, MinRequirementType},
    associations={gradingScheme6, gradings0, gradingschemes1, gradingscheme3, contains9, gradingscheme17, tasks20, grades10, fallback12, courses15, has23},
    generalizations={gen_gsml_ConcreteTask_Task, gen_gsml_TaskGroup_Task},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)