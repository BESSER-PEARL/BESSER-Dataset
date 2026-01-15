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
Univerity_Courses = Class(name="Univerity::Courses")
uncertainty_ModelElement = Class(name="uncertainty::ModelElement")
uncertainty_aCourses = Class(name="uncertainty::aCourses")
Univerity_Person = Class(name="Univerity::Person")
aCourses = Class(name="aCourses")
aPerson = Class(name="aPerson")
Univerity_uncertainty_ModelElement = Class(name="Univerity::uncertainty::ModelElement", is_abstract=True)
uncertainty_aPerson = Class(name="uncertainty::aPerson")
Univerity_University = Class(name="Univerity::University")
uncertainty_aUniversity = Class(name="uncertainty::aUniversity")
Univerity_uncertainty_uCourses = Class(name="Univerity::uncertainty::uCourses")
uncertainty_UData = Class(name="uncertainty::UData")
ModelElement = Class(name="ModelElement")
uncertainty_Univerity_Courses = Class(name="uncertainty::Univerity::Courses")
Univerity_uncertainty_UData = Class(name="Univerity::uncertainty::UData", is_abstract=True)
uCourses = Class(name="uCourses")
Univerity_uncertainty_aCourses = Class(name="Univerity::uncertainty::aCourses", is_abstract=True)
Univerity_uncertainty_uPerson = Class(name="Univerity::uncertainty::uPerson")
uncertainty_Univerity_Person = Class(name="uncertainty::Univerity::Person")
uPerson = Class(name="uPerson")
Univerity_uncertainty_aPerson = Class(name="Univerity::uncertainty::aPerson", is_abstract=True)
Univerity_uncertainty_uUniversity = Class(name="Univerity::uncertainty::uUniversity")
uncertainty_Univerity_University = Class(name="uncertainty::Univerity::University")
uUniversity = Class(name="uUniversity")
Univerity_uncertainty_aUniversity = Class(name="Univerity::uncertainty::aUniversity", is_abstract=True)

# Univerity_Courses class attributes and methods
Univerity_Courses_Name: Property = Property(name="Name", type=StringType)
Univerity_Courses_CFU: Property = Property(name="CFU", type=IntegerType)
Univerity_Courses_Semester: Property = Property(name="Semester", type=StringType)
Univerity_Courses.attributes={Univerity_Courses_Semester, Univerity_Courses_Name, Univerity_Courses_CFU}

# uncertainty_ModelElement class attributes and methods

# uncertainty_aCourses class attributes and methods

# Univerity_Person class attributes and methods
Univerity_Person_Name: Property = Property(name="Name", type=StringType)
Univerity_Person_Email: Property = Property(name="Email", type=StringType)
Univerity_Person.attributes={Univerity_Person_Email, Univerity_Person_Name}

# aCourses class attributes and methods

# aPerson class attributes and methods

# Univerity_uncertainty_ModelElement class attributes and methods

# uncertainty_aPerson class attributes and methods

# Univerity_University class attributes and methods

# uncertainty_aUniversity class attributes and methods

# Univerity_uncertainty_uCourses class attributes and methods

# uncertainty_UData class attributes and methods

# ModelElement class attributes and methods

# uncertainty_Univerity_Courses class attributes and methods

# Univerity_uncertainty_UData class attributes and methods
Univerity_uncertainty_UData_name: Property = Property(name="name", type=StringType)
Univerity_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
Univerity_uncertainty_UData.attributes={Univerity_uncertainty_UData_utype, Univerity_uncertainty_UData_name}

# uCourses class attributes and methods

# Univerity_uncertainty_aCourses class attributes and methods

# Univerity_uncertainty_uPerson class attributes and methods

# uncertainty_Univerity_Person class attributes and methods

# uPerson class attributes and methods

# Univerity_uncertainty_aPerson class attributes and methods

# Univerity_uncertainty_uUniversity class attributes and methods

# uncertainty_Univerity_University class attributes and methods

# uUniversity class attributes and methods

# Univerity_uncertainty_aUniversity class attributes and methods

# Relationships
Professor1: BinaryAssociation = BinaryAssociation(
    name="Professor1",
    ends={
        Property(name="Univerity_Courses2", type=aPerson, multiplicity=Multiplicity(0, 1), is_composite=True),
        Property(name="aPerson", type=Univerity_Courses, multiplicity=Multiplicity(1, 1))
    }
)
Student3: BinaryAssociation = BinaryAssociation(
    name="Student3",
    ends={
        Property(name="aPerson5", type=Univerity_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Courses4", type=aPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links0: BinaryAssociation = BinaryAssociation(
    name="links0",
    ends={
        Property(name="aCourses", type=Univerity_Courses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Courses", type=aCourses, multiplicity=Multiplicity(0, 9999))
    }
)
Courses8: BinaryAssociation = BinaryAssociation(
    name="Courses8",
    ends={
        Property(name="aCourses9", type=Univerity_University, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_University", type=aCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatives6: BinaryAssociation = BinaryAssociation(
    name="relatives6",
    ends={
        Property(name="aPerson7", type=Univerity_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_Person", type=aPerson, multiplicity=Multiplicity(0, 1))
    }
)
include10: BinaryAssociation = BinaryAssociation(
    name="include10",
    ends={
        Property(name="ModelElement", type=Univerity_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uleft14: BinaryAssociation = BinaryAssociation(
    name="uleft14",
    ends={
        Property(name="uncertainty_Univerity_Courses", type=Univerity_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uCourses", type=uncertainty_Univerity_Courses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
exclude11: BinaryAssociation = BinaryAssociation(
    name="exclude11",
    ends={
        Property(name="ModelElement13", type=Univerity_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_ModelElement12", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uright15: BinaryAssociation = BinaryAssociation(
    name="uright15",
    ends={
        Property(name="uncertainty_Univerity_Courses17", type=Univerity_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uCourses16", type=uncertainty_Univerity_Courses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint18: BinaryAssociation = BinaryAssociation(
    name="upoint18",
    ends={
        Property(name="uCourses", type=Univerity_uncertainty_uCourses, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uCourses19", type=uCourses, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft20: BinaryAssociation = BinaryAssociation(
    name="uleft20",
    ends={
        Property(name="uncertainty_Univerity_Person", type=Univerity_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uPerson", type=uncertainty_Univerity_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright21: BinaryAssociation = BinaryAssociation(
    name="uright21",
    ends={
        Property(name="uncertainty_Univerity_Person23", type=Univerity_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uPerson22", type=uncertainty_Univerity_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint24: BinaryAssociation = BinaryAssociation(
    name="upoint24",
    ends={
        Property(name="uPerson", type=Univerity_uncertainty_uPerson, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uPerson25", type=uPerson, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft26: BinaryAssociation = BinaryAssociation(
    name="uleft26",
    ends={
        Property(name="uncertainty_Univerity_University", type=Univerity_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uUniversity", type=uncertainty_Univerity_University, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright27: BinaryAssociation = BinaryAssociation(
    name="uright27",
    ends={
        Property(name="uncertainty_Univerity_University29", type=Univerity_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uUniversity28", type=uncertainty_Univerity_University, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint30: BinaryAssociation = BinaryAssociation(
    name="upoint30",
    ends={
        Property(name="uUniversity", type=Univerity_uncertainty_uUniversity, multiplicity=Multiplicity(1, 1)),
        Property(name="Univerity_uncertainty_uUniversity31", type=uUniversity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Univerity_Courses_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Univerity_Courses)
gen_Univerity_Courses_uncertainty_aCourses = Generalization(general=uncertainty_aCourses, specific=Univerity_Courses)
gen_Univerity_Person_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Univerity_Person)
gen_Univerity_University_uncertainty_aUniversity = Generalization(general=uncertainty_aUniversity, specific=Univerity_University)
gen_Univerity_Person_uncertainty_aPerson = Generalization(general=uncertainty_aPerson, specific=Univerity_Person)
gen_Univerity_University_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Univerity_University)
gen_Univerity_uncertainty_uCourses_uncertainty_aCourses = Generalization(general=uncertainty_aCourses, specific=Univerity_uncertainty_uCourses)
gen_Univerity_uncertainty_uCourses_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Univerity_uncertainty_uCourses)
gen_Univerity_uncertainty_uPerson_uncertainty_aPerson = Generalization(general=uncertainty_aPerson, specific=Univerity_uncertainty_uPerson)
gen_Univerity_uncertainty_uPerson_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Univerity_uncertainty_uPerson)
gen_Univerity_uncertainty_uUniversity_uncertainty_aUniversity = Generalization(general=uncertainty_aUniversity, specific=Univerity_uncertainty_uUniversity)
gen_Univerity_uncertainty_uUniversity_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Univerity_uncertainty_uUniversity)

# Domain Model
domain_model = DomainModel(
    name="Univerity",
    types={Univerity_Courses, uncertainty_ModelElement, uncertainty_aCourses, Univerity_Person, aCourses, aPerson, Univerity_uncertainty_ModelElement, uncertainty_aPerson, Univerity_University, uncertainty_aUniversity, Univerity_uncertainty_uCourses, uncertainty_UData, ModelElement, uncertainty_Univerity_Courses, Univerity_uncertainty_UData, uCourses, Univerity_uncertainty_aCourses, Univerity_uncertainty_uPerson, uncertainty_Univerity_Person, uPerson, Univerity_uncertainty_aPerson, Univerity_uncertainty_uUniversity, uncertainty_Univerity_University, uUniversity, Univerity_uncertainty_aUniversity, OperatorType},
    associations={Professor1, Student3, links0, Courses8, relatives6, include10, uleft14, exclude11, uright15, upoint18, uleft20, uright21, upoint24, uleft26, uright27, upoint30},
    generalizations={gen_Univerity_Courses_uncertainty_ModelElement, gen_Univerity_Courses_uncertainty_aCourses, gen_Univerity_Person_uncertainty_ModelElement, gen_Univerity_University_uncertainty_aUniversity, gen_Univerity_Person_uncertainty_aPerson, gen_Univerity_University_uncertainty_ModelElement, gen_Univerity_uncertainty_uCourses_uncertainty_aCourses, gen_Univerity_uncertainty_uCourses_uncertainty_UData, gen_Univerity_uncertainty_uPerson_uncertainty_aPerson, gen_Univerity_uncertainty_uPerson_uncertainty_UData, gen_Univerity_uncertainty_uUniversity_uncertainty_aUniversity, gen_Univerity_uncertainty_uUniversity_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)