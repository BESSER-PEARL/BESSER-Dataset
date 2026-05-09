





import java.util.List;
import java.util.ArrayList;

public class eol_ModelElementType extends AnyType {

    private String modelName;
    private String elementName;
    private String modelElementType;
    private String resolvedIMetamodel;
    private String resolvedIPackage;





    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;


    public eol_ModelElementType(
        String modelName,        String elementName,        String modelElementType,        String resolvedIMetamodel,        String resolvedIPackage    ) {
        super(
        );
        this.modelName = modelName;
        this.elementName = elementName;
        this.modelElementType = modelElementType;
        this.resolvedIMetamodel = resolvedIMetamodel;
        this.resolvedIPackage = resolvedIPackage;
    }


    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }
    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }
    public String getModelelementtype() {
        return modelElementType;
    }

    public void setModelelementtype(String modelElementType) {
        this.modelElementType = modelElementType;
    }
    public String getResolvedimetamodel() {
        return resolvedIMetamodel;
    }

    public void setResolvedimetamodel(String resolvedIMetamodel) {
        this.resolvedIMetamodel = resolvedIMetamodel;
    }
    public String getResolvedipackage() {
        return resolvedIPackage;
    }

    public void setResolvedipackage(String resolvedIPackage) {
        this.resolvedIPackage = resolvedIPackage;
    }

    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }

}