





import java.util.List;
import java.util.ArrayList;

public class aggregator_ValidationSet extends StatusProvider, InfosProvider, DescriptionProvider, EnabledStatusProvider, IdentificationProvider {

    private boolean abstract;
    private String label;
    private boolean extension;





    private aggregator_ValidationSet aggregator_validationset;




    private aggregator_Aggregation aggregator_aggregation;




    private List<aggregator_Contribution> aggregator_contributions;


    public aggregator_ValidationSet(
        boolean abstract,        String label,        boolean extension    ) {
        super(
        );
        this.abstract = abstract;
        this.label = label;
        this.extension = extension;
        this.aggregator_contributions = new ArrayList<>();
    }

    public aggregator_ValidationSet(
        boolean abstract,        String label,        boolean extension        ArrayList<aggregator_Contribution> aggregator_contributions    ) {
        this.abstract = abstract;
        this.label = label;
        this.extension = extension;
        this.aggregator_contributions = aggregator_contributions;
    }

    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getExtension() {
        return extension;
    }

    public void setExtension(boolean extension) {
        this.extension = extension;
    }

    public aggregator_ValidationSet getAggregator_validationset() {
        return aggregator_validationset;
    }

    public void setAggregator_validationset(aggregator_ValidationSet aggregator_validationset) {
        this.aggregator_validationset = aggregator_validationset;
    }
    public aggregator_Aggregation getAggregator_aggregation() {
        return aggregator_aggregation;
    }

    public void setAggregator_aggregation(aggregator_Aggregation aggregator_aggregation) {
        this.aggregator_aggregation = aggregator_aggregation;
    }
    public List<aggregator_Contribution> getAggregator_contributions() {
        return aggregator_contributions;
    }

    public void addAggregator_contribution(Aggregator_contribution aggregator_contribution) {
        this.aggregator_contributions.add(aggregator_contribution);
    }

}