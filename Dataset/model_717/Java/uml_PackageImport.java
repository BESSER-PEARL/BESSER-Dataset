





import java.util.List;
import java.util.ArrayList;

public class uml_PackageImport extends DirectedRelationship {

    private String visibility;





    private uml_Package uml_package;




    private uml_Namespace uml_namespace;




    private uml_Namespace uml_namespace;


    public uml_PackageImport(
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

    public uml_Package getUml_package() {
        return uml_package;
    }

    public void setUml_package(uml_Package uml_package) {
        this.uml_package = uml_package;
    }
    public uml_Namespace getUml_namespace() {
        return uml_namespace;
    }

    public void setUml_namespace(uml_Namespace uml_namespace) {
        this.uml_namespace = uml_namespace;
    }
    public uml_Namespace getUml_namespace() {
        return uml_namespace;
    }

    public void setUml_namespace(uml_Namespace uml_namespace) {
        this.uml_namespace = uml_namespace;
    }

}