





import java.util.List;
import java.util.ArrayList;

public class aggregator_Category extends MappedUnit {

    private String labelOverride;





    private aggregator_MappedRepository aggregator_mappedrepository;


    public aggregator_Category(
        String labelOverride    ) {
        super(
        );
        this.labelOverride = labelOverride;
    }


    public String getLabeloverride() {
        return labelOverride;
    }

    public void setLabeloverride(String labelOverride) {
        this.labelOverride = labelOverride;
    }

    public aggregator_MappedRepository getAggregator_mappedrepository() {
        return aggregator_mappedrepository;
    }

    public void setAggregator_mappedrepository(aggregator_MappedRepository aggregator_mappedrepository) {
        this.aggregator_mappedrepository = aggregator_mappedrepository;
    }

}