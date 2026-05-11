





import java.util.List;
import java.util.ArrayList;

public class drone_Robot extends NamedElement {






    private drone_Mission drone_mission;




    private List<drone_Equipment> drone_equipments;


    public drone_Robot(
    ) {
        super(
        );
        this.drone_equipments = new ArrayList<>();
    }

    public drone_Robot(
        ArrayList<drone_Equipment> drone_equipments    ) {
        this.drone_equipments = drone_equipments;
    }


    public drone_Mission getDrone_mission() {
        return drone_mission;
    }

    public void setDrone_mission(drone_Mission drone_mission) {
        this.drone_mission = drone_mission;
    }
    public List<drone_Equipment> getDrone_equipments() {
        return drone_equipments;
    }

    public void addDrone_equipment(Drone_equipment drone_equipment) {
        this.drone_equipments.add(drone_equipment);
    }

}