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
fenix_Occupation = Class(name="fenix::Occupation")
fenix_LessonPeriod = Class(name="fenix::LessonPeriod")
fenix_Shift = Class(name="fenix::Shift")
fenix_CourseLoad = Class(name="fenix::CourseLoad")
fenix_scheduleOfCourse = Class(name="fenix::scheduleOfCourse")
fenix_Capacity = Class(name="fenix::Capacity")

# fenix_Occupation class attributes and methods
fenix_Occupation_current: Property = Property(name="current", type=IntegerType)
fenix_Occupation_max: Property = Property(name="max", type=IntegerType)
fenix_Occupation.attributes={fenix_Occupation_max, fenix_Occupation_current}

# fenix_LessonPeriod class attributes and methods
fenix_LessonPeriod_start: Property = Property(name="start", type=StringType)
fenix_LessonPeriod_end: Property = Property(name="end", type=StringType)
fenix_LessonPeriod.attributes={fenix_LessonPeriod_start, fenix_LessonPeriod_end}

# fenix_Shift class attributes and methods
fenix_Shift_types: Property = Property(name="types", type=StringType)
fenix_Shift_name: Property = Property(name="name", type=StringType)
fenix_Shift.attributes={fenix_Shift_types, fenix_Shift_name}

# fenix_CourseLoad class attributes and methods
fenix_CourseLoad_type: Property = Property(name="type", type=StringType)
fenix_CourseLoad_totalQuantity: Property = Property(name="totalQuantity", type=IntegerType)
fenix_CourseLoad_id: Property = Property(name="id", type=StringType)
fenix_CourseLoad_name: Property = Property(name="name", type=StringType)
fenix_CourseLoad_description: Property = Property(name="description", type=StringType)
fenix_CourseLoad_unitQuantity: Property = Property(name="unitQuantity", type=IntegerType)
fenix_CourseLoad.attributes={fenix_CourseLoad_description, fenix_CourseLoad_unitQuantity, fenix_CourseLoad_type, fenix_CourseLoad_name, fenix_CourseLoad_id, fenix_CourseLoad_totalQuantity}

# fenix_scheduleOfCourse class attributes and methods

# fenix_Capacity class attributes and methods
fenix_Capacity_normal: Property = Property(name="normal", type=IntegerType)
fenix_Capacity_exam: Property = Property(name="exam", type=IntegerType)
fenix_Capacity.attributes={fenix_Capacity_exam, fenix_Capacity_normal}

# Relationships
occupation0: BinaryAssociation = BinaryAssociation(
    name="occupation0",
    ends={
        Property(name="fenix_Occupation", type=fenix_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_Shift", type=fenix_Occupation, multiplicity=Multiplicity(1, 1))
    }
)
lessons1: BinaryAssociation = BinaryAssociation(
    name="lessons1",
    ends={
        Property(name="fenix_LessonPeriod", type=fenix_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_Shift2", type=fenix_LessonPeriod, multiplicity=Multiplicity(1, 9999))
    }
)
rooms3: BinaryAssociation = BinaryAssociation(
    name="rooms3",
    ends={
        Property(name="fenix_CourseLoad", type=fenix_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_Shift4", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 9999))
    }
)
room5: BinaryAssociation = BinaryAssociation(
    name="room5",
    ends={
        Property(name="fenix_CourseLoad7", type=fenix_LessonPeriod, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_LessonPeriod6", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 1))
    }
)
topLevelSpace9: BinaryAssociation = BinaryAssociation(
    name="topLevelSpace9",
    ends={
        Property(name="fenix_CourseLoad10", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_CourseLoad8", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 1))
    }
)
lessonPeriods13: BinaryAssociation = BinaryAssociation(
    name="lessonPeriods13",
    ends={
        Property(name="fenix_LessonPeriod14", type=fenix_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_scheduleOfCourse", type=fenix_LessonPeriod, multiplicity=Multiplicity(1, 9999))
    }
)
capacity11: BinaryAssociation = BinaryAssociation(
    name="capacity11",
    ends={
        Property(name="fenix_Capacity", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_CourseLoad12", type=fenix_Capacity, multiplicity=Multiplicity(0, 1))
    }
)
courseLoads15: BinaryAssociation = BinaryAssociation(
    name="courseLoads15",
    ends={
        Property(name="fenix_CourseLoad17", type=fenix_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_scheduleOfCourse16", type=fenix_CourseLoad, multiplicity=Multiplicity(1, 9999))
    }
)
shifts18: BinaryAssociation = BinaryAssociation(
    name="shifts18",
    ends={
        Property(name="fenix_Shift20", type=fenix_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="fenix_scheduleOfCourse19", type=fenix_Shift, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="fenix",
    types={fenix_Occupation, fenix_LessonPeriod, fenix_Shift, fenix_CourseLoad, fenix_scheduleOfCourse, fenix_Capacity},
    associations={occupation0, lessons1, rooms3, room5, topLevelSpace9, lessonPeriods13, capacity11, courseLoads15, shifts18},
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