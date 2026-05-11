





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String operatingSystem;
    private String windowSystem;
    private String architecture;



    public aggregator_Configuration(
        String operatingSystem,        String windowSystem,        String architecture    ) {
        super(
        );
        this.operatingSystem = operatingSystem;
        this.windowSystem = windowSystem;
        this.architecture = architecture;
    }


    public String getOperatingsystem() {
        return operatingSystem;
    }

    public void setOperatingsystem(String operatingSystem) {
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


}