





import java.util.List;
import java.util.ArrayList;

public class datatypes_RosIDLReference extends IDLReference {

    private String namespace;
    private String rosPackage;



    public datatypes_RosIDLReference(
        String namespace,        String rosPackage    ) {
        super(
        );
        this.namespace = namespace;
        this.rosPackage = rosPackage;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getRospackage() {
        return rosPackage;
    }

    public void setRospackage(String rosPackage) {
        this.rosPackage = rosPackage;
    }


}