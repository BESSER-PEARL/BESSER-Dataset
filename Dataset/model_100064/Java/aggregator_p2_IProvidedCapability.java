





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IProvidedCapability  {

    private String version;
    private String name;
    private String namespace;



    public aggregator_p2_IProvidedCapability(
        String version,        String name,        String namespace    ) {
        this.version = version;
        this.name = name;
        this.namespace = namespace;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
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


}