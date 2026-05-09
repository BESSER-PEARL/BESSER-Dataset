





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_ElementImport extends DirectedRelationship {

    private String visibility;
    private String alias;





    private RefOntoUML_Namespace refontouml_namespace;




    private RefOntoUML_Namespace refontouml_namespace;




    private RefOntoUML_PackageableElement refontouml_packageableelement;


    public RefOntoUML_ElementImport(
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

    public RefOntoUML_Namespace getRefontouml_namespace() {
        return refontouml_namespace;
    }

    public void setRefontouml_namespace(RefOntoUML_Namespace refontouml_namespace) {
        this.refontouml_namespace = refontouml_namespace;
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

}