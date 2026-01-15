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
raas_small_test_#19723516 = Class(name="raas::small::test::#19723516")
raas_small_test_ReposRoot = Class(name="raas::small::test::ReposRoot")
raas_small_test_#29373817 = Class(name="raas::small::test::#29373817")
raas_small_test_TopClassB = Class(name="raas::small::test::TopClassB")
raas_small_test_#7345254 = Class(name="raas::small::test::#7345254")
raas_small_test_#11832905 = Class(name="raas::small::test::#11832905")
raas_small_test_TopClassM = Class(name="raas::small::test::TopClassM")
raas_small_test_TopClassA = Class(name="raas::small::test::TopClassA")
raas_small_test_#5656663 = Class(name="raas::small::test::#5656663")
raas_small_test_#16551649 = Class(name="raas::small::test::#16551649")
raas_small_test_TopClassC = Class(name="raas::small::test::TopClassC")
raas_small_test_TopClassD = Class(name="raas::small::test::TopClassD")
raas_small_test_UnderClassE = Class(name="raas::small::test::UnderClassE")
raas_small_test_UnderClassF = Class(name="raas::small::test::UnderClassF")
raas_small_test_ThirdLevelClassJ = Class(name="raas::small::test::ThirdLevelClassJ")
raas_small_test_#10382437 = Class(name="raas::small::test::#10382437")
raas_small_test_FourthLevelClassK = Class(name="raas::small::test::FourthLevelClassK")
raas_small_test_DerivedUnderClassE1 = Class(name="raas::small::test::DerivedUnderClassE1")
raas_small_test_DerivedUnderClassE2 = Class(name="raas::small::test::DerivedUnderClassE2")
raas_small_test_#30911270 = Class(name="raas::small::test::#30911270")
raas_small_test_MergingE1AndE2 = Class(name="raas::small::test::MergingE1AndE2")

# raas_small_test_#19723516 class attributes and methods

# raas_small_test_ReposRoot class attributes and methods
raas_small_test_ReposRoot_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_ReposRoot_singleAttrString: Property = Property(name="singleAttrString", type=StringType)
raas_small_test_ReposRoot_multiAttrString: Property = Property(name="multiAttrString", type=StringType)
raas_small_test_ReposRoot.attributes={raas_small_test_ReposRoot_singleAttrString, raas_small_test_ReposRoot_raasRef, raas_small_test_ReposRoot_multiAttrString}

# raas_small_test_#29373817 class attributes and methods

# raas_small_test_TopClassB class attributes and methods
raas_small_test_TopClassB_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_TopClassB_multi2lowerAttrInt: Property = Property(name="multi2lowerAttrInt", type=IntegerType)
raas_small_test_TopClassB_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_TopClassB_optionalAttrInt: Property = Property(name="optionalAttrInt", type=IntegerType)
raas_small_test_TopClassB.attributes={raas_small_test_TopClassB_singleAttrInt, raas_small_test_TopClassB_optionalAttrInt, raas_small_test_TopClassB_multi2lowerAttrInt, raas_small_test_TopClassB_raasRef}

# raas_small_test_#7345254 class attributes and methods

# raas_small_test_#11832905 class attributes and methods

# raas_small_test_TopClassM class attributes and methods
raas_small_test_TopClassM_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_TopClassM.attributes={raas_small_test_TopClassM_singleAttrInt}

# raas_small_test_TopClassA class attributes and methods
raas_small_test_TopClassA_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_TopClassA.attributes={raas_small_test_TopClassA_raasRef}

# raas_small_test_#5656663 class attributes and methods

# raas_small_test_#16551649 class attributes and methods

# raas_small_test_TopClassC class attributes and methods
raas_small_test_TopClassC_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_TopClassC_multi2lowerAttrInt: Property = Property(name="multi2lowerAttrInt", type=IntegerType)
raas_small_test_TopClassC_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_TopClassC_optionalAttrInt: Property = Property(name="optionalAttrInt", type=IntegerType)
raas_small_test_TopClassC.attributes={raas_small_test_TopClassC_raasRef, raas_small_test_TopClassC_singleAttrInt, raas_small_test_TopClassC_multi2lowerAttrInt, raas_small_test_TopClassC_optionalAttrInt}

# raas_small_test_TopClassD class attributes and methods
raas_small_test_TopClassD_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_TopClassD_optionalAttrInt: Property = Property(name="optionalAttrInt", type=IntegerType)
raas_small_test_TopClassD_optionalTimeZone: Property = Property(name="optionalTimeZone", type=StringType)
raas_small_test_TopClassD_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_TopClassD_multi2lowerAttrInt: Property = Property(name="multi2lowerAttrInt", type=IntegerType)
raas_small_test_TopClassD.attributes={raas_small_test_TopClassD_optionalTimeZone, raas_small_test_TopClassD_singleAttrInt, raas_small_test_TopClassD_optionalAttrInt, raas_small_test_TopClassD_raasRef, raas_small_test_TopClassD_multi2lowerAttrInt}

# raas_small_test_UnderClassE class attributes and methods
raas_small_test_UnderClassE_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_UnderClassE.attributes={raas_small_test_UnderClassE_raasRef}

# raas_small_test_UnderClassF class attributes and methods
raas_small_test_UnderClassF_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_UnderClassF_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_UnderClassF.attributes={raas_small_test_UnderClassF_singleAttrInt, raas_small_test_UnderClassF_raasRef}

# raas_small_test_ThirdLevelClassJ class attributes and methods
raas_small_test_ThirdLevelClassJ_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_ThirdLevelClassJ_multi2lowerAttrInt: Property = Property(name="multi2lowerAttrInt", type=IntegerType)
raas_small_test_ThirdLevelClassJ_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_ThirdLevelClassJ_optionalAttrInt: Property = Property(name="optionalAttrInt", type=IntegerType)
raas_small_test_ThirdLevelClassJ.attributes={raas_small_test_ThirdLevelClassJ_raasRef, raas_small_test_ThirdLevelClassJ_multi2lowerAttrInt, raas_small_test_ThirdLevelClassJ_singleAttrInt, raas_small_test_ThirdLevelClassJ_optionalAttrInt}

# raas_small_test_#10382437 class attributes and methods

# raas_small_test_FourthLevelClassK class attributes and methods
raas_small_test_FourthLevelClassK_multi2lowerAttrInt: Property = Property(name="multi2lowerAttrInt", type=IntegerType)
raas_small_test_FourthLevelClassK_singleAttrInt: Property = Property(name="singleAttrInt", type=IntegerType)
raas_small_test_FourthLevelClassK_optionalAttrInt: Property = Property(name="optionalAttrInt", type=IntegerType)
raas_small_test_FourthLevelClassK_raasRef: Property = Property(name="raasRef", type=StringType)
raas_small_test_FourthLevelClassK.attributes={raas_small_test_FourthLevelClassK_multi2lowerAttrInt, raas_small_test_FourthLevelClassK_raasRef, raas_small_test_FourthLevelClassK_singleAttrInt, raas_small_test_FourthLevelClassK_optionalAttrInt}

# raas_small_test_DerivedUnderClassE1 class attributes and methods

# raas_small_test_DerivedUnderClassE2 class attributes and methods

# raas_small_test_#30911270 class attributes and methods

# raas_small_test_MergingE1AndE2 class attributes and methods
raas_small_test_MergingE1AndE2_optionalAttrString: Property = Property(name="optionalAttrString", type=StringType)
raas_small_test_MergingE1AndE2.attributes={raas_small_test_MergingE1AndE2_optionalAttrString}

# Relationships
optionalContainClassB1: BinaryAssociation = BinaryAssociation(
    name="optionalContainClassB1",
    ends={
        Property(name="raas_small_test_#19723516", type=raas_small_test_ReposRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ReposRoot2", type=raas_small_test_#19723516, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
multiContainClassA0: BinaryAssociation = BinaryAssociation(
    name="multiContainClassA0",
    ends={
        Property(name="raas_small_test_#29373817", type=raas_small_test_ReposRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ReposRoot", type=raas_small_test_#29373817, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleContainClassC3: BinaryAssociation = BinaryAssociation(
    name="singleContainClassC3",
    ends={
        Property(name="raas_small_test_#7345254", type=raas_small_test_ReposRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ReposRoot4", type=raas_small_test_#7345254, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiRefClassD5: BinaryAssociation = BinaryAssociation(
    name="multiRefClassD5",
    ends={
        Property(name="raas_small_test_#11832905", type=raas_small_test_ReposRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ReposRoot6", type=raas_small_test_#11832905, multiplicity=Multiplicity(0, 9999))
    }
)
singleNonContainClassM7: BinaryAssociation = BinaryAssociation(
    name="singleNonContainClassM7",
    ends={
        Property(name="raas_small_test_TopClassM", type=raas_small_test_ReposRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ReposRoot8", type=raas_small_test_TopClassM, multiplicity=Multiplicity(1, 1))
    }
)
multiContainClassE9: BinaryAssociation = BinaryAssociation(
    name="multiContainClassE9",
    ends={
        Property(name="raas_small_test_#5656663", type=raas_small_test_TopClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_TopClassA", type=raas_small_test_#5656663, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
singleContainClassF10: BinaryAssociation = BinaryAssociation(
    name="singleContainClassF10",
    ends={
        Property(name="raas_small_test_#16551649", type=raas_small_test_TopClassA, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_TopClassA11", type=raas_small_test_#16551649, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
multiRefClassE12: BinaryAssociation = BinaryAssociation(
    name="multiRefClassE12",
    ends={
        Property(name="raas_small_test_#565666313", type=raas_small_test_TopClassB, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_TopClassB", type=raas_small_test_#5656663, multiplicity=Multiplicity(0, 9999))
    }
)
singleContainClassF14: BinaryAssociation = BinaryAssociation(
    name="singleContainClassF14",
    ends={
        Property(name="raas_small_test_#1655164915", type=raas_small_test_TopClassC, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_TopClassC", type=raas_small_test_#16551649, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
optionalContainClassK16: BinaryAssociation = BinaryAssociation(
    name="optionalContainClassK16",
    ends={
        Property(name="raas_small_test_#10382437", type=raas_small_test_ThirdLevelClassJ, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_ThirdLevelClassJ", type=raas_small_test_#10382437, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
singleRefClassD17: BinaryAssociation = BinaryAssociation(
    name="singleRefClassD17",
    ends={
        Property(name="raas_small_test_#1183290518", type=raas_small_test_DerivedUnderClassE1, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_DerivedUnderClassE1", type=raas_small_test_#11832905, multiplicity=Multiplicity(1, 1))
    }
)
multiContainClassJ19: BinaryAssociation = BinaryAssociation(
    name="multiContainClassJ19",
    ends={
        Property(name="raas_small_test_#30911270", type=raas_small_test_DerivedUnderClassE2, multiplicity=Multiplicity(1, 1)),
        Property(name="raas_small_test_DerivedUnderClassE2", type=raas_small_test_#30911270, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_raas_small_test_DerivedUnderClassE1_raas_small_test_UnderClassE = Generalization(general=raas_small_test_UnderClassE, specific=raas_small_test_DerivedUnderClassE1)
gen_raas_small_test_DerivedUnderClassE2_raas_small_test_UnderClassE = Generalization(general=raas_small_test_UnderClassE, specific=raas_small_test_DerivedUnderClassE2)
gen_raas_small_test_TopClassM_raas_small_test_UnderClassE = Generalization(general=raas_small_test_UnderClassE, specific=raas_small_test_TopClassM)
gen_raas_small_test_MergingE1AndE2_raas_small_test_DerivedUnderClassE1 = Generalization(general=raas_small_test_DerivedUnderClassE1, specific=raas_small_test_MergingE1AndE2)
gen_raas_small_test_MergingE1AndE2_raas_small_test_DerivedUnderClassE2 = Generalization(general=raas_small_test_DerivedUnderClassE2, specific=raas_small_test_MergingE1AndE2)

# Domain Model
domain_model = DomainModel(
    name="raas_small_test",
    types={raas_small_test_#19723516, raas_small_test_ReposRoot, raas_small_test_#29373817, raas_small_test_TopClassB, raas_small_test_#7345254, raas_small_test_#11832905, raas_small_test_TopClassM, raas_small_test_TopClassA, raas_small_test_#5656663, raas_small_test_#16551649, raas_small_test_TopClassC, raas_small_test_TopClassD, raas_small_test_UnderClassE, raas_small_test_UnderClassF, raas_small_test_ThirdLevelClassJ, raas_small_test_#10382437, raas_small_test_FourthLevelClassK, raas_small_test_DerivedUnderClassE1, raas_small_test_DerivedUnderClassE2, raas_small_test_#30911270, raas_small_test_MergingE1AndE2},
    associations={optionalContainClassB1, multiContainClassA0, singleContainClassC3, multiRefClassD5, singleNonContainClassM7, multiContainClassE9, singleContainClassF10, multiRefClassE12, singleContainClassF14, optionalContainClassK16, singleRefClassD17, multiContainClassJ19},
    generalizations={gen_raas_small_test_DerivedUnderClassE1_raas_small_test_UnderClassE, gen_raas_small_test_DerivedUnderClassE2_raas_small_test_UnderClassE, gen_raas_small_test_TopClassM_raas_small_test_UnderClassE, gen_raas_small_test_MergingE1AndE2_raas_small_test_DerivedUnderClassE1, gen_raas_small_test_MergingE1AndE2_raas_small_test_DerivedUnderClassE2},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)