





import java.util.List;
import java.util.ArrayList;

public class p2_IRepository  {

    private String version;
    private String name;
    private String type;
    private String location;
    private String description;
    private String provider;
    private String provisioningAgent;
    private boolean modifiable;



    public p2_IRepository(
        String version,        String name,        String type,        String location,        String description,        String provider,        String provisioningAgent,        boolean modifiable    ) {
        this.version = version;
        this.name = name;
        this.type = type;
        this.location = location;
        this.description = description;
        this.provider = provider;
        this.provisioningAgent = provisioningAgent;
        this.modifiable = modifiable;
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
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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
    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
        this.modifiable = modifiable;
    }


}