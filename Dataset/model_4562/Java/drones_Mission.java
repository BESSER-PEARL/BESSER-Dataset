





import java.util.List;
import java.util.ArrayList;

public class drones_Mission extends NamedElement {






    private List<drones_FieldObject> drones_fieldobjects;




    private List<drones_Drone> drones_drones;




    private List<drones_Action> drones_actions;


    public drones_Mission(
    ) {
        super(
        );
        this.drones_fieldobjects = new ArrayList<>();
        this.drones_drones = new ArrayList<>();
        this.drones_actions = new ArrayList<>();
    }

    public drones_Mission(
        ArrayList<drones_FieldObject> drones_fieldobjects,        ArrayList<drones_Drone> drones_drones,        ArrayList<drones_Action> drones_actions    ) {
        this.drones_fieldobjects = drones_fieldobjects;
        this.drones_drones = drones_drones;
        this.drones_actions = drones_actions;
    }


    public List<drones_FieldObject> getDrones_fieldobjects() {
        return drones_fieldobjects;
    }

    public void addDrones_fieldobject(Drones_fieldobject drones_fieldobject) {
        this.drones_fieldobjects.add(drones_fieldobject);
    }
    public List<drones_Drone> getDrones_drones() {
        return drones_drones;
    }

    public void addDrones_drone(Drones_drone drones_drone) {
        this.drones_drones.add(drones_drone);
    }
    public List<drones_Action> getDrones_actions() {
        return drones_actions;
    }

    public void addDrones_action(Drones_action drones_action) {
        this.drones_actions.add(drones_action);
    }

}