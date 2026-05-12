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
            EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="STRING"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="REGEXPR"),
			EnumerationLiteral(name="JAVASCRIPT"),
			EnumerationLiteral(name="TIMESTAMP")
    }
)

# Classes
mongodb_Field = Class(name="mongodb_Field")
mongodb_Database = Class(name="mongodb_Database")
mongodb_Collection = Class(name="mongodb_Collection")
mongodb_Document = Class(name="mongodb_Document")
mongodb_IValue = Class(name="mongodb_IValue", is_abstract=True)
mongodb_Value = Class(name="mongodb_Value")
IValue = Class(name="IValue")
mongodb_ValueList = Class(name="mongodb_ValueList")
mongodb_SubDocument = Class(name="mongodb_SubDocument")

# mongodb_Field class attributes and methods
mongodb_Field_key: Property = Property(name="key", type=StringType)
mongodb_Field.attributes={mongodb_Field_key}

# mongodb_Database class attributes and methods
mongodb_Database_name: Property = Property(name="name", type=StringType)
mongodb_Database.attributes={mongodb_Database_name}

# mongodb_Collection class attributes and methods
mongodb_Collection_name: Property = Property(name="name", type=StringType)
mongodb_Collection.attributes={mongodb_Collection_name}

# mongodb_Document class attributes and methods
mongodb_Document__id: Property = Property(name="_id", type=StringType)
mongodb_Document.attributes={mongodb_Document__id}

# mongodb_IValue class attributes and methods
mongodb_IValue_m_getValue: Method = Method(name="getValue", parameters={}, type=StringType)
mongodb_IValue_m_getValueList: Method = Method(name="getValueList", parameters={}, type=StringType)
mongodb_IValue_m_getSubDocument: Method = Method(name="getSubDocument", parameters={})
mongodb_IValue.methods={mongodb_IValue_m_getValueList, mongodb_IValue_m_getSubDocument, mongodb_IValue_m_getValue}

# mongodb_Value class attributes and methods
mongodb_Value_value: Property = Property(name="value", type=StringType)
mongodb_Value_type: Property = Property(name="type", type=StringType)
mongodb_Value.attributes={mongodb_Value_type, mongodb_Value_value}

# IValue class attributes and methods

# mongodb_ValueList class attributes and methods

# mongodb_SubDocument class attributes and methods

# Relationships
fields3: BinaryAssociation = BinaryAssociation(
    name="fields3",
    ends={
        Property(name="mongodb_Field", type=mongodb_Document, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_Document4", type=mongodb_Field, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
collections0: BinaryAssociation = BinaryAssociation(
    name="collections0",
    ends={
        Property(name="mongodb_Collection", type=mongodb_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_Database", type=mongodb_Collection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
documents1: BinaryAssociation = BinaryAssociation(
    name="documents1",
    ends={
        Property(name="mongodb_Document", type=mongodb_Collection, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_Collection2", type=mongodb_Document, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value5: BinaryAssociation = BinaryAssociation(
    name="value5",
    ends={
        Property(name="mongodb_IValue", type=mongodb_Field, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_Field6", type=mongodb_IValue, multiplicity=Multiplicity(1, 1))
    }
)
values7: BinaryAssociation = BinaryAssociation(
    name="values7",
    ends={
        Property(name="mongodb_IValue8", type=mongodb_ValueList, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_ValueList", type=mongodb_IValue, multiplicity=Multiplicity(1, 9999))
    }
)
fields9: BinaryAssociation = BinaryAssociation(
    name="fields9",
    ends={
        Property(name="mongodb_Field10", type=mongodb_SubDocument, multiplicity=Multiplicity(1, 1)),
        Property(name="mongodb_SubDocument", type=mongodb_Field, multiplicity=Multiplicity(1, 9999))
    }
)

# Generalizations
gen_mongodb_Value_IValue = Generalization(general=IValue, specific=mongodb_Value)
gen_mongodb_ValueList_IValue = Generalization(general=IValue, specific=mongodb_ValueList)
gen_mongodb_SubDocument_IValue = Generalization(general=IValue, specific=mongodb_SubDocument)

# Domain Model
domain_model = DomainModel(
    name="mongodb",
    types={mongodb_Field, mongodb_Database, mongodb_Collection, mongodb_Document, mongodb_IValue, mongodb_Value, IValue, mongodb_ValueList, mongodb_SubDocument, Type},
    associations={fields3, collections0, documents1, value5, values7, fields9},
    generalizations={gen_mongodb_Value_IValue, gen_mongodb_ValueList_IValue, gen_mongodb_SubDocument_IValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)