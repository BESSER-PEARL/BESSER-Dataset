





import java.util.List;
import java.util.ArrayList;

public class aggregator_Contribution extends EnabledStatusProvider, IdentificationProvider, InfosProvider, DescriptionProvider, StatusProvider {

    private String label;





    private aggregator_ValidationSet aggregator_validationset;


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

    public aggregator_ValidationSet getAggregator_validationset() {
        return aggregator_validationset;
    }

    public void setAggregator_validationset(aggregator_ValidationSet aggregator_validationset) {
        this.aggregator_validationset = aggregator_validationset;
    }

}