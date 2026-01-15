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
geneology_Geneology = Class(name="geneology::Geneology")
geneology_Family = Class(name="geneology::Family")
geneology_Member = Class(name="geneology::Member")

# geneology_Geneology class attributes and methods

# geneology_Family class attributes and methods
geneology_Family_name: Property = Property(name="name", type=StringType)
geneology_Family.attributes={geneology_Family_name}

# geneology_Member class attributes and methods
geneology_Member_name: Property = Property(name="name", type=StringType)
geneology_Member_female: Property = Property(name="female", type=BooleanType)
geneology_Member.attributes={geneology_Member_name, geneology_Member_female}

# Relationships
members2: BinaryAssociation = BinaryAssociation(
    name="members2",
    ends={
        Property(name="family", type=geneology_Member, multiplicity=Multiplicity(1, 9999), is_composite=True),
        Property(name="Member", type=geneology_Family, multiplicity=Multiplicity(1, 1))
    }
)
families0: BinaryAssociation = BinaryAssociation(
    name="families0",
    ends={
        Property(name="Family", type=geneology_Geneology, multiplicity=Multiplicity(1, 1)),
        Property(name="geneology", type=geneology_Family, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
geneology1: BinaryAssociation = BinaryAssociation(
    name="geneology1",
    ends={
        Property(name="Geneology", type=geneology_Family, multiplicity=Multiplicity(1, 1)),
        Property(name="families", type=geneology_Geneology, multiplicity=Multiplicity(1, 1))
    }
)
family3: BinaryAssociation = BinaryAssociation(
    name="family3",
    ends={
        Property(name="Family4", type=geneology_Member, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=geneology_Family, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="geneology",
    types={geneology_Geneology, geneology_Family, geneology_Member},
    associations={members2, families0, geneology1, family3},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)