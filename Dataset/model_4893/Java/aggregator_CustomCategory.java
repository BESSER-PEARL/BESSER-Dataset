





import java.util.List;
import java.util.ArrayList;

public class aggregator_CustomCategory extends InfosProvider, StatusProvider {

    private String identifier;
    private String label;
    private String description;





    private List<aggregator_Feature> aggregator_features;




    private aggregator_Feature aggregator_feature;


    public aggregator_CustomCategory(
        String identifier,        String label,        String description    ) {
        super(
        );
        this.identifier = identifier;
        this.label = label;
        this.description = description;
        this.aggregator_features = new ArrayList<>();
    }

    public aggregator_CustomCategory(
        String identifier,        String label,        String description        ArrayList<aggregator_Feature> aggregator_features    ) {
        this.identifier = identifier;
        this.label = label;
        this.description = description;
        this.aggregator_features = aggregator_features;
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

    public List<aggregator_Feature> getAggregator_features() {
        return aggregator_features;
    }

    public void addAggregator_feature(Aggregator_feature aggregator_feature) {
        this.aggregator_features.add(aggregator_feature);
    }
    public aggregator_Feature getAggregator_feature() {
        return aggregator_feature;
    }

    public void setAggregator_feature(aggregator_Feature aggregator_feature) {
        this.aggregator_feature = aggregator_feature;
    }

}