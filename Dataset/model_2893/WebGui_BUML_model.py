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
webGui_DomainModel = Class(name="webGui_DomainModel")
webGui_WebModel = Class(name="webGui_WebModel")
webGui_Type = Class(name="webGui_Type")
webGui_Entity = Class(name="webGui_Entity")
Type = Class(name="Type")
webGui_Feature = Class(name="webGui_Feature")
webGui_Expression = Class(name="webGui_Expression")
webGui_DataType = Class(name="webGui_DataType")
webGui_Page = Class(name="webGui_Page")
webGui_Model = Class(name="webGui_Model")
webGui_Value = Class(name="webGui_Value")
Expression = Class(name="Expression")
webGui_NumberLiteral = Class(name="webGui_NumberLiteral")
webGui_Add = Class(name="webGui_Add")
webGui_Subtract = Class(name="webGui_Subtract")
webGui_Multiply = Class(name="webGui_Multiply")
webGui_Divide = Class(name="webGui_Divide")
webGui_PageElement = Class(name="webGui_PageElement")
webGui_ActionElement = Class(name="webGui_ActionElement")
PageElement = Class(name="PageElement")
webGui_DisplayElement = Class(name="webGui_DisplayElement")
webGui_DomainPath = Class(name="webGui_DomainPath")
Value = Class(name="Value")
webGui_DomainPathTail = Class(name="webGui_DomainPathTail")

# webGui_DomainModel class attributes and methods

# webGui_WebModel class attributes and methods

# webGui_Type class attributes and methods
webGui_Type_name: Property = Property(name="name", type=StringType)
webGui_Type.attributes={webGui_Type_name}

# webGui_Entity class attributes and methods

# Type class attributes and methods

# webGui_Feature class attributes and methods
webGui_Feature_name: Property = Property(name="name", type=StringType)
webGui_Feature_multivalued: Property = Property(name="multivalued", type=BooleanType)
webGui_Feature.attributes={webGui_Feature_multivalued, webGui_Feature_name}

# webGui_Expression class attributes and methods

# webGui_DataType class attributes and methods

# webGui_Page class attributes and methods
webGui_Page_name: Property = Property(name="name", type=StringType)
webGui_Page_title: Property = Property(name="title", type=StringType)
webGui_Page.attributes={webGui_Page_name, webGui_Page_title}

# webGui_Model class attributes and methods
webGui_Model_name: Property = Property(name="name", type=StringType)
webGui_Model.attributes={webGui_Model_name}

# webGui_Value class attributes and methods

# Expression class attributes and methods

# webGui_NumberLiteral class attributes and methods
webGui_NumberLiteral_value: Property = Property(name="value", type=IntegerType)
webGui_NumberLiteral.attributes={webGui_NumberLiteral_value}

# webGui_Add class attributes and methods

# webGui_Subtract class attributes and methods

# webGui_Multiply class attributes and methods

# webGui_Divide class attributes and methods

# webGui_PageElement class attributes and methods

# webGui_ActionElement class attributes and methods
webGui_ActionElement_name: Property = Property(name="name", type=StringType)
webGui_ActionElement.attributes={webGui_ActionElement_name}

# PageElement class attributes and methods

# webGui_DisplayElement class attributes and methods

# webGui_DomainPath class attributes and methods

# Value class attributes and methods

# webGui_DomainPathTail class attributes and methods

# Relationships
domain0: BinaryAssociation = BinaryAssociation(
    name="domain0",
    ends={
        Property(name="webGui_DomainModel", type=webGui_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Model", type=webGui_DomainModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
web1: BinaryAssociation = BinaryAssociation(
    name="web1",
    ends={
        Property(name="webGui_WebModel", type=webGui_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Model2", type=webGui_WebModel, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
types3: BinaryAssociation = BinaryAssociation(
    name="types3",
    ends={
        Property(name="webGui_Type", type=webGui_DomainModel, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DomainModel4", type=webGui_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
features5: BinaryAssociation = BinaryAssociation(
    name="features5",
    ends={
        Property(name="webGui_Feature", type=webGui_Entity, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Entity", type=webGui_Feature, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="webGui_Type8", type=webGui_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Feature7", type=webGui_Type, multiplicity=Multiplicity(0, 1))
    }
)
expression9: BinaryAssociation = BinaryAssociation(
    name="expression9",
    ends={
        Property(name="webGui_Expression", type=webGui_Feature, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Feature10", type=webGui_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
pages11: BinaryAssociation = BinaryAssociation(
    name="pages11",
    ends={
        Property(name="webGui_Page", type=webGui_WebModel, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_WebModel12", type=webGui_Page, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
entity13: BinaryAssociation = BinaryAssociation(
    name="entity13",
    ends={
        Property(name="webGui_Entity15", type=webGui_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Page14", type=webGui_Entity, multiplicity=Multiplicity(0, 1))
    }
)
feature24: BinaryAssociation = BinaryAssociation(
    name="feature24",
    ends={
        Property(name="webGui_Feature26", type=webGui_DomainPathTail, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DomainPathTail25", type=webGui_Feature, multiplicity=Multiplicity(0, 1))
    }
)
tail28: BinaryAssociation = BinaryAssociation(
    name="tail28",
    ends={
        Property(name="webGui_DomainPathTail29", type=webGui_DomainPathTail, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DomainPathTail27", type=webGui_DomainPathTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left30: BinaryAssociation = BinaryAssociation(
    name="left30",
    ends={
        Property(name="webGui_Expression31", type=webGui_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Add", type=webGui_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right32: BinaryAssociation = BinaryAssociation(
    name="right32",
    ends={
        Property(name="webGui_Expression34", type=webGui_Add, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Add33", type=webGui_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left35: BinaryAssociation = BinaryAssociation(
    name="left35",
    ends={
        Property(name="webGui_Expression36", type=webGui_Subtract, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Subtract", type=webGui_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right37: BinaryAssociation = BinaryAssociation(
    name="right37",
    ends={
        Property(name="webGui_Expression39", type=webGui_Subtract, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Subtract38", type=webGui_Expression, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left40: BinaryAssociation = BinaryAssociation(
    name="left40",
    ends={
        Property(name="webGui_Value", type=webGui_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Multiply", type=webGui_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right41: BinaryAssociation = BinaryAssociation(
    name="right41",
    ends={
        Property(name="webGui_Value43", type=webGui_Multiply, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Multiply42", type=webGui_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
left44: BinaryAssociation = BinaryAssociation(
    name="left44",
    ends={
        Property(name="webGui_Value45", type=webGui_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Divide", type=webGui_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right46: BinaryAssociation = BinaryAssociation(
    name="right46",
    ends={
        Property(name="webGui_Value48", type=webGui_Divide, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Divide47", type=webGui_Value, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
contents16: BinaryAssociation = BinaryAssociation(
    name="contents16",
    ends={
        Property(name="webGui_PageElement", type=webGui_Page, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_Page17", type=webGui_PageElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
reference18: BinaryAssociation = BinaryAssociation(
    name="reference18",
    ends={
        Property(name="webGui_DomainPath", type=webGui_DisplayElement, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DisplayElement", type=webGui_DomainPath, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
feature19: BinaryAssociation = BinaryAssociation(
    name="feature19",
    ends={
        Property(name="webGui_Feature21", type=webGui_DomainPath, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DomainPath20", type=webGui_Feature, multiplicity=Multiplicity(0, 1))
    }
)
tail22: BinaryAssociation = BinaryAssociation(
    name="tail22",
    ends={
        Property(name="webGui_DomainPathTail", type=webGui_DomainPath, multiplicity=Multiplicity(1, 1)),
        Property(name="webGui_DomainPath23", type=webGui_DomainPathTail, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_webGui_Entity_Type = Generalization(general=Type, specific=webGui_Entity)
gen_webGui_DataType_Type = Generalization(general=Type, specific=webGui_DataType)
gen_webGui_Value_Expression = Generalization(general=Expression, specific=webGui_Value)
gen_webGui_NumberLiteral_Value = Generalization(general=Value, specific=webGui_NumberLiteral)
gen_webGui_Add_Expression = Generalization(general=Expression, specific=webGui_Add)
gen_webGui_Subtract_Expression = Generalization(general=Expression, specific=webGui_Subtract)
gen_webGui_Multiply_Expression = Generalization(general=Expression, specific=webGui_Multiply)
gen_webGui_Divide_Expression = Generalization(general=Expression, specific=webGui_Divide)
gen_webGui_ActionElement_PageElement = Generalization(general=PageElement, specific=webGui_ActionElement)
gen_webGui_DisplayElement_PageElement = Generalization(general=PageElement, specific=webGui_DisplayElement)
gen_webGui_DomainPath_Value = Generalization(general=Value, specific=webGui_DomainPath)

# Domain Model
domain_model = DomainModel(
    name="webGui",
    types={webGui_DomainModel, webGui_WebModel, webGui_Type, webGui_Entity, Type, webGui_Feature, webGui_Expression, webGui_DataType, webGui_Page, webGui_Model, webGui_Value, Expression, webGui_NumberLiteral, webGui_Add, webGui_Subtract, webGui_Multiply, webGui_Divide, webGui_PageElement, webGui_ActionElement, PageElement, webGui_DisplayElement, webGui_DomainPath, Value, webGui_DomainPathTail},
    associations={domain0, web1, types3, features5, type6, expression9, pages11, entity13, feature24, tail28, left30, right32, left35, right37, left40, right41, left44, right46, contents16, reference18, feature19, tail22},
    generalizations={gen_webGui_Entity_Type, gen_webGui_DataType_Type, gen_webGui_Value_Expression, gen_webGui_NumberLiteral_Value, gen_webGui_Add_Expression, gen_webGui_Subtract_Expression, gen_webGui_Multiply_Expression, gen_webGui_Divide_Expression, gen_webGui_ActionElement_PageElement, gen_webGui_DisplayElement_PageElement, gen_webGui_DomainPath_Value},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)