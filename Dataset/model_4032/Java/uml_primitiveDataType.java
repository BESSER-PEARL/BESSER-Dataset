





import java.util.List;
import java.util.ArrayList;

public class uml_primitiveDataType  {

    private String oID;
    private String kind;
    private String name;





    private uml_classifiersAndAssociations uml_classifiersandassociations;




    private uml_ownerClassifier uml_ownerclassifier;


    public uml_primitiveDataType(
        String oID,        String kind,        String name    ) {
        this.oID = oID;
        this.kind = kind;
        this.name = name;
    }


    public String getOid() {
        return oID;
    }

    public void setOid(String oID) {
        this.oID = oID;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public uml_classifiersAndAssociations getUml_classifiersandassociations() {
        return uml_classifiersandassociations;
    }

    public void setUml_classifiersandassociations(uml_classifiersAndAssociations uml_classifiersandassociations) {
        this.uml_classifiersandassociations = uml_classifiersandassociations;
    }
    public uml_ownerClassifier getUml_ownerclassifier() {
        return uml_ownerclassifier;
    }

    public void setUml_ownerclassifier(uml_ownerClassifier uml_ownerclassifier) {
        this.uml_ownerclassifier = uml_ownerclassifier;
    }

}