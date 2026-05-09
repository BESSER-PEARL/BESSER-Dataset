





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_ElementImport extends DirectedRelationship {

    private String alias;
    private String visibility;





    private RefOntoUML_Namespace refontouml_namespace;




    private RefOntoUML_PackageableElement refontouml_packageableelement;




    private RefOntoUML_Namespace refontouml_namespace;


    public RefOntoUML_ElementImport(
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

    public RefOntoUML_Namespace getRefontouml_namespace() {
        return refontouml_namespace;
    }

    public void setRefontouml_namespace(RefOntoUML_Namespace refontouml_namespace) {
        this.refontouml_namespace = refontouml_namespace;
    }
    public RefOntoUML_PackageableElement getRefontouml_packageableelement() {
        return refontouml_packageableelement;
    }

    public void setRefontouml_packageableelement(RefOntoUML_PackageableElement refontouml_packageableelement) {
        this.refontouml_packageableelement = refontouml_packageableelement;
    }
    public RefOntoUML_Namespace getRefontouml_namespace() {
        return refontouml_namespace;
    }

    public void setRefontouml_namespace(RefOntoUML_Namespace refontouml_namespace) {
        this.refontouml_namespace = refontouml_namespace;
    }

}