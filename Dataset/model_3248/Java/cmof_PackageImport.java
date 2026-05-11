





import java.util.List;
import java.util.ArrayList;

public class cmof_PackageImport extends DirectedRelationship {

    private String visibility;





    private cmof_Package cmof_package;




    private cmof_Namespace cmof_namespace;




    private cmof_Namespace cmof_namespace;


    public cmof_PackageImport(
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

    public cmof_Package getCmof_package() {
        return cmof_package;
    }

    public void setCmof_package(cmof_Package cmof_package) {
        this.cmof_package = cmof_package;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }
    public cmof_Namespace getCmof_namespace() {
        return cmof_namespace;
    }

    public void setCmof_namespace(cmof_Namespace cmof_namespace) {
        this.cmof_namespace = cmof_namespace;
    }

}