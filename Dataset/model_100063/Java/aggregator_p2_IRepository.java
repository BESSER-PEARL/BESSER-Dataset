





import java.util.List;
import java.util.ArrayList;

public class aggregator_p2_IRepository extends IAdaptable {

    private boolean modifiable;
    private String name;
    private String provider;
    private String version;
    private String location;
    private String description;
    private String type;



    public aggregator_p2_IRepository(
        boolean modifiable,        String name,        String provider,        String version,        String location,        String description,        String type    ) {
        super(
        );
        this.modifiable = modifiable;
        this.name = name;
        this.provider = provider;
        this.version = version;
        this.location = location;
        this.description = description;
        this.type = type;
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
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
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


}