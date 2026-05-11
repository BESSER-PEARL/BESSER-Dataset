





import java.util.List;
import java.util.ArrayList;

public class aggregator_MetadataRepositoryReference extends EnabledStatusProvider, InfosProvider, StatusProvider {

    private String nature;
    private String location;





    private aggregator_Aggregator aggregator_aggregator;


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

    public aggregator_Aggregator getAggregator_aggregator() {
        return aggregator_aggregator;
    }

    public void setAggregator_aggregator(aggregator_Aggregator aggregator_aggregator) {
        this.aggregator_aggregator = aggregator_aggregator;
    }

}