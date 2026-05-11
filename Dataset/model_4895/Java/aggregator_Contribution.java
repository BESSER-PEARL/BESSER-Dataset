





import java.util.List;
import java.util.ArrayList;

public class aggregator_Contribution extends InfosProvider, IdentificationProvider, StatusProvider, DescriptionProvider, EnabledStatusProvider {

    private String label;





    private aggregator_ValidationSet aggregator_validationset;




    private List<aggregator_MappedRepository> aggregator_mappedrepositorys;


    public aggregator_Contribution(
        String label    ) {
        super(
        );
        this.label = label;
        this.aggregator_mappedrepositorys = new ArrayList<>();
    }

    public aggregator_Contribution(
        String label        ArrayList<aggregator_MappedRepository> aggregator_mappedrepositorys    ) {
        this.label = label;
        this.aggregator_mappedrepositorys = aggregator_mappedrepositorys;
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
    public List<aggregator_MappedRepository> getAggregator_mappedrepositorys() {
        return aggregator_mappedrepositorys;
    }

    public void addAggregator_mappedrepository(Aggregator_mappedrepository aggregator_mappedrepository) {
        this.aggregator_mappedrepositorys.add(aggregator_mappedrepository);
    }

}