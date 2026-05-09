





import java.util.List;
import java.util.ArrayList;

public class eol_ModelElementType extends AnyType {

    private String elementName;
    private String modelName;
    private String modelType;





    private eol_IModel eol_imodel;




    private eol_IPackage eol_ipackage;




    private eol_ModelDeclarationStatement eol_modeldeclarationstatement;


    public eol_ModelElementType(
        String elementName,        String modelName,        String modelType    ) {
        super(
        );
        this.elementName = elementName;
        this.modelName = modelName;
        this.modelType = modelType;
    }


    public String getElementname() {
        return elementName;
    }

    public void setElementname(String elementName) {
        this.elementName = elementName;
    }
    public String getModelname() {
        return modelName;
    }

    public void setModelname(String modelName) {
        this.modelName = modelName;
    }
    public String getModeltype() {
        return modelType;
    }

    public void setModeltype(String modelType) {
        this.modelType = modelType;
    }

    public eol_IModel getEol_imodel() {
        return eol_imodel;
    }

    public void setEol_imodel(eol_IModel eol_imodel) {
        this.eol_imodel = eol_imodel;
    }
    public eol_IPackage getEol_ipackage() {
        return eol_ipackage;
    }

    public void setEol_ipackage(eol_IPackage eol_ipackage) {
        this.eol_ipackage = eol_ipackage;
    }
    public eol_ModelDeclarationStatement getEol_modeldeclarationstatement() {
        return eol_modeldeclarationstatement;
    }

    public void setEol_modeldeclarationstatement(eol_ModelDeclarationStatement eol_modeldeclarationstatement) {
        this.eol_modeldeclarationstatement = eol_modeldeclarationstatement;
    }

}