





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private String type;
    private String location;
    private String provider;
    private boolean modifiable;
    private String name;
    private String version;
    private String description;



    public aggregator_p2_IRepository(
        String type,        String location,        String provider,        boolean modifiable,        String name,        String version,        String description    ) {
        super(
        );
        this.type = type;
        this.location = location;
        this.provider = provider;
        this.modifiable = modifiable;
        this.name = name;
        this.version = version;
        this.description = description;
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
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
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
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}