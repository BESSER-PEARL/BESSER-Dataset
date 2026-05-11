





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_Drone extends NamedElement {






    private dronesStructure_Scenario dronesstructure_scenario;




    private dronesStructure_DroneType dronesstructure_dronetype;


    public dronesStructure_Drone(
    ) {
        super(
        );
    }



    public dronesStructure_Scenario getDronesstructure_scenario() {
        return dronesstructure_scenario;
    }

    public void setDronesstructure_scenario(dronesStructure_Scenario dronesstructure_scenario) {
        this.dronesstructure_scenario = dronesstructure_scenario;
    }
    public dronesStructure_DroneType getDronesstructure_dronetype() {
        return dronesstructure_dronetype;
    }

    public void setDronesstructure_dronetype(dronesStructure_DroneType dronesstructure_dronetype) {
        this.dronesstructure_dronetype = dronesstructure_dronetype;
    }

}