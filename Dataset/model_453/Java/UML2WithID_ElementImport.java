





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_ElementImport extends DirectedRelationship {

    private String visibility;
    private String alias;





    private UML2WithID_Namespace uml2withid_namespace;




    private UML2WithID_PackageableElement uml2withid_packageableelement;




    private UML2WithID_Namespace uml2withid_namespace;


    public UML2WithID_ElementImport(
        String visibility,        String alias    ) {
        super(
        );
        this.visibility = visibility;
        this.alias = alias;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getAlias() {
        return alias;
    }

    public void setAlias(String alias) {
        this.alias = alias;
    }

    public UML2WithID_Namespace getUml2withid_namespace() {
        return uml2withid_namespace;
    }

    public void setUml2withid_namespace(UML2WithID_Namespace uml2withid_namespace) {
        this.uml2withid_namespace = uml2withid_namespace;
    }
    public UML2WithID_PackageableElement getUml2withid_packageableelement() {
        return uml2withid_packageableelement;
    }

    public void setUml2withid_packageableelement(UML2WithID_PackageableElement uml2withid_packageableelement) {
        this.uml2withid_packageableelement = uml2withid_packageableelement;
    }
    public UML2WithID_Namespace getUml2withid_namespace() {
        return uml2withid_namespace;
    }

    public void setUml2withid_namespace(UML2WithID_Namespace uml2withid_namespace) {
        this.uml2withid_namespace = uml2withid_namespace;
    }

}