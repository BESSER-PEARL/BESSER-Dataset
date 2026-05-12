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
AttributeType: Enumeration = Enumeration(
    name="AttributeType",
    literals={
            EnumerationLiteral(name="Simple"),
			EnumerationLiteral(name="Derivate")
    }
)

# Classes
Relational_Table = Class(name="Relational_Table")
Relational_Domain = Class(name="Relational_Domain")
Relational_Constraint = Class(name="Relational_Constraint")
Relational_CandidateKey = Class(name="Relational_CandidateKey")
Relational_Attribute = Class(name="Relational_Attribute")
Relational_ForeignKey = Class(name="Relational_ForeignKey")
Relational_Schema = Class(name="Relational_Schema")
CandidateKey = Class(name="CandidateKey")
Relational_PrimitiveType = Class(name="Relational_PrimitiveType")
Domain = Class(name="Domain")
Relational_EnumerationType = Class(name="Relational_EnumerationType")
Relational_EnumeratedLiteral = Class(name="Relational_EnumeratedLiteral")

# Relational_Table class attributes and methods
Relational_Table_name: Property = Property(name="name", type=StringType)
Relational_Table.attributes={Relational_Table_name}

# Relational_Domain class attributes and methods
Relational_Domain_name: Property = Property(name="name", type=StringType)
Relational_Domain.attributes={Relational_Domain_name}

# Relational_Constraint class attributes and methods
Relational_Constraint_name: Property = Property(name="name", type=StringType)
Relational_Constraint_description: Property = Property(name="description", type=StringType)
Relational_Constraint.attributes={Relational_Constraint_name, Relational_Constraint_description}

# Relational_CandidateKey class attributes and methods
Relational_CandidateKey_name: Property = Property(name="name", type=StringType)
Relational_CandidateKey.attributes={Relational_CandidateKey_name}

# Relational_Attribute class attributes and methods
Relational_Attribute_name: Property = Property(name="name", type=StringType)
Relational_Attribute_type: Property = Property(name="type", type=StringType)
Relational_Attribute_nullable: Property = Property(name="nullable", type=BooleanType)
Relational_Attribute_multiplicity: Property = Property(name="multiplicity", type=IntegerType)
Relational_Attribute.attributes={Relational_Attribute_name, Relational_Attribute_nullable, Relational_Attribute_type, Relational_Attribute_multiplicity}

# Relational_ForeignKey class attributes and methods

# Relational_Schema class attributes and methods
Relational_Schema_name: Property = Property(name="name", type=StringType)
Relational_Schema.attributes={Relational_Schema_name}

# CandidateKey class attributes and methods

# Relational_PrimitiveType class attributes and methods

# Domain class attributes and methods

# Relational_EnumerationType class attributes and methods

# Relational_EnumeratedLiteral class attributes and methods
Relational_EnumeratedLiteral_name: Property = Property(name="name", type=StringType)
Relational_EnumeratedLiteral.attributes={Relational_EnumeratedLiteral_name}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Relational_Table", type=Relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Schema", type=Relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domains1: BinaryAssociation = BinaryAssociation(
    name="domains1",
    ends={
        Property(name="Relational_Domain", type=Relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Schema2", type=Relational_Domain, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints3: BinaryAssociation = BinaryAssociation(
    name="constraints3",
    ends={
        Property(name="Relational_Constraint", type=Relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Schema4", type=Relational_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey5: BinaryAssociation = BinaryAssociation(
    name="primaryKey5",
    ends={
        Property(name="Relational_CandidateKey", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Table6", type=Relational_CandidateKey, multiplicity=Multiplicity(1, 1))
    }
)
candidateKey7: BinaryAssociation = BinaryAssociation(
    name="candidateKey7",
    ends={
        Property(name="Relational_CandidateKey9", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Table8", type=Relational_CandidateKey, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
attributes10: BinaryAssociation = BinaryAssociation(
    name="attributes10",
    ends={
        Property(name="Relational_Attribute", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Table11", type=Relational_Attribute, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
foreignKey12: BinaryAssociation = BinaryAssociation(
    name="foreignKey12",
    ends={
        Property(name="Relational_ForeignKey", type=Relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Table13", type=Relational_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attributes20: BinaryAssociation = BinaryAssociation(
    name="attributes20",
    ends={
        Property(name="Relational_Attribute22", type=Relational_CandidateKey, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_CandidateKey21", type=Relational_Attribute, multiplicity=Multiplicity(1, 9999))
    }
)
referencedTable23: BinaryAssociation = BinaryAssociation(
    name="referencedTable23",
    ends={
        Property(name="Relational_Table25", type=Relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_ForeignKey24", type=Relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
literals26: BinaryAssociation = BinaryAssociation(
    name="literals26",
    ends={
        Property(name="Relational_EnumeratedLiteral", type=Relational_EnumerationType, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_EnumerationType", type=Relational_EnumeratedLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
domain14: BinaryAssociation = BinaryAssociation(
    name="domain14",
    ends={
        Property(name="Relational_Domain16", type=Relational_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Attribute15", type=Relational_Domain, multiplicity=Multiplicity(1, 1))
    }
)
constraints17: BinaryAssociation = BinaryAssociation(
    name="constraints17",
    ends={
        Property(name="Relational_Constraint19", type=Relational_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="Relational_Domain18", type=Relational_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Relational_ForeignKey_CandidateKey = Generalization(general=CandidateKey, specific=Relational_ForeignKey)
gen_Relational_PrimitiveType_Domain = Generalization(general=Domain, specific=Relational_PrimitiveType)
gen_Relational_EnumerationType_Domain = Generalization(general=Domain, specific=Relational_EnumerationType)

# Domain Model
domain_model = DomainModel(
    name="Relational",
    types={Relational_Table, Relational_Domain, Relational_Constraint, Relational_CandidateKey, Relational_Attribute, Relational_ForeignKey, Relational_Schema, CandidateKey, Relational_PrimitiveType, Domain, Relational_EnumerationType, Relational_EnumeratedLiteral, AttributeType},
    associations={tables0, domains1, constraints3, primaryKey5, candidateKey7, attributes10, foreignKey12, attributes20, referencedTable23, literals26, domain14, constraints17},
    generalizations={gen_Relational_ForeignKey_CandidateKey, gen_Relational_PrimitiveType_Domain, gen_Relational_EnumerationType_Domain},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)