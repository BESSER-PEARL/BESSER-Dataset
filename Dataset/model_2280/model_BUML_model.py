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
model_Delivery = Class(name="model::Delivery")
model_root = Class(name="model::root")
model_Student = Class(name="model::Student")
model_Course = Class(name="model::Course")
model_Exercise = Class(name="model::Exercise")
model_Response = Class(name="model::Response")

# model_Delivery class attributes and methods
model_Delivery_ID: Property = Property(name="ID", type=IntegerType)
model_Delivery_group_number: Property = Property(name="group_number", type=IntegerType)
model_Delivery_answer: Property = Property(name="answer", type=StringType)
model_Delivery_submission_date: Property = Property(name="submission_date", type=DateType)
model_Delivery.attributes={model_Delivery_submission_date, model_Delivery_ID, model_Delivery_group_number, model_Delivery_answer}

# model_root class attributes and methods

# model_Student class attributes and methods
model_Student_ID: Property = Property(name="ID", type=IntegerType)
model_Student_name: Property = Property(name="name", type=StringType)
model_Student.attributes={model_Student_ID, model_Student_name}

# model_Course class attributes and methods
model_Course_ID: Property = Property(name="ID", type=IntegerType)
model_Course_name: Property = Property(name="name", type=StringType)
model_Course.attributes={model_Course_name, model_Course_ID}

# model_Exercise class attributes and methods
model_Exercise_deadline_date: Property = Property(name="deadline_date", type=DateType)
model_Exercise_ID: Property = Property(name="ID", type=IntegerType)
model_Exercise.attributes={model_Exercise_deadline_date, model_Exercise_ID}

# model_Response class attributes and methods
model_Response_ID: Property = Property(name="ID", type=IntegerType)
model_Response_ok: Property = Property(name="ok", type=BooleanType)
model_Response_comment: Property = Property(name="comment", type=StringType)
model_Response.attributes={model_Response_ok, model_Response_comment, model_Response_ID}

# Relationships
containsCourse1: BinaryAssociation = BinaryAssociation(
    name="containsCourse1",
    ends={
        Property(name="model_Course", type=model_root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_root2", type=model_Course, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsDelivery3: BinaryAssociation = BinaryAssociation(
    name="containsDelivery3",
    ends={
        Property(name="model_Delivery", type=model_root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_root4", type=model_Delivery, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
containsStudent0: BinaryAssociation = BinaryAssociation(
    name="containsStudent0",
    ends={
        Property(name="model_Student", type=model_root, multiplicity=Multiplicity(1, 1)),
        Property(name="model_root", type=model_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
contains16: BinaryAssociation = BinaryAssociation(
    name="contains16",
    ends={
        Property(name="model_Exercise18", type=model_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Course17", type=model_Exercise, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attends5: BinaryAssociation = BinaryAssociation(
    name="attends5",
    ends={
        Property(name="model_Course7", type=model_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Student6", type=model_Course, multiplicity=Multiplicity(0, 9999))
    }
)
submits8: BinaryAssociation = BinaryAssociation(
    name="submits8",
    ends={
        Property(name="model_Delivery10", type=model_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Student9", type=model_Delivery, multiplicity=Multiplicity(0, 9999))
    }
)
hasSubmitted11: BinaryAssociation = BinaryAssociation(
    name="hasSubmitted11",
    ends={
        Property(name="model_Delivery12", type=model_Exercise, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Exercise", type=model_Delivery, multiplicity=Multiplicity(0, 9999))
    }
)
assignedTo13: BinaryAssociation = BinaryAssociation(
    name="assignedTo13",
    ends={
        Property(name="model_Student15", type=model_Exercise, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Exercise14", type=model_Student, multiplicity=Multiplicity(0, 9999))
    }
)
evaluates19: BinaryAssociation = BinaryAssociation(
    name="evaluates19",
    ends={
        Property(name="model_Response", type=model_Delivery, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Delivery20", type=model_Response, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Delivery, model_root, model_Student, model_Course, model_Exercise, model_Response},
    associations={containsCourse1, containsDelivery3, containsStudent0, contains16, attends5, submits8, hasSubmitted11, assignedTo13, evaluates19},
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