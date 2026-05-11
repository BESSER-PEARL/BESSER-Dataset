





import java.util.List;
import java.util.ArrayList;

public class aggregator_MetadataRepositoryReference extends StatusProvider, EnabledStatusProvider, InfosProvider {

    private String location;
    private String nature;



    public aggregator_MetadataRepositoryReference(
        String location,        String nature    ) {
        super(
        );
        this.location = location;
        this.nature = nature;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getNature() {
        return nature;
    }

    public void setNature(String nature) {
        this.nature = nature;
    }


}