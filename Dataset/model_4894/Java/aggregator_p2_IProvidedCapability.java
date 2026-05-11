





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IProvidedCapability  {

    private String namespace;
    private String name;
    private String version;



    public aggregator_p2_IProvidedCapability(
        String namespace,        String name,        String version    ) {
        this.namespace = namespace;
        this.name = name;
        this.version = version;
    }


    public String getNamespace() {
        return namespace;
    }

    public void setNamespace(String namespace) {
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


}