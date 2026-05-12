





import java.util.List;
import java.util.ArrayList;

public class build_ICapability  {

    private String name;
    private String version;
    private String namespace;



    public build_ICapability(
        String name,        String version,        String namespace    ) {
        this.name = name;
        this.version = version;
        this.namespace = namespace;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }


}