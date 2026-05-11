





import java.util.List;
import java.util.ArrayList;

public class platoon_Route  {

    private String name;





    private platoon_LeadVehicle platoon_leadvehicle;




    private platoon_World platoon_world;


    public platoon_Route(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public platoon_LeadVehicle getPlatoon_leadvehicle() {
        return platoon_leadvehicle;
    }

    public void setPlatoon_leadvehicle(platoon_LeadVehicle platoon_leadvehicle) {
        this.platoon_leadvehicle = platoon_leadvehicle;
    }
    public platoon_World getPlatoon_world() {
        return platoon_world;
    }

    public void setPlatoon_world(platoon_World platoon_world) {
        this.platoon_world = platoon_world;
    }

}