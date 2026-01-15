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
ResponsibilityRole: Enumeration = Enumeration(
    name="ResponsibilityRole",
    literals={
            EnumerationLiteral(name="ASSISTANT"),
			EnumerationLiteral(name="LECTURER"),
			EnumerationLiteral(name="COORDINATOR")
    }
)

# Classes
tdt4250_Course = Class(name="tdt4250::Course")
tdt4250__bDNfcCdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDNfcCdxEeKsSJflfBDxuw")
tdt4250__bDTmECdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDTmECdxEeKsSJflfBDxuw")
tdt4250__bDYekCdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDYekCdxEeKsSJflfBDxuw")
tdt4250__bDSX8CdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDSX8CdxEeKsSJflfBDxuw")
tdt4250_Answer = Class(name="tdt4250::Answer")
tdt4250_Student = Class(name="tdt4250::Student")
_bDXQcCdxEeKsSJflfBDxuw = Class(name="::bDXQcCdxEeKsSJflfBDxuw")
tdt4250__bDIm8SdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDIm8SdxEeKsSJflfBDxuw")
tdt4250_Assignment = Class(name="tdt4250::Assignment")
tdt4250_Person = Class(name="tdt4250::Person")
tdt4250_Teacher = Class(name="tdt4250::Teacher")
tdt4250_Root = Class(name="tdt4250::Root")
tdt4250__bDXQcCdxEeKsSJflfBDxuw = Class(name="tdt4250::::bDXQcCdxEeKsSJflfBDxuw")

# tdt4250_Course class attributes and methods
tdt4250_Course_ID: Property = Property(name="ID", type=IntegerType)
tdt4250_Course_credit: Property = Property(name="credit", type=IntegerType)
tdt4250_Course_name: Property = Property(name="name", type=StringType)
tdt4250_Course.attributes={tdt4250_Course_name, tdt4250_Course_credit, tdt4250_Course_ID}

# tdt4250__bDNfcCdxEeKsSJflfBDxuw class attributes and methods

# tdt4250__bDTmECdxEeKsSJflfBDxuw class attributes and methods

# tdt4250__bDYekCdxEeKsSJflfBDxuw class attributes and methods

# tdt4250__bDSX8CdxEeKsSJflfBDxuw class attributes and methods

# tdt4250_Answer class attributes and methods
tdt4250_Answer_content: Property = Property(name="content", type=StringType)
tdt4250_Answer.attributes={tdt4250_Answer_content}

# tdt4250_Student class attributes and methods

# _bDXQcCdxEeKsSJflfBDxuw class attributes and methods

# tdt4250__bDIm8SdxEeKsSJflfBDxuw class attributes and methods

# tdt4250_Assignment class attributes and methods
tdt4250_Assignment_name: Property = Property(name="name", type=StringType)
tdt4250_Assignment_content: Property = Property(name="content", type=StringType)
tdt4250_Assignment_mandatory: Property = Property(name="mandatory", type=BooleanType)
tdt4250_Assignment_ID: Property = Property(name="ID", type=IntegerType)
tdt4250_Assignment.attributes={tdt4250_Assignment_name, tdt4250_Assignment_mandatory, tdt4250_Assignment_content, tdt4250_Assignment_ID}

# tdt4250_Person class attributes and methods
tdt4250_Person_ID: Property = Property(name="ID", type=IntegerType)
tdt4250_Person_name: Property = Property(name="name", type=StringType)
tdt4250_Person.attributes={tdt4250_Person_name, tdt4250_Person_ID}

# tdt4250_Teacher class attributes and methods
tdt4250_Teacher_role: Property = Property(name="role", type=StringType)
tdt4250_Teacher.attributes={tdt4250_Teacher_role}

# tdt4250_Root class attributes and methods

# tdt4250__bDXQcCdxEeKsSJflfBDxuw class attributes and methods

# Relationships
has0: BinaryAssociation = BinaryAssociation(
    name="has0",
    ends={
        Property(name="tdt4250__bDNfcCdxEeKsSJflfBDxuw", type=tdt4250_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Course", type=tdt4250__bDNfcCdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isAttended1: BinaryAssociation = BinaryAssociation(
    name="isAttended1",
    ends={
        Property(name="tdt4250__bDTmECdxEeKsSJflfBDxuw", type=tdt4250_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Course2", type=tdt4250__bDTmECdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
isCoordinated3: BinaryAssociation = BinaryAssociation(
    name="isCoordinated3",
    ends={
        Property(name="tdt4250__bDYekCdxEeKsSJflfBDxuw", type=tdt4250_Course, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Course4", type=tdt4250__bDYekCdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
isSolved5: BinaryAssociation = BinaryAssociation(
    name="isSolved5",
    ends={
        Property(name="tdt4250__bDSX8CdxEeKsSJflfBDxuw", type=tdt4250_Assignment, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Assignment", type=tdt4250__bDSX8CdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
attends6: BinaryAssociation = BinaryAssociation(
    name="attends6",
    ends={
        Property(name="tdt4250__bDIm8SdxEeKsSJflfBDxuw", type=tdt4250_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Student", type=tdt4250__bDIm8SdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
submit7: BinaryAssociation = BinaryAssociation(
    name="submit7",
    ends={
        Property(name="tdt4250__bDSX8CdxEeKsSJflfBDxuw9", type=tdt4250_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Student8", type=tdt4250__bDSX8CdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
coordinates10: BinaryAssociation = BinaryAssociation(
    name="coordinates10",
    ends={
        Property(name="tdt4250__bDIm8SdxEeKsSJflfBDxuw11", type=tdt4250_Teacher, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Teacher", type=tdt4250__bDIm8SdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
containsA12: BinaryAssociation = BinaryAssociation(
    name="containsA12",
    ends={
        Property(name="tdt4250__bDIm8SdxEeKsSJflfBDxuw13", type=tdt4250_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Root", type=tdt4250__bDIm8SdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)
containsB14: BinaryAssociation = BinaryAssociation(
    name="containsB14",
    ends={
        Property(name="tdt4250__bDXQcCdxEeKsSJflfBDxuw", type=tdt4250_Root, multiplicity=Multiplicity(1, 1)),
        Property(name="tdt4250_Root15", type=tdt4250__bDXQcCdxEeKsSJflfBDxuw, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_tdt4250_Student__bDXQcCdxEeKsSJflfBDxuw = Generalization(general=_bDXQcCdxEeKsSJflfBDxuw, specific=tdt4250_Student)
gen_tdt4250_Teacher__bDXQcCdxEeKsSJflfBDxuw = Generalization(general=_bDXQcCdxEeKsSJflfBDxuw, specific=tdt4250_Teacher)

# Domain Model
domain_model = DomainModel(
    name="tdt4250",
    types={tdt4250_Course, tdt4250__bDNfcCdxEeKsSJflfBDxuw, tdt4250__bDTmECdxEeKsSJflfBDxuw, tdt4250__bDYekCdxEeKsSJflfBDxuw, tdt4250__bDSX8CdxEeKsSJflfBDxuw, tdt4250_Answer, tdt4250_Student, _bDXQcCdxEeKsSJflfBDxuw, tdt4250__bDIm8SdxEeKsSJflfBDxuw, tdt4250_Assignment, tdt4250_Person, tdt4250_Teacher, tdt4250_Root, tdt4250__bDXQcCdxEeKsSJflfBDxuw, ResponsibilityRole},
    associations={has0, isAttended1, isCoordinated3, isSolved5, attends6, submit7, coordinates10, containsA12, containsB14},
    generalizations={gen_tdt4250_Student__bDXQcCdxEeKsSJflfBDxuw, gen_tdt4250_Teacher__bDXQcCdxEeKsSJflfBDxuw},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)