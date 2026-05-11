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
LiteralType: Enumeration = Enumeration(
    name="LiteralType",
    literals={
            EnumerationLiteral(name="BOOL"),
			EnumerationLiteral(name="INT"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="CHAR")
    }
)

# Classes
base_Annotation = Class(name="base_Annotation")
base_AnnotationType = Class(name="base_AnnotationType")
base_KeyValue = Class(name="base_KeyValue")
base_SimpleAnnotationAttribute = Class(name="base_SimpleAnnotationAttribute")
AnnotationAttribute = Class(name="AnnotationAttribute")
base_EnumAnnotationAttribute = Class(name="base_EnumAnnotationAttribute")
base_Import = Class(name="base_Import")
base_Literal = Class(name="base_Literal")
base_Documentation = Class(name="base_Documentation")
base_AnnotationAttribute = Class(name="base_AnnotationAttribute")
base_NumberLiteral = Class(name="base_NumberLiteral")
base_RealLiteral = Class(name="base_RealLiteral")
NumberLiteral = Class(name="NumberLiteral")
base_IntLiteral = Class(name="base_IntLiteral")
base_StringLiteral = Class(name="base_StringLiteral")
base_LiteralArray = Class(name="base_LiteralArray")
base_BooleanLiteral = Class(name="base_BooleanLiteral")
Literal = Class(name="Literal")

# base_Annotation class attributes and methods

# base_AnnotationType class attributes and methods
base_AnnotationType_name: Property = Property(name="name", type=StringType)
base_AnnotationType_targets: Property = Property(name="targets", type=StringType)
base_AnnotationType.attributes={base_AnnotationType_name, base_AnnotationType_targets}

# base_KeyValue class attributes and methods
base_KeyValue_key: Property = Property(name="key", type=StringType)
base_KeyValue.attributes={base_KeyValue_key}

# base_SimpleAnnotationAttribute class attributes and methods
base_SimpleAnnotationAttribute_type: Property = Property(name="type", type=StringType)
base_SimpleAnnotationAttribute.attributes={base_SimpleAnnotationAttribute_type}

# AnnotationAttribute class attributes and methods

# base_EnumAnnotationAttribute class attributes and methods
base_EnumAnnotationAttribute_values: Property = Property(name="values", type=StringType)
base_EnumAnnotationAttribute.attributes={base_EnumAnnotationAttribute_values}

# base_Import class attributes and methods
base_Import_importedNamespace: Property = Property(name="importedNamespace", type=StringType)
base_Import_importURI: Property = Property(name="importURI", type=StringType)
base_Import.attributes={base_Import_importedNamespace, base_Import_importURI}

# base_Literal class attributes and methods

# base_Documentation class attributes and methods
base_Documentation_lines: Property = Property(name="lines", type=StringType)
base_Documentation.attributes={base_Documentation_lines}

# base_AnnotationAttribute class attributes and methods
base_AnnotationAttribute_optional: Property = Property(name="optional", type=BooleanType)
base_AnnotationAttribute_name: Property = Property(name="name", type=StringType)
base_AnnotationAttribute.attributes={base_AnnotationAttribute_name, base_AnnotationAttribute_optional}

# base_NumberLiteral class attributes and methods

# base_RealLiteral class attributes and methods
base_RealLiteral_value: Property = Property(name="value", type=FloatType)
base_RealLiteral.attributes={base_RealLiteral_value}

# NumberLiteral class attributes and methods

# base_IntLiteral class attributes and methods
base_IntLiteral_value: Property = Property(name="value", type=StringType)
base_IntLiteral.attributes={base_IntLiteral_value}

# base_StringLiteral class attributes and methods
base_StringLiteral_value: Property = Property(name="value", type=StringType)
base_StringLiteral.attributes={base_StringLiteral_value}

# base_LiteralArray class attributes and methods

# base_BooleanLiteral class attributes and methods
base_BooleanLiteral_isTrue: Property = Property(name="isTrue", type=BooleanType)
base_BooleanLiteral.attributes={base_BooleanLiteral_isTrue}

# Literal class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="base_AnnotationType", type=base_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="base_Annotation", type=base_AnnotationType, multiplicity=Multiplicity(0, 1))
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="base_KeyValue", type=base_Annotation, multiplicity=Multiplicity(1, 1)),
        Property(name="base_Annotation2", type=base_KeyValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value3: BinaryAssociation = BinaryAssociation(
    name="value3",
    ends={
        Property(name="base_Literal", type=base_KeyValue, multiplicity=Multiplicity(1, 1)),
        Property(name="base_KeyValue4", type=base_Literal, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
docu5: BinaryAssociation = BinaryAssociation(
    name="docu5",
    ends={
        Property(name="base_Documentation", type=base_AnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="base_AnnotationType6", type=base_Documentation, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes7: BinaryAssociation = BinaryAssociation(
    name="attributes7",
    ends={
        Property(name="base_AnnotationAttribute", type=base_AnnotationType, multiplicity=Multiplicity(1, 1)),
        Property(name="base_AnnotationType8", type=base_AnnotationAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literals9: BinaryAssociation = BinaryAssociation(
    name="literals9",
    ends={
        Property(name="base_Literal10", type=base_LiteralArray, multiplicity=Multiplicity(1, 1)),
        Property(name="base_LiteralArray", type=base_Literal, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_base_SimpleAnnotationAttribute_AnnotationAttribute = Generalization(general=AnnotationAttribute, specific=base_SimpleAnnotationAttribute)
gen_base_EnumAnnotationAttribute_AnnotationAttribute = Generalization(general=AnnotationAttribute, specific=base_EnumAnnotationAttribute)
gen_base_NumberLiteral_Literal = Generalization(general=Literal, specific=base_NumberLiteral)
gen_base_RealLiteral_NumberLiteral = Generalization(general=NumberLiteral, specific=base_RealLiteral)
gen_base_IntLiteral_NumberLiteral = Generalization(general=NumberLiteral, specific=base_IntLiteral)
gen_base_StringLiteral_Literal = Generalization(general=Literal, specific=base_StringLiteral)
gen_base_BooleanLiteral_Literal = Generalization(general=Literal, specific=base_BooleanLiteral)

# Domain Model
domain_model = DomainModel(
    name="base",
    types={base_Annotation, base_AnnotationType, base_KeyValue, base_SimpleAnnotationAttribute, AnnotationAttribute, base_EnumAnnotationAttribute, base_Import, base_Literal, base_Documentation, base_AnnotationAttribute, base_NumberLiteral, base_RealLiteral, NumberLiteral, base_IntLiteral, base_StringLiteral, base_LiteralArray, base_BooleanLiteral, Literal, LiteralType},
    associations={type0, attributes1, value3, docu5, attributes7, literals9},
    generalizations={gen_base_SimpleAnnotationAttribute_AnnotationAttribute, gen_base_EnumAnnotationAttribute_AnnotationAttribute, gen_base_NumberLiteral_Literal, gen_base_RealLiteral_NumberLiteral, gen_base_IntLiteral_NumberLiteral, gen_base_StringLiteral_Literal, gen_base_BooleanLiteral_Literal},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)