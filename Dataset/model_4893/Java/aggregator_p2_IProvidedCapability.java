





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IProvidedCapability  {

    private String name;
    private String namespace;
    private String version;



    public aggregator_p2_IProvidedCapability(
        String name,        String namespace,        String version    ) {
        this.name = name;
        this.namespace = namespace;
        this.version = version;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
        this.namespace = namespace;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }


}