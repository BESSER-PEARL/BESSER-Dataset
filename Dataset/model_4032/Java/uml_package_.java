





import java.util.List;
import java.util.ArrayList;

public class uml_package_  {

    private String oID;
    private String kind;
    private String name;





    private uml_classifiersAndAssociations uml_classifiersandassociations;




    private uml_DocumentRoot uml_documentroot;


    public uml_package_(
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
    public uml_DocumentRoot getUml_documentroot() {
        return uml_documentroot;
    }

    public void setUml_documentroot(uml_DocumentRoot uml_documentroot) {
        this.uml_documentroot = uml_documentroot;
    }

}