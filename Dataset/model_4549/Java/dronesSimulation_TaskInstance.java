





import java.util.List;
import java.util.ArrayList;

public class dronesSimulation_TaskInstance  {

    private String state;





    private dronesSimulation_DronesSimulation dronessimulation_dronessimulation;


    public dronesSimulation_TaskInstance(
        String state    ) {
        this.state = state;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public dronesSimulation_DronesSimulation getDronessimulation_dronessimulation() {
        return dronessimulation_dronessimulation;
    }

    public void setDronessimulation_dronessimulation(dronesSimulation_DronesSimulation dronessimulation_dronessimulation) {
        this.dronessimulation_dronessimulation = dronessimulation_dronessimulation;
    }

}