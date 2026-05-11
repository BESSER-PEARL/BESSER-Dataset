





import java.util.List;
import java.util.ArrayList;

public class dronesSimulation_DroneInstance  {

    private String state;
    private float currentBattery;





    private dronesSimulation_DronesSimulation dronessimulation_dronessimulation;


    public dronesSimulation_DroneInstance(
        String state,        float currentBattery    ) {
        this.state = state;
        this.currentBattery = currentBattery;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public float getCurrentbattery() {
        return currentBattery;
    }

    public void setCurrentbattery(float currentBattery) {
        this.currentBattery = currentBattery;
    }

    public dronesSimulation_DronesSimulation getDronessimulation_dronessimulation() {
        return dronessimulation_dronessimulation;
    }

    public void setDronessimulation_dronessimulation(dronesSimulation_DronesSimulation dronessimulation_dronessimulation) {
        this.dronessimulation_dronessimulation = dronessimulation_dronessimulation;
    }

}