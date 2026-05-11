





import java.util.List;
import java.util.ArrayList;

public class drone_Capability extends NamedElement {






    private drone_Robot drone_robot;




    private drone_Equipment drone_equipment;


    public drone_Capability(
    ) {
        super(
        );
    }



    public drone_Robot getDrone_robot() {
        return drone_robot;
    }

    public void setDrone_robot(drone_Robot drone_robot) {
        this.drone_robot = drone_robot;
    }
    public drone_Equipment getDrone_equipment() {
        return drone_equipment;
    }

    public void setDrone_equipment(drone_Equipment drone_equipment) {
        this.drone_equipment = drone_equipment;
    }

}