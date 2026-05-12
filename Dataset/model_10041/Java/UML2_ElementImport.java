





import java.util.List;
import java.util.ArrayList;

public class UML2_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private UML2_Namespace uml2_namespace;




    private UML2_Namespace uml2_namespace;




    private UML2_PackageableElement uml2_packageableelement;


    public UML2_ElementImport(
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

    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_Namespace getUml2_namespace() {
        return uml2_namespace;
    }

    public void setUml2_namespace(UML2_Namespace uml2_namespace) {
        this.uml2_namespace = uml2_namespace;
    }
    public UML2_PackageableElement getUml2_packageableelement() {
        return uml2_packageableelement;
    }

    public void setUml2_packageableelement(UML2_PackageableElement uml2_packageableelement) {
        this.uml2_packageableelement = uml2_packageableelement;
    }

}