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
dDL_Data_definition = Class(name="dDL::Data::definition")
dDL_Definition = Class(name="dDL::Definition")
dDL_Create_table = Class(name="dDL::Create::table")
Definition = Class(name="Definition")
dDL_Column = Class(name="dDL::Column")
dDL_TYPE = Class(name="dDL::TYPE")
dDL_ISNULL = Class(name="dDL::ISNULL")
dDL_Alter_table = Class(name="dDL::Alter::table")
dDL_Tabname = Class(name="dDL::Tabname")
dDL_Comment = Class(name="dDL::Comment")
dDL_Constraint = Class(name="dDL::Constraint")
dDL_Sequence_options = Class(name="dDL::Sequence::options")
dDL_Colname = Class(name="dDL::Colname")
dDL_Create_sequence = Class(name="dDL::Create::sequence")
dDL_Primary_key = Class(name="dDL::Primary::key")
Key = Class(name="Key")
dDL_Unique_key = Class(name="dDL::Unique::key")
dDL_Foreign_key = Class(name="dDL::Foreign::key")
dDL_Key = Class(name="dDL::Key")

# dDL_Data_definition class attributes and methods

# dDL_Definition class attributes and methods

# dDL_Create_table class attributes and methods
dDL_Create_table_id: Property = Property(name="id", type=StringType)
dDL_Create_table.attributes={dDL_Create_table_id}

# Definition class attributes and methods

# dDL_Column class attributes and methods
dDL_Column_number: Property = Property(name="number", type=IntegerType)
dDL_Column_id: Property = Property(name="id", type=StringType)
dDL_Column.attributes={dDL_Column_id, dDL_Column_number}

# dDL_TYPE class attributes and methods
dDL_TYPE_id: Property = Property(name="id", type=StringType)
dDL_TYPE.attributes={dDL_TYPE_id}

# dDL_ISNULL class attributes and methods
dDL_ISNULL_null: Property = Property(name="null", type=BooleanType)
dDL_ISNULL_nonNull: Property = Property(name="nonNull", type=BooleanType)
dDL_ISNULL.attributes={dDL_ISNULL_null, dDL_ISNULL_nonNull}

# dDL_Alter_table class attributes and methods
dDL_Alter_table_add: Property = Property(name="add", type=StringType)
dDL_Alter_table_enable: Property = Property(name="enable", type=StringType)
dDL_Alter_table_id: Property = Property(name="id", type=StringType)
dDL_Alter_table.attributes={dDL_Alter_table_add, dDL_Alter_table_enable, dDL_Alter_table_id}

# dDL_Tabname class attributes and methods
dDL_Tabname_id: Property = Property(name="id", type=StringType)
dDL_Tabname_basename: Property = Property(name="basename", type=StringType)
dDL_Tabname.attributes={dDL_Tabname_id, dDL_Tabname_basename}

# dDL_Comment class attributes and methods
dDL_Comment_columnId: Property = Property(name="columnId", type=StringType)
dDL_Comment_string: Property = Property(name="string", type=StringType)
dDL_Comment.attributes={dDL_Comment_columnId, dDL_Comment_string}

# dDL_Constraint class attributes and methods
dDL_Constraint_id: Property = Property(name="id", type=StringType)
dDL_Constraint.attributes={dDL_Constraint_id}

# dDL_Sequence_options class attributes and methods
dDL_Sequence_options_increment: Property = Property(name="increment", type=StringType)
dDL_Sequence_options_start: Property = Property(name="start", type=StringType)
dDL_Sequence_options_maxvalue: Property = Property(name="maxvalue", type=StringType)
dDL_Sequence_options_nomaxvalue: Property = Property(name="nomaxvalue", type=StringType)
dDL_Sequence_options_minvalue: Property = Property(name="minvalue", type=StringType)
dDL_Sequence_options_nominvalue: Property = Property(name="nominvalue", type=StringType)
dDL_Sequence_options_cycle: Property = Property(name="cycle", type=StringType)
dDL_Sequence_options_nocycle: Property = Property(name="nocycle", type=StringType)
dDL_Sequence_options_cache: Property = Property(name="cache", type=StringType)
dDL_Sequence_options_nocache: Property = Property(name="nocache", type=StringType)
dDL_Sequence_options_order: Property = Property(name="order", type=StringType)
dDL_Sequence_options_noorder: Property = Property(name="noorder", type=StringType)
dDL_Sequence_options.attributes={dDL_Sequence_options_nominvalue, dDL_Sequence_options_increment, dDL_Sequence_options_nomaxvalue, dDL_Sequence_options_start, dDL_Sequence_options_nocache, dDL_Sequence_options_nocycle, dDL_Sequence_options_order, dDL_Sequence_options_noorder, dDL_Sequence_options_maxvalue, dDL_Sequence_options_cache, dDL_Sequence_options_minvalue, dDL_Sequence_options_cycle}

# dDL_Colname class attributes and methods
dDL_Colname_id: Property = Property(name="id", type=StringType)
dDL_Colname.attributes={dDL_Colname_id}

# dDL_Create_sequence class attributes and methods
dDL_Create_sequence_id: Property = Property(name="id", type=StringType)
dDL_Create_sequence.attributes={dDL_Create_sequence_id}

# dDL_Primary_key class attributes and methods

# Key class attributes and methods

# dDL_Unique_key class attributes and methods

# dDL_Foreign_key class attributes and methods

# dDL_Key class attributes and methods

# Relationships
definitions0: BinaryAssociation = BinaryAssociation(
    name="definitions0",
    ends={
        Property(name="dDL_Definition", type=dDL_Data_definition, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Data_definition", type=dDL_Definition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="dDL_Column", type=dDL_Create_table, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Create_table", type=dDL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="dDL_TYPE", type=dDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Column5", type=dDL_TYPE, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
isNull6: BinaryAssociation = BinaryAssociation(
    name="isNull6",
    ends={
        Property(name="dDL_ISNULL", type=dDL_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Column7", type=dDL_ISNULL, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabname8: BinaryAssociation = BinaryAssociation(
    name="tabname8",
    ends={
        Property(name="dDL_Tabname", type=dDL_Alter_table, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Alter_table", type=dDL_Tabname, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint9: BinaryAssociation = BinaryAssociation(
    name="constraint9",
    ends={
        Property(name="dDL_Constraint11", type=dDL_Alter_table, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Alter_table10", type=dDL_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabname12: BinaryAssociation = BinaryAssociation(
    name="tabname12",
    ends={
        Property(name="dDL_Tabname13", type=dDL_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Comment", type=dDL_Tabname, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints2: BinaryAssociation = BinaryAssociation(
    name="constraints2",
    ends={
        Property(name="dDL_Constraint", type=dDL_Create_table, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Create_table3", type=dDL_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sequence_options16: BinaryAssociation = BinaryAssociation(
    name="sequence_options16",
    ends={
        Property(name="dDL_Sequence_options", type=dDL_Create_sequence, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Create_sequence", type=dDL_Sequence_options, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
colname14: BinaryAssociation = BinaryAssociation(
    name="colname14",
    ends={
        Property(name="dDL_Colname", type=dDL_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Comment15", type=dDL_Colname, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tabname22: BinaryAssociation = BinaryAssociation(
    name="tabname22",
    ends={
        Property(name="dDL_Tabname23", type=dDL_Foreign_key, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Foreign_key", type=dDL_Tabname, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
key17: BinaryAssociation = BinaryAssociation(
    name="key17",
    ends={
        Property(name="dDL_Key", type=dDL_Constraint, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Constraint18", type=dDL_Key, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
colNames19: BinaryAssociation = BinaryAssociation(
    name="colNames19",
    ends={
        Property(name="dDL_Colname21", type=dDL_Key, multiplicity=Multiplicity(1, 1)),
        Property(name="dDL_Key20", type=dDL_Colname, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dDL_Create_table_Definition = Generalization(general=Definition, specific=dDL_Create_table)
gen_dDL_Alter_table_Definition = Generalization(general=Definition, specific=dDL_Alter_table)
gen_dDL_Comment_Definition = Generalization(general=Definition, specific=dDL_Comment)
gen_dDL_Create_sequence_Definition = Generalization(general=Definition, specific=dDL_Create_sequence)
gen_dDL_Primary_key_Key = Generalization(general=Key, specific=dDL_Primary_key)
gen_dDL_Unique_key_Key = Generalization(general=Key, specific=dDL_Unique_key)
gen_dDL_Foreign_key_Key = Generalization(general=Key, specific=dDL_Foreign_key)

# Domain Model
domain_model = DomainModel(
    name="dDL",
    types={dDL_Data_definition, dDL_Definition, dDL_Create_table, Definition, dDL_Column, dDL_TYPE, dDL_ISNULL, dDL_Alter_table, dDL_Tabname, dDL_Comment, dDL_Constraint, dDL_Sequence_options, dDL_Colname, dDL_Create_sequence, dDL_Primary_key, Key, dDL_Unique_key, dDL_Foreign_key, dDL_Key},
    associations={definitions0, columns1, type4, isNull6, tabname8, constraint9, tabname12, constraints2, sequence_options16, colname14, tabname22, key17, colNames19},
    generalizations={gen_dDL_Create_table_Definition, gen_dDL_Alter_table_Definition, gen_dDL_Comment_Definition, gen_dDL_Create_sequence_Definition, gen_dDL_Primary_key_Key, gen_dDL_Unique_key_Key, gen_dDL_Foreign_key_Key},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)