





import java.util.List;
import java.util.ArrayList;

public class p2_IRepository  {

    private String version;
    private String location;
    private String type;
    private String description;
    private boolean modifiable;
    private String name;
    private String provisioningAgent;
    private String provider;



    public p2_IRepository(
        String version,        String location,        String type,        String description,        boolean modifiable,        String name,        String provisioningAgent,        String provider    ) {
        this.version = version;
        this.location = location;
        this.type = type;
        this.description = description;
        this.modifiable = modifiable;
        this.name = name;
        this.provisioningAgent = provisioningAgent;
        this.provider = provider;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
        this.modifiable = modifiable;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProvisioningagent() {
        return provisioningAgent;
    }

    public void setProvisioningagent(String provisioningAgent) {
        this.provisioningAgent = provisioningAgent;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }


}