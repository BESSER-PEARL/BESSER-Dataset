





import java.util.List;
import java.util.ArrayList;

public class platoon_Route  {

    private String name;





    private platoon_World platoon_world;




    private platoon_LeadingVehicle platoon_leadingvehicle;


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

    public platoon_World getPlatoon_world() {
        return platoon_world;
    }

    public void setPlatoon_world(platoon_World platoon_world) {
        this.platoon_world = platoon_world;
    }
    public platoon_LeadingVehicle getPlatoon_leadingvehicle() {
        return platoon_leadingvehicle;
    }

    public void setPlatoon_leadingvehicle(platoon_LeadingVehicle platoon_leadingvehicle) {
        this.platoon_leadingvehicle = platoon_leadingvehicle;
    }

}