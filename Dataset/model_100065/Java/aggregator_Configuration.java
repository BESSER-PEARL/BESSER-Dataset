





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String windowSystem;
    private String architecture;
    private String operatingSystem;





    private aggregator_Aggregation aggregator_aggregation;


    public aggregator_Configuration(
        String windowSystem,        String architecture,        String operatingSystem    ) {
        super(
        );
        this.windowSystem = windowSystem;
        this.architecture = architecture;
        this.operatingSystem = operatingSystem;
    }


    public String getWindowsystem() {
        return windowSystem;
    }

    public void setWindowsystem(String windowSystem) {
        this.windowSystem = windowSystem;
    }
    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
    }
    public String getOperatingsystem() {
        return operatingSystem;
    }

    public void setOperatingsystem(String operatingSystem) {
        this.operatingSystem = operatingSystem;
    }

    public aggregator_Aggregation getAggregator_aggregation() {
        return aggregator_aggregation;
    }

    public void setAggregator_aggregation(aggregator_Aggregation aggregator_aggregation) {
        this.aggregator_aggregation = aggregator_aggregation;
    }

}