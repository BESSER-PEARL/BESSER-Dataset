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
aFamily = Class(name="aFamily")
Families_FamilyRegistry = Class(name="Families::FamilyRegistry")
uncertainty_aFamilyRegistry = Class(name="uncertainty::aFamilyRegistry")
uncertainty_aMember = Class(name="uncertainty::aMember")
Families_uncertainty_ModelElement = Class(name="Families::uncertainty::ModelElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
Families_uncertainty_UData = Class(name="Families::uncertainty::UData", is_abstract=True)
Families_uncertainty_uFamily = Class(name="Families::uncertainty::uFamily")
uncertainty_UData = Class(name="uncertainty::UData")
uncertainty_Families_Family = Class(name="uncertainty::Families::Family")
Families_uncertainty_aFamily = Class(name="Families::uncertainty::aFamily", is_abstract=True)
Families_uncertainty_uMember = Class(name="Families::uncertainty::uMember")
uncertainty_Families_Member = Class(name="uncertainty::Families::Member")
uMember = Class(name="uMember")
Families_uncertainty_aMember = Class(name="Families::uncertainty::aMember", is_abstract=True)
Families_uncertainty_uFamilyRegistry = Class(name="Families::uncertainty::uFamilyRegistry")
uncertainty_Families_FamilyRegistry = Class(name="uncertainty::Families::FamilyRegistry")
uFamily = Class(name="uFamily")
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
Families_Member.attributes={Families_Member_firstName, Families_Member_age}

# aFamily class attributes and methods

# Families_FamilyRegistry class attributes and methods

# uncertainty_aFamilyRegistry class attributes and methods

# uncertainty_aMember class attributes and methods

# Families_uncertainty_ModelElement class attributes and methods

# ModelElement class attributes and methods

# Families_uncertainty_UData class attributes and methods
Families_uncertainty_UData_name: Property = Property(name="name", type=StringType)
Families_uncertainty_UData_utype: Property = Property(name="utype", type=StringType)
Families_uncertainty_UData.attributes={Families_uncertainty_UData_name, Families_uncertainty_UData_utype}

# Families_uncertainty_uFamily class attributes and methods

# uncertainty_UData class attributes and methods

# uncertainty_Families_Family class attributes and methods

# Families_uncertainty_aFamily class attributes and methods

# Families_uncertainty_uMember class attributes and methods

# uncertainty_Families_Member class attributes and methods

# uMember class attributes and methods

# Families_uncertainty_aMember class attributes and methods

# Families_uncertainty_uFamilyRegistry class attributes and methods

# uncertainty_Families_FamilyRegistry class attributes and methods

# uFamily class attributes and methods

# uFamilyRegistry class attributes and methods

# Families_uncertainty_aFamilyRegistry class attributes and methods

# Relationships
mother1: BinaryAssociation = BinaryAssociation(
    name="mother1",
    ends={
        Property(name="aMember3", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family2", type=aMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
father4: BinaryAssociation = BinaryAssociation(
    name="father4",
    ends={
        Property(name="aMember6", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family5", type=aMember, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children0: BinaryAssociation = BinaryAssociation(
    name="children0",
    ends={
        Property(name="aMember", type=Families_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Family", type=aMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
guardian7: BinaryAssociation = BinaryAssociation(
    name="guardian7",
    ends={
        Property(name="aFamily", type=Families_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_Member", type=aFamily, multiplicity=Multiplicity(0, 1))
    }
)
families8: BinaryAssociation = BinaryAssociation(
    name="families8",
    ends={
        Property(name="aFamily9", type=Families_FamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_FamilyRegistry", type=aFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
include10: BinaryAssociation = BinaryAssociation(
    name="include10",
    ends={
        Property(name="ModelElement", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
exclude11: BinaryAssociation = BinaryAssociation(
    name="exclude11",
    ends={
        Property(name="ModelElement13", type=Families_uncertainty_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_ModelElement12", type=ModelElement, multiplicity=Multiplicity(0, 9999))
    }
)
uleft14: BinaryAssociation = BinaryAssociation(
    name="uleft14",
    ends={
        Property(name="uncertainty_Families_Family", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint18: BinaryAssociation = BinaryAssociation(
    name="upoint18",
    ends={
        Property(name="uFamily", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily19", type=uFamily, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft20: BinaryAssociation = BinaryAssociation(
    name="uleft20",
    ends={
        Property(name="uncertainty_Families_Member", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember", type=uncertainty_Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright21: BinaryAssociation = BinaryAssociation(
    name="uright21",
    ends={
        Property(name="uncertainty_Families_Member23", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember22", type=uncertainty_Families_Member, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint24: BinaryAssociation = BinaryAssociation(
    name="upoint24",
    ends={
        Property(name="uMember", type=Families_uncertainty_uMember, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uMember25", type=uMember, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uleft26: BinaryAssociation = BinaryAssociation(
    name="uleft26",
    ends={
        Property(name="uncertainty_Families_FamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry", type=uncertainty_Families_FamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright15: BinaryAssociation = BinaryAssociation(
    name="uright15",
    ends={
        Property(name="uncertainty_Families_Family17", type=Families_uncertainty_uFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamily16", type=uncertainty_Families_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
upoint30: BinaryAssociation = BinaryAssociation(
    name="upoint30",
    ends={
        Property(name="uFamilyRegistry", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry31", type=uFamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uright27: BinaryAssociation = BinaryAssociation(
    name="uright27",
    ends={
        Property(name="uncertainty_Families_FamilyRegistry29", type=Families_uncertainty_uFamilyRegistry, multiplicity=Multiplicity(1, 1)),
        Property(name="Families_uncertainty_uFamilyRegistry28", type=uncertainty_Families_FamilyRegistry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Families_Family_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_Family)
gen_Families_Family_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_Family)
gen_Families_Member_uncertainty_aMember = Generalization(general=uncertainty_aMember, specific=Families_Member)
gen_Families_FamilyRegistry_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_FamilyRegistry)
gen_Families_FamilyRegistry_uncertainty_aFamilyRegistry = Generalization(general=uncertainty_aFamilyRegistry, specific=Families_FamilyRegistry)
gen_Families_Member_uncertainty_ModelElement = Generalization(general=uncertainty_ModelElement, specific=Families_Member)
gen_Families_uncertainty_uFamily_uncertainty_aFamily = Generalization(general=uncertainty_aFamily, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uFamily_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamily)
gen_Families_uncertainty_uMember_uncertainty_aMember = Generalization(general=uncertainty_aMember, specific=Families_uncertainty_uMember)
gen_Families_uncertainty_uMember_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uMember)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry = Generalization(general=uncertainty_aFamilyRegistry, specific=Families_uncertainty_uFamilyRegistry)
gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData = Generalization(general=uncertainty_UData, specific=Families_uncertainty_uFamilyRegistry)

# Domain Model
domain_model = DomainModel(
    name="Families",
    types={Families_Family, uncertainty_ModelElement, uncertainty_aFamily, aMember, Families_Member, aFamily, Families_FamilyRegistry, uncertainty_aFamilyRegistry, uncertainty_aMember, Families_uncertainty_ModelElement, ModelElement, Families_uncertainty_UData, Families_uncertainty_uFamily, uncertainty_UData, uncertainty_Families_Family, Families_uncertainty_aFamily, Families_uncertainty_uMember, uncertainty_Families_Member, uMember, Families_uncertainty_aMember, Families_uncertainty_uFamilyRegistry, uncertainty_Families_FamilyRegistry, uFamily, uFamilyRegistry, Families_uncertainty_aFamilyRegistry, OperatorType},
    associations={mother1, father4, children0, guardian7, families8, include10, exclude11, uleft14, upoint18, uleft20, uright21, upoint24, uleft26, uright15, upoint30, uright27},
    generalizations={gen_Families_Family_uncertainty_ModelElement, gen_Families_Family_uncertainty_aFamily, gen_Families_Member_uncertainty_aMember, gen_Families_FamilyRegistry_uncertainty_ModelElement, gen_Families_FamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_Member_uncertainty_ModelElement, gen_Families_uncertainty_uFamily_uncertainty_aFamily, gen_Families_uncertainty_uFamily_uncertainty_UData, gen_Families_uncertainty_uMember_uncertainty_aMember, gen_Families_uncertainty_uMember_uncertainty_UData, gen_Families_uncertainty_uFamilyRegistry_uncertainty_aFamilyRegistry, gen_Families_uncertainty_uFamilyRegistry_uncertainty_UData},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)