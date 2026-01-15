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
fds_NamedElement = Class(name="fds::NamedElement", is_abstract=True)
fds_Database = Class(name="fds::Database")
NamedElement = Class(name="NamedElement")
fds_Table = Class(name="fds::Table")
fds_Column = Class(name="fds::Column")
fds_FunctionalDependency = Class(name="fds::FunctionalDependency")
fds_Restriction = Class(name="fds::Restriction", is_abstract=True)
fds_RestrictionColumn = Class(name="fds::RestrictionColumn")
fds_ForeignKey = Class(name="fds::ForeignKey")
Restriction = Class(name="Restriction")
fds_PrimaryKey = Class(name="fds::PrimaryKey")
fds_CandidateKey = Class(name="fds::CandidateKey")
CandidateKey = Class(name="CandidateKey")

# fds_NamedElement class attributes and methods
fds_NamedElement_name: Property = Property(name="name", type=StringType)
fds_NamedElement.attributes={fds_NamedElement_name}

# fds_Database class attributes and methods

# NamedElement class attributes and methods

# fds_Table class attributes and methods

# fds_Column class attributes and methods

# fds_FunctionalDependency class attributes and methods

# fds_Restriction class attributes and methods

# fds_RestrictionColumn class attributes and methods

# fds_ForeignKey class attributes and methods

# Restriction class attributes and methods

# fds_PrimaryKey class attributes and methods

# fds_CandidateKey class attributes and methods

# CandidateKey class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="fds_Table", type=fds_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_Database", type=fds_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="fds_Column", type=fds_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_Table2", type=fds_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
functionalDependencies3: BinaryAssociation = BinaryAssociation(
    name="functionalDependencies3",
    ends={
        Property(name="fds_FunctionalDependency", type=fds_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_Table4", type=fds_FunctionalDependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restrictions5: BinaryAssociation = BinaryAssociation(
    name="restrictions5",
    ends={
        Property(name="fds_Restriction", type=fds_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_Table6", type=fds_Restriction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
restrictionsColumns7: BinaryAssociation = BinaryAssociation(
    name="restrictionsColumns7",
    ends={
        Property(name="RestrictionColumn", type=fds_Restriction, multiplicity=Multiplicity(1, 1)),
        Property(name="restriction", type=fds_RestrictionColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey8: BinaryAssociation = BinaryAssociation(
    name="primaryKey8",
    ends={
        Property(name="fds_PrimaryKey", type=fds_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_ForeignKey", type=fds_PrimaryKey, multiplicity=Multiplicity(1, 1))
    }
)
determinant9: BinaryAssociation = BinaryAssociation(
    name="determinant9",
    ends={
        Property(name="fds_Column11", type=fds_FunctionalDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_FunctionalDependency10", type=fds_Column, multiplicity=Multiplicity(0, 9999))
    }
)
dependant12: BinaryAssociation = BinaryAssociation(
    name="dependant12",
    ends={
        Property(name="fds_Column14", type=fds_FunctionalDependency, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_FunctionalDependency13", type=fds_Column, multiplicity=Multiplicity(0, 9999))
    }
)
restriction15: BinaryAssociation = BinaryAssociation(
    name="restriction15",
    ends={
        Property(name="Restriction", type=fds_RestrictionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="restrictionsColumns", type=fds_Restriction, multiplicity=Multiplicity(1, 1))
    }
)
column16: BinaryAssociation = BinaryAssociation(
    name="column16",
    ends={
        Property(name="fds_Column17", type=fds_RestrictionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_RestrictionColumn", type=fds_Column, multiplicity=Multiplicity(1, 1))
    }
)
pkRestrictionColumn19: BinaryAssociation = BinaryAssociation(
    name="pkRestrictionColumn19",
    ends={
        Property(name="fds_RestrictionColumn20", type=fds_RestrictionColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="fds_RestrictionColumn18", type=fds_RestrictionColumn, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fds_Database_NamedElement = Generalization(general=NamedElement, specific=fds_Database)
gen_fds_Table_NamedElement = Generalization(general=NamedElement, specific=fds_Table)
gen_fds_Column_NamedElement = Generalization(general=NamedElement, specific=fds_Column)
gen_fds_Restriction_NamedElement = Generalization(general=NamedElement, specific=fds_Restriction)
gen_fds_ForeignKey_Restriction = Generalization(general=Restriction, specific=fds_ForeignKey)
gen_fds_CandidateKey_Restriction = Generalization(general=Restriction, specific=fds_CandidateKey)
gen_fds_PrimaryKey_CandidateKey = Generalization(general=CandidateKey, specific=fds_PrimaryKey)
gen_fds_RestrictionColumn_NamedElement = Generalization(general=NamedElement, specific=fds_RestrictionColumn)

# Domain Model
domain_model = DomainModel(
    name="fds",
    types={fds_NamedElement, fds_Database, NamedElement, fds_Table, fds_Column, fds_FunctionalDependency, fds_Restriction, fds_RestrictionColumn, fds_ForeignKey, Restriction, fds_PrimaryKey, fds_CandidateKey, CandidateKey},
    associations={tables0, columns1, functionalDependencies3, restrictions5, restrictionsColumns7, primaryKey8, determinant9, dependant12, restriction15, column16, pkRestrictionColumn19},
    generalizations={gen_fds_Database_NamedElement, gen_fds_Table_NamedElement, gen_fds_Column_NamedElement, gen_fds_Restriction_NamedElement, gen_fds_ForeignKey_Restriction, gen_fds_CandidateKey_Restriction, gen_fds_PrimaryKey_CandidateKey, gen_fds_RestrictionColumn_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)