





import java.util.List;
import java.util.ArrayList;

public class behaviour_Behaviour extends NamedElement {

    private String crs;





    private List<behaviour_Drone> behaviour_drones;


    public behaviour_Behaviour(
        String crs    ) {
        super(
        );
        this.crs = crs;
        this.behaviour_drones = new ArrayList<>();
    }

    public behaviour_Behaviour(
        String crs        ArrayList<behaviour_Drone> behaviour_drones    ) {
        this.crs = crs;
        this.behaviour_drones = behaviour_drones;
    }

    public String getCrs() {
        return crs;
    }

    public void setCrs(String crs) {
        this.crs = crs;
    }

    public List<behaviour_Drone> getBehaviour_drones() {
        return behaviour_drones;
    }

    public void addBehaviour_drone(Behaviour_drone behaviour_drone) {
        this.behaviour_drones.add(behaviour_drone);
    }

}