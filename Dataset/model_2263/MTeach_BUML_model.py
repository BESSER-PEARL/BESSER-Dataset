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
mteach_Professor = Class(name="mteach::Professor")
mteach_Course = Class(name="mteach::Course")
mteach_Topic = Class(name="mteach::Topic")

# mteach_Professor class attributes and methods
mteach_Professor_lastName: Property = Property(name="lastName", type=StringType)
mteach_Professor_firstName: Property = Property(name="firstName", type=StringType)
mteach_Professor.attributes={mteach_Professor_lastName, mteach_Professor_firstName}

# mteach_Course class attributes and methods
mteach_Course_name: Property = Property(name="name", type=StringType)
mteach_Course_time: Property = Property(name="time", type=IntegerType)
mteach_Course_coefficient: Property = Property(name="coefficient", type=FloatType)
mteach_Course.attributes={mteach_Course_name, mteach_Course_time, mteach_Course_coefficient}

# mteach_Topic class attributes and methods
mteach_Topic_title: Property = Property(name="title", type=StringType)
mteach_Topic.attributes={mteach_Topic_title}

# Relationships
teachedCourses0: BinaryAssociation = BinaryAssociation(
    name="teachedCourses0",
    ends={
        Property(name="Course", type=mteach_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="professor", type=mteach_Course, multiplicity=Multiplicity(0, 9999))
    }
)
topics1: BinaryAssociation = BinaryAssociation(
    name="topics1",
    ends={
        Property(name="Topic", type=mteach_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="course", type=mteach_Topic, multiplicity=Multiplicity(1, 9999))
    }
)
professor2: BinaryAssociation = BinaryAssociation(
    name="professor2",
    ends={
        Property(name="Professor", type=mteach_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="teachedCourses", type=mteach_Professor, multiplicity=Multiplicity(0, 1))
    }
)
course3: BinaryAssociation = BinaryAssociation(
    name="course3",
    ends={
        Property(name="Course4", type=mteach_Topic, multiplicity=Multiplicity(1, 1)),
        Property(name="topics", type=mteach_Course, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mteach",
    types={mteach_Professor, mteach_Course, mteach_Topic},
    associations={teachedCourses0, topics1, professor2, course3},
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