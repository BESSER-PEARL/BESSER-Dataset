





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private uml3_0_0_PackageableElement uml3_0_0_packageableelement;




    private uml3_0_0_Namespace uml3_0_0_namespace;




    private uml3_0_0_Namespace uml3_0_0_namespace;


    public uml3_0_0_ElementImport(
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

    public uml3_0_0_PackageableElement getUml3_0_0_packageableelement() {
        return uml3_0_0_packageableelement;
    }

    public void setUml3_0_0_packageableelement(uml3_0_0_PackageableElement uml3_0_0_packageableelement) {
        this.uml3_0_0_packageableelement = uml3_0_0_packageableelement;
    }
    public uml3_0_0_Namespace getUml3_0_0_namespace() {
        return uml3_0_0_namespace;
    }

    public void setUml3_0_0_namespace(uml3_0_0_Namespace uml3_0_0_namespace) {
        this.uml3_0_0_namespace = uml3_0_0_namespace;
    }
    public uml3_0_0_Namespace getUml3_0_0_namespace() {
        return uml3_0_0_namespace;
    }

    public void setUml3_0_0_namespace(uml3_0_0_Namespace uml3_0_0_namespace) {
        this.uml3_0_0_namespace = uml3_0_0_namespace;
    }

}