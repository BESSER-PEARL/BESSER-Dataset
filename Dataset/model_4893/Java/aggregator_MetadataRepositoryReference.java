





import java.util.List;
import java.util.ArrayList;

public class aggregator_MetadataRepositoryReference extends InfosProvider, EnabledStatusProvider, StatusProvider {

    private String nature;
    private String location;



    public aggregator_MetadataRepositoryReference(
        String nature,        String location    ) {
        super(
        );
        this.nature = nature;
        this.location = location;
    }


    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}