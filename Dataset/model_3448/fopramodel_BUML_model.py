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
Status: Enumeration = Enumeration(
    name="Status",
    literals={
            EnumerationLiteral(name="pending"),
			EnumerationLiteral(name="inprocess"),
			EnumerationLiteral(name="completed"),
			EnumerationLiteral(name="cancelled")
    }
)

Course: Enumeration = Enumeration(
    name="Course",
    literals={
            EnumerationLiteral(name="InfoBSc"),
			EnumerationLiteral(name="InfoMSc"),
			EnumerationLiteral(name="InfoDiplom"),
			EnumerationLiteral(name="InfoMinorSubject"),
			EnumerationLiteral(name="InfoPostGraduate")
    }
)

AuxiliaryKind: Enumeration = Enumeration(
    name="AuxiliaryKind",
    literals={
            EnumerationLiteral(name="ProgrammingLanguage"),
			EnumerationLiteral(name="Tool"),
			EnumerationLiteral(name="Method")
    }
)

# Classes
fopramodel_FoPra = Class(name="fopramodel::FoPra")
fopramodel_Student = Class(name="fopramodel::Student")
fopramodel_ResearchGroup = Class(name="fopramodel::ResearchGroup")
fopramodel_Associate = Class(name="fopramodel::Associate")
fopramodel_ExternalAdvisor = Class(name="fopramodel::ExternalAdvisor")
fopramodel_Auxiliary = Class(name="fopramodel::Auxiliary")
fopramodel_FoPraManagementSystem = Class(name="fopramodel::FoPraManagementSystem")
fopramodel_Person = Class(name="fopramodel::Person", is_abstract=True)
Person = Class(name="Person")
fopramodel_Professor = Class(name="fopramodel::Professor")

# fopramodel_FoPra class attributes and methods
fopramodel_FoPra_title: Property = Property(name="title", type=StringType)
fopramodel_FoPra_description: Property = Property(name="description", type=StringType)
fopramodel_FoPra_status: Property = Property(name="status", type=StringType)
fopramodel_FoPra_maxNumberOfStudents: Property = Property(name="maxNumberOfStudents", type=IntegerType)
fopramodel_FoPra_start: Property = Property(name="start", type=DateType)
fopramodel_FoPra_end: Property = Property(name="end", type=DateType)
fopramodel_FoPra.attributes={fopramodel_FoPra_maxNumberOfStudents, fopramodel_FoPra_start, fopramodel_FoPra_status, fopramodel_FoPra_description, fopramodel_FoPra_end, fopramodel_FoPra_title}

# fopramodel_Student class attributes and methods
fopramodel_Student_matrikel: Property = Property(name="matrikel", type=StringType)
fopramodel_Student_course: Property = Property(name="course", type=StringType)
fopramodel_Student.attributes={fopramodel_Student_course, fopramodel_Student_matrikel}

# fopramodel_ResearchGroup class attributes and methods
fopramodel_ResearchGroup_name: Property = Property(name="name", type=StringType)
fopramodel_ResearchGroup.attributes={fopramodel_ResearchGroup_name}

# fopramodel_Associate class attributes and methods

# fopramodel_ExternalAdvisor class attributes and methods
fopramodel_ExternalAdvisor_information: Property = Property(name="information", type=StringType)
fopramodel_ExternalAdvisor.attributes={fopramodel_ExternalAdvisor_information}

# fopramodel_Auxiliary class attributes and methods
fopramodel_Auxiliary_description: Property = Property(name="description", type=StringType)
fopramodel_Auxiliary_kind: Property = Property(name="kind", type=StringType)
fopramodel_Auxiliary.attributes={fopramodel_Auxiliary_kind, fopramodel_Auxiliary_description}

# fopramodel_FoPraManagementSystem class attributes and methods

# fopramodel_Person class attributes and methods
fopramodel_Person_forename: Property = Property(name="forename", type=StringType)
fopramodel_Person_lastname: Property = Property(name="lastname", type=StringType)
fopramodel_Person.attributes={fopramodel_Person_lastname, fopramodel_Person_forename}

# Person class attributes and methods

# fopramodel_Professor class attributes and methods

# Relationships
students0: BinaryAssociation = BinaryAssociation(
    name="students0",
    ends={
        Property(name="fopras", type=fopramodel_Student, multiplicity=Multiplicity(1, 9999)),
        Property(name="Student", type=fopramodel_FoPra, multiplicity=Multiplicity(1, 1))
    }
)
rg1: BinaryAssociation = BinaryAssociation(
    name="rg1",
    ends={
        Property(name="ResearchGroup", type=fopramodel_FoPra, multiplicity=Multiplicity(1, 1)),
        Property(name="fopras2", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1))
    }
)
supervisor3: BinaryAssociation = BinaryAssociation(
    name="supervisor3",
    ends={
        Property(name="Associate", type=fopramodel_FoPra, multiplicity=Multiplicity(1, 1)),
        Property(name="fopras4", type=fopramodel_Associate, multiplicity=Multiplicity(0, 1))
    }
)
advisor5: BinaryAssociation = BinaryAssociation(
    name="advisor5",
    ends={
        Property(name="ExternalAdvisor", type=fopramodel_FoPra, multiplicity=Multiplicity(1, 1)),
        Property(name="fopras6", type=fopramodel_ExternalAdvisor, multiplicity=Multiplicity(0, 9999))
    }
)
auxiliaries7: BinaryAssociation = BinaryAssociation(
    name="auxiliaries7",
    ends={
        Property(name="Auxiliary", type=fopramodel_FoPra, multiplicity=Multiplicity(1, 1)),
        Property(name="fopras8", type=fopramodel_Auxiliary, multiplicity=Multiplicity(1, 9999))
    }
)
fopras9: BinaryAssociation = BinaryAssociation(
    name="fopras9",
    ends={
        Property(name="fopramodel_FoPra", type=fopramodel_FoPraManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fopramodel_FoPraManagementSystem", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
persons10: BinaryAssociation = BinaryAssociation(
    name="persons10",
    ends={
        Property(name="fopramodel_Person", type=fopramodel_FoPraManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fopramodel_FoPraManagementSystem11", type=fopramodel_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
auxiliaries12: BinaryAssociation = BinaryAssociation(
    name="auxiliaries12",
    ends={
        Property(name="fopramodel_Auxiliary", type=fopramodel_FoPraManagementSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="fopramodel_FoPraManagementSystem13", type=fopramodel_Auxiliary, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fopras14: BinaryAssociation = BinaryAssociation(
    name="fopras14",
    ends={
        Property(name="FoPra", type=fopramodel_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="students", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999))
    }
)
rg15: BinaryAssociation = BinaryAssociation(
    name="rg15",
    ends={
        Property(name="ResearchGroup16", type=fopramodel_Professor, multiplicity=Multiplicity(1, 1)),
        Property(name="professor", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
fopras17: BinaryAssociation = BinaryAssociation(
    name="fopras17",
    ends={
        Property(name="FoPra18", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rg", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999))
    }
)
professor19: BinaryAssociation = BinaryAssociation(
    name="professor19",
    ends={
        Property(name="Professor", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rg20", type=fopramodel_Professor, multiplicity=Multiplicity(1, 1))
    }
)
associate21: BinaryAssociation = BinaryAssociation(
    name="associate21",
    ends={
        Property(name="Associate23", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1)),
        Property(name="rg22", type=fopramodel_Associate, multiplicity=Multiplicity(0, 9999))
    }
)
rg24: BinaryAssociation = BinaryAssociation(
    name="rg24",
    ends={
        Property(name="ResearchGroup25", type=fopramodel_Associate, multiplicity=Multiplicity(1, 1)),
        Property(name="associate", type=fopramodel_ResearchGroup, multiplicity=Multiplicity(1, 1))
    }
)
fopras26: BinaryAssociation = BinaryAssociation(
    name="fopras26",
    ends={
        Property(name="FoPra27", type=fopramodel_Associate, multiplicity=Multiplicity(1, 1)),
        Property(name="supervisor", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999))
    }
)
fopras28: BinaryAssociation = BinaryAssociation(
    name="fopras28",
    ends={
        Property(name="FoPra29", type=fopramodel_ExternalAdvisor, multiplicity=Multiplicity(1, 1)),
        Property(name="advisor", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999))
    }
)
fopras30: BinaryAssociation = BinaryAssociation(
    name="fopras30",
    ends={
        Property(name="FoPra31", type=fopramodel_Auxiliary, multiplicity=Multiplicity(1, 1)),
        Property(name="auxiliaries", type=fopramodel_FoPra, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_fopramodel_Student_Person = Generalization(general=Person, specific=fopramodel_Student)
gen_fopramodel_Professor_Person = Generalization(general=Person, specific=fopramodel_Professor)
gen_fopramodel_Associate_Person = Generalization(general=Person, specific=fopramodel_Associate)
gen_fopramodel_ExternalAdvisor_Person = Generalization(general=Person, specific=fopramodel_ExternalAdvisor)

# Domain Model
domain_model = DomainModel(
    name="fopramodel",
    types={fopramodel_FoPra, fopramodel_Student, fopramodel_ResearchGroup, fopramodel_Associate, fopramodel_ExternalAdvisor, fopramodel_Auxiliary, fopramodel_FoPraManagementSystem, fopramodel_Person, Person, fopramodel_Professor, Status, Course, AuxiliaryKind},
    associations={students0, rg1, supervisor3, advisor5, auxiliaries7, fopras9, persons10, auxiliaries12, fopras14, rg15, fopras17, professor19, associate21, rg24, fopras26, fopras28, fopras30},
    generalizations={gen_fopramodel_Student_Person, gen_fopramodel_Professor_Person, gen_fopramodel_Associate_Person, gen_fopramodel_ExternalAdvisor_Person},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)