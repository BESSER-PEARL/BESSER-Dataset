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
StaffMemberType: Enumeration = Enumeration(
    name="StaffMemberType",
    literals={
            EnumerationLiteral(name="ResearchStudent"),
			EnumerationLiteral(name="Other"),
			EnumerationLiteral(name="Academic"),
			EnumerationLiteral(name="Research"),
			EnumerationLiteral(name="Technical"),
			EnumerationLiteral(name="Admin"),
			EnumerationLiteral(name="Honary")
    }
)

# Classes
university_StaffMember = Class(name="university::StaffMember")
university_Student = Class(name="university::Student")
university_Module = Class(name="university::Module")
university_Vehicle = Class(name="university::Vehicle")
university_Computer = Class(name="university::Computer")
university_Book = Class(name="university::Book")
university_University = Class(name="university::University")
NamedElement = Class(name="NamedElement")
university_Department = Class(name="university::Department")
university_Library = Class(name="university::Library")
university_PrimitiveType = Class(name="university::PrimitiveType")
university_NamedElement = Class(name="university::NamedElement", is_abstract=True)

# university_StaffMember class attributes and methods
university_StaffMember_staffMemberType: Property = Property(name="staffMemberType", type=StringType)
university_StaffMember.attributes={university_StaffMember_staffMemberType}

# university_Student class attributes and methods
university_Student_studentId: Property = Property(name="studentId", type=FloatType)
university_Student.attributes={university_Student_studentId}

# university_Module class attributes and methods

# university_Vehicle class attributes and methods
university_Vehicle_registrationNumber: Property = Property(name="registrationNumber", type=StringType)
university_Vehicle.attributes={university_Vehicle_registrationNumber}

# university_Computer class attributes and methods

# university_Book class attributes and methods
university_Book_ISBN: Property = Property(name="ISBN", type=StringType)
university_Book_authorNames: Property = Property(name="authorNames", type=StringType)
university_Book.attributes={university_Book_authorNames, university_Book_ISBN}

# university_University class attributes and methods

# NamedElement class attributes and methods

# university_Department class attributes and methods

# university_Library class attributes and methods

# university_PrimitiveType class attributes and methods
university_PrimitiveType_a: Property = Property(name="a", type=StringType)
university_PrimitiveType_b: Property = Property(name="b", type=IntegerType)
university_PrimitiveType_c: Property = Property(name="c", type=StringType)
university_PrimitiveType_bigIntList: Property = Property(name="bigIntList", type=StringType)
university_PrimitiveType_d: Property = Property(name="d", type=BooleanType)
university_PrimitiveType_e: Property = Property(name="e", type=StringType)
university_PrimitiveType_f: Property = Property(name="f", type=FloatType)
university_PrimitiveType_g: Property = Property(name="g", type=StringType)
university_PrimitiveType_h: Property = Property(name="h", type=StringType)
university_PrimitiveType_i: Property = Property(name="i", type=FloatType)
university_PrimitiveType_j: Property = Property(name="j", type=StringType)
university_PrimitiveType_k: Property = Property(name="k", type=StringType)
university_PrimitiveType_l: Property = Property(name="l", type=StringType)
university_PrimitiveType_m: Property = Property(name="m", type=StringType)
university_PrimitiveType_n: Property = Property(name="n", type=StringType)
university_PrimitiveType_o: Property = Property(name="o", type=StringType)
university_PrimitiveType_p: Property = Property(name="p", type=StringType)
university_PrimitiveType.attributes={university_PrimitiveType_h, university_PrimitiveType_a, university_PrimitiveType_k, university_PrimitiveType_e, university_PrimitiveType_c, university_PrimitiveType_i, university_PrimitiveType_j, university_PrimitiveType_m, university_PrimitiveType_l, university_PrimitiveType_b, university_PrimitiveType_f, university_PrimitiveType_o, university_PrimitiveType_d, university_PrimitiveType_g, university_PrimitiveType_n, university_PrimitiveType_bigIntList, university_PrimitiveType_p}

# university_NamedElement class attributes and methods
university_NamedElement_name: Property = Property(name="name", type=StringType)
university_NamedElement.attributes={university_NamedElement_name}

# Relationships
chancelor3: BinaryAssociation = BinaryAssociation(
    name="chancelor3",
    ends={
        Property(name="university_StaffMember", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University4", type=university_StaffMember, multiplicity=Multiplicity(0, 1))
    }
)
enrolledModules5: BinaryAssociation = BinaryAssociation(
    name="enrolledModules5",
    ends={
        Property(name="Module", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="enrolledStudents", type=university_Module, multiplicity=Multiplicity(0, 9999))
    }
)
registeredVehicle6: BinaryAssociation = BinaryAssociation(
    name="registeredVehicle6",
    ends={
        Property(name="university_Vehicle", type=university_Student, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Student", type=university_Vehicle, multiplicity=Multiplicity(0, 1))
    }
)
mainComputer7: BinaryAssociation = BinaryAssociation(
    name="mainComputer7",
    ends={
        Property(name="university_Computer", type=university_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Library8", type=university_Computer, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
books9: BinaryAssociation = BinaryAssociation(
    name="books9",
    ends={
        Property(name="university_Book", type=university_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Library10", type=university_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
departments0: BinaryAssociation = BinaryAssociation(
    name="departments0",
    ends={
        Property(name="university_Department", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University", type=university_Department, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
libraries1: BinaryAssociation = BinaryAssociation(
    name="libraries1",
    ends={
        Property(name="university_Library", type=university_University, multiplicity=Multiplicity(1, 1)),
        Property(name="university_University2", type=university_Library, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
taughtModules14: BinaryAssociation = BinaryAssociation(
    name="taughtModules14",
    ends={
        Property(name="Module15", type=university_StaffMember, multiplicity=Multiplicity(1, 1)),
        Property(name="moduleLecturers", type=university_Module, multiplicity=Multiplicity(0, 9999))
    }
)
registeredVehicles16: BinaryAssociation = BinaryAssociation(
    name="registeredVehicles16",
    ends={
        Property(name="university_Vehicle18", type=university_StaffMember, multiplicity=Multiplicity(1, 1)),
        Property(name="university_StaffMember17", type=university_Vehicle, multiplicity=Multiplicity(0, 3))
    }
)
staff19: BinaryAssociation = BinaryAssociation(
    name="staff19",
    ends={
        Property(name="university_StaffMember21", type=university_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Department20", type=university_StaffMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
students22: BinaryAssociation = BinaryAssociation(
    name="students22",
    ends={
        Property(name="university_Student24", type=university_Department, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Department23", type=university_Student, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
moduleLecturers25: BinaryAssociation = BinaryAssociation(
    name="moduleLecturers25",
    ends={
        Property(name="StaffMember", type=university_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="taughtModules", type=university_StaffMember, multiplicity=Multiplicity(0, 9999))
    }
)
libraryVans11: BinaryAssociation = BinaryAssociation(
    name="libraryVans11",
    ends={
        Property(name="university_Vehicle13", type=university_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="university_Library12", type=university_Vehicle, multiplicity=Multiplicity(0, 9999))
    }
)
enrolledStudents26: BinaryAssociation = BinaryAssociation(
    name="enrolledStudents26",
    ends={
        Property(name="Student", type=university_Module, multiplicity=Multiplicity(1, 1)),
        Property(name="enrolledModules", type=university_Student, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_university_Student_NamedElement = Generalization(general=NamedElement, specific=university_Student)
gen_university_Library_NamedElement = Generalization(general=NamedElement, specific=university_Library)
gen_university_University_NamedElement = Generalization(general=NamedElement, specific=university_University)
gen_university_Department_NamedElement = Generalization(general=NamedElement, specific=university_Department)
gen_university_Module_NamedElement = Generalization(general=NamedElement, specific=university_Module)
gen_university_Computer_NamedElement = Generalization(general=NamedElement, specific=university_Computer)
gen_university_Book_NamedElement = Generalization(general=NamedElement, specific=university_Book)
gen_university_StaffMember_NamedElement = Generalization(general=NamedElement, specific=university_StaffMember)

# Domain Model
domain_model = DomainModel(
    name="university",
    types={university_StaffMember, university_Student, university_Module, university_Vehicle, university_Computer, university_Book, university_University, NamedElement, university_Department, university_Library, university_PrimitiveType, university_NamedElement, StaffMemberType},
    associations={chancelor3, enrolledModules5, registeredVehicle6, mainComputer7, books9, departments0, libraries1, taughtModules14, registeredVehicles16, staff19, students22, moduleLecturers25, libraryVans11, enrolledStudents26},
    generalizations={gen_university_Student_NamedElement, gen_university_Library_NamedElement, gen_university_University_NamedElement, gen_university_Department_NamedElement, gen_university_Module_NamedElement, gen_university_Computer_NamedElement, gen_university_Book_NamedElement, gen_university_StaffMember_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)