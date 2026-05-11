





import java.util.List;
import java.util.ArrayList;

public class drone_Device extends NamedElement {






    private List<drone_Action> drone_actions;




    private List<drone_Property> drone_propertys;




    private drone_Drone drone_drone;


    public drone_Device(
    ) {
        super(
        );
        this.drone_actions = new ArrayList<>();
        this.drone_propertys = new ArrayList<>();
    }

    public drone_Device(
        ArrayList<drone_Action> drone_actions,        ArrayList<drone_Property> drone_propertys    ) {
        this.drone_actions = drone_actions;
        this.drone_propertys = drone_propertys;
    }


    public List<drone_Action> getDrone_actions() {
        return drone_actions;
    }

    public void addDrone_action(Drone_action drone_action) {
        this.drone_actions.add(drone_action);
    }
    public List<drone_Property> getDrone_propertys() {
        return drone_propertys;
    }

    public void addDrone_property(Drone_property drone_property) {
        this.drone_propertys.add(drone_property);
    }
    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}