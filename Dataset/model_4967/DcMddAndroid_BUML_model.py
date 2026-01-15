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
Visibility: Enumeration = Enumeration(
    name="Visibility",
    literals={
            EnumerationLiteral(name="public"),
			EnumerationLiteral(name="private"),
			EnumerationLiteral(name="protected")
    }
)

# Classes
dcmddandroid_Implements = Class(name="dcmddandroid::Implements")
dcmddandroid_Attribute = Class(name="dcmddandroid::Attribute")
dcmddandroid_Method = Class(name="dcmddandroid::Method")
dcmddandroid_Association = Class(name="dcmddandroid::Association", is_abstract=True)
dcmddandroid_Class = Class(name="dcmddandroid::Class")
AbstractClass = Class(name="AbstractClass")
dcmddandroid_NamedElement = Class(name="dcmddandroid::NamedElement", is_abstract=True)
dcmddandroid_AbstractClass = Class(name="dcmddandroid::AbstractClass", is_abstract=True)
ModelElement = Class(name="ModelElement")
EVisibility = Class(name="EVisibility")
dcmddandroid_ClassElement = Class(name="dcmddandroid::ClassElement", is_abstract=True)
NamedElement = Class(name="NamedElement")
ClassElement = Class(name="ClassElement")
dcmddandroid_Parameter = Class(name="dcmddandroid::Parameter")
dcmddandroid_CycleClass = Class(name="dcmddandroid::CycleClass")
dcmddandroid_PersistentClass = Class(name="dcmddandroid::PersistentClass")
dcmddandroid_Interface = Class(name="dcmddandroid::Interface")
dcmddandroid_EnumValue = Class(name="dcmddandroid::EnumValue")
dcmddandroid_Diagram = Class(name="dcmddandroid::Diagram")
dcmddandroid_ModelElement = Class(name="dcmddandroid::ModelElement", is_abstract=True)
dcmddandroid_Enum = Class(name="dcmddandroid::Enum")
dcmddandroid_EVisibility = Class(name="dcmddandroid::EVisibility")
dcmddandroid_Agregation = Class(name="dcmddandroid::Agregation")
Association = Class(name="Association")
dcmddandroid_Composition = Class(name="dcmddandroid::Composition")

# dcmddandroid_Implements class attributes and methods

# dcmddandroid_Attribute class attributes and methods
dcmddandroid_Attribute_defaultValue: Property = Property(name="defaultValue", type=StringType)
dcmddandroid_Attribute_type: Property = Property(name="type", type=StringType)
dcmddandroid_Attribute_secured: Property = Property(name="secured", type=StringType)
dcmddandroid_Attribute.attributes={dcmddandroid_Attribute_secured, dcmddandroid_Attribute_defaultValue, dcmddandroid_Attribute_type}

# dcmddandroid_Method class attributes and methods
dcmddandroid_Method_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
dcmddandroid_Method_returns: Property = Property(name="returns", type=StringType)
dcmddandroid_Method.attributes={dcmddandroid_Method_isAbstract, dcmddandroid_Method_returns}

# dcmddandroid_Association class attributes and methods
dcmddandroid_Association_rolSource: Property = Property(name="rolSource", type=StringType)
dcmddandroid_Association_rolTarget: Property = Property(name="rolTarget", type=StringType)
dcmddandroid_Association_minMultiplicitySource: Property = Property(name="minMultiplicitySource", type=IntegerType)
dcmddandroid_Association_maxMultiplicitySource: Property = Property(name="maxMultiplicitySource", type=IntegerType)
dcmddandroid_Association_minMultiplicityTarget: Property = Property(name="minMultiplicityTarget", type=IntegerType)
dcmddandroid_Association_maxMultiplicityTarget: Property = Property(name="maxMultiplicityTarget", type=IntegerType)
dcmddandroid_Association.attributes={dcmddandroid_Association_rolTarget, dcmddandroid_Association_minMultiplicitySource, dcmddandroid_Association_rolSource, dcmddandroid_Association_minMultiplicityTarget, dcmddandroid_Association_maxMultiplicitySource, dcmddandroid_Association_maxMultiplicityTarget}

# dcmddandroid_Class class attributes and methods

# AbstractClass class attributes and methods

# dcmddandroid_NamedElement class attributes and methods
dcmddandroid_NamedElement_name: Property = Property(name="name", type=StringType)
dcmddandroid_NamedElement.attributes={dcmddandroid_NamedElement_name}

# dcmddandroid_AbstractClass class attributes and methods
dcmddandroid_AbstractClass_isAbstract: Property = Property(name="isAbstract", type=BooleanType)
dcmddandroid_AbstractClass.attributes={dcmddandroid_AbstractClass_isAbstract}

# ModelElement class attributes and methods

# EVisibility class attributes and methods

# dcmddandroid_ClassElement class attributes and methods
dcmddandroid_ClassElement_final: Property = Property(name="final", type=BooleanType)
dcmddandroid_ClassElement_static: Property = Property(name="static", type=BooleanType)
dcmddandroid_ClassElement.attributes={dcmddandroid_ClassElement_static, dcmddandroid_ClassElement_final}

# NamedElement class attributes and methods

# ClassElement class attributes and methods

# dcmddandroid_Parameter class attributes and methods
dcmddandroid_Parameter_type: Property = Property(name="type", type=StringType)
dcmddandroid_Parameter.attributes={dcmddandroid_Parameter_type}

# dcmddandroid_CycleClass class attributes and methods

# dcmddandroid_PersistentClass class attributes and methods

# dcmddandroid_Interface class attributes and methods

# dcmddandroid_EnumValue class attributes and methods
dcmddandroid_EnumValue_intValue: Property = Property(name="intValue", type=IntegerType)
dcmddandroid_EnumValue.attributes={dcmddandroid_EnumValue_intValue}

# dcmddandroid_Diagram class attributes and methods

# dcmddandroid_ModelElement class attributes and methods

# dcmddandroid_Enum class attributes and methods

# dcmddandroid_EVisibility class attributes and methods
dcmddandroid_EVisibility_visibility: Property = Property(name="visibility", type=StringType)
dcmddandroid_EVisibility.attributes={dcmddandroid_EVisibility_visibility}

# dcmddandroid_Agregation class attributes and methods

# Association class attributes and methods

# dcmddandroid_Composition class attributes and methods

# Relationships
implements0: BinaryAssociation = BinaryAssociation(
    name="implements0",
    ends={
        Property(name="Implements", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="implements", type=dcmddandroid_Implements, multiplicity=Multiplicity(0, 9999))
    }
)
attributes1: BinaryAssociation = BinaryAssociation(
    name="attributes1",
    ends={
        Property(name="dcmddandroid_Attribute", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_AbstractClass", type=dcmddandroid_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods2: BinaryAssociation = BinaryAssociation(
    name="methods2",
    ends={
        Property(name="dcmddandroid_Method", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_AbstractClass3", type=dcmddandroid_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
associationAsSource4: BinaryAssociation = BinaryAssociation(
    name="associationAsSource4",
    ends={
        Property(name="Association", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=dcmddandroid_Association, multiplicity=Multiplicity(0, 9999))
    }
)
associationAsTarget5: BinaryAssociation = BinaryAssociation(
    name="associationAsTarget5",
    ends={
        Property(name="Association6", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=dcmddandroid_Association, multiplicity=Multiplicity(0, 9999))
    }
)
methods9: BinaryAssociation = BinaryAssociation(
    name="methods9",
    ends={
        Property(name="dcmddandroid_Method11", type=dcmddandroid_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Interface10", type=dcmddandroid_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parameters12: BinaryAssociation = BinaryAssociation(
    name="parameters12",
    ends={
        Property(name="dcmddandroid_Parameter", type=dcmddandroid_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Method13", type=dcmddandroid_Parameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
superInterfaces8: BinaryAssociation = BinaryAssociation(
    name="superInterfaces8",
    ends={
        Property(name="dcmddandroid_Interface", type=dcmddandroid_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Interface7", type=dcmddandroid_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
values15: BinaryAssociation = BinaryAssociation(
    name="values15",
    ends={
        Property(name="dcmddandroid_EnumValue", type=dcmddandroid_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Enum", type=dcmddandroid_EnumValue, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
modelElements14: BinaryAssociation = BinaryAssociation(
    name="modelElements14",
    ends={
        Property(name="dcmddandroid_ModelElement", type=dcmddandroid_Diagram, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Diagram", type=dcmddandroid_ModelElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
implements21: BinaryAssociation = BinaryAssociation(
    name="implements21",
    ends={
        Property(name="AbstractClass23", type=dcmddandroid_Implements, multiplicity=Multiplicity(1, 1)),
        Property(name="implements22", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="AbstractClass", type=dcmddandroid_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationAsSource", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1))
    }
)
target17: BinaryAssociation = BinaryAssociation(
    name="target17",
    ends={
        Property(name="AbstractClass18", type=dcmddandroid_Association, multiplicity=Multiplicity(1, 1)),
        Property(name="associationAsTarget", type=dcmddandroid_AbstractClass, multiplicity=Multiplicity(1, 1))
    }
)
implemented19: BinaryAssociation = BinaryAssociation(
    name="implemented19",
    ends={
        Property(name="dcmddandroid_Interface20", type=dcmddandroid_Implements, multiplicity=Multiplicity(1, 1)),
        Property(name="dcmddandroid_Implements", type=dcmddandroid_Interface, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_dcmddandroid_Class_AbstractClass = Generalization(general=AbstractClass, specific=dcmddandroid_Class)
gen_dcmddandroid_AbstractClass_ModelElement = Generalization(general=ModelElement, specific=dcmddandroid_AbstractClass)
gen_dcmddandroid_AbstractClass_EVisibility = Generalization(general=EVisibility, specific=dcmddandroid_AbstractClass)
gen_dcmddandroid_ClassElement_NamedElement = Generalization(general=NamedElement, specific=dcmddandroid_ClassElement)
gen_dcmddandroid_ClassElement_EVisibility = Generalization(general=EVisibility, specific=dcmddandroid_ClassElement)
gen_dcmddandroid_Method_ClassElement = Generalization(general=ClassElement, specific=dcmddandroid_Method)
gen_dcmddandroid_CycleClass_AbstractClass = Generalization(general=AbstractClass, specific=dcmddandroid_CycleClass)
gen_dcmddandroid_PersistentClass_AbstractClass = Generalization(general=AbstractClass, specific=dcmddandroid_PersistentClass)
gen_dcmddandroid_Interface_ModelElement = Generalization(general=ModelElement, specific=dcmddandroid_Interface)
gen_dcmddandroid_Interface_EVisibility = Generalization(general=EVisibility, specific=dcmddandroid_Interface)
gen_dcmddandroid_EnumValue_NamedElement = Generalization(general=NamedElement, specific=dcmddandroid_EnumValue)
gen_dcmddandroid_Association_ModelElement = Generalization(general=ModelElement, specific=dcmddandroid_Association)
gen_dcmddandroid_Attribute_ClassElement = Generalization(general=ClassElement, specific=dcmddandroid_Attribute)
gen_dcmddandroid_Diagram_NamedElement = Generalization(general=NamedElement, specific=dcmddandroid_Diagram)
gen_dcmddandroid_ModelElement_NamedElement = Generalization(general=NamedElement, specific=dcmddandroid_ModelElement)
gen_dcmddandroid_Parameter_NamedElement = Generalization(general=NamedElement, specific=dcmddandroid_Parameter)
gen_dcmddandroid_Enum_ModelElement = Generalization(general=ModelElement, specific=dcmddandroid_Enum)
gen_dcmddandroid_Agregation_Association = Generalization(general=Association, specific=dcmddandroid_Agregation)
gen_dcmddandroid_Composition_Association = Generalization(general=Association, specific=dcmddandroid_Composition)
gen_dcmddandroid_Implements_ModelElement = Generalization(general=ModelElement, specific=dcmddandroid_Implements)

# Domain Model
domain_model = DomainModel(
    name="dcmddandroid",
    types={dcmddandroid_Implements, dcmddandroid_Attribute, dcmddandroid_Method, dcmddandroid_Association, dcmddandroid_Class, AbstractClass, dcmddandroid_NamedElement, dcmddandroid_AbstractClass, ModelElement, EVisibility, dcmddandroid_ClassElement, NamedElement, ClassElement, dcmddandroid_Parameter, dcmddandroid_CycleClass, dcmddandroid_PersistentClass, dcmddandroid_Interface, dcmddandroid_EnumValue, dcmddandroid_Diagram, dcmddandroid_ModelElement, dcmddandroid_Enum, dcmddandroid_EVisibility, dcmddandroid_Agregation, Association, dcmddandroid_Composition, Visibility},
    associations={implements0, attributes1, methods2, associationAsSource4, associationAsTarget5, methods9, parameters12, superInterfaces8, values15, modelElements14, implements21, source16, target17, implemented19},
    generalizations={gen_dcmddandroid_Class_AbstractClass, gen_dcmddandroid_AbstractClass_ModelElement, gen_dcmddandroid_AbstractClass_EVisibility, gen_dcmddandroid_ClassElement_NamedElement, gen_dcmddandroid_ClassElement_EVisibility, gen_dcmddandroid_Method_ClassElement, gen_dcmddandroid_CycleClass_AbstractClass, gen_dcmddandroid_PersistentClass_AbstractClass, gen_dcmddandroid_Interface_ModelElement, gen_dcmddandroid_Interface_EVisibility, gen_dcmddandroid_EnumValue_NamedElement, gen_dcmddandroid_Association_ModelElement, gen_dcmddandroid_Attribute_ClassElement, gen_dcmddandroid_Diagram_NamedElement, gen_dcmddandroid_ModelElement_NamedElement, gen_dcmddandroid_Parameter_NamedElement, gen_dcmddandroid_Enum_ModelElement, gen_dcmddandroid_Agregation_Association, gen_dcmddandroid_Composition_Association, gen_dcmddandroid_Implements_ModelElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)