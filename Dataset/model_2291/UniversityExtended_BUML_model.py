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
SalaryRank: Enumeration = Enumeration(
    name="SalaryRank",
    literals={
            EnumerationLiteral(name="W1"),
			EnumerationLiteral(name="W2"),
			EnumerationLiteral(name="W3")
    }
)

Building: Enumeration = Enumeration(
    name="Building",
    literals={
            EnumerationLiteral(name="H"),
			EnumerationLiteral(name="A"),
			EnumerationLiteral(name="B"),
			EnumerationLiteral(name="C"),
			EnumerationLiteral(name="D"),
			EnumerationLiteral(name="E"),
			EnumerationLiteral(name="F"),
			EnumerationLiteral(name="G")
    }
)

DayOfWeek: Enumeration = Enumeration(
    name="DayOfWeek",
    literals={
            EnumerationLiteral(name="Monday"),
			EnumerationLiteral(name="Tuesday"),
			EnumerationLiteral(name="Wednesday"),
			EnumerationLiteral(name="Thursday"),
			EnumerationLiteral(name="Friday")
    }
)

Motivation: Enumeration = Enumeration(
    name="Motivation",
    literals={
            EnumerationLiteral(name="HIGH_INTEREST"),
			EnumerationLiteral(name="AVERAGE_INTEREST"),
			EnumerationLiteral(name="LOW_INTEREST")
    }
)

# Classes
universityextended_people_Professor = Class(name="universityextended::people::Professor")
Lecture = Class(name="Lecture")
universityextended_University = Class(name="universityextended::University")
Person = Class(name="Person")
Visits = Class(name="Visits")
Course = Class(name="Course")
Time = Class(name="Time")
Room = Class(name="Room")
universityextended_people_Person = Class(name="universityextended::people::Person")
universityextended_people_Student = Class(name="universityextended::people::Student")
universityextended_administration_Room = Class(name="universityextended::administration::Room")
universityextended_people_Assistant = Class(name="universityextended::people::Assistant")
Tutorial = Class(name="Tutorial")
universityextended_administration_Course = Class(name="universityextended::administration::Course")
universityextended_administration_Lecture = Class(name="universityextended::administration::Lecture")
Event = Class(name="Event")
Professor = Class(name="Professor")
universityextended_administration_Tutorial = Class(name="universityextended::administration::Tutorial")
Assistant = Class(name="Assistant")
universityextended_administration_Time = Class(name="universityextended::administration::Time")
universityextended_administration_Event = Class(name="universityextended::administration::Event")
universityextended_connection_Visits = Class(name="universityextended::connection::Visits")
Student = Class(name="Student")

# universityextended_people_Professor class attributes and methods
universityextended_people_Professor_rank: Property = Property(name="rank", type=StringType)
universityextended_people_Professor.attributes={universityextended_people_Professor_rank}

# Lecture class attributes and methods

# universityextended_University class attributes and methods

# Person class attributes and methods

# Visits class attributes and methods

# Course class attributes and methods

# Time class attributes and methods

# Room class attributes and methods

# universityextended_people_Person class attributes and methods
universityextended_people_Person_name: Property = Property(name="name", type=StringType)
universityextended_people_Person.attributes={universityextended_people_Person_name}

# universityextended_people_Student class attributes and methods
universityextended_people_Student_matriculationnumber: Property = Property(name="matriculationnumber", type=StringType)
universityextended_people_Student.attributes={universityextended_people_Student_matriculationnumber}

# universityextended_administration_Room class attributes and methods
universityextended_administration_Room_building: Property = Property(name="building", type=StringType)
universityextended_administration_Room_floor: Property = Property(name="floor", type=IntegerType)
universityextended_administration_Room_roomnumber: Property = Property(name="roomnumber", type=IntegerType)
universityextended_administration_Room.attributes={universityextended_administration_Room_floor, universityextended_administration_Room_roomnumber, universityextended_administration_Room_building}

# universityextended_people_Assistant class attributes and methods
universityextended_people_Assistant_isDoctoralCandidate: Property = Property(name="isDoctoralCandidate", type=BooleanType)
universityextended_people_Assistant.attributes={universityextended_people_Assistant_isDoctoralCandidate}

# Tutorial class attributes and methods

# universityextended_administration_Course class attributes and methods
universityextended_administration_Course_title: Property = Property(name="title", type=StringType)
universityextended_administration_Course_startOfCourse: Property = Property(name="startOfCourse", type=DateType)
universityextended_administration_Course_endOfCourse: Property = Property(name="endOfCourse", type=DateType)
universityextended_administration_Course.attributes={universityextended_administration_Course_endOfCourse, universityextended_administration_Course_startOfCourse, universityextended_administration_Course_title}

# universityextended_administration_Lecture class attributes and methods
universityextended_administration_Lecture_captions: Property = Property(name="captions", type=StringType)
universityextended_administration_Lecture.attributes={universityextended_administration_Lecture_captions}

# Event class attributes and methods

# Professor class attributes and methods

# universityextended_administration_Tutorial class attributes and methods

# Assistant class attributes and methods

# universityextended_administration_Time class attributes and methods
universityextended_administration_Time_day: Property = Property(name="day", type=StringType)
universityextended_administration_Time_startHour: Property = Property(name="startHour", type=IntegerType)
universityextended_administration_Time_endHour: Property = Property(name="endHour", type=IntegerType)
universityextended_administration_Time.attributes={universityextended_administration_Time_startHour, universityextended_administration_Time_day, universityextended_administration_Time_endHour}

# universityextended_administration_Event class attributes and methods
universityextended_administration_Event_title: Property = Property(name="title", type=StringType)
universityextended_administration_Event.attributes={universityextended_administration_Event_title}

# universityextended_connection_Visits class attributes and methods
universityextended_connection_Visits_motivation: Property = Property(name="motivation", type=StringType)
universityextended_connection_Visits.attributes={universityextended_connection_Visits_motivation}

# Student class attributes and methods

# Relationships
courseVisit9: BinaryAssociation = BinaryAssociation(
    name="courseVisit9",
    ends={
        Property(name="connection", type=universityextended_people_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="Visits10", type=Visits, multiplicity=Multiplicity(0, 9999))
    }
)
persons0: BinaryAssociation = BinaryAssociation(
    name="persons0",
    ends={
        Property(name="Person", type=universityextended_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_University", type=Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
visits1: BinaryAssociation = BinaryAssociation(
    name="visits1",
    ends={
        Property(name="Visits", type=universityextended_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_University2", type=Visits, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
courses3: BinaryAssociation = BinaryAssociation(
    name="courses3",
    ends={
        Property(name="Course", type=universityextended_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_University4", type=Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
times5: BinaryAssociation = BinaryAssociation(
    name="times5",
    ends={
        Property(name="Time", type=universityextended_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_University6", type=Time, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
rooms7: BinaryAssociation = BinaryAssociation(
    name="rooms7",
    ends={
        Property(name="Room", type=universityextended_University, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_University8", type=Room, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
lectures11: BinaryAssociation = BinaryAssociation(
    name="lectures11",
    ends={
        Property(name="administration", type=universityextended_people_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="Lecture", type=Lecture, multiplicity=Multiplicity(0, 9999))
    }
)
tutorial12: BinaryAssociation = BinaryAssociation(
    name="tutorial12",
    ends={
        Property(name="administration13", type=universityextended_people_Assistant, multiplicity=Multiplicity(1, 1)),
        Property(name="Tutorial", type=Tutorial, multiplicity=Multiplicity(0, 9999))
    }
)
lecture14: BinaryAssociation = BinaryAssociation(
    name="lecture14",
    ends={
        Property(name="administration16", type=universityextended_administration_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="Lecture15", type=Lecture, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
tutorial17: BinaryAssociation = BinaryAssociation(
    name="tutorial17",
    ends={
        Property(name="administration19", type=universityextended_administration_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="Tutorial18", type=Tutorial, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
visitor20: BinaryAssociation = BinaryAssociation(
    name="visitor20",
    ends={
        Property(name="connection22", type=universityextended_administration_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="Visits21", type=Visits, multiplicity=Multiplicity(0, 9999))
    }
)
course23: BinaryAssociation = BinaryAssociation(
    name="course23",
    ends={
        Property(name="administration25", type=universityextended_administration_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="Course24", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
lecturer26: BinaryAssociation = BinaryAssociation(
    name="lecturer26",
    ends={
        Property(name="people", type=universityextended_administration_Lecture, multiplicity=Multiplicity(1, 1)),
        Property(name="Professor", type=Professor, multiplicity=Multiplicity(1, 1))
    }
)
course27: BinaryAssociation = BinaryAssociation(
    name="course27",
    ends={
        Property(name="administration29", type=universityextended_administration_Tutorial, multiplicity=Multiplicity(1, 1)),
        Property(name="Course28", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
tutor30: BinaryAssociation = BinaryAssociation(
    name="tutor30",
    ends={
        Property(name="people31", type=universityextended_administration_Tutorial, multiplicity=Multiplicity(1, 1)),
        Property(name="Assistant", type=Assistant, multiplicity=Multiplicity(1, 1))
    }
)
time32: BinaryAssociation = BinaryAssociation(
    name="time32",
    ends={
        Property(name="Time33", type=universityextended_administration_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_administration_Event", type=Time, multiplicity=Multiplicity(1, 1))
    }
)
room34: BinaryAssociation = BinaryAssociation(
    name="room34",
    ends={
        Property(name="Room36", type=universityextended_administration_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="universityextended_administration_Event35", type=Room, multiplicity=Multiplicity(1, 1))
    }
)
course37: BinaryAssociation = BinaryAssociation(
    name="course37",
    ends={
        Property(name="administration39", type=universityextended_connection_Visits, multiplicity=Multiplicity(1, 1)),
        Property(name="Course38", type=Course, multiplicity=Multiplicity(1, 1))
    }
)
student40: BinaryAssociation = BinaryAssociation(
    name="student40",
    ends={
        Property(name="people41", type=universityextended_connection_Visits, multiplicity=Multiplicity(1, 1)),
        Property(name="Student", type=Student, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_universityextended_people_Professor_Person = Generalization(general=Person, specific=universityextended_people_Professor)
gen_universityextended_people_Student_Person = Generalization(general=Person, specific=universityextended_people_Student)
gen_universityextended_people_Assistant_Person = Generalization(general=Person, specific=universityextended_people_Assistant)
gen_universityextended_administration_Lecture_Event = Generalization(general=Event, specific=universityextended_administration_Lecture)
gen_universityextended_administration_Tutorial_Event = Generalization(general=Event, specific=universityextended_administration_Tutorial)

# Domain Model
domain_model = DomainModel(
    name="universityextended",
    types={universityextended_people_Professor, Lecture, universityextended_University, Person, Visits, Course, Time, Room, universityextended_people_Person, universityextended_people_Student, universityextended_administration_Room, universityextended_people_Assistant, Tutorial, universityextended_administration_Course, universityextended_administration_Lecture, Event, Professor, universityextended_administration_Tutorial, Assistant, universityextended_administration_Time, universityextended_administration_Event, universityextended_connection_Visits, Student, SalaryRank, Building, DayOfWeek, Motivation},
    associations={courseVisit9, persons0, visits1, courses3, times5, rooms7, lectures11, tutorial12, lecture14, tutorial17, visitor20, course23, lecturer26, course27, tutor30, time32, room34, course37, student40},
    generalizations={gen_universityextended_people_Professor_Person, gen_universityextended_people_Student_Person, gen_universityextended_people_Assistant_Person, gen_universityextended_administration_Lecture_Event, gen_universityextended_administration_Tutorial_Event},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)