





import java.util.List;
import java.util.ArrayList;

public class aggregator_Contribution extends EnabledStatusProvider, DescriptionProvider, InfosProvider, StatusProvider {

    private String label;





    private aggregator_Aggregator aggregator_aggregator;


    public aggregator_Contribution(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public aggregator_Aggregator getAggregator_aggregator() {
        return aggregator_aggregator;
    }

    public void setAggregator_aggregator(aggregator_Aggregator aggregator_aggregator) {
        this.aggregator_aggregator = aggregator_aggregator;
    }

}