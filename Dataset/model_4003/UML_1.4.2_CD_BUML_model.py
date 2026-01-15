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
UML_14_Parameter = Class(name="UML::14::Parameter", is_abstract=True)
NamedElement = Class(name="NamedElement")
UML_14_DataType = Class(name="UML::14::DataType")
UML_14_Constraint = Class(name="UML::14::Constraint", is_abstract=True)
UML_14_MultiplicityRange = Class(name="UML::14::MultiplicityRange")
UML_14_Method = Class(name="UML::14::Method")
UML_14_Association = Class(name="UML::14::Association")
UML_14_AssociationEnd = Class(name="UML::14::AssociationEnd")
UML_14_Primitive = Class(name="UML::14::Primitive")
DataType = Class(name="DataType")
UML_14_Attribute = Class(name="UML::14::Attribute")
UML_14_Generalization = Class(name="UML::14::Generalization")
UML_14_Class = Class(name="UML::14::Class")
UML_14_NamedElement = Class(name="UML::14::NamedElement", is_abstract=True)
UML_14_Enumeration = Class(name="UML::14::Enumeration")
UML_14_EnumerationLiteral = Class(name="UML::14::EnumerationLiteral")
UML_14_Comment = Class(name="UML::14::Comment")
UML_14_Model = Class(name="UML::14::Model")
UML_14_Package = Class(name="UML::14::Package")

# UML_14_Parameter class attributes and methods
UML_14_Parameter_kind: Property = Property(name="kind", type=StringType)
UML_14_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
UML_14_Parameter.attributes={UML_14_Parameter_kind, UML_14_Parameter_defaultValue}

# NamedElement class attributes and methods

# UML_14_DataType class attributes and methods

# UML_14_Constraint class attributes and methods
UML_14_Constraint_body: Property = Property(name="body", type=StringType)
UML_14_Constraint.attributes={UML_14_Constraint_body}

# UML_14_MultiplicityRange class attributes and methods
UML_14_MultiplicityRange_lower: Property = Property(name="lower", type=StringType)
UML_14_MultiplicityRange_upper: Property = Property(name="upper", type=StringType)
UML_14_MultiplicityRange.attributes={UML_14_MultiplicityRange_lower, UML_14_MultiplicityRange_upper}

# UML_14_Method class attributes and methods
UML_14_Method_body: Property = Property(name="body", type=StringType)
UML_14_Method_visibility: Property = Property(name="visibility", type=StringType)
UML_14_Method.attributes={UML_14_Method_body, UML_14_Method_visibility}

# UML_14_Association class attributes and methods

# UML_14_AssociationEnd class attributes and methods
UML_14_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=StringType)
UML_14_AssociationEnd_visibility: Property = Property(name="visibility", type=StringType)
UML_14_AssociationEnd.attributes={UML_14_AssociationEnd_visibility, UML_14_AssociationEnd_isNavigable}

# UML_14_Primitive class attributes and methods

# DataType class attributes and methods

# UML_14_Attribute class attributes and methods
UML_14_Attribute_initialValue: Property = Property(name="initialValue", type=StringType)
UML_14_Attribute_visibility: Property = Property(name="visibility", type=StringType)
UML_14_Attribute.attributes={UML_14_Attribute_initialValue, UML_14_Attribute_visibility}

# UML_14_Generalization class attributes and methods
UML_14_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
UML_14_Generalization.attributes={UML_14_Generalization_discriminator}

# UML_14_Class class attributes and methods
UML_14_Class_isActive: Property = Property(name="isActive", type=StringType)
UML_14_Class.attributes={UML_14_Class_isActive}

# UML_14_NamedElement class attributes and methods
UML_14_NamedElement_name: Property = Property(name="name", type=StringType)
UML_14_NamedElement.attributes={UML_14_NamedElement_name}

# UML_14_Enumeration class attributes and methods

# UML_14_EnumerationLiteral class attributes and methods
UML_14_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
UML_14_EnumerationLiteral.attributes={UML_14_EnumerationLiteral_value}

# UML_14_Comment class attributes and methods
UML_14_Comment_body: Property = Property(name="body", type=StringType)
UML_14_Comment.attributes={UML_14_Comment_body}

# UML_14_Model class attributes and methods

# UML_14_Package class attributes and methods

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="UML_14_DataType", type=UML_14_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Parameter", type=UML_14_DataType, multiplicity=Multiplicity(1, 1))
    }
)
child7: BinaryAssociation = BinaryAssociation(
    name="child7",
    ends={
        Property(name="UML_14_Class", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Generalization", type=UML_14_Class, multiplicity=Multiplicity(0, 9999))
    }
)
parent8: BinaryAssociation = BinaryAssociation(
    name="parent8",
    ends={
        Property(name="UML_14_Class10", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Generalization9", type=UML_14_Class, multiplicity=Multiplicity(0, 9999))
    }
)
connection11: BinaryAssociation = BinaryAssociation(
    name="connection11",
    ends={
        Property(name="AssociationEnd", type=UML_14_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
association12: BinaryAssociation = BinaryAssociation(
    name="association12",
    ends={
        Property(name="Association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=UML_14_Association, multiplicity=Multiplicity(1, 1))
    }
)
participant13: BinaryAssociation = BinaryAssociation(
    name="participant13",
    ends={
        Property(name="UML_14_Class14", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd", type=UML_14_Class, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity15: BinaryAssociation = BinaryAssociation(
    name="multiplicity15",
    ends={
        Property(name="UML_14_MultiplicityRange17", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd16", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier18: BinaryAssociation = BinaryAssociation(
    name="qualifier18",
    ends={
        Property(name="UML_14_Attribute20", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd19", type=UML_14_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes21: BinaryAssociation = BinaryAssociation(
    name="attributes21",
    ends={
        Property(name="UML_14_Attribute23", type=UML_14_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Class22", type=UML_14_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods24: BinaryAssociation = BinaryAssociation(
    name="methods24",
    ends={
        Property(name="UML_14_Method26", type=UML_14_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Class25", type=UML_14_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters1: BinaryAssociation = BinaryAssociation(
    name="parameters1",
    ends={
        Property(name="UML_14_Parameter2", type=UML_14_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Method", type=UML_14_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity3: BinaryAssociation = BinaryAssociation(
    name="multiplicity3",
    ends={
        Property(name="UML_14_MultiplicityRange", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Attribute", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="UML_14_DataType6", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Attribute5", type=UML_14_DataType, multiplicity=Multiplicity(0, 1))
    }
)
classes30: BinaryAssociation = BinaryAssociation(
    name="classes30",
    ends={
        Property(name="UML_14_Class32", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package31", type=UML_14_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages34: BinaryAssociation = BinaryAssociation(
    name="packages34",
    ends={
        Property(name="UML_14_Package35", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package33", type=UML_14_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dataTypes36: BinaryAssociation = BinaryAssociation(
    name="dataTypes36",
    ends={
        Property(name="UML_14_DataType38", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package37", type=UML_14_DataType, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizations39: BinaryAssociation = BinaryAssociation(
    name="generalizations39",
    ends={
        Property(name="UML_14_Generalization41", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package40", type=UML_14_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations42: BinaryAssociation = BinaryAssociation(
    name="associations42",
    ends={
        Property(name="UML_14_Association", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package43", type=UML_14_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments44: BinaryAssociation = BinaryAssociation(
    name="comments44",
    ends={
        Property(name="UML_14_Comment", type=UML_14_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_NamedElement", type=UML_14_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints45: BinaryAssociation = BinaryAssociation(
    name="constraints45",
    ends={
        Property(name="UML_14_Constraint", type=UML_14_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_NamedElement46", type=UML_14_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal27: BinaryAssociation = BinaryAssociation(
    name="literal27",
    ends={
        Property(name="EnumerationLiteral", type=UML_14_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="enumeration", type=UML_14_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
enumeration28: BinaryAssociation = BinaryAssociation(
    name="enumeration28",
    ends={
        Property(name="Enumeration", type=UML_14_EnumerationLiteral, multiplicity=Multiplicity(1, 1)),
        Property(name="literal", type=UML_14_Enumeration, multiplicity=Multiplicity(1, 1))
    }
)
package29: BinaryAssociation = BinaryAssociation(
    name="package29",
    ends={
        Property(name="UML_14_Package", type=UML_14_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Model", type=UML_14_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML_14_Parameter_NamedElement = Generalization(general=NamedElement, specific=UML_14_Parameter)
gen_UML_14_Method_NamedElement = Generalization(general=NamedElement, specific=UML_14_Method)
gen_UML_14_Association_NamedElement = Generalization(general=NamedElement, specific=UML_14_Association)
gen_UML_14_AssociationEnd_NamedElement = Generalization(general=NamedElement, specific=UML_14_AssociationEnd)
gen_UML_14_Class_NamedElement = Generalization(general=NamedElement, specific=UML_14_Class)
gen_UML_14_DataType_NamedElement = Generalization(general=NamedElement, specific=UML_14_DataType)
gen_UML_14_Primitive_DataType = Generalization(general=DataType, specific=UML_14_Primitive)
gen_UML_14_Attribute_NamedElement = Generalization(general=NamedElement, specific=UML_14_Attribute)
gen_UML_14_Package_NamedElement = Generalization(general=NamedElement, specific=UML_14_Package)
gen_UML_14_Enumeration_DataType = Generalization(general=DataType, specific=UML_14_Enumeration)

# Domain Model
domain_model = DomainModel(
    name="UML_14",
    types={UML_14_Parameter, NamedElement, UML_14_DataType, UML_14_Constraint, UML_14_MultiplicityRange, UML_14_Method, UML_14_Association, UML_14_AssociationEnd, UML_14_Primitive, DataType, UML_14_Attribute, UML_14_Generalization, UML_14_Class, UML_14_NamedElement, UML_14_Enumeration, UML_14_EnumerationLiteral, UML_14_Comment, UML_14_Model, UML_14_Package},
    associations={type0, child7, parent8, connection11, association12, participant13, multiplicity15, qualifier18, attributes21, methods24, parameters1, multiplicity3, type4, classes30, packages34, dataTypes36, generalizations39, associations42, comments44, constraints45, literal27, enumeration28, package29},
    generalizations={gen_UML_14_Parameter_NamedElement, gen_UML_14_Method_NamedElement, gen_UML_14_Association_NamedElement, gen_UML_14_AssociationEnd_NamedElement, gen_UML_14_Class_NamedElement, gen_UML_14_DataType_NamedElement, gen_UML_14_Primitive_DataType, gen_UML_14_Attribute_NamedElement, gen_UML_14_Package_NamedElement, gen_UML_14_Enumeration_DataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)