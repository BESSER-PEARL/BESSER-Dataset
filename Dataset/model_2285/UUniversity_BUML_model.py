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
OperatorType: Enumeration = Enumeration(
    name="OperatorType",
    literals={
            EnumerationLiteral(name="XOR"),
			EnumerationLiteral(name="AND"),
			EnumerationLiteral(name="OR")
    }
)

# Classes
UniverityU_Courses = Class(name="UniverityU_Courses")
UniverityU_uncertainty_UData = Class(name="UniverityU_uncertainty_UData", is_abstract=True)
UniverityU_uncertainty_uCourses = Class(name="UniverityU_uncertainty_uCourses")
uncertainty_UData = Class(name="uncertainty_UData")
uCourses = Class(name="uCourses")
UniverityU_uncertainty_aCourses = Class(name="UniverityU_uncertainty_aCourses", is_abstract=True)
UniverityU_uncertainty_uPerson = Class(name="UniverityU_uncertainty_uPerson")
uncertainty_ModelElement = Class(name="uncertainty_ModelElement")
uncertainty_aCourses = Class(name="uncertainty_aCourses")
aCourses = Class(name="aCourses")
aPerson = Class(name="aPerson")
UniverityU_Person = Class(name="UniverityU_Person")
uncertainty_aPerson = Class(name="uncertainty_aPerson")
UniverityU_University = Class(name="UniverityU_University")
uncertainty_aUniversity = Class(name="uncertainty_aUniversity")
UniverityU_uncertainty_ModelElement = Class(name="UniverityU_uncertainty_ModelElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
uPerson = Class(name="uPerson")
UniverityU_uncertainty_aPerson = Class(name="UniverityU_uncertainty_aPerson", is_abstract=True)
UniverityU_uncertainty_uUniversity = Class(name="UniverityU_uncertainty_uUniversity")
aUniversity = Class(name="aUniversity")
uUniversity = Class(name="uUniversity")
UniverityU_uncertainty_aUniversity = Class(name="UniverityU_uncertainty_aUniversity", is_abstract=True)

# UniverityU_Courses class attributes and methods
UniverityU_Courses_Name: Property = Property(name="Name", type=StringType)
UniverityU_Courses_CFU: Property = Property(name="CFU", type=IntegerType)
UniverityU_Courses_Semester: Property = Property(name="Semester", type=StringType)
UniverityU_Courses.attributes={UniverityU_Courses_Semester, UniverityU_Courses_Name, UniverityU_Courses_CFU}

# UniverityU_uncertainty_UData class attributes and methods
UniverityU_uncertainty_UData_name: Property = Property(name="name", type=StringType)
UniverityU_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
UniverityU_uncertainty_UData.attributes={UniverityU_uncertainty_UData_name, UniverityU_uncertainty_UData_utype}

# UniverityU_uncertainty_uCourses class attributes and methods

# uncertainty_UData class attributes and methods

# uCourses class attributes and methods

# UniverityU_uncertainty_aCourses class attributes and methods

# UniverityU_uncertainty_uPerson class attributes and methods

# uncertainty_ModelElement class attributes and methods

# uncertainty_aCourses class attributes and methods

# aCourses class attributes and methods

# aPerson class attributes and methods

# UniverityU_Person class attributes and methods
UniverityU_Person_Name: Property = Property(name="Name", type=StringType)
UniverityU_Person_Email: Property = Property(name="Email", type=StringType)
UniverityU_Person.attributes={UniverityU_Person_Email, UniverityU_Person_Name}

# uncertainty_aPerson class attributes and methods

# UniverityU_University class attributes and methods

# uncertainty_aUniversity class attributes and methods

# UniverityU_uncertainty_ModelElement class attributes and methods

# ModelElement class attributes and methods

# uPerson class attributes and methods

# UniverityU_uncertainty_aPerson class attributes and methods

# UniverityU_uncertainty_uUniversity class attributes and methods

# aUniversity class attributes and methods

# uUniversity class attributes and methods

# UniverityU_uncertainty_aUniversity class attributes and methods

# Relationships
exclude11: BinaryAssociation = BinaryAssociation(
    name="exclude11",
    ends={
        Property(name="ModelElement13", type=UniverityU_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_ModelElement12", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uleft14: BinaryAssociation = BinaryAssociation(
    name="uleft14",
    ends={
        Property(name="aCourses15", type=UniverityU_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uCourses", type=aCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright16: BinaryAssociation = BinaryAssociation(
    name="uright16",
    ends={
        Property(name="aCourses18", type=UniverityU_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uCourses17", type=aCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint19: BinaryAssociation = BinaryAssociation(
    name="upoint19",
    ends={
        Property(name="uCourses", type=UniverityU_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uCourses20", type=uCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="aCourses", type=UniverityU_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_Courses", type=aCourses, multiplicity=Multiplicity(0, 9999))
    }
)
Professor1: BinaryAssociation = BinaryAssociation(
    name="Professor1",
    ends={
        Property(name="aPerson", type=UniverityU_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_Courses2", type=aPerson, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
Student3: BinaryAssociation = BinaryAssociation(
    name="Student3",
    ends={
        Property(name="aPerson5", type=UniverityU_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_Courses4", type=aPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatives6: BinaryAssociation = BinaryAssociation(
    name="relatives6",
    ends={
        Property(name="aPerson7", type=UniverityU_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_Person", type=aPerson, multiplicity=Multiplicity(0, 1))
    }
)
Courses8: BinaryAssociation = BinaryAssociation(
    name="Courses8",
    ends={
        Property(name="aCourses9", type=UniverityU_University, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_University", type=aCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include10: BinaryAssociation = BinaryAssociation(
    name="include10",
    ends={
        Property(name="ModelElement", type=UniverityU_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uleft21: BinaryAssociation = BinaryAssociation(
    name="uleft21",
    ends={
        Property(name="aPerson22", type=UniverityU_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uPerson", type=aPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright23: BinaryAssociation = BinaryAssociation(
    name="uright23",
    ends={
        Property(name="aPerson25", type=UniverityU_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uPerson24", type=aPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint26: BinaryAssociation = BinaryAssociation(
    name="upoint26",
    ends={
        Property(name="uPerson", type=UniverityU_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uPerson27", type=uPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft28: BinaryAssociation = BinaryAssociation(
    name="uleft28",
    ends={
        Property(name="aUniversity", type=UniverityU_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uUniversity", type=aUniversity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright29: BinaryAssociation = BinaryAssociation(
    name="uright29",
    ends={
        Property(name="aUniversity31", type=UniverityU_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uUniversity30", type=aUniversity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint32: BinaryAssociation = BinaryAssociation(
    name="upoint32",
    ends={
        Property(name="uUniversity", type=UniverityU_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="UniverityU_uncertainty_uUniversity33", type=uUniversity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UniverityU_uncertainty_uCourses_uncertainty_aCourses = Generalization(general=uncertainty_aCourses, specific=UniverityU_uncertainty_uCourses)
gen_UniverityU_uncertainty_uCourses_uncertainty_UData = Generalization(general=uncertainty_UData, specific=UniverityU_uncertainty_uCourses)
gen_UniverityU_uncertainty_uPerson_uncertainty_aPerson = Generalization(general=uncertainty_aPerson, specific=UniverityU_uncertainty_uPerson)
gen_UniverityU_uncertainty_uPerson_uncertainty_UData = Generalization(general=uncertainty_UData, specific=UniverityU_uncertainty_uPerson)
gen_UniverityU_Courses_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=UniverityU_Courses)
gen_UniverityU_Courses_uncertainty_aCourses = Generalization(general=uncertainty_aCourses, specific=UniverityU_Courses)
gen_UniverityU_Person_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=UniverityU_Person)
gen_UniverityU_Person_uncertainty_aPerson = Generalization(general=uncertainty_aPerson, specific=UniverityU_Person)
gen_UniverityU_University_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=UniverityU_University)
gen_UniverityU_University_uncertainty_aUniversity = Generalization(general=uncertainty_aUniversity, specific=UniverityU_University)
gen_UniverityU_uncertainty_uUniversity_uncertainty_aUniversity = Generalization(general=uncertainty_aUniversity, specific=UniverityU_uncertainty_uUniversity)
gen_UniverityU_uncertainty_uUniversity_uncertainty_UData = Generalization(general=uncertainty_UData, specific=UniverityU_uncertainty_uUniversity)

# Domain Model
domain_model = DomainModel(
    name="UniverityU",
    types={UniverityU_Courses, UniverityU_uncertainty_UData, UniverityU_uncertainty_uCourses, uncertainty_UData, uCourses, UniverityU_uncertainty_aCourses, UniverityU_uncertainty_uPerson, uncertainty_ModelElement, uncertainty_aCourses, aCourses, aPerson, UniverityU_Person, uncertainty_aPerson, UniverityU_University, uncertainty_aUniversity, UniverityU_uncertainty_ModelElement, ModelElement, uPerson, UniverityU_uncertainty_aPerson, UniverityU_uncertainty_uUniversity, aUniversity, uUniversity, UniverityU_uncertainty_aUniversity, OperatorType},
    associations={exclude11, uleft14, uright16, upoint19, links0, Professor1, Student3, relatives6, Courses8, include10, uleft21, uright23, upoint26, uleft28, uright29, upoint32},
    generalizations={gen_UniverityU_uncertainty_uCourses_uncertainty_aCourses, gen_UniverityU_uncertainty_uCourses_uncertainty_UData, gen_UniverityU_uncertainty_uPerson_uncertainty_aPerson, gen_UniverityU_uncertainty_uPerson_uncertainty_UData, gen_UniverityU_Courses_uncertainty_ModelElement, gen_UniverityU_Courses_uncertainty_aCourses, gen_UniverityU_Person_uncertainty_ModelElement, gen_UniverityU_Person_uncertainty_aPerson, gen_UniverityU_University_uncertainty_ModelElement, gen_UniverityU_University_uncertainty_aUniversity, gen_UniverityU_uncertainty_uUniversity_uncertainty_aUniversity, gen_UniverityU_uncertainty_uUniversity_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)