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
Families_Member = Class(name="Families::Member")
uncertainty_aMember = Class(name="uncertainty::aMember")
Families_FamilyRegistry = Class(name="Families::FamilyRegistry")
uncertainty_aFamilyRegistry = Class(name="uncertainty::aFamilyRegistry")
aFamily = Class(name="aFamily")
Families_uncertainty_UData = Class(name="Families::uncertainty::UData", is_abstract=True)
Families_uncertainty_uFamily = Class(name="Families::uncertainty::uFamily")
uncertainty_UData = Class(name="uncertainty::UData")
uncertainty_Families_Family = Class(name="uncertainty::Families::Family")
uFamily = Class(name="uFamily")
Families_uncertainty_ModelElement = Class(name="Families::uncertainty::ModelElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
Families_uncertainty_uMember = Class(name="Families::uncertainty::uMember")
uncertainty_Families_Member = Class(name="uncertainty::Families::Member")
Families_uncertainty_aFamily = Class(name="Families::uncertainty::aFamily", is_abstract=True)
Families_uncertainty_aMember = Class(name="Families::uncertainty::aMember", is_abstract=True)
Families_uncertainty_uFamilyRegistry = Class(name="Families::uncertainty::uFamilyRegistry")
uncertainty_Families_FamilyRegistry = Class(name="uncertainty::Families::FamilyRegistry")
uMember = Class(name="uMember")
uFamilyRegistry = Class(name="uFamilyRegistry")
Families_uncertainty_aFamilyRegistry = Class(name="Families::uncertainty::aFamilyRegistry", is_abstract=True)

# Families_Family class attributes and methods
Families_Family_lastName: Property = Property(name="lastName", type=StringType)
Families_Family_address: Property = Property(name="address", type=StringType)
Families_Family.attributes={Families_Family_address, Families_Family_lastName}

# uncertainty_ModelElement class attributes and methods

# uncertainty_aFamily class attributes and methods

# aMember class attributes and methods

# Families_Member class attributes and methods
Families_Member_firstName: Property = Property(name="firstName", type=StringType)
Families_Member_age: Property = Property(name="age", type=IntegerType)
Families_Member.attributes={Families_Member_age, Families_Member_firstName}

# uncertainty_aMember class attributes and methods

# Families_FamilyRegistry class attributes and methods

# uncertainty_aFamilyRegistry class attributes and methods

# aFamily class attributes and methods

# Families_uncertainty_UData class attributes and methods
Families_uncertainty_UData_name: Property = Property(name="name", type=StringType)
Families_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
Families_uncertainty_UData.attributes={Families_uncertainty_UData_name, Families_uncertainty_UData_utype}

# Families_uncertainty_uFamily class attributes and methods

# uncertainty_UData class attributes and methods

# uncertainty_Families_Family class attributes and methods

# uFamily class attributes and methods

# Families_uncertainty_ModelElement class attributes and methods

# ModelElement class attributes and methods

# Families_uncertainty_uMember class attributes and methods

# uncertainty_Families_Member class attributes and methods

# Families_uncertainty_aFamily class attributes and methods

# Families_uncertainty_aMember class attributes and methods

# Families_uncertainty_uFamilyRegistry class attributes and methods

# uncertainty_Families_FamilyRegistry class attributes and methods

# uMember class attributes and methods

# uFamilyRegistry class attributes and methods

# Families_uncertainty_aFamilyRegistry class attributes and methods

# Relationships
sons0: BinaryAssociation = BinaryAssociation(
    name="sons0",
    ends={
        Property(name="aMember", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links11: BinaryAssociation = BinaryAssociation(
    name="links11",
    ends={
        Property(name="Families_Family12", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family10", type=Families_Family, multiplicity=Multiplicity(0, 9999))
    }
)
relatives13: BinaryAssociation = BinaryAssociation(
    name="relatives13",
    ends={
        Property(name="aMember14", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member", type=aMember, multiplicity=Multiplicity(0, 1))
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
exclude17: BinaryAssociation = BinaryAssociation(
    name="exclude17",
    ends={
        Property(name="ModelElement19", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement18", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uleft20: BinaryAssociation = BinaryAssociation(
    name="uleft20",
    ends={
        Property(name="uncertainty_Families_Family", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright21: BinaryAssociation = BinaryAssociation(
    name="uright21",
    ends={
        Property(name="uncertainty_Families_Family23", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily22", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
families15: BinaryAssociation = BinaryAssociation(
    name="families15",
    ends={
        Property(name="aFamily", type=Families_FamilyRegistry, multiplicity=Multiplicity(1, 1)),
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
uleft26: BinaryAssociation = BinaryAssociation(
    name="uleft26",
    ends={
        Property(name="uncertainty_Families_Member", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember", type=uncertainty_Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright27: BinaryAssociation = BinaryAssociation(
    name="uright27",
    ends={
        Property(name="uncertainty_Families_Member29", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember28", type=uncertainty_Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint24: BinaryAssociation = BinaryAssociation(
    name="upoint24",
    ends={
        Property(name="uFamily", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily25", type=uFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft32: BinaryAssociation = BinaryAssociation(
    name="uleft32",
    ends={
        Property(name="uncertainty_Families_FamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry", type=uncertainty_Families_FamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint30: BinaryAssociation = BinaryAssociation(
    name="upoint30",
    ends={
        Property(name="uMember", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember31", type=uMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint36: BinaryAssociation = BinaryAssociation(
    name="upoint36",
    ends={
        Property(name="uFamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry37", type=uFamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright33: BinaryAssociation = BinaryAssociation(
    name="uright33",
    ends={
        Property(name="uncertainty_Families_FamilyRegistry35", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry34", type=uncertainty_Families_FamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
gen_Families_uncertainty_uMember_uncertainty_aMember = Generalization(general=uncertainty_aMember, specific=Families_uncertainty_uMember)
gen_Families_uncertainty_uMember_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uMember)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry = Generalization(general=uncertainty_aFamilyRegistry, specific=Families_uncertainty_uFamilyRegistry)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamilyRegistry)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Family, uncertainty_ModelElement, uncertainty_aFamily, aMember, Families_Member, uncertainty_aMember, Families_FamilyRegistry, uncertainty_aFamilyRegistry, aFamily, Families_uncertainty_UData, Families_uncertainty_uFamily, uncertainty_UData, uncertainty_Families_Family, uFamily, Families_uncertainty_ModelElement, ModelElement, Families_uncertainty_uMember, uncertainty_Families_Member, Families_uncertainty_aFamily, Families_uncertainty_aMember, Families_uncertainty_uFamilyRegistry, uncertainty_Families_FamilyRegistry, uMember, uFamilyRegistry, Families_uncertainty_aFamilyRegistry, OperatorType},
    associations={sons0, links11, relatives13, daughters1, mother4, father7, exclude17, uleft20, uright21, families15, include16, uleft26, uright27, upoint24, uleft32, upoint30, upoint36, uright33},
    generalizations={gen_Families_Family_uncertainty_ModelElement, gen_Families_Family_uncertainty_aFamily, gen_Families_Member_uncertainty_ModelElement, gen_Families_Member_uncertainty_aMember, gen_Families_FamilyRegistry_uncertainty_ModelElement, gen_Families_FamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_uncertainty_uFamily_uncertainty_aFamily, gen_Families_uncertainty_uFamily_uncertainty_UData, gen_Families_uncertainty_uMember_uncertainty_aMember, gen_Families_uncertainty_uMember_uncertainty_UData, gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)