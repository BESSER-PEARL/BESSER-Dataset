





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private boolean modifiable;
    private String type;
    private String provider;
    private String location;
    private String version;
    private String name;
    private String description;



    public aggregator_p2_IRepository(
        boolean modifiable,        String type,        String provider,        String location,        String version,        String name,        String description    ) {
        super(
        );
        this.modifiable = modifiable;
        this.type = type;
        this.provider = provider;
        this.location = location;
        this.version = version;
        this.name = name;
        this.description = description;
    }


    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
        this.modifiable = modifiable;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}