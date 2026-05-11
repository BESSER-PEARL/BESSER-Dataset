





import java.util.List;
import java.util.ArrayList;

public class aggregator_MetadataRepositoryReference extends StatusProvider, InfosProvider, EnabledStatusProvider {

    private String location;
    private String nature;





    private aggregator_ValidationSet aggregator_validationset;


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

    public aggregator_ValidationSet getAggregator_validationset() {
        return aggregator_validationset;
    }

    public void setAggregator_validationset(aggregator_ValidationSet aggregator_validationset) {
        this.aggregator_validationset = aggregator_validationset;
    }

}