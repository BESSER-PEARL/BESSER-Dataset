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
Families_FamilyRegister = Class(name="Families::FamilyRegister")
uncertainty_ModelElement = Class(name="uncertainty::ModelElement")
uncertainty_aFamilyRegister = Class(name="uncertainty::aFamilyRegister")
aFamily = Class(name="aFamily")
Families_Family = Class(name="Families::Family")
uncertainty_aFamily = Class(name="uncertainty::aFamily")
aFamilyMember = Class(name="aFamilyMember")
aFamilyRegister = Class(name="aFamilyRegister")
Families_FamilyMember = Class(name="Families::FamilyMember")
uncertainty_aFamilyMember = Class(name="uncertainty::aFamilyMember")
Families_uncertainty_ModelElement = Class(name="Families::uncertainty::ModelElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
Families_uncertainty_UData = Class(name="Families::uncertainty::UData", is_abstract=True)
Families_uncertainty_aFamilyRegister = Class(name="Families::uncertainty::aFamilyRegister", is_abstract=True)
Families_uncertainty_uFamily = Class(name="Families::uncertainty::uFamily")
uncertainty_Families_Family = Class(name="uncertainty::Families::Family")
uFamily = Class(name="uFamily")
Families_uncertainty_aFamily = Class(name="Families::uncertainty::aFamily", is_abstract=True)
Families_uncertainty_uFamilyMember = Class(name="Families::uncertainty::uFamilyMember")
uncertainty_Families_FamilyMember = Class(name="uncertainty::Families::FamilyMember")
Families_uncertainty_uFamilyRegister = Class(name="Families::uncertainty::uFamilyRegister")
uncertainty_UData = Class(name="uncertainty::UData")
uncertainty_Families_FamilyRegister = Class(name="uncertainty::Families::FamilyRegister")
uFamilyRegister = Class(name="uFamilyRegister")
uFamilyMember = Class(name="uFamilyMember")
Families_uncertainty_aFamilyMember = Class(name="Families::uncertainty::aFamilyMember", is_abstract=True)

# Families_FamilyRegister class attributes and methods

# uncertainty_ModelElement class attributes and methods

# uncertainty_aFamilyRegister class attributes and methods

# aFamily class attributes and methods

# Families_Family class attributes and methods
Families_Family_name: Property = Property(name="name", type=StringType)
Families_Family.attributes={Families_Family_name}

# uncertainty_aFamily class attributes and methods

# aFamilyMember class attributes and methods

# aFamilyRegister class attributes and methods

# Families_FamilyMember class attributes and methods
Families_FamilyMember_name: Property = Property(name="name", type=StringType)
Families_FamilyMember.attributes={Families_FamilyMember_name}

# uncertainty_aFamilyMember class attributes and methods

# Families_uncertainty_ModelElement class attributes and methods

# ModelElement class attributes and methods

# Families_uncertainty_UData class attributes and methods
Families_uncertainty_UData_name: Property = Property(name="name", type=StringType)
Families_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
Families_uncertainty_UData.attributes={Families_uncertainty_UData_name, Families_uncertainty_UData_utype}

# Families_uncertainty_aFamilyRegister class attributes and methods

# Families_uncertainty_uFamily class attributes and methods

# uncertainty_Families_Family class attributes and methods

# uFamily class attributes and methods

# Families_uncertainty_aFamily class attributes and methods

# Families_uncertainty_uFamilyMember class attributes and methods

# uncertainty_Families_FamilyMember class attributes and methods

# Families_uncertainty_uFamilyRegister class attributes and methods

# uncertainty_UData class attributes and methods

# uncertainty_Families_FamilyRegister class attributes and methods

# uFamilyRegister class attributes and methods

# uFamilyMember class attributes and methods

# Families_uncertainty_aFamilyMember class attributes and methods

# Relationships
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="aFamily", type=Families_FamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyRegister", type=aFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
father1: BinaryAssociation = BinaryAssociation(
    name="father1",
    ends={
        Property(name="aFamilyMember", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=aFamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
daughters8: BinaryAssociation = BinaryAssociation(
    name="daughters8",
    ends={
        Property(name="aFamilyMember10", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family9", type=aFamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
familiesInverse11: BinaryAssociation = BinaryAssociation(
    name="familiesInverse11",
    ends={
        Property(name="aFamilyRegister", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family12", type=aFamilyRegister, multiplicity=Multiplicity(0, 1))
    }
)
fatherInverse13: BinaryAssociation = BinaryAssociation(
    name="fatherInverse13",
    ends={
        Property(name="aFamily14", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyMember", type=aFamily, multiplicity=Multiplicity(0, 1))
    }
)
motherInverse15: BinaryAssociation = BinaryAssociation(
    name="motherInverse15",
    ends={
        Property(name="aFamily17", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyMember16", type=aFamily, multiplicity=Multiplicity(0, 1))
    }
)
mother2: BinaryAssociation = BinaryAssociation(
    name="mother2",
    ends={
        Property(name="aFamilyMember4", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family3", type=aFamilyMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
sons5: BinaryAssociation = BinaryAssociation(
    name="sons5",
    ends={
        Property(name="aFamilyMember7", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family6", type=aFamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include24: BinaryAssociation = BinaryAssociation(
    name="include24",
    ends={
        Property(name="ModelElement", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
exclude25: BinaryAssociation = BinaryAssociation(
    name="exclude25",
    ends={
        Property(name="ModelElement27", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement26", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
sonsInverse18: BinaryAssociation = BinaryAssociation(
    name="sonsInverse18",
    ends={
        Property(name="aFamily20", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyMember19", type=aFamily, multiplicity=Multiplicity(0, 1))
    }
)
daughtersInverse21: BinaryAssociation = BinaryAssociation(
    name="daughtersInverse21",
    ends={
        Property(name="aFamily23", type=Families_FamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyMember22", type=aFamily, multiplicity=Multiplicity(0, 1))
    }
)
upoint32: BinaryAssociation = BinaryAssociation(
    name="upoint32",
    ends={
        Property(name="uFamilyRegister", type=Families_uncertainty_uFamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegister33", type=uFamilyRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft34: BinaryAssociation = BinaryAssociation(
    name="uleft34",
    ends={
        Property(name="uncertainty_Families_Family", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright35: BinaryAssociation = BinaryAssociation(
    name="uright35",
    ends={
        Property(name="uncertainty_Families_Family37", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily36", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint38: BinaryAssociation = BinaryAssociation(
    name="upoint38",
    ends={
        Property(name="uFamily", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily39", type=uFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft28: BinaryAssociation = BinaryAssociation(
    name="uleft28",
    ends={
        Property(name="uncertainty_Families_FamilyRegister", type=Families_uncertainty_uFamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegister", type=uncertainty_Families_FamilyRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright29: BinaryAssociation = BinaryAssociation(
    name="uright29",
    ends={
        Property(name="uncertainty_Families_FamilyRegister31", type=Families_uncertainty_uFamilyRegister, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegister30", type=uncertainty_Families_FamilyRegister, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft40: BinaryAssociation = BinaryAssociation(
    name="uleft40",
    ends={
        Property(name="uncertainty_Families_FamilyMember", type=Families_uncertainty_uFamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyMember", type=uncertainty_Families_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright41: BinaryAssociation = BinaryAssociation(
    name="uright41",
    ends={
        Property(name="uncertainty_Families_FamilyMember43", type=Families_uncertainty_uFamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyMember42", type=uncertainty_Families_FamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint44: BinaryAssociation = BinaryAssociation(
    name="upoint44",
    ends={
        Property(name="uFamilyMember", type=Families_uncertainty_uFamilyMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyMember45", type=uFamilyMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Families_FamilyRegister_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_FamilyRegister)
gen_Families_FamilyRegister_uncertainty_aFamilyRegister = Generalization(general=uncertainty_aFamilyRegister, specific=Families_FamilyRegister)
gen_Families_Family_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_Family)
gen_Families_Family_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_Family)
gen_Families_FamilyMember_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_FamilyMember)
gen_Families_FamilyMember_uncertainty_aFamilyMember = Generalization(general=uncertainty_aFamilyMember, specific=Families_FamilyMember)
gen_Families_uncertainty_uFamily_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uFamily_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uFamilyMember_uncertainty_aFamilyMember = Generalization(general=uncertainty_aFamilyMember, specific=Families_uncertainty_uFamilyMember)
gen_Families_uncertainty_uFamilyMember_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamilyMember)
gen_Families_uncertainty_uFamilyRegister_uncertainty_aFamilyRegister = Generalization(general=uncertainty_aFamilyRegister, specific=Families_uncertainty_uFamilyRegister)
gen_Families_uncertainty_uFamilyRegister_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamilyRegister)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_FamilyRegister, uncertainty_ModelElement, uncertainty_aFamilyRegister, aFamily, Families_Family, uncertainty_aFamily, aFamilyMember, aFamilyRegister, Families_FamilyMember, uncertainty_aFamilyMember, Families_uncertainty_ModelElement, ModelElement, Families_uncertainty_UData, Families_uncertainty_aFamilyRegister, Families_uncertainty_uFamily, uncertainty_Families_Family, uFamily, Families_uncertainty_aFamily, Families_uncertainty_uFamilyMember, uncertainty_Families_FamilyMember, Families_uncertainty_uFamilyRegister, uncertainty_UData, uncertainty_Families_FamilyRegister, uFamilyRegister, uFamilyMember, Families_uncertainty_aFamilyMember, OperatorType},
    associations={families0, father1, daughters8, familiesInverse11, fatherInverse13, motherInverse15, mother2, sons5, include24, exclude25, sonsInverse18, daughtersInverse21, upoint32, uleft34, uright35, upoint38, uleft28, uright29, uleft40, uright41, upoint44},
    generalizations={gen_Families_FamilyRegister_uncertainty_ModelElement, gen_Families_FamilyRegister_uncertainty_aFamilyRegister, gen_Families_Family_uncertainty_ModelElement, gen_Families_Family_uncertainty_aFamily, gen_Families_FamilyMember_uncertainty_ModelElement, gen_Families_FamilyMember_uncertainty_aFamilyMember, gen_Families_uncertainty_uFamily_uncertainty_aFamily, gen_Families_uncertainty_uFamily_uncertainty_UData, gen_Families_uncertainty_uFamilyMember_uncertainty_aFamilyMember, gen_Families_uncertainty_uFamilyMember_uncertainty_UData, gen_Families_uncertainty_uFamilyRegister_uncertainty_aFamilyRegister, gen_Families_uncertainty_uFamilyRegister_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)