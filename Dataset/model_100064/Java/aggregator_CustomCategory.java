





import java.util.List;
import java.util.ArrayList;

public class aggregator_CustomCategory extends InfosProvider, StatusProvider {

    private String identifier;
    private String label;
    private String description;





    private aggregator_Aggregator aggregator_aggregator;


    public aggregator_CustomCategory(
        String identifier,        String label,        String description    ) {
        super(
        );
        this.identifier = identifier;
        this.label = label;
        this.description = description;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public aggregator_Aggregator getAggregator_aggregator() {
        return aggregator_aggregator;
    }

    public void setAggregator_aggregator(aggregator_Aggregator aggregator_aggregator) {
        this.aggregator_aggregator = aggregator_aggregator;
    }

}