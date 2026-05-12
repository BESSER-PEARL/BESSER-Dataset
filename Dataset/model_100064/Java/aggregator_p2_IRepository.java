





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private String name;
    private String location;
    private String version;
    private String description;
    private String type;
    private String provider;
    private boolean modifiable;



    public aggregator_p2_IRepository(
        String name,        String location,        String version,        String description,        String type,        String provider,        boolean modifiable    ) {
        super(
        );
        this.name = name;
        this.location = location;
        this.version = version;
        this.description = description;
        this.type = type;
        this.provider = provider;
        this.modifiable = modifiable;
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
    public boolean getModifiable() {
        return modifiable;
    }

    public void setModifiable(boolean modifiable) {
        this.modifiable = modifiable;
    }


}