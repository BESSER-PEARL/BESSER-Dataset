





import java.util.List;
import java.util.ArrayList;

public class aggregator_Configuration extends EnabledStatusProvider {

    private String architecture;
    private String operatingSystem;
    private String windowSystem;



    public aggregator_Configuration(
        String architecture,        String operatingSystem,        String windowSystem    ) {
        super(
        );
        this.architecture = architecture;
        this.operatingSystem = operatingSystem;
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
    public String getWindowsystem() {
        return windowSystem;
    }

    public void setWindowsystem(String windowSystem) {
        this.windowSystem = windowSystem;
    }


}