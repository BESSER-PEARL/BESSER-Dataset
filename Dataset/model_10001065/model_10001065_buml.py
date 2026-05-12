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
data_manager = Class(name="data_manager")
subject_manager = Class(name="subject_manager")
time_manager = Class(name="time_manager")
activity_manager = Class(name="activity_manager")
ATTGS = Class(name="ATTGS")
outputgenerator = Class(name="outputgenerator")
room_manager = Class(name="room_manager")
class_manager = Class(name="class_manager")
faculty_manager = Class(name="faculty_manager")

# data_manager class attributes and methods

# subject_manager class attributes and methods

# time_manager class attributes and methods

# activity_manager class attributes and methods

# ATTGS class attributes and methods

# outputgenerator class attributes and methods

# room_manager class attributes and methods

# class_manager class attributes and methods

# faculty_manager class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="_81940f79_d055_47f0_be78_392d0d87bc71",
    types={data_manager, subject_manager, time_manager, activity_manager, ATTGS, outputgenerator, room_manager, class_manager, faculty_manager},
    associations={},
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