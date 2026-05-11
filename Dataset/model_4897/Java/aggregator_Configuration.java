





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String operatingSystem;
    private String architecture;
    private String windowSystem;





    private aggregator_Aggregation aggregator_aggregation;


    public aggregator_Configuration(
        String operatingSystem,        String architecture,        String windowSystem    ) {
        super(
        );
        this.operatingSystem = operatingSystem;
        this.architecture = architecture;
        this.windowSystem = windowSystem;
    }


    public String getOperatingsystem() {
        return operatingSystem;
    }

    public void setOperatingsystem(String operatingSystem) {
        this.operatingSystem = operatingSystem;
    }
    public String getArchitecture() {
        return architecture;
    }

    public void setArchitecture(String architecture) {
        this.architecture = architecture;
    }
    public String getWindowsystem() {
        return windowSystem;
    }

    public void setWindowsystem(String windowSystem) {
        this.windowSystem = windowSystem;
    }

    public aggregator_Aggregation getAggregator_aggregation() {
        return aggregator_aggregation;
    }

    public void setAggregator_aggregation(aggregator_Aggregation aggregator_aggregation) {
        this.aggregator_aggregation = aggregator_aggregation;
    }

}