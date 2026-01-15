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
Families_Family = Class(name="Families::Family")
uncertainty_ModelElement = Class(name="uncertainty::ModelElement")
uncertainty_aFamily = Class(name="uncertainty::aFamily")
aMember = Class(name="aMember")
aFamily = Class(name="aFamily")
Families_Member = Class(name="Families::Member")
uncertainty_aMember = Class(name="uncertainty::aMember")
Families_FamilyRegistry = Class(name="Families::FamilyRegistry")
uncertainty_aFamilyRegistry = Class(name="uncertainty::aFamilyRegistry")
Families_uncertainty_ModelElement = Class(name="Families::uncertainty::ModelElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
Families_uncertainty_UData = Class(name="Families::uncertainty::UData", is_abstract=True)
Families_uncertainty_uFamily = Class(name="Families::uncertainty::uFamily")
uncertainty_UData = Class(name="uncertainty::UData")
uFamily = Class(name="uFamily")
Families_uncertainty_aFamily = Class(name="Families::uncertainty::aFamily", is_abstract=True)
uMember = Class(name="uMember")
Families_uncertainty_aMember = Class(name="Families::uncertainty::aMember", is_abstract=True)
Families_uncertainty_uFamilyRegistry = Class(name="Families::uncertainty::uFamilyRegistry")
aFamilyRegistry = Class(name="aFamilyRegistry")
uFamilyRegistry = Class(name="uFamilyRegistry")
Families_uncertainty_aFamilyRegistry = Class(name="Families::uncertainty::aFamilyRegistry", is_abstract=True)
Families_uncertainty_uMember = Class(name="Families::uncertainty::uMember")

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family_address: Property = Property(name="address", type=StringType)
Families_Family.attributes={Families_Family_address, Families_Family_lastName}

# uncertainty_ModelElement class attributes and methods

# uncertainty_aFamily class attributes and methods

# aMember class attributes and methods

# aFamily class attributes and methods

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member_age: Property = Property(name="age", type=IntegerType)
Families_Member.attributes={Families_Member_age, Families_Member_firstName}

# uncertainty_aMember class attributes and methods

# Families_FamilyRegistry class attributes and methods

# uncertainty_aFamilyRegistry class attributes and methods

# Families_uncertainty_ModelElement class attributes and methods

# ModelElement class attributes and methods

# Families_uncertainty_UData class attributes and methods
Families_uncertainty_UData_name: Property = Property(name="name", type=StringType)
Families_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
Families_uncertainty_UData.attributes={Families_uncertainty_UData_name, Families_uncertainty_UData_utype}

# Families_uncertainty_uFamily class attributes and methods

# uncertainty_UData class attributes and methods

# uFamily class attributes and methods

# Families_uncertainty_aFamily class attributes and methods

# uMember class attributes and methods

# Families_uncertainty_aMember class attributes and methods

# Families_uncertainty_uFamilyRegistry class attributes and methods

# aFamilyRegistry class attributes and methods

# uFamilyRegistry class attributes and methods

# Families_uncertainty_aFamilyRegistry class attributes and methods

# Families_uncertainty_uMember class attributes and methods

# Relationships
sons0: BinaryAssociation = BinaryAssociation(
    name="sons0",
    ends={
        Property(name="aMember", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
daughters1: BinaryAssociation = BinaryAssociation(
    name="daughters1",
    ends={
        Property(name="aMember3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family2", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
mother4: BinaryAssociation = BinaryAssociation(
    name="mother4",
    ends={
        Property(name="aMember6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family5", type=aMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father7: BinaryAssociation = BinaryAssociation(
    name="father7",
    ends={
        Property(name="aMember9", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family8", type=aMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
links10: BinaryAssociation = BinaryAssociation(
    name="links10",
    ends={
        Property(name="aFamily", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family11", type=aFamily, multiplicity=Multiplicity(0, 9999))
    }
)
relatives12: BinaryAssociation = BinaryAssociation(
    name="relatives12",
    ends={
        Property(name="aMember13", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member", type=aMember, multiplicity=Multiplicity(0, 1))
    }
)
families14: BinaryAssociation = BinaryAssociation(
    name="families14",
    ends={
        Property(name="aFamily15", type=Families_FamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyRegistry", type=aFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include16: BinaryAssociation = BinaryAssociation(
    name="include16",
    ends={
        Property(name="ModelElement", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
exclude17: BinaryAssociation = BinaryAssociation(
    name="exclude17",
    ends={
        Property(name="Families_uncertainty_ModelElement18", type=ModelElement, multiplicity=Multiplicity(0, 9999)),
        Property(name="ModelElement19", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1))
    }
)
uleft20: BinaryAssociation = BinaryAssociation(
    name="uleft20",
    ends={
        Property(name="aFamily21", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily", type=aFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright22: BinaryAssociation = BinaryAssociation(
    name="uright22",
    ends={
        Property(name="aFamily24", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily23", type=aFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint25: BinaryAssociation = BinaryAssociation(
    name="upoint25",
    ends={
        Property(name="uFamily", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily26", type=uFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft27: BinaryAssociation = BinaryAssociation(
    name="uleft27",
    ends={
        Property(name="aMember28", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright29: BinaryAssociation = BinaryAssociation(
    name="uright29",
    ends={
        Property(name="aMember31", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember30", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint32: BinaryAssociation = BinaryAssociation(
    name="upoint32",
    ends={
        Property(name="uMember", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember33", type=uMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft34: BinaryAssociation = BinaryAssociation(
    name="uleft34",
    ends={
        Property(name="aFamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry", type=aFamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright35: BinaryAssociation = BinaryAssociation(
    name="uright35",
    ends={
        Property(name="aFamilyRegistry37", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry36", type=aFamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint38: BinaryAssociation = BinaryAssociation(
    name="upoint38",
    ends={
        Property(name="uFamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry39", type=uFamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Families_Family_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_Family)
gen_Families_Family_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_Family)
gen_Families_Member_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_Member)
gen_Families_Member_uncertainty_aMember = Generalization(general=uncertainty_aMember, specific=Families_Member)
gen_Families_FamilyRegistry_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_FamilyRegistry)
gen_Families_FamilyRegistry_uncertainty_aFamilyRegistry = Generalization(general=uncertainty_aFamilyRegistry, specific=Families_FamilyRegistry)
gen_Families_uncertainty_uFamily_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uFamily_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry = Generalization(general=uncertainty_aFamilyRegistry, specific=Families_uncertainty_uFamilyRegistry)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamilyRegistry)
gen_Families_uncertainty_uMember_uncertainty_aMember = Generalization(general=uncertainty_aMember, specific=Families_uncertainty_uMember)
gen_Families_uncertainty_uMember_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uMember)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Family, uncertainty_ModelElement, uncertainty_aFamily, aMember, aFamily, Families_Member, uncertainty_aMember, Families_FamilyRegistry, uncertainty_aFamilyRegistry, Families_uncertainty_ModelElement, ModelElement, Families_uncertainty_UData, Families_uncertainty_uFamily, uncertainty_UData, uFamily, Families_uncertainty_aFamily, uMember, Families_uncertainty_aMember, Families_uncertainty_uFamilyRegistry, aFamilyRegistry, uFamilyRegistry, Families_uncertainty_aFamilyRegistry, Families_uncertainty_uMember, OperatorType},
    associations={sons0, daughters1, mother4, father7, links10, relatives12, families14, include16, exclude17, uleft20, uright22, upoint25, uleft27, uright29, upoint32, uleft34, uright35, upoint38},
    generalizations={gen_Families_Family_uncertainty_ModelElement, gen_Families_Family_uncertainty_aFamily, gen_Families_Member_uncertainty_ModelElement, gen_Families_Member_uncertainty_aMember, gen_Families_FamilyRegistry_uncertainty_ModelElement, gen_Families_FamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_uncertainty_uFamily_uncertainty_aFamily, gen_Families_uncertainty_uFamily_uncertainty_UData, gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData, gen_Families_uncertainty_uMember_uncertainty_aMember, gen_Families_uncertainty_uMember_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)