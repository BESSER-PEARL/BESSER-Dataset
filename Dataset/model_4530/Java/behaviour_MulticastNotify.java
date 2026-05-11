





import java.util.List;
import java.util.ArrayList;

public class behaviour_MulticastNotify extends Notify {






    private List<behaviour_Drone> behaviour_drones;


    public behaviour_MulticastNotify(
    ) {
        super(
        );
        this.behaviour_drones = new ArrayList<>();
    }

    public behaviour_MulticastNotify(
        ArrayList<behaviour_Drone> behaviour_drones    ) {
        this.behaviour_drones = behaviour_drones;
    }


    public List<behaviour_Drone> getBehaviour_drones() {
        return behaviour_drones;
    }

    public void addBehaviour_drone(Behaviour_drone behaviour_drone) {
        this.behaviour_drones.add(behaviour_drone);
    }

}