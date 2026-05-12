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
project_Integer = Class(name="project_Integer")
project_Enrollment = Class(name="project_Enrollment")
project_Person = Class(name="project_Person")
project_Organization = Class(name="project_Organization")
project_Child = Class(name="project_Child")
Person = Class(name="Person")
project_Teenager = Class(name="project_Teenager")
project_Adult = Class(name="project_Adult")
project_Student = Class(name="project_Student")
project_University = Class(name="project_University")
Organization = Class(name="Organization")

# project_Integer class attributes and methods

# project_Enrollment class attributes and methods

# project_Person class attributes and methods

# project_Organization class attributes and methods

# project_Child class attributes and methods

# Person class attributes and methods

# project_Teenager class attributes and methods

# project_Adult class attributes and methods

# project_Student class attributes and methods

# project_University class attributes and methods

# Organization class attributes and methods

# Relationships
enrollments0: BinaryAssociation = BinaryAssociation(
    name="enrollments0",
    ends={
        Property(name="Enrollment", type=project_Integer, multiplicity=Multiplicity(1, 1)),
        Property(name="id", type=project_Enrollment, multiplicity=Multiplicity(0, 9999))
    }
)
universities1: BinaryAssociation = BinaryAssociation(
    name="universities1",
    ends={
        Property(name="University", type=project_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=project_University, multiplicity=Multiplicity(1, 9999))
    }
)
enrollments5: BinaryAssociation = BinaryAssociation(
    name="enrollments5",
    ends={
        Property(name="Enrollment6", type=project_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university", type=project_Enrollment, multiplicity=Multiplicity(1, 9999))
    }
)
university7: BinaryAssociation = BinaryAssociation(
    name="university7",
    ends={
        Property(name="University8", type=project_Enrollment, multiplicity=Multiplicity(1, 1)),
        Property(name="enrollments", type=project_University, multiplicity=Multiplicity(1, 1))
    }
)
student9: BinaryAssociation = BinaryAssociation(
    name="student9",
    ends={
        Property(name="Student11", type=project_Enrollment, multiplicity=Multiplicity(1, 1)),
        Property(name="enrollments10", type=project_Student, multiplicity=Multiplicity(1, 1))
    }
)
id12: BinaryAssociation = BinaryAssociation(
    name="id12",
    ends={
        Property(name="Integer", type=project_Enrollment, multiplicity=Multiplicity(1, 1)),
        Property(name="enrollments13", type=project_Integer, multiplicity=Multiplicity(1, 1))
    }
)
enrollments2: BinaryAssociation = BinaryAssociation(
    name="enrollments2",
    ends={
        Property(name="Enrollment3", type=project_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="student", type=project_Enrollment, multiplicity=Multiplicity(1, 9999))
    }
)
students4: BinaryAssociation = BinaryAssociation(
    name="students4",
    ends={
        Property(name="Student", type=project_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universities", type=project_Student, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_project_Child_Person = Generalization(general=Person, specific=project_Child)
gen_project_Teenager_Person = Generalization(general=Person, specific=project_Teenager)
gen_project_Adult_Person = Generalization(general=Person, specific=project_Adult)
gen_project_Student_Person = Generalization(general=Person, specific=project_Student)
gen_project_University_Organization = Generalization(general=Organization, specific=project_University)


# OCL Constraints
one_enrollment_per_student: Constraint = Constraint(
    name="one_enrollment_per_student",
    context=project_University,
    expression="context University inv: self.enrollments->collect(x | x.student)->asSet()->forAll(s: Student | s.enrollments->intersection(self.enrollments)->size()=1)",
    language="OCL"
)
enrollments_has_unique_id: Constraint = Constraint(
    name="enrollments_has_unique_id",
    context=project_University,
    expression="context University inv: self.enrollments->isUnique(x: Enrollment | x.id)",
    language="OCL"
)
adult_three_enrolllment: Constraint = Constraint(
    name="adult_three_enrolllment",
    context=project_Student,
    expression="context Student inv: Adult.allInstances()->notEmpty() andChild.allInstances()->isEmpty() andTeenager.allInstances()->isEmpty() and(self.oclIsKindOf(Adult) implies self.universities->size() = 3)",
    language="OCL"
)
no_child_university: Constraint = Constraint(
    name="no_child_university",
    context=project_University,
    expression="context University inv: self.students->forAll( x:Student | not x.oclIsKindOf(Child) )",
    language="OCL"
)

# Domain Model
domain_model = DomainModel(
    name="project",
    types={project_Integer, project_Enrollment, project_Person, project_Organization, project_Child, Person, project_Teenager, project_Adult, project_Student, project_University, Organization},
    associations={enrollments0, universities1, enrollments5, university7, student9, id12, enrollments2, students4},
    constraints={one_enrollment_per_student, enrollments_has_unique_id, adult_three_enrolllment, no_child_university},
    generalizations={gen_project_Child_Person, gen_project_Teenager_Person, gen_project_Adult_Person, gen_project_Student_Person, gen_project_University_Organization},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)