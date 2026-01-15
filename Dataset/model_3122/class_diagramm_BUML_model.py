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
ModifierType: Enumeration = Enumeration(
    name="ModifierType",
    literals={
            EnumerationLiteral(name="abstract"),
			EnumerationLiteral(name="final"),
			EnumerationLiteral(name="static"),
			EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

# Classes
class_diagramm_RefClass = Class(name="class::diagramm::RefClass", is_abstract=True)
class_diagramm_DataType = Class(name="class::diagramm::DataType")
RefDataType = Class(name="RefDataType")
class_diagramm_Method = Class(name="class::diagramm::Method")
RefMethod = Class(name="RefMethod")
class_diagramm_Package = Class(name="class::diagramm::Package")
RefPackage = Class(name="RefPackage")
class_diagramm_RefAssociation = Class(name="class::diagramm::RefAssociation", is_abstract=True)
class_diagramm_RefDataType = Class(name="class::diagramm::RefDataType", is_abstract=True)
class_diagramm_Attribute = Class(name="class::diagramm::Attribute")
RefAttribute = Class(name="RefAttribute")
class_diagramm_RefParameter = Class(name="class::diagramm::RefParameter", is_abstract=True)
class_diagramm_Class = Class(name="class::diagramm::Class")
RefClass = Class(name="RefClass")
class_diagramm_RefAttribute = Class(name="class::diagramm::RefAttribute", is_abstract=True)
class_diagramm_Parameter = Class(name="class::diagramm::Parameter")
RefParameter = Class(name="RefParameter")
class_diagramm_Association = Class(name="class::diagramm::Association")
RefAssociation = Class(name="RefAssociation")
class_diagramm_RefMethod = Class(name="class::diagramm::RefMethod", is_abstract=True)
class_diagramm_RefPackage = Class(name="class::diagramm::RefPackage", is_abstract=True)

# class_diagramm_RefClass class attributes and methods

# class_diagramm_DataType class attributes and methods
class_diagramm_DataType_name: Property = Property(name="name", type=StringType)
class_diagramm_DataType.attributes={class_diagramm_DataType_name}

# RefDataType class attributes and methods

# class_diagramm_Method class attributes and methods
class_diagramm_Method_name: Property = Property(name="name", type=StringType)
class_diagramm_Method_modifier: Property = Property(name="modifier", type=StringType)
class_diagramm_Method.attributes={class_diagramm_Method_modifier, class_diagramm_Method_name}

# RefMethod class attributes and methods

# class_diagramm_Package class attributes and methods
class_diagramm_Package_name: Property = Property(name="name", type=StringType)
class_diagramm_Package.attributes={class_diagramm_Package_name}

# RefPackage class attributes and methods

# class_diagramm_RefAssociation class attributes and methods

# class_diagramm_RefDataType class attributes and methods

# class_diagramm_Attribute class attributes and methods
class_diagramm_Attribute_name: Property = Property(name="name", type=StringType)
class_diagramm_Attribute_modifier: Property = Property(name="modifier", type=StringType)
class_diagramm_Attribute.attributes={class_diagramm_Attribute_name, class_diagramm_Attribute_modifier}

# RefAttribute class attributes and methods

# class_diagramm_RefParameter class attributes and methods

# class_diagramm_Class class attributes and methods
class_diagramm_Class_modifier: Property = Property(name="modifier", type=StringType)
class_diagramm_Class_name: Property = Property(name="name", type=StringType)
class_diagramm_Class.attributes={class_diagramm_Class_modifier, class_diagramm_Class_name}

# RefClass class attributes and methods

# class_diagramm_RefAttribute class attributes and methods

# class_diagramm_Parameter class attributes and methods
class_diagramm_Parameter_name: Property = Property(name="name", type=StringType)
class_diagramm_Parameter.attributes={class_diagramm_Parameter_name}

# RefParameter class attributes and methods

# class_diagramm_Association class attributes and methods
class_diagramm_Association_minCardinality: Property = Property(name="minCardinality", type=IntegerType)
class_diagramm_Association_maxCardinality: Property = Property(name="maxCardinality", type=IntegerType)
class_diagramm_Association_name: Property = Property(name="name", type=StringType)
class_diagramm_Association_isAggregation: Property = Property(name="isAggregation", type=BooleanType)
class_diagramm_Association.attributes={class_diagramm_Association_minCardinality, class_diagramm_Association_name, class_diagramm_Association_maxCardinality, class_diagramm_Association_isAggregation}

# RefAssociation class attributes and methods

# class_diagramm_RefMethod class attributes and methods

# class_diagramm_RefPackage class attributes and methods

# Relationships
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="class_diagramm_RefClass", type=class_diagramm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Package2", type=class_diagramm_RefClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations0: BinaryAssociation = BinaryAssociation(
    name="associations0",
    ends={
        Property(name="class_diagramm_RefAssociation", type=class_diagramm_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Package", type=class_diagramm_RefAssociation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitive_return7: BinaryAssociation = BinaryAssociation(
    name="primitive_return7",
    ends={
        Property(name="class_diagramm_RefDataType", type=class_diagramm_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Method8", type=class_diagramm_RefDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type9: BinaryAssociation = BinaryAssociation(
    name="type9",
    ends={
        Property(name="class_diagramm_RefClass10", type=class_diagramm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Attribute", type=class_diagramm_RefClass, multiplicity=Multiplicity(0, 1))
    }
)
return3: BinaryAssociation = BinaryAssociation(
    name="return3",
    ends={
        Property(name="class_diagramm_RefClass4", type=class_diagramm_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Method", type=class_diagramm_RefClass, multiplicity=Multiplicity(0, 1))
    }
)
parameters5: BinaryAssociation = BinaryAssociation(
    name="parameters5",
    ends={
        Property(name="class_diagramm_RefParameter", type=class_diagramm_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Method6", type=class_diagramm_RefParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="class_diagramm_RefClass15", type=class_diagramm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Parameter", type=class_diagramm_RefClass, multiplicity=Multiplicity(0, 1))
    }
)
primitive_type16: BinaryAssociation = BinaryAssociation(
    name="primitive_type16",
    ends={
        Property(name="class_diagramm_RefDataType18", type=class_diagramm_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Parameter17", type=class_diagramm_RefDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parent19: BinaryAssociation = BinaryAssociation(
    name="parent19",
    ends={
        Property(name="class_diagramm_RefClass20", type=class_diagramm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Class", type=class_diagramm_RefClass, multiplicity=Multiplicity(0, 1))
    }
)
attributes21: BinaryAssociation = BinaryAssociation(
    name="attributes21",
    ends={
        Property(name="class_diagramm_RefAttribute", type=class_diagramm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Class22", type=class_diagramm_RefAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitive_type11: BinaryAssociation = BinaryAssociation(
    name="primitive_type11",
    ends={
        Property(name="class_diagramm_RefDataType13", type=class_diagramm_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Attribute12", type=class_diagramm_RefDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="class_diagramm_RefClass26", type=class_diagramm_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Association", type=class_diagramm_RefClass, multiplicity=Multiplicity(1, 1))
    }
)
target27: BinaryAssociation = BinaryAssociation(
    name="target27",
    ends={
        Property(name="class_diagramm_RefClass29", type=class_diagramm_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Association28", type=class_diagramm_RefClass, multiplicity=Multiplicity(1, 1))
    }
)
methods23: BinaryAssociation = BinaryAssociation(
    name="methods23",
    ends={
        Property(name="class_diagramm_RefMethod", type=class_diagramm_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="class_diagramm_Class24", type=class_diagramm_RefMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_class_diagramm_DataType_RefDataType = Generalization(general=RefDataType, specific=class_diagramm_DataType)
gen_class_diagramm_Method_RefMethod = Generalization(general=RefMethod, specific=class_diagramm_Method)
gen_class_diagramm_Package_RefPackage = Generalization(general=RefPackage, specific=class_diagramm_Package)
gen_class_diagramm_Attribute_RefAttribute = Generalization(general=RefAttribute, specific=class_diagramm_Attribute)
gen_class_diagramm_Class_RefClass = Generalization(general=RefClass, specific=class_diagramm_Class)
gen_class_diagramm_Parameter_RefParameter = Generalization(general=RefParameter, specific=class_diagramm_Parameter)
gen_class_diagramm_Association_RefAssociation = Generalization(general=RefAssociation, specific=class_diagramm_Association)

# Domain Model
domain_model = DomainModel(
    name="class_diagramm",
    types={class_diagramm_RefClass, class_diagramm_DataType, RefDataType, class_diagramm_Method, RefMethod, class_diagramm_Package, RefPackage, class_diagramm_RefAssociation, class_diagramm_RefDataType, class_diagramm_Attribute, RefAttribute, class_diagramm_RefParameter, class_diagramm_Class, RefClass, class_diagramm_RefAttribute, class_diagramm_Parameter, RefParameter, class_diagramm_Association, RefAssociation, class_diagramm_RefMethod, class_diagramm_RefPackage, ModifierType},
    associations={classes1, associations0, primitive_return7, type9, return3, parameters5, type14, primitive_type16, parent19, attributes21, primitive_type11, source25, target27, methods23},
    generalizations={gen_class_diagramm_DataType_RefDataType, gen_class_diagramm_Method_RefMethod, gen_class_diagramm_Package_RefPackage, gen_class_diagramm_Attribute_RefAttribute, gen_class_diagramm_Class_RefClass, gen_class_diagramm_Parameter_RefParameter, gen_class_diagramm_Association_RefAssociation},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)