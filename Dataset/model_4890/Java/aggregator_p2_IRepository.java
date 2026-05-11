





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private String provider;
    private String type;
    private boolean modifiable;
    private String description;
    private String version;
    private String name;
    private String location;



    public aggregator_p2_IRepository(
        String provider,        String type,        boolean modifiable,        String description,        String version,        String name,        String location    ) {
        super(
        );
        this.provider = provider;
        this.type = type;
        this.modifiable = modifiable;
        this.description = description;
        this.version = version;
        this.name = name;
        this.location = location;
    }


    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}