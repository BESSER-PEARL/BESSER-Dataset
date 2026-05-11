





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String windowSystem;
    private String architecture;
    private String operatingSystem;





    private aggregator_Aggregator aggregator_aggregator;


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

    public aggregator_Aggregator getAggregator_aggregator() {
        return aggregator_aggregator;
    }

    public void setAggregator_aggregator(aggregator_Aggregator aggregator_aggregator) {
        this.aggregator_aggregator = aggregator_aggregator;
    }

}