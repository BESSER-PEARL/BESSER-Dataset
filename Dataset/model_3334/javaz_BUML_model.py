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
JavaVisibilityKind: Enumeration = Enumeration(
    name="JavaVisibilityKind",
    literals={
            EnumerationLiteral(name="PACKAGE"),
			EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE"),
			EnumerationLiteral(name="PROTECTED")
    }
)

JavaKind: Enumeration = Enumeration(
    name="JavaKind",
    literals={
            EnumerationLiteral(name="CLASS"),
			EnumerationLiteral(name="INTERFACE"),
			EnumerationLiteral(name="EXCEPTION")
    }
)

JavaParameterKind: Enumeration = Enumeration(
    name="JavaParameterKind",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="RETURN")
    }
)

# Classes
javaz_Javaz = Class(name="javaz::Javaz")
JavaElement = Class(name="JavaElement")
javaz_JavaPackageX = Class(name="javaz::JavaPackageX")
javaz_JavaClass = Class(name="javaz::JavaClass")
javaz_Method = Class(name="javaz::Method")
javaz_Field = Class(name="javaz::Field")
javaz_JavaParameter = Class(name="javaz::JavaParameter")
javaz_Block = Class(name="javaz::Block")
javaz_JavaElement = Class(name="javaz::JavaElement")

# javaz_Javaz class attributes and methods

# JavaElement class attributes and methods

# javaz_JavaPackageX class attributes and methods
javaz_JavaPackageX_needToGenerate: Property = Property(name="needToGenerate", type=BooleanType)
javaz_JavaPackageX.attributes={javaz_JavaPackageX_needToGenerate}

# javaz_JavaClass class attributes and methods
javaz_JavaClass_kind: Property = Property(name="kind", type=StringType)
javaz_JavaClass_public: Property = Property(name="public", type=BooleanType)
javaz_JavaClass_final: Property = Property(name="final", type=BooleanType)
javaz_JavaClass_rewritable: Property = Property(name="rewritable", type=BooleanType)
javaz_JavaClass_needToGenerate: Property = Property(name="needToGenerate", type=BooleanType)
javaz_JavaClass.attributes={javaz_JavaClass_final, javaz_JavaClass_needToGenerate, javaz_JavaClass_rewritable, javaz_JavaClass_public, javaz_JavaClass_kind}

# javaz_Method class attributes and methods
javaz_Method_synchronized: Property = Property(name="synchronized", type=BooleanType)
javaz_Method_visibility: Property = Property(name="visibility", type=StringType)
javaz_Method_final: Property = Property(name="final", type=BooleanType)
javaz_Method_static: Property = Property(name="static", type=BooleanType)
javaz_Method_constructor: Property = Property(name="constructor", type=BooleanType)
javaz_Method_native: Property = Property(name="native", type=BooleanType)
javaz_Method_abstract: Property = Property(name="abstract", type=BooleanType)
javaz_Method.attributes={javaz_Method_native, javaz_Method_constructor, javaz_Method_static, javaz_Method_visibility, javaz_Method_final, javaz_Method_abstract, javaz_Method_synchronized}

# javaz_Field class attributes and methods
javaz_Field_transient: Property = Property(name="transient", type=BooleanType)
javaz_Field_visibility: Property = Property(name="visibility", type=StringType)
javaz_Field_static: Property = Property(name="static", type=BooleanType)
javaz_Field_volatile: Property = Property(name="volatile", type=BooleanType)
javaz_Field_final: Property = Property(name="final", type=BooleanType)
javaz_Field_type: Property = Property(name="type", type=StringType)
javaz_Field.attributes={javaz_Field_transient, javaz_Field_volatile, javaz_Field_final, javaz_Field_visibility, javaz_Field_static, javaz_Field_type}

# javaz_JavaParameter class attributes and methods
javaz_JavaParameter_parameterKind: Property = Property(name="parameterKind", type=StringType)
javaz_JavaParameter_final: Property = Property(name="final", type=BooleanType)
javaz_JavaParameter_type: Property = Property(name="type", type=StringType)
javaz_JavaParameter_kind: Property = Property(name="kind", type=StringType)
javaz_JavaParameter.attributes={javaz_JavaParameter_parameterKind, javaz_JavaParameter_final, javaz_JavaParameter_type, javaz_JavaParameter_kind}

# javaz_Block class attributes and methods
javaz_Block_content: Property = Property(name="content", type=StringType)
javaz_Block.attributes={javaz_Block_content}

# javaz_JavaElement class attributes and methods
javaz_JavaElement_name: Property = Property(name="name", type=StringType)
javaz_JavaElement.attributes={javaz_JavaElement_name}

# Relationships
packages0: BinaryAssociation = BinaryAssociation(
    name="packages0",
    ends={
        Property(name="javaz_JavaPackageX", type=javaz_Javaz, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_Javaz", type=javaz_JavaPackageX, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classes1: BinaryAssociation = BinaryAssociation(
    name="classes1",
    ends={
        Property(name="javaz_JavaClass", type=javaz_Javaz, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_Javaz2", type=javaz_JavaClass, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods3: BinaryAssociation = BinaryAssociation(
    name="methods3",
    ends={
        Property(name="javaz_Method", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass4", type=javaz_Method, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fields5: BinaryAssociation = BinaryAssociation(
    name="fields5",
    ends={
        Property(name="javaz_Field", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass6", type=javaz_Field, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports8: BinaryAssociation = BinaryAssociation(
    name="imports8",
    ends={
        Property(name="javaz_JavaClass9", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass7", type=javaz_JavaClass, multiplicity=Multiplicity(0, 9999))
    }
)
package10: BinaryAssociation = BinaryAssociation(
    name="package10",
    ends={
        Property(name="javaz_JavaPackageX12", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass11", type=javaz_JavaPackageX, multiplicity=Multiplicity(0, 1))
    }
)
extends14: BinaryAssociation = BinaryAssociation(
    name="extends14",
    ends={
        Property(name="javaz_JavaClass15", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass13", type=javaz_JavaClass, multiplicity=Multiplicity(0, 1))
    }
)
implements17: BinaryAssociation = BinaryAssociation(
    name="implements17",
    ends={
        Property(name="javaz_JavaClass18", type=javaz_JavaClass, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_JavaClass16", type=javaz_JavaClass, multiplicity=Multiplicity(0, 9999))
    }
)
parameters19: BinaryAssociation = BinaryAssociation(
    name="parameters19",
    ends={
        Property(name="javaz_JavaParameter", type=javaz_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_Method20", type=javaz_JavaParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
block21: BinaryAssociation = BinaryAssociation(
    name="block21",
    ends={
        Property(name="javaz_Block", type=javaz_Method, multiplicity=Multiplicity(1, 1)),
        Property(name="javaz_Method22", type=javaz_Block, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_javaz_Javaz_JavaElement = Generalization(general=JavaElement, specific=javaz_Javaz)
gen_javaz_JavaClass_JavaElement = Generalization(general=JavaElement, specific=javaz_JavaClass)
gen_javaz_JavaPackageX_JavaElement = Generalization(general=JavaElement, specific=javaz_JavaPackageX)
gen_javaz_JavaParameter_JavaElement = Generalization(general=JavaElement, specific=javaz_JavaParameter)
gen_javaz_Method_JavaElement = Generalization(general=JavaElement, specific=javaz_Method)
gen_javaz_Field_JavaElement = Generalization(general=JavaElement, specific=javaz_Field)

# Domain Model
domain_model = DomainModel(
    name="javaz",
    types={javaz_Javaz, JavaElement, javaz_JavaPackageX, javaz_JavaClass, javaz_Method, javaz_Field, javaz_JavaParameter, javaz_Block, javaz_JavaElement, JavaVisibilityKind, JavaKind, JavaParameterKind},
    associations={packages0, classes1, methods3, fields5, imports8, package10, extends14, implements17, parameters19, block21},
    generalizations={gen_javaz_Javaz_JavaElement, gen_javaz_JavaClass_JavaElement, gen_javaz_JavaPackageX_JavaElement, gen_javaz_JavaParameter_JavaElement, gen_javaz_Method_JavaElement, gen_javaz_Field_JavaElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)