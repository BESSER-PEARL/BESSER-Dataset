





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_PackageImport extends DirectedRelationship {

    private String visibility;





    private RefOntoUML_Namespace refontouml_namespace;




    private RefOntoUML_Namespace refontouml_namespace;




    private RefOntoUML_Package refontouml_package;


    public RefOntoUML_PackageImport(
        String visibility    ) {
        super(
        );
        this.visibility = visibility;
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
    public RefOntoUML_Namespace getRefontouml_namespace() {
        return refontouml_namespace;
    }

    public void setRefontouml_namespace(RefOntoUML_Namespace refontouml_namespace) {
        this.refontouml_namespace = refontouml_namespace;
    }
    public RefOntoUML_Package getRefontouml_package() {
        return refontouml_package;
    }

    public void setRefontouml_package(RefOntoUML_Package refontouml_package) {
        this.refontouml_package = refontouml_package;
    }

}