





import java.util.List;
import java.util.ArrayList;

public class dronesSimulation_DroneObservation extends Observation {






    private dronesSimulation_Position dronessimulation_position;




    private dronesSimulation_Drone dronessimulation_drone;


    public dronesSimulation_DroneObservation(
    ) {
        super(
        );
    }



    public dronesSimulation_Position getDronessimulation_position() {
        return dronessimulation_position;
    }

    public void setDronessimulation_position(dronesSimulation_Position dronessimulation_position) {
        this.dronessimulation_position = dronessimulation_position;
    }
    public dronesSimulation_Drone getDronessimulation_drone() {
        return dronessimulation_drone;
    }

    public void setDronessimulation_drone(dronesSimulation_Drone dronessimulation_drone) {
        this.dronessimulation_drone = dronessimulation_drone;
    }

}