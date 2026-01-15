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
UML_14_Parameter = Class(name="UML::14::Parameter")
NamedElement = Class(name="NamedElement")
UML_14_Enumeration = Class(name="UML::14::Enumeration")
UML_14_Primitive = Class(name="UML::14::Primitive")
UML_14_Generalization = Class(name="UML::14::Generalization")
UML_14_Class = Class(name="UML::14::Class")
UML_14_Association = Class(name="UML::14::Association")
UML_14_AssociationEnd = Class(name="UML::14::AssociationEnd")
UML_14_Constraint = Class(name="UML::14::Constraint", is_abstract=True)
UML_14_MultiplicityRange = Class(name="UML::14::MultiplicityRange")
UML_14_Method = Class(name="UML::14::Method")
UML_14_Attribute = Class(name="UML::14::Attribute")
UML_14_Comment = Class(name="UML::14::Comment")
UML_14_Model = Class(name="UML::14::Model")
UML_14_Package = Class(name="UML::14::Package")
UML_14_NamedElement = Class(name="UML::14::NamedElement", is_abstract=True)
UML_14_EnumerationLiteral = Class(name="UML::14::EnumerationLiteral")

# UML_14_Parameter class attributes and methods
UML_14_Parameter_kind: Property = Property(name="kind", type=StringType)
UML_14_Parameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
UML_14_Parameter.attributes={UML_14_Parameter_defaultValue, UML_14_Parameter_kind}

# NamedElement class attributes and methods

# UML_14_Enumeration class attributes and methods

# UML_14_Primitive class attributes and methods

# UML_14_Generalization class attributes and methods
UML_14_Generalization_discriminator: Property = Property(name="discriminator", type=StringType)
UML_14_Generalization.attributes={UML_14_Generalization_discriminator}

# UML_14_Class class attributes and methods
UML_14_Class_isActive: Property = Property(name="isActive", type=StringType)
UML_14_Class.attributes={UML_14_Class_isActive}

# UML_14_Association class attributes and methods

# UML_14_AssociationEnd class attributes and methods
UML_14_AssociationEnd_isNavigable: Property = Property(name="isNavigable", type=StringType)
UML_14_AssociationEnd_visibility: Property = Property(name="visibility", type=StringType)
UML_14_AssociationEnd.attributes={UML_14_AssociationEnd_isNavigable, UML_14_AssociationEnd_visibility}

# UML_14_Constraint class attributes and methods
UML_14_Constraint_body: Property = Property(name="body", type=StringType)
UML_14_Constraint.attributes={UML_14_Constraint_body}

# UML_14_MultiplicityRange class attributes and methods
UML_14_MultiplicityRange_lower: Property = Property(name="lower", type=StringType)
UML_14_MultiplicityRange_upper: Property = Property(name="upper", type=StringType)
UML_14_MultiplicityRange.attributes={UML_14_MultiplicityRange_upper, UML_14_MultiplicityRange_lower}

# UML_14_Method class attributes and methods
UML_14_Method_body: Property = Property(name="body", type=StringType)
UML_14_Method_visibility: Property = Property(name="visibility", type=StringType)
UML_14_Method.attributes={UML_14_Method_body, UML_14_Method_visibility}

# UML_14_Attribute class attributes and methods
UML_14_Attribute_visibility: Property = Property(name="visibility", type=StringType)
UML_14_Attribute_initialValue: Property = Property(name="initialValue", type=StringType)
UML_14_Attribute.attributes={UML_14_Attribute_initialValue, UML_14_Attribute_visibility}

# UML_14_Comment class attributes and methods
UML_14_Comment_body: Property = Property(name="body", type=StringType)
UML_14_Comment.attributes={UML_14_Comment_body}

# UML_14_Model class attributes and methods

# UML_14_Package class attributes and methods

# UML_14_NamedElement class attributes and methods
UML_14_NamedElement_name: Property = Property(name="name", type=StringType)
UML_14_NamedElement.attributes={UML_14_NamedElement_name}

# UML_14_EnumerationLiteral class attributes and methods
UML_14_EnumerationLiteral_value: Property = Property(name="value", type=StringType)
UML_14_EnumerationLiteral.attributes={UML_14_EnumerationLiteral_value}

# Relationships
enumType0: BinaryAssociation = BinaryAssociation(
    name="enumType0",
    ends={
        Property(name="UML_14_Enumeration", type=UML_14_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Parameter", type=UML_14_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
multiplicity6: BinaryAssociation = BinaryAssociation(
    name="multiplicity6",
    ends={
        Property(name="UML_14_MultiplicityRange", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Attribute", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
enumType7: BinaryAssociation = BinaryAssociation(
    name="enumType7",
    ends={
        Property(name="UML_14_Enumeration9", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Attribute8", type=UML_14_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
primitiveType10: BinaryAssociation = BinaryAssociation(
    name="primitiveType10",
    ends={
        Property(name="UML_14_Primitive", type=UML_14_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Attribute11", type=UML_14_Primitive, multiplicity=Multiplicity(0, 1))
    }
)
child12: BinaryAssociation = BinaryAssociation(
    name="child12",
    ends={
        Property(name="UML_14_Class", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Generalization", type=UML_14_Class, multiplicity=Multiplicity(0, 9999))
    }
)
parent13: BinaryAssociation = BinaryAssociation(
    name="parent13",
    ends={
        Property(name="UML_14_Class15", type=UML_14_Generalization, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Generalization14", type=UML_14_Class, multiplicity=Multiplicity(0, 9999))
    }
)
connection16: BinaryAssociation = BinaryAssociation(
    name="connection16",
    ends={
        Property(name="AssociationEnd", type=UML_14_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
association17: BinaryAssociation = BinaryAssociation(
    name="association17",
    ends={
        Property(name="Association", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=UML_14_Association, multiplicity=Multiplicity(1, 1))
    }
)
participant18: BinaryAssociation = BinaryAssociation(
    name="participant18",
    ends={
        Property(name="UML_14_Class19", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd", type=UML_14_Class, multiplicity=Multiplicity(0, 1))
    }
)
primitiveType1: BinaryAssociation = BinaryAssociation(
    name="primitiveType1",
    ends={
        Property(name="UML_14_Enumeration3", type=UML_14_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Parameter2", type=UML_14_Enumeration, multiplicity=Multiplicity(0, 1))
    }
)
parameters4: BinaryAssociation = BinaryAssociation(
    name="parameters4",
    ends={
        Property(name="UML_14_Parameter5", type=UML_14_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Method", type=UML_14_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
package34: BinaryAssociation = BinaryAssociation(
    name="package34",
    ends={
        Property(name="UML_14_Package", type=UML_14_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Model", type=UML_14_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes35: BinaryAssociation = BinaryAssociation(
    name="classes35",
    ends={
        Property(name="UML_14_Class37", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package36", type=UML_14_Class, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
packages39: BinaryAssociation = BinaryAssociation(
    name="packages39",
    ends={
        Property(name="UML_14_Package40", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package38", type=UML_14_Package, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enums41: BinaryAssociation = BinaryAssociation(
    name="enums41",
    ends={
        Property(name="UML_14_Enumeration43", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package42", type=UML_14_Enumeration, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
generalizations44: BinaryAssociation = BinaryAssociation(
    name="generalizations44",
    ends={
        Property(name="UML_14_Generalization46", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package45", type=UML_14_Generalization, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associations47: BinaryAssociation = BinaryAssociation(
    name="associations47",
    ends={
        Property(name="UML_14_Association", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package48", type=UML_14_Association, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitiveTypes49: BinaryAssociation = BinaryAssociation(
    name="primitiveTypes49",
    ends={
        Property(name="UML_14_Primitive51", type=UML_14_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Package50", type=UML_14_Primitive, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
comments52: BinaryAssociation = BinaryAssociation(
    name="comments52",
    ends={
        Property(name="UML_14_Comment", type=UML_14_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_NamedElement", type=UML_14_Comment, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
multiplicity20: BinaryAssociation = BinaryAssociation(
    name="multiplicity20",
    ends={
        Property(name="UML_14_MultiplicityRange22", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd21", type=UML_14_MultiplicityRange, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
qualifier23: BinaryAssociation = BinaryAssociation(
    name="qualifier23",
    ends={
        Property(name="UML_14_Attribute25", type=UML_14_AssociationEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_AssociationEnd24", type=UML_14_Attribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
attributes26: BinaryAssociation = BinaryAssociation(
    name="attributes26",
    ends={
        Property(name="UML_14_Attribute28", type=UML_14_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Class27", type=UML_14_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods29: BinaryAssociation = BinaryAssociation(
    name="methods29",
    ends={
        Property(name="UML_14_Method31", type=UML_14_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Class30", type=UML_14_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
literal32: BinaryAssociation = BinaryAssociation(
    name="literal32",
    ends={
        Property(name="UML_14_EnumerationLiteral", type=UML_14_Enumeration, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_Enumeration33", type=UML_14_EnumerationLiteral, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
constraints53: BinaryAssociation = BinaryAssociation(
    name="constraints53",
    ends={
        Property(name="UML_14_Constraint", type=UML_14_NamedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="UML_14_NamedElement54", type=UML_14_Constraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_UML_14_Parameter_NamedElement = Generalization(general=NamedElement, specific=UML_14_Parameter)
gen_UML_14_Association_NamedElement = Generalization(general=NamedElement, specific=UML_14_Association)
gen_UML_14_AssociationEnd_NamedElement = Generalization(general=NamedElement, specific=UML_14_AssociationEnd)
gen_UML_14_Method_NamedElement = Generalization(general=NamedElement, specific=UML_14_Method)
gen_UML_14_Attribute_NamedElement = Generalization(general=NamedElement, specific=UML_14_Attribute)
gen_UML_14_Package_NamedElement = Generalization(general=NamedElement, specific=UML_14_Package)
gen_UML_14_Class_NamedElement = Generalization(general=NamedElement, specific=UML_14_Class)
gen_UML_14_Primitive_NamedElement = Generalization(general=NamedElement, specific=UML_14_Primitive)
gen_UML_14_Enumeration_NamedElement = Generalization(general=NamedElement, specific=UML_14_Enumeration)

# Domain Model
domain_model = DomainModel(
    name="UML_14",
    types={UML_14_Parameter, NamedElement, UML_14_Enumeration, UML_14_Primitive, UML_14_Generalization, UML_14_Class, UML_14_Association, UML_14_AssociationEnd, UML_14_Constraint, UML_14_MultiplicityRange, UML_14_Method, UML_14_Attribute, UML_14_Comment, UML_14_Model, UML_14_Package, UML_14_NamedElement, UML_14_EnumerationLiteral},
    associations={enumType0, multiplicity6, enumType7, primitiveType10, child12, parent13, connection16, association17, participant18, primitiveType1, parameters4, package34, classes35, packages39, enums41, generalizations44, associations47, primitiveTypes49, comments52, multiplicity20, qualifier23, attributes26, methods29, literal32, constraints53},
    generalizations={gen_UML_14_Parameter_NamedElement, gen_UML_14_Association_NamedElement, gen_UML_14_AssociationEnd_NamedElement, gen_UML_14_Method_NamedElement, gen_UML_14_Attribute_NamedElement, gen_UML_14_Package_NamedElement, gen_UML_14_Class_NamedElement, gen_UML_14_Primitive_NamedElement, gen_UML_14_Enumeration_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)