





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private String version;
    private String type;
    private String name;
    private String location;
    private boolean modifiable;
    private String provider;
    private String description;



    public aggregator_p2_IRepository(
        String version,        String type,        String name,        String location,        boolean modifiable,        String provider,        String description    ) {
        super(
        );
        this.version = version;
        this.type = type;
        this.name = name;
        this.location = location;
        this.modifiable = modifiable;
        this.provider = provider;
        this.description = description;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
        this.modifiable = modifiable;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}