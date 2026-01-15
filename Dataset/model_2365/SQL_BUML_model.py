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
Action: Enumeration = Enumeration(
    name="Action",
    literals={
            EnumerationLiteral(name="Cascade"),
			EnumerationLiteral(name="SetNull")
    }
)

Condition: Enumeration = Enumeration(
    name="Condition",
    literals={
            EnumerationLiteral(name="Delete"),
			EnumerationLiteral(name="Update")
    }
)

Property_: Enumeration = Enumeration(
    name="Property",
    literals={
            EnumerationLiteral(name="NotNull"),
			EnumerationLiteral(name="AutoIncrement"),
			EnumerationLiteral(name="Unique")
    }
)

# Classes
sql_NamedElement = Class(name="sql::NamedElement", is_abstract=True)
ModelElement = Class(name="ModelElement")
sql_Table = Class(name="sql::Table")
NamedElement = Class(name="NamedElement")
sql_Column = Class(name="sql::Column")
sql_PrimaryKey = Class(name="sql::PrimaryKey")
sql_ForeignKey = Class(name="sql::ForeignKey")
sql_Key = Class(name="sql::Key", is_abstract=True)
sql_Schema = Class(name="sql::Schema")
Key = Class(name="Key")
sql_Event = Class(name="sql::Event")
sql_ModelElement = Class(name="sql::ModelElement", is_abstract=True)
sql_Annotation = Class(name="sql::Annotation")

# sql_NamedElement class attributes and methods
sql_NamedElement_name: Property = Property(name="name", type=StringType)
sql_NamedElement.attributes={sql_NamedElement_name}

# ModelElement class attributes and methods

# sql_Table class attributes and methods

# NamedElement class attributes and methods

# sql_Column class attributes and methods
sql_Column_type: Property = Property(name="type", type=StringType)
sql_Column_properties: Property = Property(name="properties", type=StringType)
sql_Column.attributes={sql_Column_type, sql_Column_properties}

# sql_PrimaryKey class attributes and methods

# sql_ForeignKey class attributes and methods

# sql_Key class attributes and methods

# sql_Schema class attributes and methods

# Key class attributes and methods

# sql_Event class attributes and methods
sql_Event_condition: Property = Property(name="condition", type=StringType)
sql_Event_action: Property = Property(name="action", type=StringType)
sql_Event.attributes={sql_Event_action, sql_Event_condition}

# sql_ModelElement class attributes and methods

# sql_Annotation class attributes and methods
sql_Annotation_annotation: Property = Property(name="annotation", type=StringType)
sql_Annotation.attributes={sql_Annotation_annotation}

# Relationships
referencingForeignKeys5: BinaryAssociation = BinaryAssociation(
    name="referencingForeignKeys5",
    ends={
        Property(name="referencedTable", type=sql_ForeignKey, multiplicity=Multiplicity(0, 9999)),
        Property(name="ForeignKey6", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
ownedColumns0: BinaryAssociation = BinaryAssociation(
    name="ownedColumns0",
    ends={
        Property(name="Column", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable", type=sql_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedPrimaryKey1: BinaryAssociation = BinaryAssociation(
    name="ownedPrimaryKey1",
    ends={
        Property(name="PrimaryKey", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable2", type=sql_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
ownedForeignKeys3: BinaryAssociation = BinaryAssociation(
    name="ownedForeignKeys3",
    ends={
        Property(name="ForeignKey", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owningTable4", type=sql_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningSchema7: BinaryAssociation = BinaryAssociation(
    name="owningSchema7",
    ends={
        Property(name="Schema", type=sql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedTables", type=sql_Schema, multiplicity=Multiplicity(1, 1))
    }
)
owningTable8: BinaryAssociation = BinaryAssociation(
    name="owningTable8",
    ends={
        Property(name="Table", type=sql_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedColumns", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
owningTable12: BinaryAssociation = BinaryAssociation(
    name="owningTable12",
    ends={
        Property(name="Table13", type=sql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedPrimaryKey", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
keys9: BinaryAssociation = BinaryAssociation(
    name="keys9",
    ends={
        Property(name="Key", type=sql_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="column", type=sql_Key, multiplicity=Multiplicity(0, 9999))
    }
)
column10: BinaryAssociation = BinaryAssociation(
    name="column10",
    ends={
        Property(name="Column11", type=sql_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="keys", type=sql_Column, multiplicity=Multiplicity(1, 1))
    }
)
ownedEvents18: BinaryAssociation = BinaryAssociation(
    name="ownedEvents18",
    ends={
        Property(name="owningForeignKey", type=sql_Event, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="Event", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
referencedTable14: BinaryAssociation = BinaryAssociation(
    name="referencedTable14",
    ends={
        Property(name="Table15", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingForeignKeys", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
owningTable16: BinaryAssociation = BinaryAssociation(
    name="owningTable16",
    ends={
        Property(name="Table17", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedForeignKeys", type=sql_Table, multiplicity=Multiplicity(1, 1))
    }
)
owningForeignKey19: BinaryAssociation = BinaryAssociation(
    name="owningForeignKey19",
    ends={
        Property(name="ForeignKey20", type=sql_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedEvents", type=sql_ForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
ownedTables21: BinaryAssociation = BinaryAssociation(
    name="ownedTables21",
    ends={
        Property(name="Table22", type=sql_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="owningSchema", type=sql_Table, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
ownedAnnotations23: BinaryAssociation = BinaryAssociation(
    name="ownedAnnotations23",
    ends={
        Property(name="Annotation", type=sql_ModelElement, multiplicity=Multiplicity(1, 1)),
        Property(name="owningModelElement", type=sql_Annotation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owningModelElement24: BinaryAssociation = BinaryAssociation(
    name="owningModelElement24",
    ends={
        Property(name="ModelElement", type=sql_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedAnnotations", type=sql_ModelElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_sql_NamedElement_ModelElement = Generalization(general=ModelElement, specific=sql_NamedElement)
gen_sql_Table_NamedElement = Generalization(general=NamedElement, specific=sql_Table)
gen_sql_Column_NamedElement = Generalization(general=NamedElement, specific=sql_Column)
gen_sql_Column_ModelElement = Generalization(general=ModelElement, specific=sql_Column)
gen_sql_Key_ModelElement = Generalization(general=ModelElement, specific=sql_Key)
gen_sql_PrimaryKey_Key = Generalization(general=Key, specific=sql_PrimaryKey)
gen_sql_ForeignKey_Key = Generalization(general=Key, specific=sql_ForeignKey)
gen_sql_Event_ModelElement = Generalization(general=ModelElement, specific=sql_Event)
gen_sql_Schema_NamedElement = Generalization(general=NamedElement, specific=sql_Schema)

# Domain Model
domain_model = DomainModel(
    name="sql",
    types={sql_NamedElement, ModelElement, sql_Table, NamedElement, sql_Column, sql_PrimaryKey, sql_ForeignKey, sql_Key, sql_Schema, Key, sql_Event, sql_ModelElement, sql_Annotation, Action, Condition, Property_},
    associations={referencingForeignKeys5, ownedColumns0, ownedPrimaryKey1, ownedForeignKeys3, owningSchema7, owningTable8, owningTable12, keys9, column10, ownedEvents18, referencedTable14, owningTable16, owningForeignKey19, ownedTables21, ownedAnnotations23, owningModelElement24},
    generalizations={gen_sql_NamedElement_ModelElement, gen_sql_Table_NamedElement, gen_sql_Column_NamedElement, gen_sql_Column_ModelElement, gen_sql_Key_ModelElement, gen_sql_PrimaryKey_Key, gen_sql_ForeignKey_Key, gen_sql_Event_ModelElement, gen_sql_Schema_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)