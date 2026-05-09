





import java.util.List;
import java.util.ArrayList;

public class RefUML_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private RefUML_PackageableElement refuml_packageableelement;




    private RefUML_Namespace refuml_namespace;




    private RefUML_Namespace refuml_namespace;


    public RefUML_ElementImport(
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

    public RefUML_PackageableElement getRefuml_packageableelement() {
        return refuml_packageableelement;
    }

    public void setRefuml_packageableelement(RefUML_PackageableElement refuml_packageableelement) {
        this.refuml_packageableelement = refuml_packageableelement;
    }
    public RefUML_Namespace getRefuml_namespace() {
        return refuml_namespace;
    }

    public void setRefuml_namespace(RefUML_Namespace refuml_namespace) {
        this.refuml_namespace = refuml_namespace;
    }
    public RefUML_Namespace getRefuml_namespace() {
        return refuml_namespace;
    }

    public void setRefuml_namespace(RefUML_Namespace refuml_namespace) {
        this.refuml_namespace = refuml_namespace;
    }

}