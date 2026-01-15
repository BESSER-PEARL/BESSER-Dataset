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
smalluml_Class = Class(name="smalluml::Class")
smalluml_NamedElement = Class(name="smalluml::NamedElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
smalluml_Method = Class(name="smalluml::Method")
smalluml_Attribute = Class(name="smalluml::Attribute")
smalluml_Type = Class(name="smalluml::Type", is_abstract=True)
smalluml_String = Class(name="smalluml::String")
Type = Class(name="Type")
smalluml_Integer = Class(name="smalluml::Integer")
smalluml_Bool = Class(name="smalluml::Bool")
smalluml_Real = Class(name="smalluml::Real")
smalluml_UnlimitedNatural = Class(name="smalluml::UnlimitedNatural")
smalluml_Parameter = Class(name="smalluml::Parameter")
smalluml_Relation = Class(name="smalluml::Relation", is_abstract=True)
smalluml_Role = Class(name="smalluml::Role")
smalluml_Enumeration = Class(name="smalluml::Enumeration")
smalluml_Composition = Class(name="smalluml::Composition")
Relation = Class(name="Relation")
smalluml_Reference = Class(name="smalluml::Reference")
smalluml_Package = Class(name="smalluml::Package")

# smalluml_Class class attributes and methods

# smalluml_NamedElement class attributes and methods
smalluml_NamedElement_name: Property = Property(name="name", type=StringType)
smalluml_NamedElement.attributes={smalluml_NamedElement_name}

# NamedElement class attributes and methods

# smalluml_Method class attributes and methods

# smalluml_Attribute class attributes and methods

# smalluml_Type class attributes and methods

# smalluml_String class attributes and methods

# Type class attributes and methods

# smalluml_Integer class attributes and methods

# smalluml_Bool class attributes and methods

# smalluml_Real class attributes and methods

# smalluml_UnlimitedNatural class attributes and methods

# smalluml_Parameter class attributes and methods

# smalluml_Relation class attributes and methods

# smalluml_Role class attributes and methods
smalluml_Role_upperBound: Property = Property(name="upperBound", type=IntegerType)
smalluml_Role_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
smalluml_Role.attributes={smalluml_Role_upperBound, smalluml_Role_lowerBound}

# smalluml_Enumeration class attributes and methods
smalluml_Enumeration_values: Property = Property(name="values", type=StringType)
smalluml_Enumeration.attributes={smalluml_Enumeration_values}

# smalluml_Composition class attributes and methods

# Relation class attributes and methods

# smalluml_Reference class attributes and methods

# smalluml_Package class attributes and methods

# Relationships
method0: BinaryAssociation = BinaryAssociation(
    name="method0",
    ends={
        Property(name="smalluml_Method", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class", type=smalluml_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute1: BinaryAssociation = BinaryAssociation(
    name="attribute1",
    ends={
        Property(name="smalluml_Attribute", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class2", type=smalluml_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
super4: BinaryAssociation = BinaryAssociation(
    name="super4",
    ends={
        Property(name="smalluml_Class5", type=smalluml_Class, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Class3", type=smalluml_Class, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="smalluml_Type", type=smalluml_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Attribute7", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
parameter8: BinaryAssociation = BinaryAssociation(
    name="parameter8",
    ends={
        Property(name="smalluml_Parameter", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method9", type=smalluml_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
returnType10: BinaryAssociation = BinaryAssociation(
    name="returnType10",
    ends={
        Property(name="smalluml_Type12", type=smalluml_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Method11", type=smalluml_Type, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
type13: BinaryAssociation = BinaryAssociation(
    name="type13",
    ends={
        Property(name="smalluml_Type15", type=smalluml_Parameter, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Parameter14", type=smalluml_Type, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="smalluml_Role", type=smalluml_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Relation", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="smalluml_Role19", type=smalluml_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Relation18", type=smalluml_Role, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
class20: BinaryAssociation = BinaryAssociation(
    name="class20",
    ends={
        Property(name="smalluml_Class22", type=smalluml_Role, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Role21", type=smalluml_Class, multiplicity=Multiplicity(1, 1))
    }
)
member23: BinaryAssociation = BinaryAssociation(
    name="member23",
    ends={
        Property(name="smalluml_NamedElement", type=smalluml_Package, multiplicity=Multiplicity(1, 1)),
        Property(name="smalluml_Package", type=smalluml_NamedElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_smalluml_Class_NamedElement = Generalization(general=NamedElement, specific=smalluml_Class)
gen_smalluml_Attribute_NamedElement = Generalization(general=NamedElement, specific=smalluml_Attribute)
gen_smalluml_String_Type = Generalization(general=Type, specific=smalluml_String)
gen_smalluml_Integer_Type = Generalization(general=Type, specific=smalluml_Integer)
gen_smalluml_Bool_Type = Generalization(general=Type, specific=smalluml_Bool)
gen_smalluml_Real_Type = Generalization(general=Type, specific=smalluml_Real)
gen_smalluml_UnlimitedNatural_Type = Generalization(general=Type, specific=smalluml_UnlimitedNatural)
gen_smalluml_Method_NamedElement = Generalization(general=NamedElement, specific=smalluml_Method)
gen_smalluml_Parameter_NamedElement = Generalization(general=NamedElement, specific=smalluml_Parameter)
gen_smalluml_Relation_NamedElement = Generalization(general=NamedElement, specific=smalluml_Relation)
gen_smalluml_Role_NamedElement = Generalization(general=NamedElement, specific=smalluml_Role)
gen_smalluml_Enumeration_Type = Generalization(general=Type, specific=smalluml_Enumeration)
gen_smalluml_Enumeration_NamedElement = Generalization(general=NamedElement, specific=smalluml_Enumeration)
gen_smalluml_Composition_Relation = Generalization(general=Relation, specific=smalluml_Composition)
gen_smalluml_Reference_Relation = Generalization(general=Relation, specific=smalluml_Reference)
gen_smalluml_Package_NamedElement = Generalization(general=NamedElement, specific=smalluml_Package)

# Domain Model
domain_model = DomainModel(
    name="smalluml",
    types={smalluml_Class, smalluml_NamedElement, NamedElement, smalluml_Method, smalluml_Attribute, smalluml_Type, smalluml_String, Type, smalluml_Integer, smalluml_Bool, smalluml_Real, smalluml_UnlimitedNatural, smalluml_Parameter, smalluml_Relation, smalluml_Role, smalluml_Enumeration, smalluml_Composition, Relation, smalluml_Reference, smalluml_Package},
    associations={method0, attribute1, super4, type6, parameter8, returnType10, type13, source16, target17, class20, member23},
    generalizations={gen_smalluml_Class_NamedElement, gen_smalluml_Attribute_NamedElement, gen_smalluml_String_Type, gen_smalluml_Integer_Type, gen_smalluml_Bool_Type, gen_smalluml_Real_Type, gen_smalluml_UnlimitedNatural_Type, gen_smalluml_Method_NamedElement, gen_smalluml_Parameter_NamedElement, gen_smalluml_Relation_NamedElement, gen_smalluml_Role_NamedElement, gen_smalluml_Enumeration_Type, gen_smalluml_Enumeration_NamedElement, gen_smalluml_Composition_Relation, gen_smalluml_Reference_Relation, gen_smalluml_Package_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)