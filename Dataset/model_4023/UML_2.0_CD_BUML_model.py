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
uml2CD_NamedElement = Class(name="uml2CD::NamedElement", is_abstract=True)
uml2CD_Constraint = Class(name="uml2CD::Constraint")
uml2CD_Package = Class(name="uml2CD::Package")
NamedElement = Class(name="NamedElement")
uml2CD_Class = Class(name="uml2CD::Class")
uml2CD_Enumeration = Class(name="uml2CD::Enumeration")
uml2CD_Association = Class(name="uml2CD::Association")
uml2CD_Generalization = Class(name="uml2CD::Generalization")
uml2CD_PrimitiveType = Class(name="uml2CD::PrimitiveType")
uml2CD_GeneralizationSet = Class(name="uml2CD::GeneralizationSet")
uml2CD_Parameter = Class(name="uml2CD::Parameter")
uml2CD_Comment = Class(name="uml2CD::Comment")
uml2CD_Operation = Class(name="uml2CD::Operation")
uml2CD_Property = Class(name="uml2CD::Property")
uml2CD_DataType = Class(name="uml2CD::DataType", is_abstract=True)
DataType = Class(name="DataType")
uml2CD_EnumerationLiteral = Class(name="uml2CD::EnumerationLiteral")
uml2CD_UMLModel = Class(name="uml2CD::UMLModel")

# uml2CD_NamedElement class attributes and methods
uml2CD_NamedElement_name: Property = Property(name="name", type=StringType)
uml2CD_NamedElement.attributes={uml2CD_NamedElement_name}

# uml2CD_Constraint class attributes and methods
uml2CD_Constraint_specification: Property = Property(name="specification", type=StringType)
uml2CD_Constraint.attributes={uml2CD_Constraint_specification}

# uml2CD_Package class attributes and methods

# NamedElement class attributes and methods

# uml2CD_Class class attributes and methods
uml2CD_Class_active: Property = Property(name="active", type=StringType)
uml2CD_Class.attributes={uml2CD_Class_active}

# uml2CD_Enumeration class attributes and methods

# uml2CD_Association class attributes and methods
uml2CD_Association_isDerived: Property = Property(name="isDerived", type=StringType)
uml2CD_Association.attributes={uml2CD_Association_isDerived}

# uml2CD_Generalization class attributes and methods
uml2CD_Generalization_isSubstitutable: Property = Property(name="isSubstitutable", type=StringType)
uml2CD_Generalization.attributes={uml2CD_Generalization_isSubstitutable}

# uml2CD_PrimitiveType class attributes and methods

# uml2CD_GeneralizationSet class attributes and methods
uml2CD_GeneralizationSet_isCovering: Property = Property(name="isCovering", type=StringType)
uml2CD_GeneralizationSet_isDisjoint: Property = Property(name="isDisjoint", type=StringType)
uml2CD_GeneralizationSet.attributes={uml2CD_GeneralizationSet_isCovering, uml2CD_GeneralizationSet_isDisjoint}

# uml2CD_Parameter class attributes and methods
uml2CD_Parameter_kind: Property = Property(name="kind", type=StringType)
uml2CD_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
uml2CD_Parameter.attributes={uml2CD_Parameter_kind, uml2CD_Parameter_defaultValue}

# uml2CD_Comment class attributes and methods
uml2CD_Comment_value: Property = Property(name="value", type=StringType)
uml2CD_Comment.attributes={uml2CD_Comment_value}

# uml2CD_Operation class attributes and methods
uml2CD_Operation_isQuery: Property = Property(name="isQuery", type=StringType)
uml2CD_Operation_visibility: Property = Property(name="visibility", type=StringType)
uml2CD_Operation_body: Property = Property(name="body", type=StringType)
uml2CD_Operation.attributes={uml2CD_Operation_isQuery, uml2CD_Operation_body, uml2CD_Operation_visibility}

# uml2CD_Property class attributes and methods
uml2CD_Property_isDerived: Property = Property(name="isDerived", type=StringType)
uml2CD_Property_aggregation: Property = Property(name="aggregation", type=StringType)
uml2CD_Property_lower: Property = Property(name="lower", type=StringType)
uml2CD_Property_upper: Property = Property(name="upper", type=StringType)
uml2CD_Property.attributes={uml2CD_Property_lower, uml2CD_Property_upper, uml2CD_Property_isDerived, uml2CD_Property_aggregation}

# uml2CD_DataType class attributes and methods

# DataType class attributes and methods

# uml2CD_EnumerationLiteral class attributes and methods

# uml2CD_UMLModel class attributes and methods

# Relationships
comments0: BinaryAssociation = BinaryAssociation(
    name="comments0",
    ends={
        Property(name="uml2CD_Comment", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_NamedElement", type=uml2CD_Comment, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraints1: BinaryAssociation = BinaryAssociation(
    name="constraints1",
    ends={
        Property(name="uml2CD_Constraint", type=uml2CD_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_NamedElement2", type=uml2CD_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nestedPackage4: BinaryAssociation = BinaryAssociation(
    name="nestedPackage4",
    ends={
        Property(name="uml2CD_Package", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package3", type=uml2CD_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedClass5: BinaryAssociation = BinaryAssociation(
    name="packagedClass5",
    ends={
        Property(name="uml2CD_Class", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package6", type=uml2CD_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedEnum7: BinaryAssociation = BinaryAssociation(
    name="packagedEnum7",
    ends={
        Property(name="uml2CD_Enumeration", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package8", type=uml2CD_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedAssoc9: BinaryAssociation = BinaryAssociation(
    name="packagedAssoc9",
    ends={
        Property(name="uml2CD_Association", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package10", type=uml2CD_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedGeneralizations11: BinaryAssociation = BinaryAssociation(
    name="packagedGeneralizations11",
    ends={
        Property(name="uml2CD_Generalization", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package12", type=uml2CD_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packagedPrimitive13: BinaryAssociation = BinaryAssociation(
    name="packagedPrimitive13",
    ends={
        Property(name="uml2CD_PrimitiveType", type=uml2CD_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Package14", type=uml2CD_PrimitiveType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
general15: BinaryAssociation = BinaryAssociation(
    name="general15",
    ends={
        Property(name="uml2CD_Class17", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Generalization16", type=uml2CD_Class, multiplicity=Multiplicity(1, 1))
    }
)
specific18: BinaryAssociation = BinaryAssociation(
    name="specific18",
    ends={
        Property(name="uml2CD_Class20", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Generalization19", type=uml2CD_Class, multiplicity=Multiplicity(1, 1))
    }
)
generalizationSet21: BinaryAssociation = BinaryAssociation(
    name="generalizationSet21",
    ends={
        Property(name="uml2CD_GeneralizationSet", type=uml2CD_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Generalization22", type=uml2CD_GeneralizationSet, multiplicity=Multiplicity(0, 9999))
    }
)
enumType23: BinaryAssociation = BinaryAssociation(
    name="enumType23",
    ends={
        Property(name="uml2CD_Enumeration24", type=uml2CD_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Parameter", type=uml2CD_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
redefinedOperation29: BinaryAssociation = BinaryAssociation(
    name="redefinedOperation29",
    ends={
        Property(name="uml2CD_Operation", type=uml2CD_Operation, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Operation28", type=uml2CD_Operation, multiplicity=Multiplicity(0, 9999))
    }
)
ownedOperation30: BinaryAssociation = BinaryAssociation(
    name="ownedOperation30",
    ends={
        Property(name="uml2CD_Operation32", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Class31", type=uml2CD_Operation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedAttribute33: BinaryAssociation = BinaryAssociation(
    name="ownedAttribute33",
    ends={
        Property(name="uml2CD_Property", type=uml2CD_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Class34", type=uml2CD_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
memberEnd35: BinaryAssociation = BinaryAssociation(
    name="memberEnd35",
    ends={
        Property(name="uml2CD_Property37", type=uml2CD_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Association36", type=uml2CD_Property, multiplicity=Multiplicity(1, 9999))
    }
)
ownedEnd38: BinaryAssociation = BinaryAssociation(
    name="ownedEnd38",
    ends={
        Property(name="uml2CD_Property40", type=uml2CD_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Association39", type=uml2CD_Property, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ownedLiteral41: BinaryAssociation = BinaryAssociation(
    name="ownedLiteral41",
    ends={
        Property(name="uml2CD_EnumerationLiteral", type=uml2CD_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Enumeration42", type=uml2CD_EnumerationLiteral, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveType25: BinaryAssociation = BinaryAssociation(
    name="primitiveType25",
    ends={
        Property(name="uml2CD_PrimitiveType27", type=uml2CD_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_Parameter26", type=uml2CD_PrimitiveType, multiplicity=Multiplicity(0, 1))
    }
)
packages43: BinaryAssociation = BinaryAssociation(
    name="packages43",
    ends={
        Property(name="uml2CD_Package44", type=uml2CD_UMLModel, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2CD_UMLModel", type=uml2CD_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_uml2CD_Package_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Package)
gen_uml2CD_Operation_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Operation)
gen_uml2CD_Class_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Class)
gen_uml2CD_DataType_NamedElement = Generalization(general=NamedElement, specific=uml2CD_DataType)
gen_uml2CD_Property_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Property)
gen_uml2CD_Association_NamedElement = Generalization(general=NamedElement, specific=uml2CD_Association)
gen_uml2CD_PrimitiveType_DataType = Generalization(general=DataType, specific=uml2CD_PrimitiveType)
gen_uml2CD_Enumeration_DataType = Generalization(general=DataType, specific=uml2CD_Enumeration)
gen_uml2CD_EnumerationLiteral_NamedElement = Generalization(general=NamedElement, specific=uml2CD_EnumerationLiteral)

# Domain Model
domain_model = DomainModel(
    name="uml2CD",
    types={uml2CD_NamedElement, uml2CD_Constraint, uml2CD_Package, NamedElement, uml2CD_Class, uml2CD_Enumeration, uml2CD_Association, uml2CD_Generalization, uml2CD_PrimitiveType, uml2CD_GeneralizationSet, uml2CD_Parameter, uml2CD_Comment, uml2CD_Operation, uml2CD_Property, uml2CD_DataType, DataType, uml2CD_EnumerationLiteral, uml2CD_UMLModel},
    associations={comments0, constraints1, nestedPackage4, packagedClass5, packagedEnum7, packagedAssoc9, packagedGeneralizations11, packagedPrimitive13, general15, specific18, generalizationSet21, enumType23, redefinedOperation29, ownedOperation30, ownedAttribute33, memberEnd35, ownedEnd38, ownedLiteral41, primitiveType25, packages43},
    generalizations={gen_uml2CD_Package_NamedElement, gen_uml2CD_Operation_NamedElement, gen_uml2CD_Class_NamedElement, gen_uml2CD_DataType_NamedElement, gen_uml2CD_Property_NamedElement, gen_uml2CD_Association_NamedElement, gen_uml2CD_PrimitiveType_DataType, gen_uml2CD_Enumeration_DataType, gen_uml2CD_EnumerationLiteral_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)