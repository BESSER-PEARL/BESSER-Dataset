





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private String location;
    private String provider;
    private String description;
    private String type;
    private boolean modifiable;
    private String version;
    private String name;



    public aggregator_p2_IRepository(
        String location,        String provider,        String description,        String type,        boolean modifiable,        String version,        String name    ) {
        super(
        );
        this.location = location;
        this.provider = provider;
        this.description = description;
        this.type = type;
        this.modifiable = modifiable;
        this.version = version;
        this.name = name;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
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


}