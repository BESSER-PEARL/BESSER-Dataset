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
sqlview_Model = Class(name="sqlview_Model")
sqlview_Metamodel = Class(name="sqlview_Metamodel")
sqlview_Expression = Class(name="sqlview_Expression")
sqlview_SelectAttribute = Class(name="sqlview_SelectAttribute")
sqlview_MetamodelName = Class(name="sqlview_MetamodelName")
sqlview_Select = Class(name="sqlview_Select")
sqlview_From = Class(name="sqlview_From")
sqlview_Condition = Class(name="sqlview_Condition")
sqlview_JoinLeft = Class(name="sqlview_JoinLeft")
sqlview_JoinRight = Class(name="sqlview_JoinRight")
sqlview_Relation = Class(name="sqlview_Relation")
sqlview_Class = Class(name="sqlview_Class")
sqlview_Attribute = Class(name="sqlview_Attribute")
sqlview_Join = Class(name="sqlview_Join")
sqlview_EObject = Class(name="sqlview_EObject")
sqlview_EclExpression = Class(name="sqlview_EclExpression")
sqlview_Comparison = Class(name="sqlview_Comparison")
sqlview_Left = Class(name="sqlview_Left")
sqlview_Right = Class(name="sqlview_Right")

# sqlview_Model class attributes and methods
sqlview_Model_viewName: Property = Property(name="viewName", type=StringType)
sqlview_Model.attributes={sqlview_Model_viewName}

# sqlview_Metamodel class attributes and methods
sqlview_Metamodel_metamodelURL: Property = Property(name="metamodelURL", type=StringType)
sqlview_Metamodel.attributes={sqlview_Metamodel_metamodelURL}

# sqlview_Expression class attributes and methods

# sqlview_SelectAttribute class attributes and methods

# sqlview_MetamodelName class attributes and methods
sqlview_MetamodelName_name: Property = Property(name="name", type=StringType)
sqlview_MetamodelName.attributes={sqlview_MetamodelName_name}

# sqlview_Select class attributes and methods
sqlview_Select_select: Property = Property(name="select", type=StringType)
sqlview_Select.attributes={sqlview_Select_select}

# sqlview_From class attributes and methods

# sqlview_Condition class attributes and methods

# sqlview_JoinLeft class attributes and methods

# sqlview_JoinRight class attributes and methods

# sqlview_Relation class attributes and methods
sqlview_Relation_name: Property = Property(name="name", type=StringType)
sqlview_Relation.attributes={sqlview_Relation_name}

# sqlview_Class class attributes and methods
sqlview_Class_name: Property = Property(name="name", type=StringType)
sqlview_Class.attributes={sqlview_Class_name}

# sqlview_Attribute class attributes and methods
sqlview_Attribute_name: Property = Property(name="name", type=StringType)
sqlview_Attribute.attributes={sqlview_Attribute_name}

# sqlview_Join class attributes and methods

# sqlview_EObject class attributes and methods

# sqlview_EclExpression class attributes and methods
sqlview_EclExpression_value: Property = Property(name="value", type=StringType)
sqlview_EclExpression.attributes={sqlview_EclExpression_value}

# sqlview_Comparison class attributes and methods

# sqlview_Left class attributes and methods

# sqlview_Right class attributes and methods
sqlview_Right_value: Property = Property(name="value", type=StringType)
sqlview_Right.attributes={sqlview_Right_value}

# Relationships
metamodel0: BinaryAssociation = BinaryAssociation(
    name="metamodel0",
    ends={
        Property(name="sqlview_Metamodel", type=sqlview_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Model", type=sqlview_Metamodel, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
selectAttribute11: BinaryAssociation = BinaryAssociation(
    name="selectAttribute11",
    ends={
        Property(name="sqlview_SelectAttribute", type=sqlview_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Select12", type=sqlview_SelectAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodelName3: BinaryAssociation = BinaryAssociation(
    name="metamodelName3",
    ends={
        Property(name="sqlview_MetamodelName", type=sqlview_Metamodel, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Metamodel4", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel13: BinaryAssociation = BinaryAssociation(
    name="metamodel13",
    ends={
        Property(name="sqlview_MetamodelName15", type=sqlview_SelectAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_SelectAttribute14", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999))
    }
)
select5: BinaryAssociation = BinaryAssociation(
    name="select5",
    ends={
        Property(name="sqlview_Select", type=sqlview_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Expression6", type=sqlview_Select, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
from_7: BinaryAssociation = BinaryAssociation(
    name="from_7",
    ends={
        Property(name="sqlview_From", type=sqlview_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Expression8", type=sqlview_From, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
condition9: BinaryAssociation = BinaryAssociation(
    name="condition9",
    ends={
        Property(name="sqlview_Condition", type=sqlview_Expression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Expression10", type=sqlview_Condition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression1: BinaryAssociation = BinaryAssociation(
    name="expression1",
    ends={
        Property(name="sqlview_Expression", type=sqlview_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Model2", type=sqlview_Expression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinLeft22: BinaryAssociation = BinaryAssociation(
    name="joinLeft22",
    ends={
        Property(name="sqlview_JoinLeft", type=sqlview_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Join23", type=sqlview_JoinLeft, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
joinRight24: BinaryAssociation = BinaryAssociation(
    name="joinRight24",
    ends={
        Property(name="sqlview_JoinRight", type=sqlview_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Join25", type=sqlview_JoinRight, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relation26: BinaryAssociation = BinaryAssociation(
    name="relation26",
    ends={
        Property(name="sqlview_Relation", type=sqlview_Join, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Join27", type=sqlview_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_16: BinaryAssociation = BinaryAssociation(
    name="class_16",
    ends={
        Property(name="sqlview_Class", type=sqlview_SelectAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_SelectAttribute17", type=sqlview_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute18: BinaryAssociation = BinaryAssociation(
    name="attribute18",
    ends={
        Property(name="sqlview_Attribute", type=sqlview_SelectAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_SelectAttribute19", type=sqlview_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
join20: BinaryAssociation = BinaryAssociation(
    name="join20",
    ends={
        Property(name="sqlview_Join", type=sqlview_From, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_From21", type=sqlview_Join, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodelLeft28: BinaryAssociation = BinaryAssociation(
    name="metamodelLeft28",
    ends={
        Property(name="sqlview_MetamodelName30", type=sqlview_JoinLeft, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_JoinLeft29", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999))
    }
)
classLeft31: BinaryAssociation = BinaryAssociation(
    name="classLeft31",
    ends={
        Property(name="sqlview_Class33", type=sqlview_JoinLeft, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_JoinLeft32", type=sqlview_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodelRight34: BinaryAssociation = BinaryAssociation(
    name="metamodelRight34",
    ends={
        Property(name="sqlview_MetamodelName36", type=sqlview_JoinRight, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_JoinRight35", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999))
    }
)
classRight37: BinaryAssociation = BinaryAssociation(
    name="classRight37",
    ends={
        Property(name="sqlview_Class39", type=sqlview_JoinRight, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_JoinRight38", type=sqlview_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
class_48: BinaryAssociation = BinaryAssociation(
    name="class_48",
    ends={
        Property(name="sqlview_Class50", type=sqlview_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Left49", type=sqlview_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributeWhereLeft51: BinaryAssociation = BinaryAssociation(
    name="attributeWhereLeft51",
    ends={
        Property(name="sqlview_Attribute53", type=sqlview_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Left52", type=sqlview_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
metamodel54: BinaryAssociation = BinaryAssociation(
    name="metamodel54",
    ends={
        Property(name="sqlview_MetamodelName56", type=sqlview_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Right55", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999))
    }
)
value40: BinaryAssociation = BinaryAssociation(
    name="value40",
    ends={
        Property(name="sqlview_EObject", type=sqlview_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Condition41", type=sqlview_EObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
left42: BinaryAssociation = BinaryAssociation(
    name="left42",
    ends={
        Property(name="sqlview_Left", type=sqlview_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Comparison", type=sqlview_Left, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
right43: BinaryAssociation = BinaryAssociation(
    name="right43",
    ends={
        Property(name="sqlview_Right", type=sqlview_Comparison, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Comparison44", type=sqlview_Right, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
metamodel45: BinaryAssociation = BinaryAssociation(
    name="metamodel45",
    ends={
        Property(name="sqlview_MetamodelName47", type=sqlview_Left, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Left46", type=sqlview_MetamodelName, multiplicity=Multiplicity(0, 9999))
    }
)
class_57: BinaryAssociation = BinaryAssociation(
    name="class_57",
    ends={
        Property(name="sqlview_Class59", type=sqlview_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Right58", type=sqlview_Class, multiplicity=Multiplicity(0, 9999))
    }
)
attributeWhereRight60: BinaryAssociation = BinaryAssociation(
    name="attributeWhereRight60",
    ends={
        Property(name="sqlview_Attribute62", type=sqlview_Right, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlview_Right61", type=sqlview_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="sqlview",
    types={sqlview_Model, sqlview_Metamodel, sqlview_Expression, sqlview_SelectAttribute, sqlview_MetamodelName, sqlview_Select, sqlview_From, sqlview_Condition, sqlview_JoinLeft, sqlview_JoinRight, sqlview_Relation, sqlview_Class, sqlview_Attribute, sqlview_Join, sqlview_EObject, sqlview_EclExpression, sqlview_Comparison, sqlview_Left, sqlview_Right},
    associations={metamodel0, selectAttribute11, metamodelName3, metamodel13, select5, from_7, condition9, expression1, joinLeft22, joinRight24, relation26, class_16, attribute18, join20, metamodelLeft28, classLeft31, metamodelRight34, classRight37, class_48, attributeWhereLeft51, metamodel54, value40, left42, right43, metamodel45, class_57, attributeWhereRight60},
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