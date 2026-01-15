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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="int"),
			EnumerationLiteral(name="bigInt"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="byteArray"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="undefined")
    }
)

# Classes
genericsql_DataBase = Class(name="genericsql::DataBase")
NamedElement = Class(name="NamedElement")
genericsql_Table = Class(name="genericsql::Table")
genericsql_PrimaryKey = Class(name="genericsql::PrimaryKey")
genericsql_NamedElement = Class(name="genericsql::NamedElement", is_abstract=True)
genericsql_ForeignKey = Class(name="genericsql::ForeignKey")
genericsql_Field = Class(name="genericsql::Field")
genericsql_Constraint = Class(name="genericsql::Constraint", is_abstract=True)
genericsql_Check = Class(name="genericsql::Check")
Constraint = Class(name="Constraint")
genericsql_Unique = Class(name="genericsql::Unique")

# genericsql_DataBase class attributes and methods

# NamedElement class attributes and methods

# genericsql_Table class attributes and methods

# genericsql_PrimaryKey class attributes and methods

# genericsql_NamedElement class attributes and methods
genericsql_NamedElement_name: Property = Property(name="name", type=StringType)
genericsql_NamedElement_comment: Property = Property(name="comment", type=StringType)
genericsql_NamedElement.attributes={genericsql_NamedElement_comment, genericsql_NamedElement_name}

# genericsql_ForeignKey class attributes and methods

# genericsql_Field class attributes and methods
genericsql_Field_size: Property = Property(name="size", type=IntegerType)
genericsql_Field_defaultValue: Property = Property(name="defaultValue", type=StringType)
genericsql_Field_specificType: Property = Property(name="specificType", type=StringType)
genericsql_Field_notNull: Property = Property(name="notNull", type=BooleanType)
genericsql_Field_unique: Property = Property(name="unique", type=BooleanType)
genericsql_Field_type: Property = Property(name="type", type=StringType)
genericsql_Field_autoIcrement: Property = Property(name="autoIcrement", type=BooleanType)
genericsql_Field.attributes={genericsql_Field_type, genericsql_Field_unique, genericsql_Field_notNull, genericsql_Field_specificType, genericsql_Field_defaultValue, genericsql_Field_autoIcrement, genericsql_Field_size}

# genericsql_Constraint class attributes and methods

# genericsql_Check class attributes and methods
genericsql_Check_expression: Property = Property(name="expression", type=StringType)
genericsql_Check.attributes={genericsql_Check_expression}

# Constraint class attributes and methods

# genericsql_Unique class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=genericsql_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=genericsql_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKey1: BinaryAssociation = BinaryAssociation(
    name="primaryKey1",
    ends={
        Property(name="PrimaryKey", type=genericsql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=genericsql_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
database7: BinaryAssociation = BinaryAssociation(
    name="database7",
    ends={
        Property(name="DataBase", type=genericsql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=genericsql_DataBase, multiplicity=Multiplicity(1, 1))
    }
)
primaryFields8: BinaryAssociation = BinaryAssociation(
    name="primaryFields8",
    ends={
        Property(name="genericsql_Field", type=genericsql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsql_PrimaryKey", type=genericsql_Field, multiplicity=Multiplicity(1, 9999))
    }
)
table9: BinaryAssociation = BinaryAssociation(
    name="table9",
    ends={
        Property(name="Table10", type=genericsql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey", type=genericsql_Table, multiplicity=Multiplicity(0, 1))
    }
)
foreignFields11: BinaryAssociation = BinaryAssociation(
    name="foreignFields11",
    ends={
        Property(name="genericsql_Field12", type=genericsql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsql_ForeignKey", type=genericsql_Field, multiplicity=Multiplicity(0, 9999))
    }
)
table13: BinaryAssociation = BinaryAssociation(
    name="table13",
    ends={
        Property(name="Table14", type=genericsql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=genericsql_Table, multiplicity=Multiplicity(0, 1))
    }
)
refersTo15: BinaryAssociation = BinaryAssociation(
    name="refersTo15",
    ends={
        Property(name="genericsql_PrimaryKey17", type=genericsql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsql_ForeignKey16", type=genericsql_PrimaryKey, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys2: BinaryAssociation = BinaryAssociation(
    name="foreignKeys2",
    ends={
        Property(name="ForeignKey", type=genericsql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table3", type=genericsql_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields4: BinaryAssociation = BinaryAssociation(
    name="fields4",
    ends={
        Property(name="Field", type=genericsql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=genericsql_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraints6: BinaryAssociation = BinaryAssociation(
    name="constraints6",
    ends={
        Property(name="genericsql_Constraint", type=genericsql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsql_Table", type=genericsql_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table18: BinaryAssociation = BinaryAssociation(
    name="table18",
    ends={
        Property(name="Table19", type=genericsql_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="fields", type=genericsql_Table, multiplicity=Multiplicity(1, 1))
    }
)
constrainedFields20: BinaryAssociation = BinaryAssociation(
    name="constrainedFields20",
    ends={
        Property(name="genericsql_Field22", type=genericsql_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="genericsql_Constraint21", type=genericsql_Field, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_genericsql_DataBase_NamedElement = Generalization(general=NamedElement, specific=genericsql_DataBase)
gen_genericsql_Table_NamedElement = Generalization(general=NamedElement, specific=genericsql_Table)
gen_genericsql_PrimaryKey_NamedElement = Generalization(general=NamedElement, specific=genericsql_PrimaryKey)
gen_genericsql_ForeignKey_NamedElement = Generalization(general=NamedElement, specific=genericsql_ForeignKey)
gen_genericsql_Check_Constraint = Generalization(general=Constraint, specific=genericsql_Check)
gen_genericsql_Unique_Constraint = Generalization(general=Constraint, specific=genericsql_Unique)
gen_genericsql_Field_NamedElement = Generalization(general=NamedElement, specific=genericsql_Field)

# Domain Model
domain_model = DomainModel(
    name="genericsql",
    types={genericsql_DataBase, NamedElement, genericsql_Table, genericsql_PrimaryKey, genericsql_NamedElement, genericsql_ForeignKey, genericsql_Field, genericsql_Constraint, genericsql_Check, Constraint, genericsql_Unique, Type},
    associations={tables0, primaryKey1, database7, primaryFields8, table9, foreignFields11, table13, refersTo15, foreignKeys2, fields4, constraints6, table18, constrainedFields20},
    generalizations={gen_genericsql_DataBase_NamedElement, gen_genericsql_Table_NamedElement, gen_genericsql_PrimaryKey_NamedElement, gen_genericsql_ForeignKey_NamedElement, gen_genericsql_Check_Constraint, gen_genericsql_Unique_Constraint, gen_genericsql_Field_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)