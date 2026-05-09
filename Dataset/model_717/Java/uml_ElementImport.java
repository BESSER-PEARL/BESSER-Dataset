





import java.util.List;
import java.util.ArrayList;

public class uml_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private uml_Namespace uml_namespace;




    private uml_PackageableElement uml_packageableelement;




    private uml_Namespace uml_namespace;


    public uml_ElementImport(
        String alias,        String visibility    ) {
        super(
        );
        this.alias = alias;
        this.visibility = visibility;
    }


    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }

    public uml_Namespace getUml_namespace() {
        return uml_namespace;
    }

    public void setUml_namespace(uml_Namespace uml_namespace) {
        this.uml_namespace = uml_namespace;
    }
    public uml_PackageableElement getUml_packageableelement() {
        return uml_packageableelement;
    }

    public void setUml_packageableelement(uml_PackageableElement uml_packageableelement) {
        this.uml_packageableelement = uml_packageableelement;
    }
    public uml_Namespace getUml_namespace() {
        return uml_namespace;
    }

    public void setUml_namespace(uml_Namespace uml_namespace) {
        this.uml_namespace = uml_namespace;
    }

}