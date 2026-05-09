





import java.util.List;
import java.util.ArrayList;

public class RefUML_PackageImport extends DirectedRelationship {

    private String visibility;





    private RefUML_Namespace refuml_namespace;




    private RefUML_Namespace refuml_namespace;




    private RefUML_Package refuml_package;


    public RefUML_PackageImport(
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
    public RefUML_Package getRefuml_package() {
        return refuml_package;
    }

    public void setRefuml_package(RefUML_Package refuml_package) {
        this.refuml_package = refuml_package;
    }

}