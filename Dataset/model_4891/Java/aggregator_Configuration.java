





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String architecture;
    private String windowSystem;
    private String operatingSystem;



    public aggregator_Configuration(
        String architecture,        String windowSystem,        String operatingSystem    ) {
        super(
        );
        this.architecture = architecture;
        this.windowSystem = windowSystem;
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
    public String getOperatingsystem() {
        return operatingSystem;
    }

    public void setOperatingsystem(String operatingSystem) {
        this.operatingSystem = operatingSystem;
    }


}