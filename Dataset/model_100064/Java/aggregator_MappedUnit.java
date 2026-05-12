





import java.util.List;
import java.util.ArrayList;

public class aggregator_MappedUnit extends EnabledStatusProvider, InstallableUnitRequest {






    private List<aggregator_Configuration> aggregator_configurations;


    public aggregator_MappedUnit(
    ) {
        super(
        );
        this.aggregator_configurations = new ArrayList<>();
    }

    public aggregator_MappedUnit(
        ArrayList<aggregator_Configuration> aggregator_configurations    ) {
        this.aggregator_configurations = aggregator_configurations;
    }


    public List<aggregator_Configuration> getAggregator_configurations() {
        return aggregator_configurations;
    }

    public void addAggregator_configuration(Aggregator_configuration aggregator_configuration) {
        this.aggregator_configurations.add(aggregator_configuration);
    }

}