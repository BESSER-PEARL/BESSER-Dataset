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
scheduleOfCourse_Shift = Class(name="scheduleOfCourse::Shift")
scheduleOfCourse_Occupation = Class(name="scheduleOfCourse::Occupation")
scheduleOfCourse_Lesson = Class(name="scheduleOfCourse::Lesson")
scheduleOfCourse_Room = Class(name="scheduleOfCourse::Room")
scheduleOfCourse_LessonPeriod = Class(name="scheduleOfCourse::LessonPeriod")
scheduleOfCourse_CourseLoad = Class(name="scheduleOfCourse::CourseLoad")
scheduleOfCourse_Capacity = Class(name="scheduleOfCourse::Capacity")
scheduleOfCourse_TopLevelSpace = Class(name="scheduleOfCourse::TopLevelSpace")
scheduleOfCourse_scheduleOfCourse = Class(name="scheduleOfCourse::scheduleOfCourse")

# scheduleOfCourse_Shift class attributes and methods
scheduleOfCourse_Shift_name: Property = Property(name="name", type=StringType)
scheduleOfCourse_Shift_types: Property = Property(name="types", type=StringType)
scheduleOfCourse_Shift.attributes={scheduleOfCourse_Shift_types, scheduleOfCourse_Shift_name}

# scheduleOfCourse_Occupation class attributes and methods
scheduleOfCourse_Occupation_current: Property = Property(name="current", type=IntegerType)
scheduleOfCourse_Occupation_max: Property = Property(name="max", type=IntegerType)
scheduleOfCourse_Occupation.attributes={scheduleOfCourse_Occupation_max, scheduleOfCourse_Occupation_current}

# scheduleOfCourse_Lesson class attributes and methods
scheduleOfCourse_Lesson_start: Property = Property(name="start", type=StringType)
scheduleOfCourse_Lesson_end: Property = Property(name="end", type=StringType)
scheduleOfCourse_Lesson.attributes={scheduleOfCourse_Lesson_start, scheduleOfCourse_Lesson_end}

# scheduleOfCourse_Room class attributes and methods
scheduleOfCourse_Room_type: Property = Property(name="type", type=StringType)
scheduleOfCourse_Room_id: Property = Property(name="id", type=StringType)
scheduleOfCourse_Room_name: Property = Property(name="name", type=StringType)
scheduleOfCourse_Room_description: Property = Property(name="description", type=StringType)
scheduleOfCourse_Room.attributes={scheduleOfCourse_Room_name, scheduleOfCourse_Room_type, scheduleOfCourse_Room_description, scheduleOfCourse_Room_id}

# scheduleOfCourse_LessonPeriod class attributes and methods
scheduleOfCourse_LessonPeriod_start: Property = Property(name="start", type=StringType)
scheduleOfCourse_LessonPeriod_end: Property = Property(name="end", type=StringType)
scheduleOfCourse_LessonPeriod.attributes={scheduleOfCourse_LessonPeriod_start, scheduleOfCourse_LessonPeriod_end}

# scheduleOfCourse_CourseLoad class attributes and methods
scheduleOfCourse_CourseLoad_type: Property = Property(name="type", type=StringType)
scheduleOfCourse_CourseLoad_totalQuantity: Property = Property(name="totalQuantity", type=IntegerType)
scheduleOfCourse_CourseLoad_unitQuantity: Property = Property(name="unitQuantity", type=IntegerType)
scheduleOfCourse_CourseLoad.attributes={scheduleOfCourse_CourseLoad_type, scheduleOfCourse_CourseLoad_totalQuantity, scheduleOfCourse_CourseLoad_unitQuantity}

# scheduleOfCourse_Capacity class attributes and methods
scheduleOfCourse_Capacity_normal: Property = Property(name="normal", type=IntegerType)
scheduleOfCourse_Capacity_exam: Property = Property(name="exam", type=IntegerType)
scheduleOfCourse_Capacity.attributes={scheduleOfCourse_Capacity_normal, scheduleOfCourse_Capacity_exam}

# scheduleOfCourse_TopLevelSpace class attributes and methods
scheduleOfCourse_TopLevelSpace_type: Property = Property(name="type", type=StringType)
scheduleOfCourse_TopLevelSpace_id: Property = Property(name="id", type=StringType)
scheduleOfCourse_TopLevelSpace_name: Property = Property(name="name", type=StringType)
scheduleOfCourse_TopLevelSpace.attributes={scheduleOfCourse_TopLevelSpace_type, scheduleOfCourse_TopLevelSpace_id, scheduleOfCourse_TopLevelSpace_name}

# scheduleOfCourse_scheduleOfCourse class attributes and methods

# Relationships
occupation0: BinaryAssociation = BinaryAssociation(
    name="occupation0",
    ends={
        Property(name="scheduleOfCourse_Occupation", type=scheduleOfCourse_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Shift", type=scheduleOfCourse_Occupation, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
lessons1: BinaryAssociation = BinaryAssociation(
    name="lessons1",
    ends={
        Property(name="scheduleOfCourse_Lesson", type=scheduleOfCourse_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Shift2", type=scheduleOfCourse_Lesson, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
rooms3: BinaryAssociation = BinaryAssociation(
    name="rooms3",
    ends={
        Property(name="scheduleOfCourse_Room", type=scheduleOfCourse_Shift, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Shift4", type=scheduleOfCourse_Room, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
lessonPeriods5: BinaryAssociation = BinaryAssociation(
    name="lessonPeriods5",
    ends={
        Property(name="scheduleOfCourse_LessonPeriod", type=scheduleOfCourse_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_scheduleOfCourse", type=scheduleOfCourse_LessonPeriod, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
shifts8: BinaryAssociation = BinaryAssociation(
    name="shifts8",
    ends={
        Property(name="scheduleOfCourse_Shift10", type=scheduleOfCourse_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_scheduleOfCourse9", type=scheduleOfCourse_Shift, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
room11: BinaryAssociation = BinaryAssociation(
    name="room11",
    ends={
        Property(name="scheduleOfCourse_Room13", type=scheduleOfCourse_Lesson, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Lesson12", type=scheduleOfCourse_Room, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
topLevelSpace14: BinaryAssociation = BinaryAssociation(
    name="topLevelSpace14",
    ends={
        Property(name="scheduleOfCourse_TopLevelSpace", type=scheduleOfCourse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Room15", type=scheduleOfCourse_TopLevelSpace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
capacity16: BinaryAssociation = BinaryAssociation(
    name="capacity16",
    ends={
        Property(name="scheduleOfCourse_Capacity", type=scheduleOfCourse_Room, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_Room17", type=scheduleOfCourse_Capacity, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
courseLoads6: BinaryAssociation = BinaryAssociation(
    name="courseLoads6",
    ends={
        Property(name="scheduleOfCourse_CourseLoad", type=scheduleOfCourse_scheduleOfCourse, multiplicity=Multiplicity(1, 1)),
        Property(name="scheduleOfCourse_scheduleOfCourse7", type=scheduleOfCourse_CourseLoad, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="scheduleOfCourse",
    types={scheduleOfCourse_Shift, scheduleOfCourse_Occupation, scheduleOfCourse_Lesson, scheduleOfCourse_Room, scheduleOfCourse_LessonPeriod, scheduleOfCourse_CourseLoad, scheduleOfCourse_Capacity, scheduleOfCourse_TopLevelSpace, scheduleOfCourse_scheduleOfCourse},
    associations={occupation0, lessons1, rooms3, lessonPeriods5, shifts8, room11, topLevelSpace14, capacity16, courseLoads6},
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