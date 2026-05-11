





import java.util.List;
import java.util.ArrayList;

public class drone_Battery  {






    private List<drone_Property> drone_propertys;




    private drone_Robot drone_robot;


    public drone_Battery(
    ) {
        this.drone_propertys = new ArrayList<>();
    }

    public drone_Battery(
        ArrayList<drone_Property> drone_propertys    ) {
        this.drone_propertys = drone_propertys;
    }


    public List<drone_Property> getDrone_propertys() {
        return drone_propertys;
    }

    public void addDrone_property(Drone_property drone_property) {
        this.drone_propertys.add(drone_property);
    }
    public drone_Robot getDrone_robot() {
        return drone_robot;
    }

    public void setDrone_robot(drone_Robot drone_robot) {
        this.drone_robot = drone_robot;
    }

}