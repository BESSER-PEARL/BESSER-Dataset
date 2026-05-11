





import java.util.List;
import java.util.ArrayList;

public class Classes_Kernel_PackageImport extends DirectedRelationship {

    private String visibility;





    private Namespace namespace;




    private Package package;


    public Classes_Kernel_PackageImport(
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

    public Namespace getNamespace() {
        return namespace;
    }

    public void setNamespace(Namespace namespace) {
        this.namespace = namespace;
    }
    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}