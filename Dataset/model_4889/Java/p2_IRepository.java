





import java.util.List;
import java.util.ArrayList;

public class p2_IRepository  {

    private String type;
    private String name;
    private String version;
    private String provider;
    private String provisioningAgent;
    private String location;
    private String description;
    private boolean modifiable;



    public p2_IRepository(
        String type,        String name,        String version,        String provider,        String provisioningAgent,        String location,        String description,        boolean modifiable    ) {
        this.type = type;
        this.name = name;
        this.version = version;
        this.provider = provider;
        this.provisioningAgent = provisioningAgent;
        this.location = location;
        this.description = description;
        this.modifiable = modifiable;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getProvisioningagent() {
        return provisioningAgent;
    }

    public void setProvisioningagent(String provisioningAgent) {
        this.provisioningAgent = provisioningAgent;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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


}