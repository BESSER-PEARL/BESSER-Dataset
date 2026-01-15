from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class MethodReference:

    pass
class ast_ExpressionMethodReference(MethodReference):

    pass
class ast_TypeMethodReference(MethodReference):

    pass
class ast_CreationReference(MethodReference):

    pass
class ast_SuperMethodReference(MethodReference):

    pass
class AbstractTypeDeclaration:

    pass
class ast_EnumDeclaration(AbstractTypeDeclaration):

    pass
class ast_AnnotationTypeDeclaration(AbstractTypeDeclaration):

    pass
class ast_TypeDeclaration(AbstractTypeDeclaration):

    def __init__(self, interface: bool, ast_TypeDeclaration306: "ast_SimpleName" = None, ast_TypeDeclaration309: set["ast_TypeParameter"] = None, ast_TypeDeclaration312: "ast_Type" = None, ast_TypeDeclaration315: set["ast_Type"] = None, ast_TypeDeclaration318: set["ast_BodyDeclaration"] = None, ast_TypeDeclaration: "ast_Javadoc" = None, ast_TypeDeclaration303: set["ast_IExtendedModifier"] = None):
        self.interface = interface
        self.ast_TypeDeclaration306 = ast_TypeDeclaration306
        self.ast_TypeDeclaration309 = ast_TypeDeclaration309 if ast_TypeDeclaration309 is not None else set()
        self.ast_TypeDeclaration312 = ast_TypeDeclaration312
        self.ast_TypeDeclaration315 = ast_TypeDeclaration315 if ast_TypeDeclaration315 is not None else set()
        self.ast_TypeDeclaration318 = ast_TypeDeclaration318 if ast_TypeDeclaration318 is not None else set()
        self.ast_TypeDeclaration = ast_TypeDeclaration
        self.ast_TypeDeclaration303 = ast_TypeDeclaration303 if ast_TypeDeclaration303 is not None else set()
        
    @property
    def interface(self) -> bool:
        return self.__interface

    @interface.setter
    def interface(self, interface: bool):
        self.__interface = interface

    @property
    def ast_TypeDeclaration303(self):
        return self.__ast_TypeDeclaration303

    @ast_TypeDeclaration303.setter
    def ast_TypeDeclaration303(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration303", None)
        self.__ast_TypeDeclaration303 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_IExtendedModifier304"):
                    opp_val = getattr(item, "ast_IExtendedModifier304", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_IExtendedModifier304", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_IExtendedModifier304"):
                    opp_val = getattr(item, "ast_IExtendedModifier304", None)
                    
                    setattr(item, "ast_IExtendedModifier304", self)
                    

    @property
    def ast_TypeDeclaration(self):
        return self.__ast_TypeDeclaration

    @ast_TypeDeclaration.setter
    def ast_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration", None)
        self.__ast_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Javadoc301"):
                opp_val = getattr(old_value, "ast_Javadoc301", None)
                if opp_val == self:
                    setattr(old_value, "ast_Javadoc301", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Javadoc301"):
                opp_val = getattr(value, "ast_Javadoc301", None)
                setattr(value, "ast_Javadoc301", self)

    @property
    def ast_TypeDeclaration312(self):
        return self.__ast_TypeDeclaration312

    @ast_TypeDeclaration312.setter
    def ast_TypeDeclaration312(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration312", None)
        self.__ast_TypeDeclaration312 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type313"):
                opp_val = getattr(old_value, "ast_Type313", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type313", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type313"):
                opp_val = getattr(value, "ast_Type313", None)
                setattr(value, "ast_Type313", self)

    @property
    def ast_TypeDeclaration309(self):
        return self.__ast_TypeDeclaration309

    @ast_TypeDeclaration309.setter
    def ast_TypeDeclaration309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration309", None)
        self.__ast_TypeDeclaration309 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_TypeParameter310"):
                    opp_val = getattr(item, "ast_TypeParameter310", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_TypeParameter310", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_TypeParameter310"):
                    opp_val = getattr(item, "ast_TypeParameter310", None)
                    
                    setattr(item, "ast_TypeParameter310", self)
                    

    @property
    def ast_TypeDeclaration306(self):
        return self.__ast_TypeDeclaration306

    @ast_TypeDeclaration306.setter
    def ast_TypeDeclaration306(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration306", None)
        self.__ast_TypeDeclaration306 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SimpleName307"):
                opp_val = getattr(old_value, "ast_SimpleName307", None)
                if opp_val == self:
                    setattr(old_value, "ast_SimpleName307", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SimpleName307"):
                opp_val = getattr(value, "ast_SimpleName307", None)
                setattr(value, "ast_SimpleName307", self)

    @property
    def ast_TypeDeclaration315(self):
        return self.__ast_TypeDeclaration315

    @ast_TypeDeclaration315.setter
    def ast_TypeDeclaration315(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration315", None)
        self.__ast_TypeDeclaration315 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Type316"):
                    opp_val = getattr(item, "ast_Type316", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Type316", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Type316"):
                    opp_val = getattr(item, "ast_Type316", None)
                    
                    setattr(item, "ast_Type316", self)
                    

    @property
    def ast_TypeDeclaration318(self):
        return self.__ast_TypeDeclaration318

    @ast_TypeDeclaration318.setter
    def ast_TypeDeclaration318(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TypeDeclaration__ast_TypeDeclaration318", None)
        self.__ast_TypeDeclaration318 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_BodyDeclaration319"):
                    opp_val = getattr(item, "ast_BodyDeclaration319", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_BodyDeclaration319", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_BodyDeclaration319"):
                    opp_val = getattr(item, "ast_BodyDeclaration319", None)
                    
                    setattr(item, "ast_BodyDeclaration319", self)
                    

class VariableDeclaration:

    pass
class Name:

    pass
class ast_QualifiedName(Name):

    pass
class AnnotatableType:

    pass
class ast_QualifiedType(AnnotatableType):

    pass
class ast_SimpleType(AnnotatableType):

    pass
class ast_NameQualifiedType(AnnotatableType):

    pass
class ast_WildcardType(AnnotatableType):

    def __init__(self, upperBound: bool, ast_WildcardType: set["ast_Annotation"] = None, ast_WildcardType430: "ast_Type" = None):
        self.upperBound = upperBound
        self.ast_WildcardType = ast_WildcardType if ast_WildcardType is not None else set()
        self.ast_WildcardType430 = ast_WildcardType430
        
    @property
    def upperBound(self) -> bool:
        return self.__upperBound

    @upperBound.setter
    def upperBound(self, upperBound: bool):
        self.__upperBound = upperBound

    @property
    def ast_WildcardType(self):
        return self.__ast_WildcardType

    @ast_WildcardType.setter
    def ast_WildcardType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_WildcardType__ast_WildcardType", None)
        self.__ast_WildcardType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Annotation428"):
                    opp_val = getattr(item, "ast_Annotation428", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Annotation428", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Annotation428"):
                    opp_val = getattr(item, "ast_Annotation428", None)
                    
                    setattr(item, "ast_Annotation428", self)
                    

    @property
    def ast_WildcardType430(self):
        return self.__ast_WildcardType430

    @ast_WildcardType430.setter
    def ast_WildcardType430(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_WildcardType__ast_WildcardType430", None)
        self.__ast_WildcardType430 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type431"):
                opp_val = getattr(old_value, "ast_Type431", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type431", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type431"):
                opp_val = getattr(value, "ast_Type431", None)
                setattr(value, "ast_Type431", self)

class ast_PrimitiveType(AnnotatableType):

    def __init__(self, primitiveTypeCode: str, ast_PrimitiveType: set["ast_Annotation"] = None):
        self.primitiveTypeCode = primitiveTypeCode
        self.ast_PrimitiveType = ast_PrimitiveType if ast_PrimitiveType is not None else set()
        
    @property
    def primitiveTypeCode(self) -> str:
        return self.__primitiveTypeCode

    @primitiveTypeCode.setter
    def primitiveTypeCode(self, primitiveTypeCode: str):
        self.__primitiveTypeCode = primitiveTypeCode

    @property
    def ast_PrimitiveType(self):
        return self.__ast_PrimitiveType

    @ast_PrimitiveType.setter
    def ast_PrimitiveType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PrimitiveType__ast_PrimitiveType", None)
        self.__ast_PrimitiveType = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Annotation219"):
                    opp_val = getattr(item, "ast_Annotation219", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Annotation219", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Annotation219"):
                    opp_val = getattr(item, "ast_Annotation219", None)
                    
                    setattr(item, "ast_Annotation219", self)
                    

class Comment:

    pass
class ast_BlockComment(Comment):

    pass
class ast_LineComment(Comment):

    pass
class ast_VariableDeclarationFragment(VariableDeclaration):

    pass
class ast_Javadoc(Comment):

    pass
class BodyDeclaration:

    pass
class ast_AnnotationTypeMemberDeclaration(BodyDeclaration):

    pass
class ast_EnumConstantDeclaration(BodyDeclaration):

    pass
class ast_MethodDeclaration(BodyDeclaration):

    def __init__(self, constructor: bool, ast_MethodDeclaration: "ast_Javadoc" = None, ast_MethodDeclaration165: set["ast_IExtendedModifier"] = None, ast_MethodDeclaration176: "ast_Type" = None, ast_MethodDeclaration179: "ast_SimpleName" = None, ast_MethodDeclaration182: set["ast_SingleVariableDeclaration"] = None, ast_MethodDeclaration185: set["ast_Dimension"] = None, ast_MethodDeclaration188: set["ast_Type"] = None, ast_MethodDeclaration191: "ast_Block" = None, ast_MethodDeclaration168: set["ast_TypeParameter"] = None, ast_MethodDeclaration170: "ast_Type" = None, ast_MethodDeclaration173: "ast_SimpleName" = None):
        self.constructor = constructor
        self.ast_MethodDeclaration = ast_MethodDeclaration
        self.ast_MethodDeclaration165 = ast_MethodDeclaration165 if ast_MethodDeclaration165 is not None else set()
        self.ast_MethodDeclaration176 = ast_MethodDeclaration176
        self.ast_MethodDeclaration179 = ast_MethodDeclaration179
        self.ast_MethodDeclaration182 = ast_MethodDeclaration182 if ast_MethodDeclaration182 is not None else set()
        self.ast_MethodDeclaration185 = ast_MethodDeclaration185 if ast_MethodDeclaration185 is not None else set()
        self.ast_MethodDeclaration188 = ast_MethodDeclaration188 if ast_MethodDeclaration188 is not None else set()
        self.ast_MethodDeclaration191 = ast_MethodDeclaration191
        self.ast_MethodDeclaration168 = ast_MethodDeclaration168 if ast_MethodDeclaration168 is not None else set()
        self.ast_MethodDeclaration170 = ast_MethodDeclaration170
        self.ast_MethodDeclaration173 = ast_MethodDeclaration173
        
    @property
    def constructor(self) -> bool:
        return self.__constructor

    @constructor.setter
    def constructor(self, constructor: bool):
        self.__constructor = constructor

    @property
    def ast_MethodDeclaration(self):
        return self.__ast_MethodDeclaration

    @ast_MethodDeclaration.setter
    def ast_MethodDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration", None)
        self.__ast_MethodDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Javadoc163"):
                opp_val = getattr(old_value, "ast_Javadoc163", None)
                if opp_val == self:
                    setattr(old_value, "ast_Javadoc163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Javadoc163"):
                opp_val = getattr(value, "ast_Javadoc163", None)
                setattr(value, "ast_Javadoc163", self)

    @property
    def ast_MethodDeclaration165(self):
        return self.__ast_MethodDeclaration165

    @ast_MethodDeclaration165.setter
    def ast_MethodDeclaration165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration165", None)
        self.__ast_MethodDeclaration165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_IExtendedModifier166"):
                    opp_val = getattr(item, "ast_IExtendedModifier166", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_IExtendedModifier166", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_IExtendedModifier166"):
                    opp_val = getattr(item, "ast_IExtendedModifier166", None)
                    
                    setattr(item, "ast_IExtendedModifier166", self)
                    

    @property
    def ast_MethodDeclaration170(self):
        return self.__ast_MethodDeclaration170

    @ast_MethodDeclaration170.setter
    def ast_MethodDeclaration170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration170", None)
        self.__ast_MethodDeclaration170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type171"):
                opp_val = getattr(old_value, "ast_Type171", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type171"):
                opp_val = getattr(value, "ast_Type171", None)
                setattr(value, "ast_Type171", self)

    @property
    def ast_MethodDeclaration176(self):
        return self.__ast_MethodDeclaration176

    @ast_MethodDeclaration176.setter
    def ast_MethodDeclaration176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration176", None)
        self.__ast_MethodDeclaration176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type177"):
                opp_val = getattr(old_value, "ast_Type177", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type177"):
                opp_val = getattr(value, "ast_Type177", None)
                setattr(value, "ast_Type177", self)

    @property
    def ast_MethodDeclaration191(self):
        return self.__ast_MethodDeclaration191

    @ast_MethodDeclaration191.setter
    def ast_MethodDeclaration191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration191", None)
        self.__ast_MethodDeclaration191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Block192"):
                opp_val = getattr(old_value, "ast_Block192", None)
                if opp_val == self:
                    setattr(old_value, "ast_Block192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Block192"):
                opp_val = getattr(value, "ast_Block192", None)
                setattr(value, "ast_Block192", self)

    @property
    def ast_MethodDeclaration179(self):
        return self.__ast_MethodDeclaration179

    @ast_MethodDeclaration179.setter
    def ast_MethodDeclaration179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration179", None)
        self.__ast_MethodDeclaration179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SimpleName180"):
                opp_val = getattr(old_value, "ast_SimpleName180", None)
                if opp_val == self:
                    setattr(old_value, "ast_SimpleName180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SimpleName180"):
                opp_val = getattr(value, "ast_SimpleName180", None)
                setattr(value, "ast_SimpleName180", self)

    @property
    def ast_MethodDeclaration188(self):
        return self.__ast_MethodDeclaration188

    @ast_MethodDeclaration188.setter
    def ast_MethodDeclaration188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration188", None)
        self.__ast_MethodDeclaration188 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Type189"):
                    opp_val = getattr(item, "ast_Type189", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Type189", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Type189"):
                    opp_val = getattr(item, "ast_Type189", None)
                    
                    setattr(item, "ast_Type189", self)
                    

    @property
    def ast_MethodDeclaration168(self):
        return self.__ast_MethodDeclaration168

    @ast_MethodDeclaration168.setter
    def ast_MethodDeclaration168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration168", None)
        self.__ast_MethodDeclaration168 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_TypeParameter"):
                    opp_val = getattr(item, "ast_TypeParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_TypeParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_TypeParameter"):
                    opp_val = getattr(item, "ast_TypeParameter", None)
                    
                    setattr(item, "ast_TypeParameter", self)
                    

    @property
    def ast_MethodDeclaration182(self):
        return self.__ast_MethodDeclaration182

    @ast_MethodDeclaration182.setter
    def ast_MethodDeclaration182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration182", None)
        self.__ast_MethodDeclaration182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_SingleVariableDeclaration183"):
                    opp_val = getattr(item, "ast_SingleVariableDeclaration183", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_SingleVariableDeclaration183", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_SingleVariableDeclaration183"):
                    opp_val = getattr(item, "ast_SingleVariableDeclaration183", None)
                    
                    setattr(item, "ast_SingleVariableDeclaration183", self)
                    

    @property
    def ast_MethodDeclaration185(self):
        return self.__ast_MethodDeclaration185

    @ast_MethodDeclaration185.setter
    def ast_MethodDeclaration185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration185", None)
        self.__ast_MethodDeclaration185 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Dimension186"):
                    opp_val = getattr(item, "ast_Dimension186", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Dimension186", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Dimension186"):
                    opp_val = getattr(item, "ast_Dimension186", None)
                    
                    setattr(item, "ast_Dimension186", self)
                    

    @property
    def ast_MethodDeclaration173(self):
        return self.__ast_MethodDeclaration173

    @ast_MethodDeclaration173.setter
    def ast_MethodDeclaration173(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodDeclaration__ast_MethodDeclaration173", None)
        self.__ast_MethodDeclaration173 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SimpleName174"):
                opp_val = getattr(old_value, "ast_SimpleName174", None)
                if opp_val == self:
                    setattr(old_value, "ast_SimpleName174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SimpleName174"):
                opp_val = getattr(value, "ast_SimpleName174", None)
                setattr(value, "ast_SimpleName174", self)

class ast_Initializer(BodyDeclaration):

    pass
class ast_FieldDeclaration(BodyDeclaration):

    pass
class ast_AbstractTypeDeclaration(BodyDeclaration):

    pass
class ast_SingleVariableDeclaration(VariableDeclaration):

    def __init__(self, varargs: bool, ast_SingleVariableDeclaration: "ast_CatchClause" = None, ast_SingleVariableDeclaration183: "ast_MethodDeclaration" = None, ast_SingleVariableDeclaration233: set["ast_IExtendedModifier"] = None, ast_SingleVariableDeclaration236: "ast_Type" = None, ast_SingleVariableDeclaration239: set["ast_Annotation"] = None, ast_SingleVariableDeclaration242: "ast_SimpleName" = None, ast_SingleVariableDeclaration245: set["ast_Dimension"] = None, ast_SingleVariableDeclaration248: "ast_Expression" = None, ast_SingleVariableDeclaration367: "ast_EnhancedForStatement" = None):
        self.varargs = varargs
        self.ast_SingleVariableDeclaration = ast_SingleVariableDeclaration
        self.ast_SingleVariableDeclaration183 = ast_SingleVariableDeclaration183
        self.ast_SingleVariableDeclaration233 = ast_SingleVariableDeclaration233 if ast_SingleVariableDeclaration233 is not None else set()
        self.ast_SingleVariableDeclaration236 = ast_SingleVariableDeclaration236
        self.ast_SingleVariableDeclaration239 = ast_SingleVariableDeclaration239 if ast_SingleVariableDeclaration239 is not None else set()
        self.ast_SingleVariableDeclaration242 = ast_SingleVariableDeclaration242
        self.ast_SingleVariableDeclaration245 = ast_SingleVariableDeclaration245 if ast_SingleVariableDeclaration245 is not None else set()
        self.ast_SingleVariableDeclaration248 = ast_SingleVariableDeclaration248
        self.ast_SingleVariableDeclaration367 = ast_SingleVariableDeclaration367
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def ast_SingleVariableDeclaration248(self):
        return self.__ast_SingleVariableDeclaration248

    @ast_SingleVariableDeclaration248.setter
    def ast_SingleVariableDeclaration248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration248", None)
        self.__ast_SingleVariableDeclaration248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression249"):
                opp_val = getattr(old_value, "ast_Expression249", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression249", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression249"):
                opp_val = getattr(value, "ast_Expression249", None)
                setattr(value, "ast_Expression249", self)

    @property
    def ast_SingleVariableDeclaration183(self):
        return self.__ast_SingleVariableDeclaration183

    @ast_SingleVariableDeclaration183.setter
    def ast_SingleVariableDeclaration183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration183", None)
        self.__ast_SingleVariableDeclaration183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodDeclaration182"):
                opp_val = getattr(old_value, "ast_MethodDeclaration182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodDeclaration182"):
                opp_val = getattr(value, "ast_MethodDeclaration182", None)
                if opp_val is None:
                    setattr(value, "ast_MethodDeclaration182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_SingleVariableDeclaration367(self):
        return self.__ast_SingleVariableDeclaration367

    @ast_SingleVariableDeclaration367.setter
    def ast_SingleVariableDeclaration367(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration367", None)
        self.__ast_SingleVariableDeclaration367 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EnhancedForStatement"):
                opp_val = getattr(old_value, "ast_EnhancedForStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_EnhancedForStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EnhancedForStatement"):
                opp_val = getattr(value, "ast_EnhancedForStatement", None)
                setattr(value, "ast_EnhancedForStatement", self)

    @property
    def ast_SingleVariableDeclaration239(self):
        return self.__ast_SingleVariableDeclaration239

    @ast_SingleVariableDeclaration239.setter
    def ast_SingleVariableDeclaration239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration239", None)
        self.__ast_SingleVariableDeclaration239 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Annotation240"):
                    opp_val = getattr(item, "ast_Annotation240", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Annotation240", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Annotation240"):
                    opp_val = getattr(item, "ast_Annotation240", None)
                    
                    setattr(item, "ast_Annotation240", self)
                    

    @property
    def ast_SingleVariableDeclaration(self):
        return self.__ast_SingleVariableDeclaration

    @ast_SingleVariableDeclaration.setter
    def ast_SingleVariableDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration", None)
        self.__ast_SingleVariableDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_CatchClause"):
                opp_val = getattr(old_value, "ast_CatchClause", None)
                if opp_val == self:
                    setattr(old_value, "ast_CatchClause", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_CatchClause"):
                opp_val = getattr(value, "ast_CatchClause", None)
                setattr(value, "ast_CatchClause", self)

    @property
    def ast_SingleVariableDeclaration245(self):
        return self.__ast_SingleVariableDeclaration245

    @ast_SingleVariableDeclaration245.setter
    def ast_SingleVariableDeclaration245(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration245", None)
        self.__ast_SingleVariableDeclaration245 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Dimension246"):
                    opp_val = getattr(item, "ast_Dimension246", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Dimension246", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Dimension246"):
                    opp_val = getattr(item, "ast_Dimension246", None)
                    
                    setattr(item, "ast_Dimension246", self)
                    

    @property
    def ast_SingleVariableDeclaration236(self):
        return self.__ast_SingleVariableDeclaration236

    @ast_SingleVariableDeclaration236.setter
    def ast_SingleVariableDeclaration236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration236", None)
        self.__ast_SingleVariableDeclaration236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type237"):
                opp_val = getattr(old_value, "ast_Type237", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type237"):
                opp_val = getattr(value, "ast_Type237", None)
                setattr(value, "ast_Type237", self)

    @property
    def ast_SingleVariableDeclaration242(self):
        return self.__ast_SingleVariableDeclaration242

    @ast_SingleVariableDeclaration242.setter
    def ast_SingleVariableDeclaration242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration242", None)
        self.__ast_SingleVariableDeclaration242 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SimpleName243"):
                opp_val = getattr(old_value, "ast_SimpleName243", None)
                if opp_val == self:
                    setattr(old_value, "ast_SimpleName243", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SimpleName243"):
                opp_val = getattr(value, "ast_SimpleName243", None)
                setattr(value, "ast_SimpleName243", self)

    @property
    def ast_SingleVariableDeclaration233(self):
        return self.__ast_SingleVariableDeclaration233

    @ast_SingleVariableDeclaration233.setter
    def ast_SingleVariableDeclaration233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SingleVariableDeclaration__ast_SingleVariableDeclaration233", None)
        self.__ast_SingleVariableDeclaration233 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_IExtendedModifier234"):
                    opp_val = getattr(item, "ast_IExtendedModifier234", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_IExtendedModifier234", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_IExtendedModifier234"):
                    opp_val = getattr(item, "ast_IExtendedModifier234", None)
                    
                    setattr(item, "ast_IExtendedModifier234", self)
                    

class Statement:

    pass
class ast_ConstructorInvocation(Statement):

    pass
class ast_SwitchCase(Statement):

    pass
class ast_ExpressionStatement(Statement):

    pass
class ast_EnhancedForStatement(Statement):

    pass
class ast_ContinueStatement(Statement):

    pass
class ast_LabeledStatement(Statement):

    pass
class ast_VariableDeclarationStatement(Statement):

    pass
class ast_TryStatement(Statement):

    pass
class ast_EmptyStatement(Statement):

    pass
class ast_Block(Statement):

    pass
class ast_IfStatement(Statement):

    pass
class ast_ThrowStatement(Statement):

    pass
class ast_BreakStatement(Statement):

    pass
class ast_ReturnStatement(Statement):

    pass
class ast_ForStatement(Statement):

    pass
class ast_DoStatement(Statement):

    pass
class ast_SwitchStatement(Statement):

    pass
class ast_SynchronizedStatement(Statement):

    pass
class ast_TypeDeclarationStatement(Statement):

    pass
class ast_SuperConstructorInvocation(Statement):

    pass
class ast_WhileStatement(Statement):

    pass
class ast_AssertStatement(Statement):

    pass
class Type:

    pass
class ast_IntersectionType(Type):

    pass
class ast_ParameterizedType(Type):

    pass
class ast_AnnotatableType(Type):

    pass
class ast_UnionType(Type):

    pass
class ast_ArrayType(Type):

    pass
class ast_SimpleName(Name):

    def __init__(self, identifier: str, ast_SimpleName: "ast_MemberRef" = None, ast_SimpleName17: "ast_MethodRef" = None, ast_SimpleName52: "ast_BreakStatement" = None, ast_SimpleName95: "ast_ContinueStatement" = None, ast_SimpleName107: "ast_FieldAccess" = None, ast_SimpleName158: "ast_LabeledStatement" = None, ast_SimpleName180: "ast_MethodDeclaration" = None, ast_SimpleName174: "ast_MethodDeclaration" = None, ast_SimpleName200: "ast_MethodInvocation" = None, ast_SimpleName224: "ast_QualifiedName" = None, ast_SimpleName243: "ast_SingleVariableDeclaration" = None, ast_SimpleName262: "ast_SuperFieldAccess" = None, ast_SimpleName270: "ast_SuperMethodInvocation" = None, ast_SimpleName307: "ast_TypeDeclaration" = None, ast_SimpleName335: "ast_VariableDeclarationFragment" = None, ast_SimpleName365: "ast_MethodRefParameter" = None, ast_SimpleName398: "ast_EnumConstantDeclaration" = None, ast_SimpleName410: "ast_TypeParameter" = None, ast_SimpleName381: "ast_EnumDeclaration" = None, ast_SimpleName434: "ast_MemberValuePair" = None, ast_SimpleName445: "ast_AnnotationTypeDeclaration" = None, ast_SimpleName459: "ast_AnnotationTypeMemberDeclaration" = None, ast_SimpleName426: "ast_QualifiedType" = None, ast_SimpleName480: "ast_NameQualifiedType" = None, ast_SimpleName493: "ast_ExpressionMethodReference" = None, ast_SimpleName501: "ast_SuperMethodReference" = None, ast_SimpleName509: "ast_TypeMethodReference" = None):
        self.identifier = identifier
        self.ast_SimpleName = ast_SimpleName
        self.ast_SimpleName17 = ast_SimpleName17
        self.ast_SimpleName52 = ast_SimpleName52
        self.ast_SimpleName95 = ast_SimpleName95
        self.ast_SimpleName107 = ast_SimpleName107
        self.ast_SimpleName158 = ast_SimpleName158
        self.ast_SimpleName180 = ast_SimpleName180
        self.ast_SimpleName174 = ast_SimpleName174
        self.ast_SimpleName200 = ast_SimpleName200
        self.ast_SimpleName224 = ast_SimpleName224
        self.ast_SimpleName243 = ast_SimpleName243
        self.ast_SimpleName262 = ast_SimpleName262
        self.ast_SimpleName270 = ast_SimpleName270
        self.ast_SimpleName307 = ast_SimpleName307
        self.ast_SimpleName335 = ast_SimpleName335
        self.ast_SimpleName365 = ast_SimpleName365
        self.ast_SimpleName398 = ast_SimpleName398
        self.ast_SimpleName410 = ast_SimpleName410
        self.ast_SimpleName381 = ast_SimpleName381
        self.ast_SimpleName434 = ast_SimpleName434
        self.ast_SimpleName445 = ast_SimpleName445
        self.ast_SimpleName459 = ast_SimpleName459
        self.ast_SimpleName426 = ast_SimpleName426
        self.ast_SimpleName480 = ast_SimpleName480
        self.ast_SimpleName493 = ast_SimpleName493
        self.ast_SimpleName501 = ast_SimpleName501
        self.ast_SimpleName509 = ast_SimpleName509
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def ast_SimpleName410(self):
        return self.__ast_SimpleName410

    @ast_SimpleName410.setter
    def ast_SimpleName410(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName410", None)
        self.__ast_SimpleName410 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_TypeParameter409"):
                opp_val = getattr(old_value, "ast_TypeParameter409", None)
                if opp_val == self:
                    setattr(old_value, "ast_TypeParameter409", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_TypeParameter409"):
                opp_val = getattr(value, "ast_TypeParameter409", None)
                setattr(value, "ast_TypeParameter409", self)

    @property
    def ast_SimpleName17(self):
        return self.__ast_SimpleName17

    @ast_SimpleName17.setter
    def ast_SimpleName17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName17", None)
        self.__ast_SimpleName17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodRef16"):
                opp_val = getattr(old_value, "ast_MethodRef16", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodRef16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodRef16"):
                opp_val = getattr(value, "ast_MethodRef16", None)
                setattr(value, "ast_MethodRef16", self)

    @property
    def ast_SimpleName180(self):
        return self.__ast_SimpleName180

    @ast_SimpleName180.setter
    def ast_SimpleName180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName180", None)
        self.__ast_SimpleName180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodDeclaration179"):
                opp_val = getattr(old_value, "ast_MethodDeclaration179", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodDeclaration179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodDeclaration179"):
                opp_val = getattr(value, "ast_MethodDeclaration179", None)
                setattr(value, "ast_MethodDeclaration179", self)

    @property
    def ast_SimpleName445(self):
        return self.__ast_SimpleName445

    @ast_SimpleName445.setter
    def ast_SimpleName445(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName445", None)
        self.__ast_SimpleName445 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_AnnotationTypeDeclaration444"):
                opp_val = getattr(old_value, "ast_AnnotationTypeDeclaration444", None)
                if opp_val == self:
                    setattr(old_value, "ast_AnnotationTypeDeclaration444", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_AnnotationTypeDeclaration444"):
                opp_val = getattr(value, "ast_AnnotationTypeDeclaration444", None)
                setattr(value, "ast_AnnotationTypeDeclaration444", self)

    @property
    def ast_SimpleName434(self):
        return self.__ast_SimpleName434

    @ast_SimpleName434.setter
    def ast_SimpleName434(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName434", None)
        self.__ast_SimpleName434 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MemberValuePair433"):
                opp_val = getattr(old_value, "ast_MemberValuePair433", None)
                if opp_val == self:
                    setattr(old_value, "ast_MemberValuePair433", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MemberValuePair433"):
                opp_val = getattr(value, "ast_MemberValuePair433", None)
                setattr(value, "ast_MemberValuePair433", self)

    @property
    def ast_SimpleName200(self):
        return self.__ast_SimpleName200

    @ast_SimpleName200.setter
    def ast_SimpleName200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName200", None)
        self.__ast_SimpleName200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodInvocation199"):
                opp_val = getattr(old_value, "ast_MethodInvocation199", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodInvocation199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodInvocation199"):
                opp_val = getattr(value, "ast_MethodInvocation199", None)
                setattr(value, "ast_MethodInvocation199", self)

    @property
    def ast_SimpleName335(self):
        return self.__ast_SimpleName335

    @ast_SimpleName335.setter
    def ast_SimpleName335(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName335", None)
        self.__ast_SimpleName335 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_VariableDeclarationFragment334"):
                opp_val = getattr(old_value, "ast_VariableDeclarationFragment334", None)
                if opp_val == self:
                    setattr(old_value, "ast_VariableDeclarationFragment334", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_VariableDeclarationFragment334"):
                opp_val = getattr(value, "ast_VariableDeclarationFragment334", None)
                setattr(value, "ast_VariableDeclarationFragment334", self)

    @property
    def ast_SimpleName398(self):
        return self.__ast_SimpleName398

    @ast_SimpleName398.setter
    def ast_SimpleName398(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName398", None)
        self.__ast_SimpleName398 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EnumConstantDeclaration397"):
                opp_val = getattr(old_value, "ast_EnumConstantDeclaration397", None)
                if opp_val == self:
                    setattr(old_value, "ast_EnumConstantDeclaration397", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EnumConstantDeclaration397"):
                opp_val = getattr(value, "ast_EnumConstantDeclaration397", None)
                setattr(value, "ast_EnumConstantDeclaration397", self)

    @property
    def ast_SimpleName270(self):
        return self.__ast_SimpleName270

    @ast_SimpleName270.setter
    def ast_SimpleName270(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName270", None)
        self.__ast_SimpleName270 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SuperMethodInvocation269"):
                opp_val = getattr(old_value, "ast_SuperMethodInvocation269", None)
                if opp_val == self:
                    setattr(old_value, "ast_SuperMethodInvocation269", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SuperMethodInvocation269"):
                opp_val = getattr(value, "ast_SuperMethodInvocation269", None)
                setattr(value, "ast_SuperMethodInvocation269", self)

    @property
    def ast_SimpleName158(self):
        return self.__ast_SimpleName158

    @ast_SimpleName158.setter
    def ast_SimpleName158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName158", None)
        self.__ast_SimpleName158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_LabeledStatement"):
                opp_val = getattr(old_value, "ast_LabeledStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_LabeledStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_LabeledStatement"):
                opp_val = getattr(value, "ast_LabeledStatement", None)
                setattr(value, "ast_LabeledStatement", self)

    @property
    def ast_SimpleName(self):
        return self.__ast_SimpleName

    @ast_SimpleName.setter
    def ast_SimpleName(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName", None)
        self.__ast_SimpleName = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MemberRef12"):
                opp_val = getattr(old_value, "ast_MemberRef12", None)
                if opp_val == self:
                    setattr(old_value, "ast_MemberRef12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MemberRef12"):
                opp_val = getattr(value, "ast_MemberRef12", None)
                setattr(value, "ast_MemberRef12", self)

    @property
    def ast_SimpleName381(self):
        return self.__ast_SimpleName381

    @ast_SimpleName381.setter
    def ast_SimpleName381(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName381", None)
        self.__ast_SimpleName381 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_EnumDeclaration380"):
                opp_val = getattr(old_value, "ast_EnumDeclaration380", None)
                if opp_val == self:
                    setattr(old_value, "ast_EnumDeclaration380", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_EnumDeclaration380"):
                opp_val = getattr(value, "ast_EnumDeclaration380", None)
                setattr(value, "ast_EnumDeclaration380", self)

    @property
    def ast_SimpleName501(self):
        return self.__ast_SimpleName501

    @ast_SimpleName501.setter
    def ast_SimpleName501(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName501", None)
        self.__ast_SimpleName501 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SuperMethodReference500"):
                opp_val = getattr(old_value, "ast_SuperMethodReference500", None)
                if opp_val == self:
                    setattr(old_value, "ast_SuperMethodReference500", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SuperMethodReference500"):
                opp_val = getattr(value, "ast_SuperMethodReference500", None)
                setattr(value, "ast_SuperMethodReference500", self)

    @property
    def ast_SimpleName52(self):
        return self.__ast_SimpleName52

    @ast_SimpleName52.setter
    def ast_SimpleName52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName52", None)
        self.__ast_SimpleName52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_BreakStatement"):
                opp_val = getattr(old_value, "ast_BreakStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_BreakStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_BreakStatement"):
                opp_val = getattr(value, "ast_BreakStatement", None)
                setattr(value, "ast_BreakStatement", self)

    @property
    def ast_SimpleName480(self):
        return self.__ast_SimpleName480

    @ast_SimpleName480.setter
    def ast_SimpleName480(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName480", None)
        self.__ast_SimpleName480 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_NameQualifiedType479"):
                opp_val = getattr(old_value, "ast_NameQualifiedType479", None)
                if opp_val == self:
                    setattr(old_value, "ast_NameQualifiedType479", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_NameQualifiedType479"):
                opp_val = getattr(value, "ast_NameQualifiedType479", None)
                setattr(value, "ast_NameQualifiedType479", self)

    @property
    def ast_SimpleName95(self):
        return self.__ast_SimpleName95

    @ast_SimpleName95.setter
    def ast_SimpleName95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName95", None)
        self.__ast_SimpleName95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ContinueStatement"):
                opp_val = getattr(old_value, "ast_ContinueStatement", None)
                if opp_val == self:
                    setattr(old_value, "ast_ContinueStatement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ContinueStatement"):
                opp_val = getattr(value, "ast_ContinueStatement", None)
                setattr(value, "ast_ContinueStatement", self)

    @property
    def ast_SimpleName493(self):
        return self.__ast_SimpleName493

    @ast_SimpleName493.setter
    def ast_SimpleName493(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName493", None)
        self.__ast_SimpleName493 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ExpressionMethodReference492"):
                opp_val = getattr(old_value, "ast_ExpressionMethodReference492", None)
                if opp_val == self:
                    setattr(old_value, "ast_ExpressionMethodReference492", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ExpressionMethodReference492"):
                opp_val = getattr(value, "ast_ExpressionMethodReference492", None)
                setattr(value, "ast_ExpressionMethodReference492", self)

    @property
    def ast_SimpleName224(self):
        return self.__ast_SimpleName224

    @ast_SimpleName224.setter
    def ast_SimpleName224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName224", None)
        self.__ast_SimpleName224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_QualifiedName223"):
                opp_val = getattr(old_value, "ast_QualifiedName223", None)
                if opp_val == self:
                    setattr(old_value, "ast_QualifiedName223", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_QualifiedName223"):
                opp_val = getattr(value, "ast_QualifiedName223", None)
                setattr(value, "ast_QualifiedName223", self)

    @property
    def ast_SimpleName365(self):
        return self.__ast_SimpleName365

    @ast_SimpleName365.setter
    def ast_SimpleName365(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName365", None)
        self.__ast_SimpleName365 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodRefParameter364"):
                opp_val = getattr(old_value, "ast_MethodRefParameter364", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodRefParameter364", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodRefParameter364"):
                opp_val = getattr(value, "ast_MethodRefParameter364", None)
                setattr(value, "ast_MethodRefParameter364", self)

    @property
    def ast_SimpleName509(self):
        return self.__ast_SimpleName509

    @ast_SimpleName509.setter
    def ast_SimpleName509(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName509", None)
        self.__ast_SimpleName509 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_TypeMethodReference508"):
                opp_val = getattr(old_value, "ast_TypeMethodReference508", None)
                if opp_val == self:
                    setattr(old_value, "ast_TypeMethodReference508", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_TypeMethodReference508"):
                opp_val = getattr(value, "ast_TypeMethodReference508", None)
                setattr(value, "ast_TypeMethodReference508", self)

    @property
    def ast_SimpleName426(self):
        return self.__ast_SimpleName426

    @ast_SimpleName426.setter
    def ast_SimpleName426(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName426", None)
        self.__ast_SimpleName426 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_QualifiedType425"):
                opp_val = getattr(old_value, "ast_QualifiedType425", None)
                if opp_val == self:
                    setattr(old_value, "ast_QualifiedType425", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_QualifiedType425"):
                opp_val = getattr(value, "ast_QualifiedType425", None)
                setattr(value, "ast_QualifiedType425", self)

    @property
    def ast_SimpleName307(self):
        return self.__ast_SimpleName307

    @ast_SimpleName307.setter
    def ast_SimpleName307(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName307", None)
        self.__ast_SimpleName307 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_TypeDeclaration306"):
                opp_val = getattr(old_value, "ast_TypeDeclaration306", None)
                if opp_val == self:
                    setattr(old_value, "ast_TypeDeclaration306", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_TypeDeclaration306"):
                opp_val = getattr(value, "ast_TypeDeclaration306", None)
                setattr(value, "ast_TypeDeclaration306", self)

    @property
    def ast_SimpleName262(self):
        return self.__ast_SimpleName262

    @ast_SimpleName262.setter
    def ast_SimpleName262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName262", None)
        self.__ast_SimpleName262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SuperFieldAccess261"):
                opp_val = getattr(old_value, "ast_SuperFieldAccess261", None)
                if opp_val == self:
                    setattr(old_value, "ast_SuperFieldAccess261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SuperFieldAccess261"):
                opp_val = getattr(value, "ast_SuperFieldAccess261", None)
                setattr(value, "ast_SuperFieldAccess261", self)

    @property
    def ast_SimpleName174(self):
        return self.__ast_SimpleName174

    @ast_SimpleName174.setter
    def ast_SimpleName174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName174", None)
        self.__ast_SimpleName174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodDeclaration173"):
                opp_val = getattr(old_value, "ast_MethodDeclaration173", None)
                if opp_val == self:
                    setattr(old_value, "ast_MethodDeclaration173", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodDeclaration173"):
                opp_val = getattr(value, "ast_MethodDeclaration173", None)
                setattr(value, "ast_MethodDeclaration173", self)

    @property
    def ast_SimpleName107(self):
        return self.__ast_SimpleName107

    @ast_SimpleName107.setter
    def ast_SimpleName107(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName107", None)
        self.__ast_SimpleName107 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_FieldAccess106"):
                opp_val = getattr(old_value, "ast_FieldAccess106", None)
                if opp_val == self:
                    setattr(old_value, "ast_FieldAccess106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_FieldAccess106"):
                opp_val = getattr(value, "ast_FieldAccess106", None)
                setattr(value, "ast_FieldAccess106", self)

    @property
    def ast_SimpleName243(self):
        return self.__ast_SimpleName243

    @ast_SimpleName243.setter
    def ast_SimpleName243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName243", None)
        self.__ast_SimpleName243 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SingleVariableDeclaration242"):
                opp_val = getattr(old_value, "ast_SingleVariableDeclaration242", None)
                if opp_val == self:
                    setattr(old_value, "ast_SingleVariableDeclaration242", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SingleVariableDeclaration242"):
                opp_val = getattr(value, "ast_SingleVariableDeclaration242", None)
                setattr(value, "ast_SingleVariableDeclaration242", self)

    @property
    def ast_SimpleName459(self):
        return self.__ast_SimpleName459

    @ast_SimpleName459.setter
    def ast_SimpleName459(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_SimpleName__ast_SimpleName459", None)
        self.__ast_SimpleName459 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_AnnotationTypeMemberDeclaration458"):
                opp_val = getattr(old_value, "ast_AnnotationTypeMemberDeclaration458", None)
                if opp_val == self:
                    setattr(old_value, "ast_AnnotationTypeMemberDeclaration458", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_AnnotationTypeMemberDeclaration458"):
                opp_val = getattr(value, "ast_AnnotationTypeMemberDeclaration458", None)
                setattr(value, "ast_AnnotationTypeMemberDeclaration458", self)

class IDocElement:

    pass
class ast_IDocElement:

    pass
class ASTNode:

    pass
class ast_MemberValuePair(ASTNode):

    pass
class ast_MemberRef(ASTNode, IDocElement):

    pass
class ast_TypeParameter(ASTNode):

    pass
class ast_CatchClause(ASTNode):

    pass
class ast_ImportDeclaration(ASTNode):

    def __init__(self, static: bool, onDemand: bool, ast_ImportDeclaration: "ast_CompilationUnit" = None, ast_ImportDeclaration136: "ast_Name" = None):
        self.static = static
        self.onDemand = onDemand
        self.ast_ImportDeclaration = ast_ImportDeclaration
        self.ast_ImportDeclaration136 = ast_ImportDeclaration136
        
    @property
    def static(self) -> bool:
        return self.__static

    @static.setter
    def static(self, static: bool):
        self.__static = static

    @property
    def onDemand(self) -> bool:
        return self.__onDemand

    @onDemand.setter
    def onDemand(self, onDemand: bool):
        self.__onDemand = onDemand

    @property
    def ast_ImportDeclaration136(self):
        return self.__ast_ImportDeclaration136

    @ast_ImportDeclaration136.setter
    def ast_ImportDeclaration136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ImportDeclaration__ast_ImportDeclaration136", None)
        self.__ast_ImportDeclaration136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Name137"):
                opp_val = getattr(old_value, "ast_Name137", None)
                if opp_val == self:
                    setattr(old_value, "ast_Name137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Name137"):
                opp_val = getattr(value, "ast_Name137", None)
                setattr(value, "ast_Name137", self)

    @property
    def ast_ImportDeclaration(self):
        return self.__ast_ImportDeclaration

    @ast_ImportDeclaration.setter
    def ast_ImportDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_ImportDeclaration__ast_ImportDeclaration", None)
        self.__ast_ImportDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_CompilationUnit78"):
                opp_val = getattr(old_value, "ast_CompilationUnit78", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_CompilationUnit78"):
                opp_val = getattr(value, "ast_CompilationUnit78", None)
                if opp_val is None:
                    setattr(value, "ast_CompilationUnit78", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_AnonymousClassDeclaration(ASTNode):

    pass
class ast_TagElement(ASTNode, IDocElement):

    def __init__(self, tagName: str, ast_TagElement: set["ast_IDocElement"] = None, ast_TagElement156: "ast_Javadoc" = None):
        self.tagName = tagName
        self.ast_TagElement = ast_TagElement if ast_TagElement is not None else set()
        self.ast_TagElement156 = ast_TagElement156
        
    @property
    def tagName(self) -> str:
        return self.__tagName

    @tagName.setter
    def tagName(self, tagName: str):
        self.__tagName = tagName

    @property
    def ast_TagElement(self):
        return self.__ast_TagElement

    @ast_TagElement.setter
    def ast_TagElement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TagElement__ast_TagElement", None)
        self.__ast_TagElement = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_IDocElement"):
                    opp_val = getattr(item, "ast_IDocElement", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_IDocElement", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_IDocElement"):
                    opp_val = getattr(item, "ast_IDocElement", None)
                    
                    setattr(item, "ast_IDocElement", self)
                    

    @property
    def ast_TagElement156(self):
        return self.__ast_TagElement156

    @ast_TagElement156.setter
    def ast_TagElement156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_TagElement__ast_TagElement156", None)
        self.__ast_TagElement156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Javadoc155"):
                opp_val = getattr(old_value, "ast_Javadoc155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Javadoc155"):
                opp_val = getattr(value, "ast_Javadoc155", None)
                if opp_val is None:
                    setattr(value, "ast_Javadoc155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ast_MethodRefParameter(ASTNode):

    def __init__(self, varargs: bool, ast_MethodRefParameter: "ast_MethodRef" = None, ast_MethodRefParameter361: "ast_Type" = None, ast_MethodRefParameter364: "ast_SimpleName" = None):
        self.varargs = varargs
        self.ast_MethodRefParameter = ast_MethodRefParameter
        self.ast_MethodRefParameter361 = ast_MethodRefParameter361
        self.ast_MethodRefParameter364 = ast_MethodRefParameter364
        
    @property
    def varargs(self) -> bool:
        return self.__varargs

    @varargs.setter
    def varargs(self, varargs: bool):
        self.__varargs = varargs

    @property
    def ast_MethodRefParameter(self):
        return self.__ast_MethodRefParameter

    @ast_MethodRefParameter.setter
    def ast_MethodRefParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodRefParameter__ast_MethodRefParameter", None)
        self.__ast_MethodRefParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_MethodRef19"):
                opp_val = getattr(old_value, "ast_MethodRef19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_MethodRef19"):
                opp_val = getattr(value, "ast_MethodRef19", None)
                if opp_val is None:
                    setattr(value, "ast_MethodRef19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ast_MethodRefParameter361(self):
        return self.__ast_MethodRefParameter361

    @ast_MethodRefParameter361.setter
    def ast_MethodRefParameter361(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodRefParameter__ast_MethodRefParameter361", None)
        self.__ast_MethodRefParameter361 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Type362"):
                opp_val = getattr(old_value, "ast_Type362", None)
                if opp_val == self:
                    setattr(old_value, "ast_Type362", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Type362"):
                opp_val = getattr(value, "ast_Type362", None)
                setattr(value, "ast_Type362", self)

    @property
    def ast_MethodRefParameter364(self):
        return self.__ast_MethodRefParameter364

    @ast_MethodRefParameter364.setter
    def ast_MethodRefParameter364(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_MethodRefParameter__ast_MethodRefParameter364", None)
        self.__ast_MethodRefParameter364 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_SimpleName365"):
                opp_val = getattr(old_value, "ast_SimpleName365", None)
                if opp_val == self:
                    setattr(old_value, "ast_SimpleName365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_SimpleName365"):
                opp_val = getattr(value, "ast_SimpleName365", None)
                setattr(value, "ast_SimpleName365", self)

class ast_Dimension(ASTNode):

    pass
class ast_CompilationUnit(ASTNode):

    pass
class ast_Comment(ASTNode):

    pass
class ast_TextElement(ASTNode, IDocElement):

    def __init__(self, text: str):
        self.text = text
        
    @property
    def text(self) -> str:
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

class ast_BodyDeclaration(ASTNode):

    pass
class ast_Statement(ASTNode):

    pass
class ast_MethodRef(ASTNode, IDocElement):

    pass
class ast_VariableDeclaration(ASTNode):

    pass
class ast_PackageDeclaration(ASTNode):

    pass
class ast_Type(ASTNode):

    pass
class ast_IExtendedModifier:

    pass
class ast_Expression(ASTNode):

    pass
class Expression:

    pass
class ast_TypeLiteral(Expression):

    pass
class ast_StringLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class ast_SuperFieldAccess(Expression):

    pass
class ast_MethodReference(Expression):

    pass
class ast_NumberLiteral(Expression):

    def __init__(self, token: str):
        self.token = token
        
    @property
    def token(self) -> str:
        return self.__token

    @token.setter
    def token(self, token: str):
        self.__token = token

class ast_InstanceofExpression(Expression):

    pass
class ast_PostfixExpression(Expression):

    def __init__(self, operator: str, ast_PostfixExpression: "ast_Expression" = None):
        self.operator = operator
        self.ast_PostfixExpression = ast_PostfixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_PostfixExpression(self):
        return self.__ast_PostfixExpression

    @ast_PostfixExpression.setter
    def ast_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PostfixExpression__ast_PostfixExpression", None)
        self.__ast_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression215"):
                opp_val = getattr(old_value, "ast_Expression215", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression215"):
                opp_val = getattr(value, "ast_Expression215", None)
                setattr(value, "ast_Expression215", self)

class ast_BooleanLiteral(Expression):

    def __init__(self, booleanValue: bool):
        self.booleanValue = booleanValue
        
    @property
    def booleanValue(self) -> bool:
        return self.__booleanValue

    @booleanValue.setter
    def booleanValue(self, booleanValue: bool):
        self.__booleanValue = booleanValue

class ast_LambdaExpression(Expression):

    def __init__(self, parentheses: bool, ast_LambdaExpression: set["ast_VariableDeclaration"] = None, ast_LambdaExpression470: "ast_ASTNode" = None):
        self.parentheses = parentheses
        self.ast_LambdaExpression = ast_LambdaExpression if ast_LambdaExpression is not None else set()
        self.ast_LambdaExpression470 = ast_LambdaExpression470
        
    @property
    def parentheses(self) -> bool:
        return self.__parentheses

    @parentheses.setter
    def parentheses(self, parentheses: bool):
        self.__parentheses = parentheses

    @property
    def ast_LambdaExpression(self):
        return self.__ast_LambdaExpression

    @ast_LambdaExpression.setter
    def ast_LambdaExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_LambdaExpression__ast_LambdaExpression", None)
        self.__ast_LambdaExpression = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_VariableDeclaration"):
                    opp_val = getattr(item, "ast_VariableDeclaration", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_VariableDeclaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_VariableDeclaration"):
                    opp_val = getattr(item, "ast_VariableDeclaration", None)
                    
                    setattr(item, "ast_VariableDeclaration", self)
                    

    @property
    def ast_LambdaExpression470(self):
        return self.__ast_LambdaExpression470

    @ast_LambdaExpression470.setter
    def ast_LambdaExpression470(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_LambdaExpression__ast_LambdaExpression470", None)
        self.__ast_LambdaExpression470 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_ASTNode"):
                opp_val = getattr(old_value, "ast_ASTNode", None)
                if opp_val == self:
                    setattr(old_value, "ast_ASTNode", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_ASTNode"):
                opp_val = getattr(value, "ast_ASTNode", None)
                setattr(value, "ast_ASTNode", self)

class ast_MethodInvocation(Expression):

    pass
class ast_InfixExpression(Expression):

    def __init__(self, operator: str, ast_InfixExpression: "ast_Expression" = None, ast_InfixExpression141: "ast_Expression" = None, ast_InfixExpression144: set["ast_Expression"] = None):
        self.operator = operator
        self.ast_InfixExpression = ast_InfixExpression
        self.ast_InfixExpression141 = ast_InfixExpression141
        self.ast_InfixExpression144 = ast_InfixExpression144 if ast_InfixExpression144 is not None else set()
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_InfixExpression144(self):
        return self.__ast_InfixExpression144

    @ast_InfixExpression144.setter
    def ast_InfixExpression144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_InfixExpression__ast_InfixExpression144", None)
        self.__ast_InfixExpression144 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ast_Expression145"):
                    opp_val = getattr(item, "ast_Expression145", None)
                    
                    if opp_val == self:
                        setattr(item, "ast_Expression145", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ast_Expression145"):
                    opp_val = getattr(item, "ast_Expression145", None)
                    
                    setattr(item, "ast_Expression145", self)
                    

    @property
    def ast_InfixExpression141(self):
        return self.__ast_InfixExpression141

    @ast_InfixExpression141.setter
    def ast_InfixExpression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_InfixExpression__ast_InfixExpression141", None)
        self.__ast_InfixExpression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression142"):
                opp_val = getattr(old_value, "ast_Expression142", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression142"):
                opp_val = getattr(value, "ast_Expression142", None)
                setattr(value, "ast_Expression142", self)

    @property
    def ast_InfixExpression(self):
        return self.__ast_InfixExpression

    @ast_InfixExpression.setter
    def ast_InfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_InfixExpression__ast_InfixExpression", None)
        self.__ast_InfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression139"):
                opp_val = getattr(old_value, "ast_Expression139", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression139"):
                opp_val = getattr(value, "ast_Expression139", None)
                setattr(value, "ast_Expression139", self)

class ast_FieldAccess(Expression):

    pass
class ast_CharacterLiteral(Expression):

    def __init__(self, escapedValue: str):
        self.escapedValue = escapedValue
        
    @property
    def escapedValue(self) -> str:
        return self.__escapedValue

    @escapedValue.setter
    def escapedValue(self, escapedValue: str):
        self.__escapedValue = escapedValue

class ast_ThisExpression(Expression):

    pass
class ast_ArrayCreation(Expression):

    pass
class ast_ClassInstanceCreation(Expression):

    pass
class ast_ArrayAccess(Expression):

    pass
class ast_NullLiteral(Expression):

    pass
class ast_ParenthesizedExpression(Expression):

    pass
class ast_ConditionalExpression(Expression):

    pass
class ast_PrefixExpression(Expression):

    def __init__(self, operator: str, ast_PrefixExpression: "ast_Expression" = None):
        self.operator = operator
        self.ast_PrefixExpression = ast_PrefixExpression
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_PrefixExpression(self):
        return self.__ast_PrefixExpression

    @ast_PrefixExpression.setter
    def ast_PrefixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_PrefixExpression__ast_PrefixExpression", None)
        self.__ast_PrefixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression217"):
                opp_val = getattr(old_value, "ast_Expression217", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression217", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression217"):
                opp_val = getattr(value, "ast_Expression217", None)
                setattr(value, "ast_Expression217", self)

class ast_CastExpression(Expression):

    pass
class ast_VariableDeclarationExpression(Expression):

    pass
class ast_SuperMethodInvocation(Expression):

    pass
class ast_Assignment(Expression):

    def __init__(self, operator: str, ast_Assignment: "ast_Expression" = None, ast_Assignment48: "ast_Expression" = None):
        self.operator = operator
        self.ast_Assignment = ast_Assignment
        self.ast_Assignment48 = ast_Assignment48
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def ast_Assignment48(self):
        return self.__ast_Assignment48

    @ast_Assignment48.setter
    def ast_Assignment48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Assignment__ast_Assignment48", None)
        self.__ast_Assignment48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression49"):
                opp_val = getattr(old_value, "ast_Expression49", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression49"):
                opp_val = getattr(value, "ast_Expression49", None)
                setattr(value, "ast_Expression49", self)

    @property
    def ast_Assignment(self):
        return self.__ast_Assignment

    @ast_Assignment.setter
    def ast_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ast_Assignment__ast_Assignment", None)
        self.__ast_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ast_Expression46"):
                opp_val = getattr(old_value, "ast_Expression46", None)
                if opp_val == self:
                    setattr(old_value, "ast_Expression46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ast_Expression46"):
                opp_val = getattr(value, "ast_Expression46", None)
                setattr(value, "ast_Expression46", self)

class ast_ArrayInitializer(Expression):

    pass
class ast_Name(IDocElement, Expression):

    pass
class Annotation:

    pass
class ast_NormalAnnotation(Annotation):

    pass
class ast_SingleMemberAnnotation(Annotation):

    pass
class ast_MarkerAnnotation(Annotation):

    pass
class ast_ASTNode:

    pass
class IExtendedModifier:

    pass
class ast_Modifier(ASTNode, IExtendedModifier):

    def __init__(self, keyword: str):
        self.keyword = keyword
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

class ast_Annotation(Expression, IExtendedModifier):

    pass