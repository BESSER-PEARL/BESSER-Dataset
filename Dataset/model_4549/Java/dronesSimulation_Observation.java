





import java.util.List;
import java.util.ArrayList;

public class dronesSimulation_Observation  {

    private String time;
    private String id;





    private dronesSimulation_DroneInstance dronessimulation_droneinstance;


    public dronesSimulation_Observation(
        String time,        String id    ) {
        this.time = time;
        this.id = id;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dronesSimulation_DroneInstance getDronessimulation_droneinstance() {
        return dronessimulation_droneinstance;
    }

    public void setDronessimulation_droneinstance(dronesSimulation_DroneInstance dronessimulation_droneinstance) {
        this.dronessimulation_droneinstance = dronessimulation_droneinstance;
    }

}