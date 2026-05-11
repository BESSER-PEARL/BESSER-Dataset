





import java.util.List;
import java.util.ArrayList;

public class drone_ROSDriver extends NamedElement {

    private String version;
    private String url;





    private drone_Drone drone_drone;


    public drone_ROSDriver(
        String version,        String url    ) {
        super(
        );
        this.version = version;
        this.url = url;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}